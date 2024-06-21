# Milk-V Mars

## 测试环境

### 操作系统信息

- BuildRoot/Debian（官方提供）
    - 下载链接：https://github.com/milkv-mars/mars-buildroot-sdk/releases/
    - 参考安装文档：https://milkv.io/zh/docs/mars/getting-started/boot
- Ubuntu
    - 下载链接：https://cdimage.ubuntu.com/releases/24.04/release/ubuntu-24.04-preinstalled-server-riscv64+milkvmars.img.xz
    - 参考安装文档：https://milkv.io/zh/docs/mars/getting-started/boot

### 硬件开发板信息

- Milk-V Mars

## 测试结果

| 软件分类             | 软件包名 | 测试结果（测试报告）             |
|------------------|----------|--------------------------------|
| Debian 镜像启动      | N/A      | [成功][Debian]（Milk-V 厂商镜像） |
| BuildRoot 构建及启动 | N/A      | [成功][BuildRoot]               |
| Ubuntu 镜像启动      | N/A      | [成功][Ubuntu]                  |

[Debian]: ./Debian/README.md
[BuildRoot]: ./BuildRoot/README.md
[Ubuntu]: ./Ubuntu/README.md