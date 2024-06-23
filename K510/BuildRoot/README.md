# BuildRoot K510 Test Report

## Test Environment

### Operating System Information

- Build System Environment: Ubuntu 20.04.4 LTS in Docker
- System Version: v1.9
- Reference Installation Document: https://github.com/kendryte/k510_buildroot

### Hardware Information

- Canaan K510 CRB-V1.2 KIT
- A USB Power Adapter
- Two USB-A to C Cables (included with the development board; one for power supply and the other for USB-UART and auxiliary power supply)
- A microSD Card (minimum capacity of 1GiB; default generated image size is 512MiB)

## Installation Steps

### Building System Image

#### Installing Docker

Refer to the documentation for your specific distribution or the official Docker documentation for installation instructions.

#### Clone Source Repository

```shell
git clone --depth=1 https://github.com/kendryte/k510_buildroot
```

#### Build the Image

```shell
sh k510_buildroot/tools/docker/run_k510_docker.sh
make dl
make
```

Note: The build is single-threaded by default, which can take a considerable amount of time. Ensure you have a stable network connection.

Upon completion, the `sysimage-sdcard.img` image will be generated in the `k510_buildroot/k510_crb_lp3_v1_2_defconfig/image/` directory.

#### Flashing the Image with dd

Note: `/dev/sdc` represents the location of the storage card. Modify according to your actual setup.

```shell
sudo dd if=sysimage-sdcard.img of=/dev/sdc bs=1M status=progress
```

### Logging into the System

Insert the microSD card and ensure the onboard SW1 switch is set to boot from the microSD card position:

| BOOT1  | BOOT0  | Boot Mode  |
|--------|--------|------------|
| 0(ON)  | 0(ON)  | Serial     |
| 0(ON)  | 1(OFF) | microSD    |
| 1(OFF) | 0(ON)  | NAND Flash |
| 1(OFF) | 1(OFF) | eMMC       |

Connect the USB Type-C for power and the USB-UART serial cable. The connectors are located on either side of the development board, labeled `DC:5V` and `UART` respectively.

(The K510 features an onboard CH340 for USB-UART, allowing direct connection. The UART interface also serves as an auxiliary power supply via USB, so it's recommended to connect it.)

Switch the power button `K1` to the ON position, connect via serial, and log into the system.

## Expected Results

The system should boot normally and allow login via the onboard serial port.

## Actual Results

The system booted successfully and login via the onboard serial port was also successful.

### Boot Information

```log
[root@canaan ~ ]$ uname -a
Linux canaan 4.17.0 #1 SMP PREEMPT Fri Apr 12 18:13:44 CST 2024 riscv64 GNU/Linux
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

Screen recording (From flashing image to login):

[![asciicast](https://asciinema.org/a/wdVYHHOcy5laeXA2tKewkqNRR.svg)](https://asciinema.org/a/wdVYHHOcy5laeXA2tKewkqNRR)

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
