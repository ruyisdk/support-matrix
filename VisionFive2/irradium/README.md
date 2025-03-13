---
sys: irradium
sys_ver: 3.7
sys_var: core

status: basic
last_update: 2025-03-06
---

# irradium VisionFive 2 Test Report

## Test Environment

### Operating System Information

- System Version: irradium 3.7 
- Download Link: https://dl.irradium.org/irradium/images/visionfive_2/
- Reference Installation Document: https://dl.irradium.org/irradium/images/visionfive_2/README.TXT

### Hardware Information

- StarFive VisionFive 2
- A USB power adapter
- A USB-A to C or C to C cable
- A microSD card
- A USB to UART debugger (e.g., CH340, CH341, FT2232, etc.)
- Three Dupont wires

## Installation Steps

### Decompress and Flash the Image to the microSD Card


```bash
zstd -d irradium-3.7-riscv64-core-visionfive_2-6.13.1-build-20250208.img.zst
sudo dd if=irradium-3.7-riscv64-core-visionfive_2-6.13.1-build-20250208.img of=/dev/<your-device> bs=1M status=progress
```

### Logging into the System

Logging into the system via the serial port.

Username: `root`
No password.

## Expected Results

The system should boot normally and allow login via the serial port.

## Actual Results

The system booted successfully and login via the serial port was successful.

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

# 
# uname -a
Linux visionfive-2 6.13.1 #4 SMP PREEMPT Sat Feb  8 00:21:02 EET 2025 riscv64 GNU/Linux
# cat /etc/os-release 
NAME=irradium
VERSION="3.7"
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

# 
```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
