---
sys: ubuntu
sys_ver: 24.10
sys_var: LTS

status: basic
last_update: 2024-10-21
---

# Ubuntu 24.04.1 LTS VisionFive 2 Version Test Report

## Test Environment

### Operating System Information

- System Version: Ubuntu 24.04.1 LTS
- Download Link: https://ubuntu.com/download/risc-v
- Reference Installation Document: https://wiki.ubuntu.com/RISC-V/StarFive%20VisionFive%202

### Hardware Information

- StarFive VisionFive 2
- A USB power adapter
- A USB-A to C or C to C cable
- A microSD card
- A USB to UART debugger (e.g., CH340, CH341, FT2232, etc.)
- Three Dupont wires

## Installation Steps

### Decompress and Flash Image to microSD Card

```bash
xzcat ubuntu-24.04.1-preinstalled-server-riscv64+visionfive2.img.xz | sudo dd bs=1M conv=fsync of=/dev/<your-device>
```

### Boot Mode Selection

The StarFive VisionFive 2 offers multiple boot modes, configurable via onboard dip switches prior to powering on. Refer to the StarFive [official documentation](https://doc.rvspace.org/VisionFive2/Quick_Start_Guide/VisionFive2_SDK_QSG/boot_mode_settings.html).

The board also has silk-screen labels for guidance.

To boot the Ubuntu image, select the SDIO3.0 mode (i.e., `RGPIO_0 = 1`, `RGPIO_1 = 0`).

### First boot

Insert the SD card and power on the board.Enter the U-Boot console by pressing enter when seeing the "Hit any key to stop autoboot:" message to reset the environment:

```
env default -f -a
env save
```

Power cycle the board. When booting the first time wait until you see an output line confirming that cloud-init has finished. Cloud init is responsible for generating the SSH keys and setting the default password. The line to wait for will look similar to
``` log
[   55.765266] cloud-init[1067]: Cloud-init v. 24.1.3-0ubuntu3.3 finished at Thu, 08 Aug 2024 14:51:52 +0000. Datasource DataSourceNoCloud [seed=/var/lib/cloud/seed/nocloud-net][dsmode=net].  Up 55.74 seconds
```

### Logging into the System

Login to the system via the serial port.

Default username: `ubuntu`
Default password: `ubuntu`

Upon first login, you will be prompted to change the default password.

## Expected Results

The system should boot normally and allow login via the serial port.

## Actual Results

The system booted normally, and login via the serial port was successful.

### Boot log 

```log 

Ubuntu 24.04.1 LTS ubuntu ttyS0

ubuntu login: ubuntu
Password: 
You are required to change your password immediately (administrator enforced).
Changing password for ubuntu.
Current password: 
New password: 
Retype new password: 
Welcome to Ubuntu 24.04.1 LTS (GNU/Linux 6.8.0-41-generic riscv64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/pro

 System information as of Mon Oct 21 05:36:22 UTC 2024

  System load:  0.41              Temperature:           48.3 C
  Usage of /:   7.5% of 28.02GB   Processes:             130
  Memory usage: 5%                Users logged in:       0
  Swap usage:   0%                IPv4 address for end0: 192.168.31.89

Expanded Security Maintenance for Applications is not enabled.

0 updates can be applied immediately.

Enable ESM Apps to receive additional future security updates.
See https://ubuntu.com/esm or run: sudo pro status


The list of available updates is more than a week old.
To check for new updates run: sudo apt update


The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

To run a command as administrator (user "root"), use "sudo <command>".
See "man sudo_root" for details.

ubuntu@ubuntu:~$ cat /etc/os-release 
PRETTY_NAME="Ubuntu 24.04.1 LTS"
NAME="Ubuntu"
VERSION_ID="24.04"
VERSION="24.04.1 LTS (Noble Numbat)"
VERSION_CODENAME=noble
ID=ubuntu
ID_LIKE=debian
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
UBUNTU_CODENAME=noble
LOGO=ubuntu-logo
ubuntu@ubuntu:~$ uname -a
Linux ubuntu 6.8.0-41-generic #41.1-Ubuntu SMP PREEMPT_DYNAMIC Tue Aug 13 09:58:43 UTC 2024 riscv64 riscv64 riscv64 GNU/Linux

```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
