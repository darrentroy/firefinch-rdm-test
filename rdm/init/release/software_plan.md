---
category: PLAN
id: PLAN-001
revision: 1
title: Software Plan
company_name: Company
---

# Purpose

This document outlines how software developers should develop, maintain, and configure Project.

It includes the software development and the software maintenance plan.

All software life cycle process are described in this document.

# Software Development Life Cycle Model

Project will be developed using an evolutionary software development life cycle model.

The "evolutionary" strategy develops the software system using a sequence of builds.  Customer needs and software system requirements are partially defined up front, then are refined in each succeeding build.

# Development Process

## Development Planning Activity


System requirements are recorded in Greenlight Guru.  Each system requirement requires a unique identifier so that we can trace its related software requirements back to it.


## Requirements Analysis Activity

Software requirements are recorded in the form of Github Issues that have been tagged with the `requirement` label.  See Appendix A for a list of the different types of requirements, and some guidance for how to write them.

To the extent possible, software requirements should be enumerated at the start of the project.  As new requirements are recognized during development, new Github Issues should be created.  If an existing requirement becomes irrelevant, it should be tagged with the `obsolete` label.


an optional list of software requirement ids, and a type, according to the following format:



Any risk control measures that will be implemented in software should be included as requirements.


When requirements are added or are changed, the developer must:

1. Re-evaluate the medical device risk analysis and update it as appropriate
2. Ensure that existing requirements, including system requirements, are re-evaluated and updated as appropriate

3. Verify that the software requirements implement the system requirements, and that the software requirements are properly linked to the system requirements
4. Verify that the software requirements implement all risk controls

5. Verify that the software requirements don't contradict each other
6. Verify that the software requirements are unambiguous
7. Verify that the software requirements are stated in terms that permit establishment of test criteria and performance of tests to determine whether the test criteria have been met


## Architectural Design Activity

After the initial set of requirements have been gathered and verified, develop and document a software system architecture in a file called `DESIGN.md` in the root of the project's git repository.  The architecture does not need to be fully thought out up-front, since code construction often helps guide architectural decisions.  As appropriate, prefer block diagrams and flow charts to textual descriptions, and include them inline in the `DESIGN.md` file.

The software system architecture should describe whether, and how, it is divided into smaller software items, and it should show the software and hardware interfaces between the software items and external software components.

## Detailed Design Activity


## Unit Implementation and Verification Activity

All code will be stored within a Git repository.

The master branch of the git repository should contain the most up-to-date, tested version of the code.

New development should usually occur within separate branches.  These branches can be merged into the master branch after the changes in them have been verified.

If, for some reason, it is necessary to commit new work directly on the master branch, justify why this was necessary in the git commit message.


## Integration and Integration Testing Activity
## System Testing Activity


## Software Release Activity

When a new version of the software is released, the git commit corresponding to the state of the code should be tagged with the version number.

# Maintenance Process

# Risk Management Process

# Configuration Management Process

# Problem Resolution Process

# Traceability

# Documents

1. Software Development Plan (this document)
2. Risk Management File

# References

1. ISO62304:2006

# Appendix A

## Requirements File

Writing software requirements is an art and a science; one must find balance between precision and usefulness.

Software requirements are often categorized as one of the following types:

a. Functional and capability requirements
  - performance (e.g., purpose of software, timing requirements),
  - physical characteristics (e.g., code language, platform, operating system),
  - computing environment (e.g., hardware, memory size, processing unit, time zone, network infrastructure) under which the software is to perform, and
  - need for compatibility with upgrades or multiple SOUP or other device versions.

b. Sofware system inputs and outputs
  - data characteristics (e.g., numerical, alpha-numeric, format) ranges,
  - limits, and
  - defaults.

c. Interfaces between the software system and other systems

d. Software-driven alarms, warnings, and operator messages

e. Security requirements
  - those related to the compromise of sensitive information,
  - authentication,
  - authorization,
  - audit trail, and
  - communication integrity.

f. Usability engineering requirements that are sensitive to human errors and training
  - support for manual operations,
  - human-equipment interactions,
  - constraints on personnel, and
  - areas needing concentrated human attention.

g. Data definitions and database requirements

h. Installation and acceptance requirements of the delivered medical device software at the operation and maintenance site or sites

i. Requirements related to methods of operation and maintenance

j. User documentation to be developed

k. User maintenance requirements

l. Regulatory requirements


m. Risk control measures