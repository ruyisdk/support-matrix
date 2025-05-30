---
sys: irradium
sys_ver: "3.8"
sys_var: null

status: basic
last_update: 2025-05-30
---

# Armbian Milk-V Mars Test Report

## Test Environment

### Operating System Information

- System Version: irradium 3.8
- Download Link: <https://mirror.serverion.com/irradium/images/visionfive_2/irradium-3.8-riscv64-core-visionfive_2-6.12.28-build-20250512.img.zst>
- Reference Installation Document:
  - <https://milkv.io/zh/docs/mars/getting-started/boot>
  - <https://mirror.serverion.com/irradium/images/visionfive_2/README.TXT>

### Hardware Information

- Milk-V Mars (8GB RAM)
- A USB power adapter and A USB-A to C or C to C cable
- A microSD card
- A USB to UART debugger (e.g., CH340, CH341, FT2232, etc.)

## Installation Steps

### Decompress and Flash Image to microSD Card

Use `zstd` to decompress the image,  and then use `dd` command or `balenaEtcher` software to flash the image to the microSD card. (Assuming `/dev/sdc` is the microSD card device)

```bash
zstd -d irradium-3.8-riscv64-core-visionfive_2-6.12.28-build-20250512.img.zst

sudo dd if=irradium-3.8-riscv64-core-visionfive_2-6.12.28-build-20250512.img of=/dev/sdc bs=1M status=progress

sync
```

### Boot Mode Selection

Milk-V Mars provides multiple boot modes after the hardware version V1.2, which can be configured via onboard dip switches before powering on; the board itself is also silk-screened for reference.

To boot the irradium image, select the SPI Flash boot mode (`GPIO_0 = 0`, `GPIO_1 = 0`). Note that this mode may require you to update the firmware in the Flash beforehand.

### Logging into the System

Log into the system via the serial port.

Default username: `root` (automatic login)

Without password

## Expected Results

The system should boot up normally and allow login via the serial port.

## Actual Results

The system starts normally and the output is successfully viewed through the serial port.

### Boot Log

```log
irradium  (visionfive-2) (ttyS0)

visionfive-2 login: root
You are required to change your password immediately (administrator enforced).
New password:
Retype new password:
 _                   _  _
|_| ___  ___  ___  _| ||_| _ _  _____
| ||  _||  _|| .'|| . || || | ||     |
|_||_|  |_|  |__,||___||_||___||_|_|_|
      _       _            ___  _              ___
 _ _ |_| ___ |_| ___  ___ |  _||_| _ _  ___   |_  |
| | || ||_ -|| || . ||   ||  _|| || | || -_|  |  _|
 \_/ |_||___||_||___||_|_||_|  |_| \_/ |___|  |___|

# uname -a
Linux visionfive-2 6.12.28 #1 SMP PREEMPT Mon May 12 01:22:37 EEST 2025 riscv64 GNU/Linux

# cat /etc/os-release
NAME=irradium
VERSION="3.8"
ID=irradium
PRETTY_NAME="irradium"
HOME_URL="https://irradium.org/"
BUG_REPORT_URL="https://irradium.org/bugs/"

# cat /proc/cpuinfo
processor       : 0
hart            : 1
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd_zba_zbb
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x4210427
hart isa        : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd_zba_zbb

processor       : 1
hart            : 2
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
```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
