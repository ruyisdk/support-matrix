---
sys: openeuler
sys_ver: 24.03-LTS-SP1
sys_var: null

status: Basic
last_update: 2025-05-21
---

# SpacemiT Muse Pi Pro, openEuler 24.03-LTS-SP1 Test Report

## Test Environment

### System Information

- Download Link: https://images.oerv.ac.cn/board?uri=products/spacemit/muse_pi_pro.json&name=MUSE+Pi+Pro
- Reference Install Document: https://developer.spacemit.com/documentation?token=QSfGwmkhqiHwqQkHmCicH2Qnnyg
- Reference Install Document: https://images.oerv.ac.cn/board?uri=products/spacemit/muse_pi_pro.json&name=MUSE+Pi+Pro

### Hardware Information

- SpacemiT Muse Pi Pro Board
- USB Charger
- USB Type-C cables
- UART to USB Debugger
- microSD Card

## Installation Steps

### Flashing the firmware

The original Muse Pi Pro uses UEFI as its firmware, but the openEuler uses U-Boot and BootSTD as its firmware. So, we need to flash the firmware to the Muse Pi Pro's SPI NOR flash. 

Download the firmware, and extract it. Then, use `fastboot` to flash the firmware to the SPI NOR flash.

```bash
wget https://repo.tarsier-infra.isrc.ac.cn/openEuler-RISC-V/testing/spacemit_k1_20250421/spacemit_k1_fw.tar.zst
tar -xvf spacemit_k1_fw.tar.zst
```

Under the USB Type-A port, you can see three buttons. Let the ethernet port facing up, from top to bottom, the buttons are **PWR**, **RST**, and **FDL** . You shall hold the **FDL** button while power on/RST, to enter the fastboot mode. You shall see the dfu-device in your system:

```log
❯ sudo fastboot devices
dfu-device       DFU download
```

Then, use `fastboot` to flash the firmware to the SPI NOR flash.

```bash
fastboot stage FSBL.bin
fastboot continue
sleep 1 # wait for 1s
fastboot stage u-boot.itb
fastboot continue
sleep 1 # wait for 1s
fastboot flash mtd partition.json
fastboot flash mtd-bootinfo bootinfo_spinor.bin
fastboot flash mtd-fsbl FSBL.bin
fastboot flash mtd-opensbi fw_dynamic.itb
fastboot flash mtd-uboot u-boot.itb
```

**Note: This will remove the original UEFI bootloader. How to restore it will be discussed below.**

### Flashing the Image to SD Card

Use `dd` to flash the image to the microSD card.

```bash
wget https://repo.tarsier-infra.isrc.ac.cn/openEuler-RISC-V/testing/spacemit_k1_20250421/openEuler-24.03-LTS-SP1-base-spacemit_k1-testing.img.zst
zstd -d openEuler-24.03-LTS-SP1-base-spacemit_k1-testing.img.zst
```

```bash
sudo dd if=openEuler-24.03-LTS-SP1-base-spacemit_k1-testing.img of=/dev/your-device bs=1M status=progress
```

Please replace `/dev/your-device` with the actual device name of your microSD card. Make sure to double-check the device name to avoid overwriting your own disk.

### Logging into the System

Logging into the system via the serial port.

Default Username: `root`/`openeuler`
Default Password: `openEuler12#$`

### Restore UEFI Bootloader

In order to restore the UEFI bootloader, you need to flash the original UEFI firmware to the SPI NOR flash. You can find the firmware in the spacemit bianbu system. You can find the image at the following link:
[https://archive.spacemit.com/image/k1/version/bianbu-computer-uefi/](https://archive.spacemit.com/image/k1/version/bianbu-computer-uefi/)

After downloading the firmware, extract it. Then, use `fastboot` to flash the firmware to the SPI NOR flash.

```bash
sudo fastboot stage factory/FSBL.bin
sudo fastboot continue
sleep 1 # Wait for 1 sec
sudo fastboot stage edk2.itb
sudo fastboot continue
sleep 1 # wait for 1s
fastboot flash mtd partition_2M.json
fastboot flash mtd-bootinfo factory/bootinfo_spinor.bin
fastboot flash mtd-fsbl factory/FSBL.bin
fastboot flash mtd-env env.bin
fastboot flash mtd-opensbi fw_dynamic.itb
fastboot flash mtd-uboot edk2.itb
```

## Expected Results

The system should boot normally and allow login via the onboard serial port.

## Actual Results

The system booted successfully and login via the onboard serial port was also successful.

### Boot Log

Screen recording (from flashing image to login):
[![asciicast](https://asciinema.org/a/UPkandKkjpEHPjdGBsl9CMXjt.svg)](https://asciinema.org/a/UPkandKkjpEHPjdGBsl9CMXjt)

```log
openEuler 24.03 (LTS-SP1)
Kernel 6.6.63-0.0.0.23.oe2403sp1.riscv64 on an riscv64

Activate the web console with: systemctl enable --now cockpit.socket

openeuler-riscv64 login: root
Password: 


Welcome to 6.6.63-0.0.0.23.oe2403sp1.riscv64

System information as of time:  Sat Jan  1 08:00:39 CST 2000

System load:    3.06
Memory used:    1.0%
Swap used:      0.0%
Usage On:       3%
Users online:   1


[root@openeuler-riscv64 ~]# uname -a
Linux openeuler-riscv64 6.6.63-0.0.0.23.oe2403sp1.riscv64 #1 SMP PREEMPT Sun Apr 20 10:21:48 UTC 2025 riscv64 riscv64 riscv64 GNU/Linux
[root@openeuler-riscv64 ~]# cat /etc/os-release 
NAME="openEuler"
VERSION="24.03 (LTS-SP1)"
ID="openEuler"
VERSION_ID="24.03"
PRETTY_NAME="openEuler 24.03 (LTS-SP1)"
ANSI_COLOR="0;31"

[root@openeuler-riscv64 ~]# lscpu
Architecture:          riscv64
  Byte Order:          Little Endian
CPU(s):                8
  On-line CPU(s) list: 0-7
Model name:            Spacemit(R) X60
  Thread(s) per core:  1
  Core(s) per socket:  8
  Socket(s):           1
  Frequency boost:     disabled
  CPU(s) scaling MHz:  100%
  CPU max MHz:         1600.0000
  CPU min MHz:         614.4000
Caches (sum of all):   
  L1d:                 256 KiB (8 instances)
  L1i:                 256 KiB (8 instances)
  L2:                  1 MiB (2 instances)
NUMA:                  
  NUMA node(s):        1
  NUMA node0 CPU(s):   0-7
```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
