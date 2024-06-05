# Armbian Lichee Cluster 4A Test Report

## Test Environment

### System Information

- System Version: Ubuntu 20.04 LTS
- Download Link: [https://github.com/chainsx/armbian-riscv-build/tree/main](https://github.com/chainsx/armbian-riscv-build/tree/main)
    - u-boot: [https://github.com/chainsx/thead-u-boot/actions](https://github.com/chainsx/thead-u-boot/actions)
- Reference Installation Document: [https://github.com/chainsx/armbian-riscv-build/blob/main/doc/licheepi-4a-install-guide.md](https://github.com/chainsx/armbian-riscv-build/blob/main/doc/licheepi-4a-install-guide.md)
- fastboot links:
    - [https://pan.baidu.com/e/1xH56ZlewB6UOMlke5BrKWQ](https://pan.baidu.com/e/1xH56ZlewB6UOMlke5BrKWQ)
    - [https://mega.nz/folder/phoQlBTZ#cZeQ3qZ__pDvP94PT3_bGA](https://mega.nz/folder/phoQlBTZ#cZeQ3qZ__pDvP94PT3_bGA)


### Hardware Information

- Lichee Cluster 4A 8G / 16G
- DC 12V Power Supply
- USB-A to A
    - or LPi4A Dock
- One microSD card
- Network and Ethernet cable (connect to BMC not switch)

## Installation Steps

*Below is an example of flashing to the first board in the cluster*

### Flashing Image

Use `unxz` to extract the image.
Use `dd` to flash the image to the microSD card.

```bash
unxz /path/to/Armbian.img.xz
sudo dd if=/path/to/Armbian.img of=/dev/your_device bs=1M status=progress
```

### Flashing Bootloader

Use the u-boot downloaded above.

```bash
sudo ./fastboot flash ram ./path/to/your/lpi4a-$(ram_size)-u-boot-with-spl.bin
sudo ./fastboot reboot
sleep 10
sudo ./fastboot flash uboot ./path/to/your/lpi4a-$(ram_size)-u-boot-with-spl.bin
```

### Logging to the System

Logging into the system via SOL (Serial Over LAN).

Default BMC username: `root`

Default BMC password: `0penBmc` **Note that it's `0` not `O`**

Connect via `ssh -p 2301 root@lichee-rv.local`

Initially, the system will prompt you to set a username and password.

### Common Issues

If USB is not working, it's because the Linux device tree needs patching. [Download patch](https://dl.sipeed.com/fileList/LICHEE/LicheeCluster4A/04_Firmware/lpi4a/src/linux/0001-arch-riscv-boot-dts-lpi4a-disable-i2c-io-expander-fo.patch)

## Expected Results

The system should boot up normally, allowing login via SOL (Serial Over LAN).

## Actual Results

The system booted up normally, allowing login via SOL (Serial Over LAN).

### Boot Log

Screen recording (from flashing the system to startup):

[![asciicast](https://asciinema.org/a/glbyZg6rjqfWu1YiQhyj62Zww.svg)](https://asciinema.org/a/glbyZg6rjqfWu1YiQhyj62Zww)

```log
Welcome to ARMBIAN! 

Documentation: https://docs.armbian.com | Community: https://forum.armbian.com

Create root password: ********
Repeat root password: ********
Rejected - it does not contain enough DIFFERENT characters. Try again [3].
Create root password: ********
Repeat root password: ********

Choose default system command shell:

1) bash
2) zsh

Shell: BASH

Creating a new user account. Press <Ctrl-C> to abort

Desktop environment will not be enabled if you abort the new user creation

Please provide a username (eg. your first name): plct
Create user (plct) password: ********
Repeat user (plct) password: ********

Please provide your real name: Plct

Dear Plct, your account plct has been created and is sudo enabled.
Please use this account for your daily work from now on.

Detected timezone: Asia/Hong_Kong

Set user language based on your location? [Y/n] 


At your location, more locales are possible:

1) en_HK.UTF-8              3) Skip generating locales
2) zh_HK.UTF-8
Please enter your choice:1) en_HK.UTF-8             3) Skip generating locales
2) zh_HK.UTF-8
Please enter your choice:1

Generating locales: en_HK.UTF-8

Now starting desktop environment...

root@licheepi-4a:~# uname -a
Linux licheepi-4a 5.10.113-thead-g052b22ef8baf #riscv SMP PREEMPT Sun Sep 24 07:26:26 UTC 2023 riscv64 riscv64 riscv64 GNU/Linux
root@licheepi-4a:~# cat /etc/os-release 
NAME="Ubuntu"
VERSION="20.04 LTS (Focal Fossa)"
ID=ubuntu
ID_LIKE=debian
PRETTY_NAME="Armbian-riscv 23.09.15-riscv Focal"
VERSION_ID="20.04"
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
VERSION_CODENAME=focal
UBUNTU_CODENAME=focal
root@licheepi-4a:~# 

```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
