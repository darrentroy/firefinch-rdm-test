import collections

import jinja2
from jinja2.environment import TemplateStream

from rdm.extensions import RdmExtension, dynamic_class_loader


def invert_dependencies(objects, id_key, dependencies_key):
    # TODO: add docstring
    inverted = collections.defaultdict(lambda: set())
    for o in objects:
        for d in o[dependencies_key]:
            inverted[d].add(o[id_key])
    inverted_as_list = list(inverted.items())
    return sorted(inverted_as_list, key=lambda i: i[0].split('-'))


def join_to(foreign_keys, table, primary_key='id'):
    '''
    Given a set of ids for an object, and a list of the objects these ids refer
    to, select out the objects by joining using the specified primary key
    (which defaults to 'id').
    '''
    joined = []
    for foreign_key in foreign_keys:
        selected_row = None
        for row in table:
            if row[primary_key] == foreign_key:
                selected_row = row
                break
        joined.append(selected_row)
    return joined


def render_template_to_file(template_filename, context, output_file, loaders=None):
    generator = generate_template_output(template_filename, context, loaders=loaders)
    TemplateStream(generator).dump(output_file)


def render_template_to_string(template_filename, context, loaders=None):
    return ''.join(generate_template_output(template_filename, context, loaders=loaders))


def generate_template_output(template_filename, context, loaders=None):
    environment = _create_jinja_environment(context, loaders)
    template = environment.get_template(template_filename)
    source_line_list = _generate_source_line_list(template, context)
    return _generate_output_lines(environment, source_line_list)


def _create_jinja_environment(context, loaders=None):
    extensions = _create_extension_list(context)
    loader = _create_loader(loaders)
    environment = jinja2.Environment(
        cache_size=0,
        undefined=jinja2.StrictUndefined,
        loader=loader,
        extensions=extensions,
    )
    environment.filters['invert_dependencies'] = invert_dependencies
    environment.filters['join_to'] = join_to
    return environment


def _create_extension_list(context):
    system_dict = context.get('system', {})
    extension_descriptor_list = system_dict.get('extension_load_list', [])
    return dynamic_class_loader(extension_descriptor_list)


def _create_loader(loaders=None):
    if loaders is None:
        loaders = [
            jinja2.FileSystemLoader('.'),
            jinja2.PackageLoader('rdm', '.'),
        ]

    return jinja2.ChoiceLoader(loaders)


def _generate_source_line_list(template, context):
    generator = template.generate(**context)
    for filter in [split_into_lines, append_newlines]:
        generator = (x for x in filter(generator))
    return [line for line in generator]


def _generate_output_lines(environment, source_line_list):
    output_generator = (line for line in source_line_list)
    post_process_filters = RdmExtension.post_processing_filter_list(environment)
    for post_process_filter in post_process_filters:
        output_generator = (x for x in post_process_filter(output_generator))
    return output_generator


def split_into_lines(generator):
    for item in generator:
        for line in item.split('\n'):
            yield line


def append_newlines(generator):
    for item in generator:
        yield item + '\n'
