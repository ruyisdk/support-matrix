# openEuler RISC-V 23.03 D1 Version Test Report

## Test Environment

### Operating System Information

- System Version: openEuler 23.03 RISC-V preview
- Download Link: [Download Link](https://mirror.iscas.ac.cn/openeuler-sig-riscv/openEuler-RISC-V/preview/openEuler-23.03-V1-riscv64/D1/)
- Reference Installation Document: [Installation Document](https://gitee.com/openeuler/RISC-V/tree/master/release/openEuler-23.03/Installation_Book/D1_and_Licheerv)

### Hardware Information

- AWOL Nezha D1 / Sipeed Lichee RV Dock
- A USB-A power adapter
- A USB-A to C cable
- A microSD card
- A USB to UART debugger (e.g., CH340, CH341, FT2232, etc.)
- Three Dupont wires

## Installation Steps

### Using `ruyi` CLI to Flash the Image to the microSD Card

Install the [`ruyi`](https://github.com/ruyisdk/ruyi) package manager and run `ruyi device provision`, following the prompts.

### Logging into the System

Logging to the system via the serial port.

Default username: `openeuler` or `root`
Default password: `openEuler12#$`

## Expected Results

The system should boot normally and allow login via the onboard serial port.

## Actual Results

The system booted successfully and login via the onboard serial port was also successful.

### Boot Log

```log
openEuler 23.03                                                                                                                                   
Kernel 6.1.0-0.rv64                                                                                                                               
                                                                                                                                                  
openeuler-riscv64 login: c3.11.oe2303.riscv64 on an riscv64                                                                                       
                                                                                                                                                  
openeuler-riscv64 login: root                                                                                                                     
Password: [   57.563173] EXT4-fs (mmcblk0p4): resized filesystem to 15498496                                                                      
                                                                                                                                                  
                                                                                                                                                  
                                                                                                                                                  
Welcome to 6.1.0-0.rc3.11.oe2303.riscv64                                                                                                          
                                                                                                                                                  
System information as of time:  Fri Jan  2 08:01:41 CST 1970                                                                                      
                                                                                                                                                  
System load:    3.42                                                                                                                              
Processes:      93                                                                                                                                
Memory used:    6.8%                                                                                                                              
Swap used:      0.0%                                                                                                                              
Usage On:       2%                                                                                                                                
Users online:   1                                                                                                                                 
                                                                                                                                                  
                                                                                                                                                  
[root@openeuler-riscv64 ~]# cat /proc/cpuinfo                                                                                                     
processor       : 0                                                                                                                               
hart            : 0                                                                                                                               
isa             : rv64imafdc                                                                                                                      
mmu             : sv39                                                                                                                            
uarch           : thead,c906                                                                                                                      
mvendorid       : 0x5b7                                                                                                                           
marchid         : 0x0                                                                                                                             
mimpid          : 0x0                                                                                                                             
                                                                                                                                                  
[root@openeuler-riscv64 ~]#
```

Screen recording (From flashing image to login):

[![asciicast](https://asciinema.org/a/dJV431qjqOPT6iR7hzieM3G41.svg)](https://asciinema.org/a/dJV431qjqOPT6iR7hzieM3G41)

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
