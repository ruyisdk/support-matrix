# Fedora 38 K230 测试报告

## 测试环境

### 操作系统信息

官方预编译 SDK 已经含有了 RT-Smart。

- 下载链接：https://github.com/kendryte/k230_sdk/releases/tag/v1.4
- 参考安装文档：https://github.com/kendryte/k230_docs/blob/main/zh/01_software/board/K230_SDK_%E4%BD%BF%E7%94%A8%E8%AF%B4%E6%98%8E.md

### 硬件信息

- 开发板：Canaan Kendryte K230
- USB A to C / USB C to C 线缆

## 安装步骤

### 刷写镜像

使用 `unzstd` 解压镜像。
清空你的 sd 卡。
使用 `dd` 将镜像写入 microSD 卡。

```bash
gizp -d /path/to/k230.img.gz
sudo wipefs -a /dev/your_device
sudo dd if=/path/to/k230.img of=/dev/your_device bs=1M status=progress
```

### 登录系统

通过串口登录系统。

默认用户： `root`
无默认密码。

其中小核 tty 为 Linux，大核 tty 为 RT-Smart。

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

系统正常启动，成功通过板载串口登录。

### 启动信息

屏幕录像（从烧录到登录系统）：

[![asciicast](https://asciinema.org/a/urysrirhMB8fivXe1JHQ65Hyv.svg)](https://asciinema.org/a/urysrirhMB8fivXe1JHQ65Hyv)

```log
Welcome to the Fedora RISC-V disk image
https://openkoji.iscas.ac.cn/koji/

Build date: Tue Aug 15 19:14:20 UTC 2023

Kernel 6.6.0+ on an riscv64 (ttyS0)

The root password is 'riscv'.
root password logins are disabled in SSH starting Fedora.

If DNS isn’t working, try editing ‘/etc/yum.repos.d/fedora-riscv.repo’.

For updates and latest information read:
https://fedoraproject.org/wiki/Architectures/RISC-V

Fedora RISC-V
-------------
fedora-riscv login: root
Password: 
Last login: Sun Mar  3 02:47:32 on ttyS0
-bash-5.2# uname -a
Linux fedora-riscv 6.6.0+ #1 SMP Wed Mar 13 09:16:28 UTC 2024 riscv64 GNU/Linux
-bash-5.2# cat /etc/os-release 
NAME="Fedora Linux"
VERSION="38 (Thirty Eight)"
ID=fedora
VERSION_ID=38
VERSION_CODENAME=""
PLATFORM_ID="platform:f38"
PRETTY_NAME="Fedora Linux 38 (Thirty Eight)"
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

```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。