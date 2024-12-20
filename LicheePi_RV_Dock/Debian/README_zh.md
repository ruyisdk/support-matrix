# Debian 11 LicheePi RV Dock 测试报告

## 测试环境

### 操作系统信息

- 系统版本：Debian
- 下载链接：[MEGA](https://mega.nz/folder/lx4CyZBA#PiFhY7oSVQ3gp2ZZ_AnwYA)
- 参考安装文档：https://wiki.sipeed.com/hardware/zh/lichee/RV/flash.html

### 硬件信息

- Sipeed LicheePi RV Dock
- 电源适配器
- microSD 卡一张
- USB to UART 调试器一个

## 安装步骤

### 刷写镜像

1. 打开烧录软件 [PhoenixCard](https://dl.sipeed.com/shareURL/LICHEE/D1/Lichee_RV/tool)，选择烧录的固件，将内存卡通过读卡器插入电脑中
2. 选择 `启动卡` 选项
3. 选择正确的盘符
4. 点击 `烧卡`
5. 根据状态栏的颜色可以判断烧录结果：红色的话说明烧录失败，建议使用 `SD card Formatter` 格式化后再重新烧录一次

### 登录系统

通过串口登录系统。

默认用户名：`root`
默认密码：`licheepi`

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

系统正常启动，成功通过板载串口登录。

### 启动信息

屏幕录像（从刷写镜像到登录系统）：

[![asciicast](https://asciinema.org/a/7osW4u2FvkucqlfODK4nEBMQm.svg)](https://asciinema.org/a/7osW4u2FvkucqlfODK4nEBMQm)

```log
Debian GNU/Linux 11 RVBoards ttyS0

RVBoards login: root
Password: 

Login incorrect
RVBoards login: root
Password: 
Linux RVBoards 5.4.61 #12 PREEMPT Thu Jun 3 08:39:01 UTC 2021 riscv64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Wed May 19 18:39:24 CST 2021 on ttyS0
root@RVBoards:~# uname -a
Linux RVBoards 5.4.61 #12 PREEMPT Thu Jun 3 08:39:01 UTC 2021 riscv64 GNU/Linux
root@RVBoards:~# cat /etc/os-release 
PRETTY_NAME="Debian GNU/Linux 11 (bullseye)"
NAME="Debian GNU/Linux"
VERSION_ID="11"
VERSION="11 (bullseye)"
VERSION_CODENAME=bullseye
ID=debian
HOME_URL="https://www.debian.org/"
SUPPORT_URL="https://www.debian.org/support"
BUG_REPORT_URL="https://bugs.debian.org/"
root@RVBoards:~# Debian GNU/Linux 11 sipeed ttyS0

sipeed login: root
Password: 
Linux sipeed 5.4.61 #217 PREEMPT Thu Dec 30 06:50:31 UTC 2021 riscv64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Mon May 24 06:56:42 UTC 2021 on ttyS0
root@sipeed:~# uname 
Message from syslogd@sipeed at May 24 06:57:35 ...
 kernel:[  102.178091] Oops [#6]

root@sipeed:~# uname -a
Linux sipeed 5.4.61 #217 PREEMPT Thu Dec 30 06:50:31 UTC 2021 riscv64 GNU/Linux
root@sipeed:~# cat /etc/os-release 
PRETTY_NAME="Debian GNU/Linux 11 (bullseye)"
NAME="Debian GNU/Linux"
VERSION_ID="11"
VERSION="11 (bullseye)"
VERSION_CODENAME=bullseye
ID=debian
HOME_URL="https://www.debian.org/"
SUPPORT_URL="https://www.debian.org/support"
BUG_REPORT_URL="https://bugs.debian.org/"
root@sipeed:~# 
Message from syslogd@sipeed at May 24 06:58:00 ...
 kernel:[  127.198571] Oops [#7]

root@sipeed:~# cat /proc/cpuinfo 
processor       : 0
hart            : 0
isa             : rv64imafdcvu
mmu             : sv39

root@sipeed:~# 

```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。
