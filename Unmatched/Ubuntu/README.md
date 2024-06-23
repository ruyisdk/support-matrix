# Ubuntu 23.10 HiFive Unmatched Test Report

## Test Environment

### Operating System Information

- System Version: Ubuntu 23.10
- Download Link: [https://ubuntu.com/download/risc-v](https://ubuntu.com/download/risc-v)
- Reference Installation Document: [https://wiki.ubuntu.com/RISC-V/SiFive%20HiFive%20Unmatched](https://wiki.ubuntu.com/RISC-V/SiFive%20HiFive%20Unmatched)

### Hardware Information

- HiFive Unmatched Rev A
- A microUSB cable (provided with HiFive Unmatched)
- An ATX power supply
- A 64GB Sandisk Extreme Pro microSD card (UHS-I)

## Installation Steps

### Boot Device Selection

Ensure the dip switch is set to boot from the microSD card. If you haven't changed it, the factory default setting is to boot from the microSD card.

The dip switch should be set as follows: `MSEL[3:0]=1011`

### Flashing the Image to the microSD Card Using `ruyi` CLI

Install the [`ruyi`](https://github.com/ruyisdk/ruyi) package manager, run `ruyi device provision`, and follow the prompts.

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
ubuntu@ubuntu:~$ cat /proc/cpuinfo 
processor       : 0
hart            : 1
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x20181004

processor       : 1
hart            : 2
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x20181004

processor       : 2
hart            : 3
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x20181004

processor       : 3
hart            : 4
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x20181004

ubuntu@ubuntu:~$ uname -a
Linux ubuntu 6.5.0-9-generic #9.1-Ubuntu SMP Sat Oct  7 17:18:31 UTC 2023 riscv64 riscv64 riscv64 GNU/Linux
ubuntu@ubuntu:~$ cat /etc/os-release 
PRETTY_NAME="Ubuntu 23.10"
NAME="Ubuntu"
VERSION_ID="23.10"
VERSION="23.10 (Mantic Minotaur)"
VERSION_CODENAME=mantic
ID=ubuntu
ID_LIKE=debian
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
UBUNTU_CODENAME=mantic
LOGO=ubuntu-logo
ubuntu@ubuntu:~$
```

Screen recording (from flashing the image to logging into the system):

[![asciicast](https://asciinema.org/a/Rh773h5eOalKZlzjQRFrQDnjY.svg)](https://asciinema.org/a/Rh773h5eOalKZlzjQRFrQDnjY)

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
