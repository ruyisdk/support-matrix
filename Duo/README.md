# Milk-V Duo

## Test Environment

### Operating System Information

- BuildRoot & FreeRTOS
  - Download link: https://github.com/milkv-duo/duo-buildroot-sdk/releases
    - Official BuildRoot SDK provided by Milk-V, including FreeRTOS
  - Reference Installation Document: https://github.com/milkv-duo/duo-buildroot-sdk
- Arch Linux
  - Download link: https://drive.google.com/file/d/1Qf8ioR29KCsvt2MIWre168Um9Q8ot_z5/view?usp=sharing
  - Reference Installation Document: https://xyzdims.com/3d-printers/misc-hardware-notes/iot-milk-v-duo-risc-v-esbc-running-linux/#ArchLinux_Disk_Image
- Debian trixie/sid
  - Download link: https://drive.google.com/file/d/1TqMuFsRo5Es2Y6-qAyxV8jnFdAkcCp4v/view?usp=sharing
  - Reference Installation Document: https://github.com/hongwenjun/riscv64/tree/main/milkv-duo
- Fedora 38
  - Download link: https://github.com/chainsx/fedora-riscv-builder/releases/download/20230719-1650/Fedora-38-Minimal-MilkV-Duo-riscv64.img.xz
  - Reference Installation Document: https://github.com/chainsx/fedora-riscv-builder
- RT-Thread 5.1.0
  - Source code link: https://github.com/RT-Thread/rt-thread
  - Reference Installation Document: https://github.com/RT-Thread/rt-thread/tree/master/bsp/cvitek/cv1800b
- openEuler 23.03 riscv64
  - Download links:
    - buildroot: https://github.com/milkv-duo/duo-buildroot-sdk.git
    - rootfs: https://mirror.iscas.ac.cn/openeuler-sig-riscv/openEuler-RISC-V/preview/openEuler-23.03-V1-riscv64/openeuler-rootfs.tar.gz
  - Reference Installation Document: https://blog.inuyasha.love/linuxeveryday/33.html

### Hardware Information

- Milk-V Duo (64M, CV1800B)

## Test Results


| Software Category              | Package Name | Test Results (Test Report)                        |
| ------------------------------ | ------------ | ------------------------------------------------- |
| BuildRoot Image Boot           | N/A          | [Success][Duo] (flashed via `ruyi` CLI)           |
| FreeRTOS Boot                  | N/A          | [Success][FreeRTOS] (included in BuildRoot image) |
| Arch Linux Image Boot          | N/A          | [Success][Arch]                                   |
| Debian Image Boot              | N/A          | [Success][Debian]                                 |
| RT-Thread Image Build and Boot | N/A          | [Success][RT-Thread]                              |
| Fedora Image Boot              | N/A          | [Failed][Fedora]                                  |
| openEuler                      | N/A          | [Success][oE]                                     |
| ThreadX Image Build and Boot   | N/A          | [Success][ThreadX]                                |
| Zephyr Image Build and Boot    | N/A          | [Success][Zephyr]                                 |

[Duo]: ./BuildRoot/README.md
[Arch]: ./ArchLinux/README.md
[Debian]: ./Debian/README.md
[Fedora]: ./Fedora/README.md
[RT-Thread]: ./RT-Thread/README.md
[FreeRTOS]: ./FreeRTOS/README.md
[oE]: ./openEuler/README.md
[ThreadX]: ./ThreadX/README.md
[Zephyr]: ./Zephyr/README.md

