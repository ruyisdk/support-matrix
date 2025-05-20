---
sys: NixOS
sys_ver: "23.05"
sys_var: null

status: basic
last_update: 2025-05-20
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

- Lichee Pi 4A (8GB RAM + 32GB eMMC)
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

Screen recording:

[![asciicast](https://asciinema.org/a/1tapS19lE8Mnlsr8tHgjT3bOr.svg)](https://asciinema.org/a/1tapS19lE8Mnlsr8tHgjT3bOr)



```log
[  OK  ] Mounted FUSE Control File System.
[  OK  ] Mounted Kernel Configuration File System.
[  OK  ] Finished Load/Save OS Random Seed.
[  OK  ] Finished Apply Kernel Variables.
[  OK  ] Finished Flush Journal to Persistent Storage.
         Starting Create Volatile Files and Directories...
[  OK  ] Started Rule-based Manager for Device Events and Files.
[FAILED] Failed to start Firewall.
See 'systemctl status firewall.service' for details.
[  OK  ] Finished Create Volatile Files and Directories.
         Starting Rebuild Journal Catalog...
         Starting Network Time Synchronization...
         Starting Record System Boot/Shutdown in UTMP...
[  OK  ] Finished Rebuild Journal Catalog.
[  OK  ] Finished Record System Boot/Shutdown in UTMP.
         Starting Update is Completed...
[  OK  ] Finished Update is Completed.
[  OK  ] Started Network Time Synchronization.
[  OK  ] Found device /dev/ttyS0.
[  OK  ] Finished Coldplug All udev Devices.
[  OK  ] Created slice Slice /system/systemd-backlight.
[  OK  ] Reached target Sound Card.
[  OK  ] Listening on Load/Save RF …itch Status /dev/rfkill Watch.
         Starting Load/Save Screen …f backlight:pwm-backlight@0...
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
         Starting Load/Save RF Kill Switch Status...
[  OK  ] Started Name Service Cache Daemon (nsncd).
[  OK  ] Started Load/Save RF Kill Switch Status.
[  OK  ] Finished Kernel Auditing.
[  OK  ] Finished CPU Frequency Setup.
[  OK  ] Finished Logrotate configuration check.
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
[  OK  ] Finished resolvconf update.
[  OK  ] Started D-Bus System Message Bus.
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

lp4a login: lp4a
Password:

[lp4a@lp4a:~]$ uname -a
Linux lp4a 5.10.113 #1-NixOS SMP PREEMPT Tue Jan 1 00:00:00 UTC 1980 riscv64 GNU/Linux

[lp4a@lp4a:~]$ neofetch
          ▗▄▄▄       ▗▄▄▄▄    ▄▄▄▖            lp4a@lp4a
          ▜███▙       ▜███▙  ▟███▛            ---------
           ▜███▙       ▜███▙▟███▛             OS: NixOS 23.05.20230806.240472b (Stoat) riscv64
            ▜███▙       ▜██████▛              Host: T-HEAD Light Lichee Pi 4A configuration for 8GB DDR board
     ▟█████████████████▙ ▜████▛     ▟▙        Kernel: 5.10.113
    ▟███████████████████▙ ▜███▙    ▟██▙       Uptime: 1 min
           ▄▄▄▄▖           ▜███▙  ▟███▛       Packages: 306 (nix-system)
          ▟███▛             ▜██▛ ▟███▛        Shell: bash 5.2.15
         ▟███▛               ▜▛ ▟███▛         Terminal: /dev/ttyS0
▟███████████▛                  ▟██████████▙   CPU: (4) @ 1.848GHz
▜██████████▛                  ▟███████████▛   Memory: 172MiB / 7781MiB
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
