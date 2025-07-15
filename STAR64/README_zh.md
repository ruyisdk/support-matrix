# Pine64 Star64

## 测试环境

### 操作系统信息

**注：Star64 理论上可以使用所有 Visionfive2 镜像，但 USB、Wifi 和 PCI 可能不工作（见[Bringup Notes](https://wiki.pine64.org/wiki/STAR64)）**

- NuttX
    - 源码链接：https://github.com/apache/nuttx
    - 参考安装文档：https://nuttx.apache.org/docs/latest/platforms/risc-v/jh7110/boards/star64/index.html
    - 工具链：
        - 启动镜像：https://github.com/starfive-tech/VisionFive2/releases/download/JH7110_VF2_515_v5.11.3/sdcard.img
        - DTB：https://github.com/starfive-tech/VisionFive2/releases
        - toolchain: https://github.com/sifive/freedom-tools/releases
        - kflash：https://github.com/kendryte/kflash.py
- Armbian
    - 下载链接：https://www.armbian.com/star64/
    - 参考安装文档：https://www.hackster.io/lupyuen/rtos-on-a-risc-v-sbc-star64-jh7110-apache-nuttx-2a7429
- Deepin
    - 下载链接：https://github.com/deepin-community/deepin-riscv-board/releases/download/v20221209/deepin-visionfive-2-20221208180420.img.zst.0
    - 参考安装文档：https://cdimage.deepin.com/RISC-V/VisionFive-v2-image/README.txt
- DietPi
    - 下载链接：https://dietpi.com/downloads/images/DietPi_Star64-RISC-V-Trixie.img.xz
    - 参考安装文档：https://dietpi.com/blog/?p=2629
- irradium
    - 下载链接：https://dl.irradium.org/irradium/images/star64/irradium-3.8-riscv64-xfce-star64-6.12.33-build-20250613.img.zst
    - 参考安装文档：https://dl.irradium.org/irradium/images/star64/
- NetBSD
    - 下载链接: [riscv64.img.gz](https://nyftp.netbsd.org/pub/NetBSD-daily/HEAD/latest/riscv-riscv64/binary/gzimg/)
- Yocto
    - 下载链接：https://github.com/Fishwaldo/meta-pine64/releases/tag/v2.1
    - 参考安装文档：https://github.com/Fishwaldo/meta-pine64
- Ubuntu 25.04:
    - 下载链接：https://cdimage.ubuntu.com/releases/25.04/release/ubuntu-25.04-preinstalled-server-riscv64+jh7110.img.xz
    - 参考安装文档：https://canonical-ubuntu-boards.readthedocs-hosted.com/en/latest/how-to/pine64-star64/
- Arch Linux
    - 源码链接：https://github.com/yogo1212/arch-linux-star64
    - 参考安装文档：https://github.com/yogo1212/arch-linux-star64
- NixOS
    - 源码链接：https://git.sr.ht/~fgaz/nixos-star64
    - 参考安装文档：https://git.sr.ht/~fgaz/nixos-star64

### 硬件开发板信息

- Pine64 Star64

## 测试结果

| 软件分类                  | 软件包名 | 测试结果（测试报告） |
| ------------------------- | -------- | -------------------- |
| NuttX 镜像构建及启动      | N/A      | [Basic][NuttX]       |
| Armbian 镜像启动          | N/A      | [CFH][Armbian]       |
| Yocto 镜像启动            | N/A      | [Basic][Yocto]       |
| Ubuntu 镜像启动           | N/A      | [Basic][Ubuntu]      |
| Arch Linux 镜像构建及启动 | N/A      | [CFH][ArchLinux]     |
| NixOS 镜像构建及启动      | N/A      | [CFH][NixOS]         |
| Deepin 镜像启动           | N/A      | [Basic][Deepin]      |
| DietPi 镜像启动           | N/A      | [Basic][DietPi]      |
| irradium 镜像启动         | N/A      | [Basic][irradium]    |
| NetBSD 镜像启动           | N/A      | [Basic][NetBSD]      |

[NixOS]: ./NixOS/README_zh.md
[NuttX]: ./NuttX/README_zh.md
[Armbian]: ./Armbian/README_zh.md
[Yocto]: ./Yocto/README_zh.md
[Ubuntu]: ./Ubuntu/README_zh.md
[ArchLinux]: ./ArchLinux/README_zh.md
[Deepin]: ./Deepin/README_zh.md
[DietPi]: ./DietPi/README_zh.md
[irradium]: ./irradium/README_zh.md
[NetBSD]: ./NetBSD/README_zh.md