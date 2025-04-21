---
sys: armbian
sys_ver: "23.09.15"
sys_var: null

status: good
last_update: 2025-04-21
---

# Armbian LPi4A Test Report

## Test Environment

### System Information

- System Version: 23.09.15
- Download Link: [Releases · chainsx/armbian-riscv-build](https://github.com/chainsx/armbian-riscv-build/releases)
  - u-boot: [Releases · chainsx/armbian-riscv-build](https://github.com/chainsx/armbian-riscv-build/releases)
- Reference Installation Document: [LicheePi 4A Install Guide](https://github.com/chainsx/armbian-riscv-build/blob/main/doc/licheepi-4a-install-guide.md)

### Hardware Information

- Lichee Pi 4A (8GB RAM + 32GB eMMC)
- Power Adapter
- A USB to UART Debugger

## Installation Steps

### Flashing Bootloader

Enter fastboot mode.

- Press BOOT while powering on.
- (Refer to the official tutorial) Use the fastboot command to flash u-boot.

```bash
sudo ./fastboot flash ram ./path/to/your/lpi4a-8gb-u-boot-with-spl.bin
sudo ./fastboot reboot
sleep 1
sudo ./fastboot flash uboot ./path/to/your/lpi4a-8gb-u-boot-with-spl.bin
```

### Flashing Image

Use `unxz` to decompress the image.
Use `dd` to flash the image to the EMMC.

```bash
unxz /path/to/Armbian-riscv_23.09.15-riscv_Licheepi-4a_focal_current_5.10.113_xfce_desktop.img.xz
// Interrupt the countdown in u-boot by pressing Ctrl+C to enter the u-boot command line
// Input the following commands:
Light LPI4A# ums 0 mmc 0
// Then, the EMMC will be mapped as a USB Mass Storage device on the computer.
sudo dd if=/path/to/Armbian-riscv_23.09.15-riscv_Licheepi-4a_focal_current_5.10.113_xfce_desktop.img of=/path/to/device bs=1M status=progress
```

### Logging into the System

Logging into the system via the serial port.

On initial startup, you will be prompted to set up a user and locales.

### Desktop Environment

The desktop environment should start automatically.


## Expected Results

The system should boot normally and allow login via the onboard serial port.

## Actual Results

The system booted successfully and login via the onboard serial port was also successful.

### Boot Log

![desktop](desktop.png)

Screen recording:

[![asciicast](https://asciinema.org/a/yoqY7oCXaEcRB8bGwc7GmQyEc.svg)](https://asciinema.org/a/yoqY7oCXaEcRB8bGwc7GmQyEc)

```log
Now starting desktop environment...

root@licheepi-4a:~# neofetch
            .-/+oossssoo+/-.               root@licheepi-4a
        `:+ssssssssssssssssss+:`           ----------------
      -+ssssssssssssssssssyyssss+-         OS: Ubuntu 20.04 LTS riscv64
    .ossssssssssssssssssdMMMNysssso.       Host: T-HEAD Light Lichee Pi 4A configuration for 8GB DDR board
   /ssssssssssshdmmNNmmyNMMMMhssssss/      Kernel: 5.10.113-thead-g052b22ef8baf
  +ssssssssshmydMMMMMMMNddddyssssssss+     Uptime: 2 mins
 /sssssssshNMMMyhhyyyyhmNMMMNhssssssss/    Packages: 1283 (dpkg)
.ssssssssdMMMNhsssssssssshNMMMdssssssss.   Shell: bash 5.0.16
+sssshhhyNMMNyssssssssssssyNMMMysssssss+   Terminal: /dev/ttyS0
ossyNMMMNyMMhsssssssssssssshmmmhssssssso   CPU: (4) @ 1.848GHz
ossyNMMMNyMMhsssssssssssssshmmmhssssssso   Memory: 161MiB / 7705MiB
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
