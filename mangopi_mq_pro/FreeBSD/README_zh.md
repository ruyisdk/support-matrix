# FreeBSD MangoPi MQ Pro 测试报告

## 测试环境

### 操作系统信息

- 下载链接：https://github.com/freebsd-d1/freebsd-d1
- 参考安装文档：https://github.com/freebsd-d1/freebsd-d1

### 硬件信息

- MangoPi MQ Pro
- 电源适配器
- microSD 卡一张
- USB to UART 调试器一个

## 安装步骤

### 编译和刷写镜像

**下面的编译步骤需要在 FreeBSD 环境下进行，推荐使用虚拟机。**
clone 仓库并生成镜像：

```bash
git clone https://github.com/freebsd-d1/freebsd-d1.git
cd freebsd-d1
pkg install gmake ccache llvm14 riscv64-none-elf-gcc python3 bison swig py39-setuptools
git submodule update --init
gmake
dd if=freebsd-d1.img of=/dev/your/device
```

### 登录系统

通过串口登录系统。

默认用户名：`root`

默认无密码。

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

系统正常启动，能够通过板载串口登录。

### 启动信息

```log
Fri Mar  7 21:29:20 UTC 2025

FreeBSD/riscv (freebsd-d1) (rcons)

login: root
Mar  7 21:29:23 freebsd-d1 login[1090]: ROOT LOGIN (root) ON rcons
FreeBSD 14.0-CURRENT #0 n258218-3243c065a44f: Fri Mar  7 21:25:14 UTC 2025     root@freebsd:/root/freebsd-d1/freebsd/obj/riscv.riscv64/sys/GENERIC

Welcome to FreeBSD!

Release Notes, Errata: https://www.FreeBSD.org/releases/
Security Advisories:   https://www.FreeBSD.org/security/
FreeBSD Handbook:      https://www.FreeBSD.org/handbook/
FreeBSD FAQ:           https://www.FreeBSD.org/faq/
Questions List:        https://www.FreeBSD.org/lists/questions/
FreeBSD Forums:        https://forums.FreeBSD.org/

Documents installed with the system are in the /usr/local/share/doc/freebsd/
directory, or can be installed later with:  pkg install en-freebsd-doc
For other languages, replace "en" with a language code like de or fr.

Show the version of FreeBSD installed:  freebsd-version ; uname -a
Please include that output and any error messages when posting questions.
Introduction to manual pages:  man man
FreeBSD directory layout:      man hier

To change this login announcement, see motd(5).
root@freebsd-d1:~ # uname -a
FreeBSD freebsd-d1 14.0-CURRENT FreeBSD 14.0-CURRENT #0 n258218-3243c065a44f: Fri Mar  7 21:25:14 UTC 2025     root@freebsd:/root/freebsd-d1/freebsd/obj/riscv.riscv64/sys/GENERIC riscv
root@freebsd-d1:~ # cat /etc/os-release 
NAME=FreeBSD
VERSION="14.0-CURRENT"
VERSION_ID="14.0"
ID=freebsd
ANSI_COLOR="0;31"
PRETTY_NAME="FreeBSD 14.0-CURRENT"
CPE_NAME="cpe:/o:freebsd:freebsd:14.0"
HOME_URL="https://FreeBSD.org/"
BUG_REPORT_URL="https://bugs.FreeBSD.org/"
root@freebsd-d1:~ # 
```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。