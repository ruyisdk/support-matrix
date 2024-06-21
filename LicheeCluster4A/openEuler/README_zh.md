# openEuler Lichee Cluster 4A 版本测试报告

## 测试环境

### 操作系统信息

- 系统版本：openEuler 23.09 RISC-V preview
- 下载链接：https://mirror.iscas.ac.cn/openeuler-sig-riscv/openEuler-RISC-V/preview/openEuler-23.09-V1-riscv64/lpi4a/
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

BMC 默认密码：`0penBmc` **注意是 `0` 而不是 `O`**

通过 `ssh -p 2301 root@lichee-rv.local` 连接

默认用户名：`openeuler` 或 `root`
默认密码：`openEuler12#$`

### 常见问题

若无法使用 USB，是因为 Linux 设备树需要 patch。[patch 下载](https://dl.sipeed.com/fileList/LICHEE/LicheeCluster4A/04_Firmware/lpi4a/src/linux/0001-arch-riscv-boot-dts-lpi4a-disable-i2c-io-expander-fo.patch)

若不想手动编译 dtb，也可以考虑自行从 [预编译镜像](https://dl.sipeed.com/shareURL/LICHEE/LicheeCluster4A/04_Firmware/lpi4a/bin) 中提取 dtb（light-lpi4a.dtb）并替换 boot 下对应文件。

## 预期结果

系统正常启动，能够通过 SOL (Serial Over LAN) 登录。

## 实际结果

系统正常启动，能够通过 SOL (Serial Over LAN) 登录。

### 启动信息

屏幕录像（从刷写系统到启动）：

[![asciicast](https://asciinema.org/a/PtLMh7Dm2RX3C4RPoTajplYbj.svg)](https://asciinema.org/a/PtLMh7Dm2RX3C4RPoTajplYbj)

```log
Authorized users only. All activities may be monitored and reported.
openeuler-riscv64 login: openeuler
Password: 
Last login: Tue Apr  2 10:35:06 on ttyS0

Authorized users only. All activities may be monitored and reported.


Welcome to 5.10.113

System information as of time:  Tue Apr  2 10:35:58 AM CST 2024

System load:    0.84
Processes:      144
Memory used:    2.2%
Swap used:      0.0%
Usage On:       13%
IP address:     192.168.36.10
Users online:   1
To run a command as administrator(user "root"),use "sudo <command>".
[openeuler@openeuler-riscv64 ~]$ uname -a
Linux openeuler-riscv64 5.10.113 #1 SMP PREEMPT Wed Nov 22 16:04:58 UTC 2023 riscv64 riscv64 riscv64 GNU/Linux
[openeuler@openeuler-riscv64 ~]$ cat /etc/os-release 
NAME="openEuler"
VERSION="23.09"
ID="openEuler"
VERSION_ID="23.09"
PRETTY_NAME="openEuler 23.09"
ANSI_COLOR="0;31"

[openeuler@openeuler-riscv64 ~]$ 

```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。