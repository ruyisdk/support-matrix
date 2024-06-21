# Fedora 38 LPi4A chainsx 版本 测试报告

## 测试环境

### 系统信息

- 系统版本：Fedora 38
- 下载链接：[https://github.com/chainsx/fedora-riscv-builder/releases](https://github.com/chainsx/fedora-riscv-builder/releases)
- 参考安装文档：[https://wiki.sipeed.com/hardware/zh/lichee/th1520/lpi4a/4_burn_image.html](https://wiki.sipeed.com/hardware/zh/lichee/th1520/lpi4a/4_burn_image.html)
- fastboot 链接：
    - [https://pan.baidu.com/e/1xH56ZlewB6UOMlke5BrKWQ](https://pan.baidu.com/e/1xH56ZlewB6UOMlke5BrKWQ)
    - [https://mega.nz/folder/phoQlBTZ#cZeQ3qZ__pDvP94PT3_bGA](https://mega.nz/folder/phoQlBTZ#cZeQ3qZ__pDvP94PT3_bGA)

### 硬件信息

- Lichee Pi 4A (8G RAM + 64G eMMC)
- 电源适配器
- microSD 卡一张
- USB to UART 调试器一个

## 安装步骤

### 刷写 bootloader

进入 fastboot。
- 正式版确认 boot 拨码开关为 eMMC。
- 按动 BOOT 同时上电。
- （详见官方教程）
使用 fastboot 按命令烧录 u-boot。

```bash
sudo ./fastboot flash ram ./path/to/your/lpi4a-($ram_size)gb-u-boot-with-spl.bin
sudo ./fastboot reboot
sleep 10
sudo ./fastboot flash uboot ./path/to/your/lpi4a-($ram_size)gb-u-boot-with-spl.bin
```

### 刷写镜像

使用 `unxz` 解压镜像。
使用 `dd` 将镜像写入 microSD 卡。

```bash
unxz /path/to/fedora.raw.xz
sudo dd if=/path/to/fedora.raw of=/dev/your_device bs=1M status=progress
```

### 登录系统

通过串口登录系统。

默认用户名： `root`
默认密码： `fedora`

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

系统正常启动，成功通过板载串口登录。

### 启动信息

屏幕录像（从刷写镜像到登录系统）：

[![asciicast](https://asciinema.org/a/EkD4lbohO4sNJGO518rLQtL59.svg)](https://asciinema.org/a/EkD4lbohO4sNJGO518rLQtL59)

```log
Fedora Linux 38 (Thirty Eight)
Kernel 5.10.113-g052b22ef8baf on an riscv64 (ttyS0)

fedora-riscv login: root
Password: 
Last login: Thu May 11 00:00:31 on ttyS0
[root@fedora-riscv ~]# [   35.894822] soc_dovdd18_scan: disabling
[   35.899400] soc_dvdd12_scan: disabling
[   35.903909] soc_avdd28_scan_en: disabling

[root@fedora-riscv ~]# uname -a
Linux fedora-riscv 5.10.113-g052b22ef8baf #1 SMP PREEMPT Thu Sep 14 05:05:31 UTC 2023 riscv64 GNU/Linux
[root@fedora-riscv ~]# cat /etc/os-release 
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