---
sys: deepin
sys_ver: 23
sys_var: null

status: good
last_update: 2025-03-03
---

# Deepin RISC-V preview Pioneer test report

## Test environment

### OS information

- OS version: Deepin 23 preview-20240815
- Download Links:
    - OS image: https://ci.deepin.com/repo/deepin/deepin-ports/cdimage/20240815/riscv64/deepin-23-beige-preview-riscv64-sg2042-20240815-125146.tar.xz
    - Firmware: https://ci.deepin.com/repo/deepin/deepin-ports/cdimage/latest/riscv64/bootloaders/sophgo-bootloader-single-sg2042-dev.zip
- Reference installation manual: https://deepin-community.github.io/sig-deepin-ports/docs/install/riscv/sg2042

### Hardware info

- Milk-V Pioneer v1.3
- microSD Card (≥ 512MB)
- NVMe SSD (comes with this machine)
- microSD card reader
- NVMe-USB SSD enclosure
- USB-A to C / C to C cable
- VGA/HDMI monitor and cable (or a capture card as used in this test)
- USB keyboard & mouse

## Installation steps

### Extract and flash image

Use `tar` and `unzip` to extrace OS image and firmware.

Use `dd` to write these images.

Unzip `sophgo-bootloader-multi-sg2042-dev.zip`, write `firmware_single_sg2042-dev.img` to microSD card.

Erase all partitions on the NVMe SSD, recreate a GPT partition table, create a new partition and write the ext4 system image to this partition.



`/dev/sdX`, `/dev/sdY` are microSD card and the NVMe SSD.

```bash
unzip sophgo-bootloader-multi-sg2042-dev.zip
sudo wipefs -af /dev/sdX
sudo dd if=firmware_single_sg2042-dev.img of=/dev/sdX bs=1M status=progress
sudo wipefs -af /dev/sdY
sudo fdisk /dev/sdY
# Enter g, n, and Enter *3, then enter w to write the changes to disk
tar -xvf deepin-23-beige-preview-riscv64-sg2042-20240815-125146.tar.xz
sudo dd if=./deepin-sg2042-riscv64-stable-desktop-installer.root.ext4 of=/dev/sdY1 bs=4M status=progress
echo ", +" | sudo sfdisk -N 1 /dev/sdY
sudo resize2fs /dev/sdY1
```

### Login

Login via GUI.

Choose the language and keyboard layout and complete the installation wizard.

Default username: `root`

Default password: `deepin`

## Expected Results

The system boots up normally and we can successfully login to the desktop.

## Actual Results

The system boots normally，and we can successfully login to the desktop.

If we switch to another TTY (e.g. Ctrl + Alt + F2) then we can login to the shell.failed

> The following screenshots are from USB HDMI capture card directly from the machine.

![](image/1.png)

If you see the installation wizard jumps to a tty screen, please wait for a few minutes to load the login screen

![](image/2.png)

Desktop

![](image/3.png)

System Info:

![](image/4.png)

### Boot log

Screen recording (from flashing to bootup): 
[![asciicast](https://asciinema.org/a/8JieNFV9nQP1bYTpRcV3muhbB.svg)](https://asciinema.org/a/8JieNFV9nQP1bYTpRcV3muhbB)

Check the screenshots above.

## Test criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Conclusion

Test successful.