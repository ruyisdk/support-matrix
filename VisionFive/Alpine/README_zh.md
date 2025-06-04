# Ubuntu VisionFive 测试报告

## 测试环境

### 系统信息

- 系统版本：3.20.0_alpha20231219 (edge)
- 下载链接：https://dev.alpinelinux.org/~mps/riscv64/visionfive-v1-mmc.img.xz
- 参考安装文档：https://arvanta.net/alpine/alpine-on-visionfive/

### 硬件信息

- StarFive VisionFive
- 电源适配器
- microSD 卡一张
- USB to UART 调试器一个

## 安装步骤

### 刷写镜像

使用 `xz` 解压镜像。
使用 `dd` 将镜像写入 microSD 卡。

```bash
xz -d visionfive-v1-mmc.img.xz
dd if=visionfive-v1-mmc.img of=/dev/<your-device> 
```

### 登录系统

通过串口登录系统。
直接登录到 root,无密码。


## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

系统正常启动，能够通过板载串口登录。

### 启动信息

屏幕录制（从刷写到登录）：
[![asciicast](https://asciinema.org/a/ui1P6rp5yjFTxO7YehuV7jC8s.svg)](https://asciinema.org/a/ui1P6rp5yjFTxO7YehuV7jC8s)

```log
Welcome to Alpine Linux 3.20.0_alpha20231219 (edge)
Kernel 6.8.0-rc2-0-vf1 on an riscv64 (ttyS0)

[press ENTER to login]
localhost login: root (automatic login)

Welcome to Alpine!

The Alpine Wiki contains a large amount of how-to guides and general
information about administrating Alpine systems.
See <https://wiki.alpinelinux.org/>.

You can setup the system with the command: setup-alpine

You may change this message by editing /etc/motd.

localhost:~# cat /etc/os-release 
NAME="Alpine Linux"
ID=alpine
VERSION_ID=3.20.0_alpha20231219
PRETTY_NAME="Alpine Linux edge"
HOME_URL="https://alpinelinux.org/"
BUG_REPORT_URL="https://gitlab.alpinelinux.org/alpine/aports/-/issues"
localhost:~# uname -a
Linux localhost 6.8.0-rc2-0-vf1 #1-Alpine SMP PREEMPT Fri, 02 Feb 2024 18:42:11 +0000 riscv64 Linux
localhost:~# lscpu
Architecture:          riscv64
  Byte Order:          Little Endian
CPU(s):                2
  On-line CPU(s) list: 0,1
localhost:~# 
```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功
