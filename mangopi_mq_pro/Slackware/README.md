---
sys: slackware
sys_ver: 15
sys_var: null

status: basic
last_update: 2025-03-04
---

# Slackware MangoPi MQ Pro Test Report

## Test Environment

### Operating System Information

- Download Link: http://dl.slarm64.org/slackware/images/mangopi_mq_pro/slarm64-current-riscv64-xfce-mangopi_mq_pro-6.1.53-build-20230919.img.zst
- Reference Installation Document: http://dl.slarm64.org/slackware/images/mangopi_mq_pro/

> Note: This image is provided by community developers (at slarm64) and is not an official image.

### Hardware Information

- MangoPi MQ Pro
- Power Adapter
- A microSD card
- A USB to UART Debugger

## Installation Steps

### Flashing Image

Use `zstd` to decompress the image.
Use `dd` to flash the image to the microSD card.

```bash
zstd -d slarm64-current-riscv64-xfce-mangopi_mq_pro-6.1.53-build-20230919.img.zst
sudo dd if=slarm64-current-riscv64-xfce-mangopi_mq_pro-6.1.53-build-20230919.img of=/dev/your_device bs=1M status=progress
```

### Logging into the System

Plug in the power via the USB-C "OTG" port (instead of "HOST") to avoid issues with faulty power supply (see https://forums.100ask.net/t/topic/876/6).

Logging into the system via the serial port.

Default username: `root`
Default password: none (immediate setup of password and a new user required after login)

## Expected Results

The system should boot normally and allow login via the onboard serial port.

## Actual Results

The system booted normally and login via the onboard serial port is also successful.

### Boot Log

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

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.