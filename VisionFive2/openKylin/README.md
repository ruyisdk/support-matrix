---
sys: openkylin
sys_ver: 2.0-SP1
sys_var: null

status: good
last_update: 2025-01-15
---

# openKylin 2.0 SP1 VisionFive 2 Test Report

## Test Environment

### Operating System Information

- System Version: openKylin 2.0 SP1
- Download Link: https://www.openkylin.top/downloads/index-en.html
- Reference Installation Document: https://docs.openkylin.top/zh/01_%E5%AE%89%E8%A3%85%E5%8D%87%E7%BA%A7%E6%8C%87%E5%8D%97/%E5%9C%A8riscv%E4%B8%8A%E5%AE%89%E8%A3%85/%E5%9C%A8VisionFive2%E4%B8%8A%E5%AE%89%E8%A3%85openKylin (Chinese)
### Hardware Information

- StarFive VisionFive 2
- A USB Power Adapter
- A USB-A to C or C to C Cable
- A microSD Card
- A USB to UART Debugger (e.g., CH340, CH341, FT2232, etc.)
- Three Dupont Wires

## Installation Steps

### Unzipping and Flashing Image to microSD Card

Assume `/dev/sdc` is the storage card.

```bash
xz -d openKylin-Embedded-V2.0-SP1-visionfive2-riscv64.img.xz
sudo dd if=openKylin-Embedded-V2.0-SP1-visionfive2-riscv64.img of=/dev/sdc bs=1M status=progress
```

### Boot Mode Selection

StarFive VisionFive 2 offers multiple boot modes, which can be configured via the onboard dip switch before powering on; the board itself has silkscreen labels.

To boot the openKylin image, select the 1-bit QSPI Nor Flash mode (i.e., `RGPIO_0 = 0`, `RGPIO_1 = 0`). Note that this mode may require updating the firmware within the Flash beforehand. If the boot fails, please refer to the official documentation for firmware upgrade instructions: [Updating SPL and U-Boot](https://doc.rvspace.org/VisionFive2/Quick_Start_Guide/VisionFive2_QSG/spl_u_boot_0.html)

### Logging into the System

Logging into the system via the serial port.

Default username: `openkylin` 
Default password: `openkylin`

## Expected Results

The system should boot normally and allow login through the graphical interface.

## Actual Results

The system booted successfully and login through the graphical interface was successful.

### Boot Log

```log

```

![login](./image.png)

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test Successful.
