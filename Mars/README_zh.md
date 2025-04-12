# Milk-V Mars

## 测试环境

### 操作系统信息

- BuildRoot/Debian（官方提供）
  - 下载链接：<https://github.com/milkv-mars/mars-buildroot-sdk/releases/>
  - 参考安装文档：<https://milkv.io/zh/docs/mars/getting-started/boot>
- Ubuntu 24.10
  - 下载链接：<https://cdimage.ubuntu.com/releases/24.10/release/ubuntu-24.10-preinstalled-server-riscv64+milkvmars.img.xz>
- Ubuntu 24.04.2 LTS
  - 下载链接：<https://cdimage.ubuntu.com/releases/24.04.2/release/ubuntu-24.04.2-preinstalled-server-riscv64+milkvmars.img.xz>
  - 参考安装文档：<https://milkv.io/zh/docs/mars/getting-started/boot>
- Deepin 25 preview
  - 下载链接：<https://ci.deepin.com/repo/deepin/deepin-ports/cdimage/20250122/riscv64/deepin-25-beige-preview-riscv64-jh7110-20250122-110620.tar.xz>
  - 参考安装文档：
    1. <https://milkv.io/zh/docs/mars/getting-started/boot>
    2. <https://deepin-community.github.io/sig-deepin-ports/docs/install/riscv/jh7110>
- eweOS 6.13.8
  - 下载链接：<https://github.com/panglars/eweos-vf2-mainline>
  - 参考安装文档：<https://github.com/panglars/eweos-vf2-mainline/blob/main/README.md>
  - eweOS官网：<https://os.ewe.moe/>
- Fedora 41
  - 下载链接：<https://mirror.iscas.ac.cn/fedora-riscv/dl/StarFive/visionfive2/images/fedora-disk-gnome-workstation_starfive_vf2_f41_20241201091200.raw.gz>
  - 参考安装文档：
    1. <https://milkv.io/zh/docs/mars/getting-started/boot>
    2. <https://images.fedoravforce.org/Mars>
- Guix
  - 下载链接：<https://ci.guix.gnu.org/search/latest?query=spec:images+status:success+system:x86_64-linux+visionfive2-barebones-raw-image>
  - 参考安装文档：<https://milkv.iso/zh/docs/mars/getting-started/boot>

### 硬件开发板信息

- Milk-V Mars

## 测试结果

| 软件分类             | 软件包名 | 测试结果（测试报告）              |
| -------------------- | -------- | --------------------------------- |
| Debian 镜像启动      | N/A      | [成功][Debian]（Milk-V 厂商镜像） |
| BuildRoot 构建及启动 | N/A      | [成功][BuildRoot]                 |
| Ubuntu 镜像启动      | N/A      | [成功][Ubuntu]                     |
| Ubuntu LTS 镜像启动  | N/A      | [成功][Ubuntu LTS]                 |
| Deepin 镜像启动      | N/A      | [成功][Deepin]                     |
| eweOS 镜像启动       | N/A      | [成功][eweOS]                     |
| Fedora 镜像启动      | N/A      | [成功][Fedora]                     |
| Guix 镜像启动        | N/A      | [成功][Guix]                     |

[Debian]: ./Debian/README_zh.md
[BuildRoot]: ./BuildRoot/README_zh.md
[Ubuntu]: ./Ubuntu/README_zh.md
[Ubuntu LTS]: ./Ubuntu/README_LTS_zh.md
[Deepin]: ./Deepin/README_zh.md
[eweOS]: ./eweOS/README_zh.md
[Fedora]: ./Fedora/README_zh.md
[Guix]: ./Guix/README_zh.md
