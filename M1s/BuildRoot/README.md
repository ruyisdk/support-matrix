# BuildRoot Sipeed M1s Dock Test Report

## Test Environment

### Operating System Information

- System Version: 20240401
- Download Link: https://github.com/sipeed/LicheeRV-Nano-Build/releases
    - Precompiled Image: https://dl.sipeed.com/fileList/MAIX/M1s/M1s_Dock/7_Firmware/m1sdock_linux_20221116.zip
- Reference Installation Document: https://github.com/sipeed/LicheeRV-Nano-Build/releases

### Hardware Information

- Sipeed M1s Dock
- A Type-C cable

## Installation Steps

### Get the Image

Download and extract the precompiled image:
```bash
wget https://dl.sipeed.com/fileList/MAIX/M1s/M1s_Dock/7_Firmware/m1sdock_linux_20221116.zip
unzip m1sdock_linux_20221116.zip

```

### Flashing the Program via Serial Port

Connect the computer and the **UART-labeled** C port using the Type-C cable.

Download the flashing tool and use the appropriate version for your system to flash the firmware.

After powering on, press and hold the boot button, then press the reset button, and finally release the boot button.

Enter the MCU page, and flash m0 and d0 (files named low_load_bl808_m0/d0@0x58000000.bin) at address 0x58000000, with group set to group0. Ensure to select the high serial port!

![mcu](./mcu.png)

Next, enter the IOT page, check the Single Download Options box, fill in the start address with the address in the filename, and flash the whole_img file.

![iot](./iot.png)

### Connecting via Serial Port

Connect the Type-C cable to the **UART-labeled** C port.

## Expected Results

The system should start normally with serial output.

## Actual Results

The system started successfully, with serial output.

### Boot Information

```log
--------Start Local Services--------
********************************
********************************

Linux login: root
login[40]: root login on 'ttyS0'
Processing /etc/profile ... 
Set search library path in /etc/profile
Set user path in /etc/profile
id: unknown ID 0
Welcome to Linux
[@Linux root]#uname -a
Linux Linux 5.10.4 #4 SMP Fri Nov 4 18:23:30 CST 2022 riscv64 GNU/Linux
[@Linux root]#cat /proc/cpuinfo 
processor       : 0
hart            : 0
isa             : rv64imafdcvsu
mmu             : sv39
model name      : T-HEAD C910
freq            : 1.2GHz
icache          : 64kB
dcache          : 64kB
l2cache         : 2MB
tlb             : 1024 4-ways
cache line      : 64Bytes
address sizes   : 40 bits physical, 39 bits virtual
vector version  : 0.7.1

[@Linux root]#

```

Screen recording (entering the system):

[![asciicast](https://asciinema.org/a/R5eNAV87OGvoJfoNcpVCtMKRO.svg)](https://asciinema.org/a/R5eNAV87OGvoJfoNcpVCtMKRO)

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.

