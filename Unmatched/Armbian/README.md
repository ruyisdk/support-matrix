---
sys: armbian
sys_ver: 25.2.0-trunk.266
sys_var: noble

status: cfh
last_update: 2025-04-14
---

# Armbian Unmatched Test Report

## Test Environment

### Operating System Information

- Download Link: https://www.armbian.com/sifive-unmatched/
    - https://github.com/armbian/community/releases/tag/25.2.0-trunk.266
        - Minimal: https://github.com/armbian/community/releases/download/25.2.0-trunk.266/Armbian_community_25.2.0-trunk.266_Unmatched_noble_edge_6.1.123_minimal.img.xz
        - Xfce: https://github.com/armbian/community/releases/download/25.2.0-trunk.266/Armbian_community_25.2.0-trunk.266_Unmatched_noble_edge_6.1.123_xfce_desktop.img.xz
    - Archive version (23.8.1): https://imola.armbian.com/archive/unmatched/archive/
- Reference Installation Document: https://docs.armbian.com/User-Guide_Getting-Started/

### Hardware Information

- HiFive Unmatched Rev A
- A microUSB cable (comes with HiFive Unmatched)
- An ATX power supply
- A microSD card

## Installation Steps

### Flashing Image

After downloading, unzip and flash the image:

```bash
unxz -k Armbian_community_25.2.0-trunk.266_Unmatched_noble_edge_6.1.123_minimal.img.xz
sudo dd if=Armbian_community_25.2.0-trunk.266_Unmatched_noble_edge_6.1.123_minimal.img of=/dev/your/sdcard bs=1M status=progress
```

### Logging into the System

Connect to the development board via the serial port.

Upon startup, the system will prompt the user to manually configure the username, password, timezone, language, etc.

The Xfce version requires configuration completion before entering the desktop environment.

Configuration can be done via the serial port. If a keyboard and monitor are connected, it can also be done via the keyboard.

## Expected Results

The system boots up normally, and information can be viewed through the onboard serial port.

## Actual Results

Neither version booted up.

The image doesn't comes with U-Boot, however even with U-Boot on SPI and OS on M.2 NVMe, U-Boot still can't detect any OS on the SSD and boot.

Version 23.8.1 from Armbian archive didn't boot from microSD either.

### Boot Log

Screen recording (from flashing the system to booting up):

N/A

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test failed / CFH

## Other notes

There is an issue in the community related to this: https://github.com/armbian/community/issues/28

However Unmatched is marked as "Community maintained", which is in fact unsupported by Armbian officially, thus this issue was already closed.