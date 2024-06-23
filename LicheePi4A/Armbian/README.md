# Armbian LPi4A Test Report

## Test Environment

### System Information

- System Version: Ubuntu 20.04 LTS 
- Download Link: [Armbian-RISCV-Build Repository](https://github.com/chainsx/armbian-riscv-build/tree/main)
    - u-boot: [thead-u-boot Actions](https://github.com/chainsx/thead-u-boot/actions)
- Reference Installation Document: [LicheePi 4A Install Guide](https://github.com/chainsx/armbian-riscv-build/blob/main/doc/licheepi-4a-install-guide.md)
- Fastboot Links:
    - [Baidu Pan Link](https://pan.baidu.com/e/1xH56ZlewB6UOMlke5BrKWQ)
    - [MegaNZ Link](https://mega.nz/folder/phoQlBTZ#cZeQ3qZ__pDvP94PT3_bGA)

### Hardware Information

- Lichee Pi 4A (8GB RAM + 64GB eMMC)
- Power Adapter
- A microSD card
- A USB to UART Debugger

## Installation Steps

### Flashing Image

Use `unxz` to decompress the image.
Use `dd` to flash the image to the microSD card.

```bash
unxz /path/to/Armbian.img.xz
sudo dd if=/path/to/Armbian.img of=/dev/your_device bs=1M status=progress
```

### Flashing Bootloader

Enter fastboot mode.
- Ensure the boot dip switch is set to eMMC.
- Press BOOT while powering on.
- (Refer to the official tutorial) Use the fastboot command to flash u-boot.

```bash
sudo ./fastboot flash ram ./path/to/your/lpi4a-$(ram_size)-u-boot-with-spl.bin
sudo ./fastboot reboot
sleep 10
sudo ./fastboot flash uboot ./path/to/your/lpi4a-$(ram_size)-u-boot-with-spl.bin
```

### Logging into the System

Logging into the system via the serial port.

On initial startup, you will be prompted to set up a user and password.

## Expected Results

The system should boot normally and allow login via the onboard serial port.

## Actual Results

The system booted successfully and login via the onboard serial port was also successful.

### Boot Log

Screen recording (From flashing image to system login):
[![asciicast](https://asciinema.org/a/CPXNwT3yJUG4wHDKdWGucbHm9.svg)](https://asciinema.org/a/CPXNwT3yJUG4wHDKdWGucbHm9))

```log
Welcome to ARMBIAN! 

Documentation: https://docs.armbian.com | Community: https://forum.armbian.com

Create root password: *****
Repeat root password: *****
Rejected - it is too short. Try again [3].
Create root password: ********
Repeat root password: ********

Choose default system command shell:

1) bash
2) zsh

Shell: BASH

Creating a new user account. Press <Ctrl-C> to abort

Desktop environment will not be enabled if you abort the new user creation

Please provide a username (eg. your first name): ^C
Disabling user account creation procedure

root@licheepi-4a:~# neofetch 
            .-/+oossssoo+/-.                                                                                                    
        `:+ssssssssssssssssss+:`           ---------------- 
      -+ssssssssssssssssssyyssss+-         OS: Ubuntu 20.04 LTS riscv64 
    .ossssssssssssssssssdMMMNysssso.       Host: T-HEAD Light Lichee Pi 4A configuration for 8GB DDR board 
   /ssssssssssshdmmNNmmyNMMMMhssssss/      Kernel: 5.10.113-thead-g052b22ef8baf 
  +ssssssssshmydMMMMMMMNddddyssssssss+     Uptime: 1 min 
 /sssssssshNMMMyhhyyyyhmNMMMNhssssssss/    Packages: 1283 (dpkg) 
.ssssssssdMMMNhsssssssssshNMMMdssssssss.   Shell: bash 5.0.16 
+sssshhhyNMMNyssssssssssssyNMMMysssssss+   Terminal: /dev/ttyS0 
ossyNMMMNyMMhsssssssssssssshmmmhssssssso   CPU: (4) @ 1.848GHz 
ossyNMMMNyMMhsssssssssssssshmmmhssssssso   Memory: 165MiB / 7705MiB 
+sssshhhyNMMNyssssssssssssyNMMMysssssss+
.ssssssssdMMMNhsssssssssshNMMMdssssssss.                           
 /sssssssshNMMMyhhyyyyhdNMMMNhssssssss/                            
  +sssssssssdmydMMMMMMMMddddyssssssss+
   /ssssssssssshdmNNNNmyNMMMMhssssss/
    .ossssssssssssssssssdMMMNysssso.
      -+sssssssssssssssssyyyssss+-
        `:+ssssssssssssssssss+:`
            .-/+oossssoo+/-.


```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.

