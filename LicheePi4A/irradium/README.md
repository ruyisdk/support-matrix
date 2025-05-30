---
sys: irradium
sys_ver: "3.8"
sys_var: null

status: CFT
last_update: CFT
---

# irradium LicheePi 4A Test Report

## Test Environment

### System Information

- System Version: irradium 3.8
- Download Link:
  - image: <https://mirror.serverion.com/irradium/images/lichee_pi_4a/irradium-3.8-riscv64-core-lichee_pi_4a-6.6.90-build-20250510.img.zst>
  - boot: <https://mirror.serverion.com/irradium/images/lichee_pi_4a/boot-20250510.tar.xz>
- Reference Installation Document: <https://mirror.serverion.com/irradium/images/lichee_pi_4a/README.TXT>

### Hardware Information

- Lichee Pi 4A (16G RAM + 128G eMMC)
- Power Adapter
- A USB to UART Debugger

## Installation Steps

### Flashing the Bootloader

Extract the installation suite.
Navigate to the fastboot tool directory.
Flash the u-boot.

```bash
zstd -d irradium-3.8-riscv64-core-lichee_pi_4a-6.6.90-build-20250510.img.zst
xz -d boot-20250510.tar.xz
sudo fastboot flash ram u-boot-with-spl-lpi4a(-16g).bin
sudo fastboot reboot
sudo fastboot flash uboot u-boot-with-spl-lpi4a(-16g).bin
```

### Flashing the Image

Flash the root partition into the eMMC.

```bash
sudo fastboot flash root irradium-3.8-riscv64-core-lichee_pi_4a-6.6.90-build-20250510.img
```

### Logging into the System

Logging into the system via serial console.

Default username: `root` (automatic login)

Without password

## Expected Results

The system should boot successfully, allowing login via the onboard serial console.

## Actual Results

The system booted up correctly, and login via the onboard serial console was successful.

### Boot Log

```log
CFT
```

### Common Issue

In case of desktop freeze, try switching from wayland.

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

CFT
