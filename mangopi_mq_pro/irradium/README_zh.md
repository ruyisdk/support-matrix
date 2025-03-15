# irradium MangoPi MQ-Pro 版本测试报告

## 测试环境

### 操作系统信息

- 系统版本：irradium 3.7
- 下载链接：https://dl.irradium.org/irradium/images/mangopi_mq_pro/
- 参考安装文档：https://dl.irradium.org/irradium/images/mangopi_mq_pro/README.TXT

### 硬件信息

- MangoPi MQ-Pro
- USB 电源适配器一个
- USB-A to C 或 C to C 线缆一条
- microSD 卡一张
- USB to UART 调试器一个（如：CH340, CH341, FT2232 等）
- 杜邦线三根

## 安装步骤

### 解压并刷写镜像到 microSD 卡

```bash
zstd -d irradium-3.7-riscv64-xfce-mangopi_mq_pro-6.1.120-build-20241216.img.zst
sudo dd if=irradium-3.7-riscv64-xfce-mangopi_mq_pro-6.1.120-build-20241216.img of=/dev/<your-device> bs=1M status=progress
```

### 登录系统

通过串口登录系统。

用户名：`root`
无密码。

## 预期结果

系统正常启动，能够通过串口登录。

## 实际结果

系统正常启动，成功通过串口登录。

### 启动信息

```log
U-Boot 2022.01-sun20iw1p1 (Sep 24 2024 - 22:38:13 +0300)

DRAM:  512 MiB
Core:  39 devices, 17 uclasses, devicetree: separate
WDT:   Started watchdog@6011000 with servicing (16s timeout)
MMC:   mmc@4020000: 0, mmc@4021000: 1
Loading Environment from nowhere... OK
In:    serial@2500000
Out:   serial@2500000
Err:   serial@2500000
Net:   No ethernet found.
Hit any key to stop autoboot:  0 
switch to partitions #0, OK
mmc0 is current device
Scanning mmc 0:1...
Found U-Boot script /boot/boot.scr
2667 bytes read in 3 ms (868.2 KiB/s)
## Executing script at 4fc00000
Boot script loaded from mmc 0
127 bytes read in 2 ms (61.5 KiB/s)
22658 bytes read in 8 ms (2.7 MiB/s)
25580544 bytes read in 2911 ms (8.4 MiB/s)
Failed to load '/boot/dtb/allwinner/overlay/-fixup.scr'
4338626 bytes read in 749 ms (5.5 MiB/s)
## Loading init Ramdisk from Legacy Image at 4ff00000 ...
   Image Name:   uInitrd
   Image Type:   RISC-V Linux RAMDisk Image (gzip compressed)
   Data Size:    4338562 Bytes = 4.1 MiB
   Load Address: 00000000
   Entry Point:  00000000
   Verifying Checksum ... OK
## Flattened Device Tree blob at 4fa00000
   Booting using the fdt blob at 0x4fa00000
   Loading Ramdisk to 49bdc000, end 49fff382 ... OK
   Loading Device Tree to 0000000049b6e000, end 0000000049bdbfff ... OK

Starting kernel ...

�[    0.003755] BUG: sleeping function called from invalid context at include/linux/sched/mm.h:274
[    0.003799] in_atomic(): 1, irqs_disabled(): 1, non_block: 0, pid: 1, name: swapper
[    0.003825] preempt_count: 1, expected: 0
[    0.822606] sun20i-codec 2030000.audio-codec: ASoC: Property 'routing' does not exist or its length is not even
[    0.822656] sun20i-codec 2030000.audio-codec: error -EINVAL: Failed to initialize card
[    1.104328] sun20i-codec 2030000.audio-codec: ASoC: Property 'routing' does not exist or its length is not even
[    1.104375] sun20i-codec 2030000.audio-codec: error -EINVAL: Failed to initialize card
[    9.555256] udevd[151]: specified group 'netdev' unknown


irradium  (mangopi-mq-pro) (ttyS0)

mangopi-mq-pro login: root
You are required to change your password immediately (administrator enforced).
New password: 
Retype new password: 
 _                   _  _             
|_| ___  ___  ___  _| ||_| _ _  _____ 
| ||  _||  _|| .'|| . || || | ||     |
|_||_|  |_|  |__,||___||_||___||_|_|_|
                                 _                                
 _____  ___  ___  ___  ___  ___ |_|   _____  ___    ___  ___  ___ 
|     || .'||   || . || . || . || |  |     || . |  | . ||  _|| . |
|_|_|_||__,||_|_||_  ||___||  _||_|  |_|_|_||_  |  |  _||_|  |___|
                 |___|     |_|                |_|  |_|            

# uname -a
Linux mangopi-mq-pro 6.1.120 #1 Sun Dec 15 23:35:12 EET 2024 riscv64 GNU/Linux
# cat /etc/os-release 
NAME=irradium
VERSION="3.7"
ID=irradium
PRETTY_NAME="irradium"
HOME_URL="https://irradium.org/"
BUG_REPORT_URL="https://irradium.org/bugs/"
# lscpu
Architecture:           riscv64
  Byte Order:           Little Endian
CPU(s):                 1
  On-line CPU(s) list:  0
Vendor ID:              0x5b7
  Model name:           thead,c906
    CPU family:         0x0
    Model:              0x0
    Thread(s) per core: 1
    Core(s) per socket: 1
    Socket(s):          1
Caches (sum of all):    
  L1d:                  32 KiB (1 instance)
  L1i:                  32 KiB (1 instance)
# cat /proc/cpuinfo
processor       : 0
hart            : 0
isa             : rv64imafdc
mmu             : sv39
uarch           : thead,c906
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

# 

```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。
