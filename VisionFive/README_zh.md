# StarFive VisionFive

## 测试环境

### 操作系统信息

- Fedora
    - 下载链接：https://fedora.starfivetech.com/pub/downloads/VisionFive-release/Fedora-riscv64-jh7100-developer-xfce-Rawhide-20211226-214100.n.0-sda.raw.zst
  - 参考安装文档：https://doc.rvspace.org/VisionFive/PDF/VisionFive_Quick_Start_Guide.pdf
- openEuler
  - 下载链接：https://mirror.iscas.ac.cn/openeuler-sig-riscv/openEuler-RISC-V/preview/openEuler-23.09-V1-riscv64/Visionfive/
  - 参考安装文档：https://gitee.com/openeuler/RISC-V/tree/master/release/openEuler-23.03/Installation_Book/Visionfive
  - 下载链接：https://mirror.iscas.ac.cn/openeuler-sig-riscv/openEuler-RISC-V/preview/openEuler-23.09-V1-riscv64/Visionfive/
  - 参考安装文档：https://gitee.com/openeuler/RISC-V/tree/master/release/openEuler-23.03/Installation_Book/Visionfive
- Ubuntu
  - 下载链接：https://ubuntu.com/download/risc-v
  - 参考安装文档：https://wiki.ubuntu.com/RISC-V/StarFive%20VisionFive
- openKylin
  - 下载链接：https://www.openkylin.top/downloads/old_releases.html
  - 参考安装文档：https://docs.openkylin.top/zh/%E7%A4%BE%E5%8C%BA%E5%BC%80%E5%8F%91%E6%8C%87%E5%8D%97/riscv%E4%B8%8A%E5%AE%89%E8%A3%85openKylin
- openSUSE
  - 下载链接：https://download.opensuse.org/repositories/devel:/RISCV:/Factory:/Contrib:/StarFive/images/
  - 参考安装文档：https://en.opensuse.org/HCL:VisionFive
- Armbian
  - 下载链接：https://www.armbian.com/vision-five/
  - 参考安装文档：https://docs.armbian.com/User-Guide_Getting-Started/
- OpenWRT
  - 下载链接：https://firmware-selector.openwrt.org/?version=SNAPSHOT&target=starfive%2Fgeneric&id=visionfive-v1
  - 参考安装文档：https://openwrt.org/docs/techref/hardware/soc/soc.allwinner.starfive?s[]=visionfive
- OpenBSD
  - 下载链接：https://cdn.openbsd.org/pub/OpenBSD/snapshots/riscv64/
  - 参考安装文档：https://cdn.openbsd.org/pub/OpenBSD/snapshots/riscv64/INSTALL.riscv64
- Buildroot
  - 源码链接：https://buildroot.org/download.html
  - 参考安装文档：https://gitlab.com/buildroot.org/buildroot/-/tree/master/board/visionfive?ref_type=heads

### 硬件开发板信息

- StarFive VisionFive

## 测试结果

| 软件分类                 | 软件包名 | 测试结果（测试报告）       |
|----------------------|----------|------------------------|
| openEuler/Base 镜像启动  | N/A      | [成功][oERVBase]         |
| openEuler/Xfce 镜像启动  | N/A      | [成功][oERVXfce]         |
| Fedora 镜像启动          | N/A      | [成功][Fedora]（官方支持） |
| Ubuntu 镜像启动          | N/A      | [成功][Ubuntu]           |
| openKylin 镜像启动       | N/A      | [成功][oK]（官方支持）     |
| openSUSE 镜像启动        | N/A      | [成功][openSUSE]         |
| Armbian 镜像启动         | N/A      | [成功][Armbian]          |
| OpenWRT 镜像启动         | N/A      | [成功][OpenWRT]          |
| OpenBSD 镜像启动         | N/A      | [成功][OpenBSD]          |
| Buildroot 镜像构建及启动 | N/A      | [成功][Buildroot]        |

[oERVBase]: ./openEuler/README_zh.md
[oERVXfce]: ./openEuler/README_zh.md
[Fedora]: ./Fedora/README_zh.md
[Ubuntu]: ./Ubuntu/README_zh.md
[oK]: ./openKylin/README_zh.md
[openSUSE]: ./openSUSE/README_zh.md
[Armbian]: ./Armbian/README_zh.md
[OpenWRT]: ./OpenWRT/README_zh.md
[OpenBSD]: ./OpenBSD/README_zh.md
[Buildroot]: ./BuildRoot/README_zh.md