# OpenWRT SnapShot VisionFive 测试报告

## 测试环境

### 系统信息

- 系统版本：OpenWRT SnapShot
- 下载链接：[https://firmware-selector.openwrt.org/?version=SNAPSHOT&target=starfive%2Fgeneric&id=visionfive-v1](https://firmware-selector.openwrt.org/?version=SNAPSHOT&target=starfive%2Fgeneric&id=visionfive-v1)
- 参考安装文档：[https://openwrt.org/docs/techref/hardware/soc/soc.allwinner.starfive?s[]=visionfive](https://openwrt.org/docs/techref/hardware/soc/soc.allwinner.starfive?s[]=visionfive)

### 硬件信息

- StarFive VisionFive
- 电源适配器
- microSD 卡一张
- USB to UART 调试器一个

## 安装步骤

### 刷写镜像

使用 `gzip` 解压镜像。
使用 `dd` 将镜像写入 microSD 卡。

```bash
wget https://downloads.openwrt.org/snapshots/targets/starfive/generic/openwrt-starfive-generic-visionfive-v1-ext4-sdcard.img.gz
gzip -d /path/to/openwrt.img.gz
sudo dd if=/path/to/openwrt.img of=/dev/your-device bs=1M status=progress
```

### 更新/引导 boot


若 u-boot 无法引导而是进入了命令行，需要更新 u-boot（详见：（pr 31）[https://github.com/starfive-tech/u-boot/pull/31]）：

官方文档：[https://starfivetech.com/uploads/VisionFive%20Single%20Board%20Computer%20Quick%20Start%20Guide.pdf](https://starfivetech.com/uploads/VisionFive%20Single%20Board%20Computer%20Quick%20Start%20Guide.pdf)

u-boot 下载：https://github.com/starfive-tech/Fedora_on_StarFive/releases

或者，手动输入以下命令以引导系统：

```u-boot
fatload mmc 0:3 0x84000000 Image
fatload mmc 0:3 0x88000000 dtb
setenv bootargs "earlyprintk console=ttyS0,115200 debug rootwait earlycon=sbi root=/dev/mmcblk0p4"
booti 0x84000000 - 0x88000000
```

### 登录系统

通过串口登录系统。

默认无密码，自动登录 root。

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

系统正常启动，成功通过板载串口登录。

### 启动信息

屏幕录像（从刷写镜像到登录系统）：

[![asciicast](https://asciinema.org/a/GwgQgY4G4s2PihEHoXxsLyjP9.svg)](https://asciinema.org/a/GwgQgY4G4s2PihEHoXxsLyjP9)

```log

BusyBox v1.36.1 (2024-03-25 10:02:16 UTC) built-in shell (ash)

  _______                     ________        __
 |       |.-----.-----.-----.|  |  |  |.----.|  |_
 |   -   ||  _  |  -__|     ||  |  |  ||   _||   _|
 |_______||   __|_____|__|__||________||__|  |____|
          |__| W I R E L E S S   F R E E D O M
 -----------------------------------------------------
 OpenWrt SNAPSHOT, r25661-bf4c04a4d0
 -----------------------------------------------------
=== WARNING! =====================================
There is no root password defined on this device!
Use the "passwd" command to set up a new password
in order to prevent unauthorized SSH logins.
--------------------------------------------------
root@OpenWrt:/# [   16.898199] starfive-dwmac 10020000.ethernet eth0: Register MEM_TYPE_PAGE_POOL RxQ-0
[   16.912314] starfive-dwmac 10020000.ethernet eth0: PHY [stmmac-0:00] driver [YT8521 Gigabit Ethernet] (irq=POLL)
[   16.932602] dwmac1000: Master AXI performs fixed burst length
[   16.938387] starfive-dwmac 10020000.ethernet eth0: No Safety Features support found
[   16.946043] starfive-dwmac 10020000.ethernet eth0: No MAC Management Counters available
[   16.954027] starfive-dwmac 10020000.ethernet eth0: IEEE 1588-2008 Advanced Timestamp supported
[   16.962864] starfive-dwmac 10020000.ethernet eth0: registered PTP clock
[   16.969491] starfive-dwmac 10020000.ethernet eth0: configuring for phy/rgmii-txid link mode
[   16.980763] br-lan: port 1(eth0) entered blocking state
[   16.986006] br-lan: port 1(eth0) entered disabled state
[   16.991454] device eth0 entered promiscuous mode

root@OpenWrt:/# uname -a
Linux OpenWrt 6.1.82 #0 SMP Mon Mar 25 10:02:16 2024 riscv64 GNU/Linux
root@OpenWrt:/# cat /etc/os-release 
NAME="OpenWrt"
VERSION="SNAPSHOT"
ID="openwrt"
ID_LIKE="lede openwrt"
PRETTY_NAME="OpenWrt SNAPSHOT"
VERSION_ID="snapshot"
HOME_URL="https://openwrt.org/"
BUG_URL="https://bugs.openwrt.org/"
SUPPORT_URL="https://forum.openwrt.org/"
BUILD_ID="r25661-bf4c04a4d0"
OPENWRT_BOARD="starfive/generic"
OPENWRT_ARCH="riscv64_riscv64"
OPENWRT_TAINTS=""
OPENWRT_DEVICE_MANUFACTURER="OpenWrt"
OPENWRT_DEVICE_MANUFACTURER_URL="https://openwrt.org/"
OPENWRT_DEVICE_PRODUCT="Generic"
OPENWRT_DEVICE_REVISION="v0"
OPENWRT_RELEASE="OpenWrt SNAPSHOT r25661-bf4c04a4d0"

```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。