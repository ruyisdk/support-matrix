# Microchip Polarfire SoC FPGA Icicle Kit

## 测试环境

### 操作系统信息

- Ubuntu 24.04
    - 下载链接：https://cdimage.ubuntu.com/releases/24.04/release/
    - 参考安装文档：https://wiki.ubuntu.com/RISC-V/PolarFire%20SoC%20FPGA%20Icicle%20Kit
- BuildRoot 24.02.2
    - 源码下载链接：https://buildroot.org/downloads/buildroot-2024.02.2.tar.gz
    - 参考安装文档：https://gitlab.com/buildroot.org/buildroot/-/tree/master/board/microchip/mpfs_icicle?ref_type=heads
- OpenEmbedded / Yocto
    - 下载链接：https://github.com/polarfire-soc/meta-polarfire-soc-yocto-bsp
    - 参考安装文档：https://github.com/polarfire-soc/meta-polarfire-soc-yocto-bsp
- Arch Linux
    - 下载链接：https://archriscv.felixc.at/
    - 参考安装文档：https://felixc.at/2022/06/newbies-polarfire-soc-icicle-kit-first-experience
- OpenBSD
  - 下载链接：https://cdn.openbsd.org/pub/OpenBSD/snapshots/riscv64/
  - 参考安装文档：https://cdn.openbsd.org/pub/OpenBSD/snapshots/riscv64/INSTALL.riscv64
- FreeRTOS
    - 参考安装文档：https://github.com/polarfire-soc/polarfire-soc-documentation/blob/master/applications-and-demos/asymmetric-multiprocessing/amp_zh.md#building-the-linux--freertos--bm-demo
- Zephyr
    - 参考安装文档：https://docs.zephyrproject.org/latest/boards/microchip/mpfs_icicle/doc/index.html
- NuttX
    - 参考安装文档：https://nuttx.apache.org/docs/latest/platforms/risc-v/mpfs/index.html

### 硬件开发板信息

- Microchip Polarfire SoC FPGA Icicle Kit

## 测试结果

| 软件分类                | 软件包名 | 测试结果（测试报告）        |
|-----------------------|----------|---------------------------|
| Ubuntu 镜像启动         | N/A      | [Basic][Ubuntu]（官方支持） |
| Yocto 镜像构建及启动    | N/A      | [Basic][Yocto]            |
| BuildRoot 镜像启动      | N/A      | [Basic][BuildRoot]        |
| Arch Linux 启动         | N/A      | [CFT][Arch]               |
| OpenBSD 镜像启动        | N/A      | [CFT][OpenBSD]            |
| FreeRTOS 镜像构建及启动 | N/A      | [CFT][FreeRTOS]           |
| Zephyr 镜像构建及启动   | N/A      | [CFT][Zephyr]             |
| NuttX 镜像构建及启动    | N/A      | [CFT][NuttX]              |


[Ubuntu]: ./Ubuntu/README_zh.md
[BuildRoot]: ./BuildRoot/README_zh.md
[Yocto]: ./Yocto/README_zh.md
[Arch]: ./ArchLinux/README_zh.md
[OpenBSD]: ./OpenBSD/README_zh.md
[FreeRTOS]: ./FreeRTOS/README_zh.md
[Zephyr]: ./Zephyr/README_zh.md
[NuttX]: ./NuttX/README_zh.md