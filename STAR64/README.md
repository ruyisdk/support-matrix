---
vendor: pine64
product: Star64
cpu: JH7110
cpu_core: SiFive U74 + SiFive S7 + SiFive E24
ram: 4GB/8GB
---

# Pine64 Star64

## Test Environment

### Operating System Information

**Note: Star64 can use all Visionfive2 images, but USB, WiFi, and PCI might not work (see [Bringup Notes](https://wiki.pine64.org/wiki/STAR64))**

- NuttX
    - Source Link: https://github.com/apache/nuttx
    - Reference Installation Document: https://nuttx.apache.org/docs/latest/platforms/risc-v/jh7110/boards/star64/index.html
    - Toolchain:
        - Boot Image: https://github.com/starfive-tech/VisionFive2/releases/download/JH7110_VF2_515_v5.11.3/sdcard.img
        - DTB: https://github.com/starfive-tech/VisionFive2/releases
        - Toolchain: https://github.com/sifive/freedom-tools/releases
        - kflash: https://github.com/kendryte/kflash.py
- Armbian
    - Download Link: https://www.armbian.com/star64/
    - Reference Installation Document: https://www.hackster.io/lupyuen/rtos-on-a-risc-v-sbc-star64-jh7110-apache-nuttx-2a7429
- Yocto
    - Download Link: https://github.com/Fishwaldo/meta-pine64/releases/tag/v2.1
    - Reference Installation Document: https://github.com/Fishwaldo/meta-pine64
- Ubuntu 25.04:
  - Download Link: https://cdimage.ubuntu.com/releases/25.04/release/ubuntu-25.04-preinstalled-server-riscv64+jh7110.img.xz
  - Reference Installation Document: https://canonical-ubuntu-boards.readthedocs-hosted.com/en/latest/how-to/pine64-star64/
- Arch Linux
    - Source code Link: https://github.com/yogo1212/arch-linux-star64
    - Reference Installation Document: https://github.com/yogo1212/arch-linux-star64
- NixOS
    - Source code link: https://git.sr.ht/~fgaz/nixos-star64
    - Reference Installation Document: https://git.sr.ht/~fgaz/nixos-star64

### Hardware Information

- Pine64 Star64

## Test Results

| Software Category             | Package Name | Test Result (Test Report) |
| ----------------------------- | ------------ | ------------------------- |
| NuttX Image Build & Boot      | N/A          | [CFT][NuttX]              |
| Armbian Image Boot            | N/A          | [CFH][Armbian]            |
| Yocto Image Boot              | N/A          | [CFH][Yocto]              |
| Ubuntu Image Boot             | N/A          | [Basic][Ubuntu]           |
| Arch Linux Image Build & Boot | N/A          | [CFH][ArchLinux]          |
| NixOS Image Build & Boot      | N/A          | [CFH][NixOS]              |

[NuttX]: ./NuttX/README.md
[NixOS]: ./NixOS/README.md
[Armbian]: ./Armbian/README.md
[Yocto]: ./Yocto/README.md
[Ubuntu]: ./Ubuntu/README.md
[ArchLinux]: ./ArchLinux/README.md
