---
sys: deepin
sys_ver: 25-beige-preview
sys_var: null

status: good
last_update: 2025-04-07
---

# Deepin preview LPi4A Test Report

## Test Environment

### System Information

- System Version: Deepin 25-beige-preview 20250122
- Download Link: https://deepin-community.github.io/sig-deepin-ports/images/riscv/download
- Reference Installation Document: https://cdimage.deepin.com/RISC-V/preview-20240517-riscv64/README.md
- Desktop Environment: DDE (Pre-installed in the image)

### Hardware Information

- Lichee Pi 4A (8GB RAM + 32GB eMMC)
- Power Adapter
- A USB to UART Debugger

## Installation Steps

### Get Image

Download image and decompress.

```bash
wget https://ci.deepin.com/repo/deepin/deepin-ports/cdimage/20250122/riscv64/deepin-25-beige-preview-riscv64-th1520-20250122-113934.tar.xz
tar -xvf deepin-25-beige-preview-riscv64-th1520-20250122-113934.tar.xz
```

### Get u-boot

The tar doesn't contain the u-boot bin, you need to get it on your own: https://cdimage.deepin.com/RISC-V/preview-20240815-riscv64/uboot-th1520-revyos.zip

Choose whether you need the 16g version based on your ram size.

If you are using a 8GB version LicheePi 4A , use the `light_lpi4a/u-boot-with-spl.bin`

If you are using a 16GB version LicheePi 4A , use the `light_lpi4a_16g/u-boot-with-spl.bin`

```bash
wget https://cdimage.deepin.com/RISC-V/preview-20240815-riscv64/uboot-th1520-revyos.zip
unzip uboot-th1520-revyos.zip
```

### Flashing the Image

Use `fastboot` flash image.

```bash
sudo fastboot flash ram light_lpi4a/u-boot-with-spl.bin
sudo fastboot reboot
sudo fastboot flash uboot light_lpi4a/u-boot-with-spl.bin
sudo fastboot flash boot deepin-th1520-riscv64-25-desktop-installer.boot.ext4
sudo fastboot flash root deepin-th1520-riscv64-25-desktop-installer.root.ext4
```

### Logging into the System

Default username: `root`
Password: `deepin`

The frist startup will take you to the installation guide to create users on your own.

## Expected Results

The system should boot successfully, allowing login via the onboard serial console.

## Actual Results

The system boots up successfully, and login via onboard serial port is successful. Can login to the desktop environment.

### Boot log

```log
Deepin GNU/Linux 23 deepin-riscv64-th1520 ttyS0

deepin-riscv64-th1520 login: root
Password:
Verification successful
Linux deepin-riscv64-th1520 5.10.113-th1520-revyos-510 #1 SMP PREEMPT Tue Aug 27 10:05:53 UTC 2024 riscv64
Welcome to deepin 25 GNU/Linux

    * Homepage: https://www.deepin.org/

    * Bugreport: https://bbs.deepin.org/


root@deepin-riscv64-th1520:~# uname -a
Linux deepin-riscv64-th1520 5.10.113-th1520-revyos-510 #1 SMP PREEMPT Tue Aug 27 10:05:53 UTC 2024 riscv64 GNU/Linux
root@deepin-riscv64-th1520:~# cat /etc/os-release
PRETTY_NAME="Deepin 25"
NAME="Deepin"
VERSION_CODENAME=beige
ID=deepin
HOME_URL="https://www.deepin.org/"
BUG_REPORT_URL="https://bbs.deepin.org"
VERSION_ID="25"
VERSION="25"
root@deepin-riscv64-th1520:~# lscpu
Architecture:          riscv64
  Byte Order:          Little Endian
CPU(s):                4
  On-line CPU(s) list: 0-3
root@deepin-riscv64-th1520:~#
```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.

