---
sys: alpine
sys_ver: "3.20.0_alpha20231219 (edge)"
sys_var: null

status: basic
last_update: 2025-05-16
---

# Alpine Milk-V Mars Test Report

## Test Environment

### Operating System Information

- System Version: Alpine Linux 3.20.0_alpha20231219 (edge)
- Download Link: <https://dev.alpinelinux.org/~mps/riscv64/visionfive-v2-mmc.img.xz>
- Reference Installation Document:
  - <https://milkv.io/zh/docs/mars/getting-started/boot>
  - <https://arvanta.net/alpine/alpine-on-visionfive>

### Hardware Information

- Milk-V Mars (8GB RAM)
- A USB power adapter and A USB-A to C or C to C cable
- A microSD card
- A USB to UART debugger (e.g., CH340, CH341, FT2232, etc.)

## Installation Steps

### Decompress and Flash Image to microSD Card

Use `xz` to decompress the image,  and then use `dd` command or `balenaEtcher` software to flash the image to the microSD card. (Assuming `/dev/sdc` is the microSD card device)

```bash
wget https://dev.alpinelinux.org/~mps/riscv64/visionfive-v2-mmc.img.xz

xz -d visionfive-v2-mmc.img.xz

sudo dd if=visionfive-v2-mmc.img of=/dev/sdc bs=1M status=progress

sync
```

### Logging into the System

Log into the system via the serial port.

Default username: `root` (automatic login), without password.

## Expected Results

The system should boot up normally and allow login via the serial port.

## Actual Results

The system starts normally and the output is successfully viewed through the serial port.

### Boot Log

```log
Welcome to Alpine Linux 3.20.0_alpha20231219 (edge)
Kernel 6.7.4-0-starfive on an riscv64 (ttyS0)

[press ENTER to login]
localhost login: root (automatic login)

Welcome to Alpine!

The Alpine Wiki contains a large amount of how-to guides and general
information about administrating Alpine systems.
See <https://wiki.alpinelinux.org/>.

You can setup the system with the command: setup-alpine

You may change this message by editing /etc/motd.

localhost:~# cat /etc/os-release
NAME="Alpine Linux"
ID=alpine
VERSION_ID=3.20.0_alpha20231219
PRETTY_NAME="Alpine Linux edge"
HOME_URL="https://alpinelinux.org/"
BUG_REPORT_URL="https://gitlab.alpinelinux.org/alpine/aports/-/issues"

localhost:~# uname -a
Linux localhost 6.7.4-0-starfive #1-Alpine SMP PREEMPT_DYNAMIC Tue, 06 Feb 2024 12:21:03 +0000 riscv64 Linux

localhost:~# cat /proc/cpuinfo
processor       : 0
hart            : 1
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zba_zbb
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x4210427
hart isa        : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zba_zbb

processor       : 1
hart            : 2
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zba_zbb
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x4210427
hart isa        : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zba_zbb

processor       : 2
hart            : 3
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zba_zbb
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x4210427
hart isa        : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zba_zbb

processor       : 3
hart            : 4
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zba_zbb
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x4210427
hart isa        : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zba_zbb

localhost:~#
```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
