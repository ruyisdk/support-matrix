---
sys: ubuntu
sys_ver: "25.04"
sys_var: null

status: basic
last_update: 2025-05-20
---

# Ubuntu 25.04 LicheeRV Dock Test Report

## Test Environment

### Operating System Information

- System Version: Ubuntu 25.04
- Download Link: https://ubuntu.com/download/risc-v
- Reference Installation Document: https://canonical-ubuntu-boards.readthedocs-hosted.com/en/latest/how-to/sipeed-licheerv-dock/

### Hardware Information

- Sipeed Lichee RV Dock
- A USB-A Power Adapter
- A USB-A to C Cable
- A microSD Card
- A USB to UART Debugger (e.g., CH340, CH341, FT2232, etc.)
- Three DuPont Wires

## Installation Steps

### Flashing Image to microSD Card

Use `dd` to flash the image to the microSD card.

### Logging into the System

Logging into the system via the serial port.

Default Username: `ubuntu`
Default Password: `ubuntu`

On first login, the system will prompt you to change the password.

## Expected Results

The system should boot normally and allow login via the onboard serial port.

## Actual Results

The system booted successfully and login via the onboard serial port was also successful.

### Boot Log

```log

Ubuntu 25.04 ubuntu ttyS0

ubuntu login: ubuntu
Password: 
You are required to change your password immediately (administrator enforced).
Changing password for ubuntu.
Current password: 
New password: 
Retype new password: 
Welcome to Ubuntu 25.04 (GNU/Linux 6.14.0-13-generic riscv64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/pro

 System information as of Tue Apr 15 02:53:44 UTC 2025

  System load:    1.01      Processes:             27
  Usage of /home: unknown   Users logged in:       0
  Memory usage:   2%        IPv4 address for eth0: 10.10.10.2
  Swap usage:     0%


0 updates can be applied immediately.



The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

To run a command as administrator (user "root"), use "sudo <command>".
See "man sudo_root" for details.

ubuntu@ubuntu:~$ cat /etc/os-release 
PRETTY_NAME="Ubuntu 25.04"
NAME="Ubuntu"
VERSION_ID="25.04"
VERSION="25.04 (Plucky Puffin)"
VERSION_CODENAME=plucky
ID=ubuntu
ID_LIKE=debian
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
UBUNTU_CODENAME=plucky
LOGO=ubuntu-logo
ubuntu@ubuntu:~$ uname -a
Linux ubuntu 6.14.0-13-generic #13.2-Ubuntu SMP PREEMPT_DYNAMIC Sun Apr  6 05:26:54 UTC 2025 riscv64 riscv64 riscv64 GNU/Linux
ubuntu@ubuntu:~$ cat /proc/cpuinfo 
processor	: 0
hart		: 0
isa		: rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd
mmu		: sv39
uarch		: thead,c906
mvendorid	: 0x5b7
marchid		: 0x0
mimpid		: 0x0
hart isa	: rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd

ubuntu@ubuntu:~$ 
```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
