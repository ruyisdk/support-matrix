---
sys: openeuler
sys_ver: 24.03-LTS-SP1
sys_var: null

status: basic
last_update: 2025-03-03
---

# openEuler RISC-V 24.03 LTS SP1 Pioneer Test Report

## Test Environment

### Operating System Information

- System Version: openEuler RISC-V 24.03 LTS SP1 (Image, Legacy boot)
- Download Link: [openEuler mirror](https://mirrors.nju.edu.cn/openeuler/openEuler-24.03-LTS-SP1/embedded_img/riscv64/SG2042/) (Or in [openEuler website](https://www.openeuler.org/en/download/#openEuler%2024.03%20LTS%20SP1) Choose: riscv64 -> embedded -> SG2042 -> Choose Mirror Site)
- Installation Guide: [Installing on Pioneer Box - openEuler Docs](https://docs.openeuler.org/en/docs/24.03_LTS_SP1/docs/Installation/RISC-V-Pioneer1.3.html)

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
unzip openEuler-24.03-LTS-SP1-riscv64-sg2042.img.zip
sudo dd if=openEuler-24.03-LTS-SP1-riscv64-sg2042.img of=/dev/sda bs=4M status=progress
sync
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

![console](./console.png)

```log
Authorized users only. All activities may be monitored and reported.
openeuler@192.168.36.39's password: 

Authorized users only. All activities may be monitored and reported.
Last login: Mon Mar  3 17:13:14 2025


Welcome to 6.6.0-72.0.0.76.oe2403sp1.riscv64

System information as of time:  Mon Mar  3 17:14:07 CST 2025

System load:    0.07
Memory used:    .6%
Swap used:      0.0%
Usage On:       14%
IP address:     192.168.36.39
Users online:   2
To run a command as administrator(user "root"),use "sudo <command>".
[openeuler@openeuler-riscv64 ~]$ uname -a
Linux openeuler-riscv64 6.6.0-72.0.0.76.oe2403sp1.riscv64 #1 SMP PREEMPT Sun Dec 29 15:11:05 UTC 2024 riscv64 riscv64 riscv64 GNU/Linux
[openeuler@openeuler-riscv64 ~]$ lscpu
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
[openeuler@openeuler-riscv64 ~]$ cat /etc/os-release 
NAME="openEuler"
VERSION="24.03 (LTS-SP1)"
ID="openEuler"
VERSION_ID="24.03"
PRETTY_NAME="openEuler 24.03 (LTS-SP1)"
ANSI_COLOR="0;31"

[openeuler@openeuler-riscv64 ~]$ 
```

Screen recording (from bootup to SSH login): 

[![asciicast](https://asciinema.org/a/Wzbli8yUqqYEF2D4A4X2M5fUu.svg)](https://asciinema.org/a/Wzbli8yUqqYEF2D4A4X2M5fUu)

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.

