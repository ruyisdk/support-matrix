# Buildroot Icicle Kit 测试报告

## 测试环境

### 系统信息

### 操作系统信息

- 系统版本：Buildroot
- 源码链接：https://buildroot.org/download.html
    - 截止本文编写时，Buildroot 的最新稳定 / LTS 版本为：[buildroot-2024.02.2](https://buildroot.org/downloads/buildroot-2024.02.2.tar.gz)
- 参考安装文档：https://gitlab.com/buildroot.org/buildroot/-/tree/master/board/visionfive?ref_type=heads
- 构建机系统：Arch Linux x86_64

### 硬件信息

- Microchip Polarfire SoC FPGA Icicle Kit 开发板
- 原装 12V 5A DC 5.5*2.1mm 电源适配器（原厂附带线材为美标插脚，在中国大陆使用需要转接器/更换国标线材）
- micro-USB to USB-A 线缆两条（出厂附带），用于连接 USB-UART、更新 FPGA/HSS 和烧录镜像至板载 eMMC
- （可选）SD 卡一张（不推荐使用 microSD + 卡套转接的方式，可能无法识别；此外请确保存储卡没有处于写保护状态）

## 构建及刷写镜像

由于 PolarFire SoC FPGA Icicle Kit 的 Buildroot 已经主线化，直接从 Buildroot 获取源码即可构建出可用镜像。

### 准备构建环境

```shell
sudo pacman -S which sed make binutils diffutils gcc bash patch gzip bzip2 perl tar cpio unzip rsync file bc findutils wget
# 或者从 AUR 安装，需要 AUR Helper，如 yay, paru 等
# paru -S buildroot-meta
```

若您不使用 Arch Linux，请参考 [官方文档](https://buildroot.org/downloads/manual/manual.html#requirement) 安装所需依赖（注意，软件包名称可能不一致）。

### 构建镜像

```shell
wget https://buildroot.org/downloads/buildroot-2024.02.2.tar.gz
tar xvf buildroot-2024.02.2.tar.gz
cd buildroot-2024.02.2/
make microchip_mpfs_icicle_defconfig
make -j$(nproc)
```

Note: 请确保您的互联网连接正常，编译过程中会自动下载依赖。

构建结束后将在 `output/images` 生成 `sdcard.img` 镜像。

### （可选）更新 FPGA Design 和 Hart Software Services (HSS)

此操作并非必须，如果遇到问题可尝试更新 FPGA 和 HSS。

参考 [Ubuntu](../Ubuntu/README.md) 中提到的步骤进行更新。

### 烧写镜像

Polarfire SoC FPGA Icicle Kit 支持从板载 eMMC 启动或 SD 卡启动。

默认优先 SD 卡。当 SD 卡不存在或 SD 卡启动失败时会从板载 eMMC 启动。

### 烧录镜像至 eMMC

连接 microUSB 线缆至 USB OTG 接口，位于 SD 卡槽附近，丝印 `J19`。

连接 USB UART，位于以太网接口一侧，丝印 `J11`。

计算机上会识别到一个 CP2108 USB 转 UART，如果这是您计算机上唯一一个 USB 转 UART，此时会识别到四个串口。

Windows 上会出现四个 COM 口，Linux 下会出现 /dev/ttyUSB{0,1,2,3}。

其中，`Interface 0` 为 `HSS` 输出，`Interface 1` 为 U-Boot 和 Linux 控制台输出。

在 Linux 系统下，分别对应第一个和第二个串口。

| 串口功能              | Windows     | Linux        |
|--------------------|-------------|--------------|
| HSS 控制台            | Interface 0 | /dev/ttyUSB0 |
| U-Boot & Linux 控制台 | Interface 1 | /dev/ttyUSB1 |

欲向 eMMC 烧录镜像，连接至 `HSS` 控制台，在启动时（提示 `Press a key to enter CLI, ESC to skip`）按任意键打断启动流程。

输入：

```
mmc
usbdmsc
```

会提示 `Waiting for USB Host to connect`。

此时计算机一侧应该会出现一个 USB 大容量存储设备。至此可以使用 Win32DiskImager/Rufus/USBImager/dd 等工具直接向其中写入镜像了。

镜像烧写完成后，在 HSS 控制台按 Ctrl+C 退出 USB 存储模式。至此镜像烧录结束。

### 烧录镜像至 SD 卡

直接使用 Rufus/Win32DiskImager/dd 等工具写入镜像至 SD 卡即可。

```shell
sudo dd if=sdcard.img of=/dev/sdX bs=1M status=progress
```

### 登录系统

通过串口登录系统。

默认用户名： `root`

默认密码：无，输入用户名后自动登录

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

系统正常启动，成功通过板载串口登录。

### 启动信息

```log
Welcome to Buildroot
mpfs_icicle login: root
# uname -a
Linux mpfs_icicle 6.1.74-linux4microchip+fpga-2024.02 #1 SMP Mon May 13 18:29:54 CST 2024 riscv64 GNU/Linux
# cat /etc/os-release
NAME=Buildroot
VERSION=2024.02.2
ID=buildroot
VERSION_ID=2024.02.2
PRETTY_NAME="Buildroot 2024.02.2"
# cat /proc/cpuinfo
processor       : 0
hart            : 1
isa             : rv64imafdc
mmu             : sv39
uarch           : sifive,u54-mc
mvendorid       : 0x1cf
marchid         : 0x1
mimpid          : 0x0

processor       : 1
hart            : 2
isa             : rv64imafdc
mmu             : sv39
uarch           : sifive,u54-mc
mvendorid       : 0x1cf
marchid         : 0x1
mimpid          : 0x0

processor       : 2
hart            : 3
isa             : rv64imafdc
mmu             : sv39
uarch           : sifive,u54-mc
mvendorid       : 0x1cf
marchid         : 0x1
mimpid          : 0x0

processor       : 3
hart            : 4
isa             : rv64imafdc
mmu             : sv39
uarch           : sifive,u54-mc
mvendorid       : 0x1cf
marchid         : 0x1
mimpid          : 0x0

#
```

屏幕录像（从刷写镜像到登录系统）：

[![asciicast](https://asciinema.org/a/js18pAh0YMTp0g9bQD1tXsBgH.svg)](https://asciinema.org/a/js18pAh0YMTp0g9bQD1tXsBgH)

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。