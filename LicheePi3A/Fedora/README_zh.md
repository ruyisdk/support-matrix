# Fedora Minimal 41 荔枝派 Lichee Pi 3A 测试报告

## 测试环境

### 系统信息

- 系统版本: fedora-v-force Fedora Minimal 41
- 下载链接: https://mirror.iscas.ac.cn/fedora-riscv/dl/SpacemiT/K1_M1/images/latest/k1-fedora-minimal.img.gz
- 参考安装文档: https://wiki.sipeed.com/hardware/zh/lichee/K1/lpi3a/1_intro.html

### 硬件信息

- 荔枝派 Lichee Pi 3A
- 电源适配器
- USB 转 UART 调试器
- microSD 卡

## 安装步骤

### 使用 `dd` 将镜像写入 SD 卡

下载并解压镜像后，使用 `dd` 将镜像写入 microSD 卡。

```bash
gzip -d k1-fedora-minimal.img.gz
sudo dd if=k1-fedora-minimal.img of=/dev/your-device bs=1M status=progress oflag=dsync
```

### 登录系统

通过串口登录系统。

默认用户名： `root`
默认密码： `riscv`

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

系统正常启动，成功通过板载串口登录。

### 启动信息

屏幕录像（从刷写镜像到登录系统）：
[![asciicast](https://asciinema.org/a/xXecoLrIq2cKdvmbVfMWDzJYU.svg)](https://asciinema.org/a/xXecoLrIq2cKdvmbVfMWDzJYU)

```log
Welcome to the Fedora RISC-V disk image
https://openkoji.iscas.ac.cn/koji/

Build date: Mon Jul  1 03:20:03 UTC 2024

Kernel 6.1.15 on an riscv64 (ttyS0)

The root password is 'riscv'.
root password logins are disabled in SSH starting Fedora.

If DNS isn’t working, try editing ‘/etc/yum.repos.d/fedora-riscv.repo’.

For updates and latest information read:
https://fedoraproject.org/wiki/Architectures/RISC-V

Fedora RISC-V
-------------
fedora-riscv login: root
Password: 
[root@fedora-riscv ~]# cat /etc/os-release 
NAME="Fedora Linux"
VERSION="41 (Rawhide Prerelease)"
ID=fedora
VERSION_ID=41
VERSION_CODENAME=""
PLATFORM_ID="platform:f41"
PRETTY_NAME="Fedora Linux 41 (Rawhide Prerelease)"
ANSI_COLOR="0;38;2;60;110;180"
LOGO=fedora-logo-icon
CPE_NAME="cpe:/o:fedoraproject:fedora:41"
DEFAULT_HOSTNAME="fedora"
HOME_URL="https://fedoraproject.org/"
DOCUMENTATION_URL="https://docs.fedoraproject.org/en-US/fedora/rawhide/system-administrators-guide/"
SUPPORT_URL="https://ask.fedoraproject.org/"
BUG_REPORT_URL="https://bugzilla.redhat.com/"
REDHAT_BUGZILLA_PRODUCT="Fedora"
REDHAT_BUGZILLA_PRODUCT_VERSION=rawhide
REDHAT_SUPPORT_PRODUCT="Fedora"
REDHAT_SUPPORT_PRODUCT_VERSION=rawhide
SUPPORT_END=2025-05-13
[root@fedora-riscv ~]# uname -a
Linux fedora-riscv 6.1.15 #4 SMP PREEMPT Mon Jul 15 09:53:57 CST 2024 riscv64 GNU/Linux
[root@fedora-riscv ~]# lscpu
Architecture:           riscv64
  Byte Order:           Little Endian
CPU(s):                 8
  On-line CPU(s) list:  0-7
Vendor ID:              0x710
  Model name:           Spacemit(R) X60
    CPU family:         0x8000000058000001
    Model:              0x1000000049772200
    Thread(s) per core: 1
    Core(s) per socket: 8
    Socket(s):          1
    CPU(s) scaling MHz: 100%
    CPU max MHz:        1600.0000
    CPU min MHz:        614.4000
Caches (sum of all):    
  L1d:                  256 KiB (8 instances)
  L1i:                  256 KiB (8 instances)
  L2:                   1 MiB (2 instances)
[root@fedora-riscv ~]# 
```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

成功
