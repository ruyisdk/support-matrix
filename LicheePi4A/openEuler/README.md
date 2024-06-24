# openEuler RISC-V 23.09 LPi4A Test Report

## Test Environment

### System Information

- System Version: openEuler 23.09 RISC-V preview
- Download Link: https://mirror.iscas.ac.cn/openeuler-sig-riscv/openEuler-RISC-V/preview/openEuler-23.09-V1-riscv64/lpi4a/
- Reference Installation Document: https://mirror.iscas.ac.cn/openeuler-sig-riscv/openEuler-RISC-V/preview/openEuler-23.09-V1-riscv64/lpi4a/README.lpi4a.txt

### Hardware Information

- Lichee Pi 4A (16G RAM + 128G eMMC)
- USB-C Power Adapter / DC Power Supply
- A microSD card (Sandisk Extreme Pro 64G UHS-I)
- A USB-UART Debugger

## Installation Steps

### Using the `ruyi` CLI to Flash Image to Onboard eMMC

Install [`ruyi`](https://github.com/ruyisdk/ruyi) package manager, then run `ruyi device provision` and follow the prompts.

### Logging into the System

Logging into the system via serial console.

Default username: `openeuler` or `root`
Default password: `openEuler12#$`

## Expected Results

The system boots up successfully and allows login via the serial console.

If connected to a network, SSH login should be possible.

## Actual Results

The system boots up without issues, and both serial console and SSH login are successful.

### Boot Log

```log
System load:    1.47                                                                                                                                                         
Processes:      130                                                                                                                                                          
Memory used:    .6%                                                                                                                                                          
Swap used:      0.0%                                                                                                                                                         
Usage On:       2%                                                                                                                                                           
IP address:     10.0.0.8                                                                                                                                                     
Users online:   1                                                                                                                                                            
To execute a command as the administrator (user "root"), use "sudo <command>".                                                                                                         

[openeuler@openeuler-riscv64 ~]$ cat /etc/os-release                                                                                                                         
NAME="openEuler"                                                                                                                                                             
VERSION="23.09"                                                                                                                                                              
ID="openEuler"                                                                                                                                                               
VERSION_ID="23.09"                                                                                                                                                           
PRETTY_NAME="openEuler 23.09"                                                                                                                                                
ANSI_COLOR="0;31"                                                                                                                                                            
                                                                                                                                                                             
[openeuler@openeuler-riscv64 ~]$ uname -a                                                                                                                                    
Linux openeuler-riscv64 5.10.113 #1 SMP PREEMPT Wed Nov 22 16:04:58 UTC 2023 riscv64 riscv64 riscv64 GNU/Linux

[openeuler@openeuler-riscv64 ~]$ cat /proc/cpuinfo                                                                                                                           
processor       : 0                                                                                                                                                          
hart            : 0                                                                                                                                                          
isa             : rv64imafdcvsu                                                                                                                                              
mmu             : sv39                                                                                                                                                       
cpu-freq        : 1.848Ghz                                                                                                                                                   
cpu-icache      : 64KB                                                                                                                                                       
cpu-dcache      : 64KB                                                                                                                                                       
cpu-l2cache     : 1MB                                                                                                                                                        
cpu-tlb         : 1024 4-ways                                                                                                                                                
cpu-cacheline   : 64Bytes                                                                                                                                                    
cpu-vector      : 0.7.1                                                                                                                                                      

processor       : 1                                                                                                                                                          
hart            : 1                                                                                                                                                          
isa             : rv64imafdcvsu                                                                                                                                              
mmu             : sv39                                                                                                                                                       
cpu-freq        : 1.848Ghz                                                                                                                                                   
cpu-icache      : 64KB                                                                                                                                                       
cpu-dcache      : 64KB                                                                                                                                                       
cpu-l2cache     : 1MB                                                                                                                                                        
cpu-tlb         : 1024 4-ways                                                                                                                                                
cpu-cacheline   : 64Bytes                                                                                                                                                    
cpu-vector      : 0.7.1                                                                                                                                                      

processor       : 2                                                                                                                                                          
hart            : 2                                                                                                                                                          
isa             : rv64imafdcvsu                                                                                                                                              
mmu             : sv39                                                                                                                                                       
cpu-freq        : 1.848Ghz                                                                                                                                                   
cpu-icache      : 64KB                                                                                                                                                       
cpu-dcache      : 64KB                                                                                                                                                       
cpu-l2cache     : 1MB                                                                                                                                                        
cpu-tlb         : 1024 4-ways                                                                                                                                                
cpu-cacheline   : 64Bytes                                                                                                                                                    
cpu-vector      : 0.7.1                                                                                                                                                      

processor       : 3                                                                                                                                                          
hart            : 3                                                                                                                                                          
isa             : rv64imafdcvsu                                                                                                                                              
mmu             : sv39                                                                                                                                                       
cpu-freq        : 1.848Ghz                                                                                                                                                   
cpu-icache      : 64KB                                                                                                                                                       
cpu-dcache      : 64KB                                                                                                                                                       
cpu-l2cache     : 1MB                                                                                                                                                        
cpu-tlb         : 1024 4-ways                                                                                                                                                
cpu-cacheline   : 64Bytes                                                                                                                                                    
cpu-vector      : 0.7.1                                                                                                                                                      
```

Screen recording (from flashing image to logging into system):

[![asciicast](https://asciinema.org/a/oXGHqeiBmb0n5zIKHnbGnnRb2.svg)](https://asciinema.org/a/oXGHqeiBmb0n5zIKHnbGnnRb2)


## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
