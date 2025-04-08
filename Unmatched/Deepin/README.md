---
sys: deepin
sys_ver: null
sys_var: null

status: good
last_update: 2025-04-05
---

# Deepin HiFive Unmatched Report

## Test Environment

### System Information

- System Version: Deepin (2022.11.11, EOL)
- Download Link: https://cdimage.deepin.com/RISC-V/Unmatched-image/deepin-sifive.7z
- Reference Installation Document: https://cdimage.deepin.com/RISC-V/Unmatched-image/README.txt

> [!Warning]
> Deepin for the HiFive Unmatched is now EOL. This image is from 20221111 and is not recommended for production due to possible security vulnerabilites.
>

### Hardware Information

- HiFive Unmatched Rev A
- A microUSB cable (included with HiFive Unmatched)
- An ATX power supply
- NVMe SSD

## Installation Steps

### Flashing Image

**The image is NOT for SD card, a NVMe SSD is needed!**

Use `7z` to decompress the image.
Use `dd` to write the image to the microSD card.

```bash
7z e deepin-sifive.7z
sudo dd if=deepin-sifive.img of=/dev/your/device bs=1M status=progress
```

### Logging into the System

Logging into the system via the serial port or via GUI.

Default Username: `root`
Default Password: `Riscv2022#`

Default Username: `deepin`
Default Password: `deepin#`

## Expected Results

The system should boot up normally and allow login through the onboard serial port or through the GUI

## Actual Results

The system should boot up normally and login both through the onboard serial port and through the GUI is successful.

### Boot Log

```log
Verification successful
Linux deepin-riscv 6.0.0-4-riscv64 #1 SMP Debian 6.0.8-1 (2022-11-11) riscv64
Welcome to Deepin 23 GNU/Linux

    * Homepage:https://www.deepin.org/

    * Bugreport:https://bbs.deepin.org/


Last login: Fri Jan 24 19:09:43 2025
deepin@deepin-riscv:~$ cat /etc/os-release
PRETTY_NAME="Deepin 23"
NAME="Deepin"
VERSION_ID="23"
VERSION="23"
ID=Deepin
HOME_URL="https://www.deepin.org/"
BUG_REPORT_URL="https://bbs.deepin.org"
VERSION_CODENAME=beige
deepin@deepin-riscv:~$ cat /proc/cpuinfo
processor       : 0
hart            : 1
isa             : rv64imafdc
mmu             : sv39
uarch           : sifive,bullet0

processor       : 1
hart            : 2
isa             : rv64imafdc
mmu             : sv39
uarch           : sifive,bullet0

processor       : 2
hart            : 3
isa             : rv64imafdc
mmu             : sv39
uarch           : sifive,bullet0

processor       : 3
hart            : 4
isa             : rv64imafdc
mmu             : sv39
uarch           : sifive,bullet0

deepin@deepin-riscv:~$ uname -a
Linux deepin-riscv 6.0.0-4-riscv64 #1 SMP Debian 6.0.8-1 (2022-11-11) riscv64 GNU/Linux
deepin@deepin-riscv:~$
```

![](image/2025-01-25-03-15-31.png)

![](image/2025-01-25-03-14-53.png)

See https://github.com/QA-Team-lo/oscompare/blob/main/Deepin/Unmatched/README.md for our report on its desktop experience.

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.