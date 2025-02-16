---
sys: bianbu
sys_ver: v2.0.4
sys_var: null

status: basic
last_update: 2024-10-24
---

# Bianbu Banana Pi BPI-F3 Test Report

## Test Environment

### System Information

- System version: v2.0.4
- Download Links: https://archive.spacemit.com/image/k1/version/bianbu/v2.0.4/
- Reference Installation Document: https://docs.banana-pi.org/en/BPI-F3/GettingStarted_BPI-F3

### Hardware Information

- Banana Pi BPI-F3
- Power Adapter
- A microSD Card
- A USB to UART Debugger

## Installation Steps

### Flashing the Image (SD Card)

**Please make sure to choose the file ending with `.img.zip`**
After downloading and extracting the image, use `dd` to flash the image to the microSD card.

```bash
unzip bianbu-24.04-minimal-k1-v2.0.4-release-20241205234138.img.zip
sudo dd if=/path/to/bianbu-24.04-minimal-k1-v2.0.4-release-20241205234138.img of=/dev/your-device bs=1M status=progress
```

### Logging into the System

Logging into the system via the serial port.

Default Username: `root`
Default Password: `bianbu`

## Expected Results

The system should boot normally and allow login via the onboard serial port.

## Actual Results

The system booted successfully and login via the onboard serial port was also successful.

### Boot Log

Screen recording (from flashing image to login):
[![asciicast](https://asciinema.org/a/6A0cxWuJLx4MNh7AtRdLJHFpu.svg)](https://asciinema.org/a/6A0cxWuJLx4MNh7AtRdLJHFpu)

```log
Welcome to Bianbu 2.0.4 (GNU/Linux 6.6.36 riscv64)

 * Documentation:  https://bianbu.spacemit.com
 * Support:        https://ticket.spacemit.com

root@k1:~# uname -a
Linux k1 6.6.36 #2.0.4.2 SMP PREEMPT Thu Dec  5 15:02:13 UTC 2024 riscv64 riscv64 riscv64 GNU/Linux

root@k1:~# cat /etc/os-release
PRETTY_NAME="Bianbu 2.0.4"
NAME="Bianbu"
VERSION_ID="2.0.4"
VERSION="2.0.4 (Noble Numbat)"
VERSION_CODENAME=noble
ID=bianbu
ID_LIKE=debian
HOME_URL="https://bianbu.spacemit.com"
SUPPORT_URL="https://bianbu.spacemit.com"
BUG_REPORT_URL="https://ticket.spacemit.com"
PRIVACY_POLICY_URL="https://www.spacemit.com/privacy-policy"
UBUNTU_CODENAME=noble
LOGO=ubuntu-logo

root@k1:~# cat /proc/cpuinfo
processor	: 0
hart		: 0
model name	: Spacemit(R) X60
isa		: rv64imafdcv_zicbom_zicboz_zicntr_zicond_zicsr_zifencei_zihintpause_zihpm_zfh_zfhmin_zca_zcd_zba_zbb_zbc_zbs_zkt_zve32f_zve32x_zve64d_zve64f_zve64x_zvfh_zvfhmin_zvkt_sscofpmf_sstc_svinval_svnapot_svpbmt
mmu		: sv39
mvendorid	: 0x710
marchid		: 0x8000000058000001
mimpid		: 0x1000000049772200

processor	: 1
hart		: 1
model name	: Spacemit(R) X60
isa		: rv64imafdcv_zicbom_zicboz_zicntr_zicond_zicsr_zifencei_zihintpause_zihpm_zfh_zfhmin_zca_zcd_zba_zbb_zbc_zbs_zkt_zve32f_zve32x_zve64d_zve64f_zve64x_zvfh_zvfhmin_zvkt_sscofpmf_sstc_svinval_svnapot_svpbmt
mmu		: sv39
mvendorid	: 0x710
marchid		: 0x8000000058000001
mimpid		: 0x1000000049772200

processor	: 2
hart		: 2
model name	: Spacemit(R) X60
isa		: rv64imafdcv_zicbom_zicboz_zicntr_zicond_zicsr_zifencei_zihintpause_zihpm_zfh_zfhmin_zca_zcd_zba_zbb_zbc_zbs_zkt_zve32f_zve32x_zve64d_zve64f_zve64x_zvfh_zvfhmin_zvkt_sscofpmf_sstc_svinval_svnapot_svpbmt
mmu		: sv39
mvendorid	: 0x710
marchid		: 0x8000000058000001
mimpid		: 0x1000000049772200

processor	: 3
hart		: 3
model name	: Spacemit(R) X60
isa		: rv64imafdcv_zicbom_zicboz_zicntr_zicond_zicsr_zifencei_zihintpause_zihpm_zfh_zfhmin_zca_zcd_zba_zbb_zbc_zbs_zkt_zve32f_zve32x_zve64d_zve64f_zve64x_zvfh_zvfhmin_zvkt_sscofpmf_sstc_svinval_svnapot_svpbmt
mmu		: sv39
mvendorid	: 0x710
marchid		: 0x8000000058000001
mimpid		: 0x1000000049772200

processor	: 4
hart		: 4
model name	: Spacemit(R) X60
isa		: rv64imafdcv_zicbom_zicboz_zicntr_zicond_zicsr_zifencei_zihintpause_zihpm_zfh_zfhmin_zca_zcd_zba_zbb_zbc_zbs_zkt_zve32f_zve32x_zve64d_zve64f_zve64x_zvfh_zvfhmin_zvkt_sscofpmf_sstc_svinval_svnapot_svpbmt
mmu		: sv39
mvendorid	: 0x710
marchid		: 0x8000000058000001
mimpid		: 0x1000000049772200

processor	: 5
hart		: 5
model name	: Spacemit(R) X60
isa		: rv64imafdcv_zicbom_zicboz_zicntr_zicond_zicsr_zifencei_zihintpause_zihpm_zfh_zfhmin_zca_zcd_zba_zbb_zbc_zbs_zkt_zve32f_zve32x_zve64d_zve64f_zve64x_zvfh_zvfhmin_zvkt_sscofpmf_sstc_svinval_svnapot_svpbmt
mmu		: sv39
mvendorid	: 0x710
marchid		: 0x8000000058000001
mimpid		: 0x1000000049772200

processor	: 6
hart		: 6
model name	: Spacemit(R) X60
isa		: rv64imafdcv_zicbom_zicboz_zicntr_zicond_zicsr_zifencei_zihintpause_zihpm_zfh_zfhmin_zca_zcd_zba_zbb_zbc_zbs_zkt_zve32f_zve32x_zve64d_zve64f_zve64x_zvfh_zvfhmin_zvkt_sscofpmf_sstc_svinval_svnapot_svpbmt
mmu		: sv39
mvendorid	: 0x710
marchid		: 0x8000000058000001
mimpid		: 0x1000000049772200

processor	: 7
hart		: 7
model name	: Spacemit(R) X60
isa		: rv64imafdcv_zicbom_zicboz_zicntr_zicond_zicsr_zifencei_zihintpause_zihpm_zfh_zfhmin_zca_zcd_zba_zbb_zbc_zbs_zkt_zve32f_zve32x_zve64d_zve64f_zve64x_zvfh_zvfhmin_zvkt_sscofpmf_sstc_svinval_svnapot_svpbmt
mmu		: sv39
mvendorid	: 0x710
marchid		: 0x8000000058000001
mimpid		: 0x1000000049772200
```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
