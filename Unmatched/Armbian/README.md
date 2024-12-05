---
sys: armbian
sys_ver: 25.2.0
sys_var: null

status: cft
last_update: 2024-12-04
----

# Armbian Unmatched Test Report

## Test Environment

### Operating System Information

- Download Link: https://www.armbian.com/sifive-unmatched/
- Reference Installation Document: https://docs.armbian.com/User-Guide_Getting-Started/

### Hardware Information

- Development Board: Unmatched
- USB A to C / USB C to C Cable
- SD Card

## Installation Steps

### Flashing Image

After downloading, unzip and flash the image:
```bash
unxz -k Armbian_community_25.2.0-trunk.86_Unmatched_noble_edge_6.1.119_minimal.img.xz
sudo dd if=Armbian_community_25.2.0-trunk.86_Unmatched_noble_edge_6.1.119_minimal.img.xz of=/dev/your/sdcard bs=1M status=progress
```

### Logging into the System

Connect to the development board via the serial port.

Upon startup, the system will prompt the user to manually configure the username, password, timezone, language, etc.

The Xfce version requires configuration completion before entering the desktop environment.

Configuration can be done via the serial port. If a keyboard and monitor are connected, it can also be done via the keyboard.

## Expected Results

The system boots up normally, and information can be viewed through the onboard serial port.

## Actual Results

CFT

### Boot Log

Screen recording (from flashing the system to booting up):
```log
```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

CFT