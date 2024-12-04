# OpenWrt 23.05.2 D1 测试报告

## 测试环境

### 操作系统信息

- 系统版本：OpenWrt 23.05.2
- 下载链接（OpenWrt Firmware Selector）：
  - Sipeed Lichee RV Dock: https://firmware-selector.openwrt.org/?version=SNAPSHOT&target=d1%2Fgeneric&id=lichee_rv_dock
- 参考安装文档：https://openwrt.org/docs/techref/hardware/soc/soc.allwinner.d1

> 在 OpenWrt Firmware Selector 中可以在线定制构建系统镜像，添加用户所需要的预装软件包。本次测试使用的为**未经修改**的原版镜像。

### 硬件信息

- Sipeed Lichee RV Dock
- USB-A 电源一个
- USB-A to C 线缆一条
- microSD 卡一张
- USB to UART 调试器一个（如：CH340, CH341, FT2232 等）
- 杜邦线三根

## 安装步骤

### 刷写镜像到 microSD 卡

使用 `dd` 刷入镜像到 microSD 卡。

```bash
xz -dkv openwrt-d1-lichee_rv_dock-squashfs-sdcard.img.gz
sudo dd if=openwrt-d1-lichee_rv_dock-squashfs-sdcard.img of=/dev/sdc status=progress
```

### 登录系统

通过串口登录系统。

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

系统正常启动，成功通过板载串口登录。

### 启动信息

```log
BusyBox v1.36.1 (2024-03-13 22:51:23 UTC) built-in shell (ash)

  _______                     ________        __
 |       |.-----.-----.-----.|  |  |  |.----.|  |_
 |   -   ||  _  |  -__|     ||  |  |  ||   _||   _|
 |_______||   __|_____|__|__||________||__|  |____|
          |__| W I R E L E S S   F R E E D O M
 -----------------------------------------------------
 OpenWrt SNAPSHOT, r25540-7b89388674
 -----------------------------------------------------
=== WARNING! =====================================
There is no root password defined on this device!
Use the "passwd" command to set up a new password
in order to prevent unauthorized SSH logins.
--------------------------------------------------
root@OpenWrt:/# uname -a
Linux OpenWrt 6.1.81 #0 SMP Wed Mar 13 22:51:23 2024 riscv64 GNU/Linux
root@OpenWrt:/# cat /proc/cpuinfo 
processor       : 0
hart            : 0
isa             : rv64imafdc
mmu             : sv39
uarch           : thead,c906
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0
```

屏幕录像（从刷写镜像到登录系统）：

[![asciicast](https://asciinema.org/a/FtuRf4hQ7gWi0lTR4JkBxXJMw.svg)](https://asciinema.org/a/FtuRf4hQ7gWi0lTR4JkBxXJMw)

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。
