---
sys: openkylin
sys_ver: 2.0
sys_var: null

status: cfh
last_update: 2025-04-05
---

# openKylin Milk-V Jupiter Test report

## Test Environment

### System Information

- System version: openKylin 2.0-SP1
- Download link: [https://www.openkylin.top/downloads/index-cn.html](https://www.openkylin.top/downloads/index-cn.html)
- Reference installation document: [https://docs.openkylin.top/zh/01_%E5%AE%89%E8%A3%85%E5%8D%87%E7%BA%A7%E6%8C%87%E5%8D%97/%E5%9C%A8riscv%E4%B8%8A%E5%AE%89%E8%A3%85/%E5%9C%A8LicheePi4A%E4%B8%8A%E5%AE%89%E8%A3%85openKylin](https://docs.openkylin.top/zh/01_%E5%AE%89%E8%A3%85%E5%8D%87%E7%BA%A7%E6%8C%87%E5%8D%97/%E5%9C%A8riscv%E4%B8%8A%E5%AE%89%E8%A3%85/%E5%9C%A8LicheePi4A%E4%B8%8A%E5%AE%89%E8%A3%85openKylin)

### Hardware Information

- Milk-V Jupiter Board (Key Stone K1/M1, 4G/8G/16G)
    -  M1 + 16G is tested in this report
- DC 5.5*2.5mm 12V PSU / USB PD (12V required) / ATX PSU
    - 12V 3A is recommended for DC PSU, if more power is needed (e.g. using PCI-E peripherals) then ATX PSU is preferred
    - USB Type-C port isn't available when flashing using `titanflasher` or `fastboot`, external DC/ATX PSU is required
    - In this test report we're using a 12V 3A DC power supply
- A microSD card, or eMMC module, or NVMe SSD
    - Boot priority: `microSD > NVMe SSD > eMMC`
    - When booting from SD, the board won't go through SPI Flash
    - If either NVMe SSD or eMMC module is installed, `titanflasher` will only flash U-Boot to SPI Flash
    - In this test report we're using NVMe SSD, model: Samsung PM961 128GB
- A USB to UART debugger
    - In this test report we're using CH343P
- USB Type-C cables (depends on your usage, at least one for flashing OS image)
- USB keyboard/mouse, HDMI cable, HDMI monitor/capture card (if using `desktop` variant)

## Installation Steps

### Flash Image to microSD Card

```bash
tar -xvf openKylin-Embedded-V2.0-SP1-spacemit-k1-riscv64.img.tar.xz
sudo dd if=openKylin-Embedded-V2.0-SP1-spacemit-k1-riscv64.img of=/dev/sda bs=4M status=progress
```

For Windows users, try Rufus.

### Logging into the System

Logging into the system via the serial port.

Default Username: `openkylin`
Default Password: `openkylin`

## Expected Results

The system should boot normally and allow login via the onboard serial port.

The `desktop` image should have working HDMI output, and the user can complete the quick start guide, setup account and log into the desktop.

## Actual Results

Boot failed resulting in something like a bootloop. This repeats for several times until the system enters the initranfs shell. rootfs also failed to mount.

### Boot Log

[![asciicast](https://asciinema.org/a/CzVNtF5admSUNFr177hLNFYTr.svg)](https://asciinema.org/a/CzVNtF5admSUNFr177hLNFYTr)

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test failed.