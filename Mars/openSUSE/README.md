---
sys: opensuse
sys_ver: "20250527"
sys_var: null

status: basic
last_update: 2025-05-29
---

# openKylin 2.0 SP1 Milk-V Mars Test Report

## Test Environment

### Operating System Information

- System Version: openSUSE Tumbleweed 20250527
- Download Link: <https://downloadcontent.opensuse.org/repositories/devel:/RISCV:/Factory:/Contrib:/StarFive:/VisionFive2/images/openSUSE-Tumbleweed-RISC-V-JeOS-starfivevisionfive2.riscv64-2025.04.28-Build1.26.raw.xz>
- Reference Installation Document:
  - <https://milkv.io/zh/docs/mars/getting-started/boot>
  - <https://en.opensuse.org/HCL:VisionFive2>

### Hardware Information

- Milk-V Mars (8GB RAM)
- A USB power adapter and A USB-A to C or C to C cable
- A microSD card
- A USB to UART debugger (e.g., CH340, CH341, FT2232, etc.)

## Installation Steps

### Decompress and Flash Image to microSD Card

Use `xz` to decompress the image,  and then use `dd` command or `balenaEtcher` software to flash the image to the microSD card. (Assuming `/dev/sdc` is the microSD card device)

```bash
xz -d openSUSE-Tumbleweed-RISC-V-JeOS-starfivevisionfive2.riscv64-2025.04.28-Build1.26.raw.xz

sudo dd if=openSUSE-Tumbleweed-RISC-V-JeOS-starfivevisionfive2.riscv64-2025.04.28-Build1.26.raw of=/dev/sdX bs=1M status=progress

sync
```

### Boot Mode Selection

Milk-V Mars provides multiple boot modes after the hardware version V1.2, which can be configured via onboard dip switches before powering on; the board itself is also silk-screened for reference.

To boot the openSUSE image, select the microSD card boot mode (`GPIO_0 = 1`, `GPIO_1 = 0`).

### Logging into the System

Log into the system via the serial port.

Default user: `root`

Default password: `linux`

## Expected Results

The system should boot up normally and allow login via the serial port.

## Actual Results

The system starts normally and the output is successfully viewed through the serial port.

### Boot Log

```log
Welcome to openSUSE Tumbleweed 20250527 - Kernel 6.15.0-112-default (ttyS0).

end0: 192.168.137.233 fe80::490c:948d:eb6e:60bf
wlP1p1s0:


localhost login: root
Password:
Have a lot of fun...
localhost:~ # uname -a
Linux localhost.localdomain 6.15.0-112-default #1 SMP PREEMPT_DYNAMIC Mon May 26 04:54:06 UTC 2025 (ed9faca) riscv64 riscv64 riscv64 GNU/Linux

localhost:~ # cat /etc/os-release
NAME="openSUSE Tumbleweed"
# VERSION="20250527"
ID="opensuse-tumbleweed"
ID_LIKE="opensuse suse"
VERSION_ID="20250527"
PRETTY_NAME="openSUSE Tumbleweed"
ANSI_COLOR="0;32"
# CPE 2.3 format, boo#1217921
CPE_NAME="cpe:2.3:o:opensuse:tumbleweed:20250527:*:*:*:*:*:*:*"
#CPE 2.2 format
#CPE_NAME="cpe:/o:opensuse:tumbleweed:20250527"
BUG_REPORT_URL="https://bugzilla.opensuse.org"
SUPPORT_URL="https://bugs.opensuse.org"
HOME_URL="https://www.opensuse.org"
DOCUMENTATION_URL="https://en.opensuse.org/Portal:Tumbleweed"
LOGO="distributor-logo-Tumbleweed"

localhost:~ # cat /proc/cpuinfo
processor       : 0
hart            : 1
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zaamo_zalrsc_zca_zcd_zba_zbb
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x4210427
hart isa        : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zaamo_zalrsc_zca_zcd_zba_zbb

processor       : 1
hart            : 2
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zaamo_zalrsc_zca_zcd_zba_zbb
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x4210427
hart isa        : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zaamo_zalrsc_zca_zcd_zba_zbb

processor       : 2
hart            : 3
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zaamo_zalrsc_zca_zcd_zba_zbb
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x4210427
hart isa        : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zaamo_zalrsc_zca_zcd_zba_zbb

processor       : 3
hart            : 4
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zaamo_zalrsc_zca_zcd_zba_zbb
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x4210427
hart isa        : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zaamo_zalrsc_zca_zcd_zba_zbb

localhost:~ #
```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
