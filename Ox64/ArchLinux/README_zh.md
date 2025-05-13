# Arch Linux Pine64 Ox64 测试报告

## 测试环境

### 操作系统信息

- 下载链接：https://github.com/domhathair/pine64_ox64_archlinux/releases/download/v2024.06.1/sdcard.tar.gz
  - SDK：https://github.com/bouffalolab/bl_mcu_sdk
  - 烧录工具：https://openbouffalo.org/static-assets/bldevcube/BouffaloLabDevCube-v1.8.3.zip
- 参考安装文档：https://github.com/domhathair/pine64_ox64_archlinux

### 硬件信息

- Pine64 Ox64
- Type-C 或者 microUSB 线一根
- 一个 UART 调试器 （推荐 CH340G，不建议使用 CP2102）
- 一张 microSD 卡
- 一个 microSD 读卡器

## 安装步骤

### 获取镜像

下载并解压预编译镜像和固件：
```bash
wget https://github.com/openbouffalo/buildroot_bouffalo/releases/download/v1.0.1/bl808-linux-pine64_ox64_full_defconfig.tar.gz
tar -xvf bl808-linux-pine64_ox64_full_defconfig.tar.gz
cd bl808-linux-pine64_ox64_full_defconfig/firmware
xz -d sdcard-pine64_ox64_full_defconfig.img.xz
```

### 串口方式刷写程序

按住 BOOT 按钮的同时通过 microUSB 或 Type-C 接口上电。将烧录用 UART (pin 14 & 15) 分别连接到调试器的 RX 和 TX。

下载烧录工具后使用对应系统的工具烧录。请确保所使用的 BLDevCube 版本为 1.8.3 **或更早**。

进入 MCU 页面，按如下所示设置参数：

M0: Group: group0, Image Addr: `0x58000000`, 选择 `m0_lowload_bl808_m0.bin`

M0: Group: group0, Image Addr: `0x58100000`, 选择 `d0_lowload_bl808_d0.bin`

选择对应的 UART 接口，波特率 2000000。点击 "Create & Download" 进行刷写。

![mcu](./mcu.png)

然后进入 IOT 页面，按如下所示设置参数：

选中 "Single Download", 地址 `0x800000`， 选择 `bl808-firmware.bin`。点击 "Create & Download" 进行刷写。

![iot](./iot.png)

### 将镜像烧写至 SD 卡

```shell
wget https://github.com/domhathair/pine64_ox64_archlinux/releases/download/v2024.06.1/sdcard.tar.gz
tar -xvf sdcard.tar.gz
dd if=sdcard.img of=/dev/your/device status=progress
```

### 启动系统

插入 SD 卡，将串口 UART (pin 32 & 31) 分别连接到调试器的 RX 和 TX。注意设置 波特率为 2000000。

默认用户名：`root`
默认密码：`archriscv`

## 预期结果

系统正常启动，能够看到串口输出。

## 实际结果

系统正常启动，能够看到串口输出。

### 启动信息

```log
Arch Linux 6.5.11 (hvc0)

buildroot login:
Arch Linux 6.5.11 (ttyS0)

buildroot login: root
Password:
[root@buildroot ~]# uname -a
Linux buildroot 6.5.11 #1 Fri Jun 28 00:07:35 MSK 2024 riscv64 GNU/Linux
[root@buildroot ~]# cat /etc/os-release
NAME="Arch Linux"
PRETTY_NAME="Arch Linux"
ID=arch
BUILD_ID=rolling
ANSI_COLOR="38;2;23;147;209"
HOME_URL="https://archlinux.org/"
DOCUMENTATION_URL="https://wiki.archlinux.org/"
SUPPORT_URL="https://bbs.archlinux.org/"
BUG_REPORT_URL="https://gitlab.archlinux.org/groups/archlinux/-/issues"
PRIVACY_POLICY_URL="https://terms.archlinux.org/docs/privacy-policy/"
LOGO=archlinux-logo
[root@buildroot ~]# lscpu
Architecture:           riscv64
  Byte Order:           Little Endian
CPU(s):                 1
  On-line CPU(s) list:  0
Vendor ID:              0x5b7
  Model name:           -
    CPU family:         0x0
    Model:              0x0
    Thread(s) per core: 1
    Core(s) per socket: 1
    Socket(s):          1
[root@buildroot ~]#
```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。