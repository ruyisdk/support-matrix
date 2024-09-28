---
product: Milk-V Mars
cpu: JH7110
cpu_core: SiFive U74 + SiFive S7 + SiFive E24
---

# Milk-V Mars

## Test Environment

### Operating System Information

- BuildRoot/Debian (officially provided)
    - Download Link: https://github.com/milkv-mars/mars-buildroot-sdk/releases/
    - Reference Installation Document: https://milkv.io/zh/docs/mars/getting-started/boot
- Ubuntu
    - Download Link: https://cdimage.ubuntu.com/releases/24.04/release/ubuntu-24.04-preinstalled-server-riscv64+milkvmars.img.xz
    - Reference Installation Document: https://milkv.io/zh/docs/mars/getting-started/boot
- Deepin
    - Download Link: https://cdimage.deepin.com/RISC-V/preview-20240613-riscv64/deepin-23-beige-preview-riscv64-milkv-mars-20240613-123442.tar.xz
    - Reference Installation Document: https://milkv.io/zh/docs/mars/getting-started/boot

### Hardware Information

- Milk-V Mars

## Test Results

| Software Category      | Package Name | Test Result (Test Report)                    |
| ---------------------- | ------------ | -------------------------------------------- |
| Debian Image Boot      | N/A          | [Successful][Debian] (Milk-V Official Image) |
| BuildRoot Build & Boot | N/A          | [Successful][BuildRoot]                      |
| Ubuntu Image Boot      | N/A          | [Successful][Ubuntu]                         |
| Deepin Image Boot      | N/A          | [CFT][Deepin]                                |

[Debian]: ./Debian/README.md
[BuildRoot]: ./BuildRoot/README.md
[Ubuntu]: ./Ubuntu/README.md
[Deepin]: ./Deepin/README.md
