# RevyOS Lichee Cluster 4A 版本测试报告

## 测试环境

### 操作系统信息

- 系统版本：RevyOS
- 参考安装文档：https://revyos.github.io/

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

### 使用 `ruyi` CLI 刷写镜像到板载 eMMC

安装 [`ruyi`](https://github.com/ruyisdk/ruyi) 包管理器，运行 `ruyi device provision` 并按提示操作。

镜像按照 LPi4A 选择即可。

### 登录系统

通过 SOL (Serial Over LAN) 登录系统。

BMC 默认用户名：`root`

BMC 默认密码：`0penBmc`  **注意是 `0` 而不是 `O`**

通过 `ssh -p 2301 root@lichee-rv.local` 连接

默认用户名：`debian`
默认密码：`debian`

### 常见问题

若无法使用 USB，是因为 Linux 设备树需要 patch。[patch 下载](https://dl.sipeed.com/fileList/LICHEE/LicheeCluster4A/04_Firmware/lpi4a/src/linux/0001-arch-riscv-boot-dts-lpi4a-disable-i2c-io-expander-fo.patch)

若不想手动编译 dtb，也可以考虑自行从 [预编译镜像](https://dl.sipeed.com/shareURL/LICHEE/LicheeCluster4A/04_Firmware/lpi4a/bin) 中提取 dtb（light-lpi4a.dtb）并替换 boot 下对应文件。

## 预期结果

系统正常启动，能够通过 SOL (Serial Over LAN) 登录。

## 实际结果

系统正常启动，能够通过 SOL (Serial Over LAN) 登录。

### 启动信息

屏幕录像（从刷写系统到启动）：

[![asciicast](https://asciinema.org/a/G0poBmxPbBjIfpVOC1PW2xh9y.svg)](https://asciinema.org/a/G0poBmxPbBjIfpVOC1PW2xh9y)

```log
Debian GNU/Linux 12 lpi4a ttyS0

lpi4a login: 
lpi4a login: debian

Password: 

   ____              _ ____  ____  _  __
  |  _ \ _   _ _   _(_) ___||  _ \| |/ /
  | |_) | | | | | | | \___ \| | | | ' / 
  |  _ <| |_| | |_| | |___) | |_| | . \ 
  |_| \_\\__,_|\__, |_|____/|____/|_|\_\
               |___/                    
                   -- Presented by ISCAS

  Debian GNU/Linux 12 (bookworm) (kernel 5.10.113-lpi4a)

Linux lpi4a 5.10.113-lpi4a #2023.12.08.03.26+b8c5d3546 SMP PREEMPT Fri Dec 8 03:26:13 UTC 2 riscv64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Tue Feb 28 19:16:04 CST 2023 on ttyS0
debian@lpi4a:~$
debian@lpi4a:~$ uname -a
Linux lpi4a 5.10.113-lpi4a #2023.12.08.03.26+b8c5d3546 SMP PREEMPT Fri Dec 8 03:26:13 UTC 2 riscv64 GNU/Linux
debian@lpi4a:~$ cat /etc/os-release 
PRETTY_NAME="Debian GNU/Linux 12 (bookworm)"
NAME="Debian GNU/Linux"
VERSION_ID="12"
VERSION="12 (bookworm)"
VERSION_CODENAME=bookworm
ID=debian
HOME_URL="https://www.debian.org/"
SUPPORT_URL="https://www.debian.org/support"
BUG_REPORT_URL="https://bugs.debian.org/"
debian@lpi4a:~$ 

```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。