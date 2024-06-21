# openKylin Lichee Cluster 4A 版本测试报告

## 测试环境

### 操作系统信息

- 系统版本：openKylin 2.0 alpha
- 下载链接：[https://www.openkylin.top/downloads/index-cn.html](https://www.openkylin.top/downloads/index-cn.html)
- 参考安装文档：[https://docs.openkylin.top/zh/%E7%A4%BE%E5%8C%BA%E5%BC%80%E5%8F%91%E6%8C%87%E5%8D%97/riscv%E4%B8%8A%E5%AE%89%E8%A3%85openKylin](https://docs.openkylin.top/zh/%E7%A4%BE%E5%8C%BA%E5%BC%80%E5%8F%91%E6%8C%87%E5%8D%97/riscv%E4%B8%8A%E5%AE%89%E8%A3%85openKylin)

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

### 刷写 bootloader

解压安装套件。
进入 fastboot 工具所在目录。
刷入 u-boot 与 boot。

```bash
tar -xvf openKylin-2.0-alpha-licheepi4a.tar.xz
cd openkylin-2.0-alpha-licheepi4a/fastboot/linux
sudo ./fastboot flash ram ../../images/$(ram_size)/u-boot-nonsec-2020.10-r0-noswap.bin
sudo ./fastboot reboot
sudo ./fastboot flash uboot ../../images/$(ram_size)/u-boot-nonsec-2020.10-r0-noswap.bin
sudo ./fastboot flash boot ../../images/$(ram_size)/boot.ext4
```

### 刷写镜像

将 root 分区刷入 eMMC 中。

```bash
sudo ./fastboot flash root ../../images/openkylin-2.0-alpha-licheepi4a-riscv64.ext4
```

### 登录系统

通过 SOL (Serial Over LAN) 登录系统。

BMC 默认用户名：`root`

BMC 默认密码：`0penBmc` **注意是 `0` 而不是 `O`**

通过 `ssh -p 2301 root@lichee-rv.local` 连接

默认用户名： `openkylin`
默认密码： `openkylin`

### 常见问题

若无法使用 USB，是因为 Linux 设备树需要 patch。[patch 下载](https://dl.sipeed.com/fileList/LICHEE/LicheeCluster4A/04_Firmware/lpi4a/src/linux/0001-arch-riscv-boot-dts-lpi4a-disable-i2c-io-expander-fo.patch)

若不想手动编译 dtb，也可以考虑自行从 [预编译镜像](https://dl.sipeed.com/shareURL/LICHEE/LicheeCluster4A/04_Firmware/lpi4a/bin) 中提取 dtb（light-lpi4a.dtb）并替换 boot 下对应文件。

## 预期结果

系统正常启动，能够通过 SOL (Serial Over LAN) 登录。

## 实际结果

系统正常启动，能够通过 SOL (Serial Over LAN) 登录。

### 启动信息

屏幕录像（从刷写系统到启动）：

[![asciicast](https://asciinema.org/a/d4d3yatzsx13CRtcdqV0RF7Td.svg)](https://asciinema.org/a/d4d3yatzsx13CRtcdqV0RF7Td)

```log
openKylin 2.0 openkylin ttyS0

openkylin login: openkylin
输入密码
Welcome to openKylin 2.0 (GNU/Linux 5.10.113-yocto-standard riscv64)

 * Support:        https://openkylin.top

The programs included with the openKylin system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

openKylin comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

openkylin@openkylin:~$ uname -a
Linux openkylin 5.10.113-yocto-standard #1 SMP PREEMPT Tue Dec 26 12:49:40 UTC 2023 riscv64 riscv64 riscv64 GNU/Linux
openkylin@openkylin:~$ cat /etc/os-release 
NAME="openKylin"
FULL_NAME="openKylin"
VERSION="2.0 (nile)"
VERSION_US="2.0 (nile)"
ID=openkylin
PRETTY_NAME="openKylin 2.0"
VERSION_ID="2.0"
HOME_URL="https://www.openkylin.top/"
VERSION_CODENAME=nile
PRODUCT_FEATURES=3
openkylin@openkylin:~$ 

```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。