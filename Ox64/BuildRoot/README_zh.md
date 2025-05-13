# BuildRoot Pine64 Ox64 测试报告

## 测试环境

### 操作系统信息

- 下载链接：https://github.com/openbouffalo/buildroot_bouffalo/releases/download/v1.0.1/bl808-linux-pine64_ox64_full_defconfig.tar.gz
  - SDK：https://github.com/bouffalolab/bl_mcu_sdk
  - 烧录工具：https://openbouffalo.org/static-assets/bldevcube/BouffaloLabDevCube-v1.8.3.zip
- 参考安装文档：https://www.hackster.io/lupyuen/8-risc-v-sbc-on-a-real-time-operating-system-ox64-nuttx-474358

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
dd if=sdcard-pine64_ox64_full_defconfig.img of=/dev/your/device status=progress
```

### 启动系统

插入 SD 卡，将串口 UART (pin 32 & 31) 分别连接到调试器的 RX 和 TX。注意设置 波特率为 2000000。

## 预期结果

系统正常启动，能够看到串口输出。

## 实际结果

系统正常启动，能够看到串口输出。

### 启动信息

```log
swapon: /dev/mmcblk0p1: read swap header failed
Resizing Rootfs
CHANGED: partition=3 start=2506786 old: size=1048576 end=3555361 new: size=59827133 end=62333918
Partition Resized
resize2fs 1.46.5 (30-Dec-2021)
Filesystem at /dev/mmcblk0p3 is mounted on /; on-line resizing required
old_desc_blocks = 1, new_desc_blocks = 2
[    3.120120] EXT4-fs (mmcblk0p3): resizing filesystem from 131072 to 7478391 blocks
[    3.805460] EXT4-fs (mmcblk0p3): resized filesystem to 7478391
The filesystem on /dev/mmcblk0p3 is now 7478391 (4k) blocks long.

Rootfs Resized
Running mkswap
Setting up swapspace version 1, size = 1024 MiB (1073737728 bytes)
no label, UUID=d4bded1e-1d6b-44f1-a861-45c71d817090
[    4.139249] Adding 1048572k swap on /dev/mmcblk0p1.  Priority:-2 extents:1 across:1048572k SS
Swap Partition Formatted
Starting syslogd: OK
Starting klogd: OK
Running sysctl: OK
Starting mdev... OK
Saving random seed: OK
Starting rpcbind: OK
Starting iptables: OK
Starting network: OK
Starting dhcpcd...
dhcpcd-9.4.1 starting
dhcp_vendor: Invalid argument
forked to background, child pid 131
Starting sntp: sntp 4.2.8p15@1.3728-o Mon Mar  6 10:45:15 UTC 2023 (1)
pool.ntp.org lookup error Temporary failure in name resolution
FAIL
Starting ntpd: OK
Starting dropbear sshd: OK

Welcome to Buildroot
ox64 login: root
Last login: Thu Jan  1 00:00:35 on console
# uname -a
Linux ox64 6.2.0 #1 Mon Mar  6 11:17:27 UTC 2023 riscv64 GNU/Linux
# cat /etc/os-release
NAME=Buildroot
VERSION=2022.11.1
ID=buildroot
VERSION_ID=2022.11.1
PRETTY_NAME="Buildroot 2022.11.1"
#

```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。