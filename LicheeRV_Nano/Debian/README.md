# BuildRoot LicheeRV Nano Test Report

## Test Environment

### Operating System Information

- System Version: Initial Release
- Download Link: [sophgo-sg200x-debian on GitHub](https://github.com/Fishwaldo/sophgo-sg200x-debian)
- Reference Installation Document: [sophgo-sg200x-debian on GitHub](https://github.com/Fishwaldo/sophgo-sg200x-debian)

### Hardware Information

- LicheeRV Nano
- A Type-C power cable
- A UART to USB debugger

## Installation Steps

### Using `dd` to flash the image to the microSD card

Download the image and perform decompression and flashing:

```shell
lz4 -dk licheervnano_sd.img.lz4
sudo dd if=licheervnano_sd.img of=/dev/your_device bs=1M status=progress
```

### Logging into the System

Logging into the system through the serial port.

| Username | Password |
|----------|----------|
| root     | rv       |
| debian   | rv       |


## Expected Results

The system should boot up normally and allow login through the serial port.

## Actual Results

The system booted up successfully, and login through the serial port was successful.

### Boot Log

Screen recording (from flashing the image to login):

[![asciicast](https://asciinema.org/a/d6uwAengdlXVbMj0KAdVbPhMX.svg)](https://asciinema.org/a/d6uwAengdlXVbMj0KAdVbPhMX)

```log
Debian GNU/Linux trixie/sid licheervnano ttyS0                                                                          
                                                                                                                        
licheervnano login: root                                                                                                
Password:                                                                                                               
Linux licheervnano 5.10.4-20240329-1+ #1 PREEMPT Sat Apr 13 07:08:27 UTC 2024 riscv64                                   
                                                                                                                        
The programs included with the Debian GNU/Linux system are free software;                                               
the exact distribution terms for each program are described in the                                                      
individual files in /usr/share/doc/*/copyright.                                                                         
                                                                                                                        
Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent                                                       
permitted by applicable law.                                                                                            
root@licheervnano:~# cat /proc/cpuinfo                                                                                  
processor       : 0                                                                                                     
hart            : 0                                                                                                     
isa             : rv64imafdvcsu                                                                                         
mmu             : sv39                                                                                                  
                                                                                                                        
root@licheervnano:~# cat /etc/os-release                                                                                
PRETTY_NAME="Debian GNU/Linux trixie/sid"                                                                               
NAME="Debian GNU/Linux"                                                                                                 
VERSION_CODENAME=trixie                                                                                                 
ID=debian                                                                                                               
HOME_URL="https://www.debian.org/"                                                                                      
SUPPORT_URL="https://www.debian.org/support"                                                                            
BUG_REPORT_URL="https://bugs.debian.org/"                                                                               
root@licheervnano:~# uname -a                                                                                           
Linux licheervnano 5.10.4-20240329-1+ #1 PREEMPT Sat Apr 13 07:08:27 UTC 2024 riscv64 GNU/Linux                         
root@licheervnano:~# 
```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.

