# openKylin 1.0 HiFive Unmatched Test Report

## Test Environment

### Operating System Information

- System Version: openKylin 1.0
- Download Link: https://www.openkylin.top/downloads
- Reference Installation Document: https://docs.openkylin.top/zh/%E7%A4%BE%E5%8C%BA%E5%BC%80%E5%8F%91%E6%8C%87%E5%8D%97/riscv%E4%B8%8A%E5%AE%89%E8%A3%85openKylin

### Hardware Information

- HiFive Unmatched Rev A
- A microUSB cable (included with HiFive Unmatched)
- An ATX power supply
- A microSD card (Sandisk Extreme Pro 64G UHS-I)

## Installation Steps

### Boot Device Selection

Ensure the DIP switch is set to boot from the microSD card. If not changed, the factory default is boot from microSD.

The DIP switch should be set as follows: `MSEL[3:0]=1011`

### Use `ruyi` CLI to Flash the Image to the microSD Card

Install the [`ruyi`](https://github.com/ruyisdk/ruyi) package manager, run `ruyi device provision` and follow the prompts.

### Logging into the System

Logging into the system via the onboard serial port (connect using a microUSB cable to another computer) or graphical interface.

Default username: `openkylin`
Default password: `openkylin`

## Expected Results

The system should boot normally and allow login via the onboard serial port or graphical interface.

## Actual Results

The system booted successfully and login via the onboard serial port was successful.

### Boot Log

```log
Welcome to openKylin 1.0 (GNU/Linux 5.11.0-1030-generic riscv64)                                                      
                                                                                                                      
 * Support:        https://openkylin.top                                                                              
                                                                                                                      
The programs included with the openKylin system are free software;                                                    
the exact distribution terms for each program are described in the                                                    
individual files in /usr/share/doc/*/copyright.                                                                       
                                                                                                                      
openKylin comes with ABSOLUTELY NO WARRANTY, to the extent permitted by                                               
applicable law.                                                                                                       
                                                                                                                      
To run a command as administrator (user "root"), use "sudo <command>".                                                
See "man sudo_root" for details.                                                                                      
                                                                                                                      
openkylin@openkylin:~$                                                                                                
openkylin@openkylin:~$ cat /etc/os-release                                                                            
NAME="openKylin"                                                                                                      
FULL_NAME="openKylin"                                                                                                 
VERSION="1.0 (yangtze)"                                                                                               
VERSION_US="1.0 (yangtze)"                                                                                            
ID=openkylin                                                                                                          
PRETTY_NAME="openKylin 1.0"                                                                                           
VERSION_ID="1.0"                                                                                                      
HOME_URL="https://www.openkylin.top/"                                                                                 
VERSION_CODENAME=yangtze                                                                                              
PRODUCT_FEATURES=3                                                                                                    
openkylin@openkylin:~$ cat /proc/cpuinfo                                                                              
processor       : 0                                                                                                   
hart            : 4                                                                                                   
isa             : rv64imafdc                                                                                          
mmu             : sv39                                                                                                
uarch           : sifive,u74-mc                                                                                       
                                                                                                                      
processor       : 1                                                                                                   
hart            : 1                                                                                                   
isa             : rv64imafdc                                                                                          
mmu             : sv39                                                                                                
uarch           : sifive,u74-mc                                                                                       
                                                                                                                      
processor       : 2                                                                                                   
hart            : 2                                                                                                   
isa             : rv64imafdc                                                                                          
mmu             : sv39                                                                                                
uarch           : sifive,u74-mc                                                                                       
                                                                                                                      
processor       : 3                                                                                                   
hart            : 3                                                                                                   
isa             : rv64imafdc                                                                                          
mmu             : sv39                                                                                                
uarch           : sifive,u74-mc                                                                                       
                                                                                                                      
openkylin@openkylin:~$ 
```

Screen recording (From flashing image to logging):

[![asciicast](https://asciinema.org/a/Wgz7wgCph6BhEQpEskH4LDMd4.svg)](https://asciinema.org/a/Wgz7wgCph6BhEQpEskH4LDMd4)

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
