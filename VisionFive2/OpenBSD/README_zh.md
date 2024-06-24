# OpenBSD 7.5 VisionFive 2 测试报告

## 测试环境

### 系统信息

- 系统版本：OpenWRT SnapShot
- 下载链接：[https://cdn.openbsd.org/pub/OpenBSD/snapshots/riscv64/](https://cdn.openbsd.org/pub/OpenBSD/snapshots/riscv64/)
    - dtb 文件：https://marc.info/?l=openbsd-misc&m=169046816826966&w=2
- 参考安装文档：[https://cdn.openbsd.org/pub/OpenBSD/snapshots/riscv64/INSTALL.riscv64](https://cdn.openbsd.org/pub/OpenBSD/snapshots/riscv64/INSTALL.riscv64)
    -  社区教程：https://gist.github.com/csgordon/74658096f7838382b40bd64e11f6983e

### 硬件信息

- StarFive VisionFive
- 电源适配器
- microSD 卡一张
- USB to UART 调试器一个
- Internet 有线网连接

## 安装步骤

### 刷写安装镜像

使用 `gzip` 解压镜像。
使用 `dd` 将镜像写入 microSD 卡。

```bash
wget https://cdn.openbsd.org/pub/OpenBSD/snapshots/riscv64/install75.img
sudo dd if=install75.img of=/dev/your-device bs=1M status=progress
```

将 dtb 文件放入 EFI 根目录中：

```bash
mkdir -p mnt
sudo mount /dev/your-device-p1 mnt
cp jh7110-starfive-visionfive-2-v1.3b.dtb mnt/
sudo umount mnt
```

### 启动系统

手动中断 u-boot 流程，并输入启动命令：
```bash
load mmc 1:1 ${fdt_addr_r} jh7110-starfive-visionfive-2-v1.3b.dtb
load mmc 1:1 ${kernel_addr_r} efi/boot/bootriscv64.efi
bootefi ${kernel_addr_r} ${fdt_addr_r}
```

跟随流程安装，然后将 dtb 再次放入 EFI 根目录内（若其被覆盖）。

### 持久化 uboot

```bash
env default -a -f
setenv bootcmd "load mmc 1:1 ${fdt_addr_r} jh7110-starfive-visionfive-2-v1.3b.dtb; load mmc 1:1 ${kernel_addr_r} efi/boot/bootriscv64.efi; bootefi ${kernel_addr_r} ${fdt_addr_r}"
saveenv
```

### 登录系统

通过串口登录系统。

用户和密码在安装时被设置。

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

系统正常启动，成功通过板载串口登录。

### 启动信息

屏幕录像（从刷写镜像到登录系统）：

[![asciicast](https://asciinema.org/a/Cz0uvucqmbP1P0yzgZ2hnMbZY.svg)](https://asciinema.org/a/Cz0uvucqmbP1P0yzgZ2hnMbZY)


```log
Tue Mar 26 22:01:09 CST 2024

OpenBSD/riscv64 (plct.my.domain) (console)

login: root
Password:
OpenBSD 7.5 (GENERIC.MP) #1: Fri Mar 22 19:01:44 MDT 2024

Welcome to OpenBSD: The proactively secure Unix-like operating system.

Please use the sendbug(1) utility to report bugs in the system.
Before reporting a bug, please try to reproduce it with the latest
version of the code.  With bug reports, please try to ensure that
enough information to reproduce the problem is enclosed, and if a
known fix for it exists, include that as well.

You have new mail.
plct# uname -a
OpenBSD plct.my.domain 7.5 GENERIC.MP#1 riscv64
plct#             

```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。