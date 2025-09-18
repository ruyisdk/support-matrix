---
sys: tizen
sys_ver: null
sys_var: null

status: basic
last_update: 2025-09-18
---

# Tizen Snapshot VisionFive 2 Test Report

## Test Environment

### System Information

- System Version: Tizen-Unified-X riscv64 Snapshot 20250917
- Download Link:
  - boot image: http://download.tizen.org/snapshots/TIZEN/Tizen/Tizen-Unified-X/reference/images/standard/tizen-boot-riscv64-vf2/tizen-unified-x_20250917.211322_tizen-boot-riscv64-vf2.tar.gz
  - platform image: http://download.tizen.org/snapshots/TIZEN/Tizen/Tizen-Unified-X/reference/images/standard/tizen-headless-riscv64/tizen-unified-x_20250918.035403_tizen-headless-riscv64.tar.gz
- Reference Installation Document: https://docs.tizen.org/platform/developing/flashing-rpi/

### Hardware Information

- StarFive VisionFive2
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
wget http://download.tizen.org/snapshots/TIZEN/Tizen/Tizen-Unified-X/reference/images/standard/tizen-boot-riscv64-vf2/tizen-unified-x_20250917.211322_tizen-boot-riscv64-vf2.tar.gz
wget http://download.tizen.org/snapshots/TIZEN/Tizen/Tizen-Unified-X/reference/images/standard/tizen-headless-riscv64/tizen-unified-x_20250918.035403_tizen-headless-riscv64.tar.gz
# or use headed image instead of headless:
# wget http://download.tizen.org/snapshots/TIZEN/Tizen/Tizen-Unified-X/reference/images/standard/tizen-headed-riscv64/tizen-unified-x_20250918.035403_tizen-headed-riscv64.tar.gz

```

Insert your SD card and run the script: (replace `/dev/mmcblk0` with your SD card device)
```bash
sudo ./tizen-fusing-scripts/scripts/sd_fusing.py -d /dev/mmcblk0 -t vf2 --format
sudo ./tizen-fusing-scripts/scripts/sd_fusing.py -d /dev/mmcblk0 -b tizen-unified-x_20250917.211322_tizen-boot-riscv64-vf2.tar.gz  tizen-unified-x_20250917.211322_tizen-headless-riscv64.tar.gz  -t vf2
```

### Boot Mode Selection

The StarFive VisionFive 2 offers multiple boot modes, configurable via onboard dip switches prior to powering on. Refer to the StarFive [official documentation](https://doc.rvspace.org/VisionFive2/Quick_Start_Guide/VisionFive2_SDK_QSG/boot_mode_settings.html).

The board also has silk-screen labels for guidance.

To boot Tizen, select the SDIO3.0 mode (i.e., `RGPIO_0 = 1`, `RGPIO_1 = 0`).

### Logging into the System

Login to the system via the serial port.

Default Username: `root`

Default Password: `tizen`

## Expected Results

The system boots up normally and allows login through the onboard serial port.

## Actual Results

The system booted up successfully and login through the onboard serial port was successful.

### Boot Log

```log
[   20.335661] file system registered
[   20.374657] read descriptors
[   20.390855] read strings
[   20.439559] read descriptors
[   20.445429] read strings

localhost login: root
Password:
[   78.562452] kauditd_printk_skb: 32 callbacks suppressed
[   78.562461] audit: type=1006 audit(978307277.740:16): pid=396 uid=0 subj=User::Shell old-auid=4294967295 auid=0 tty=ttyS0 old-ses=4294967295 ses=3 res=1
Welcome to Tizen[   78.581412] audit: type=1300 audit(978307277.740:16): arch=c00000f3 syscall=64 success=yes exit=1 a0=4 a1=3fd51276e0 a2=1 a3=0 items=0 ppid=1 pid=396 auid=0 uid=0 gid=0 euid=0 suid=0 fsuid=0 egid=0 sgid=0 fsgid=0 tty=ttyS0 ses=3 comm="login" exe="/usr/bin/login" subj=User::Shell key=(null)

[   78.608409] audit: type=1327 audit(978307277.740:16): proctitle=2F62696E2F6C6F67696E002D70002D2D
root:~> cat /etc/os-release
NAME=Tizen
VERSION="10.0.0 (Tizen10.0/Unified)"
ID=tizen
VERSION_ID=10.0.0
PRETTY_NAME="Tizen 10.0.0 (Tizen10.0/Unified)"
ANSI_COLOR="0;36"
CPE_NAME="cpe:/o:tizen:tizen:10.0.0"
BUILD_ID=tizen-unified-x_20250917.211322_tizen-headless-riscv64
root:~> uname -a
Linux localhost 6.6.17-riscv-visionfive2 #1 SMP Wed Sep 17 22:13:06 UTC 2025 riscv64 GNU/Linux
```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
