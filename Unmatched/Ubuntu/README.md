---
sys: ubuntu
sys_ver: "24.10"
sys_var: null

status: basic
last_update: 2025-04-11
---

# Ubuntu 24.10 HiFive Unmatched Test Report

## Test Environment

### Operating System Information

- System Version: Ubuntu 24.10
- Download Link: [https://ubuntu.com/download/risc-v](https://ubuntu.com/download/risc-v) | [TUNA mirror](https://mirror.tuna.tsinghua.edu.cn/ubuntu-cdimage/releases/oracular/release/ubuntu-24.10-preinstalled-server-riscv64+unmatched.img.xz)
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
xzcat ubuntu-24.10-preinstalled-server-riscv64+unmatched.img.xz | sudo dd of=/dev/sdX bs=4M iflag=fullblock status=progress 
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

(Some `cloud-init` logs are redacted.)

```log
0 updates can be applied immediately.


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
ubuntu@ubuntu:~$ cat /proc/cpuinfo
processor       : 0
hart            : 1
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x20181004
hart isa        : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd

processor       : 1
hart            : 2
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x20181004
hart isa        : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd

processor       : 2
hart            : 3
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x20181004
hart isa        : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd

processor       : 3
hart            : 4
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x20181004
hart isa        : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd

ubuntu@ubuntu:~$ uname -a
Linux ubuntu 6.11.0-8-generic #8.1-Ubuntu SMP PREEMPT_DYNAMIC Tue Oct  1 11:40:56 UTC 2024 riscv64 riscv64 riscv64 GNU/Linux
```

Screen recording:

[![asciicast](https://asciinema.org/a/YGiZPo96BSLnFojaCEwV370z6.svg)](https://asciinema.org/a/YGiZPo96BSLnFojaCEwV370z6)

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.