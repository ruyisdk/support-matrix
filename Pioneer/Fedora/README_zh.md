# Fedora 38 Pioneer 测试报告

## 测试环境

- 系统版本：Fedora 38
- 下载链接：[Google Drive](https://drive.google.com/file/d/1IjxeKiwtyDTmc2YGbn7yvpbCx0B1kkBh/view)
- 参考安装文档：[https://milkv.io/zh/docs/pioneer/getting-started/InstallOS](https://milkv.io/zh/docs/pioneer/getting-started/InstallOS)

### 硬件信息

- Milk-V Pioneer Box v1.1
- microSD 卡一张
- USB to UART 调试器一个（或 HDMI 线 + 显示器）

## 安装步骤

### 刷写镜像

使用 `unxz` 解压镜像。
使用 `dd` 将镜像写入 microSD 卡。

```bash
unxz /path/to/fedora.raw.xz
sudo dd if=/path/to/fedora.raw of=/dev/your_device bs=4M status=progress
```

### 登录系统

通过串口登录系统。

默认用户名： `root`
默认密码： `riscv`

若从 HDMI 初次启动，系统会进入安装向导界面。

## 预期结果

系统正常启动，能够通过板载串口登录。能进入安装向导。

## 实际结果

系统正常启动，成功通过板载串口登录。能进入安装向导。

### 启动信息

屏幕录像（从刷写镜像到登录系统）：

[![asciicast](https://asciinema.org/a/o9SKKWMrCoOV38yKIzNDcLEDb.svg)](https://asciinema.org/a/o9SKKWMrCoOV38yKIzNDcLEDb)

```log
Welcome to the Fedora RISC-V disk image
https://openkoji.iscas.ac.cn/koji/

Build date: Mon Oct  9 21:52:55 UTC 2023

Kernel 6.1.55 on an riscv64 (ttyS0)

The root password is 'riscv'.
root password logins are disabled in SSH starting Fedora.

If DNS isn’t working, try editing ‘/etc/yum.repos.d/fedora-riscv.repo’.

For updates and latest information read:
https://fedoraproject.org/wiki/Architectures/RISC-V

Fedora RISC-V
-------------
fedora-riscv login: root
Password: 
Last login: Tue Aug  8 20:07:30 on ttyS0
[root@fedora-riscv ~]# uname -a
Linux fedora-riscv 6.1.55 #1 SMP Sat Oct  7 21:05:27 CST 2023 riscv64 GNU/Linux
[root@fedora-riscv ~]# cat /etc/os-release 
NAME="Fedora Linux"
VERSION="38 (Workstation Edition)"
ID=fedora
VERSION_ID=38
VERSION_CODENAME=""
PLATFORM_ID="platform:f38"
PRETTY_NAME="Fedora Linux 38 (Workstation Edition)"
ANSI_COLOR="0;38;2;60;110;180"
LOGO=fedora-logo-icon
CPE_NAME="cpe:/o:fedoraproject:fedora:38"
DEFAULT_HOSTNAME="fedora"
HOME_URL="https://fedoraproject.org/"
DOCUMENTATION_URL="https://docs.fedoraproject.org/en-US/fedora/f38/system-administrators-guide/"
SUPPORT_URL="https://ask.fedoraproject.org/"
BUG_REPORT_URL="https://bugzilla.redhat.com/"
REDHAT_BUGZILLA_PRODUCT="Fedora"
REDHAT_BUGZILLA_PRODUCT_VERSION=38
REDHAT_SUPPORT_PRODUCT="Fedora"
REDHAT_SUPPORT_PRODUCT_VERSION=38
SUPPORT_END=2024-05-14
VARIANT="Workstation Edition"
VARIANT_ID=workstation
[root@fedora-riscv ~]# cat /proc/cpuinfo 
processor       : 0
hart            : 2
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 1
hart            : 0
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 2
hart            : 1
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 3
hart            : 3
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 4
hart            : 4
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 5
hart            : 5
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 6
hart            : 6
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 7
hart            : 7
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 8
hart            : 8
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 9
hart            : 9
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 10
hart            : 10
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 11
hart            : 11
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 12
hart            : 12
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 13
hart            : 13
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 14
hart            : 14
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 15
hart            : 15
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 16
hart            : 16
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 17
hart            : 17
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 18
hart            : 18
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 19
hart            : 19
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 20
hart            : 20
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 21
hart            : 21
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 22
hart            : 22
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 23
hart            : 23
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 24
hart            : 24
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 25
hart            : 25
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 26
hart            : 26
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 27
hart            : 27
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 28
hart            : 28
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 29
hart            : 29
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 30
hart            : 30
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 31
hart            : 31
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 32
hart            : 32
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 33
hart            : 33
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 34
hart            : 34
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 35
hart            : 35
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 36
hart            : 36
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 37
hart            : 37
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 38
hart            : 38
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 39
hart            : 39
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 40
hart            : 40
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 41
hart            : 41
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 42
hart            : 42
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 43
hart            : 43
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 44
hart            : 44
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 45
hart            : 45
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 46
hart            : 46
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 47
hart            : 47
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 48
hart            : 48
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 49
hart            : 49
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 50
hart            : 50
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 51
hart            : 51
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 52
hart            : 52
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 53
hart            : 53
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 54
hart            : 54
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 55
hart            : 55
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 56
hart            : 56
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 57
hart            : 57
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 58
hart            : 58
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 59
hart            : 59
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 60
hart            : 60
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 61
hart            : 61
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 62
hart            : 62
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 63
hart            : 63
isa             : rv64imafdcv
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0
```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。