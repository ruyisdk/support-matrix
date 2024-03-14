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
  - 参考安装文档：
    - Nezha D1: https://wiki.ubuntu.com/RISC-V/Nezha%20D1
    - Sipeed Lichee RV Dock: https://wiki.ubuntu.com/RISC-V/LicheeRV
- OpenWrt
  - 下载链接（OpenWrt Firmware Selector）：
    - Nezha D1: https://firmware-selector.openwrt.org/?version=SNAPSHOT&target=d1%2Fgeneric&id=nezha
    - Sipeed Lichee RV Dock: https://firmware-selector.openwrt.org/?version=SNAPSHOT&target=d1%2Fgeneric&id=lichee_rv_dock
  - 参考安装文档：https://openwrt.org/docs/techref/hardware/soc/soc.allwinner.d1

### 硬件开发板信息

- Sipeed Lichee RV Dock
- AWOL Nezha D1

## 测试结果

| 软件分类                       | 软件包名     | 测试结果（测试报告）          |
|----------------------------|--------------|---------------------------|
| openEuler/Base 镜像启动        | N/A          | [成功][oERVBase]            |
| openEuler/Xfce 镜像启动        | Xfce Desktop | [成功][oERVXfce]            |
| Tina-Linux 镜像启动 - Nezha D1 | N/A          | [成功][TinaNezha]（官方支持） |
| Ubuntu 镜像启动                | N/A          | [成功][Ubuntu]（官方支持）    |
| Ubuntu 镜像启动                | N/A          | [成功][Ubuntu]（官方支持）    |
| OpenWrt 镜像启动               | N/A          | [成功][OpenWrt]（官方支持）   |

[oERVDL]: https://mirror.iscas.ac.cn/openeuler-sig-riscv/openEuler-RISC-V/preview/openEuler-23.03-V1-riscv64/D1/
[oERVBase]: ./openEuler/README.md
[oERVXfce]: https://gitee.com/openeuler/RISC-V/tree/master/release/openEuler-23.03/Installation_Book/D1_and_Licheerv
[TinaNezha]: https://d1.docs.aw-ol.com/study/study_1tina/
[Ubuntu]: ./Ubuntu/README.md
[OpenWrt]: ./OpenWrt/README.md