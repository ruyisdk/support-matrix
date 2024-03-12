# LicheeRV / AWOL Nezha D1

## 测试环境

### 操作系统信息

- openEuler RISC-V 23.03 Preview
  - 下载链接：https://mirror.iscas.ac.cn/openeuler-sig-riscv/openEuler-RISC-V/preview/openEuler-23.03-V1-riscv64/D1/
    - 可选包含 Xfce 桌面的镜像或者仅提供命令行的 Base 镜像
  - 参考安装文档：https://gitee.com/openeuler/RISC-V/tree/master/release/openEuler-23.03/Installation_Book/D1_and_Licheerv
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

| 软件分类                | 软件包名     | 测试结果（测试报告） |
|---------------------|--------------|------------------|
| openEuler/Base 镜像启动 | N/A          | [成功][oERVBase]   |
| openEuler/Xfce 镜像启动 | Xfce Desktop | [成功][oERVXfce]   |
| Tina-Linux 镜像启动     | N/A          | 成功（官方支持）     |
| Ubuntu 镜像启动         | N/A          | 成功（官方支持）     |
| OpenWrt 镜像启动        | N/A          | 成功（官方支持）     |

[oERVBase]: https://gitee.com/yunxiangluo/ruyisdk-test/blob/master/20240130/D1-%E9%95%9C%E5%83%8F%E5%88%B7%E5%86%99%E6%B5%8B%E8%AF%95.md
[oERVXfce]: https://gitee.com/openeuler/RISC-V/tree/master/release/openEuler-23.03/Installation_Book/D1_and_Licheerv