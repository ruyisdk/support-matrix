# postmarketOS DongshanPI-Nezha STU 测试报告

## 测试环境

### 操作系统信息

- 下载链接（pmbootstrap）: https://wiki.postmarketos.org/wiki/Pmbootstrap
- 参考安装文档：https://wiki.postmarketos.org/index.php?title=MangoPi_MQ-Pro_(mangopi-mq-pro)&direction=prev&oldid=46021

### 硬件信息

- MangoPi MQ Pro
- 电源适配器
- microSD 卡一张
- USB to UART 调试器一个

## 安装步骤

### 通过 `pmbootstrap` 安装

安装 `pmbootstrap` ，如在 Arch Linux 下：
```bash
pacman -S pmbootstrap
```

使用 `pmbootstrap` 安装和刷写镜像：
```bash
pmbootstrap init
pmbootstrap install --sdcard=/dev/sdX
pmbootstrap shutdown
```
安装过程中同时会进行系统配置，请选择 target vendor 为 `dongshanpi`, target board 为 `nezhastu`。

### 登录系统

通过串口登录系统。

用户名和密码在上述安装过程中自行配置。

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

系统正常启动，能够通过板载串口登录。

### 启动信息

```log
Welcome to postmarketOS
Kernel 6.1.0-rc3 on an riscv64 (/dev/ttyS0)
dongshanpi-nezhastu login: pmosriscv
Password: 
Welcome to postmarketOS! o/

This distribution is based on Alpine Linux.
First time using postmarketOS? Make sure to read the cheatsheet in the wiki:

-> https://postmarketos.org/cheatsheet

You may change this message by editing /etc/motd.
dongshanpi-nezhastu:~$ uname -a
Linux dongshanpi-nezhastu 6.1.0-rc3 #1 Wed Jul 31 00:22:22 UTC 2024 riscv64 Linux
dongshanpi-nezhastu:~$ cat /etc/os-release 
PRETTY_NAME="postmarketOS edge"
NAME="postmarketOS"
VERSION_ID="edge"
VERSION="edge"
ID="postmarketos"
ID_LIKE="alpine"
HOME_URL="https://www.postmarketos.org/"
SUPPORT_URL="https://gitlab.postmarketos.org/postmarketOS"
BUG_REPORT_URL="https://gitlab.postmarketos.org/postmarketOS/pmaports/issues"
LOGO="postmarketos-logo"
ANSI_COLOR="0;32"
dongshanpi-nezhastu:~$ 

```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。