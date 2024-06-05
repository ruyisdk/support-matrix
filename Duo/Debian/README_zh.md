# Debian Milk-V Duo 测试报告

## 测试环境

### 操作系统信息

- 系统版本：Debian trixie/sid
- 下载链接：https://drive.google.com/file/d/1TqMuFsRo5Es2Y6-qAyxV8jnFdAkcCp4v/view?usp=sharing
- 参考安装文档：https://github.com/hongwenjun/riscv64/tree/main/milkv-duo

> Note: 此镜像为社区开发者提供，非官方镜像。

### 硬件信息

- Milk-V Duo 64M
- USB 电源适配器一个
- USB-A to C 或 USB C to C 线缆一条
- microSD 卡一张
- USB to UART 调试器一个（如：CH340, CH341, FT2232 等）
- 杜邦线三根
- Milk-V Duo 本体上预先焊接好调试所需的排针
- 可选：Milk-V Duo IOB（底板）

## 安装步骤

### 使用 `dd` 刷写镜像到 microSD 卡

```shell
7z x duo-debian-full.7z
dd if=debian.img of=/dev/sdc bs=1M status=progress
```

### 登录系统

通过串口登录系统。

用户名：`root`
密码：`riscv`

## 预期结果

系统正常启动，能够通过串口登录。

## 实际结果

系统正常启动，成功通过串口登录。

### 启动信息

```log
Debian GNU/Linux trixie/sid milkv-duo ttyS0

milkv-duo login: root
Password: 
Linux milkv-duo 5.10.4-tag- #7 PREEMPT Tue Oct 24 23:07:12 JST 2023 riscv64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Mon Jul 24 19:51:14 UTC 2023 on ttyS0
root@milkv-duo:~# uname -a
Linux milkv-duo 5.10.4-tag- #7 PREEMPT Tue Oct 24 23:07:12 JST 2023 riscv64 GNU/Linux
root@milkv-duo:~# cat /proc/cpuinfo 
processor       : 0
hart            : 0
isa             : rv64imafdvcsu
mmu             : sv39

root@milkv-duo:~# cat /etc/os-release 
PRETTY_NAME="Debian GNU/Linux trixie/sid"
NAME="Debian GNU/Linux"
VERSION_CODENAME=trixie
ID=debian
HOME_URL="https://www.debian.org/"
SUPPORT_URL="https://www.debian.org/support"
BUG_REPORT_URL="https://bugs.debian.org/"
root@milkv-duo:~# 
```

启动流程屏幕录像：

[![asciicast](https://asciinema.org/a/oOEaHElWFYEJMCmsOkqDZfbEv.svg)](https://asciinema.org/a/oOEaHElWFYEJMCmsOkqDZfbEv)


## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。