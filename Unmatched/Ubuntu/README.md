---
sys: ubuntu
sys_ver: 24.04
sys_var: null

status: basic
last_update: 2024-06-21
---

# Ubuntu 24.04 HiFive Unmatched Test Report

## Test Environment

### Operating System Information

- System Version: Ubuntu 24.04
- Download Link: [https://ubuntu.com/download/risc-v](https://ubuntu.com/download/risc-v) | [TUNA mirror](https://mirror.tuna.tsinghua.edu.cn/ubuntu-cdimage/releases/noble/release/ubuntu-24.04-preinstalled-server-riscv64+unmatched.img.xz)
- Reference Installation Document: [https://wiki.ubuntu.com/RISC-V/SiFive%20HiFive%20Unmatched](https://wiki.ubuntu.com/RISC-V/SiFive%20HiFive%20Unmatched)

### Hardware Information

- HiFive Unmatched Rev A
- A microUSB cable (provided with HiFive Unmatched)
- An ATX power supply
- A 64GB Sandisk Extreme Pro microSD card (UHS-I)

## Installation Steps

### Boot Device Selection

Ensure the DIP switch is set to boot from the microSD card. If you haven't changed it, the factory default setting is to boot from the microSD card.

The dip switch should be set as follows: `MSEL[3:0]=1011`

### Flashing the Image to the microSD Card Using `dd`

Download the image, decompress it, and flash it to the microSD card.

```shell
xzcat ubuntu-24.04-preinstalled-server-riscv64+unmatched.img.xz | sudo dd of=/dev/sdc bs=4M iflag=fullblock status=progress 
```

### Logging into the System

Logging into the system via the onboard serial port (connect using a microUSB cable to another computer).

Default username: `ubuntu`
Default password: `ubuntu`

On initial login, the system will prompt you to change the password.

## Expected Results

The system should boot normally and allow login via the onboard serial port.

## Actual Results

The system booted successfully, and login via the onboard serial port was also successful.

### Boot Log

```log
Welcome to Ubuntu 24.04 LTS (GNU/Linux 6.8.0-31-generic riscv64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/pro

 System information disabled due to load higher than 1.0

Expanded Security Maintenance for Applications is not enabled.

0 updates can be applied immediately.

Enable ESM Apps to receive additional future security updates.
See https://ubuntu.com/esm or run: sudo pro status



The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

To run a command as administrator (user "root"), use "sudo <command>".
See "man sudo_root" for details.

ubuntu@ubuntu:~$ cat /proc/cpuinfo
processor       : 0
hart            : 2
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x20181004
hart isa        : rv64imafdc_zicntr_zicsr_zifencei_zihpm

processor       : 1
hart            : 1
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x20181004
hart isa        : rv64imafdc_zicntr_zicsr_zifencei_zihpm

processor       : 2
hart            : 3
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x20181004
hart isa        : rv64imafdc_zicntr_zicsr_zifencei_zihpm

processor       : 3
hart            : 4
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x20181004
hart isa        : rv64imafdc_zicntr_zicsr_zifencei_zihpm

ubuntu@ubuntu:~$ uname -a
Linux ubuntu 6.8.0-31-generic #31.1-Ubuntu SMP PREEMPT_DYNAMIC Sun Apr 21 01:12:53 UTC 2024 riscv64 riscv64 riscv64 GNU/Linux
ubuntu@ubuntu:~$ cat /etc/os-release
PRETTY_NAME="Ubuntu 24.04 LTS"
NAME="Ubuntu"
VERSION_ID="24.04"
VERSION="24.04 LTS (Noble Numbat)"
VERSION_CODENAME=noble
ID=ubuntu
ID_LIKE=debian
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
UBUNTU_CODENAME=noble
LOGO=ubuntu-logo
ubuntu@ubuntu:~$
```

Screen recording:

[![asciicast](https://asciinema.org/a/gAA0BN4Xo1fR6gBNDaCud8pPY.svg)](https://asciinema.org/a/gAA0BN4Xo1fR6gBNDaCud8pPY)

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
