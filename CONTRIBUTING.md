# RISC-V Board and OS Support Matrix Contribution Guide

[English](./CONTRIBUTING.md) / [中文](./CONTRIBUTING_zh.md)

## Overview

This document is intended for developers who wish to contribute to the RuyiSDK Support Matrix project. The project uses GitHub Pull Request mechanisms for collaboration.

Before contributing, you need to:
1. Have a [GitHub account](https://github.com/signup)
2. Be familiar with basic Git operations and GitHub workflow
3. Understand the project data structure specifications (see below)

If you are not familiar with GitHub and Git, we recommend first reviewing the [GitHub Quick Start Guide](https://docs.github.com/en/get-started/quickstart/hello-world).

This document contains general contribution information. Different parts of the project also have more specific instructions:
- [Boards (example VisionFive2)](./VisionFive2/README.md): List and description of supported boards.
- [OS (example VisionFive2/Alpine)](./VisionFive2/Alpine/README.md): Supported operating system variants.
- [Repository metadata parsing, SVG generation, and image source synchronization tools](./assets/): When adding new boards or operating systems, [metadata.yml](./assets/metadata.yml) may need to be updated.
- [Metadata parsing plugins for image source synchronization](./assets/src/ruyi_index_updator/upload_plugin): For some metadata where sys_ver doesn't follow semver standards, adjustments might be made via plugins.

Project structure hierarchy:

```plaintext
support-matrix
 |
 |--- Board
    |
    |--- README.md # Board documentation, containing basic board metadata
    |
    |--- Systems
    |    |
    |    |--- README.md # Main variant documentation, containing basic system metadata
    |    |
    |    |--- README_variant.md # Other variant documentation, containing variant metadata
    |    |
    |    |--- README(_variant)_lang.yaml # Translations in different languages, **does NOT contain metadata!**
    |
    |--- others.yml # Metadata for systems without documentation
```

## Code of Conduct

Please be respectful and considerate of others when contributing to RuyiSDK. We aim to foster an open and welcoming environment for all contributors.

Please follow [the RuyiSDK Code of Conduct](https://ruyisdk.org/en/code_of_conduct).

## Quick Start

### Creating a PR Workflow

1. Fork and clone the repository locally
2. Create a branch and update/add board, test reports
3. Commit your changes, ensuring commit messages are clear and understandable, and contains a `Signed-off-by` tag (see below)
    * It's better to squash your commits before pushing.
4. Push your commits to your forked repository and create a Pull Request

> [!Note]
> If the metadata cannot be parsed or the document content does not meet requirements, your pull request may require modifications.

### Developer's Certificate of Origin (DCO)

We require that all contributions to RuyiSDK are covered under the [Developer's Certificate of Origin (DCO)](https://developercertificate.org/). The DCO is a lightweight way for contributors to certify that they wrote or otherwise have the right to submit the code they are contributing.

#### What is the DCO?

The DCO is a declaration that you make when you sign-off a commit, simple
enough that the original text is fully reproduced below.

```
Developer Certificate of Origin
Version 1.1

Copyright (C) 2004, 2006 The Linux Foundation and its contributors.

Everyone is permitted to copy and distribute verbatim copies of this
license document, but changing it is not allowed.


Developer's Certificate of Origin 1.1

By making a contribution to this project, I certify that:

(a) The contribution was created in whole or in part by me and I
    have the right to submit it under the open source license
    indicated in the file; or

(b) The contribution is based upon previous work that, to the best
    of my knowledge, is covered under an appropriate open source
    license and I have the right under that license to submit that
    work with modifications, whether created in whole or in part
    by me, under the same open source license (unless I am
    permitted to submit under a different license), as indicated
    in the file; or

(c) The contribution was provided directly to me by some other
    person who certified (a), (b) or (c) and I have not modified
    it.

(d) I understand and agree that this project and the contribution
    are public and that a record of the contribution (including all
    personal information I submit with it, including my sign-off) is
    maintained indefinitely and may be redistributed consistent with
    this project or the open source license(s) involved.
```

#### How to Sign-Off Commits

You need to add a `Signed-off-by` line to each commit message, which certifies that you agree with the DCO:

```
Signed-off-by: Your Name <your.email@example.com>
```

You can add this automatically by using the `-s` or `--signoff` flag when committing:

```
git commit -s -m "Your commit message"
```

Make sure that the name and email in the signature matches your Git configuration. You can set your Git name and email with:

```
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

#### DCO enforcement in CI

All pull requests go through an automated DCO check in our continuous integration (CI) pipeline. This check verifies that all commits in your pull request have a proper DCO sign-off. If any commits are missing the sign-off, the CI check will fail, and your pull request cannot be merged until the issue is fixed.

## Data Structure Specifications

### Metadata Definitions

All documents must include a YAML metadata header, with fields defined as follows:

```yaml
# /Board/README.md
---
vendor: _     # Vendor identifier (lowercase letters + underscores)
product: _    # Full product name
cpu: _        # Processor model
cpu_core: _   # CPU core architecture
board_variant: [] # Board variant (optional, like 8g/16g version)
cpu_arch: [] # Supported CPU architectures (like xuantie-e902, armv8-a...)
# Supported CPU architectures are listed in assets/metadata.yml:arches
# If none of the above, add a new one in assets/metadata.yml:arches
---
```

Note that some boards currently lack the vendor field, which can be left empty. If you need to fill it in, please follow the RuyiSDK naming convention.

```yaml
# /Board/OS/README.md
sys: armbian          # System identifier (refer to assets/metadata.yml)
sys_ver: "24.05"        # System version (Should be the same as the one of the image, shouldn't add any extra part to match other format like semantic versioning. Prepend `v` is optional. *Notice: something like `24.05` would be seen as a number, so please add quotation if necessary*)
sys_var: minimal      # Variant identifier (optional)
status: basic         # Support status (none/wip/cft/cfh/cfi/partial/basic/good)
last_updated: 2024-03-01  # Last update date
---
```

Note that LTS versions of operating systems count as separate variants.

The LTS identifier exists in some sys_var fields as a variant for historical reasons, but the current convention is to place it in the sys_ver field.

Ideally, Ubuntu 24.04.1 in NeZha-D1s/Ubuntu/README_LTS.md should be written as:

```yaml
sys_ver: 24.04-LTS-SP1        # System version (Should be the same as the one of the image, shouldn't add any extra part to match other format like semantic versioning. Prepend `v` is optional.)
sys_var: LTS                  # Variant identifier (optional)
```

If there are any parts that are still unclear, please contact @wychlw.

### Status Enumeration Description

Refer to [README.md](./README.md) `Notes` part.

| Status Value | Description                                          |
|--------------|------------------------------------------------------|
| none         | No support for this OS/board combo, either from official or other sources |
| wip          | Official announcements say there will be/is support for this OS/board, but no image or other resources (e.g. source code) avaliable yet |
| cfi          | Official documentations claims there is support for this OS, but no OS image avaliable yet |
| cft          | An OS image is avaliable, need further verification on real hardware |
| cfh          | Official documentations/community forums show this OS is supported on this board, but failed to boot up |
| partial      | Partial functionality available                      |
| basic        | Can boot up and run                                  |
| good         | Supports GUI                                         |

## Documentation Writing Standards

### Test Report Requirements

Please refer to the following templates:

- [Report template for a single OS](./report-template/[board-name]/[os-name]/README.md)
- [Report template for board overview](./report-template/[board-name]/README.md)

### Internationalization (i18n)
- Main documentation should be written in English (README.md)
- Translation documents use the README_{lang}.md format (e.g. Chinese translation can use README_zh.md)
- Translation documents **do NOT contain** metadata headers
- Maintain correct hyperlinks between documents
- Use consistent terminology with other documents in the same language
