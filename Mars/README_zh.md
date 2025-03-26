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
- Deepin
  - 下载链接：<https://ci.deepin.com/repo/deepin/deepin-ports/cdimage/20250122/riscv64/deepin-25-beige-preview-riscv64-jh7110-20250122-110620.tar.xz>
  - 参考安装文档：
    1. <https://milkv.io/zh/docs/mars/getting-started/boot>
    2. <https://deepin-community.github.io/sig-deepin-ports/docs/install/riscv/jh7110>

### 硬件开发板信息

- Milk-V Mars

## 测试结果

| 软件分类             | 软件包名 | 测试结果（测试报告）              |
| -------------------- | -------- | --------------------------------- |
| Debian 镜像启动      | N/A      | [成功][Debian]（Milk-V 厂商镜像） |
| BuildRoot 构建及启动 | N/A      | [成功][BuildRoot]                 |
| Ubuntu 镜像启动      | N/A      | [CFT][Ubuntu]                     |
| Ubuntu LTS 镜像启动  | N/A      | [成功][Ubuntu LTS]                 |
| Deepin 镜像启动      | N/A      | [成功][Deepin]                     |

[Debian]: ./Debian/README_zh.md
[BuildRoot]: ./BuildRoot/README_zh.md
[Ubuntu]: ./Ubuntu/README_zh.md
[Ubuntu LTS]: ./Ubuntu/README_LTS_zh.md
[Deepin]: ./Deepin/README_zh.md
