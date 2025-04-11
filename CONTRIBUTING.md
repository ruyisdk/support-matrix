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

## Quick Start

### Creating a PR Workflow

1. Fork and clone the repository locally
2. Create a branch and update/add board, test reports
3. Commit your changes, ensuring commit messages are clear and understandable (Better to squash your commits before pushing.)
4. Push your commits to your forked repository and create a Pull Request

> [!Note]
> If the metadata cannot be parsed or the document content does not meet requirements, your pull request may require modifications.

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

---

Notes:

Below are some fields that you may meet in the metadata header, but not listed above. These fields tend to play a specific role other tools to fill up some special demands.

```yaml
skip_sync: true/false # Whether to skip synchronization with RuyiSDK.
link: some_link # A link to the image source. Sometimes it's difficult to generate a link to the image source, so this field is used to provide a link directly.
symlink: [xxx, yyy] # A list which lets tools treat the current file as multiple files. Sometimes a report can cover multiple OS variants, so this field is used to provide a list of OS variants. Like, a image with or with out GUI, or a image with or without some special features.
```

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