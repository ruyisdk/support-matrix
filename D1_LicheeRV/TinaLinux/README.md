---
sys: tina
sys_ver: 20210804
sys_var: null

status: basic
last_update: 2024-06-21
---

# Tina Linux LicheeRV Dock Test Report

## Test Environment

### Operating System Information

- System Version: D1-H Nezha HDMI Test Firmware 20210804
- Download Link: https://mega.nz/folder/lx4CyZBA#PiFhY7oSVQ3gp2ZZ_AnwYA
- Reference Installation Document: https://wiki.sipeed.com/hardware/en/lichee/RV/flash.html

### Hardware Information

- LicheeRV Dock 
- USB-A power adapter
- A USB-A to C cable
- A microSD card
- A USB to UART debugger (e.g., CH340, CH341, FT2232, etc.)
- Three Dupont wires

## Installation Steps

### Flashing Image to microSD Card

Use `dd` to flash the image to the microSD card.

```bash
sudo dd if=LicheeRV_Tina_hdmi_8723ds.img of=/dev/sdc status=progress 
```

### Logging into the System

Log into the system via the serial port.

## Expected Results

The system should boot normally and allow login via the onboard serial port.

## Actual Results

The system booted successfully and login via the onboard serial port was also successful.

### Boot Log

```log
BusyBox v1.27.2 () built-in shell (ash)                                                                               
                                                                                                                      
 _____  _              __     _                                                                                       
|_   _||_| ___  _ _   |  |   |_| ___  _ _  _ _                                                                        
  | |   _ |   ||   |  |  |__ | ||   || | ||_'_|                                                                       
  | |  | || | || _ |  |_____||_||_|_||___||_,_|                                                                       
  |_|  |_||_|_||_|_|  Tina is Based on OpenWrt!                                                                       
 ----------------------------------------------                                                                       
 Tina Linux (Neptune, 5C1C9C53)                                                                                       
 ----------------------------------------------                                                                       
root@TinaLinux:/# cat /proc/cpuinfo                                                                                   
processor       : 0                                                                                                   
hart            : 0                                                                                                   
isa             : rv64imafdcvu                                                                                        
mmu             : sv39                                                                                                
                                                                                                                      
root@TinaLinux:/# uname -a                                                                                            
Linux TinaLinux 5.4.61 #49 PREEMPT Wed Apr 28 09:23:43 UTC 2021 riscv64 GNU/Linux                                     
root@TinaLinux:/#
```

Screen recording (From flashing image to login):
[![asciicast](https://asciinema.org/a/WSlC5RUcJFYH6hZnjxZYwqPtk.svg)](https://asciinema.org/a/WSlC5RUcJFYH6hZnjxZYwqPtk)

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
