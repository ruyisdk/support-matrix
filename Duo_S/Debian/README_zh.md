# Debian Milk-V Duo S 测试报告

## 测试环境

### 操作系统信息

- 下载链接：https://github.com/scpcom/sophgo-sg200x-debian/releases/tag/v1.6.35
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

Debian GNU/Linux 13 duos-a0d7 ttyS0

duos-a0d7 login: root
Password:
Linux duos-a0d7 5.10.235-20250615-6+duos #1 PREEMPT Mon Jun 16 00:47:42 UTC 2025 riscv64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
root@duos-a0d7:~# lscpu
Architecture:          riscv64
  Byte Order:          Little Endian
CPU(s):                1
  On-line CPU(s) list: 0
root@duos-a0d7:~# uname -a
Linux duos-a0d7 5.10.235-20250615-6+duos #1 PREEMPT Mon Jun 16 00:47:42 UTC 2025 riscv64 GNU/Linux
root@duos-a0d7:~#

```

屏幕录像：

[![asciicast](https://asciinema.org/a/wg2iVMT950W3x8gLiZEFRPch3.svg)](https://asciinema.org/a/wg2iVMT950W3x8gLiZEFRPch3)

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。
