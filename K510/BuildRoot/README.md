---
sys: buildroot
sys_ver: "2020.02.11"
sys_var: null
provider: Vendor
status: basic
last_update: 2026-08-30
---

# BuildRoot K510 Test Report

## Test Environment

### Operating System Information

- Build environment: Ubuntu 20.04.4 LTS in Docker
- System Version: Buildroot 2020.02.11
- Installation reference: https://github.com/kendryte/k510_buildroot

### Hardware Information

- Canaan K510 CRB-V1.2 KIT
- One USB power adapter
- Two USB-A to Type-C cables (included with the development board; one for power supply and the other for USB-UART and auxiliary power supply)
- One microSD card (capacity ≥ 1 GiB; the default generated image size is 512 MiB)

## Installation Steps

### Build the System Image

#### Install Docker

Refer to the documentation for your Linux distribution or the official Docker documentation for installation.

Verify that Docker is working properly:

```shell
docker --version
```

#### Clone the Source Repository

```shell
git clone --depth=1 https://github.com/kendryte/k510_buildroot
```

#### Start the Build

Enter the Docker build environment:

```shell
sh k510_buildroot/tools/docker/run_k510_docker.sh

# Run inside the container:
make dl
make

# Exit the container after the build is complete:
exit
```

Note that the build uses a single thread by default and may take a long time. Make sure the network connection is stable.

Locate the generated system image:

```shell
find k510_buildroot/k510_crb_lp3_v1_2_defconfig \
-name "sysimage-sdcard.img" -type f
```

The image generated in this test was:

```shell
k510_buildroot/k510_crb_lp3_v1_2_defconfig/images/sysimage-sdcard.img
```

#### Flash the Image Using `dd`

Note that `/dev/sdX` is the device corresponding to the microSD card. Modify it according to the actual device path.

```shell
sudo dd if=k510_buildroot/k510_crb_lp3_v1_2_defconfig/images/sysimage-sdcard.img of=/dev/sdX bs=1M status=progress
```

### Log In to the System

Insert the microSD card and make sure the onboard SW1 switch is set to microSD boot mode:

| BOOT1  | BOOT0  | Boot Mode  |
| ------ | ------ | ---------- |
| 0(ON)  | 0(ON)  | UART       |
| 0(ON)  | 1(OFF) | microSD    |
| 1(OFF) | 0(ON)  | NAND Flash |
| 1(OFF) | 1(OFF) | eMMC       |

Connect the development board:

- `DC:5V`: Power supply
- `UART`: USB-UART serial port

Confirm the serial device, for example:

```text
/dev/ttyUSB0
```

Configure the serial port when using minicom for the first time:

```shell
sudo minicom -s
```

Configure the following settings:

```text
Serial Device          : /dev/ttyUSB0
Bps/Par/Bits           : 115200 8N1
Hardware Flow Control  : No
```

Open the serial terminal:

```shell
sudo minicom
```

Set the `K1` power switch to `ON` and wait for the system to boot.

Login information:

```text
Username: root
Password: empty (press Enter directly)
```

## Expected Results

The system boots normally and can be accessed through the onboard serial port.

## Actual Results

The system booted normally and was successfully accessed through the onboard serial port.

### Boot Information

```log
[root@canaan ~ ]$ uname -a
Linux canaan 4.17.0 #1 SMP PREEMPT Tue Jul 14 18:27:09 CST 2026 riscv64 GNU/Linx

[root@canaan ~ ]$ cat /etc/os-release
NAME=Buildroot
VERSION=-g2ce01d0
ID=buildroot
VERSION_ID=2020.02.11
PRETTY_NAME="Buildroot 2020.02.11"

[root@canaan ~ ]$ cat /proc/cpuinfo
hart    : 0
isa     : rv64i2p0m2p0a2p0f2p0d2p0c2p0xv5-0p0
mmu     : sv39

hart    : 1
isa     : rv64i2p0m2p0a2p0f2p0d2p0c2p0xv5-0p0
mmu     : sv39

[root@canaan ~ ]$
```

Screen recording (from flashing the image to logging in to the system):

[![asciicast](https://asciinema.org/a/1264225.svg)](https://asciinema.org/a/1264225)

## Test Criteria

Test successful: The actual results match the expected results.

Test failed: The actual results do not match the expected results.

## Test Conclusion

Test successful.
