# OpenWrt 24.10.0 HiFive Unmatched 测试报告

## 测试环境

### 操作系统信息

- 系统版本：OpenWrt 24.10.0
- 下载链接（OpenWrt Firmware Selector）：https://firmware-selector.openwrt.org/?version=24.10.0&target=sifiveu%2Fgeneric&id=sifive_unmatched
- 参考安装文档：https://openwrt.org/docs/techref/hardware/soc/soc.sifive

> 在 OpenWrt Firmware Selector 中可以在线定制构建系统镜像，添加用户所需要的预装软件包。本次测试使用的为**未经修改**的原版镜像。

### 硬件信息

- HiFive Unmatched Rev A
- microUSB 线缆一条（随 HiFive Unmatched 附赠）
- ATX 电源一个
- microSD 卡一张

## 安装步骤

### 引导设备选择

确保拨码开关已调整为从 microSD 卡引导。若您未更改，出厂默认即为从 microSD 卡引导。

拨码开关应如下设置：`MSEL[3:0]=1011`

### 使用 dd 刷写镜像到 microSD 卡

`/dev/sdX` 为 microSD 卡，请根据实际情况修改。

```shell
wget https://downloads.openwrt.org/releases/24.10.0/targets/sifiveu/generic/openwrt-24.10.0-sifiveu-generic-sifive_unmatched-ext4-sdcard.img.gz
gzip -d openwrt-24.10.0-sifiveu-generic-sifive_unmatched-ext4-sdcard.img.gz
sudo dd if=openwrt-24.10.0-sifiveu-generic-sifive_unmatched-ext4-sdcard.img of=/dev/sdX bs=1M status=progress; sync
sudo eject /dev/sdX
```

### 登录系统

通过板载串口（使用 microUSB 线缆连接至其他计算机）登录系统。

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

系统正常启动，成功通过板载串口登录。

### 启动信息

```log
BusyBox v1.36.1 (2025-02-03 23:09:37 UTC) built-in shell (ash)

  _______                     ________        __
 |       |.-----.-----.-----.|  |  |  |.----.|  |_
 |   -   ||  _  |  -__|     ||  |  |  ||   _||   _|
 |_______||   __|_____|__|__||________||__|  |____|
          |__| W I R E L E S S   F R E E D O M
 -----------------------------------------------------
 OpenWrt 24.10.0, r28427-6df0e3d02a
 -----------------------------------------------------
=== WARNING! =====================================
There is no root password defined on this device!
Use the "passwd" command to set up a new password
in order to prevent unauthorized SSH logins.
--------------------------------------------------
root@OpenWrt:~# cat /etc/os-release
NAME="OpenWrt"
VERSION="24.10.0"
ID="openwrt"
ID_LIKE="lede openwrt"
PRETTY_NAME="OpenWrt 24.10.0"
VERSION_ID="24.10.0"
HOME_URL="https://openwrt.org/"
BUG_URL="https://bugs.openwrt.org/"
SUPPORT_URL="https://forum.openwrt.org/"
BUILD_ID="r28427-6df0e3d02a"
OPENWRT_BOARD="sifiveu/generic"
OPENWRT_ARCH="riscv64_riscv64"
OPENWRT_TAINTS=""
OPENWRT_DEVICE_MANUFACTURER="OpenWrt"
OPENWRT_DEVICE_MANUFACTURER_URL="https://openwrt.org/"
OPENWRT_DEVICE_PRODUCT="Generic"
OPENWRT_DEVICE_REVISION="v0"
OPENWRT_RELEASE="OpenWrt 24.10.0 r28427-6df0e3d02a"
OPENWRT_BUILD_DATE="1738624177"
root@OpenWrt:~# cat /etc/openwrt_
openwrt_release  openwrt_version
root@OpenWrt:~# cat /etc/openwrt_version
r28427-6df0e3d02a
root@OpenWrt:~# cat /etc/openwrt_release
DISTRIB_ID='OpenWrt'
DISTRIB_RELEASE='24.10.0'
DISTRIB_REVISION='r28427-6df0e3d02a'
DISTRIB_TARGET='sifiveu/generic'
DISTRIB_ARCH='riscv64_riscv64'
DISTRIB_DESCRIPTION='OpenWrt 24.10.0 r28427-6df0e3d02a'
DISTRIB_TAINTS=''
root@OpenWrt:~# uname -a
Linux OpenWrt 6.6.73 #0 SMP Mon Feb  3 23:09:37 2025 riscv64 GNU/Linux
root@OpenWrt:~# cat /proc/cpuinfo
processor       : 0
hart            : 4
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x20181004

processor       : 1
hart            : 1
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x20181004

processor       : 2
hart            : 2
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x20181004

processor       : 3
hart            : 3
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x20181004

root@OpenWrt:~#
```

屏幕录像：

[![asciicast](https://asciinema.org/a/kWBM8bOzlgglxaWfDXBe9fEiQ.svg)](https://asciinema.org/a/kWBM8bOzlgglxaWfDXBe9fEiQ)

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。