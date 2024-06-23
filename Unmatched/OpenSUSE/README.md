# openSUSE Tumbleweed HiFive Unmatched Test Report

## Test Environment

### Operating System Information

- System Version: openSUSE Tumbleweed
- Download Link: <https://download.opensuse.org/repositories/home:/Andreas_Schwab:/riscv:/unmatched/images/openSUSE-Tumbleweed-RISC-V-JeOS-hifiveunmatched.riscv64-2024.03.15-Build1.7.raw.xz>
- Reference Installation Document: <https://en.opensuse.org/HCL:HiFive_Unmatched>

### Hardware Information

- HiFive Unmatched Rev A
- A microUSB cable (included with HiFive Unmatched)
- An ATX power supply
- A microSD card (SanDisk Extreme Pro 64G UHS-I)

## Installation Steps

### Boot Device Selection

Ensure the dip switches are set to boot from the microSD card. If unchanged, the factory default is to boot from the microSD card.

The dip switches should be set as follows: `MSEL[3:0]=1011`

### Unzip and Flash Image to microSD Card

`/dev/sdc` is the location of the microSD card; please adjust according to your circumstances.

```bash
xzcat openSUSE-Tumbleweed-RISC-V-JeOS-hifiveunmatched.riscv64-2024.03.15-Build1.7.raw.xz | sudo dd bs=4M of=/dev/sdc iflag=fullblock status=progress
```

### Logging into the System

Log into the system via the onboard serial port (connect using a microUSB cable to another computer).

Default Username: `root`
Default Password: `linux`

## Expected Results

The system should boot normally and allow login via the onboard serial port.

## Actual Results

The system booted successfully, and login via the onboard serial port was also successful.

### Boot Log

```log
Welcome to openSUSE Tumbleweed 20240320 - Kernel 6.8.1-1-default (ttySIF0).                                                         
                                                                                                                                    
end0:                                                                                                                               
                                                                                                                                    
                                                                                                                                    
localhost login: root                                                                                                               
Password:                                                                                                                           
Have a lot of fun...                                                                                                                
stty: 'standard input': unable to perform all requested operations                                                                  
localhost:~ # cat /etc/os-release                                                                                                   
NAME="openSUSE Tumbleweed"                                                                                                          
# VERSION="20240320"                                                                                                                
ID="opensuse-tumbleweed"                                                                                                            
ID_LIKE="opensuse suse"                                                                                                             
VERSION_ID="20240320"                                                                                                               
PRETTY_NAME="openSUSE Tumbleweed"                                                                                                   
ANSI_COLOR="0;32"                                                                                                                   
# CPE 2.3 format, boo#1217921                                                                                                       
CPE_NAME="cpe:2.3:o:opensuse:tumbleweed:20240320:*:*:*:*:*:*:*"                                                                     
#CPE 2.2 format                                                                                                                     
#CPE_NAME="cpe:/o:opensuse:tumbleweed:20240320"                                                                                     
BUG_REPORT_URL="https://bugzilla.opensuse.org"                                                                                      
SUPPORT_URL="https://bugs.opensuse.org"                                                                                             
HOME_URL="https://www.opensuse.org"                                                                                                 
DOCUMENTATION_URL="https://en.opensuse.org/Portal:Tumbleweed"                                                                       
LOGO="distributor-logo-Tumbleweed"
localhost:~ # uname -a                                                                                                              
Linux localhost.localdomain 6.8.1-1-default #1 SMP PREEMPT_DYNAMIC Tue Mar 19 07:32:20 UTC 2024 (d922afa) riscv64 riscv64 riscv64 Gx
localhost:~ # 
```

Screen recording (from flashing the image to logging)

[![asciicast](https://asciinema.org/a/Yq2qb4xYNEMzUBxIcUkdyI2pp.svg)](https://asciinema.org/a/Yq2qb4xYNEMzUBxIcUkdyI2pp)

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
