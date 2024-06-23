# Debian bookworm/sid HiFive Unmatched Test Report

## Test Environment

### Operating System Information

- System Version: Debian bookworm/sid
- Download Link: https://people.debian.org/~deiv/riscv/debian-sid-risc-v-sifive-unmatched.tar.xz
- Reference Installation Document: https://wiki.debian.org/InstallingDebianOn/SiFive/%20HiFiveUnmatched

### Hardware Information

- HiFive Unmatched Rev A
- A microUSB cable (included with HiFive Unmatched)
- An ATX power supply
- A microSD card (Sandisk Extreme Pro 64G UHS-I)

## Installation Steps

### Boot Device Selection

Ensure the DIP switch is set to boot from the microSD card. By default, the factory setting is already configured to boot from the microSD card.

The DIP switch should be set as follows: `MSEL[3:0]=1011`

### Decompress and Flash the Image to the microSD Card

`/dev/sdc` is the location of the microSD card, please adjust accordingly.

```bash
tar xvf debian-sid-risc-v-sifive-unmatched.tar.xz
sudo dd if=debian-sid-risc-v-sifive-unmatched.img of=/dev/sdc bs=1M status=progress
```

### Logging into the System

Logging into the system via the onboard serial port (using the microUSB cable connected to another computer).

Default username: `root`
Default password: `sifive`

## Expected Results

The system boots normally and allows login through the onboard serial port.

## Actual Results

The system booted successfully and login through the onboard serial port was also successful.

### Boot Log

```log
Debian GNU/Linux bookworm/sid unmatched ttySIF0                                                                       
                                                                                                                      
unmatched login: root                                                                                                 
Password:                                                                                                             
Linux unmatched 5.14.0-3-riscv64 #1 SMP Debian 5.14.12-1 (2021-10-14) riscv64                                         
                                                                                                                      
The programs included with the Debian GNU/Linux system are free software;                                             
the exact distribution terms for each program are described in the                                                    
individual files in /usr/share/doc/*/copyright.                                                                       
                                                                                                                      
Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent                                                     
permitted by applicable law.                                                                                          
root@unmatched:~# uname -a                                                                                            
Linux unmatched 5.14.0-3-riscv64 #1 SMP Debian 5.14.12-1 (2021-10-14) riscv64 GNU/Linux                               
root@unmatched:~# cat /etc/os-release                                                                                 
PRETTY_NAME="Debian GNU/Linux bookworm/sid"                                                                           
NAME="Debian GNU/Linux"                                                                                               
ID=debian                                                                                                             
HOME_URL="https://www.debian.org/"                                                                                    
SUPPORT_URL="https://www.debian.org/support"                                                                          
BUG_REPORT_URL="https://bugs.debian.org/"                                                                             
root@unmatched:~# cat /proc/cpuinfo                                                                                   
processor       : 0                                                                                                   
hart            : 4                                                                                                   
isa             : rv64imafdc                                                                                          
mmu             : sv39                                                                                                
uarch           : sifive,bullet0                                                                                      
                                                                                                                      
processor       : 1                                                                                                   
hart            : 1                                                                                                   
isa             : rv64imafdc                                                                                          
mmu             : sv39                                                                                                
uarch           : sifive,bullet0                                                                                      
                                                                                                                      
processor       : 2                                                                                                   
hart            : 2                                                                                                   
isa             : rv64imafdc                                                                                          
mmu             : sv39                                                                                                
uarch           : sifive,bullet0                                                                                      
                                                                                                                      
processor       : 3                                                                                                   
hart            : 3                                                                                                   
isa             : rv64imafdc                                                                                          
mmu             : sv39                                                                                                
uarch           : sifive,bullet0                                                                                      
                                                                                                                      
root@unmatched:~# 
```

Screen recording (From flashing image to login):

[![asciicast](https://asciinema.org/a/YjvmONomTstvHYU4yLnKVX7Rv.svg)](https://asciinema.org/a/YjvmONomTstvHYU4yLnKVX7Rv)

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
