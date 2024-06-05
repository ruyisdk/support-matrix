# OpenWRT Lichee Cluster 4A 版本测试报告

## 测试环境

### 操作系统信息

- 系统版本：OpenWRT
- 下载链接：[https://github.com/chainsx/openwrt-th1520/releases](https://github.com/chainsx/openwrt-th1520/releases)
- 参考安装文档：[https://github.com/chainsx/armbian-riscv-build/blob/main/doc/licheepi-4a-install-guide_zh.md](https://github.com/chainsx/armbian-riscv-build/blob/main/doc/licheepi-4a-install-guide_zh.md)
- fastboot 链接：
    - [https://pan.baidu.com/e/1xH56ZlewB6UOMlke5BrKWQ](https://pan.baidu.com/e/1xH56ZlewB6UOMlke5BrKWQ)
    - [https://mega.nz/folder/phoQlBTZ#cZeQ3qZ__pDvP94PT3_bGA](https://mega.nz/folder/phoQlBTZ#cZeQ3qZ__pDvP94PT3_bGA)


### 硬件信息

- Lichee Cluster 4A 8G / 16G
- DC 12V 电源
- USB-A to A
    - 或 LPi4A 底板
- microSD 卡一张
- 网络和网线（注意连接到 BMC 而非交换机）

## 安装步骤

*以下以刷写到集群中一号板为例*

### 刷写镜像

使用 `gzip` 解压镜像。
使用 `dd` 将镜像写入 microSD 卡。

```bash
gzip -d /path/to/openwrt.img.xz
sudo dd if=/path/to/openwrt.img of=/dev/your_device bs=1M status=progress
```


### 刷写 bootloader

此处使用上面下载的 u-boot。

```bash
sudo ./fastboot flash ram ./path/to/your/lpi4a-$(ram_size)-u-boot-with-spl.bin
sudo ./fastboot reboot
sleep 10
sudo ./fastboot flash uboot ./path/to/your/lpi4a-$(ram_size)-u-boot-with-spl.bin
```

### 登录系统

通过 SOL (Serial Over LAN) 登录系统。

BMC 默认用户名：`root`

BMC 默认密码：`0penBmc` **注意是 `0` 而不是 `O`**

通过 `ssh -p 2301 root@lichee-rv.local` 连接

初次启动自动进入 root 用户。

### 常见问题

若无法使用 USB，是因为 Linux 设备树需要 patch。[patch 下载](https://dl.sipeed.com/fileList/LICHEE/LicheeCluster4A/04_Firmware/lpi4a/src/linux/0001-arch-riscv-boot-dts-lpi4a-disable-i2c-io-expander-fo.patch)

## 预期结果

系统正常启动，能够通过 SOL (Serial Over LAN) 登录。

## 实际结果

系统正常启动，能够通过 SOL (Serial Over LAN) 登录。

### 启动信息

屏幕录像（从刷写系统到启动）：

[![asciicast](https://asciinema.org/a/z6gochTcLaWlL9m0f1Gj6vyoe.svg)](https://asciinema.org/a/z6gochTcLaWlL9m0f1Gj6vyoe)

```log
BusyBox v1.36.1 (2023-11-11 16:56:38 UTC) built-in shell (ash)


                              |/
                             _/_
    +-----------------+ ____  O
    |                 ||    \
    |                 ||     \     O     O
    |   ___   RISC-V  ||  ___ |   /|\_  /|\_
    +--/ o \----------++-/ o \+  _/ \  _/ \
       \___/             \___/
 -----------------------------------------------------
 OpenWrt SNAPSHOT, r0-707f69c
 -----------------------------------------------------
=== WARNING! =====================================
There is no root password defined on this device!
Use the "passwd" command to set up a new password
in order to prevent unauthorized SSH logins.
--------------------------------------------------
root@OpenWrt:/# uname pa
BusyBox v1.36.1 (2023-11-11 16:56:38 UTC) multi-call binary.

Usage: uname [-amnrspvio]

Print system information

        -a      Print all
        -m      Machine (hardware) type
        -n      Hostname
        -r      Kernel release
        -s      Kernel name (default)
        -p      Processor type
        -v      Kernel version
        -i      Hardware platform
        -o      OS name
root@OpenWrt:/# uname -a
Linux OpenWrt 5.10.113-g707f69c27511 #0 SMP PREEMPT Sat Nov 11 16:56:38 2023 riscv64 GNU/Linux
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
BUILD_ID="r0-707f69c"
OPENWRT_BOARD="thead/th1520"
OPENWRT_ARCH="riscv64_riscv64"
OPENWRT_TAINTS="no-all"
OPENWRT_DEVICE_MANUFACTURER="OpenWrt"
OPENWRT_DEVICE_MANUFACTURER_URL="https://openwrt.org/"
OPENWRT_DEVICE_PRODUCT="Generic"
OPENWRT_DEVICE_REVISION="v0"
OPENWRT_RELEASE="OpenWrt SNAPSHOT r0-707f69c"
root@OpenWrt:/# [   33.853164] soc_dovdd18_scan: disabling

```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。