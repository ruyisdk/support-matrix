---
sys: opencloudos
sys_ver: "23"
sys_var: null

status: basic
last_update: 2025-04-17
---

# openCloudOS-Stream 23 Pioneer Test Report

## Test Environment

### Operating System Information

- System Version: openCloudOS-Stream 23
- Download Link: [http://43.139.5.209/sdcard-img/](http://43.139.5.209/sdcard-img/)
- Reference Installation Document: [readme.md](http://43.139.5.209/sdcard-img/readme.md)

### Hardware Information

- Milk-V Pioneer Box v1.3
- A microSD card
- A USB Type-C cable (used to connect the onboard serial port)

## Installation Steps

### Flashing Image

Decompress the image using `xz`.
Write the image to the microSD card using `dd`.

```bash
xz -d ocs_developer_sdcard-0.2.img.xz
dd if=ocs_developer_sdcard-0.2.img of=/dev/yout-device bs=4M status=progress
```

### Logging into the System

Logging into the system via the serial port.

Default username: `root`
Default password: `riscv666!`

## Expected Results

The system boots up normally and allows login through the serial port.

## Actual Results

The system boots up normally and login through the serial port is successful.

### Boot Log

```log
[root@riscv64 ~]# uname -a
Linux riscv64.developer.ocs23 6.6.68 #1 SMP Thu Apr 10 17:26:47 CST 2025 riscv64 riscv64 riscv64 GNU/Linux
[root@riscv64 ~]# lscpu
Architecture:          riscv64
  Byte Order:          Little Endian
CPU(s):                64
  On-line CPU(s) list: 0-63
NUMA:                  
  NUMA node(s):        4
  NUMA node0 CPU(s):   0-7,16-23
  NUMA node1 CPU(s):   8-15,24-31
  NUMA node2 CPU(s):   32-39,48-55
  NUMA node3 CPU(s):   40-47,56-63
[root@riscv64 ~]# fastfetch 
        #####            root@riscv64
       #######           ------------
       ##O#O##           OS: OpenCloudOS Stream 23 riscv64
       #######           Host: Sophgo Mango
     ###########         Kernel: Linux 6.6.68
    #############        Uptime: 2 mins
   ###############       Packages: 1366 (rpm)
   ################      Shell: bash 5.2.15
  #################      Display (DELL U2719DS): 2048x1080 @ 60 Hz in 27" [External]
#####################    Cursor: Adwaita
#####################    Terminal: vt220
  #################      CPU: mango (64)
                         GPU: AMD Radeon HD 6450/7450/8450 / R5 230 OEM [Discrete]
                         Memory: 1.49 GiB / 124.91 GiB (1%)
                         Swap: Disabled
                         Disk (/): 4.72 GiB / 11.16 GiB (42%) - ext4
                         Local IP (enP2p197s0): 192.168.36.39/22
                         Locale: en_US.UTF-8

                                                 
                                                 
[root@riscv64 ~]# cat /etc/os-release 
NAME="OpenCloudOS Stream"
VERSION="23"
RELEASE="2410"
ID="opencloudos"
ID_LIKE="opencloudos"
VERSION_ID="23"
PLATFORM_ID="platform:ocs23"
PRETTY_NAME="OpenCloudOS Stream 23"
ANSI_COLOR="0;31"
CPE_NAME="cpe:/o:opencloudos:opencloudos:23"
HOME_URL="https://www.opencloudos.org/"
BUG_REPORT_URL="https://bugs.opencloudos.tech/"
[root@riscv64 ~]# 
```

Serial logs (from flashing the system to booting up):

[![asciicast](https://asciinema.org/a/xGlmsQEUP3IgJDbllh85yLaKA.svg)](https://asciinema.org/a/xGlmsQEUP3IgJDbllh85yLaKA)

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
