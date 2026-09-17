---
sys: debian
sys_ver: "202510"
sys_var: null
provider: Vendor
status: basic
last_update: 2026-08-30
---

# Debian VisionFive 2 Lite Test Report

## Test Environment

### Operating System Information

- System Version: Debian GNU/Linux trixie/sid (StarFive Debian 202510 Engineering Release)
- Download Link: [https://github.com/starfive-tech/Debian/](https://github.com/starfive-tech/Debian/releases/download/v0.15.0-engineering-release-wayland/starfive-jh7110-202510-minimal-desktop-wayland.img.bz2)
- Reference Installation Document: [Flashing OS to Onboard eMMC (eMMC Version)](https://doc-en.rvspace.org/VisionFive2Lite/VisionFive2LiteQSG/VisionFive2_QSGLite/flashing_os_to_onboard_emmc_emmc_version.html)

### Hardware Information

- VisionFive 2 Lite
- USB-TTL
- Type-C data cable
- Three Dupont wires

## Installation Steps

### Decompress the Image

Download `starfive-jh7110-202510-minimal-desktop-wayland.img.bz2` and decompress it to obtain:

```text
starfive-jh7110-202510-minimal-desktop-wayland.img
```

### Prepare Flashing Tools

The following tools are required:

```text
fastboot
img2simg
```

On an Ubuntu/Debian host, run:

```bash
sudo apt update
sudo apt install -y fastboot android-sdk-libsparse-utils
```

On a Windows host, install Android Platform Tools to obtain `fastboot`, and install `android-sdk-libsparse-utils` through WSL or another Linux environment to obtain `img2simg`.

### Connect the Serial Port

Connect the VisionFive 2 Lite using a USB to UART debugger:

```text
VisionFive 2 Lite GND -> USB-UART GND
VisionFive 2 Lite TX  -> USB-UART RX
VisionFive 2 Lite RX  -> USB-UART TX
```

Connect to the board using a serial terminal with the following parameters:

```text
Baud rate:    115200
Data bits:    8
Parity:       none
Stop bits:    1
Flow control: none
```

At the same time, connect the VisionFive 2 Lite to the host using a USB Type-C cable.

### Enter Fastboot Mode

Power on the board and press any key during the U-Boot countdown to interrupt automatic boot and enter U-Boot.

Run:

```bash
fastboot usb 0
```

Check the Fastboot device on the host:

```bash
fastboot devices
```

The output should be similar to:

```text
<device_serial>    fastboot
```

This indicates that the board has successfully entered Fastboot mode.

### Convert to a Sparse Image

Enter the directory containing the image:

```bash
cd <path-to-image>
```

Run:

```bash
img2simg \
starfive-jh7110-202510-minimal-desktop-wayland.img \
starfive-jh7110-202510-minimal-desktop-wayland-sparse.img
```

After conversion, the following image is generated:

```text
starfive-jh7110-202510-minimal-desktop-wayland-sparse.img
```

### Flash the Image to eMMC

Check the Fastboot device again:

```bash
fastboot devices
```

Flash the sparse image to the onboard eMMC:

```bash
fastboot flash mmc0 starfive-jh7110-202510-minimal-desktop-wayland-sparse.img
```

The actual flashing result in this test was:

```text
Sending sparse 'mmc0' 1/4 (1044499 KB)             OKAY [ 30.351s]
Writing 'mmc0'                                     OKAY [ 30.389s]
Sending sparse 'mmc0' 2/4 (1047329 KB)             OKAY [ 30.142s]
Writing 'mmc0'                                     OKAY [ 27.204s]
Sending sparse 'mmc0' 3/4 (1006939 KB)             OKAY [ 29.268s]
Writing 'mmc0'                                     OKAY [ 29.344s]
Sending sparse 'mmc0' 4/4 (783420 KB)              OKAY [ 22.683s]
Writing 'mmc0'                                     OKAY [ 20.660s]
Finished. Total time: 222.577s
```

After flashing is complete, power off the board, wait a few seconds, and power it on again.

### Logging into the System

Log into the system via the serial port.

Default username: `user`

Default password: `starfive`

## Expected Results

The system should boot up normally and allow login via the serial port.

## Actual Results

The system booted up successfully, and login via the serial port was successful.

### Boot Log

```log
Debian GNU/Linux trixie/sid starfive ttyS0

starfive login: user
Password:
Linux starfive 6.12.5-starfive #70SF SMP Sun Sep 28 11:33:07 UTC 2025 riscv64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
[   37.017948] mipi_0p9: disabling
user@starfive:~$ uname -a
Linux starfive 6.12.5-starfive #70SF SMP Sun Sep 28 11:33:07 UTC 2025 riscv64 GNU/Linux
user@starfive:~$ cat /etc/os-release
PRETTY_NAME="Debian GNU/Linux trixie/sid"
NAME="Debian GNU/Linux"
VERSION_CODENAME=trixie
ID=debian
HOME_URL="https://www.debian.org/"
SUPPORT_URL="https://www.debian.org/support"
BUG_REPORT_URL="https://bugs.debian.org/"
BUILD_ID=70
BUILD_DATE=T2025-09-30
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

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
