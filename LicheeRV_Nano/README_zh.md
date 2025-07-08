# LicheeRV Nano

## 测试环境

### 操作系统信息

- BuildRoot & FreeRTOS
  - 下载链接：https://github.com/sipeed/LicheeRV-Nano-Build/releases
    - Sipeed 官方提供的 BuildRoot SDK，同时包含了 FreeRTOS
  - 参考安装文档：https://github.com/sipeed/LicheeRV-Nano-Build
- Debian
  - 下载链接：https://github.com/scpcom/sophgo-sg200x-debian/releases/download/v1.6.7/licheervnano-e_sd.img.lz4
  - 参考安装文档：https://github.com/scpcom/sophgo-sg200x-debian
- Ubuntu
  - 下载链接：https://github.com/Z841973620/licheervnano-ubuntu/releases/tag/jammy
  - 参考安装文档：https://github.com/Z841973620/licheervnano-ubuntu
- Alpine Linux 3.20.3 riscv64
  - 下载链接：
    - Alpine minirootfs: [https://alpinelinux.org/downloads/](https://dl-cdn.alpinelinux.org/alpine/v3.20/releases/riscv64/alpine-minirootfs-3.20.3-riscv64.tar.gz)
  - 参考安装文档：
    - [Alpine Wiki (Installation)](https://wiki.alpinelinux.org/wiki/Installation)
    - [Alpine Wiki (How to make a cross architecture chroot)](https://wiki.alpinelinux.org/wiki/How_to_make_a_cross_architecture_chroot)
- Fedora 41
  - 下载链接：https://mirror.iscas.ac.cn/fedora-riscv/dl/Sipeed/LicheeRV_Nano/images/latest/LicheeRV_Nano-fedora-minimal.img.gz
  - 参考安装文档：https://github.com/chainsx/fedora-riscv-builder

### 硬件开发板信息

- LicheeRV Nano (SG2002)

## 测试结果

| 软件分类           | 软件包名 | 测试结果（测试报告）                 |
| ------------------ | -------- | ------------------------------------ |
| BuildRoot 镜像启动 | N/A      | [Basic][BuildRoot]                   |
| FreeRTOS 启动      | N/A      | [Basic][FreeRTOS]                    |
| Debian 镜像启动    | N/A      | [Basic][Debian]                      |
| Ubuntu 镜像启动    | N/A      | [Basic][Ubuntu]                      |
| Alpine Linux 启动  | N/A      | [Basic][Alpine]（需手工构建 rootfs） |
| Fedora 镜像启动    | N/A      | [Basic][Fedora]                      |

[BuildRoot]: ./BuildRoot/README_zh.md
[FreeRTOS]: ./FreeRTOS/README_zh.md
[Debian]: ./Debian/README_zh.md
[Ubuntu]: ./Ubuntu/README_zh.md
[Alpine]: ./Alpine/README_zh.md
[Fedora]: ./Fedora/README_zh.md