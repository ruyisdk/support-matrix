# Debian Trixie Milk-V Mars 测试报告

## 测试环境

### 操作系统信息

- 系统版本：Debian 13 (Trixie)
- 下载链接：
    - debian-installer mini ISO: https://deb.debian.org/debian/dists/trixie/main/installer-riscv64/current/images/netboot/mini.iso
    - u-boot-starfive: http://deb.debian.org/debian/pool/main/u/u-boot/u-boot-starfive_2025.01-3_riscv64.deb
- 参考安装文档：[Debian Wiki](https://wiki.debian.org/InstallingDebianOn/StarFive/VisionFiveV2)
- Milk-V Wiki（启动设置）：https://milkv.io/docs/mars/getting-started/setup#boot-mode-switch

### 硬件信息

- Milk-V Mars（v1.2，8GB RAM，其他版本也应当可用）
- USB 电源适配器
- USB-A to C 或 C to C 线缆一条
- microSD 卡一张
- U 盘一个（至少 128MB，用于存储 Debian mini netboot ISO）
- USB to UART 调试器一个（如：CH340, CH341, CH343, FT2232 等）
- 三条杜邦线
- 有线网络连接
- 牙签一根，或者其他能拨动拨码开关的小东西 ;)

由于 MIPI DSI 和 HDMI (DC8200) 的主线化工作尚未完成，目前没有显示/图形界面支持。

目前只能从 UART 串口或者 SSH 连接开发板。

## 安装步骤

Debian 提供了多种安装方法。

对于 U-Boot 和系统本身，实际上都可以从 USB、网络或者串口启动。

U-Boot 的镜像相对较小，通过串口（X-MODEM 或 Y-MODEM）即可引导；然而 netboot ISO 相对较大，通过串口传输可能要花费两个小时，实在是难以推荐这种方式。

然而还有一个问题：厂商的 U-Boot 缺少 USB 支持，实际上也没办法通过 USB 来更新 U-Boot。

因而在 Mars 上比较可行的方式（如果你的开发板以前用的是厂商固件的话）：

一阶段（临时从 RAM 启动 Debian U-Boot）：通过 UART 加载 U-Boot SPL -> 通过 UART 加载 U-Boot 本体 -> 重启进入 Debian U-Boot

二阶段（将 Debian 镜像永久刷入 SPI Flash）：将 Debian U-Boot SPL 和 U-Boot 本体刷进 SPI -> 再次重启进入 U-Boot

三阶段（实际的系统安装流程）：通过 USB 启动 debian-installer 安装介质 -> 结束

每一阶段之间可能会需要切换启动模式/调整拨码开关，请务必仔细阅读。

在开始之前：参考 Milk-V 的文档，把拨码开关设置成 UART 恢复模式。

即：`GPIO0=GPIO1=1`。

### 一阶段：启动进 Debian U-Boot

首先，当然要下载 Debian 的 U-Boot 镜像。

如果你已经有一个可用的 Debian 系统环境，直接使用 `dpkg` 即可解压：

```
wget http://deb.debian.org/debian/pool/main/u/u-boot/u-boot-starfive_2025.01-3_riscv64.deb
dpkg -x u-boot-starfive_2025.01-3_riscv64.deb u-boot-starfive_2025.01-3_riscv64
```

如果没有 Debian 环境，也可以使用 7-Zip 或者 `binutils` 的 `ar`：

```shell
wget http://deb.debian.org/debian/pool/main/u/u-boot/u-boot-starfive_2025.01-3_riscv64.deb
# 7-Zip
7z x u-boot-starfive_2025.01-3_riscv64.deb
tar xvf data.tar
# ar
ar x u-boot-starfive_2025.01-3_riscv64.deb
tar xvf data.tar.xz
```

确认开发板拨码开关已经调整至 UART 恢复模式（全部设置为 0）。

现在可以开启一个串口中断，比如 `tio` 或 `minicom`（本次均使用 `tio`）。

（本次测试中使用的串口调试器是 CH343P，因此显示的串口设备是 `ttyACM` 而不是 `ttyUSB`，请按实际情况调整；另外，可能需要 `sudo`。）

```shell
tio /dev/ttyACM0 -o 1
```

给开发板上电，应该能看到如下输出：

```log
(C)StarFive
CC
```

按 `Ctrl+T` 然后按 `X`

```log
[15:50:16.277] Please enter which X modem protocol to use:
[15:50:16.277]  (0) XMODEM-1K send
[15:50:16.277]  (1) XMODEM-CRC send
[15:50:16.277]  (2) XMODEM-CRC receive
CCCCCCCCCC
```

按 `0`

```log
[15:50:17.644] Send file with XMODEM-1K
[15:50:17.644] Enter file name:
```

输入：`u-boot-spl.bin.normal.out`

```log
[15:50:25.199] Sending file 'u-boot-spl.bin.normal.out'
[15:50:25.199] Press any key to abort transfer
................................................................................................................................................|
[15:50:39.047] Done

U-Boot SPL 2025.01-3 (Apr 08 2025 - 23:07:41 +0000)
DDR version: dc2e84f0.
Trying to boot from UART
C
```

按 `Ctrl+T` 然后按 `Y`

```log
[15:50:43.179] Send file with YMODEM
[19:50:43.179] Enter file name: 
```

输入 `u-boot.itb`

```log
[15:50:43.179] Send file with YMODEM
[15:50:45.975] Sending file 'u-boot.itb'
[15:50:45.975] Press any key to abort transfer
..........................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................|
[15:52:21.529] Done
Loaded 1024523 bytes


U-Boot 2025.01-3 (Apr 08 2025 - 23:07:41 +0000)

CPU:   sifive,u74-mc
Model: Milk-V Mars
DRAM:  8 GiB
Core:  133 devices, 26 uclasses, devicetree: board
WDT:   Not starting watchdog@13070000
MMC:   mmc@16010000: 0, mmc@16020000: 1
Loading Environment from SPIFlash... SF: Detected gd25lq128 with page size 256 Bytes, erase size 4 KiB, total 16 MiB
*** Warning - bad CRC, using default environment

StarFive EEPROM format v2

--------EEPROM INFO--------
Vendor : MILK-V
Product full SN: MARS-V11-2340-D008E000-00000FB6
data version: 0x2
PCB revision: 0xc1
BOM revision: A
Ethernet MAC0 address: 6c:cf:39:00:94:c3
Ethernet MAC1 address: 6c:cf:39:00:94:c4
--------EEPROM INFO--------

starfive_7110_pcie pcie@2b000000: Starfive PCIe bus probed.
starfive_7110_pcie pcie@2c000000: Starfive PCIe bus probed.
In:    serial@10000000
Out:   serial@10000000
Err:   serial@10000000
Net:   eth0: ethernet@16030000
starting USB...
Bus xhci_pci: Register 5000420 NbrPorts 5
Starting the controller
USB XHCI 1.00
scanning bus xhci_pci for devices... 2 USB Device(s) found
       scanning usb for storage devices... 0 Storage Device(s) found
Working FDT set to ff72da10
Hit any key to stop autoboot:  0
```

按照提示，按下任意键打断自动启动。

现在我们已经在 Debian 的 U-Boot 内了，可以准备开始下一阶段了。

### 二阶段：将 Debian U-Boot 刷入 SPI Flash

运行 `sf probe`:

```log
StarFive # sf probe
SF: Detected gd25lq128 with page size 256 Bytes, erase size 4 KiB, total 16 MiB
StarFive # 
```

运行 `loady $loadaddr && sf update $loadaddr 0 $filesize`

```
StarFive # loady $loadaddr && sf update $loadaddr 0 $filesize
## Ready for binary (ymodem) download to 0x82000000 at 115200 bps...
C
```

按 `Ctrl+T` 然后按 `Y`

```log
[15:52:38.149] Send file with YMODEM
[15:52:38.149] Enter file name:
```

输入 `u-boot-spl.bin.normal.out`

```log
[15:52:41.925] Sending file 'u-boot-spl.bin.normal.out'
[15:52:41.925] Press any key to abort transfer
.................................................................................................................................................|
[15:52:59.538] Done
## Total Size      = 0x00023f4a = 147274 Bytes
## Start Addr      = 0x82000000
device 0 offset 0x0, size 0x23f4a
147274 bytes written, 0 bytes skipped in 0.628s, speed 238999 B/s
StarFive #
```

运行 `loady $loadaddr && sf update $loadaddr 100000 $filesize`

```log
StarFive # loady $loadaddr && sf update $loadaddr 100000 $filesize
## Ready for binary (ymodem) download to 0x82000000 at 115200 bps...
C
```

按 `Ctrl+T` 然后啊 `Y`

```log
[15:53:17.756] Send file with YMODEM
[15:53:17.756] Enter file name:
```

输入 `u-boot.itb`

```log
[15:53:20.837] Sending file 'u-boot.itb'
[15:53:20.837] Press any key to abort transfer
..........................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................|
[15:54:56.178] Done
## Total Size      = 0x000fa20b = 1024523 Bytes
## Start Addr      = 0x82000000
device 0 offset 0x100000, size 0xfa20b
925696 bytes written, 98827 bytes skipped in 6.490s, speed 161575 B/s
StarFive #
```

现在运行 `env erase` 来擦除 U-Boot 环境变量：

```log
StarFive # env erase
Erasing Environment on SPIFlash... OK
StarFive #
Erasing Environment on SPIFlash... OK
StarFive #
```

至此，Debian U-Boot 镜像已经刷入 SPI Flash。

给开发板断电，将拨码开关切换至 QSPI NOR Flash 启动模式，`GPIO0=GPIO1=0`，接下来开始 debian-installer 的系统安装阶段。

### 三阶段：从 USB 启动并进行 Debian 系统安装

首先下载 netboot mini ISO：

```shell
wget https://deb.debian.org/debian/dists/trixie/main/installer-riscv64/current/images/netboot/mini.iso
```

插入 U 盘，将 ISO 写进 U 盘。

> [!WARNING]
> U 盘上所有设备都将丢失！
> 数据无价，务必备份好再进行下一步操作。

假设 U 盘位于 `/dev/sdX`：

```shell
sudo wipefs -af /dev/sdX
sudo dd if=mini.iso of=/dev/sdX bs=1M status=progress
sync; sudo eject /dev/sdX
```

拔掉 U 盘，插入 Mars 的 USB 3.0 接口，然后上电。

> [!NOTE]
> Mars 有四个 USB 接口。
> 靠近网口的两个 USB 口有时会不识别设备。
> 如果出现这种情况，使用另一侧的两个 USB 3.0 接口，然后运行 `usb reset` 来重新扫描 USB 设备。

```log
U-Boot SPL 2025.01-3 (Apr 08 2025 - 23:07:41 +0000)
DDR version: dc2e84f0.
Trying to boot from SPI


U-Boot 2025.01-3 (Apr 08 2025 - 23:07:41 +0000)

CPU:   sifive,u74-mc
Model: Milk-V Mars
DRAM:  8 GiB
Core:  133 devices, 26 uclasses, devicetree: board
WDT:   Not starting watchdog@13070000
MMC:   mmc@16010000: 0, mmc@16020000: 1
Loading Environment from SPIFlash... SF: Detected gd25lq128 with page size 256 Bytes, erase size 4 KiB, total 16 MiB
*** Warning - bad CRC, using default environment

StarFive EEPROM format v2                                                                                                                  

--------EEPROM INFO--------
Vendor : MILK-V
Product full SN: MARS-V11-2340-D008E000-00000FB6
data version: 0x2
PCB revision: 0xc1
BOM revision: A
Ethernet MAC0 address: 6c:cf:39:00:94:c3
Ethernet MAC1 address: 6c:cf:39:00:94:c4
--------EEPROM INFO--------

starfive_7110_pcie pcie@2b000000: Starfive PCIe bus probed.
starfive_7110_pcie pcie@2c000000: Starfive PCIe bus probed.
In:    serial@10000000
Out:   serial@10000000
Err:   serial@10000000
Net:   eth0: ethernet@16030000
starting USB...
Bus xhci_pci: Register 5000420 NbrPorts 5
Starting the controller
USB XHCI 1.00
scanning bus xhci_pci for devices... 3 USB Device(s) found
       scanning usb for storage devices... 1 Storage Device(s) found
Working FDT set to ff72da10
Hit any key to stop autoboot:  0
Card did not respond to voltage select! : -110
Failed to load EFI variables
** Booting bootflow '<NULL>' with efi_mgr
Booting: usb 0
```

开发板应当能启动进入 GRUB 然后开始 debian-installer 流程。

如果没有，中断自动启动，手动运行：

```shell
usb start
run bootcmd_usb0
```

接下来就是普通的 Debian 安装流程了。

可以进行任意更改，但有几点需要注意的：

- 由于 Mars 和 VisionFive 2 不一样，没有 M.2 NVMe 接口，建议禁用 `swap`。
- 提示是否要在可移动设备安装 EFI 的时候，选择 是/Yes。
    - 这样做的话，GRUB 会在 `EFI/BOOT/BOOTRISCV64.EFI` 额外放置一份 GRUB，这样 U-Boot 会自动扫描到并从此处启动。

安装完成后，如果想要读取/编辑 U-Boot 环境变量，可以考虑安装 `u-boot-tools` 并向 `/etc/fw_env.config` 中写入如下配置：

```
# Edit /etc/fw_env.config and set to content as below:

# NOR example
# MTD device name       Device offset   Env. size       Flash sector size       Number of sectors
/dev/mtd1               0x0000          0x10000         0x1000
```

### 登录系统

通过串口登录系统。

用户名/密码为安装途中设置，没有默认值。

## 预期结果

系统正常启动，能够通过串口登录。

## 实际结果

系统正常启动，成功通过串口查看输出。

### 启动信息

完整的安装流程和启动日志可见下方的 asciicast 录像。

[![asciicast](https://asciinema.org/a/faBiHx1pVS6YuStFiAn4oOuPW.svg)](https://asciinema.org/a/faBiHx1pVS6YuStFiAn4oOuPW)

启动日志：

```log
Loading Linux 6.12.43+deb13-riscv64 ...
Loading initial ramdisk ...
/dev/mmcblk1p2: clean, 29899/7766016 files, 872792/31043072 blocks

Debian GNU/Linux 13 mars ttyS0

mars login: mx
Password:
Linux mars 6.12.43+deb13-riscv64 #1 SMP Debian 6.12.43-1 (2025-08-27) riscv64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
mx@mars:~$ uname -a
Linux mars 6.12.43+deb13-riscv64 #1 SMP Debian 6.12.43-1 (2025-08-27) riscv64 GNU/Linux
mx@mars:~$ cat /etc/os-release
PRETTY_NAME="Debian GNU/Linux 13 (trixie)"
NAME="Debian GNU/Linux"
VERSION_ID="13"
VERSION="13 (trixie)"
VERSION_CODENAME=trixie
DEBIAN_VERSION_FULL=13.1
ID=debian
HOME_URL="https://www.debian.org/"
SUPPORT_URL="https://www.debian.org/support"
BUG_REPORT_URL="https://bugs.debian.org/"
mx@mars:~$ cat /etc/debian_version
13.1
mx@mars:~$ cat /proc/cpuinfo
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

mx@mars:~$ lscpu
Architecture:                riscv64
  Byte Order:                Little Endian
CPU(s):                      4
  On-line CPU(s) list:       0-3
Vendor ID:                   0x489
  Model name:                sifive,u74-mc
    CPU family:              0x8000000000000007
    Model:                   0x4210427
    Thread(s) per core:      1
    Core(s) per socket:      4
    Socket(s):               1
    CPU(s) scaling MHz:      100%
    CPU max MHz:             1500.0000
    CPU min MHz:             375.0000
Caches (sum of all):
  L1d:                       128 KiB (4 instances)
  L1i:                       128 KiB (4 instances)
  L2:                        2 MiB (1 instance)
NUMA:
  NUMA node(s):              1
  NUMA node0 CPU(s):         0-3
Vulnerabilities:
  Gather data sampling:      Not affected
  Indirect target selection: Not affected
  Itlb multihit:             Not affected
  L1tf:                      Not affected
  Mds:                       Not affected
  Meltdown:                  Not affected
  Mmio stale data:           Not affected
  Reg file data sampling:    Not affected
  Retbleed:                  Not affected
  Spec rstack overflow:      Not affected
  Spec store bypass:         Not affected
  Spectre v1:                Not affected
  Spectre v2:                Not affected
  Srbds:                     Not affected
  Tsa:                       Not affected
  Tsx async abort:           Not affected
  mx@mars:~$ sudo apt update; sudo apt install -y fastfetch
[sudo] password for mx:
Hit:1 http://mirror.nju.edu.cn/debian trixie InRelease
Hit:2 http://mirror.nju.edu.cn/debian trixie-updates InRelease
Hit:3 http://security.debian.org/debian-security trixie-security InRelease
All packages are up to date.
Installing:
  fastfetch

Installing dependencies:
  libyyjson0

Summary:
  Upgrading: 0, Installing: 2, Removing: 0, Not Upgrading: 0
  Download size: 669 kB
  Space needed: 1,879 kB / 117 GB available

Get:1 http://mirror.nju.edu.cn/debian trixie/main riscv64 libyyjson0 riscv64 0.10.0+ds-1+b1 [117 kB]
Get:2 http://mirror.nju.edu.cn/debian trixie/main riscv64 fastfetch riscv64 2.40.4+dfsg-1 [552 kB]
Fetched 669 kB in 0s (2,567 kB/s)
Selecting previously unselected package libyyjson0:riscv64.
(Reading database ... 26400 files and directories currently installed.)
Preparing to unpack .../libyyjson0_0.10.0+ds-1+b1_riscv64.deb ...
Unpacking libyyjson0:riscv64 (0.10.0+ds-1+b1) ...
Selecting previously unselected package fastfetch.
Preparing to unpack .../fastfetch_2.40.4+dfsg-1_riscv64.deb ...
Unpacking fastfetch (2.40.4+dfsg-1) ...
Setting up libyyjson0:riscv64 (0.10.0+ds-1+b1) ...
Setting up fastfetch (2.40.4+dfsg-1) ...
Processing triggers for man-db (2.13.1-1) ...
Processing triggers for libc-bin (2.41-12) ...
mx@mars:~$ fastfetch
        _,met$$$$$gg.          mx@mars
     ,g$$$$$$$$$$$$$$$P.       -------
   ,g$$P""       """Y$$.".     OS: Debian GNU/Linux 13 (trixie) riscv64
  ,$$P'              `$$$.     Host: Milk-V Mars
',$$P       ,ggs.     `$$b:    Kernel: Linux 6.12.43+deb13-riscv64
`d$$'     ,$P"'   .    $$$     Uptime: 1 min
 $$P      d$'     ,    $$P     Packages: 302 (dpkg)
 $$:      $$.   -    ,d$$'     Shell: bash 5.2.37
 $$;      Y$b._   _,d$P'       Terminal: vt220
 Y$$.    `.`"Y$$$$P"'          CPU: jh7110 (4) @ 1.50 GHz
 `$$b      "-.__               Memory: 308.27 MiB / 7.74 GiB (4%)
  `Y$$b                        Swap: Disabled
   `Y$$.                       Disk (/): 952.57 MiB / 116.00 GiB (1%) - ext4
     `$$b.                     Local IP (end0): 10.0.0.32/24
       `Y$$b.                  Locale: en_US.UTF-8
         `"Y$b._
             `""""

mx@mars:~$
```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功
