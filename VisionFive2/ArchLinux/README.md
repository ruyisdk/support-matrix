---
sys: archlinux
sys_ver: null
sys_var: null

status: basic
last_update: 2024-10-25
---

# Arch Linux VisionFive 2 Version Test Report

## Test Environment

### Operating System Information

- System Version: ArchLinux-VF2_6.6_v5.13.1-cwt23
- Download Link: https://github.com/cwt-vf2/archlinux-image-vf2/releases/tag/cwt23
- Reference Installation Document: https://forum.rvspace.org/t/arch-linux-image-for-visionfive-2/1459

> This image is provided by community developers and is not an official image. Arch Linux RISC-V currently only offers `rootfs`.

### Hardware Information

- StarFive VisionFive 2
- A USB Power Adapter
- A USB-A to C or C to C Cable
- A microSD Card
- A USB to UART Debugger (e.g., CH340, CH341, FT2232, etc.)
- Three Dupont Wires

## Installation Steps

### Decompress and Flash Image to microSD Card

Assume `/dev/sdc` is the storage card.

```bash
zstd -d ArchLinux-VF2_6.6_v5.13.1-cwt23.img.zst
sudo dd if=ArchLinux-VF2_6.6_v5.13.1-cwt23.img of=/dev/sdc bs=4M status=progress
```

### Boot Mode Selection

StarFive VisionFive 2 offers various boot modes, which can be configured via onboard dip switches before powering on; there are also silk screen labels on the development board itself.

To boot the Arch image, you can select the 1-bit QSPI Nor Flash mode (i.e., `RGPIO_0 = 0`, `RGPIO_1 = 0`). Note that this mode may require a prior firmware update in the Flash. If your boot is unsuccessful, please refer to the official documentation for firmware upgrading: [Update SPL and U-Boot](https://doc.rvspace.org/VisionFive2/Quick_Start_Guide/VisionFive2_QSG/spl_u_boot_0.html)

### Logging into the System

Logging into the system via the serial port.

Username: `root`
Default Password: `archriscv`

or

Username: `user`
Password: `user`

## Expected Results

The system boots normally and allows login via the serial port.

## Actual Results

The system booted normally and login via the serial port was successful.

### Boot Log

```log
Arch Linux 6.6.32-cwt-5.13.1-1 (ttyS0)

ArchVF2 login: root
Password: 
[root@ArchVF2 ~]# uname -a
Linux ArchVF2 6.6.32-cwt-5.13.1-1 #1 SMP PREEMPT_DYNAMIC Mon Sep 30 16:40:34 +07 2024 riscv64 GNU/Linux
[root@ArchVF2 ~]# cat /etc/os-release 
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
[root@ArchVF2 ~]# cat /proc/cpuinfo 
processor	: 0
hart		: 2
isa		: rv64imafdc_zicntr_zicsr_zifencei_zihpm_zba_zbb
mmu		: sv39
uarch		: sifive,u74-mc
mvendorid	: 0x489
marchid		: 0x8000000000000007
mimpid		: 0x4210427

processor	: 1
hart		: 1
isa		: rv64imafdc_zicntr_zicsr_zifencei_zihpm_zba_zbb
mmu		: sv39
uarch		: sifive,u74-mc
mvendorid	: 0x489
marchid		: 0x8000000000000007
mimpid		: 0x4210427

processor	: 2
hart		: 3
isa		: rv64imafdc_zicntr_zicsr_zifencei_zihpm_zba_zbb
mmu		: sv39
uarch		: sifive,u74-mc
mvendorid	: 0x489
marchid		: 0x8000000000000007
mimpid		: 0x4210427

processor	: 3
hart		: 4
isa		: rv64imafdc_zicntr_zicsr_zifencei_zihpm_zba_zbb
mmu		: sv39
uarch		: sifive,u74-mc
mvendorid	: 0x489
marchid		: 0x8000000000000007
mimpid		: 0x4210427

[root@ArchVF2 ~]# 
```

Screen recording (from flashing the image to logging into the system):
[![asciicast](https://asciinema.org/a/373WIY16lHwlqjbsj7SkIdWnU.svg)](https://asciinema.org/a/373WIY16lHwlqjbsj7SkIdWnU)

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
