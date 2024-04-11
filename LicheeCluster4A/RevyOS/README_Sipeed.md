# RevyOS Sipeed 厂商镜像 Lichee Cluster 4A 版本测试报告

## 测试环境

### 操作系统信息

- 系统版本：RevyOS 20230614-183009
- 下载链接：https://dl.sipeed.com/shareURL/LICHEE/LicheeCluster4A/04_Firmware/lpi4a/bin
- 参考安装文档：https://wiki.sipeed.com/hardware/zh/lichee/th1520/lc4a/lc4a.html

### 硬件信息

- Lichee Cluster 4A 8G / 16G
- DC 12V 电源
- USB-A to A
    - 或 LPi4A 底板
- 网络和网线（注意连接到 BMC 而非交换机）


## 安装步骤

*以下以刷写到集群中一号板为例*

### 连接对应 SOM

使用 A to A 线缆连接 SOM。

### 刷写镜像

使用 `unxz` 解压镜像。

```bash
unxz -k boot-20230614-182922.ext4.xz rootfs-20230614-183009.ext4.xz
```

使用 `fastboot` 刷写镜像
```bash
sudo ./fastboot flash ram u-boot-with-spl-lpi4a.bin
sudo ./fastboot reboot
sudo ./fastboot flash uboot u-boot-with-spl-lpi4a.bin
sudo ./fastboot flash boot boot-20230614-182922.ext4
sudo ./fastboot flash root rootfs-20230614-183009.ext4
```

### 登录系统

通过 SOL (Serial Over LAN) 登录系统。

BMC 默认用户名：`root`

BMC 默认密码：`0penBmc`  **注意是 `0` 而不是 `O`**

通过 `ssh -p 2301 root@lichee-rv.local` 连接

默认用户名：`debian`
默认密码：`debian`

## 预期结果

系统正常启动，能够通过 SOL (Serial Over LAN) 登录。

## 实际结果

系统正常启动，能够通过 SOL (Serial Over LAN) 登录。

### 启动信息

屏幕录像（从刷写系统到启动）：

[![asciicast](https://asciinema.org/a/KwCIHjcPOuepxFiwUGhh7sLuh.svg)](https://asciinema.org/a/KwCIHjcPOuepxFiwUGhh7sLuh)

```log
Debian GNU/Linux 12 lc4aa0c8 ttyS0

lc4aa0c8 login: debian
Password: 
Linux lc4aa0c8 5.10.113-cluster #1 SMP PREEMPT 1 riscv64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Tue Apr  9 05:31:05 UTC 2024 on ttyS0
debian@lc4aa0c8:~$ uname -a
Linux lc4aa0c8 5.10.113-cluster #1 SMP PREEMPT 1 riscv64 GNU/Linux
debian@lc4aa0c8:~$ cat /etc/os-release 
PRETTY_NAME="Debian GNU/Linux 12 (bookworm)"
NAME="Debian GNU/Linux"
VERSION_ID="12"
VERSION="12 (bookworm)"
VERSION_CODENAME=bookworm
ID=debian
HOME_URL="https://www.debian.org/"
SUPPORT_URL="https://www.debian.org/support"
BUG_REPORT_URL="https://bugs.debian.org/"
debian@lc4aa0c8:~$ cat /etc/revyos-release 
20230614-183009
debian@lc4aa0c8:~$ 

```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。