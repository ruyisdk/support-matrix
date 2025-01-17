---
sys: deepin
sys_ver: 20240815
sys_var: null

status: cfh
last_update: 2024-10-31
---

# Deepin preview LPi4A Test Report

## Test Environment

### System Information

- System Version: Deepin preview 20240815
- Download Link: https://cdimage.deepin.com/RISC-V/preview-20240815-riscv64/deepin-23-beige-preview-riscv64-th1520-20240815-132955.tar.xz
- Reference Installation Document: https://cdimage.deepin.com/RISC-V/preview-20240517-riscv64/README.md

### Hardware Information

- Lichee Pi 4A (8GB RAM + 32GB eMMC)
- Power Adapter
- A USB to UART Debugger

## Installation Steps

Note: The official deepin site has a really slow connection. Recommand use some mirror site like [Qilu University of Technology](https://mirrors.qlu.edu.cn/deepin-cd/deepin-cd/RISC-V/preview-20240815-riscv64/)

### Get uboot

The tar doesn't contain the u-boot bin, you need to get it on your own: https://cdimage.deepin.com/RISC-V/preview-20240815-riscv64/uboot-th1520-revyos.zip

Choose whether you need the 16g version based on your ram size.

If you are using a 8GB version LicheePi 4A , use the `light_lpi4a/u-boot-with-spl.bin`

If you are using a 16GB version LicheePi 4A , use the `light_lpi4a_16g/u-boot-with-spl.bin`

### Flashing the Bootloader

Extract the installation suite.
Flash the u-boot and boot.

```bash
tar -xvf deepin-23-beige-preview-riscv64-th1520-20240815-132955.tar.xz
sudo fastboot flash ram u-boot-with-spl.bin
sudo fastboot reboot
sudo fastboot flash uboot u-boot-with-spl.bin
sudo fastboot flash boot deepin-th1520-riscv64-stable-desktop-installer.boot.ext4
```

### Flashing the Image

Flash the root partition into the eMMC.

```bash
sudo fastboot flash root deepin-th1520-riscv64-stable-desktop-installer.root.ext4
```

### Logging into the System

Reboot the system, then a installization guide will pop out.

Default username: `root`
Password: `deepin`

## Expected Results

The system should boot successfully, allowing login via the onboard serial console.

## Actual Results

AON firmware is not working properly, the system is not booting.

### How to fix

Just get a aon firmware from RevyOS and put it into the boot partition, then it works.

You can get the aon firmware from this image: [https://mirror.iscas.ac.cn/revyos/extra/images/lpi4a/20240720/boot-lpi4a-20240720_171951.ext4.zst](https://mirror.iscas.ac.cn/revyos/extra/images/lpi4a/20240720/boot-lpi4a-20240720_171951.ext4.zst)

```bash
sudo losetup -P boot-lpi4a-20240720_171951.ext4
sudo losetup boot-lpi4a-20240720_171951.ext4
sudo losetup -f boot-lpi4a-20240720_171951.ext4
mkdir mnt
sudo mount /dev/loop0 mnt
ls mnt
cp mnt/light_aon_fpga.bin .
sudo umount mnt
sudo losetup -f deepin-th1520-riscv64-stable-desktop-installer.boot.ext4
sudo mount /dev/loop1 mnt
sudo rm mnt/light_aon_fpga.bin
sudo cp light_aon_fpga.bin mnt/
sudo umount mnt
sudo losetup -d /dev/loop1
sudo fastboot flash ram light_lpi4a/u-boot-with-spl.bin
sudo fastboot reboot
sudo fastboot flash boot deepin-th1520-riscv64-stable-desktop-installer.boot.ext4

```

See [issue](https://github.com/linuxdeepin/developer-center/issues/10829)

### Boot Log

Screen recording (system login):
Waiting for system to be fixed...

```log
deepin-riscv64-th1520 login: root
Password:
Verification successful
Linux deepin-riscv64-th1520 5.10.113-th1520 #1 SMP PREEMPT Wed Apr 24 13:12:14 UTC 2024 riscv64
Welcome to Deepin 23 GNU/Linux

    * Homepage:https://www.deepin.org/

    * Bugreport:https://bbs.deepin.org/


root@deepin-riscv64-th1520:~# cat /etc/os-release 
PRETTY_NAME="Deepin 23"
NAME="Deepin"
VERSION_ID="23"
VERSION="23"
ID=deepin
HOME_URL="https://www.deepin.org/"
BUG_REPORT_URL="https://bbs.deepin.org"
VERSION_CODENAME=beige
root@deepin-riscv64-th1520:~# uname -a
Linux deepin-riscv64-th1520 5.10.113-th1520 #1 SMP PREEMPT Wed Apr 24 13:12:14 UTC 2024 riscv64 GNU/Linux
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

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

CFH
