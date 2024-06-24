# Bianbu Banana Pi BPI-F3 Test Report

## Test Environment

### System Information

- Download Links:
  - Baidu Netdisk: https://pan.baidu.com/s/15owwUEjIU_i26cI1iigAew?pwd=8888 (pincode: 8888)
  - Google Drive: https://drive.google.com/drive/folders/1LQoioz6N5YQpSOxY47OmetnPX4yggtT0?usp=sharing
- Download Links (Desktop Version):
  - Baidu Netdisk: https://pan.baidu.com/s/1zvFkX92f5gpZdKjP-vGJvA?pwd=8888 (pincode: 8888)
  - Google Drive: https://drive.google.com/drive/folders/1kCHiMwjnhvZaRBy5vkj6UlPeAlpRQ14P?usp=sharing
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
unzip Bianbu-23.10-desktop-k1-v1.0rc1-release-20240429194149.img
sudo dd if=/path/to/Bianbu-23.10-desktop-k1-v1.0rc1-release-20240429194149.img of=/dev/your-device bs=1M status=progress
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
[![asciicast](https://asciinema.org/a/TFRjqFjOEIHc38Wha93bw0ti8.svg)](https://asciinema.org/a/TFRjqFjOEIHc38Wha93bw0ti8)

```log
Bianbu 1.0rc1 k1 ttyS0k1 login: root
密码： 
Welcome to Bianbu 1.0rc1 (GNU/Linux 6.1.15 riscv64)

 * Documentation:  coming soon
 * Management:     coming soon
 * Support:        coming soon

0 updates can be applied immediately.


The programs included with the Bianbu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Bianbu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

root@k1:~# cat /etc/os-release 
PRETTY_NAME="Bianbu 1.0rc1"
NAME="Bianbu"
VERSION_ID="1.0rc1"
VERSION="1.0rc1 (Mantic Minotaur)"
VERSION_CODENAME=mantic
ID=bianbu
ID_LIKE=debian
HOME_URL="coming soon"
SUPPORT_URL="coming soon"
BUG_REPORT_URL="coming soon"
PRIVACY_POLICY_URL="coming soon"
UBUNTU_CODENAME=mantic
LOGO=ubuntu-logo
root@k1:~# uname -a
Linux k1 6.1.15 #1.0~rc1 SMP PREEMPT Mon Apr 29 09:05:59 UTC 2024 riscv64 riscv64 riscv64 GNU/Linux
root@k1:~# 

```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
