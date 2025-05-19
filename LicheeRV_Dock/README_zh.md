# Lichee RV Dock

## 测试环境

### 操作系统信息

- openEuler RISC-V 23.03 Preview
  - 下载链接：[ISCAS Mirror][oERVDL]
    - 可选包含 Xfce 桌面的镜像或者仅提供命令行的 Base 镜像
  - 参考安装文档：[openEuler/RISC-V][oERVXfce]
- Tina Linux
  - 下载链接：
    - Sipeed Lichee RV: https://wiki.sipeed.com/hardware/zh/lichee/RV/flash.html
  - 参考安装文档：
    - Sipeed Lichee RV: https://wiki.sipeed.com/hardware/zh/lichee/RV/flash.html
- Ubuntu 
  - 25.04 下载链接: https://ubuntu.com/download/risc-v
  - 24.04.2 LTS 下载链接: https://ubuntu.com/download/risc-v
  - 参考安装文档：https://wiki.ubuntu.com/RISC-V/LicheeRVhttps://canonical-ubuntu-boards.readthedocs-hosted.com/en/latest/how-to/sipeed-licheerv-dock/
- OpenWrt 23.05.2
  - 下载链接（OpenWrt Firmware Selector）：
    - Sipeed Lichee RV Dock: https://firmware-selector.openwrt.org/?version=SNAPSHOT&target=d1%2Fgeneric&id=lichee_rv_dock
  - 参考安装文档：https://openwrt.org/docs/techref/hardware/soc/soc.allwinner.d1
- Debian
  - 下载链接：https://mega.nz/folder/lx4CyZBA#PiFhY7oSVQ3gp2ZZ_AnwYA
  - 参考安装文档：https://wiki.sipeed.com/hardware/zh/lichee/RV/flash.html
- Arch Linux
  - 基础镜像：Ubuntu 24.10: [ubuntu-24.10](https://ubuntu.com/download/risc-v) 
    - 或任意 D1 的镜像
    - Rootfs：[archriscv-2024-09-22.tar.zst](https://archriscv.felixc.at/images/archriscv-2024-09-22.tar.zst)
    - 参考安装文档：https://github.com/felixonmars/archriscv-packages/wiki/RV64-%E6%9D%BF%E5%AD%90%E6%9B%B4%E6%8D%A2-rootfs-%E6%8C%87%E5%8D%97
- openSUSE Tumbleweed
  - 下载链接：[https://download.opensuse.org/repositories/devel:/RISCV:/Factory:/Contrib:/AllwinnerD1/images/](https://download.opensuse.org/repositories/devel:/RISCV:/Factory:/Contrib:/AllwinnerD1/images/)
  - 参考安装文档：[https://en.opensuse.org/HCL:Nezha](https://en.opensuse.org/HCL:Nezha)
- NixOS
  - 下载链接：https://github.com/chuangzhu/nixos-sun20iw1p1/releases
  - 参考安装文档:https://github.com/chuangzhu/nixos-sun20iw1p1
- irradium
  - 下载链接: https://dl.irradium.org/irradium/images/lichee_rv_dock/
  - 参考安装文档: https://dl.irradium.org/irradium/images/lichee_rv_dock/README.TXT

### 硬件开发板信息

- Sipeed Lichee RV Dock

## 测试结果

| 软件分类                | 软件包名     | 测试结果（测试报告）          |
|-------------------------|--------------|-------------------------------|
| openEuler/Base 镜像启动 | N/A          | [成功][oERV]                  |
| openEuler/Xfce 镜像启动 | Xfce Desktop | [成功][oERV]                  |
| Tina-Linux 镜像启动     | N/A          | [成功][TinaNezha]（官方支持） |
| Ubuntu 镜像启动         | N/A          | [CFT][Ubuntu]（官方支持）     |
| Ubuntu LTS 镜像启动     | N/A          | [CFT][Ubuntu-LTS]（官方支持） |
| OpenWrt 镜像启动        | N/A          | [成功][OpenWrt]（官方支持）   |
| Debian 镜像启动         | N/A          | [成功][Debian]                |
| openSUSE 镜像启动       | N/A          | [成功][openSUSE]              |
| Arch Linux 镜像启动     | N/A          | [成功][Arch]                  |
| NixOS 镜像启动          | N/A          | [成功][NixOS]                 |
| irradium 镜像启动       | N/A          | [成功][irradium]              |

[oERVDL]: https://mirror.iscas.ac.cn/openeuler-sig-riscv/openEuler-RISC-V/preview/openEuler-23.03-V1-riscv64/D1/
[oERV]: ./openEuler/README_zh.md
[TinaNezha]: ./TinaLinux/README_zh.md
[Ubuntu]: ./Ubuntu/README_zh.md
[Ubuntu-LTS]: ./Ubuntu/README_LTS_zh.md
[OpenWrt]: ./OpenWrt/README_zh.md
[Debian]: ./Debian/README_zh.md
[openSUSE]: ./openSUSE/README_zh.md
[Arch]: ./ArchLinux/README_zh.md
[NixOS]: ./NixOS/README_zh.md
[irradium]: ./irradium/README_zh.md
