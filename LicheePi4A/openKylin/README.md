# openKylin 2.0 alpha LPi4A 测试报告

## 测试环境

### 系统信息

- 系统版本：openKylin 2.0 alpha
- 下载链接：[https://www.openkylin.top/downloads/index-cn.html](https://www.openkylin.top/downloads/index-cn.html)
- 参考安装文档：[https://docs.openkylin.top/zh/%E7%A4%BE%E5%8C%BA%E5%BC%80%E5%8F%91%E6%8C%87%E5%8D%97/riscv%E4%B8%8A%E5%AE%89%E8%A3%85openKylin](https://docs.openkylin.top/zh/%E7%A4%BE%E5%8C%BA%E5%BC%80%E5%8F%91%E6%8C%87%E5%8D%97/riscv%E4%B8%8A%E5%AE%89%E8%A3%85openKylin)

### 硬件信息

- Lichee Pi 4A (8G RAM + 64G eMMC)
- 电源适配器
- USB to UART 调试器一个

## 安装步骤

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

通过串口登录系统。

默认用户名： `openkylin`
默认密码： `openkylin`

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

系统正常启动，成功通过板载串口登录。

### 启动信息

屏幕录像（从刷写镜像到登录系统）：

[![asciicast](https://asciinema.org/a/ewHfNb9rFIHqHfqznJgiDHapM.svg)](https://asciinema.org/a/ewHfNb9rFIHqHfqznJgiDHapM)

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

![neofetch](./neofetch.png)

### 常见问题

若桌面卡死，尝试使用非 wayland。

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。
