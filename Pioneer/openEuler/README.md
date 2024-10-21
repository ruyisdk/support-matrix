---
sys: openeuler
sys_ver: 24.03
sys_var: null

status: good
last_update: 2024-06-21
---

# openEuler RISC-V 24.03 LTS Pioneer Test Report

## Test Environment

### Operating System Information

- System Version: openEuler RISC-V 24.03 LTS (Image, Legacy boot)
- Download Link: [openEuler website](https://www.openeuler.org/en/download/archive/detail/?version=openEuler%2024.03%20LTS) (Choose: riscv64 -> embedded -> SG2042 -> Choose Mirror Site)
- Installation Guide: [Installing on Pioneer Box - openEuler Docs](https://docs.openeuler.org/en/docs/24.03_LTS/docs/Installation/RISC-V-Pioneer1.3.html)

### Hardware Information

- Milk-V Pioneer Box v1.3
- A microSD card (or NVMe SSD + NVMe SSD to USB hard drive enclosure)
- A USB Type-C cable (used to connect the onboard serial port)

## Installation Steps

### Flashing Image to microSD card or NVMe SSD using `dd`

Download the image, then burn it to microSD card or NVMe drive using `dd`.

If you're using Windows, we recommend using tools like Rufus or Etcher.

Replace `/dev/sda` with your actual drive's name.

```shell
unzip openEuler-24.03-LTS-riscv64-sg2042.img.zip
sudo wipefs -af /dev/sda
sudo dd if=openEuler-24.03-LTS-riscv64-sg2042.img of=/dev/sda bs=1M status=progress
sudo eject /dev/sda
```

### Logging into the System

According to openEuler's docs:

> Due to the limitations of the current factory firmware, the RISC-V serial output is incomplete during device startup, and the serial output will be closed before the operating system is fully loaded. The graphics card needs to be inserted into the `PCIe` slot and connected to a monitor to observe the complete startup process.

We'll log into the system via SSH instead of serial here.

Check the device's IP on your router.

Or you can just connect a monitor, keyboard and mouse to Pioneer and login.

Default username: `openeuler` or `root`
Default password: `openEuler12#$`

## Expected Results

The system starts up properly and can be accessed via SSH.

## Actual Results

The system starts up correctly and SSH login is successful.

### Boot Log

```log
Authorized users only. All activities may be monitored and reported.


Welcome to 6.6.0-27.0.0.31.oe2403.riscv64

System information as of time:  Mon Jul  8 14:30:48 CST 2024

System load:    1.30
Memory used:    .6%
Swap used:      0.0%
Usage On:       14%
IP address:     10.0.0.12
Users online:   1
To run a command as administrator(user "root"),use "sudo <command>".
[openeuler@openeuler-riscv64 ~]$ cat /etc/os-release 
NAME="openEuler"
VERSION="24.03 (LTS)"
ID="openEuler"
VERSION_ID="24.03"
PRETTY_NAME="openEuler 24.03 (LTS)"
ANSI_COLOR="0;31"

[openeuler@openeuler-riscv64 ~]$ cat /etc/o
openEuler-latest     openEuler_security/  opensc-riscv64.conf  os-release           
openEuler-release    openldap/            opt/                 
[openeuler@openeuler-riscv64 ~]$ cat /etc/openEuler-release 
openEuler release 24.03 (LTS)
[openeuler@openeuler-riscv64 ~]$ uname -a
Linux openeuler-riscv64 6.6.0-27.0.0.31.oe2403.riscv64 #1 SMP Fri May 24 21:52:58 CST 2024 riscv64 riscv64 riscv64 GNU/Linux
[openeuler@openeuler-riscv64 ~]$ cat /proc/cpuinfo 
processor       : 0
hart            : 3
isa             : rv64imafdcv_zicntr_zicsr_zifencei_zihpm
mmu             : sv39
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

...

[openeuler@openeuler-riscv64 ~]$
```

Screen recording (from bootup to SSH login): 

[![asciicast](https://asciinema.org/a/ffNh01g1dltQqIOwGRl4Re9ri.svg)](https://asciinema.org/a/ffNh01g1dltQqIOwGRl4Re9ri)

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.

