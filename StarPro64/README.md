---
vendor: PINE64
product: StarPro64
cpu: EIC7700X
cpu_core: SiFive P550
ram: 8GB / 16GB / 32 GB

board_variant: [
    generic,
]
cpu_arch: [
    sifive-p500,
]
---

# StarPro64

## Overview
The StarPro64 is a RISC-V single-board computer from PINE64, featuring the EIC7700X SoC with a CPU speed of 1.8 GHz and NPU performance of 19.95 TOPS. It retains the model-A board format, similar to the Star64, with dual Ethernet ports, digital video output, USB 2.0 and 3.0 ports, a full GPIO header, and a 4x PCIe lane.

## Hardware Specifications

Reference: https://pine64.org/documentation/StarPro64/_full/#specifications

- **Processor**: ESWIN EIC7700X
- **Memory**: 8GB / 16GB / 32GB LPDDR5
- **Storage**:
  - on-board 128Mbit (16MByte) XSPI NOR flash memory - bootable
  - microSD - bootable, supports SDHC and SDXC and storage up to 256GB
  - eMMC - bootable (optional eMMC Module)
- **Interfaces**:
  - PCIe Gen3 ×4 lane
  - 2×20 pins “Pi2” GPIO Header
  - 4 lane MiPi DSI port for LCD panel
  - 4 lane MiPi CSI port for camera module
  - 2× USB3.0 Dedicated Host port
  - 2× USB2.0 Shared Host port
- **Power**: 12V DC

## Supported Operating Systems
- deepin - 25

## Test Results
| Software Category | Package Name | Test Results (Test Report) |
|-------------------|--------------|----------------------------|
| deepin Image Boot | N/A          | Success                    |
