# Milk-V Duo S

## 测试环境

### 操作系统信息

- BuildRoot & FreeRTOS
  - 下载链接：https://github.com/milkv-duo/duo-buildroot-sdk/releases
    - Milk-V 官方提供的 BuildRoot SDK，同时包含了 FreeRTOS
  - 参考安装文档：https://github.com/milkv-duo/duo-buildroot-sdk
- Apache NuttX RTOS
  - 源码链接
    - NuttX: https://github.com/lupyuen2/wip-nuttx/tree/sg2000
    - NuttX Apps: https://github.com/lupyuen2/wip-nuttx-apps/tree/sg2000
  - 参考安装文档；https://github.com/lupyuen/nuttx-sg2000
- Debian
  - 下载链接：https://github.com/Fishwaldo/sophgo-sg200x-debian/releases/tag/v1.4.0
  - 参考安装文档：https://github.com/Fishwaldo/sophgo-sg200x-debian
- Zephyr
  - 源码链接：https://github.com/zephyrproject-rtos/zephyr/tree/main
  - 参考文档：
      - https://docs.zephyrproject.org/latest/develop/getting_started/index.html
      - https://github.com/milkv-duo/duo-buildroot-sdk
- Ubuntu
  - 下载链接：https://drive.google.com/file/d/1mkzLhvtjJup3GbgWKZdwL80PZMMXg7n1/view
  - 参考文档：https://xyzdims.com/3d-printers/misc-hardware-notes/iot-milk-v-duo-risc-v-esbc-running-linux/
- OpenWrt
  - 下载链接：https://github.com/draftbottle/Milkv-duo-openwrt/releases/download/v4.0/milkv-duos.img
  - 参考文档：
	  - https://community.milkv.io/t/milk-v-duo-openwrt/2399/10
	  - https://github.com/draftbottle/VizOS
- NixOS
  - 源码链接: https://github.com/NickCao/nixos-riscv
  - 参考安装文档: https://github.com/NickCao/nixos-riscv/README.md

### 硬件开发板信息

- Milk-V Duo S (512M, SG2000)

## 测试结果

| 软件分类                | 软件包名     | 测试结果（测试报告） |
| ----------------------- | ------------ | -------------------- |
| BuildRoot 镜像启动      | N/A          | [成功][BuildRoot]    |
| BuildRoot 镜像启动      | N/A          | [成功][BuildRootV2]  |
| Debian 镜像启动         | N/A          | [成功][Debian]       |
| FreeRTOS 启动           | mailbox-test | [成功][FreeRTOS]     |
| Apache NuttX 构建及启动 | N/A          | [成功][NuttX]        |
| Zephyr 镜像构建及启动   | N/A          | [成功][Zephyr]       |
| Ubuntu 镜像启动         | N/A          | [成功][Ubuntu]       |
| OpenWrt 镜像构建及启动  | N/A          | [成功][OpenWrt]      |
| NixOS 镜像构建及启动    | N/A          | [成功][NixOS]        |

[BuildRoot]: ./BuildRoot/README_zh.md
[BuildRootV2]: ./BuildRoot/README_v2_zh.md
[Debian]: ./Debian/README_zh.md
[FreeRTOS]: ./FreeRTOS/README_zh.md
[NuttX]: ./NuttX/README_zh.md
[Zephyr]: ./Zephyr/README_zh.md
[Ubuntu]: ./Ubuntu/README_zh.md
[OpenWrt]: ./OpenWrt/README_zh.md
[NixOS]: ./NixOS/README_zh.md