# OpenWRT SnapShot VisionFive 2 测试报告

## 测试环境

### 系统信息

- 系统版本：OpenWRT SnapShot
- 下载链接：[https://firmware-selector.openwrt.org/?version=SNAPSHOT&target=starfive%2Fgeneric&id=visionfive2-v1.3b](https://firmware-selector.openwrt.org/?version=SNAPSHOT&target=starfive%2Fgeneric&id=visionfive2-v1.3b)
- 参考安装文档：[https://doc.rvspace.org/VisionFive2/Application_Notes/VisionFive2_OpenWrt/VisionFive_2/openwrt/compile.html](https://doc.rvspace.org/VisionFive2/Application_Notes/VisionFive2_OpenWrt/VisionFive_2/openwrt/compile.html)

### 硬件信息

- StarFive VisionFive2
- 电源适配器
- microSD 卡一张
- USB to UART 调试器一个

## 安装步骤

### 刷写镜像

使用 `gzip` 解压镜像。
使用 `dd` 将镜像写入 microSD 卡。

```bash
wget https://downloads.openwrt.org/snapshots/targets/starfive/generic/openwrt-starfive-generic-visionfive2-v1.3b-ext4-sdcard.img.gz
gzip -d /path/to/openwrt.img.gz
sudo dd if=/path/to/openwrt.img of=/dev/your-device bs=1M status=progress
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

[![asciicast](https://asciinema.org/a/cNB8FumIO4mB00Ppi1OoMCFyq.svg)](https://asciinema.org/a/cNB8FumIO4mB00Ppi1OoMCFyq)

```log
BusyBox v1.36.1 (2024-03-25 22:00:37 UTC) built-in shell (ash)

  _______                     ________        __
 |       |.-----.-----.-----.|  |  |  |.----.|  |_
 |   -   ||  _  |  -__|     ||  |  |  ||   _||   _|
 |_______||   __|_____|__|__||________||__|  |____|
          |__| W I R E L E S S   F R E E D O M
 -----------------------------------------------------
 OpenWrt SNAPSHOT, r25665-79e9ce354e
 -----------------------------------------------------
=== WARNING! =====================================
There is no root password defined on this device!
Use the "passwd" command to set up a new password
in order to prevent unauthorized SSH logins.
--------------------------------------------------
root@OpenWrt:/# uname -a
Linux OpenWrt 6.1.82 #0 SMP Mon Mar 25 22:00:37 2024 riscv64 GNU/Linux
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
BUILD_ID="r25665-79e9ce354e"
OPENWRT_BOARD="starfive/generic"
OPENWRT_ARCH="riscv64_riscv64"
OPENWRT_TAINTS=""
OPENWRT_DEVICE_MANUFACTURER="OpenWrt"
OPENWRT_DEVICE_MANUFACTURER_URL="https://openwrt.org/"
OPENWRT_DEVICE_PRODUCT="Generic"
OPENWRT_DEVICE_REVISION="v0"
OPENWRT_RELEASE="OpenWrt SNAPSHOT r25665-79e9ce354e"
root@OpenWrt:/# 
```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。