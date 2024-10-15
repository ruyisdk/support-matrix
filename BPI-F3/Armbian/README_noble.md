---
sys: armbian
sys_ver: 6.1.15
sys_var: noble

status: basic
last_update: 2024-09-13
---

# Armbian Banana Pi BPI-F3 Test Report

## Test Environment

### System Information

- Download Links: https://mirrors.tuna.tsinghua.edu.cn/armbian-releases/bananapif3/archive/Armbian_24.8.1_Bananapif3_noble_legacy_6.1.15_minimal.img.xz
- Reference Installation Document: https://docs.banana-pi.org/en/BPI-F3/GettingStarted_BPI-F3

### Hardware Information

- Banana Pi BPI-F3
- Power Adapter
- A microSD Card
- A USB to UART Debugger

## Installation Steps

### Flashing the Image (SD Card)

After downloading and extracting the image, use `dd` to flash the image to the microSD card.

```bash
xz -kd Armbian_24.8.1_Bananapif3_noble_legacy_6.1.15_minimal.img.xz
sudo dd if=/path/to/Armbian_24.8.1_Bananapif3_noble_legacy_6.1.15_minimal.img.xz of=/dev/your-device bs=1M status=progress
```

### Logging into the System

Logging into the system via the serial port.

On the first boot, create a user.

## Expected Results

The system should boot up normally and allow login through the onboard serial port.

## Actual Results

The system booted successfully and login through the onboard serial port was also successful.

### Boot Log

Screen recording (From flashing image to system login):
[![asciicast](https://asciinema.org/a/aZN2jn6DdEN0clVNhLDFG5Ann.svg)](https://asciinema.org/a/aZN2jn6DdEN0clVNhLDFG5Ann)

```log
uname -a&& echo zE5YXe0d 
uname -a&& echo zE5YXe0d 

Linux bananapif3 6.1.15-legacy-spacemit #1 SMP Fri Aug  2 07:47:59 UTC 2024 riscv64 riscv64 riscv64 GNU/Linux
zE5YXe0d
root@bananapif3:~# cat /etc/os-release&& echo Sqndhdce 
cat /etc/os-release&& echo Sqndhdce 

PRETTY_NAME="Armbian 24.8.1 noble"
NAME="Ubuntu"
VERSION_ID="24.04"
VERSION="24.04 LTS (Noble Numbat)"
VERSION_CODENAME=noble
ID=ubuntu
ID_LIKE=debian
HOME_URL="https://github.com/armbian/build"
SUPPORT_URL="https://community.armbian.com/"
BUG_REPORT_URL="https://github.com/armbian/community/issues"
PRIVACY_POLICY_URL="https://duckduckgo.com/"
UBUNTU_CODENAME=noble
LOGO="armbian-logo"
ARMBIAN_PRETTY_NAME="Armbian 24.8.1 noble"
Sqndhdce
root@bananapif3:~# cat /proc/cpuinfo&& echo W8tQXFQR 
cat /proc/cpuinfo&& echo W8tQXFQR 

processor	: 0
hart		: 0
model name	: Spacemit(R) X60
isa		: rv64imafdcv_sscofpmf_sstc_svpbmt_zicbom_zicboz_zicbop_zihintpause
mmu		: sv39
mvendorid	: 0x710
marchid		: 0x8000000058000001
mimpid		: 0x1000000049772200

processor	: 1
hart		: 1
model name	: Spacemit(R) X60
isa		: rv64imafdcv_sscofpmf_sstc_svpbmt_zicbom_zicboz_zicbop_zihintpause
mmu		: sv39
mvendorid	: 0x710
marchid		: 0x8000000058000001
mimpid		: 0x1000000049772200

processor	: 2
hart		: 2
model name	: Spacemit(R) X60
isa		: rv64imafdcv_sscofpmf_sstc_svpbmt_zicbom_zicboz_zicbop_zihintpause
mmu		: sv39
mvendorid	: 0x710
marchid		: 0x8000000058000001
mimpid		: 0x1000000049772200

processor	: 3
hart		: 3
model name	: Spacemit(R) X60
isa		: rv64imafdcv_sscofpmf_sstc_svpbmt_zicbom_zicboz_zicbop_zihintpause
mmu		: sv39
mvendorid	: 0x710
marchid		: 0x8000000058000001
mimpid		: 0x1000000049772200

processor	: 4
hart		: 4
model name	: Spacemit(R) X60
isa		: rv64imafdcv_sscofpmf_sstc_svpbmt_zicbom_zicboz_zicbop_zihintpause
mmu		: sv39
mvendorid	: 0x710
marchid		: 0x8000000058000001
mimpid		: 0x1000000049772200

processor	: 5
hart		: 5
model name	: Spacemit(R) X60
isa		: rv64imafdcv_sscofpmf_sstc_svpbmt_zicbom_zicboz_zicbop_zihintpause
mmu		: sv39
mvendorid	: 0x710
marchid		: 0x8000000058000001
mimpid		: 0x1000000049772200

processor	: 6
hart		: 6
model name	: Spacemit(R) X60
isa		: rv64imafdcv_sscofpmf_sstc_svpbmt_zicbom_zicboz_zicbop_zihintpause
mmu		: sv39
mvendorid	: 0x710
marchid		: 0x8000000058000001
mimpid		: 0x1000000049772200

processor	: 7
hart		: 7
model name	: Spacemit(R) X60
isa		: rv64imafdcv_sscofpmf_sstc_svpbmt_zicbom_zicboz_zicbop_zihintpause
mmu		: sv39
mvendorid	: 0x710
marchid		: 0x8000000058000001
mimpid		: 0x1000000049772200

W8tQXFQR
root@bananapif3:~# 

```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
