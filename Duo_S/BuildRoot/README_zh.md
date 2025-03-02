# BuildRoot Milk-V Duo S 测试报告

## 测试环境

### 操作系统信息

- 系统版本：DuoS-V2.0.0 (musl   版本)
- 下载链接：https://github.com/milkv-duo/duo-buildroot-sdk-v2/releases/
- 参考安装文档：https://github.com/milkv-duo/duo-buildroot-sdk-v2

### 硬件信息

- Milk-V Duo S (512M, SG2000)
- USB 电源适配器一个
- USB-A to C 或 USB C to C 线缆一条，用于给开发板供电
- microSD 卡一张
- USB 读卡器一个
- USB to UART 调试器一个（如：CP2102, FT2232 等，注意不可使用 CH340/341 系列，会出现乱码）
- 杜邦线三根

## 安装步骤

###  下载 Duo S 镜像并解压

```bash
wget https://github.com/milkv-duo/duo-buildroot-sdk-v2/releases/download/v2.0.0/milkv-duos-musl-riscv64-sd_v2.0.0.img.zip
unzip milkv-duos-musl-riscv64-sd_v2.0.0.img.zip
```

###  刷写镜像

使用 `dd` 命令将镜像刷写到 SD 卡：

```bash
sudo dd if=milkv-duos-musl-riscv64-sd_v2.0.0.img of=/dev/your/device bs=1M status=progress
```

### 登录系统

通过串口登录系统。

## 预期结果

系统正常启动，能够通过板载串口和ssh登录。

## 实际结果

系统正常启动，成功通过板载串口与ssh登录。

### 启动信息

> 出现 aic8800 insmod 失败是因为测试时使用的是不带 Wi-Fi 芯片的 Duo S。
> 
> 这是正常情况。

```log
Starting app...

[root@milkv-duo]~# [    5.417921] aicbsp: sdio_err:<aicwf_sdio_bus_pwrctl,1431>: bus down
[    6.149662] ieee80211 phy0: 
[    6.149662] *******************************************************
[    6.149662] ** CAUTION: USING PERMISSIVE CUSTOM REGULATORY RULES **
[    6.149662] *******************************************************

[root@milkv-duo]~# uname -a
Linux milkv-duo 5.10.4-tag- #1 PREEMPT Mon Dec 9 10:28:13 CST 2024 riscv64 GNU/Linux
[root@milkv-duo]~# cat /etc/os-release 
NAME=Buildroot
VERSION=-g2b4e5fdbc
ID=buildroot
VERSION_ID=2024.02.3
PRETTY_NAME="Buildroot 2024.02.3"
[root@milkv-duo]~# cat /proc/cpuinfo 
processor       : 0
hart            : 0
isa             : rv64imafdvcsu
mmu             : sv39

```

屏幕录像（从刷写镜像到登录系统）：

[![asciicast](https://asciinema.org/a/48Jw8Gwh6NqCJpnVejBntLIxd.svg)](https://asciinema.org/a/48Jw8Gwh6NqCJpnVejBntLIxd)

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。
