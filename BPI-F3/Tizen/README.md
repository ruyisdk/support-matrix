---
sys: tizen
sys_ver: null
sys_var: null

status: cft
last_update: 2025-09-18
---

# Tizen Snapshot Banana Pi BPI-F3 Test Report

## Test Environment

### System Information

- System Version: Tizen-Unified-X riscv64 Snapshot 20250917
- Download Link:
  - boot image: http://download.tizen.org/snapshots/TIZEN/Tizen/Tizen-Unified-X/reference/images/standard/tizen-boot-riscv64-bpif3/tizen-unified-x_20250918.035403_tizen-boot-riscv64-bpif3.tar.gz
  - platform image: http://download.tizen.org/snapshots/TIZEN/Tizen/Tizen-Unified-X/reference/images/standard/tizen-headless-riscv64/tizen-unified-x_20250918.035403_tizen-headless-riscv64.tar.gz
- Reference Installation Document: https://docs.tizen.org/platform/developing/flashing-rpi/

### Hardware Information

- Banana Pi BPI-F3
- Power Adapter
- A microSD card
- A USB to UART Debugger

## Installation Steps

### Flashing the Image

Install `pv`:

```bash
sudo apt-get install pv
```

Fetch the SD card flashing script:

```bash
git clone git://review.tizen.org/git/platform/kernel/tizen-fusing-scripts -b tizen
cd tizen-fusing-scripts
```

Download the `boot` and `platform` images (do NOT unzip them):

```bash
wget http://download.tizen.org/snapshots/TIZEN/Tizen/Tizen-Unified-X/reference/images/standard/tizen-boot-riscv64-bpif3/tizen-unified-x_20250918.035403_tizen-boot-riscv64-bpif3.tar.gz
wget http://download.tizen.org/snapshots/TIZEN/Tizen/Tizen-Unified-X/reference/images/standard/tizen-headless-riscv64/tizen-unified-x_20250918.035403_tizen-headless-riscv64.tar.gz
# or use headed image instead of headless:
# wget http://download.tizen.org/snapshots/TIZEN/Tizen/Tizen-Unified-X/reference/images/standard/tizen-headed-riscv64/tizen-unified-x_20250918.035403_tizen-headed-riscv64.tar.gz
```

Insert your SD card and run the script: (replace `/dev/mmcblk0` with your SD card device)
```bash
sudo ./tizen-fusing-scripts/scripts/sd_fusing.py -d /dev/mmcblk0 -t bpif3 --format
sudo ./tizen-fusing-scripts/scripts/sd_fusing.py -d /dev/mmcblk0 -b tizen-unified-x_20250918.035403_tizen-boot-riscv64-bpif3.tar.gz tizen-unified-x_20250917.211322_tizen-headless-riscv64.tar.gz  -t bpif3
```

### Logging into the System

Login to the system via the serial port.

Default Username: `root`

Default Password: `tizen`

## Expected Results

The system boots up normally and allows login through the onboard serial port.

## Actual Results

CFT

### Boot Log

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

CFT
