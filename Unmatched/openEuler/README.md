---
sys: openeuler
sys_ver: "24.03-LTS-SP2"
sys_var: LTS

status: basic
last_update: 2025-10-24
---

# openEuler RISC-V 24.03 LTS SP2 HiFive Unmatched Test Report

## Test Environment

### Operating System Information

- System Version: openEuler 24.03 LTS SP2
- Download Link: https://www.openeuler.openatom.cn/en/download/#openEuler%2024.03%20LTS%20SP2
- Reference Installation Document
    - https://ruyisdk.cn/t/topic/1525
    - https://wiki.debian.org/InstallingDebianOn/SiFive/HiFiveUnmatched

> [!NOTE]
> This is the official mainline openEuler riscv64 DVD ISO.
> You'll need mainline U-Boot with EFI support to boot.
> In this test report there's no GPU installed. In theory, you should be able to use GUI if there is a GPU.

### Hardware Information

- HiFive Unmatched Rev A
- A microUSB cable (included with HiFive Unmatched)
- An ATX power supply
- A microSD card or USB drive (large enough to store the openEuler ISO image)
- M.2 NVMe SSD (Optional, follow the installation document)
- Internet connection

The following are for users expecting a desktop experience:
- A PCIe graphics card
- USB Keyboard & Mouse
- Display (and its cables)

## Installation Steps

### Build and flash U-Boot to SPI Flash

Need a running OS on the Unmatched.

You can obtain U-Boot binary from Debian.

```shell
wget http://deb.debian.org/debian/pool/main/u/u-boot/u-boot-sifive_2025.01-3_riscv64.deb
dpkg -x u-boot-sifive_2025.01-3_riscv64.deb .
# If you're not on Debian, you may try 7-Zip
# 7z x u-boot-sifive_2025.01-3_riscv64.deb
# tar xvf data.tar
# Or with ar
# ar x u-boot-sifive_2025.01-3_riscv64.deb
# tar xvf data.tar.xz
cd usr/lib/u-boot/sifive_unmatched
sudo modprobe mtdblock
sgdisk --clear -a 1 \
    --new=1:40:2087     --change-name=1:spl   --typecode=1:5B193300-FC78-40CD-8002-E86C45580B47 \
    --new=2:2088:10279  --change-name=2:uboot --typecode=2:2E54B353-1271-4842-806F-E436D6AF6985 \
    --new=3:10280:10535 --change-name=3:env   --typecode=3:3DE21764-95BD-54BD-A5C3-4ABE786F38A8 \
    /dev/mtdblock0
dd if=u-boot-spl.bin of=/dev/mtdblock0 bs=4096 seek=5 conv=sync
dd if=u-boot.itb  of=/dev/mtdblock0 bs=4096 seek=261 conv=sync
```

After flashing, poweroff the board normally.

### Boot Device Selection

Ensure the dip switch is set to boot from SPI Flash. If not changed, the factory default is to boot from the microSD card.

The dip switch should be set as follows: `MSEL[3:0]=1011`

### Use `dd` to Flash the Image to the microSD Card

```shell
wget https://dl-cdn.openeuler.openatom.cn/openEuler-24.03-LTS-SP2/ISO/riscv64/openEuler-24.03-LTS-SP2-netinst-riscv64-dvd.iso
sudo wipefs -af /dev/sdX
sudo dd if=openEuler-24.03-LTS-SP2-netinst-riscv64-dvd.iso of=/dev/sdX bs=1M status=progress
sync; sudo eject /dev/sdX
```

Unplug the USB drive/microSD card, and insert it into any USB ports/microSD slot on Unmatched.

### OS Installation

There are 2 serial ports on Unmatched, the second of which is the CPU serial.

If there's no GPU installed, openEuler's Anaconda installer will fallback to output on serial.

In this report we're using serial terminal, with the text installer.

(This is not the most convenient way however, it's more recommended to plug in a GPU and use the GUI installer instead.)

See [this](<https://asciinema.org/a/HncsUaCkyzLLomdo1rmwFT7hF)>) screen record for installation process.

Some notable issues:

1. You'll need to fill in the network install source manually, e.g. https://repo.openeuler.org/openEuler-24.03-LTS-SP2/OS/riscv64/
2. You may have troubles installing GRUB, when prompting as below, choose yes:
```
Question

The following error occurred while installing the boot loader. The system will                                          
not be bootable. Would you like to ignore this and continue with installation?                                          

Failed to set new efi boot target. This is most likely a kernel or firmware bug.

Please respond 'yes' or 'no'
```
3. By default U-Boot can't pick up GRUB EFI. After the installation finished and rebooted, remove the installation media, enters U-Boot, interrupt autoboot and run the following commands to boot temporarily:
```shell
nvme scan
load nvme 0:1 $kernel_addr_r /EFI/openEuler/grubriscv64.efi
bootefi $kernel_addr_r
```
4. After entering the system, you'll need to install GRUB as `--removable` to make U-Boot pick up GRUB automatically and boot:
```shell
dnf install -y grub2-efi-riscv64-modules
grub2-install --removable
grub2-mkconfig -o /boot/grub2/grub.cfg
```

### Logging into the System

Log into the system via the onboard serial port (using the microUSB cable connected to another computer).

Default username and password are set during the installation process.

## Expected Results

The system should boot normally and allow login through the onboard serial port.

## Actual Results

The system booted successfully and login through the onboard serial port was successful.

### Boot Log

```log
Welcome to 6.6.0-98.0.0.103.oe2403sp2.riscv64

System information as of time:  Fri Sep 19 09:43:03 PM CST 2025

System load:    3.39
Memory used:    1.6%
Swap used:      0%
Usage On:       3%
IP address:     10.0.0.116
Users online:   1


[root@localhost ~]# cat /etc/os-release
NAME="openEuler"
VERSION="24.03 (LTS-SP2)"
ID="openEuler"
VERSION_ID="24.03"
PRETTY_NAME="openEuler 24.03 (LTS-SP2)"
ANSI_COLOR="0;31"

[root@localhost ~]# cat[   70.739081][ T5034] Btrfs loaded, zoned=yes, fsverity=no
 /sys/firmware/[   72.697419][ T5276] systemd-rc-local-generator[5276]: /etc/rc.d/rc.local is not marked executable, skipping.

devicetree/ efi/        fdt
[root@localhost ~]# cat /sys/firmware/[  OK  ] Reached target Multi-User System.
         Starting Record Runlevel Change in UTMP...
[  OK  ] Finished openEuler Security Tool.
[  OK  ] Finished Record Runlevel Change in UTMP.
devicetree/base/
#address-cells   config/          memory@80000000/ serial-number
aliases/         cpus/            model            #size-cells
binman/          fit-images/      name             soc/
chosen/          gpio-poweroff/   reserved-memory/
compatible       hfclk/           rtcclk/
[root@localhost ~]# cat /sys/firmware/devicetree/base/model
SiFive HiFive Unmatched A00[root@localhost ~]# cat /proc/cpuinfo
processor       : 0
hart            : 2
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd
mmu             : sv39
uarch           : sifive,bullet0
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x20181004

processor       : 1
hart            : 1
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd
mmu             : sv39
uarch           : sifive,bullet0
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x20181004

processor       : 2
hart            : 3
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd
mmu             : sv39
uarch           : sifive,bullet0
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x20181004

processor       : 3
hart            : 4
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd
mmu             : sv39
uarch           : sifive,bullet0
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x20181004

[root@localhost ~]# cat /sys/firmware/devicetree/base/model
SiFive HiFive Unmatched A00[root@localhost ~]#
[root@localhost ~]# uname -a
Linux localhost.localdomain 6.6.0-98.0.0.103.oe2403sp2.riscv64 #1 SMP PREEMPT Fri Jun 27 10:45:15 UTC 2025 riscv64 riscv64 riscv64 GNU/Linux
[root@localhost ~]# cat /etc/os-release
NAME="openEuler"
VERSION="24.03 (LTS-SP2)"
ID="openEuler"
VERSION_ID="24.03"
PRETTY_NAME="openEuler 24.03 (LTS-SP2)"
ANSI_COLOR="0;31"

[root@localhost ~]# cat /etc/openEuler-release
openEuler release 24.03 (LTS-SP2)
[root@localhost ~]# lscpu
Architecture:          riscv64
  Byte Order:          Little Endian
CPU(s):                4
  On-line CPU(s) list: 0-3
NUMA:
  NUMA node(s):        1
  NUMA node0 CPU(s):   0-3
[root@localhost ~]#
```

Screen record:
[![asciicast](https://asciinema.org/a/HncsUaCkyzLLomdo1rmwFT7hF.svg)](https://asciinema.org/a/HncsUaCkyzLLomdo1rmwFT7hF)

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
