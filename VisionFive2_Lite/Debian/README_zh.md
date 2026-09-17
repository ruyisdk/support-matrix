# Debian VisionFive 2 Lite 版本测试报告

## 测试环境

### 操作系统信息

- 系统版本：Debian GNU/Linux trixie/sid（StarFive Debian 202510 Engineering Release）
- 下载链接：[https://github.com/starfive-tech/Debian/](https://github.com/starfive-tech/Debian/releases/download/v0.15.0-engineering-release-wayland/starfive-jh7110-202510-minimal-desktop-wayland.img.bz2)
- 参考安装文档：[刷机操作系统到板载eMMC（eMMC版本）](https://doc-en.rvspace.org/VisionFive2Lite/VisionFive2LiteQSG/VisionFive2_QSGLite/flashing_os_to_onboard_emmc_emmc_version.html)

### 硬件信息

- VisionFive 2 Lite；
- USB-TTL；
- Type-C 数据线；
- 3 根杜邦线

## 安装步骤

### 解压镜像

下载镜像`starfive-jh7110-202510-minimal-desktop-wayland.img.bz2`并得到：

```text
starfive-jh7110-202510-minimal-desktop-wayland.img
```

### 准备刷写工具

需要以下工具：

```
fastboot
img2simg
```

Ubuntu/Debian 主机可执行：

```
sudo apt update
sudo apt install -y fastboot android-sdk-libsparse-utils
```

Windows 主机可安装 Android Platform Tools 获取 `fastboot`，并通过 WSL 或其他 Linux 环境安装 `android-sdk-libsparse-utils` 获取 `img2simg`。

### 连接串口

使用 USB to UART 调试器连接 VisionFive 2 Lite：

```
VisionFive 2 Lite GND -> USB-UART GND
VisionFive 2 Lite TX  -> USB-UART RX
VisionFive 2 Lite RX  -> USB-UART TX
```

使用串口终端连接开发板，串口参数设置为：

```
Baud rate:    115200
Data bits:    8
Parity:       none
Stop bits:    1
Flow control: none
```

同时使用 USB Type-C 线缆将 VisionFive 2 Lite 连接至主机。

### 进入 Fastboot 模式

给开发板上电，在 U-Boot 启动倒计时时按任意键中断自动启动，进入 U-Boot。

执行：

```
fastboot usb 0
```

在主机中确认 Fastboot 设备：

```
fastboot devices
```

能够看到类似：

```
<device_serial>    fastboot
```

说明开发板已经正常进入 Fastboot 模式。

### 转换 Sparse 镜像

进入镜像所在目录：

```
cd <path-to-image>
```

执行：

```
img2simg \
starfive-jh7110-202510-minimal-desktop-wayland.img \
starfive-jh7110-202510-minimal-desktop-wayland-sparse.img
```

转换完成后得到：

```
starfive-jh7110-202510-minimal-desktop-wayland-sparse.img
```

### 刷写镜像至 eMMC

再次确认 Fastboot 设备：

```
fastboot devices
```

将 sparse 镜像刷写至板载 eMMC：

```
fastboot flash mmc0 starfive-jh7110-202510-minimal-desktop-wayland-sparse.img
```

本次测试实际刷写结果如下：

```
Sending sparse 'mmc0' 1/4 (1044499 KB)             OKAY [ 30.351s]
Writing 'mmc0'                                     OKAY [ 30.389s]
Sending sparse 'mmc0' 2/4 (1047329 KB)             OKAY [ 30.142s]
Writing 'mmc0'                                     OKAY [ 27.204s]
Sending sparse 'mmc0' 3/4 (1006939 KB)             OKAY [ 29.268s]
Writing 'mmc0'                                     OKAY [ 29.344s]
Sending sparse 'mmc0' 4/4 (783420 KB)              OKAY [ 22.683s]
Writing 'mmc0'                                     OKAY [ 20.660s]
Finished. Total time: 222.577s
```

刷写完成后关闭开发板电源，等待数秒后重新上电。

### 登录系统

通过串口登录系统。

默认用户名：`user`
默认密码：`starfive`

## 预期结果

系统正常启动，能够通过串口登录。

## 实际结果

系统正常启动，成功通过串口登录。

### 启动信息

```log
Debian GNU/Linux trixie/sid starfive ttyS0

starfive login: user
Password:
Linux starfive 6.12.5-starfive #70SF SMP Sun Sep 28 11:33:07 UTC 2025 riscv64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
[   37.017948] mipi_0p9: disabling
user@starfive:~$ uname -a
Linux starfive 6.12.5-starfive #70SF SMP Sun Sep 28 11:33:07 UTC 2025 riscv64 GNU/Linux
user@starfive:~$ cat /etc/os-release
PRETTY_NAME="Debian GNU/Linux trixie/sid"
NAME="Debian GNU/Linux"
VERSION_CODENAME=trixie
ID=debian
HOME_URL="https://www.debian.org/"
SUPPORT_URL="https://www.debian.org/support"
BUG_REPORT_URL="https://bugs.debian.org/"
BUILD_ID=70
BUILD_DATE=T2025-09-30
user@starfive:~$ cat /proc/cpuinfo
processor       : 0
hart            : 1
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd_zba_zbb
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x4210427
hart isa        : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd_zba_zbb

processor       : 1
hart            : 2
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd_zba_zbb
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x4210427
hart isa        : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd_zba_zbb

processor       : 2
hart            : 3
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd_zba_zbb
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x4210427
hart isa        : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd_zba_zbb

processor       : 3
hart            : 4
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd_zba_zbb
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x4210427
hart isa        : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd_zba_zbb

user@starfive:~$
```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。