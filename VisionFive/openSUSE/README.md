# openSUSE Tumbleweed VisionFive Test Report

## Test Environment

### System Information

- System Version: openSUSE Tumbleweed
- Download Link: [https://download.opensuse.org/repositories/devel:/RISCV:/Factory:/Contrib:/StarFive/images/](https://download.opensuse.org/repositories/devel:/RISCV:/Factory:/Contrib:/StarFive/images/)
- Reference Installation Document: [https://en.opensuse.org/HCL:VisionFive](https://en.opensuse.org/HCL:VisionFive)

### Hardware Information

- StarFive VisionFive
- Power Adapter
- A microSD Card
- A USB to UART Debugger

## Installation Steps

### Flashing the Image

Use `unxz` to decompress the image.
Use `dd` to write the image to the microSD card.

```bash
unxz /path/to/openSUSE.raw.xz
sudo dd if=/path/to/openSUSE.raw of=/dev/your-device bs=1M status=progress
```

### Patching the Image

After mounting the SD card:

Create `/boot/uEnv.txt` and add the following content:

```
fdt_high=0xffffffffffffffff
initrd_high=0xffffffffffffffff

scriptaddr=0x88100000
script_offset_f=0x1fff000
script_size_f=0x1000

kernel_addr_r=0x84000000
kernel_comp_addr_r=0x90000000
kernel_comp_size=0x10000000

fdt_addr_r=0x88000000
ramdisk_addr_r=0x88300000

fdtfile=starfive/jh7100-starfive-visionfive-v1.dtb

bootcmd=load mmc 0:1 0xa0000000 /EFI/BOOT/bootriscv64.efi; bootefi 0xa0000000
bootcmd_mmc0=devnum=0; run mmc_boot
```

Add the following content to each entry in `/boot/grub2/grub.cfg` (after `linux`):

```
devicetree /boot/dtb/starfive/jh7100-starfive-visionfive-v1.dtb
```

### Logging into the System

Log into the system via the serial port.

Default Username: `root`
Default Password: `linux`

## Expected Results

The system should boot normally and allow login via the onboard serial port.

## Actual Results

The system booted successfully and login via the onboard serial port was also successful.

### Boot Log

Screen recording (From flashing the image to logging in):

[![asciicast](https://asciinema.org/a/bTRGI0BeLsyA2Fg9xMZtXeVHU.svg)](https://asciinema.org/a/bTRGI0BeLsyA2Fg9xMZtXeVHU)

```log
Welcome to openSUSE Tumbleweed 20240321 - Kernel 6.8.1-130-default (ttyS0).

eth0:  
wlan0:  


localhost login: root
Password: 
Have a lot of fun...
localhost:~ # uname -a
Linux localhost.localdomain 6.8.1-130-default #1 SMP PREEMPT_DYNAMIC Mon Mar 18 09:49:44 UTC 2024 (74a8025) riscv64 riscv64 risx
localhost:~ # cat /etc/os-release 
NAME="openSUSE Tumbleweed"
# VERSION="20240321"
ID="opensuse-tumbleweed"
ID_LIKE="opensuse suse"
VERSION_ID="20240321"
PRETTY_NAME="openSUSE Tumbleweed"
ANSI_COLOR="0;32"
# CPE 2.3 format, boo#1217921
CPE_NAME="cpe:2.3:o:opensuse:tumbleweed:20240321:*:*:*:*:*:*:*"
#CPE 2.2 format
#CPE_NAME="cpe:/o:opensuse:tumbleweed:20240321"
BUG_REPORT_URL="https://bugzilla.opensuse.org"
SUPPORT_URL="https://bugs.opensuse.org"
HOME_URL="https://www.opensuse.org"
DOCUMENTATION_URL="https://en.opensuse.org/Portal:Tumbleweed"
LOGO="distributor-logo-Tumbleweed"

```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
