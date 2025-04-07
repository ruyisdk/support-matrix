---
sys: ubuntu
sys_ver: 24.04.2
sys_var: LTS

status: basic
last_update: 2025-03-24
---

# Ubuntu 24.04.2 LTS on Milk-V Mars Test Report

## Test Environment

### Operating System Information

- Ubuntu 24.04.2 LTS
  - Download Link: <https://cdimage.ubuntu.com/releases/24.04.2/release/ubuntu-24.04.2-preinstalled-server-riscv64+milkvmars.img.xz>
  - Reference Installation Document: <https://milkv.io/zh/docs/mars/getting-started/boot>

### Hardware Information

- Milk-V Mars (8GB RAM)
- A USB power adapter and A USB-A to C or C to C cable
- A microSD card
- A USB to UART debugger (e.g., CH340, CH341, FT2232, etc.)

## Installation Steps

### Flashing the Image

Use `tar` to decompress the image.
Use `dd` command or use the `balenaEtcher` software to flash the image to the microSD card.

Here, `/dev/sdc` corresponds to the storage device.

```bash
tar -xvf ubuntu-24.04.1-preinstalled-server-riscv64+milkvmars.img.xz
sudo dd if=ubuntu-24.04.1-preinstalled-server-riscv64+milkvmars.img of=/dev/sdc bs=1M status=progress
```

### Updating U-Boot

**If a Kernel Panic occurs during startup, U-Boot update is required:**

Insert the flashed SD card and quickly press Enter when `Hit any key to stop autoboot` appears on the serial terminal to enter the U-Boot command line interface.
After entering the U-Boot console, input the following commands in sequence:

```bash
sf probe
load mmc 1:1 $kernel_addr_r /usr/lib/u-boot/starfive_visionfive2/u-boot-spl.bin.normal.out
sf update $kernel_addr_r 0 $filesize
load mmc 1:1 $kernel_addr_r /usr/lib/u-boot/starfive_visionfive2/u-boot.itb
sf update $kernel_addr_r 0x100000 $filesize
```

### Logging into the System

Logging into the system via the serial port.

Default username: `ubuntu`

Default password: `ubuntu`

## Expected Results

The system should boot normally, allowing login via the onboard serial port.

## Actual Results

The system booted successfully, and the output was successfully viewed via the serial port. HDMI cannot output the graphical interface properly.

### Boot Log

```log
Ubuntu 24.04.2 LTS ubuntu ttyS0

ubuntu login: ubuntu
Password:
You are required to change your password immediately (administrator enforced).
Changing password for ubuntu.
Current password:
New password:
Retype new password:
Welcome to Ubuntu 24.04.2 LTS (GNU/Linux 6.8.0-52-generic riscv64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/pro

 System information as of Sat Feb 15 09:12:23 UTC 2025

  System load:    1.09      Processes:             29
  Usage of /home: unknown   Users logged in:       0
  Memory usage:   2%        IPv4 address for eth0: 10.10.10.2
  Swap usage:     0%

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

ubuntu@ubuntu:~$ cat /etc/os-release
PRETTY_NAME="Ubuntu 24.04.2 LTS"
NAME="Ubuntu"
VERSION_ID="24.04"
VERSION="24.04.2 LTS (Noble Numbat)"
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
Linux ubuntu 6.8.0-52-generic #53.1-Ubuntu SMP PREEMPT_DYNAMIC Sun Jan 26 04:38:25 UTC 2025 riscv64 riscv64 riscv64 GNU/Linux

ubuntu@ubuntu:~$ cat /proc/cpuinfo
processor       : 0
hart            : 2
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zba_zbb
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x4210427
hart isa        : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zba_zbb

processor       : 1
hart            : 1
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zba_zbb
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x4210427
hart isa        : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zba_zbb

processor       : 2
hart            : 3
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zba_zbb
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x4210427
hart isa        : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zba_zbb

processor       : 3
hart            : 4
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zba_zbb
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x4210427
hart isa        : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zba_zbb

ubuntu@ubuntu:~$
```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
