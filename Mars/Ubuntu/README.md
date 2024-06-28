# Ubuntu 24.04 LTS on Milk-V Mars Test Report

## Test Environment

### Operating System Information

- Ubuntu 24.04 LTS
  - Download Link: https://cdimage.ubuntu.com/releases/24.04/release/ubuntu-24.04-preinstalled-server-riscv64+milkvmars.img.xz
  - Reference Installation Document: https://milkv.io/zh/docs/mars/getting-started/boot

### Hardware Information

- Milk-V Mars

## Installation Steps

### Flashing the Image

Use `unxz` to decompress the image. 
Use `dd` to flash the image to the microSD card.

Here, `/dev/sdc` corresponds to the storage device.

```bash
unxz -d ubuntu-24.04-preinstalled-server-riscv64+milkvmars.img.xz
sudo dd if=ubuntu-24.04-preinstalled-server-riscv64+milkvmars.img of=/dev/sdc bs=1M status=progress
```

### Updating U-Boot

**If a Kernel Panic occurs during startup, U-Boot update is required**

Insert the flashed SD card and quickly press Enter when "Hit any key to stop autoboot" appears on the serial terminal to enter the U-Boot command line interface.
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

The system should boot normally, allowing login via the onboard serial port, and should enter the installation wizard.

## Actual Results

The system booted successfully, and the output was successfully viewed via the serial port.

### Boot Information

Screen recording:
[![asciicast](https://asciinema.org/a/a3DgDMfhYPQgWhUjTTScbJ04n.svg)](https://asciinema.org/a/a3DgDMfhYPQgWhUjTTScbJ04n)

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

ubuntu@ubuntu:~$ cat /etc-o
cat: /etc-o: No such file or directory
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
ubuntu@ubuntu:~$ uname -a
Linux ubuntu 6.8.0-31-generic #31.1-Ubuntu SMP PREEMPT_DYNAMIC Sun Apr 21 01:12:53 UTC 2024 riscv64 riscv64 riscv64 GNU/Lix
ubuntu@ubuntu:~$ 
 

```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
