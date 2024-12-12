---
sys: RevyOS
sys_ver: 20231210
sys_var: null

status: CFT
last_update: 2024-12-12
---

# RevyOS BeagleV-Ahead Test Report

## Test Environment

### System Information

- Download link: https://mirror.iscas.ac.cn/revyos/extra/images/beagle/20231210/
- Reference Installation Document: https://docs.beagleboard.org/latest/boards/beaglev/ahead/02-quick-start.html

### Hardware Information

- BeagleV-Ahead
- USB-C Power Adapter / DC power supply
- USB-UART debugger

## Installation Steps

### Flashing Image 

Install fastboot:
```bash
sudo apt-get install android-sdk-platform-tools
```

Unpack the installation package. Run the automatic flashing script:

```bash
zstd -d boot-ahead-20231210_134926.ext4.zst -o boot.ext4
zstd -d root-ahead-20231210_134926.ext4.zst -o root.ext4

sudo fastboot flash ram ./u-boot-with-spl.bin
sudo fastboot reboot
sudo fastboot oem format
sudo fastboot flash uboot ./u-boot-with-spl.bin
sudo fastboot flash boot ./boot.ext4
sudo fastboot flash root ./root.ext4
sudo fastboot reboot
```

### Logging into the System

Logging into the system via serial port.

Default username: `debian`
Default password: `debian`

## Expected Results

The system boots up successfully and can be logged into through the onboard serial port.

## Actual Results

CFT

### Boot Log

Screen recording (from flashing the image to startup):

```log

```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

CFT
