# OpenWRT Milk-V Mars 测试报告

## 测试环境

### 硬件信息

- 开发板：Milk-V Mars (8GB RAM)
- 其他硬件：
  - USB 电源适配器和USB-A to C 或 C to C 线缆一条
  - microSD 卡一张
  - USB to UART 调试器一个（如：CH340, CH341, FT2232 等）

### 操作系统信息

- 操作系统版本：OpenWRT 24.10.1 (Build ID: r28597-0425664679)
- 下载链接：<https://downloads.openwrt.org/releases/24.10.1/targets/starfive/generic/openwrt-24.10.1-starfive-generic-visionfive2-v1.3b-ext4-sdcard.img.gz>
- 参考安装文档：
  - <https://milkv.io/zh/docs/mars/getting-started/boot>
  - <https://doc.rvspace.org/VisionFive2/Application_Notes/VisionFive2_OpenWrt/VisionFive_2/openwrt/compile.html>
  - <https://firmware-selector.openwrt.org/?version=24.10.1&target=starfive%2Fgeneric&id=visionfive2-v1.3b>

## 安装步骤

### 刷写镜像

使用 `gzip` 命令解压镜像，并使用 `dd` 命令或 `balenaEtcher` 软件将镜像写入 microSD 卡。

其中，`/dev/sdc` 为存储卡对应设备。

```bash
wget https://downloads.openwrt.org/releases/24.10.1/targets/starfive/generic/openwrt-24.10.1-starfive-generic-visionfive2-v1.3b-ext4-sdcard.img.gz

gzip -d openwrt-24.10.1-starfive-generic-visionfive2-v1.3b-ext4-sdcard.img.gz

sudo dd if=openwrt-24.10.1-starfive-generic-visionfive2-v1.3b-ext4-sdcard.img of=/dev/sdc bs=1M status=progress

sync
```

### 登录系统

通过串口登录系统。

默认用户名： `root` (自动登录)

默认无密码

由于镜像没有SPL和U-Boot，所以需要将板子的拨码开关设置为 `00`，以此来使用板上SPI-Flash中内置的SPL和U-Boot来引导启动MicroSD卡中的OpenWRT镜像。

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

系统正常启动，成功通过串口查看输出。

### 启动信息

```log
BusyBox v1.36.1 (2025-04-13 16:38:32 UTC) built-in shell (ash)

  _______                     ________        __
 |       |.-----.-----.-----.|  |  |  |.----.|  |_
 |   -   ||  _  |  -__|     ||  |  |  ||   _||   _|
 |_______||   __|_____|__|__||________||__|  |____|
          |__| W I R E L E S S   F R E E D O M
 -----------------------------------------------------
 OpenWrt 24.10.1, r28597-0425664679
 -----------------------------------------------------
=== WARNING! =====================================
There is no root password defined on this device!
Use the "passwd" command to set up a new password
in order to prevent unauthorized SSH logins.
--------------------------------------------------
root@OpenWrt:~# 

root@OpenWrt:~# cat /etc/os-release
NAME="OpenWrt"
VERSION="24.10.1"
ID="openwrt"
ID_LIKE="lede openwrt"
PRETTY_NAME="OpenWrt 24.10.1"
VERSION_ID="24.10.1"
HOME_URL="https://openwrt.org/"
BUG_URL="https://bugs.openwrt.org/"
SUPPORT_URL="https://forum.openwrt.org/"
BUILD_ID="r28597-0425664679"
OPENWRT_BOARD="starfive/generic"
OPENWRT_ARCH="riscv64_riscv64"
OPENWRT_TAINTS=""
OPENWRT_DEVICE_MANUFACTURER="OpenWrt"
OPENWRT_DEVICE_MANUFACTURER_URL="https://openwrt.org/"
OPENWRT_DEVICE_PRODUCT="Generic"
OPENWRT_DEVICE_REVISION="v0"
OPENWRT_RELEASE="OpenWrt 24.10.1 r28597-0425664679"
OPENWRT_BUILD_DATE="1744562312"

root@OpenWrt:~# uname -a
Linux OpenWrt 6.6.86 #0 SMP Sun Apr 13 16:38:32 2025 riscv64 GNU/Linux

root@OpenWrt:~# cat /proc/cpuinfo
processor       : 0
hart            : 1
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zba_zbb
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x4210427

processor       : 1
hart            : 2
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zba_zbb
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x4210427

processor       : 2
hart            : 3
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zba_zbb
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x4210427

processor       : 3
hart            : 4
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zba_zbb
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x4210427
```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功
