# Fedora 38 HiFive Unmatched Test Report

## Test Environment

### Operating System Information

- System Version: Fedora 38
- Download Link: https://dl.fedoraproject.org/pub/alt/risc-v/disk_images/Fedora-Developer-38-20230519.n.0.SiFive.Unmatched.and.QEMU/Fedora-Developer-38-20230519.n.0-mmc.raw.img.xz
- Reference Installation Document: https://dl.fedoraproject.org/pub/alt/risc-v/disk_images/Fedora-Developer-38-20230519.n.0.SiFive.Unmatched.and.QEMU/README.md

### Hardware Information

- HiFive Unmatched Rev A
- A microUSB cable (included with HiFive Unmatched)
- An ATX power supply
- A microSD card (Sandisk Extreme Pro 64G UHS-I)

## Installation Steps

### Boot Device Selection

Ensure that the dip switch is set to boot from the microSD card. The default factory setting is to boot from the microSD card.

The dip switch should be set as follows: `MSEL[3:0]=1011`

### Extract and Flash the Image to the microSD Card

`/dev/sdc` represents the microSD card location. Please adjust as necessary.

```bash
sudo wipefs -af /dev/sdc
xzcat Fedora-Developer-38-20230519.n.0-mmc.raw.img.xz | sudo dd of=/dev/sdc iflag=fullblock bs=4M status=progress
```

### Logging into the System

Log into the system via the onboard serial port using a microUSB cable connected to another computer.

Default username: `riscv` or `root`
Default password: `fedora_rocks!`

## Expected Results

The system should boot normally and allow login via the onboard serial port.

## Actual Results

The system booted successfully and login via the onboard serial port was also successful.

### Boot Log

```log
https://fedoraproject.org/wiki/Architectures/RISC-V                                                                                 
                                                                                                                                    
Build date: Fri May 19 12:44:23 UTC 2023                                                                                            
                                                                                                                                    
Kernel 6.2.16-300.0.riscv64.fc38.riscv64 on an riscv64 (ttySIF0)                                                                    
                                                                                                                                    
The root password is 'fedora_rocks!'.                                                                                               
root password logins are disabled in SSH starting Fedora 31.                                                                        
User 'riscv' with password 'fedora_rocks!' in 'wheel' group is provided.                                                            
                                                                                                                                    
To install new packages use 'dnf install ...'                                                                                       
                                                                                                                                    
To upgrade disk image use 'dnf upgrade --best'                                                                                      
                                                                                                                                    
If DNS isn’t working, try editing ‘/etc/yum.repos.d/fedora-riscv.repo’.                                                             
                                                                                                                                    
For updates and latest information read:                                                                                            
https://fedoraproject.org/wiki/Architectures/RISC-V                                                                                 
                                                                                                                                    
Fedora/RISC-V                                                                                                                       
-------------                                                                                                                       
Koji:               http://fedora.riscv.rocks/koji/                                                                                 
SCM:                http://fedora.riscv.rocks:3000/                                                                                 
Distribution rep.:  http://fedora.riscv.rocks/repos-dist/                                                                           
Koji internal rep.: http://fedora.riscv.rocks/repos/                                                                                
fedora-riscv login: root                                                                                                            
Password:                                                                                                                           
Login incorrect                                                                                                                     
                                                                                                                                    
fedora-riscv login: root                                                                                                            
Password:                                                                                                                           
Login incorrect 

fedora-riscv login: root                                                                                                            
Password:                                                                                                                           
Last failed login: Wed May 10 20:04:31 EDT 2023 on ttySIF0                                                                          
There were 2 failed login attempts since the last successful login.                                                                 
[root@fedora-riscv ~]# cat /etc/os-release                                                                                          
NAME="Fedora Linux"                                                                                                                 
VERSION="38 (Thirty Eight)"                                                                                                         
ID=fedora                                                                                                                           
VERSION_ID=38                                                                                                                       
VERSION_CODENAME=""                                                                                                                 
PLATFORM_ID="platform:f38"                                                                                                          
PRETTY_NAME="Fedora Linux 38 (Thirty Eight)"                                                                                        
ANSI_COLOR="0;38;2;60;110;180"                                                                                                      
LOGO=fedora-logo-icon                                                                                                               
CPE_NAME="cpe:/o:fedoraproject:fedora:38"                                                                                           
DEFAULT_HOSTNAME="fedora"                                                                                                           
HOME_URL="https://fedoraproject.org/"                                                                                               
DOCUMENTATION_URL="https://docs.fedoraproject.org/en-US/fedora/f38/system-administrators-guide/"                                    
SUPPORT_URL="https://ask.fedoraproject.org/"                                                                                        
BUG_REPORT_URL="https://bugzilla.redhat.com/"                                                                                       
REDHAT_BUGZILLA_PRODUCT="Fedora"                                                                                                    
REDHAT_BUGZILLA_PRODUCT_VERSION=38                                                                                                  
REDHAT_SUPPORT_PRODUCT="Fedora"                                                                                                     
REDHAT_SUPPORT_PRODUCT_VERSION=38                                                                                                   
SUPPORT_END=2024-05-14                                                                                                              
[root@fedora-riscv ~]#
```

Screen recording (From flashing image to login)

[![asciicast](https://asciinema.org/a/vulbDuQBEkAx4ldcquyMpVR2m.svg)](https://asciinema.org/a/vulbDuQBEkAx4ldcquyMpVR2m)

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
