# Debian Milk-V Duo S 测试报告

## 测试环境

### 操作系统信息

- 下载链接：https://github.com/scpcom/sophgo-sg200x-debian/releases/tag/v1.6.31
- 参考安装文档：https://github.com/scpcom/sophgo-sg200x-debian

### 硬件信息

- Milk-V Duo S (512M, SG2000)
- USB 电源适配器一个
- USB-A to C 或 USB C to C 线缆一条，用于给开发板供电
- microSD 卡一张
- USB 读卡器一个
- USB to UART 调试器一个
- 杜邦线三根

## 安装步骤

### 使用 `dd` 刷写镜像到 microSD 卡

```shell
lz4 -dk duos-e_sd.img.lz4
sudo dd if=duos-e_sd.img of=/dev/sdX bs=1M status=progress
```

### 登录系统

通过串口登录系统。

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

系统正常启动，成功通过板载串口登录。

### 启动信息

```log
Debian GNU/Linux 13 duos-a0d7 ttyS0

duos-a0d7 login: debian
Password:
Linux duos-a0d7 5.10.235-20250531-6+duos #1 PREEMPT Sun Jun 8 03:30:58 UTC 2025 riscv64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
debian@duos-a0d7:~$ cat /etc/os-release
PRETTY_NAME="Debian GNU/Linux 13 (trixie)"
NAME="Debian GNU/Linux"
VERSION_ID="13"
VERSION="13 (trixie)"
VERSION_CODENAME=trixie
DEBIAN_VERSION_FULL=13.0
ID=debian
HOME_URL="https://www.debian.org/"
SUPPORT_URL="https://www.debian.org/support"
BUG_REPORT_URL="https://bugs.debian.org/"
debian@duos-a0d7:~$ uname -a
Linux duos-a0d7 5.10.235-20250531-6+duos #1 PREEMPT Sun Jun 8 03:30:58 UTC 2025 riscv64 GNU/Linux
debian@duos-a0d7:~$ cat /proc/cpuinfo
processor       : 0
hart            : 0
isa             : rv64imafdvcsu
mmu             : sv39

debian@duos-a0d7:~$
```

屏幕录像：

[![asciicast](https://asciinema.org/a/f2rfBYYV0SuSLxsjZSJ8VHNLV.svg)](https://asciinema.org/a/f2rfBYYV0SuSLxsjZSJ8VHNLV)

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。
