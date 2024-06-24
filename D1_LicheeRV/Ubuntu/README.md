# Ubuntu 24.04 D1 Test Report

## Test Environment

### Operating System Information

- System Version: Ubuntu 24.04
- Download Link: https://ubuntu.com/download/risc-v
    - Or from mirror sites: [Nezha](https://mirror.tuna.tsinghua.edu.cn/ubuntu-cdimage/releases/mantic/release/ubuntu-23.10-preinstalled-server-riscv64+nezha.img.xz) | [Lichee RV](https://mirror.tuna.tsinghua.edu.cn/ubuntu-cdimage/releases/mantic/release/ubuntu-23.10-preinstalled-server-riscv64+licheerv.img.xz)
- Reference Installation Document: https://wiki.ubuntu.com/RISC-V/LicheeRV

### Hardware Information

- AWOL Nezha D1 / Sipeed Lichee RV Dock
- A USB-A Power Adapter
- A USB-A to C Cable
- A microSD Card
- A USB to UART Debugger (e.g., CH340, CH341, FT2232, etc.)
- Three DuPont Wires

## Installation Steps

### Flashing Image to microSD Card

Use `dd` to flash the image to the microSD card.

### Logging into the System

Logging into the system via the serial port.

Default Username: `ubuntu`
Default Password: `ubuntu`

On first login, the system will prompt you to change the password.

## Expected Results

The system should boot normally and allow login via the onboard serial port.

## Actual Results

The system booted successfully and login via the onboard serial port was also successful.

### Boot Log

```log
ubuntu@ubuntu:~$ cat /proc/cpuinfo
processor       : 0
hart            : 0
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm
mmu             : sv39
uarch           : thead,c906
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0
hart isa        : rv64imafdc_zicntr_zicsr_zifencei_zihpm
```

Screen recording (from flashing the image to logging into the system):

[![asciicast](https://asciinema.org/a/zwX03rXaG8pP6mQMDYuSzb0Eb.svg)](https://asciinema.org/a/zwX03rXaG8pP6mQMDYuSzb0Eb)

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
