# BuildRoot Milk-V Duo S Test Report

## Test Environment

### Operating System Information

- System Version: Duo-V1.1.0
- Download Link: https://github.com/milkv-duo/duo-buildroot-sdk/releases
- Reference Installation Document: https://github.com/milkv-duo/duo-buildroot-sdk

### Hardware Information

- Milk-V Duo S (512M, SG2000)
- A USB Power Adapter
- A USB-A to C or USB C to C Cable for powering the development board
- A microSD Card
- A USB Card Reader
- A USB to UART Debugger (e.g., CP2102, FT2232, etc. Be aware that WCH CH340/341 series will cause garbled text output, DO NOT USE)

## Installation Steps

### Using `ruyi` CLI to Flash Image to microSD Card

Install the [`ruyi`](https://github.com/ruyisdk/ruyi) package manager, run `ruyi device provision`, and follow the prompts.

### Logging into the System

Log into the system via the serial port.

## Expected Results

The system should boot normally and allow login via the onboard serial port.

## Actual Results

The system booted successfully and login via the onboard serial port was also successful.

### Boot Information

> The aic8800 insmod failure occurred because the Duo S used in the test does not have a Wi-Fi chip.
> 
> This is normal.

```log
Starting app...                                                                                                                     
                                                                                                                                    
[root@milkv-duo]~# insmod: can't insert '/mnt/system/ko/aic8800_fdrv.ko': No such device                                            
                                                                                                                                    
[root@milkv-duo]~#                                                                                                                  
[root@milkv-duo]~# uname -a                                                                                                         
Linux milkv-duo 5.10.4-tag- #1 PREEMPT Mon Feb 26 16:01:35 CST 2024 riscv64 GNU/Linux                                               
[root@milkv-duo]~# cat /proc/cpuinfo                                                                                                
processor       : 0                                                                                                                 
hart            : 0                                                                                                                 
isa             : rv64imafdvcsu                                                                                                     
mmu             : sv39                                                                                                              
                                                                                                                                    
[root@milkv-duo]~# cat /etc/os-release                                                                                              
NAME=Buildroot                                                                                                                      
VERSION=20240226-1609                                                                                                               
ID=buildroot                                                                                                                        
VERSION_ID=2021.05                                                                                                                  
PRETTY_NAME="Buildroot 2021.05"                                                                                                     
[root@milkv-duo]~# 
```

Screen recording (From flashing image to login):

[![asciicast](https://asciinema.org/a/Zbt8azPsJFYLWOYCKgPNrt9S7.svg)](https://asciinema.org/a/Zbt8azPsJFYLWOYCKgPNrt9S7)

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
