---
sys: ubuntu
sys_ver: "24.10"
sys_var: null

status: basic
last_update: 2025-03-03
---

# Ubuntu MangoPi MQ Pro Test Report

## Test Environment

### Operating System Information

- Download Link: https://cdimage.ubuntu.com/releases/24.10/release/ubuntu-24.10-preinstalled-server-riscv64+nezha.img.xz
- Reference Installation Document: [MangoPi MQ Pro Guide](https://mangopi.org/mqpro)

### Hardware Information

- MangoPi MQ Pro
- Power Adapter
- A microSD card
- A USB to UART Debugger

## Installation Steps

### Flashing Image

Use `xz` to decompress the image.
Use `dd` to flash the image to the microSD card.

```bash
xz -kd /path/to/ubuntu-24.10-preinstalled-server-riscv64+nezha.img.xz
sudo dd if=/path/to/ubuntu-24.10-preinstalled-server-riscv64+nezha.img of=/dev/your_device bs=1M status=progress
```

### Logging into the System

Logging into the system via the serial port.

Default Username: `ubuntu`
Default Password: `ubuntu`

## Expected Results

The system should boot normally and allow login via the onboard serial port.

## Actual Results

The system booted successfully and login via the onboard serial port was also successful.

### Boot Log

```log
Ubuntu 24.10 ubuntu ttyS0

ubuntu login: ubuntu
Password: 
You are required to change your password immediately (administrator enforced).
Changing password for ubuntu.
Current password: 
New password: 
Retype new password: 
Welcome to Ubuntu 24.10 (GNU/Linux 6.11.0-8-generic riscv64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/pro

 System information as of Mon Oct  7 18:11:55 UTC 2024

  System load:    1.12      Processes:             26
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

ubuntu@ubuntu:~$ uname -a
Linux ubuntu 6.11.0-8-generic #8.1-Ubuntu SMP PREEMPT_DYNAMIC Tue Oct  1 11:40:56 UTC 2024 riscv64 riscv64 riscv64 GNU/Linux
ubuntu@ubuntu:~$ cat /etc/os-release 
PRETTY_NAME="Ubuntu 24.10"
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
ubuntu@ubuntu:~$ lscpu
Architecture:           riscv64
  Byte Order:           Little Endian
CPU(s):                 1
  On-line CPU(s) list:  0
Vendor ID:              0x5b7
  Model name:           thead,c906
    CPU family:         0x0
    Model:              0x0
    Thread(s) per core: 1
    Core(s) per socket: 1
    Socket(s):          1
    CPU(s) scaling MHz: 100%
    CPU max MHz:        1008.0000
    CPU min MHz:        408.0000
Caches (sum of all):    
  L1d:                  32 KiB (1 instance)
  L1i:                  32 KiB (1 instance)
NUMA:                   
  NUMA node(s):         1
  NUMA node0 CPU(s):    0
ubuntu@ubuntu:~$ 

```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.