# Debian Milk-V Duo S 测试报告

## 测试环境

### 操作系统信息

- 系统版本：Debian 13 (trixie)，社区镜像 v1.9.6
- 下载链接：https://github.com/scpcom/sophgo-sg200x-debian/releases/tag/v1.9.6
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
         Starting systemd-random-seed.service - Load/Save OS Random Seed...
[   13.079265] systemd[1]: Failed to start systemd-sysctl.service - Apply Kernel Variables.
[FAILED] Failed to start systemd-sysctl.service - Apply Kernel Variables.
See 'systemctl status systemd-sysctl.service' for details.

Debian GNU/Linux 13 duos-1f79 ttyS0

duos-1f79 login: root
Password:
Linux duos-1f79 5.10.260-20260711-6+duos #1 PREEMPT Tue Jul 14 03:03:04 UTC 2026 riscv64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
root@duos-1f79:~# lscpu
Architecture:          riscv64
  Byte Order:          Little Endian
CPU(s):                1
  On-line CPU(s) list: 0
root@duos-1f79:~# uname -a
Linux duos-1f79 5.10.260-20260711-6+duos #1 PREEMPT Tue Jul 14 03:03:04 UTC 2026 riscv64 GNU/Linux
root@duos-1f79:~#

```

> 注：启动过程中 `systemd-sysctl.service` 启动失败，具体原因尚未确认。本次测试中，系统仍成功通过串口登录。

屏幕录像：

[![asciicast](https://asciinema.org/a/x5lUx5XQO1zB9w2C.svg)](https://asciinema.org/a/x5lUx5XQO1zB9w2C)

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。系统正常启动，成功通过板载串口登录。
