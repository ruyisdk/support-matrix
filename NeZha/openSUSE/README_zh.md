# openSUSE Tumbleweed AWOL Nezha D1 测试报告

## 测试环境

### 系统信息

- 系统版本：openSUSE Tumbleweed
- 下载链接：[openSUSE-Tumbleweed-RISC-V-JeOS-nezha.riscv64.raw.xz](https://download.opensuse.org/repositories/devel:/RISCV:/Factory:/Contrib:/AllwinnerD1/images/)
- 参考安装文档：[https://en.opensuse.org/HCL:Nezha](https://en.opensuse.org/HCL:Nezha)

### 硬件信息

- AWOL Nezha D1 
- 电源适配器
- microSD 卡一张
- USB to UART 调试器一个

## 安装步骤

### 刷写镜像

使用 `unxz` 解压镜像。
使用 `dd` 将镜像写入 microSD 卡。

```bash
unxz /path/to/openSUSE.raw.xz
sudo dd if=/path/to/openSUSE.raw of=/dev/your-device bs=1M status=progress
```

### 登录系统

*系统启动较为缓慢。*

通过串口登录系统。

默认用户名： `root`
默认密码： `linux`

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

系统正常启动，成功通过板载串口登录。

### 启动信息

屏幕录像（从刷写镜像到登录系统）：

[![asciicast](https://asciinema.org/a/qGx3Er1vKkhIuC19Ixbj50HNk.svg)](https://asciinema.org/a/qGx3Er1vKkhIuC19Ixbj50HNk)


```log

Welcome to openSUSE Tumbleweed 20
Welcome to openSUSE Tumbleweed 20240115 - Kernel240115 - Kernel 6.5.2-4-default (h 6.5.2-4-default (ttyS0).



localhost login: vc0).



localhost login: root
Password: 
Have a lot of fun...
localhost:~ # uname -a
Linux localhost.localdomain 6.5.2-4-default #1 SMP Wed Sep 13 03:16:12 UTC 2023 (b06df44) riscv64 riscv64 riscv64 GNU/Linux
localhost:~ # cat /etc/os-release 
NAME="openSUSE Tumbleweed"
# VERSION="20240115"
ID="opensuse-tumbleweed"
ID_LIKE="opensuse suse"
VERSION_ID="20240115"
PRETTY_NAME="openSUSE Tumbleweed"
ANSI_COLOR="0;32"
CPE_NAME="cpe:/o:opensuse:tumbleweed:20240115"
BUG_REPORT_URL="https://bugzilla.opensuse.org"
SUPPORT_URL="https://bugs.opensuse.org"
HOME_URL="https://www.opensuse.org"
DOCUMENTATION_URL="https://en.opensuse.org/Portal:Tumbleweed"
LOGO="distributor-logo-Tumbleweed"

```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。
