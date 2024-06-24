# openSUSE Tumbleweed VisionFive 2 Test Report

## Test Environment

### Operating System Information

- System Version: openSUSE-Tumbleweed-RISC-V-JeOS-starfivevisionfive2.riscv64-2024.03.15-Build23.14.raw.xz
- Download Link: https://download.opensuse.org/repositories/devel:/RISCV:/Factory:/Contrib:/StarFive:/VisionFive2/images/
- Reference Installation Document: https://en.opensuse.org/HCL:VisionFive2

### Hardware Information

- StarFive VisionFive 2
- A USB Power Adapter
- A USB-A to C or C to C Cable
- A microSD Card
- A USB to UART Debugger (e.g., CH340, CH341, FT2232, etc.)
- Three Dupont Wires

## Installation Steps

### Decompress and Flash the Image to the microSD Card

Assuming `/dev/sdc` is the storage card.

```bash
xzcat openSUSE-Tumbleweed-RISC-V-JeOS-starfivevisionfive2.riscv64-2024.03.15-Build23.14.raw.xz | sudo dd of=/dev/sdc iflag=fullblock status=progress bs=4M
```

### Boot Mode Selection

StarFive VisionFive 2 provides multiple boot modes, configurable through onboard dip switches before powering on; these are marked on the board itself.

To boot the openSUSE image, select the microSD card boot mode (i.e., `RGPIO_0 = 1`, `RGPIO_1 = 0`).

> Note: In this mode, there is a small chance of boot failure. If you encounter boot failure, you might see output similar to the following on the serial port:
>
>```log
>dwmci_s: Response Timeout.                                                                                            
>dwmci_s: Response Timeout.                                                                                            
>BOOT fail,Error is 0xffffffff
>```
>
> You can try repowering the board or pressing the button near the USB Type-C power interface. This usually resolves the issue.

### Logging into the System

Login to the system via the serial port.

Username: `root`
Default Password: `linux`

## Expected Results

The system should boot normally and allow login via the serial port.

## Actual Results

The system booted successfully and login via the serial port was successful.

### Boot Log

```log
Welcome to openSUSE Tumbleweed 20240322 - Kernel 6.8.1-85-default (ttyS0).                                                          
                                                                                                                                    
end0:  fe80::ecba:cd3:320d:39f8                                                                                                     
end1:                                                                                                                               
                                                                                                                                    
                                                                                                                                    

localhost login: root                                                                                                               
Password:                                                                                                                           
Have a lot of fun...                                                                                                                
localhost:~ # uname -a                                                                                                              
Linux localhost.localdomain 6.8.1-85-default #1 SMP PREEMPT_DYNAMIC Fri Mar 22 07:05:00 UTC 2024 (c838682) riscv64 riscv64 riscv64 x
localhost:~ # cat /etc/os-release                                                                                                   
NAME="openSUSE Tumbleweed"                                                                                                          
# VERSION="20240322"                                                                                                                
ID="opensuse-tumbleweed"                                                                                                            
ID_LIKE="opensuse suse"                                                                                                             
VERSION_ID="20240322"                                                                                                               
PRETTY_NAME="openSUSE Tumbleweed"                                                                                                   
ANSI_COLOR="0;32"                                                                                                                   
# CPE 2.3 format, boo#1217921                                                                                                       
CPE_NAME="cpe:2.3:o:opensuse:tumbleweed:20240322:*:*:*:*:*:*:*"                                                                     
#CPE 2.2 format                                                                                                                     
#CPE_NAME="cpe:/o:opensuse:tumbleweed:20240322"                                                                                     
BUG_REPORT_URL="https://bugzilla.opensuse.org"                                                                                      
SUPPORT_URL="https://bugs.opensuse.org"                                                                                             
HOME_URL="https://www.opensuse.org"                                                                                                 
DOCUMENTATION_URL="https://en.opensuse.org/Portal:Tumbleweed"                                                                       
LOGO="distributor-logo-Tumbleweed"                                                                                                  
localhost:~ # 
```

Screen recording (from flashing the image to logging into the system):

[![asciicast](https://asciinema.org/a/z3xt9HGtT5iVtI7tbtQNi9rHf.svg)](https://asciinema.org/a/z3xt9HGtT5iVtI7tbtQNi9rHf)

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
