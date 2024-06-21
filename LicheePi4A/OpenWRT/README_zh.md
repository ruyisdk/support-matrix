# OpenWRT LPi4A 测试报告

## 测试环境

### 系统信息

- 系统版本：OpenWRT
- 下载链接：[https://github.com/chainsx/openwrt-th1520/releases](https://github.com/chainsx/openwrt-th1520/releases)
- 参考安装文档：[https://github.com/chainsx/armbian-riscv-build/blob/main/doc/licheepi-4a-install-guide_ch.md](https://github.com/chainsx/armbian-riscv-build/blob/main/doc/licheepi-4a-install-guide_ch.md)
- fastboot 链接：
    - [https://pan.baidu.com/e/1xH56ZlewB6UOMlke5BrKWQ](https://pan.baidu.com/e/1xH56ZlewB6UOMlke5BrKWQ)
    - [https://mega.nz/folder/phoQlBTZ#cZeQ3qZ__pDvP94PT3_bGA](https://mega.nz/folder/phoQlBTZ#cZeQ3qZ__pDvP94PT3_bGA)

### 硬件信息

- Lichee Pi 4A (8G RAM + 64G eMMC)
- 电源适配器
- microSD 卡一张
- USB to UART 调试器一个

## 安装步骤

### 刷写镜像

使用 `gzip` 解压镜像。
使用 `dd` 将镜像写入 microSD 卡。

```bash
gzip -d /path/to/openwrt.img.xz
sudo dd if=/path/to/openwrt.img of=/dev/your_device bs=1M status=progress
```

### 刷写 bootloader

进入 fastboot。
- 正式版确认 boot 拨码开关为 eMMC。
- 按动 BOOT 同时上电。
- （详见官方教程）
使用 fastboot 按命令烧录 u-boot。

```bash
sudo ./fastboot flash ram ./path/to/your/lpi4a-$(ram_size)-u-boot-with-spl.bin
sudo ./fastboot reboot
sleep 10
sudo ./fastboot flash uboot ./path/to/your/lpi4a-$(ram_size)-u-boot-with-spl.bin
```

### 登录系统

通过串口登录系统。

初次启动自动进入 root 用户。

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

系统正常启动，成功通过板载串口登录。

### 启动信息

屏幕录像（从刷写镜像到登录系统）：

[![asciicast](https://asciinema.org/a/DNRiqiUpdDxlAWHnSkQTvqsNt.svg)](https://asciinema.org/a/DNRiqiUpdDxlAWHnSkQTvqsNt)

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
root@OpenWrt:/# 

```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。