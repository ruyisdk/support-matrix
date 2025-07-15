# Ubuntu LicheeRV Nano 测试报告

## 测试环境

### 操作系统信息

- 下载链接：https://github.com/Z841973620/licheervnano-ubuntu/releases/tag/jammy
- 参考安装文档：https://github.com/Z841973620/licheervnano-ubuntu

### 硬件信息

- LicheeRV Nano
- Type-C 电源线一根
- UART 转 USB 调试器一个

## 安装步骤

### 使用 `dd` 刷写镜像到 microSD 卡

下载镜像后进行解压和刷写：

```shell
wget https://github.com/Z841973620/licheervnano-ubuntu/releases/download/jammy/licheervnano-ubuntu22.04-riscv64.img.xz
xz -d licheervnano-ubuntu22.04-riscv64.img.xz
sudo dd if=licheervnano-ubuntu22.04-riscv64.img of=/dev/your_device bs=1M status=progress
```

### 登录系统

通过串口登录系统。

用户名: `root`
密码：`ubuntu`

## 预期结果

系统正常启动，能够通过串口登录。

## 实际结果

系统正常启动，能够通过串口登录。

### 启动信息

```log
Ubuntu 22.04 LTS LicheeRV-Nano ttyS0

LicheeRV-Nano login: root
Password:
Welcome to Ubuntu 22.04 LTS (GNU/Linux 5.10.4 riscv64)

 System information disabled due to load higher than 1.0

The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

root@LicheeRV-Nano:~# uname -a
Linux LicheeRV-Nano 5.10.4 #1 Sat Jul 5 08:49:26 UTC 2025 riscv64 riscv64 riscv64 GNU/Linux
root@LicheeRV-Nano:~# cat /etc/os-release
PRETTY_NAME="Ubuntu 22.04 LTS"
NAME="Ubuntu"
VERSION_ID="22.04"
VERSION="22.04 (Jammy Jellyfish)"
VERSION_CODENAME=jammy
ID=ubuntu
ID_LIKE=debian
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
UBUNTU_CODENAME=jammy
root@LicheeRV-Nano:~# cat /proc/cpuinfo
processor       : 0
hart            : 0
isa             : rv64imafdvcsu
mmu             : sv39

root@LicheeRV-Nano:~#

```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。