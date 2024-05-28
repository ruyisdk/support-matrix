# Debian Milk-V Duo 256M 测试报告

## 测试环境

### 操作系统信息

- 系统版本：Debian
- 下载链接：https://github.com/Fishwaldo/sophgo-sg200x-debian
- 参考安装文档：https://github.com/Fishwaldo/sophgo-sg200x-debian

> Note: 此镜像为社区开发者提供，非官方镜像。

### 硬件信息

- Milk-V Duo 256M
- USB-A to C 或 USB C to C 线缆一条
- microSD 卡一张
- USB to UART 调试器一个（如：CH340, CH341, FT2232 等）
- 可选：Milk-V Duo IOB（底板）

## 安装步骤

### 使用 `dd` 刷写镜像到 microSD 卡

```shell
wget https://github.com/Fishwaldo/sophgo-sg200x-debian/releases/download/v1.3.0/duo256_sd.img.lz4
lz4 -d duo256_sd.img.lz4
sudo dd if=duo256_sd.img of=/dev/your/device bs=1M status=progress
```

### 登录系统

通过串口登录系统。

用户名：`root`
密码：`rv`

## 预期结果

系统正常启动，能够通过串口登录。

## 实际结果

系统正常启动，成功通过串口登录。

### 启动信息

```log
Debian GNU/Linux trixie/sid duo256 ttyS0

duo256 login: root
Password: 
Linux duo256 5.10.4-20240329-1+ #1 Sat May 18 10:13:53 UTC 2024 riscv64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
root@duo256:~# cat /etc/os-release 
PRETTY_NAME="Debian GNU/Linux trixie/sid"
NAME="Debian GNU/Linux"
VERSION_CODENAME=trixie
ID=debian
HOME_URL="https://www.debian.org/"
SUPPORT_URL="https://www.debian.org/support"
BUG_REPORT_URL="https://bugs.debian.org/"
root@duo256:~# uname -a\
> 
Linux duo256 5.10.4-20240329-1+ #1 Sat May 18 10:13:53 UTC 2024 riscv64 GNU/Linux
root@duo256:~# 

```

启动流程屏幕录像：
[![asciicast](https://asciinema.org/a/4p20IBBlCuE8jMxEExj19vMqd.svg)](https://asciinema.org/a/4p20IBBlCuE8jMxEExj19vMqd)


## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

成功