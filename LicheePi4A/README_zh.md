# Lichee Pi 4A

## 测试环境

### 操作系统信息

- openEuler RISC-V 24.03 Preview
    - 下载链接：https://mirror.iscas.ac.cn/openeuler-sig-riscv/openEuler-RISC-V/testing/2403LTS-test/v1/lpi4a/
    - 参考安装文档：https://docs.openeuler.org/zh/docs/24.03_LTS/docs/Installation/RISC-V-LicheePi4A.html
- RevyOS 20231210
    - 下载链接：https://mirror.iscas.ac.cn/revyos/extra/images/lpi4a/
    - 参考安装文档：https://docs.revyos.dev/
- openKylin 2.0 alpha
    - 下载链接：https://www.openkylin.top/downloads/index-cn.html
    - 参考安装文档：https://docs.openkylin.top/zh/%E7%A4%BE%E5%8C%BA%E5%BC%80%E5%8F%91%E6%8C%87%E5%8D%97/riscv%E4%B8%8A%E5%AE%89%E8%A3%85openKylin
- Fedora 38
    - 下载链接：https://openkoji.iscas.ac.cn/pub/dl/riscv/T-Head/th1520_light/images/
    - 参考安装文档：https://fedoraproject.org/wiki/Architectures/RISC-V/T-Head
- Armbian (Ubuntu 20.04 LTS)
    - 下载链接：https://github.com/chainsx/armbian-riscv-build/tree/main
    - 参考安装文档：https://github.com/chainsx/armbian-riscv-build/blob/main/doc/licheepi-4a-install-guide_ch.md
- ArchLinux
    - 下载链接：[https://mirror.iscas.ac.cn/archriscv/images/](https://mirror.iscas.ac.cn/archriscv/images/)
    - 参考安装文档：[ArchWiki](https://wiki.archlinux.org/title/General_recommendations)
- Deepin preview 20240603
    - 下载链接：https://cdimage.deepin.com/RISC-V/preview-20240613-riscv64/deepin-23-beige-preview-riscv64-lpi4a-20240613-122949.tar.xz
    - 参考安装文档：https://cdimage.deepin.com/RISC-V/preview-20240517-riscv64/README.md
### 硬件开发板信息

- Lichee Pi 4A 16GB RAM + 128GB eMMC
- Lichee Pi 4A 8GB RAM + 32GB eMMC

## 测试结果

| 软件分类                  | 软件包名 | 测试结果（测试报告）          |
| ------------------------- | -------- | ----------------------------- |
| openEuler/Base 镜像启动   | N/A      | [成功][oERV]                  |
| openEuler/Xfce 镜像启动   | Xfce     | [成功][oERV]                  |
| RevyOS 桌面镜像启动       | N/A      | [成功][RevyOS]（官方支持）    |
| Fedora 桌面镜像启动       | N/A      | [成功][Fedora]（官方支持）    |
| openKylin 桌面镜像启动    | N/A      | [成功][openKylin]（官方支持） |
| Armbian (Ubuntu) 镜像启动 | N/A      | [成功][Armbian]               |
| OpenWRT 镜像启动          | N/A      | [成功][OpenWRT]               |
| ArchLinux 桌面镜像启动    | N/A      | [成功][ArchLinux]             |
| Deepin 桌面镜像启动       | N/A      | [成功][Deepin]                |

[oERV]: ./openEuler/README_zh.md
[RevyOS]: ./RevyOS/README_zh.md
[Fedora]: ./Fedora/README_zh.md
[Armbian]: ./Armbian/README_zh.md
[openKylin]: ./openKylin/README_zh.md
[OpenWRT]: ./OpenWRT/README_zh.md
[ArchLinux]: ./ArchLinux/README_zh.md
[Deepin]: ./Deepin/README_zh.md