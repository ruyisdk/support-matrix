---
vendor: [Vendor identifier - Board identifier]
product: [Development Board Name]
cpu: [CPU Model]
cpu_core: [CPU Core Architecture]
ram: [Memory and flash information]
board_variant: [Board Variant] # e.g., 8g/16g version. If you don't have a variant, use generic instead.
cpu_arch: [ # Supported CPU Architectures lists are in assets/metadata.yml:arches
    CPU Architectures, # eg: xuantie-e902, armv8-a...
    # If none of the above, add a new one in assets/metadata.yml:arches
]
---

# [Development Board Name]

## Overview
This development board is a high-performance embedded platform suitable for various applications such as IoT, edge computing, and robotics.

## Hardware Specifications
- **Processor**: [CPU Model]
- **Memory**: [Memory Size]
- **Storage**: [Storage Type and Size]
- **Interfaces**: [Interface Types, e.g., USB, HDMI]
- **Power**: [Power Requirements]

## Supported Operating Systems
- [Operating System Name 1] - [Version]
- [Operating System Name 2] - [Version]
- [Operating System Name 3] - [Version]

## Test Results
| Software Category | Package Name | Test Results (Test Report) |
|-------------------|--------------|----------------------------|
| [Operating System Name 1] | N/A | [Success/Failure] |
| [Operating System Name 2] | N/A | [Success/Failure] |
| [Operating System Name 3] | N/A | [Success/Failure] |
