---
sys: ubuntu
sys_ver: 24.10-beta
sys_var: null

status: basic
last_update: 2024-06-21
---

# Ubuntu 24.10-beta D1 Test Report

## Test Environment

### Operating System Information

- System Version: Ubuntu 24.10 beta
- Download Link: https://ubuntu.com/download/risc-v
    - Or from mirror sites: [Nezha](https://mirror.tuna.tsinghua.edu.cn/ubuntu-cdimage/releases/24.10/beta/ubuntu-24.10-beta-preinstalled-server-riscv64%2Bnezha.img.xz) | [Lichee RV](https://mirror.tuna.tsinghua.edu.cn/ubuntu-cdimage/releases/24.10/beta/ubuntu-24.10-beta-preinstalled-server-riscv64%2Blicheerv.img.xz)
- Reference Installation Document: https://wiki.ubuntu.com/RISC-V/LicheeRV

### Hardware Information

- AWOL Nezha D1 / Sipeed Lichee RV Dock
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

New password: 
Retype new password: 
uname -a && echo pFANgBWl 
Welcome to Ubuntu Oracular Oriole (development branch) (GNU/Linux 6.8.0-31-generic riscv64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/pro

 System information as of Thu Sep 19 03:13:06 UTC 2024

  System load:    1.15      Processes:             27
  Usage of /home: unknown   Users logged in:       0
  Memory usage:   5%        IPv4 address for eth0: 10.10.10.2
  Swap usage:     0%

0 updates can be applied immediately.



The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

To run a command as administrator (user "root"), use "sudo <command>".
See "man sudo_root" for details.

ubuntu@ubuntu:~$ uname -a && echo pFANgBWl 

Linux ubuntu 6.8.0-31-generic #31.1-Ubuntu SMP PREEMPT_DYNAMIC Sun Apr 21 01:12:53 UTC 2024 riscv64 riscv64 riscv64 GNU/Linux
pFANgBWl
ubuntu@ubuntu:~$ cat /etc/os-release && echo 6wiXKfwS 

PRETTY_NAME="Ubuntu Oracular Oriole (development branch)"
NAME="Ubuntu"
VERSION_ID="24.10"
VERSION="24.10 (Oracular Oriole)"
VERSION_CODENAME=oracular
ID=ubuntu
ID_LIKE=debian
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
UBUNTU_CODENAME=oracular
LOGO=ubuntu-logo
6wiXKfwS
ubuntu@ubuntu:~$ cat /proc/cpuinfo && echo zaKdnCxp 

processor	: 0
hart		: 0
isa		: rv64imafdc_zicntr_zicsr_zifencei_zihpm
mmu		: sv39
uarch		: thead,c906
mvendorid	: 0x5b7
marchid		: 0x0
mimpid		: 0x0
hart isa	: rv64imafdc_zicntr_zicsr_zifencei_zihpm

zaKdnCxp
ubuntu@ubuntu:~$ 
```

Screen recording (from flashing the image to logging into the system):

[![asciicast](https://asciinema.org/a/r9ivCdzlZAGbyuz1SjpnZEJx3.svg)](https://asciinema.org/a/r9ivCdzlZAGbyuz1SjpnZEJx3)

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
