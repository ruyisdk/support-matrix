# Arch Linux Milk-V Duo Test Report

## Test Environment

### Operating System Information

- System Version: milkv-duo-archlinux-riscv64-2023-10-09-7.0gb-v0.0.3-spiritdude.img
- Download Link: https://drive.google.com/file/d/1Qf8ioR29KCsvt2MIWre168Um9Q8ot_z5/view?usp=sharing
- Reference Installation Document: https://xyzdims.com/3d-printers/misc-hardware-notes/iot-milk-v-duo-risc-v-esbc-running-linux/#ArchLinux_Disk_Image

> Note: This image is provided by community developers and is not an official image.

### Hardware Information

- Milk-V Duo 64M
- One USB Power Adapter
- One USB-A to C or USB C to C Cable
- One microSD Card
- One USB to UART Debugger (e.g., CH340, CH341, FT2232, etc.)
- Three Dupont Wires
- Milk-V Duo with necessary header pins pre-soldered for debugging
- Optional: Milk-V Duo IOB (Baseboard)

## Installation Steps

### Using `dd` to Flash the Image to the microSD Card 

```shell
unzip milkv-duo-archlinux-riscv64-2023-10-09-7.0gb-v0.0.3-spiritdude.zip
dd if=milkv-duo-archlinux-riscv64-2023-10-09-7.0gb-v0.0.3-spiritdude.img of=/dev/sdc bs=1M status=progress
```

### Logging into the System

Logging into the system via the serial port.

Username: `root`
Password: `milkv`

## Expected Results

The system boots up normally and allows login through the serial port.

## Actual Results

The system boots up normally and login through the serial port is successful.

### Boot Log

```log
[root@archlinux ~]# uname -a                                                                                                        
Linux archlinux 5.10.4-tag- #1 PREEMPT Wed Oct 18 17:20:17 CEST 2023 riscv64 GNU/Linux                                              
[root@archlinux ~]# neofetch                                                                                                        
                   -`                                                                                                               
                  .o+`                   --------------                                                                             
                 `ooo/                   OS: Arch Linux riscv64                                                                     
                `+oooo:                  Host: Cvitek. CV180X ASIC. C906.                                                           
               `+oooooo:                 Kernel: 5.10.4-tag-                                                                        
               -+oooooo+:                Uptime: 54 secs                                                                            
             `/:-:++oooo+:               Packages: 143 (pacman)                                                                     
            `/++++/+++++++:              Shell: bash 5.1.16                                                                         
           `/++++++++++++++:             Terminal: /dev/ttyS0                                                                       
          `/+++ooooooooooooo/`           CPU: (1)                                                                                   
         ./ooosssso++osssssso+`          Memory: 23MiB / 54MiB                                                                      
        .oossssso-````/ossssss+`                                                                                                    
       -osssssso.      :ssssssso.                                                                                                   
      :osssssss/        osssso+++.                                                                                                  
     /ossssssss/        +ssssooo/-                                                                                                  
   `/ossssso+/:-        -:/+osssso+-                                                                                                
  `+sso+:-`                 `.-/+oso:                                                                                               
 `++:.                           `-/+/                                                                                              
 .`                                 `/                                                                                              
                                                                                                                                    
[root@archlinux ~]# 
```

Screen recording (From flashing image to login):

[![asciicast](https://asciinema.org/a/GIQOyBNHONziQszZ13HDhs2lP.svg)](https://asciinema.org/a/GIQOyBNHONziQszZ13HDhs2lP)

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
