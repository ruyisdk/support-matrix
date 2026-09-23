---
sys: ubuntu
sys_ver: "24.04.4"
sys_var: server
status: basic
last_update: 2026-08-27
---

# Ubuntu 24.04.4 LTS Test Report for VisionFive 2 Lite

## Test Environment

### Operating System Information

- System Version: Ubuntu 24.04.4 LTS Server
- System Image: `ubuntu-24.04.4-preinstalled-server-riscv64+jh7110.img.xz`
- Download link: https://cdimage.ubuntu.com/releases/24.04.3/release/
- Reference installation document: https://canonical-ubuntu-boards.readthedocs-hosted.com/en/latest/how-to/starfive-visionfive-2/
> Note: The image above is provided by StarFive for VisionFive 2 Lite. During testing, the system reported Ubuntu 24.04.4 LTS with Linux 6.12.5-starfive. No manual kernel replacement was performed during the test.

### Hardware Information

- StarFive VisionFive 2 Lite
- Type-C power adapter
- Type-C data cable
- USB-to-TTL serial adapter
- Three Dupont wires

## Installation Steps

### Extract the System Image

Download the system image:

```
ubuntu-24.04.4-preinstalled-server-riscv64+jh7110.img.xz
```

Extract the corresponding `.img` image file for subsequent flashing to eMMC.

### Connect the Serial Port and Enter Fastboot

Download and extract SFFB Tool:

```
https://files.waveshare.net/wiki/VisionFive2/SFFB_Tool_V1.0.7z
```

Prepare the Tera Term serial terminal.

Use a USB-to-TTL serial adapter to connect to the corresponding serial pins on the VisionFive 2 Lite 40-pin header.

Board side:

```
GND    TX    RX
```

Connect them to the serial adapter as follows:

```
GND    RX    TX
```

Connect the serial adapter to a USB port on the computer, open Tera Term, and set the baud rate to:

```
115200
```

Power on the board and simultaneously press any key in the serial terminal to interrupt autoboot and enter the U-Boot command line.

Run:

```
fastboot usb 0
```

The board will enter Fastboot mode.

### Install the Driver and Flash the Image

Open Windows Device Manager and confirm that the following device appears:

```
USB Download Gadget
```

Select:

```
Update driver
→ Browse my computer for drivers
```

Select the following driver directory:

```
SFFB_Tool_V1.0\usb_driver
```

Complete the driver installation.

Open SFFB Tool, select the extracted system image, and then click:

```
Start All
```

or:

```
Action → Run
```

to start flashing the image.

After the image transfer completes, power off the board.

### First Boot

Power on the VisionFive 2 Lite again and monitor the boot process through the serial terminal until the Ubuntu login prompt appears.

### Log In to the System

Log in through the serial terminal.

Default username:

```
user
```

Default password:

```
starfive
```

## Expected Result

The system boots normally and can be accessed through the serial terminal.

## Actual Result

The system booted normally and was successfully accessed through the serial terminal.

### Boot Information

```
Ubuntu 24.04.4 LTS starfive ttyS0

starfive login: user
Password:
Welcome to Ubuntu 24.04.4 LTS (GNU/Linux 6.12.5-starfive riscv64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/pro

System information as of Wed Jul 15 14:34:55 UTC 2026

  System load:            2.37
  Usage of /:             49.1% of 51.40GB
  Memory usage:           8%
  Swap usage:             0%
  Temperature:            48.0 C
  Processes:              213
  Users logged in:        0
  IPv4 address for wlan0: 192.0.2.1
  IPv6 address for wlan0: 2001:db8::1
  IPv6 address for wlan0: 2001:db8::2

Expanded Security Maintenance for Applications is not enabled.

48 updates can be applied immediately.
To see these additional updates run: apt list --upgradable

41 additional security updates can be applied with ESM Apps.
Learn more about enabling ESM Apps service at https://ubuntu.com/esm

17 updates could not be installed automatically. For more details,
see /var/log/unattended-upgrades/unattended-upgrades.log

user@starfive:~$ uname -a
Linux starfive 6.12.5-starfive #70SF SMP Sun Sep 28 11:33:07 UTC 2025 riscv64 riscv64 riscv64 GNU/Linux

user@starfive:~$ lscpu
Architecture:             riscv64
Byte Order:               Little Endian
CPU(s):                   4
On-line CPU(s) list:      0-3
Vulnerabilities:
  Gather data sampling:   Not affected
  Itlb multihit:          Not affected
  L1tf:                   Not affected
  Mds:                    Not affected
  Meltdown:               Not affected
  Mmio stale data:        Not affected
  Reg file data sampling: Not affected
  Retbleed:               Not affected
  Spec rstack overflow:   Not affected
  Spec store bypass:      Not affected
  Spectre v1:             Not affected
  Spectre v2:             Not affected
  Srbds:                  Not affected
  Tsx async abort:        Not affected

user@starfive:~$ cat /proc/cpuinfo
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

user@starfive:~$
```

## Test Criteria

Test success: The actual result is consistent with the expected result.

Test failure: The actual result is inconsistent with the expected result.

## Test Conclusion

Test successful.
