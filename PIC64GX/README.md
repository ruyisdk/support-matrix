---
product: PIC64GX Curiosity Kit
cpu: PIC64GX1000-V/FCS
cpu_core: SiFive U54 + SiFive E51
---

# Microchip PIC64GX Curiosity Kit

## Test Environment

### Operating System Information

- Ubuntu 24.10
    - Download Link: https://cdimage.ubuntu.com/releases/24.10/release/
    - Reference Installation Document: https://wiki.ubuntu.com/RISC-V/Microchip%20PIC64GX1000%20Curiosity%20Kit
- Ubuntu 24.04.2 LTS
    - Download Link: https://cdimage.ubuntu.com/releases/24.04.2/release/
    - Reference Installation Document: https://wiki.ubuntu.com/RISC-V/Microchip%20PIC64GX1000%20Curiosity%20Kit
- OpenEmbedded / Yocto
    - Download Link: https://github.com/pic64gx/meta-pic64gx-yocto-bsp
    - Reference Installation Document: https://github.com/pic64gx/meta-pic64gx-yocto-bsp
- Zephyr
    - Reference Installation Document: https://github.com/pic64gx/pic64gx-zephyr

### Hardware Information

- Microchip Polarfire SoC FPGA Icicle Kit

## Test Results

| Software Category           | Package Name | Test Results (Test Report)          |
|-----------------------------|--------------|-------------------------------------|
| Ubuntu Image Boot           | N/A          | [CFT][Ubuntu] (Official Support)    |
| Ubuntu LTS Image Boot       | N/A          | [CFT][Ubuntu LTS] (Official Support)|
| Yocto Image Build and Boot  | N/A          | [CFT][Yocto]                        |
| Zephyr Image Build and Boot | N/A          | [CFT][Zephyr]                       |

[Ubuntu]: ./Ubuntu/README.md
[Ubuntu LTS]: ./Ubuntu/README_LTS.md
[Yocto]: ./Yocto/README.md
[Zephyr]: ./Zephyr/README.md