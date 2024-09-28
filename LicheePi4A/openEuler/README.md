---
sys: openeuler
sys_ver: 24.03
sys_var: null

status: good
last_update: 2024-06-21
---

# openEuler RISC-V 24.03 LPi4A Test Report

## Test Environment

### System Information

- System Version: openEuler 24.03 LTS RISC-V
- Download Link: https://www.openeuler.org/en/download/?version=openEuler%2024.03%20LTS
- Reference Installation Document: https://docs.openeuler.org/en/docs/24.03_LTS/docs/Installation/RISC-V-LicheePi4A.html

### Hardware Information

- Lichee Pi 4A (16G RAM + 128G eMMC)
- USB-C Power Adapter / DC Power Supply
- A USB-UART Debugger

## Installation Steps

### Download and decompress image

Download the image from official website: https://www.openeuler.org/en/download/?version=openEuler%2024.03%20LTS

Choose `RISC-V -> Embedded -> lpi4a`.

### Flash to onboard eMMC via `fastboot`

By default the USB VID/PID of LPi4A are't in the udev rules, you might need to use `sudo` while using `fastboot`.

Hold the **BOOT** button, then connect the USB-C cable (to your PC on the other side) to enter USB burning mode.

In Windows using device manager, you'll see a device named `USB download gadget`.

In Linux using `lsusb` you'll see a device like: `ID 2345:7654 T-HEAD USB download gadget`.

Use the following commands to flash the image.

```shell
fastboot flash ram u-boot-with-spl-lpi4a-16g.bin
fastboot reboot
# Wait a few seconds until the board reboots and reconnects to your PC
fastboot flash uboot u-boot-with-spl-lpi4a-16g.bin
fastboot flash boot openEuler-24.03-LTS-riscv64-lpi4a-base-boot.ext4
fastboot flash root openEuler-24.03-LTS-riscv64-lpi4a-base-root.ext4
```

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
Welcome to 6.6.0-27.0.0.31.oe2403.riscv64                                                                               
                                                                                                                        
System information as of time:  Thu Sep  5 18:03:57 CST 2024                                                            
                                                                                                                        
System load:    2.50                                                                                                    
Memory used:    1.2%                                                                                                    
Swap used:      0.0%                                                                                                    
Usage On:       2%                                                                                                      
IP address:     10.0.0.8                                                                                                
Users online:   1                                                                                                       
To run a command as administrator(user "root"),use "sudo <command>".                                                    
[openeuler@openeuler-riscv64 ~]$ cat /etc/os-release                                                                    
NAME="openEuler"                                                                                                        
VERSION="24.03 (LTS)"                                                                                                   
ID="openEuler"                                                                                                          
VERSION_ID="24.03"                                                                                                      
PRETTY_NAME="openEuler 24.03 (LTS)"                                                                                     
ANSI_COLOR="0;31"                                                                                                       
                                                                                                                        
[openeuler@openeuler-riscv64 ~]$ uname -a                                                                               
Linux openeuler-riscv64 6.6.0-27.0.0.31.oe2403.riscv64 #1 SMP Fri May 24 21:52:58 CST 2024 riscv64 riscv64 riscv64 GNU/Linux
```

Screen recording (from flashing image to logging into system):

[![asciicast](https://asciinema.org/a/Jo6gwkRgaOBAeXgbwIuK4OWel.svg)](https://asciinema.org/a/Jo6gwkRgaOBAeXgbwIuK4OWel)

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
