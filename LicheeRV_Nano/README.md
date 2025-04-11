---
vendor: sipeed-licheervnano
product: LicheeRV Nano
cpu: SG2002
cpu_core: XuanTie C906 + ARM Cortex-A53
ram: 2G
---

# LicheeRV Nano

## Test Environment

### Operating System Information

- BuildRoot & FreeRTOS
  - Download Link: https://github.com/sipeed/LicheeRV-Nano-Build/releases
    - BuildRoot SDK provided by Sipeed, which also includes FreeRTOS
  - Reference Installation Document: https://github.com/sipeed/LicheeRV-Nano-Build
- Debian
  - Download Link: https://github.com/scpcom/sophgo-sg200x-debian/releases/download/v1.6.7/licheervnano-e_sd.img.lz4
  - Reference Installation Document: https://github.com/scpcom/sophgo-sg200x-debian
- Alpine Linux 3.20.3 riscv64
  - Download Link:
    - Alpine minirootfs: [https://alpinelinux.org/downloads/](https://dl-cdn.alpinelinux.org/alpine/v3.20/releases/riscv64/alpine-minirootfs-3.20.3-riscv64.tar.gz)
  - Reference Installation Document:
    - [Alpine Wiki (Installation)](https://wiki.alpinelinux.org/wiki/Installation)
    - [Alpine Wiki (How to make a cross architecture chroot)](https://wiki.alpinelinux.org/wiki/How_to_make_a_cross_architecture_chroot)
- Fedora 41
  - Download Link: https://mirror.iscas.ac.cn/fedora-riscv/dl/Sipeed/LicheeRV_Nano/images/latest/LicheeRV_Nano-fedora-minimal.img.gz
  - Reference Installation Document: https://github.com/chainsx/fedora-riscv-builder

### Hardware Information

- LicheeRV Nano (SG2002)

## Test Results

| Software Category | Package Name | Test Results (Test Report)                          |
| ----------------- | ------------ | --------------------------------------------------- |
| BuildRoot Image   | N/A          | [Basic][BuildRoot]                                  |
| FreeRTOS Startup  | N/A          | [Basic][FreeRTOS]                                   |
| Debian Image      | N/A          | [Basic][Debian]                                     |
| Fedora Image      | N/A          | [Basic][Fedora]                                     |
| Alpine Linux Boot | N/A          | [Basic][Alpine] (requires building rootfs manually) |

[BuildRoot]: ./BuildRoot/README.md
[FreeRTOS]: ./FreeRTOS/README.md
[Debian]: ./Debian/README.md
[Alpine]: ./Alpine/README.md
[Fedora]: ./Fedora/README.md
