---
sys: archlinux
sys_ver: null
sys_var: null

status: basic
last_update: 2025-05-10
---

# ArchLinux Milk-V Mars Test Report

## Test Environment

### Hardware Information

- Development Board: Milk-V Mars (8GB RAM)
- Other Hardware:
  - A USB power adapter and A USB-A to C or C to C cable
  - A microSD card
  - A USB to UART debugger (e.g., CH340, CH341, FT2232, etc.)

### Operating System Information

- OS Version: ArchLinux (VF2_6.12_v5.14.0-cwt24)
- Download Link: <https://github.com/cwt-vf2/archlinux-image-vf2/releases/download/cwt24/ArchLinux-VF2_6.12_v5.14.0-cwt24.img.zst>
- Reference Installation Document:
  - <https://forum.rvspace.org/t/arch-linux-image-for-visionfive-2/1459>
  - <https://milkv.io/zh/docs/mars/getting-started/boot>
  - <https://doc.rvspace.org/VisionFive2/Application_Notes/VisionFive2_OpenWrt/VisionFive_2/openwrt/compile.html>

## Installation Steps

### Flashing the Image

Use `zstd` command to decompress the image,  and then use `dd` command or `balenaEtcher` software to flash the image to the microSD card.

Here, `/dev/sdc` corresponds to the storage device.

```bash
wget https://github.com/cwt-vf2/archlinux-image-vf2/releases/download/cwt24/ArchLinux-VF2_6.12_v5.14.0-cwt24.img.zst

zstd -d ArchLinux-VF2_6.12_v5.14.0-cwt24.img.zst

sudo dd if=ArchLinux-VF2_6.12_v5.14.0-cwt24.img of=/dev/sdX bs=1M status=progress

sync
```

### Logging into the System

Logging into the system via the serial port.

Default username: `root`

Default password: `archriscv`

or

Username: `user`

Password: `user`

## Expected Results

The system should boot normally, allowing login via the onboard serial port.

## Actual Results

The system starts normally and the output is successfully viewed through the serial port.

### Boot Information

```log
Arch Linux 6.12.18-cwt-5.14.0-2 (ttyS0)

ArchVF2 login: root
Password:
[root@ArchVF2 ~]#

[root@ArchVF2 ~]# uname -a
Linux ArchVF2 6.12.18-cwt-5.14.0-2 #1 SMP PREEMPT_DYNAMIC Tue Apr  8 17:15:39 +07 2025 riscv64 GNU/Linux

[root@ArchVF2 ~]# cat /etc/os-release
NAME="Arch Linux"
PRETTY_NAME="Arch Linux"
ID=arch
BUILD_ID=rolling
ANSI_COLOR="38;2;23;147;209"
HOME_URL="https://archlinux.org/"
DOCUMENTATION_URL="https://wiki.archlinux.org/"
SUPPORT_URL="https://bbs.archlinux.org/"
BUG_REPORT_URL="https://gitlab.archlinux.org/groups/archlinux/-/issues"
PRIVACY_POLICY_URL="https://terms.archlinux.org/docs/privacy-policy/"
LOGO=archlinux-logo

[root@ArchVF2 ~]# cat /proc/cpuinfo
processor       : 0
hart            : 2
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd_zba_zbb
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x4210427
hart isa        : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd_zba_zbb

processor       : 1
hart            : 1
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

[root@ArchVF2 ~]#
```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
