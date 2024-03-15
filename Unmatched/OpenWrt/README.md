# OpenWrt 23.05.2 HiFive Unmatched 测试报告

## 测试环境

### 操作系统信息

- 系统版本：OpenWrt 23.05.2
- 下载链接（OpenWrt Firmware Selector）：https://firmware-selector.openwrt.org/?version=23.05.2&target=sifiveu%2Fgeneric&id=sifive_unmatched
- 参考安装文档：https://openwrt.org/docs/techref/hardware/soc/soc.sifive

> 在 OpenWrt Firmware Selector 中可以在线定制构建系统镜像，添加用户所需要的预装软件包。本次测试使用的 & `ruyi` 包管理器提供的为**未经修改**的原版镜像。

### 硬件信息

- HiFive Unmatched Rev A
- microUSB 线缆一条（随 HiFive Unmatched 附赠）
- ATX 电源一个
- microSD 卡一张（Sandisk Extreme Pro 64G UHS-I）

## 安装步骤

### 引导设备选择

确保拨码开关已调整为从 microSD 卡引导。若您未更改，出厂默认即为从 microSD 卡引导。

拨码开关应如下设置：`MSEL[3:0]=1011`

### 使用 `ruyi` CLI 刷写镜像到 microSD 卡

安装 [`ruyi`](https://github.com/ruyisdk/ruyi) 包管理器，运行 `ruyi device provision` 并按提示操作。

### 登录系统

通过板载串口（使用 microUSB 线缆连接至其他计算机）登录系统。

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

系统正常启动，成功通过板载串口登录。

### 启动信息

```log
[    3.585478] init: - preinit -
[    4.187220] random: jshn: uninitialized urandom read (4 bytes read)
[    4.211546] random: jshn: uninitialized urandom read (4 bytes read)
[    4.227475] random: jshn: uninitialized urandom read (4 bytes read)
[    4.276587] macb 10090000.ethernet eth0: PHY [10090000.ethernet-ffffffff:00] driver [Generic PHY] (irq=POLL)
[    4.285668] macb 10090000.ethernet eth0: configuring for phy/gmii link mode
Press the [f] key and hit [enter] to enter failsafe mode
Press the [1], [2], [3] or [4] key and hit [enter] to select the debug level
[    6.372369] mount_root: mounting /dev/root
[    6.385001] EXT4-fs (mmcblk0p4): re-mounted. Opts: (null). Quota mode: disabled.
[    6.442366] urandom-seed: Seed file not found (/etc/urandom.seed)
[    6.496980] procd: - early -
[    7.136220] procd: - ubus -
[    7.169138] random: ubusd: uninitialized urandom read (4 bytes read)
[    7.187663] random: ubusd: uninitialized urandom read (4 bytes read)
[    7.193446] random: ubusd: uninitialized urandom read (4 bytes read)
[    7.200886] procd: - init -
Please press Enter to activate this console.
[    7.526267] kmodloader: loading kernel modules from /etc/modules.d/*
[    7.540236] i2c_dev: i2c /dev entries driver
[    7.609264] hwmon hwmon0: temp1_input not attached to any thermal zone
[    7.615055] hwmon hwmon0: temp2_input not attached to any thermal zone
[    7.956942] PPP generic driver version 2.4.2
[    7.961025] NET: Registered PF_PPPOX protocol family
[    7.969043] kmodloader: done loading kernel modules from /etc/modules.d/*
[    8.000916] urngd: v1.0.2 started.
[    8.187850] random: crng init done
[    8.190467] random: 24 urandom warning(s) missed due to ratelimiting
[   14.796276] macb 10090000.ethernet eth0: PHY [10090000.ethernet-ffffffff:00] driver [Generic PHY] (irq=POLL)
[   14.805440] macb 10090000.ethernet eth0: configuring for phy/gmii link mode
[   14.813676] br-lan: port 1(eth0) entered blocking state
[   14.818128] br-lan: port 1(eth0) entered disabled state
[   14.823658] device eth0 entered promiscuous mode



BusyBox v1.36.1 (2023-11-14 13:38:11 UTC) built-in shell (ash)

  _______                     ________        __
 |       |.-----.-----.-----.|  |  |  |.----.|  |_
 |   -   ||  _  |  -__|     ||  |  |  ||   _||   _|
 |_______||   __|_____|__|__||________||__|  |____|
          |__| W I R E L E S S   F R E E D O M
 -----------------------------------------------------
 OpenWrt 23.05.2, r23630-842932a63d
 -----------------------------------------------------
=== WARNING! =====================================
There is no root password defined on this device!
Use the "passwd" command to set up a new password
in order to prevent unauthorized SSH logins.
--------------------------------------------------
root@OpenWrt:/# cat /etc/o
odhcp6c.user     openwrt_release  opkg.conf        os-release
odhcp6c.user.d/  openwrt_version  opkg/
root@OpenWrt:/# cat /etc/os-release 
NAME="OpenWrt"
VERSION="23.05.2"
ID="openwrt"
ID_LIKE="lede openwrt"
PRETTY_NAME="OpenWrt 23.05.2"
VERSION_ID="23.05.2"
HOME_URL="https://openwrt.org/"
BUG_URL="https://bugs.openwrt.org/"
SUPPORT_URL="https://forum.openwrt.org/"
BUILD_ID="r23630-842932a63d"
OPENWRT_BOARD="sifiveu/generic"
OPENWRT_ARCH="riscv64_riscv64"
OPENWRT_TAINTS=""
OPENWRT_DEVICE_MANUFACTURER="OpenWrt"
OPENWRT_DEVICE_MANUFACTURER_URL="https://openwrt.org/"
OPENWRT_DEVICE_PRODUCT="Generic"
OPENWRT_DEVICE_REVISION="v0"
OPENWRT_RELEASE="OpenWrt 23.05.2 r23630-842932a63d"
root@OpenWrt:/# cat /proc/cpuinfo 
processor       : 0
hart            : 1
isa             : rv64imafdc
mmu             : sv39
uarch           : sifive,u74-mc
                                                                        
processor       : 1                                                       
hart            : 2                                                     
isa             : rv64imafdc                                            
mmu             : sv39
uarch           : sifive,u74-mc

processor       : 2
hart            : 3
isa             : rv64imafdc
mmu             : sv39
uarch           : sifive,u74-mc

processor       : 3
hart            : 4
isa             : rv64imafdc
mmu             : sv39
uarch           : sifive,u74-mc

root@OpenWrt:/#
```

屏幕录像（从刷写镜像到登录系统）：

[![asciicast](https://asciinema.org/a/cAMBxvAP8iqIrdf1xCiQ3clJP.svg)](https://asciinema.org/a/cAMBxvAP8iqIrdf1xCiQ3clJP)

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。