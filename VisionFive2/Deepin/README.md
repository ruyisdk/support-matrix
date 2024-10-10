---
sys: deepin
sys_ver: 23
sys_var: null

status: basic
last_update: 2024-06-21
---

# Deepin VisionFive 2 Test Report

## Test Environment

### Operating System Information

- System Version: Deepin 23 preview
- Download Link: https://cdimage.deepin.com/RISC-V/preview-20240613-riscv64/deepin-23-beige-preview-riscv64-visionfive2-20240613-125619.tar.xz
- Reference Installation Document: https://cdimage.deepin.com/RISC-V/VisionFive-v2-image/README.txt

### Hardware Information

- StarFive VisionFive 2
- A USB power adapter
- A USB-A to C or C to C cable
- A microSD card
- A USB to UART debugger (e.g., CH340, CH341, FT2232, etc.)
- Three Dupont wires

## Installation Steps

### Decompress and Flash Image to microSD Card

Assuming `/dev/sda` is the storage card.

```bash
tar -xvf deepin-23-beige-preview-riscv64-visionfive2-20240613-125619.tar.xz
sudo dd if=deepin-visionfive2-riscv64-stable-desktop-installer.img of=/dev/sda bs=1M status=progress
```

#### Issue: Kernel panic

If you see something like:
```log
Kernel panic - not syncing: VFS: Unable to mount root fs on unknown-block(0,0)
```

A fix in the boot file is needed. 

Run `sudo blkid` on your machine, you shall see something like:
```log
/dev/sda4: LABEL="root" UUID="4c4bc538-15f7-4687-8509-d02d23d09b15" BLOCK_SIZE="4096" TYPE="ext4" PARTLABEL="root" PARTUUID="a8a69a6c-a25e-4d7a-939c-f539566a1fdd"
/dev/sda2: PARTLABEL="uboot" PARTUUID="f8dee89e-c53b-48ef-bb3f-ff25b8a25cbf"
/dev/sda3: UUID="847A-3FD4" BLOCK_SIZE="512" TYPE="vfat" PARTLABEL="image" PARTUUID="d1acffb2-3c52-4b50-a25e-63330675c57f"
/dev/sda1: PARTLABEL="spl" PARTUUID="a4afe21c-10a5-4111-a88e-639128d69b2c"
```

Remember the PARTUUID of the fourth partition. Like in the log above, it's `PARTUUID="a8a69a6c-a25e-4d7a-939c-f539566a1fdd"`

Mount the third partition of the SD card and change the extlinux/extlinux.conf, you should replace the `root=LABEL=root` to `root=PARTUUID=$(your partuuid)`

Umount and reboot on the board, now you should boot up normally.

### Boot Mode Selection

StarFive VisionFive 2 offers multiple boot modes, configurable via onboard DIP switches before powering on. The board itself also has silk-screen labels.

To boot the original Debian image, select the 1-bit QSPI Nor Flash mode (i.e., `RGPIO_0 = 0`, `RGPIO_1 = 0`). Note that this mode may require updating the firmware in the Flash beforehand. If the boot is unsuccessful, please refer to the official documentation for firmware upgrade details: [Updating SPL and U-Boot](https://doc.rvspace.org/VisionFive2/Quick_Start_Guide/VisionFive2_QSG/spl_u_boot_0.html)

If not updating the firmware, choose the microSD card boot mode (i.e., `RGPIO_0 = 1`, `RGPIO_1 = 0`).

> Note: There is a slight chance that the system may fail to boot in this mode. If boot failure occurs, the serial output might resemble the following:
>
>```log
>dwmci_s: Response Timeout.                                                                                            
>dwmci_s: Response Timeout.                                                                                            
>BOOT fail,Error is 0xffffffff
>```
>
> You can try repowering the development board or pressing the button near the USB Type-C power port. This usually resolves the boot issue.

### Logging into the System

Log into the system via the serial port.

Default username: `root`
Default password: `deepin`

## Expected Results

The system should boot up normally and allow login via the serial port.

## Actual Results

Need to manually tweak the boot config to boot.

The system booted up successfully, and login via the serial port was successful.

### Boot Log

```log
Deepin GNU/Linux 23 deepin-riscv64-visionfive2 ttyS0

deepin-riscv64-visionfive2 login: root
Password:
Verification successful
Linux deepin-riscv64-visionfive2 6.6.20-visionfive2-66y #1 SMP Tue May 28 03:46:53 UTC 2024 riscv64
Welcome to Deepin 23 GNU/Linux

    * Homepage:https://www.deepin.org/

    * Bugreport:https://bbs.deepin.org/


root@deepin-riscv64-visionfive2:~# uname -a
Linux deepin-riscv64-visionfive2 6.6.20-visionfive2-66y #1 SMP Tue May 28 03:46:53 UTC 2024 riscv64 GNU/Linux
root@deepin-riscv64-visionfive2:~# cat /etc/os
os-release  os-version  ostree/     
root@deepin-riscv64-visionfive2:~# cat /etc/os-release 
PRETTY_NAME="Deepin 23"
NAME="Deepin"
VERSION_ID="23"
VERSION="23"
ID=Deepin
HOME_URL="https://www.deepin.org/"
BUG_REPORT_URL="https://bbs.deepin.org"
VERSION_CODENAME=beige

```

Screen recording (from flashing the image to system login):
[![asciicast](https://asciinema.org/a/oZhyQXdhDgf2uzT8EZSshqcim.svg)](https://asciinema.org/a/oZhyQXdhDgf2uzT8EZSshqcim)

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test partially successful.
