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
3. Commit your changes, ensuring commit messages are clear and understandable
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
---
```

```yaml
# /Board/OS/README.md
sys: armbian          # System identifier (refer to assets/metadata.yml)
sys_ver: 24.05        # System version (preferably using semantic versioning)
sys_var: minimal      # Variant identifier (optional)
status: basic         # Support status (none/wip/cft/cfh/cfi/partial/basic/good)
last_updated: 2024-03-01  # Last update date
---
```

### Status Enumeration Description

Refer to [README.md](./README.md) `Notes` part.

| Status Value | Description                                          |
|--------------|------------------------------------------------------|
| good         | Supports GUI                                         |
| basic        | Can boot up and run                                  |
| cfh          | Official docs/forums show support, but failed to boot|
| cft          | Image available, needs hardware verification         |
| cfi          | Official docs claim support, but no image available  |
| wip          | Support announced, but no image or source available  |
| none         | No support for this OS/board combination             |
| partial      | Partial functionality available                      |

## Documentation Writing Standards

### Test Report Requirements
1. Test environment must include:

   ```markdown
   ## Test Environment
   ### System information (system version, download link, reference installation documentation)
   ### Hardware Information (board information, debugger information)
   ```

2. **Test steps** must include:
   ```markdown
   ## Installation Steps
   ### Image Flashing
   1. Download the image file
   2. If additional operations are needed to switch to flashing mode, please include these
   3. Use the dd command to write to storage device / flash with fastboot / use manufacturer-provided tools
   
   ### System Boot Process
   1. Login from serial port
   2. First boot configuration process
   3. Record terminal operations using asciinema
   ```

3. **Verification results** must include:

   ```markdown
   ## Expected Results
   ## Actual Results
   1. Key segments of boot logs
   2. Function test screenshots/recordings
   ```

4. It's recommended to refer to example documents in the project for writing.

### Internationalization (I18N)
- Main documentation should be written in English (README.md)
- Chinese translation documents should use the README_zh.md format
- Translation documents **do NOT contain** metadata headers
- Maintain correct hyperlinks between documents
- Use consistent terminology with other documents in the same language
