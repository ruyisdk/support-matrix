---
sys: deepin
sys_ver: 20241227
sys_var: null

status: good
last_update: 2025-01-22
---

# Deepin preview LPi4A Test Report

## Test Environment

### System Information

- System Version: Deepin preview 20241227
- Download Link: https://deepin-community.github.io/sig-deepin-ports/images/riscv/download
- Reference Installation Document: https://cdimage.deepin.com/RISC-V/preview-20240517-riscv64/README.md

### Hardware Information

- Lichee Pi 4A (16GB RAM + 128GB eMMC)
- Power Adapter
- A USB to UART Debugger

## Installation Steps

### Get uboot

The tar doesn't contain the u-boot bin, you need to get it on your own: https://cdimage.deepin.com/RISC-V/preview-20240815-riscv64/uboot-th1520-revyos.zip

Choose whether you need the 16g version based on your ram size.

If you are using a 8GB version LicheePi 4A , use the `light_lpi4a/u-boot-with-spl.bin`

If you are using a 16GB version LicheePi 4A , use the `light_lpi4a_16g/u-boot-with-spl.bin`

### Flashing the Bootloader

Extract the installation suite.
Flash the u-boot and boot.

```bash
tar -xvf deepin-23-beige-preview-riscv64-th1520-20241227-161022.tar.xz
sudo fastboot flash ram u-boot-with-spl.bin
sudo fastboot reboot
sudo fastboot flash uboot u-boot-with-spl.bin
sudo fastboot flash boot deepin-th1520-riscv64-v23-desktop-installer.boot.ext4
```

### Flashing the Image

Flash the root partition into the eMMC.

```bash
sudo fastboot flash root deepin-th1520-riscv64-v23-desktop-installer.root.ext4
```

### Logging into the System

Reboot the system, then a installization guide will pop out.

Default username: `root`
Password: `deepin`

## Expected Results

The system should boot successfully, allowing login via the onboard serial console.

## Actual Results

The system boots up successfully, and login via onboard serial port is successful.

### Boot Log

```log
Deepin GNU/Linux 23 deepin-riscv64-th1520 ttyS0

deepin-riscv64-th1520 login: root
Password:
Verification successful
Linux deepin-riscv64-th1520 5.10.113-th1520-revyos-510 #1 SMP PREEMPT Tue Aug 27 10:05:53 UTC 2024 riscv64
Welcome to Deepin 23 GNU/Linux

    * Homepage:https://www.deepin.org/

    * Bugreport:https://bbs.deepin.org/


root@deepin-riscv64-th1520:~# uname -a
Linux deepin-riscv64-th1520 5.10.113-th1520-revyos-510 #1 SMP PREEMPT Tue Aug 27 10:05:53 UTC 2024 riscv64 GNU/Linux
root@deepin-riscv64-th1520:~# cat /etc/os-release 
PRETTY_NAME="Deepin 23"
NAME="Deepin"
VERSION_ID="23"
VERSION="23"
ID=deepin
HOME_URL="https://www.deepin.org/"
BUG_REPORT_URL="https://bbs.deepin.org"
VERSION_CODENAME=beige
root@deepin-riscv64-th1520:~# cat /proc/cpuinfo 
processor       : 0
hart            : 0
isa             : rv64imafdcvsu
mmu             : sv39
cpu-freq        : 1.848Ghz
cpu-icache      : 64KB
cpu-dcache      : 64KB
cpu-l2cache     : 1MB
cpu-tlb         : 1024 4-ways
cpu-cacheline   : 64Bytes
cpu-vector      : 0.7.1

processor       : 1
hart            : 1
isa             : rv64imafdcvsu
mmu             : sv39
cpu-freq        : 1.848Ghz
cpu-icache      : 64KB
cpu-dcache      : 64KB
cpu-l2cache     : 1MB
cpu-tlb         : 1024 4-ways
cpu-cacheline   : 64Bytes
cpu-vector      : 0.7.1

processor       : 2
hart            : 2
isa             : rv64imafdcvsu
mmu             : sv39
cpu-freq        : 1.848Ghz
cpu-icache      : 64KB
cpu-dcache      : 64KB
cpu-l2cache     : 1MB
cpu-tlb         : 1024 4-ways
cpu-cacheline   : 64Bytes
cpu-vector      : 0.7.1

processor       : 3
hart            : 3
isa             : rv64imafdcvsu
mmu             : sv39
cpu-freq        : 1.848Ghz
cpu-icache      : 64KB
cpu-dcache      : 64KB
cpu-l2cache     : 1MB
cpu-tlb         : 1024 4-ways
cpu-cacheline   : 64Bytes
cpu-vector      : 0.7.1
```

![](./image.png)

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
