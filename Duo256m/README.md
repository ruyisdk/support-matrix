---
product: Milk-V Duo (256M)
cpu: SG2002
cpu_core: XuanTie C906 + ARM Cortex-A53
---

# Milk-V Duo 256M

## Test Environment

### Operating System Information

- BuildRoot & FreeRTOS
  - Download link: [https://github.com/milkv-duo/duo-buildroot-sdk/releases](https://github.com/milkv-duo/duo-buildroot-sdk/releases)
    - Official Milk-V provided BuildRoot SDK, which also includes FreeRTOS.
  - Reference Installation Document: [https://github.com/milkv-duo/duo-buildroot-sdk](https://github.com/milkv-duo/duo-buildroot-sdk)
- Debian
  - Download link: [https://github.com/Fishwaldo/sophgo-sg200x-debian](https://github.com/Fishwaldo/sophgo-sg200x-debian)
  - Reference Installation Document: [https://github.com/Fishwaldo/sophgo-sg200x-debian](https://github.com/Fishwaldo/sophgo-sg200x-debian)
- FreeRTOS
  - Download link: https://github.com/milkv-duo/duo-buildroot-sdk/releases
  - Reference Installation Document: https://github.com/milkv-duo/duo-buildroot-sdk
      - FreeRTOS: https://milkv.io/zh/docs/duo/getting-started/rtoscore
- RT-Thread
  - Source code link: [https://github.com/RT-Thread/rt-thread](https://github.com/RT-Thread/rt-thread)
  - Reference Installation Document: [https://github.com/RT-Thread/rt-thread/blob/6101f1fd29374ac69c107e3cfeadfa06b0c901f9/bsp/cvitek/cv18xx_risc-v/README.md](https://github.com/RT-Thread/rt-thread/blob/6101f1fd29374ac69c107e3cfeadfa06b0c901f9/bsp/cvitek/cv18xx_risc-v/README.md)
- Zephyr
  - Source code link: https://github.com/zephyrproject-rtos/zephyr/tree/main
  - Reference Installation Document:
      - https://docs.zephyrproject.org/latest/develop/getting_started/index.html
      - https://github.com/milkv-duo/duo-buildroot-sdk
- Alpine Linux 3.20.3 riscv64
  - Download Link: 
    - Alpine minirootfs: [https://alpinelinux.org/downloads/](https://dl-cdn.alpinelinux.org/alpine/v3.20/releases/riscv64/alpine-minirootfs-3.20.3-riscv64.tar.gz)
    - Latest Duo 256M Debian image (for the kernel and its modules): [https://github.com/Fishwaldo/sophgo-sg200x-debian/releases/](https://github.com/Fishwaldo/sophgo-sg200x-debian/releases/download/v1.4.0/duo256_sd.img.lz4)
  - Reference Installation Document: 
    - [Alpine Wiki (Installation)](https://wiki.alpinelinux.org/wiki/Installation)
    - [Alpine Wiki (How to make a cross architecture chroot)](https://wiki.alpinelinux.org/wiki/How_to_make_a_cross_architecture_chroot)
### Hardware Information

- Milk-V Duo (256M, SG2002)

## Test Results

| Software Category            | Package Name | Test Result (Report)                                  |
| ---------------------------- | ------------ | ----------------------------------------------------- |
| BuildRoot Image Boot         | N/A          | [Success][BuildRoot]                                  |
| FreeRTOS Boot                | N/A          | [Success][FreeRTOS] (Included in BuildRoot image)     |
| Debian Image Boot            | N/A          | [Success][Debian]                                     |
| RT-Thread Image Build & Boot | N/A          | [Success][RT-Thread]                                  |
| Zephyr Image Build & Boot    | N/A          | [Success][Zephyr]                                     |
| Alpine Linux Boot            | N/A          | [WIP/CFH][Alpine] (requires manually building rootfs) |

[BuildRoot]: ./BuildRoot/README.md
[Debian]: ./Debian/README.md
[RT-Thread]: ./RT-Thread/README.md
[FreeRTOS]: ./FreeRTOS/README.md
[Zephyr]: ./Zephyr/README.md
[Alpine]: ./Alpine/README.md