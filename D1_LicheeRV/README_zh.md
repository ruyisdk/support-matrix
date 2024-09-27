# LicheeRV / AWOL Nezha D1

## 测试环境

### 操作系统信息

- openEuler RISC-V 23.03 Preview
  - 下载链接：[ISCAS Mirror][oERVDL]
    - 可选包含 Xfce 桌面的镜像或者仅提供命令行的 Base 镜像
  - 参考安装文档：[openEuler/RISC-V][oERVXfce]
- Tina Linux
  - 下载链接：
    - Nezha D1: https://d1.docs.aw-ol.com/source/3_getimg/
    - Sipeed Lichee RV: https://wiki.sipeed.com/hardware/zh/lichee/RV/flash.html
  - 参考安装文档：
    - Nezha D1: https://d1.docs.aw-ol.com/study/study_1tina/
    - Sipeed Lichee RV: https://wiki.sipeed.com/hardware/zh/lichee/RV/flash.html
- Ubuntu
  - 下载链接：https://ubuntu.com/download/risc-v
    - 镜像源： [Nezha](https://mirror.tuna.tsinghua.edu.cn/ubuntu-cdimage/releases/24.10/beta/ubuntu-24.10-beta-preinstalled-server-riscv64%2Bnezha.img.xz) | [Lichee RV](https://mirror.tuna.tsinghua.edu.cn/ubuntu-cdimage/releases/24.10/beta/ubuntu-24.10-beta-preinstalled-server-riscv64%2Blicheerv.img.xz)
  - 参考安装文档：
    - Nezha D1: https://wiki.ubuntu.com/RISC-V/Nezha%20D1
    - Sipeed Lichee RV Dock: https://wiki.ubuntu.com/RISC-V/LicheeRV
- OpenWrt 23.05.2
  - 下载链接（OpenWrt Firmware Selector）：
    - Nezha D1: https://firmware-selector.openwrt.org/?version=SNAPSHOT&target=d1%2Fgeneric&id=nezha
    - Sipeed Lichee RV Dock: https://firmware-selector.openwrt.org/?version=SNAPSHOT&target=d1%2Fgeneric&id=lichee_rv_dock
  - 参考安装文档：https://openwrt.org/docs/techref/hardware/soc/soc.allwinner.d1
- Debian
  - 下载链接：http://www.perfxlab.cn:8080/rvboards/
  - 参考安装文档：https://d1.docs.aw-ol.com/strong/strong_4debian/#v041
- Fedora 36
  - 下载链接：https://openkoji.iscas.ac.cn/pub/dl/riscv/Allwinner/Nezha_D1/images-release/Fedora/
  - 参考安装文档：https://fedoraproject.org/wiki/Architectures/RISC-V/Allwinner/zh-cn
- Arch Linux
  - 基础镜像：Ubuntu 24.10 Beta: [ubuntu-24.10-beta-preinstalled-server-riscv64%2Bnezha.img.xz](https://mirror.tuna.tsinghua.edu.cn/ubuntu-cdimage/releases/24.10/beta/ubuntu-24.10-beta-preinstalled-server-riscv64%2Bnezha.img.xz) 
    - 或任意 D1 的镜像
  - Rootfs：[archriscv-20220727.tar.zst](https://archriscv.felixc.at/images/archriscv-20220727.tar.zst)
  - 参考安装文档：https://github.com/felixonmars/archriscv-packages/wiki/RV64-%E6%9D%BF%E5%AD%90%E6%9B%B4%E6%8D%A2-rootfs-%E6%8C%87%E5%8D%97
  h
- openSUSE Tumbleweed
  - 下载链接：[https://download.opensuse.org/repositories/devel:/RISCV:/Factory:/Contrib:/AllwinnerD1/images/](https://download.opensuse.org/repositories/devel:/RISCV:/Factory:/Contrib:/AllwinnerD1/images/)
  - 参考安装文档：[https://en.opensuse.org/HCL:Nezha](https://en.opensuse.org/HCL:Nezha)

### 硬件开发板信息

- Sipeed Lichee RV Dock
- AWOL Nezha D1

## 测试结果

| 软件分类                       | 软件包名     | 测试结果（测试报告）          |
| ------------------------------ | ------------ | ----------------------------- |
| openEuler/Base 镜像启动        | N/A          | [成功][oERV]                  |
| openEuler/Xfce 镜像启动        | Xfce Desktop | [成功][oERV]                  |
| Tina-Linux 镜像启动 - Nezha D1 | N/A          | [成功][TinaNezha]（官方支持） |
| Ubuntu 镜像启动                | N/A          | [成功][Ubuntu]（官方支持）    |
| OpenWrt 镜像启动               | N/A          | [成功][OpenWrt]（官方支持）   |
| Debian 镜像启动                | N/A          | [成功][Debian]                |
| Fedora 镜像启动                | N/A          | [成功][Fedora]                |
| openSUSE 镜像启动              | N/A          | [成功][openSUSE]              |
| Arch Linux 镜像启动            | N/A          | [成功][Arch]                  |

[oERVDL]: https://mirror.iscas.ac.cn/openeuler-sig-riscv/openEuler-RISC-V/preview/openEuler-23.03-V1-riscv64/D1/
[oERV]: ./openEuler/README_zh.md
[TinaNezha]: ./TinaLinux/README_zh.md
[Ubuntu]: ./Ubuntu/README_zh.md
[OpenWrt]: ./OpenWrt/README_zh.md
[Debian]: ./Debian/README_zh.md
[Fedora]: ./Fedora/README_zh.md
[openSUSE]: ./openSUSE/README_zh.md
[Arch]: ./ArchLinux/README_zh.md