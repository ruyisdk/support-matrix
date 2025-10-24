# openEuler RISC-V HiFive Unmatched 版本测试报告

## 测试环境

### 操作系统信息

- 系统版本：openEuler 24.03 LTS SP2
- 下载链接：https://www.openeuler.openatom.cn/zh/download/#openEuler%2024.03%20LTS%20SP2
- 参考安装文档
    - https://ruyisdk.cn/t/topic/1525
    - https://wiki.debian.org/InstallingDebianOn/SiFive/HiFiveUnmatched

> [!NOTE]
> 此镜像为 openEuler 主线 riscv64 DVD ISO。
> 需要搭配支持 EFI 的主线 U-Boot 使用。
> 本次并未安装显卡进行图形界面测试，理论上安装显卡后应当可以正常使用桌面环境。

### 硬件信息

- HiFive Unmatched Rev A
- microUSB 线缆一条（随 HiFive Unmatched 附赠）
- ATX 电源一个
- microSD 卡一张或 U 盘一个（大小足够烧录 openEuler ISO 镜像）
- M.2 NVMe SSD
- 可用的网络连接

如需使用图形界面：

- PCI-E 显卡一张
- USB 键盘&鼠标
- 显示器（以及所需线缆）

## 安装步骤

### 构建并烧录 U-Boot 至 SPI Flash

需要在 Unmatched 上已经有能运行的操作系统。

可从 Debian 获取可用的 U-Boot 二进制。

```shell
wget http://deb.debian.org/debian/pool/main/u/u-boot/u-boot-sifive_2025.01-3_riscv64.deb
dpkg -x u-boot-sifive_2025.01-3_riscv64.deb .
# 如果使用的不是 Debian，可使用 7-Zip
# 7z x u-boot-sifive_2025.01-3_riscv64.deb
# tar xvf data.tar
# 或使用 ar
# ar x u-boot-sifive_2025.01-3_riscv64.deb
# tar xvf data.tar.xz
cd usr/lib/u-boot/sifive_unmatched
sudo modprobe mtdblock
sgdisk --clear -a 1 \
    --new=1:40:2087     --change-name=1:spl   --typecode=1:5B193300-FC78-40CD-8002-E86C45580B47 \
    --new=2:2088:10279  --change-name=2:uboot --typecode=2:2E54B353-1271-4842-806F-E436D6AF6985 \
    --new=3:10280:10535 --change-name=3:env   --typecode=3:3DE21764-95BD-54BD-A5C3-4ABE786F38A8 \
    /dev/mtdblock0
dd if=u-boot-spl.bin of=/dev/mtdblock0 bs=4096 seek=5 conv=sync
dd if=u-boot.itb  of=/dev/mtdblock0 bs=4096 seek=261 conv=sync
```

刷写完成后，正常关闭开发板。

### 引导设备选择

确保拨码开关已调整为从 SPI 引导。若您未更改，出厂默认应为从 microSD 卡引导。

拨码开关应如下设置：`MSEL[3:0]=1011`

### 使用 `dd` 刷写镜像到 microSD 卡或 U 盘

> [!WARNING]
> U 盘/存储卡上所有数据都将丢失！
> 数据无价，务必备份好再进行下一步操作。

```shell
wget https://dl-cdn.openeuler.openatom.cn/openEuler-24.03-LTS-SP2/ISO/riscv64/openEuler-24.03-LTS-SP2-netinst-riscv64-dvd.iso
sudo wipefs -af /dev/sdX
sudo dd if=openEuler-24.03-LTS-SP2-netinst-riscv64-dvd.iso of=/dev/sdX bs=1M status=progress
sync; sudo eject /dev/sdX
```

拔掉 U 盘，插入 Unmatched 的任意 USB 口。

如果是烧录到了存储卡，将存储卡插入 microSD 卡槽。

### 系统安装

Unmatched 提供两个串口，第二个为 CPU 串口。

如果没有安装显卡，openEuler 的 Anaconda 安装器默认会从串口输出。

本次使用串口终端，使用纯文本安装器。

（此方式操作并不算方便，如果条件允许的情况下，建议还是安装显卡然后使用图形化安装器。）

参考[此屏幕录像](https://asciinema.org/a/HncsUaCkyzLLomdo1rmwFT7hF)的流程进行安装。

需要注意的一些问题：

1. 需要手动填入网络安装源，例如 https://repo.openeuler.org/openEuler-24.03-LTS-SP2/OS/riscv64/
2. 安装 GRUB 时可能遇到问题，遇到如下提示时先选择 yes：
```
Question

The following error occurred while installing the boot loader. The system will                                          
not be bootable. Would you like to ignore this and continue with installation?                                          

Failed to set new efi boot target. This is most likely a kernel or firmware bug.

Please respond 'yes' or 'no'
```
3. 默认安装的 GRUB EFI 无法被 U-Boot 识别，安装完成并重启后，拔除安装介质，进入 U-Boot 后，打断启动，运行如下命令临时启动系统：

```shell
nvme scan
load nvme 0:1 $kernel_addr_r /EFI/openEuler/grubriscv64.efi
bootefi $kernel_addr_r
```
4. 进入系统后，需要将 GRUB 以 `--removable` 安装，使 U-Boot 可以自动识别并启动：

```shell
dnf install -y grub2-efi-riscv64-modules
grub2-install --removable
grub2-mkconfig -o /boot/grub2/grub.cfg
```

### 登录系统

通过板载串口（使用 microUSB 线缆连接至其他计算机）登录系统。

默认用户名和密码为安装时配置。

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

系统正常启动，成功通过板载串口登录。

### 启动信息

```log
Welcome to 6.6.0-98.0.0.103.oe2403sp2.riscv64

System information as of time:  Fri Sep 19 09:43:03 PM CST 2025

System load:    3.39
Memory used:    1.6%
Swap used:      0%
Usage On:       3%
IP address:     10.0.0.116
Users online:   1


[root@localhost ~]# cat /etc/os-release
NAME="openEuler"
VERSION="24.03 (LTS-SP2)"
ID="openEuler"
VERSION_ID="24.03"
PRETTY_NAME="openEuler 24.03 (LTS-SP2)"
ANSI_COLOR="0;31"

[root@localhost ~]# cat[   70.739081][ T5034] Btrfs loaded, zoned=yes, fsverity=no
 /sys/firmware/[   72.697419][ T5276] systemd-rc-local-generator[5276]: /etc/rc.d/rc.local is not marked executable, skipping.

devicetree/ efi/        fdt
[root@localhost ~]# cat /sys/firmware/[  OK  ] Reached target Multi-User System.
         Starting Record Runlevel Change in UTMP...
[  OK  ] Finished openEuler Security Tool.
[  OK  ] Finished Record Runlevel Change in UTMP.
devicetree/base/
#address-cells   config/          memory@80000000/ serial-number
aliases/         cpus/            model            #size-cells
binman/          fit-images/      name             soc/
chosen/          gpio-poweroff/   reserved-memory/
compatible       hfclk/           rtcclk/
[root@localhost ~]# cat /sys/firmware/devicetree/base/model
SiFive HiFive Unmatched A00[root@localhost ~]# cat /proc/cpuinfo
processor       : 0
hart            : 2
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd
mmu             : sv39
uarch           : sifive,bullet0
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x20181004

processor       : 1
hart            : 1
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd
mmu             : sv39
uarch           : sifive,bullet0
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x20181004

processor       : 2
hart            : 3
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd
mmu             : sv39
uarch           : sifive,bullet0
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x20181004

processor       : 3
hart            : 4
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd
mmu             : sv39
uarch           : sifive,bullet0
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x20181004

[root@localhost ~]# cat /sys/firmware/devicetree/base/model
SiFive HiFive Unmatched A00[root@localhost ~]#
[root@localhost ~]# uname -a
Linux localhost.localdomain 6.6.0-98.0.0.103.oe2403sp2.riscv64 #1 SMP PREEMPT Fri Jun 27 10:45:15 UTC 2025 riscv64 riscv64 riscv64 GNU/Linux
[root@localhost ~]# cat /etc/os-release
NAME="openEuler"
VERSION="24.03 (LTS-SP2)"
ID="openEuler"
VERSION_ID="24.03"
PRETTY_NAME="openEuler 24.03 (LTS-SP2)"
ANSI_COLOR="0;31"

[root@localhost ~]# cat /etc/openEuler-release
openEuler release 24.03 (LTS-SP2)
[root@localhost ~]# lscpu
Architecture:          riscv64
  Byte Order:          Little Endian
CPU(s):                4
  On-line CPU(s) list: 0-3
NUMA:
  NUMA node(s):        1
  NUMA node0 CPU(s):   0-3
[root@localhost ~]#
```

屏幕录像：
[![asciicast](https://asciinema.org/a/HncsUaCkyzLLomdo1rmwFT7hF.svg)](https://asciinema.org/a/HncsUaCkyzLLomdo1rmwFT7hF)

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。