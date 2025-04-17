---
sys: irradium
sys_ver: "3.7"
sys_var: core

status: basic
last_update: 2025-03-14
---

# Irradium LicheeRV Dock Test Report

## Test Environment

### Operating System Information

- Download link: https://dl.irradium.org/irradium/images/lichee_rv_dock/
- Reference Installation Document: https://dl.irradium.org/irradium/images/lichee_rv_dock/README.TXT

### Hardware Information

- Sipeed Lichee RV Dock
- A USB-A Power Adapter
- A USB-A to C Cable
- A microSD Card
- A USB to UART Debugger (e.g., CH340, CH341, FT2232, etc.)
- Three DuPont Wires

## Installation Steps

### Flashing Image to microSD Card

Use `dd` to flash the image to the microSD card.

```sh
zstd -d  irradium-3.7-riscv64-core-lichee_rv_dock-6.1.120-build-20241217.img.zst 
sudo dd if=irradium-3.7-riscv64-core-lichee_rv_dock-6.1.120-build-20241217.img of=/dev/<your-device> bs=1M status=progress 
```

### Logging into the System

Logging into the system via the serial port.

No passwd. On first login, the system will prompt you to change the password.

## Expected Results

The system should boot normally and allow login via the onboard serial port.

## Actual Results

The system booted successfully and login via the onboard serial port was also successful.

### Boot Log

```log

irradium  (lichee-rv-dock) (ttyS0)

lichee-rv-dock login: root
You are required to change your password immediately (administrator enforced).
New password: 
Retype new password: 
 _                   _  _             
|_| ___  ___  ___  _| ||_| _ _  _____ 
| ||  _||  _|| .'|| . || || | ||     |
|_||_|  |_|  |__,||___||_||___||_|_|_|
 _  _       _                              _            _   
| ||_| ___ | |_  ___  ___    ___  _ _    _| | ___  ___ | |_ 
| || ||  _||   || -_|| -_|  |  _|| | |  | . || . ||  _|| '_|
|_||_||___||_|_||___||___|  |_|   \_/   |___||___||___||_,_|

# uname -a
Linux lichee-rv-dock 6.1.120 #1 Sun Dec 15 23:35:12 EET 2024 riscv64 GNU/Linux
# cat /etc/os-release 
NAME=irradium
VERSION="3.7"
ID=irradium
PRETTY_NAME="irradium"
HOME_URL="https://irradium.org/"
BUG_REPORT_URL="https://irradium.org/bugs/"
# cat /proc/cpuinfo 
processor       : 0
hart            : 0
isa             : rv64imafdc
mmu             : sv39
uarch           : thead,c906
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

# 
```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
