---
product: HiFive Premier P550
cpu: EIC7700X
cpu_core: SiFive P550
ram: 16G/32G
---

# HiFive Premier P550

## Overview

The HiFive Premier P550 is a high-performance RISC-V single-board computer in a Mini-DTX form factor powered by the ESWIN EIC7700X SoC with a SiFive Quad-Core P550 64-bit RISC-V processor running at 1.4 GHz with an integrated Imagination AXM-8-256 GPU and hardware accelerated AI NPU with ~20 TOPS. It has full featured PC IO and is pre-installed with Ubuntu 24.04 operating system.

## Hardware Specifications

- **Processor**: ESWIN EIC7700X (Quad-Core SiFive P550)
- **Memory**: 16GB/32GB LPDDR5
- **Storage**: 128GB eMMC
- **Interfaces**:
  - 2 10/100/1000 Ethernet RJ45 connectors
  - 1 Ethernet RJ45 connector for remote board management using dedicated MCU
  - 1 M.2 Key E connector for Wi-Fi / Bluetooth module (Interface via SDIO / UART)
  - 1 PCI Express Gen 3 x4 via a PCIe x16 slot
  - 2 Stacked USB 3.2 Gen 1 Type-A Connectors
  - 1 USB 19-pin male connector to support 2 USB 3.2 Gen 1 connectors on front panel
  - 1 USB type-E connector to support 1 USB 3.2 Gen Type-C connector on front panel
  - 1 JTAG Header
  - 1 SATA 3 connector (6Gb/s)
  - 1 microSD card connector
  - 1 USB Type-C (USB2 only) connector for debug UART/JTAG support through FT4232H
  - 1 HDMI 2.0 connector
  - Mini-ITX case compliant Front Panel Connector
  - 1 CR1220 battery holder for Real Time Clock
  - 3 fan headers
  - 1 header for audio interface (front panel stereo line-out and line-in / microphone signals)
  - 1 rear panel stereo jack with microphone input
  - 1 40-pin Peripheral I/O Header (1 I2C, 1x QSPI, 1x UART, 16x GPIO)
- **Power**: standard ATX power

## Supported Operating Systems

- Ubuntu - 2025.02.00 (Based on Ubuntu 24.04.01 LTS) (SiFive official support)
  - Download link: <https://github.com/sifiveinc/hifive-premier-p550-ubuntu/releases/tag/2025.02.00>
  - Reference Installation Document: <https://www.sifive.com/document-file/hifive-premier-p550-image-update-procedure>
- Debian - Debian-v1.0.0-20250228 (ESWIN official support)
  - Download link: <https://github.com/eswincomputing/eic7x-images/releases/tag/Debian-v1.0.0-20250228>
  - Reference Installation Document: <https://github.com/eswincomputing/eic7x-images/releases/download/Yocto-v1.0.0-20241021/EIC7700_Debian_Yocto_Ubuntu_System_Burnning_Guide.pdf>
- Yocto - 2024.11.00-HFP550 (SiFive official support)
  - Download link: <https://github.com/sifiveinc/freedom-u-sdk/releases/tag/2024.11.00-HFP550>
  - Reference Installation Document: <https://www.sifive.com/document-file/hifive-premier-p550-image-update-procedure>
- Deepin - 20250422-122731-EIC7700 (Deepin 25 Preview)
  - Download link: <https://ci.deepin.com/repo/deepin/deepin-ports/cdimage/20250422/riscv64/deepin-25-crimson-preview-riscv64-eic7700-20250422-122731.tar.xz>
  - Reference Installation Document: [README.md](./Deepin/README.md)

## Test Results

| Software Category     | Package Name | Test Results (Test Report) |
|-----------------------|--------------|----------------------------|
| Ubuntu LTS image boot | N/A          | [CFT][Ubuntu LTS]          |
| Debian image boot     | N/A          | [CFT][Debian]              |
| Yocto image boot      | N/A          | [CFT][Yocto]               |
| Deepin                | N/A          | [Success][Deepin]          |

[Ubuntu LTS]: ./Ubuntu/README_LTS.md
[Debian]: ./Debian/README.md
[Yocto]: ./Yocto/README.md
[Deepin]: ./Deepin/README.md
