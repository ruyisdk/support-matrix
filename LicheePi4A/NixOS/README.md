---
sys: NixOS 
sys_ver: 23.05
sys_var: null

status: basic



---

# NixOS LPi4A Test Report

## Test Environment

### System Information

- System Version: NixOS 23.05
- Download Link: [Releases · ryan4yin/nixos-licheepi4a](https://github.com/ryan4yin/nixos-licheepi4a/releases)
  - u-boot: [Releases · ryan4yin/nixos-licheepi4a](https://github.com/ryan4yin/nixos-licheepi4a/releases)
- Fastboot Links:
  - [Baidu Pan Link](https://pan.baidu.com/e/1xH56ZlewB6UOMlke5BrKWQ)
  - [MegaNZ Link](https://mega.nz/folder/phoQlBTZ#cZeQ3qZ__pDvP94PT3_bGA)

### Hardware Information

- Lichee Pi 4A (16GB RAM + 128GB eMMC)
- Power Adapter
- A microSD card
- A USB to UART Debugger

## Installation Steps

### Flashing Image

Use `zstd` to decompress the image.
Use `dd` to flash the image to the microSD card.

```bash
zstd -d /path/to/nixos-licheepi4a-sd-image-23.05.20230806.240472b-riscv64-linux.img.zst
sudo dd if=/path/to/nixos-licheepi4a-sd-image-23.05.20230806.240472b-riscv64-linux.img.zst of=/dev/your_device bs=1M status=progress
```

### Flashing Bootloader

Enter fastboot mode.

- Press BOOT while powering on.
- (Refer to the official tutorial) Use the fastboot command to flash u-boot.

```bash
sudo ./fastboot flash ram ./path/to/your/u-boot-with-spl.bin
sudo ./fastboot reboot
sudo ./fastboot flash uboot ./path/to/your/u-boot-with-spl.bin
```

### Logging into the System

Logging into the system via the serial port.

default username：`lp4a` default password: `lp4a` 

## Expected Results

The system should boot normally and allow login via the onboard serial port.

## Actual Results

The system booted successfully and login via the onboard serial port was also successful.

### Boot Log

Screen recording 

(From flashing uboot to system login, Flashing the image to the SD card has been completed in advance. ):
[![asciicast](https://asciinema.org/a/KxABHjizPRNfyyZuy5mg4FVTO.svg)](https://asciinema.org/a/KxABHjizPRNfyyZuy5mg4FVTO)

```log
[  OK  ] Finished Rebuild Journal Catalog.                                      
         Starting Update is Completed...                                        
[  OK  ] Finished Update is Completed.                                          
[  OK  ] Finished Record System Boot/Shutdown in UTMP.                          
[  OK  ] Started Network Time Synchronization.                                  
[  OK  ] Found device /dev/ttyS0.                                               
[  OK  ] Finished Coldplug All udev Devices.                                    
[  OK  ] Created slice Slice /system/systemd-backlight.                         
[  OK  ] Reached target Sound Card.                                             
[  OK  ] Listening on Load/Save RF …itch Status /dev/rfkill Watch.              
         Starting Load/Save Screen …f backlight:pwm-backlight@0...              
         Starting Load/Save RF Kill Switch Status...                            
[  OK  ] Started Load/Save RF Kill Switch Status.                               
[  OK  ] Finished Load/Save Screen … of backlight:pwm-backlight@0.              
[  OK  ] Reached target System Initialization.                                  
[  OK  ] Started logrotate.timer.                                               
[  OK  ] Started Daily Cleanup of Temporary Directories.                        
[  OK  ] Reached target Timer Units.                                            
[  OK  ] Listening on D-Bus System Message Bus Socket.                          
[  OK  ] Listening on Nix Daemon Socket.                                        
[  OK  ] Reached target Socket Units.                                           
[  OK  ] Reached target Basic System.                                           
         Starting Kernel Auditing...                                            
         Starting CPU Frequency Setup...                                        
         Starting DHCP Client...                                                
         Starting Logrotate configuration check...                              
         Starting Name Service Cache Daemon (nsncd)...                          
[  OK  ] Started Reset console on configuration changes.                        
         Starting resolvconf update...                                          
[  OK  ] Finished Kernel Auditing.                                              
[  OK  ] Finished CPU Frequency Setup.                                          
[  OK  ] Finished Logrotate configuration check.                                
[  OK  ] Started Name Service Cache Daemon (nsncd).                             
[  OK  ] Reached target Host and Network Name Lookups.                          
[  OK  ] Reached target User and Group Name Lookups.                            
         Starting D-Bus System Message Bus...                                   
         Starting User Login Management...                                      
[  OK  ] Stopped target Host and Network Name Lookups.                          
         Stopping Host and Network Name Lookups...                              
[  OK  ] Stopped target User and Group Name Lookups.                            
         Stopping User and Group Name Lookups...                                
         Stopping Name Service Cache Daemon (nsncd)...                          
[  OK  ] Stopped Name Service Cache Daemon (nsncd).                             
[  OK  ] Started D-Bus System Message Bus.                                      
[  OK  ] Finished resolvconf update.                                            
[  OK  ] Reached target Preparation for Network.                                
[  OK  ] Reached target All Network Interfaces (deprecated).                    
         Starting Networking Setup...                                           
         Starting Name Service Cache Daemon (nsncd)...                          
[  OK  ] Started User Login Management.                                         
[  OK  ] Started Name Service Cache Daemon (nsncd).                             
[  OK  ] Reached target Host and Network Name Lookups.                          
[  OK  ] Reached target User and Group Name Lookups.                            
[  OK  ] Finished Networking Setup.                                             
         Starting Extra networking commands....                                 
[  OK  ] Finished Extra networking commands..                                   
[  OK  ] Reached target Network.                                                
         Starting SSH Daemon...                                                 
         Starting Permit User Sessions...                                       
[  OK  ] Finished Permit User Sessions.                                         
[  OK  ] Started Getty on tty1.                                                 
[  OK  ] Started Serial Getty on ttyS0.                                         
[  OK  ] Reached target Login Prompts.                                          
                                                                                
                                                                                
<<< Welcome to NixOS 23.05.20230806.240472b (riscv64) - ttyS0 >>>               
                                                                                
Run 'nixos-help' for the NixOS manual.                                          
                                                                                
lp4a login: root                                                                
Password:                                                                       
                                                                                
Login incorrect                                                                 
lp4a login: lp4a                                                                
Password:                                                                       
                                                                                
[0;lp4a@lp4a: ~lp4a@lp4a:~]$ neofetch                                           
          ▗▄▄▄       ▗▄▄▄▄    ▄▄▄▖                                              
          ▜███▙       ▜███▙  ▟███▛            ---------                         
           ▜███▙       ▜███▙▟███▛             OS: NixOS 23.05.20230806.240472b  
            ▜███▙       ▜██████▛              Host: T-HEAD Light Lichee Pi 4A c 
     ▟█████████████████▙ ▜████▛     ▟▙        Kernel: 5.10.113                  
    ▟███████████████████▙ ▜███▙    ▟██▙       Uptime: 1 min                     
           ▄▄▄▄▖           ▜███▙  ▟███▛       Packages: 306 (nix-system)        
          ▟███▛             ▜██▛ ▟███▛        Shell: bash 5.2.15                
         ▟███▛               ▜▛ ▟███▛         Terminal: /dev/ttyS0              
▟███████████�                 ▟██████████▙ CPU: (4--+) @ 1.848GHz               
▜██████████▛                  ▟███████████▛   Memory: 173MiB / 7781MiB          
      ▟███▛ ▟▙               ▟███▛                                              
     ▟███▛ ▟██▙             ▟███▛                                               
    ▟███▛  ▜███▙           ▝▀▀▀▀                                                
    ▜██▛    ▜███▙ ▜██████████████████▛                                          
     ▜▛     ▟████▙ ▜████████████████▛                                           
           ▟██████▙       ▜███▙                                                 
          ▟███▛▜███▙       ▜███▙                                                
         ▟███▛  ▜███▙       ▜███▙                                               
         ▝▀▀▀    ▀▀▀▀▘       ▀▀▀▘                                               
                                     
```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.