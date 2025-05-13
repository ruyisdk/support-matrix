---
product: Pine64 Ox64
cpu: BL808
cpu_core: XuanTie C906 + XuanTie E907 + XuanTie E902
ram: 768KB(SRAM) + 64MB(PSRAM)
---

# Sipeed M1s

## Test Environment

### Operating System Information

- BuildRoot
  - Download Link: https://github.com/openbouffalo/buildroot_bouffalo/releases/download/v1.0.1/bl808-linux-pine64_ox64_full_defconfig.tar.gz
    - SDK: https://github.com/bouffalolab/bl_mcu_sdk
    - Flashing Tool: https://openbouffalo.org/static-assets/bldevcube/BouffaloLabDevCube-v1.8.3.zip
  - Reference Installation Document: https://www.hackster.io/lupyuen/8-risc-v-sbc-on-a-real-time-operating-system-ox64-nuttx-474358
- ArchLinux
  - Download Link: https://github.com/domhathair/pine64_ox64_archlinux/releases/download/v2024.06.1/sdcard.tar.gz
    - SDK: https://github.com/bouffalolab/bl_mcu_sdk
    - Flashing Tool: https://openbouffalo.org/static-assets/bldevcube/BouffaloLabDevCube-v1.8.3.zip
  - Reference Installation Document: https://github.com/domhathair/pine64_ox64_archlinux
- NuttX
  - Download Link: https://github.com/lupyuen2/wip-nuttx/releases/download/gpio2-1/Image
    - SDK: https://github.com/bouffalolab/bl_mcu_sdk
    - Flashing Tool: https://openbouffalo.org/static-assets/bldevcube/BouffaloLabDevCube-v1.8.3.zip
  - Reference Installation Document: https://www.hackster.io/lupyuen/8-risc-v-sbc-on-a-real-time-operating-system-ox64-nuttx-474358

### Hardware Information

- Pine64 Ox64 (BL808, 128MB XSPI Flash)

## Test Results

| Software Category     | Package Name | Test Result (Test Report) |
| --------------------- | ------------ | ------------------------- |
| BuildRoot Image Boot  | N/A          | [Successful][BuildRoot]   |
| Arch Linux Image Boot | N/A          | [Successful][ArchLinux]   |
| NuttX Image Boot      | N/A          | [Successful][NuttX]       |

[BuildRoot]: ./BuildRoot/README.md
[NuttX]: ./NuttX/README.md
[ArchLinux]: ./ArchLinux/README.md
