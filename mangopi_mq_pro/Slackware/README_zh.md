# Slackware MangoPi MQ Pro 测试报告

## 测试环境

### 操作系统信息

- 下载链接：http://dl.slarm64.org/slackware/images/mangopi_mq_pro/slarm64-current-riscv64-xfce-mangopi_mq_pro-6.1.53-build-20230919.img.zst
- 参考安装文档：http://dl.slarm64.org/slackware/images/mangopi_mq_pro/

> Note: 此镜像为社区项目 (slarm64) 提供，非官方镜像。

### 硬件信息

- MangoPi MQ Pro
- 电源适配器
- microSD 卡一张
- USB to UART 调试器一个

## 安装步骤

### 刷写镜像

使用 `zstd` 解压镜像。
使用 `dd` 将镜像写入 microSD 卡。

```bash
zstd -d slarm64-current-riscv64-xfce-mangopi_mq_pro-6.1.53-build-20230919.img.zst
sudo dd if=slarm64-current-riscv64-xfce-mangopi_mq_pro-6.1.53-build-20230919.img of=/dev/your_device bs=1M status=progress
```

### 登录系统

注意 Type-C 电源线应插入板子的 OTG 接口而不是 Host 接口，以避免出现供电不稳；参见 https://forums.100ask.net/t/topic/876/6。

通过串口登录系统。

默认用户名：`root`
默认密码：无 （登录后设置密码和新用户）

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

系统正常启动，能够通过板载串口登录。

### 启动信息

```log
U-Boot 2022.01-sun20iw1p1 (Jun 10 2023 - 20:13:15 +0300)

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
25570816 bytes read in 2913 ms (8.4 MiB/s)
Failed to load '/boot/dtb/allwinner/overlay/-fixup.scr'
7031144 bytes read in 1211 ms (5.5 MiB/s)
## Loading init Ramdisk from Legacy Image at 4ff00000 ...
   Image Name:   uInitrd
   Image Type:   RISC-V Linux RAMDisk Image (gzip compressed)
   Data Size:    7031080 Bytes = 6.7 MiB
   Load Address: 00000000
   Entry Point:  00000000
   Verifying Checksum ... OK
## Flattened Device Tree blob at 4fa00000
   Booting using the fdt blob at 0x4fa00000
   Loading Ramdisk to 4994b000, end 49fff928 ... OK
   Loading Device Tree to 00000000498dd000, end 000000004994afff ... OK

Starting kernel ...

�[    0.839283] sun20i-codec 2030000.audio-codec: ASoC: Property 'routing' does not exist or its length is not even
[    0.839356] sun20i-codec 2030000.audio-codec: error -EINVAL: Failed to initialize card
[    1.456162] sun20i-codec 2030000.audio-codec: ASoC: Property 'routing' does not exist or its length is not even
[    1.456207] sun20i-codec 2030000.audio-codec: error -EINVAL: Failed to initialize card


=======================================================================

if you want to transfer the system to SDcard to internal memory (eMMC or NAND),
follow transfer-to-disk

=======================================================================

slarm64 GNU/Linux (ttyS0)
Kernel 6.1.53 (riscv64)

mangopi-mq-pro login: root
You are required to change your password immediately (administrator enforced).
New password: 
BAD PASSWORD: The password fails the dictionary check - it does not contain enough DIFFERENT characters
New password: 
Retype new password: 
      _                   ___  ___ 
 ___ | | ___  ___  _____ |  _|| | |
|_ -|| || .'||  _||     || . ||_  |
|___||_||__,||_|  |_|_|_||___|  |_|
                                 _                                
 _____  ___  ___  ___  ___  ___ |_|   _____  ___    ___  ___  ___ 
|     || .'||   || . || . || . || |  |     || . |  | . ||  _|| . |
|_|_|_||__,||_|_||_  ||___||  _||_|  |_|_|_||_  |  |  _||_|  |___|
                 |___|     |_|                |_|  |_|            


Support: slarm64.org

Creating new account. Please provide a username (eg. your forename): origami

Login name for new user: origami

User ID ('UID') [ defaults to next available ]: 

Initial group [ users ]: 
Additional UNIX groups:

Users can belong to additional UNIX groups on the system.
For local users using graphical desktop login managers such
as XDM/KDM, users may need to be members of additional groups
to access the full functionality of removable media devices.

* Security implications *
Please be aware that by adding users to additional groups may
potentially give access to the removable media of other users.

If you are creating a new user for remote shell access only,
users do not need to belong to any additional groups as standard,
so you may press ENTER at the next prompt.

Press ENTER to continue without adding any additional groups
Or press the UP arrow key to add/select/edit additional groups
:  

Home directory [ /home/origami ] 

Shell [ /bin/bash ] 

Expiry date (YYYY-MM-DD) []: 

New account will be created as follows:

---------------------------------------
Login name.......:  origami
UID..............:  [ Next available ]
Initial group....:  users
Additional groups:  [ None ]
Home directory...:  /home/origami
Shell............:  /bin/bash
Expiry date......:  [ Never ]

This is it... if you want to bail out, hit Control-C.  Otherwise, press
ENTER to go ahead and make the account.


Creating new account...


Changing finger information for origami.
Name []: 
Office []: 
Office Phone []: 
Home Phone []: 


Finger information not changed.
New password: 
Retype new password: 
passwd: password updated successfully


Account setup complete.

Dear , your account origami has been created.
Please use this account for your daily work from now on.

root@mangopi-mq-pro:~# uname -a
Linux mangopi-mq-pro 6.1.53 #1 Mon Sep 18 00:20:14 EEST 2023 riscv64 GNU/Linux
root@mangopi-mq-pro:~# cat /etc/os-release 
NAME=Slackware
VERSION="15.0"
ID=slackware
VERSION_ID=15.0
PRETTY_NAME="Slackware 15.0 riscv64 (post 15.0 -current)"
ANSI_COLOR="0;34"
CPE_NAME="cpe:/o:slackware:slackware_linux:15.0"
HOME_URL="http://slackware.com/"
SUPPORT_URL="http://www.linuxquestions.org/questions/slackware-14/"
BUG_REPORT_URL="http://www.linuxquestions.org/questions/slackware-14/"
VERSION_CODENAME=current
root@mangopi-mq-pro:~# lscpu
Architecture:          riscv64
  Byte Order:          Little Endian
CPU(s):                1
  On-line CPU(s) list: 0
root@mangopi-mq-pro:~# 
```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。