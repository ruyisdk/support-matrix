# Debian LicheeRV Nano 测试报告

## 测试环境

### 操作系统信息

- 下载链接：https://github.com/scpcom/sophgo-sg200x-debian/releases/download/v1.6.7/licheervnano-e_sd.img.lz4
- 参考安装文档：https://github.com/scpcom/sophgo-sg200x-debian/

### 硬件信息

- LicheeRV Nano
- Type-C 电源线一根
- UART 转 USB 调试器一个

## 安装步骤

### 使用 `dd` 刷写镜像到 microSD 卡

下载镜像后进行解压和刷写：

```shell
wget https://github.com/scpcom/sophgo-sg200x-debian/releases/download/v1.6.7/licheervnano-e_sd.img.lz4
lz4 -dk licheervnano-e_sd.img.lz4
sudo dd if=licheervnano-e_sd.img of=/dev/your_device bs=1M status=progress
```

### 登录系统

通过串口登录系统。

| 用户名 | 密码 |
| ------ | ---- |
| root   | rv   |
| debian | rv   |


## 预期结果

系统正常启动，能够通过串口登录。

## 实际结果

系统正常启动，能够通过串口登录。

### 启动信息

```log
Debian GNU/Linux trixie/sid licheervnano-6681 ttyS0

licheervnano-6681 login: [  OK  ] Finished e2scrub_reap.service - Remove Stale Online ext4 Metadata Check Snapshots.
[  OK  ] Finished finalize-image.service - Finalize the Image.
         Starting ssh.service - OpenBSD Secure Shell server...
[  OK  ] Started ssh.service - OpenBSD Secure Shell server.
[  OK  ] Reached target multi-user.target - Multi-User System.
[  OK  ] Reached target graphical.target - Graphical Interface.

licheervnano-6681 login: root
Password:
Linux licheervnano-6681 5.10.235-20250403-6+licheervnano #1 PREEMPT Sat Apr 5 17:40:58 UTC 2025 riscv64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
root@licheervnano-6681:~# uname -a
Linux licheervnano-6681 5.10.235-20250403-6+licheervnano #1 PREEMPT Sat Apr 5 17:40:58 UTC 2025 riscv64 GNU/Linux
root@licheervnano-6681:~# cat /etc/os-release
PRETTY_NAME="Debian GNU/Linux trixie/sid"
NAME="Debian GNU/Linux"
VERSION_CODENAME=trixie
ID=debian
HOME_URL="https://www.debian.org/"
SUPPORT_URL="https://www.debian.org/support"
BUG_REPORT_URL="https://bugs.debian.org/"
root@licheervnano-6681:~# lscpu
Architecture:          riscv64
  Byte Order:          Little Endian
CPU(s):                1
  On-line CPU(s) list: 0
root@licheervnano-6681:~# cat /proc/cpuinfo
processor       : 0
hart            : 0
isa             : rv64imafdvcsu
mmu             : sv39

root@licheervnano-6681:~#

```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。