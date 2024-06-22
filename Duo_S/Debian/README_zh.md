# Debian Milk-V Duo S 测试报告

## 测试环境

### 操作系统信息

- 下载链接：https://github.com/Fishwaldo/sophgo-sg200x-debian/releases/tag/v1.1.0
- 参考安装文档：https://github.com/Fishwaldo/sophgo-sg200x-debian

### 硬件信息

- Milk-V Duo S (512M, SG2000)
- USB 电源适配器一个
- USB-A to C 或 USB C to C 线缆一条，用于给开发板供电
- microSD 卡一张
- USB 读卡器一个
- USB to UART 调试器一个（如：CP2102, FT2232 等，注意不可使用 CH340/341 系列，会出现乱码）
- 杜邦线三根

## 安装步骤

### 使用 `dd` 刷写镜像到 microSD 卡

```shell
lz4 -dk duos_sd.img.lz4
sudo dd if=duos_sd.img of=/dev/sdX bs=1M status=progress
```

### 登录系统

通过串口登录系统。

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

系统正常启动，成功通过板载串口登录。

### 启动信息

```log
Linux duos 5.10.4-20240329-1+ #1 PREEMPT Wed Apr 24 11:26:16 UTC 2024 riscv64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
root@duos:~# cat /etc/os-release
PRETTY_NAME="Debian GNU/Linux trixie/sid"
NAME="Debian GNU/Linux"
VERSION_CODENAME=trixie
ID=debian
HOME_URL="https://www.debian.org/"
SUPPORT_URL="https://www.debian.org/support"
BUG_REPORT_URL="https://bugs.debian.org/"
root@duos:~# uname -a
Linux duos 5.10.4-20240329-1+ #1 PREEMPT Wed Apr 24 11:26:16 UTC 2024 riscv64 GNU/Linux
root@duos:~# cat /proc/cpuinfo
processor       : 0
hart            : 0
isa             : rv64imafdvcsu
mmu             : sv39

root@duos:~#
```

屏幕录像：

[![asciicast](https://asciinema.org/a/SHxcbudKKPuuuARa7iMAhW0RO.svg)](https://asciinema.org/a/SHxcbudKKPuuuARa7iMAhW0RO)

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。