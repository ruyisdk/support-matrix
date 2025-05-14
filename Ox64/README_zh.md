# Pine64 Ox64

## 测试环境

### 操作系统信息

- BuildRoot
  - 下载链接：https://github.com/openbouffalo/buildroot_bouffalo/releases/download/v1.0.1/bl808-linux-pine64_ox64_full_defconfig.tar.gz
    - SDK：https://github.com/bouffalolab/bl_mcu_sdk
    - 烧录工具：https://openbouffalo.org/static-assets/bldevcube/BouffaloLabDevCube-v1.8.3.zip
  - 参考安装文档：https://www.hackster.io/lupyuen/8-risc-v-sbc-on-a-real-time-operating-system-ox64-nuttx-474358
- Arch Linux
  - 下载链接：https://github.com/domhathair/pine64_ox64_archlinux/releases/download/v2024.06.1/sdcard.tar.gz
    - SDK：https://github.com/bouffalolab/bl_mcu_sdk
    - 烧录工具：https://openbouffalo.org/static-assets/bldevcube/BouffaloLabDevCube-v1.8.3.zip
  - 参考安装文档：https://github.com/domhathair/pine64_ox64_archlinux
- NuttX
  - 下载链接：https://github.com/lupyuen2/wip-nuttx/releases/download/gpio2-1/Image
    - SDK：https://github.com/bouffalolab/bl_mcu_sdk
    - 烧录工具：https://openbouffalo.org/static-assets/bldevcube/BouffaloLabDevCube-v1.8.3.zip
  - 参考安装文档：https://www.hackster.io/lupyuen/8-risc-v-sbc-on-a-real-time-operating-system-ox64-nuttx-474358

### 硬件开发板信息

- Pine64 Ox64 (BL808, 128MB XSPI Flash)

## 测试结果

| 软件分类            | 软件包名 | 测试结果（测试报告） |
| ------------------- | -------- | -------------------- |
| BuildRoot 镜像启动  | N/A      | [成功][BuildRoot]    |
| Arch Linux 镜像启动 | N/A      | [成功][ArchLinux]    |
| NuttX 镜像启动      | N/A      | [成功][NuttX]        |

[BuildRoot]: ./BuildRoot/README_zh.md
[NuttX]: ./NuttX/README_zh.md
[ArchLinux]: ./ArchLinux/README_zh.md
