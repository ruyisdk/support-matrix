---
sys: tina
sys_ver: 20210804
sys_var: null

status: basic
last_update: 2024-12-06
---

# Tina Linux LicheePi RV Dock Test Report

## Test Environment

### Operating System Information

- System Version: LicheeRV_Tina_hdmi_8723ds
- Download Link: https://mega.nz/folder/lx4CyZBA#PiFhY7oSVQ3gp2ZZ_AnwYA
- Reference Installation Document: https://wiki.sipeed.com/hardware/en/lichee/RV/flash.html

### Hardware Information

- LicheePi RV Dock
- USB-A power adapter
- A USB-A to C cable
- A microSD card
- A USB to UART debugger (e.g., CH340, CH341, FT2232, etc.)
- Three Dupont wires

## Installation Steps

### Flashing Image to microSD Card

1. Run [PhoenixCard](https://dl.sipeed.com/shareURL/LICHEE/D1/Lichee_RV/tool),Click Image marked to choose your target firmware
2. We choose `Startup` marked
3. Click `Burn` marked to burn your target firmware into tf card
4. From Status bar marked to see your progress;If it's red when finishing this means it fails burning, then we should rerun `SD Card Formatter` to format the TF card to increase its success possibility.

### Logging into the System

Log into the system via the serial port.

## Expected Results

The system should boot normally and allow login via the onboard serial port.

## Actual Results

The system booted successfully and login via the onboard serial port was also successful.

### Boot Log

```log
Please press Enter to activate this console.



BusyBox v1.27.2 () built-in shell (ash)

    __  ___     _        __   _               
   /  |/  /__ _(_)_ __  / /  (_)__  __ ____ __
  / /|_/ / _ `/ /\ \ / / /__/ / _ \/ // /\ \ /
 /_/  /_/\_,_/_//_\_\ /____/_/_//_/\_,_//_\_\ 
 ----------------------------------------------
 Maix Linux (Neptune, 5C1C9C53)
 ----------------------------------------------
Trying to connect to SWUpdate...
root@MaixLinux:/# uname -a
Linux MaixLinux 5.4.61 #189 PREEMPT Thu Dec 23 07:30:37 UTC 2021 riscv64 GNU/Linux
root@MaixLinux:/# cat /proc/cpuinfo 
processor       : 0
hart            : 0
isa             : rv64imafdcvu
mmu             : sv39

root@MaixLinux:/# 
```


## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
