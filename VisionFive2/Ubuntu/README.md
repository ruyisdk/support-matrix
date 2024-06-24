# Ubuntu 24.04 VisionFive 2 Version Test Report

## Test Environment

### Operating System Information

- System Version: Ubuntu 24.04
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

Assume `/dev/sdc` as the storage card.

```bash
xz -d openKylin-1.0.1-visionfive2-riscv64.img.xz 
sudo dd if=openKylin-1.0.1-visionfive2-riscv64.img of=/dev/sdc bs=1M status=progress
```

### Boot Mode Selection

The StarFive VisionFive 2 offers multiple boot modes, configurable via onboard dip switches prior to powering on. Refer to the StarFive [official documentation](https://doc.rvspace.org/VisionFive2/Quick_Start_Guide/VisionFive2_SDK_QSG/boot_mode_settings.html).

The board also has silk-screen labels for guidance.

To boot the Ubuntu image, select the 1-bit QSPI Nor Flash mode (i.e., `RGPIO_0 = 0`, `RGPIO_1 = 0`).

Note: This mode requires prior firmware update in Flash. For details, refer to the official documentation: [Update SPL and U-Boot](https://doc.rvspace.org/VisionFive2/Quick_Start_Guide/VisionFive2_QSG/spl_u_boot_0.html)

Note: According to the Ubuntu [official documentation](https://wiki.ubuntu.com/RISC-V/StarFive%20VisionFive%202), use the image provided by the mainline U-Boot. Refer to the U-Boot [official documentation](https://u-boot.readthedocs.io/en/latest/board/starfive/visionfive2.html).

### Logging into the System

Login to the system via the serial port.

Default username: `ubuntu`
Default password: `ubuntu`

Upon first login, you will be prompted to change the default password.

## Expected Results

The system should boot normally and allow login via the serial port.

## Actual Results

The system booted normally, and login via the serial port was successful.

### Boot Log

```log
Welcome to Ubuntu 23.10 (GNU/Linux 6.5.0-9-generic riscv64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Tue Sep 19 15:56:54 UTC 2023

  System load:  0.74              Swap usage:  0%       Users logged in: 0
  Usage of /:   3.3% of 57.42GB   Temperature: 41.8 C
  Memory usage: 5%                Processes:   139

0 updates can be applied immediately.



The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

To run a command as administrator (user "root"), use "sudo <command>".
See "man sudo_root" for details.

ubuntu@ubuntu:~$ cat /proc/cpuinfo 
processor       : 0
hart            : 1
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zba_zbb
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x4210427

processor       : 1
hart            : 2
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zba_zbb
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x4210427

processor       : 2
hart            : 3
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zba_zbb
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x4210427

processor       : 3
hart            : 4
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zba_zbb
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x4210427

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
ubuntu@ubuntu:~$ uname -a
Linux ubuntu 6.5.0-9-generic #9.1-Ubuntu SMP Sat Oct  7 17:18:31 UTC 2023 riscv64 riscv64 riscv64 GNU/Linux
ubuntu@ubuntu:~$ 
```

Screen recording (from flashing image to system login):

[![asciicast](https://asciinema.org/a/gJWTbPGEv0N9dMcDSSOsblKoB.svg)](https://asciinema.org/a/gJWTbPGEv0N9dMcDSSOsblKoB)

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Ubuntu 24.10 is not tested yet/CFT; Ubuntu 23.10 has passed the test.
