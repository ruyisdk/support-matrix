# Fedora 38 LPi4A chainsx Test Report

## Test Environment

### System Information

- System Version: Fedora 38
- Download Link: [https://github.com/chainsx/fedora-riscv-builder/releases](https://github.com/chainsx/fedora-riscv-builder/releases)
- Reference Installation Document: [https://wiki.sipeed.com/hardware/zh/lichee/th1520/lpi4a/4_burn_image.html](https://wiki.sipeed.com/hardware/zh/lichee/th1520/lpi4a/4_burn_image.html)
- Fastboot Links:
    - [https://pan.baidu.com/e/1xH56ZlewB6UOMlke5BrKWQ](https://pan.baidu.com/e/1xH56ZlewB6UOMlke5BrKWQ)
    - [https://mega.nz/folder/phoQlBTZ#cZeQ3qZ__pDvP94PT3_bGA](https://mega.nz/folder/phoQlBTZ#cZeQ3qZ__pDvP94PT3_bGA)

### Hardware Information

- Lichee Pi 4A (8GB RAM + 64GB eMMC)
- Power Adapter
- A microSD Card
- A USB to UART Debugger

## Installation Steps

### Flashing Bootloader

Enter fastboot mode.
- Make sure the boot DIP switch is set to eMMC for the production version.
- Press the BOOT button while powering on.
- (Refer to the official tutorial) Use fastboot command to burn the u-boot.

```bash
sudo ./fastboot flash ram ./path/to/your/lpi4a-($ram_size)gb-u-boot-with-spl.bin
sudo ./fastboot reboot
sleep 10
sudo ./fastboot flash uboot ./path/to/your/lpi4a-($ram_size)gb-u-boot-with-spl.bin
```

### Flashing Image

Use `unxz` to extract the image.
Use `dd` to flash the image to the microSD card.

```bash
unxz /path/to/fedora.raw.xz
sudo dd if=/path/to/fedora.raw of=/dev/your_device bs=1M status=progress
```

### Logging into System

Logging into the system via serial console.

Default username: `root`
Default password: `fedora`

## Expected Results

The system should start up successfully and be accessible via the onboard serial console.

## Actual Results

The system started up correctly and I successfully logged in via the onboard serial console.

### Boot Log

Screen recording (from flashing the image to logging into the system):

[![asciicast](https://asciinema.org/a/EkD4lbohO4sNJGO518rLQtL59.svg)](https://asciinema.org/a/EkD4lbohO4sNJGO518rLQtL59)

```log
Fedora Linux 38 (Thirty Eight)
Kernel 5.10.113-g052b22ef8baf on an riscv64 (ttyS0)

fedora-riscv login: root
Password: 
Last login: Thu May 11 00:00:31 on ttyS0
[root@fedora-riscv ~]# [   35.894822] soc_dovdd18_scan: disabling
[   35.899400] soc_dvdd12_scan: disabling
[   35.903909] soc_avdd28_scan_en: disabling
[root@fedora-riscv ~]# uname -a
Linux fedora-riscv 5.10.113-g052b22ef8baf #1 SMP PREEMPT Thu Sep 14 05:05:31 UTC 2023 riscv64 GNU/Linux
[root@fedora-riscv ~]# cat /etc/os-release 
NAME="Fedora Linux"
VERSION="38 (Thirty Eight)"
ID=fedora
VERSION_ID=38
VERSION_CODENAME=""
PLATFORM_ID="platform:f38"
PRETTY_NAME="Fedora Linux 38 (Thirty Eight)"
ANSI_COLOR="0;38;2;60;110;180"
LOGO=fedora-logo-icon
CPE_NAME="cpe:/o:fedoraproject:fedora:38"
DEFAULT_HOSTNAME="fedora"
HOME_URL="https://fedoraproject.org/"
DOCUMENTATION_URL="https://docs.fedoraproject.org/en-US/fedora/f38/system-administrators-guide/"
SUPPORT_URL="https://ask.fedoraproject.org/"
BUG_REPORT_URL="https://bugzilla.redhat.com/"
REDHAT_BUGZILLA_PRODUCT="Fedora"
REDHAT_BUGZILLA_PRODUCT_VERSION=38
REDHAT_SUPPORT_PRODUCT="Fedora"
REDHAT_SUPPORT_PRODUCT_VERSION=38
SUPPORT_END=2024-05-14
```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.

