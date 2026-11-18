---
sys: revyos
sys_ver: "20260504"
sys_var: null

status: good
last_update: 2026-11-18
---

# RevyOS LPi4A Test Report

## Test Environment

### System Information

- System Version: RevyOS 20260504
- Download Link: [Nginx Directory](https://fast-mirror.isrc.ac.cn/revyos/extra/images/lpi4a/20260504/)
- Reference Installation Document: [Visit here](https://revyos.github.io/docs/)

### Hardware Information

- Lichee Pi 4A (8GB RAM + 32GB eMMC)
- USB-C Power Adapter / DC Power Supply
- USB-UART Debugger

## Installation Steps

### Download and decompress image

Download the image, use `zstd` to decompress the image:

```shell
wget https://fast-mirror.isrc.ac.cn/revyos/extra/images/lpi4a/20260504/u-boot-with-spl-lpi4a.bin
wget https://fast-mirror.isrc.ac.cn/revyos/extra/images/lpi4a/20260504/boot-lpi4a-20260504_080619.ext4.zst
wget https://fast-mirror.isrc.ac.cn/revyos/extra/images/lpi4a/20260504/root-lpi4a-20260504_080619.ext4.zst
zstd -d boot-lpi4a-20260504_080619.ext4.zst
zstd -d root-lpi4a-20260504_080619.ext4.zst
```

### Flash to onboard eMMC via `fastboot`

#### Use boot button to enter fastboot mode

Hold the **BOOT** button, then connect the USB-C cable (to your PC on the other side) to enter USB burning mode.

Use the following commands to flash the image.

```shell
sudo fastboot devices
sudo fastboot flash ram u-boot-with-spl-lpi4a.bin
sudo fastboot reboot
sudo fastboot flash uboot u-boot-with-spl-lpi4a.bin
sudo fastboot flash boot boot-lpi4a-20260504_080619.ext4
sudo fastboot flash root root-lpi4a-20260504_080619.ext4
```

### Logging into the System

Logging into the system via serial console or graphical interface.

Default username: `debian`
Default password: `debian`
> Before connecting the board to a network, log in via the serial console or local desktop and run `passwd` to set a unique password for the default account.

## Expected Results

The system boots up successfully and can be accessed via the serial console.

## Actual Results

The system boots successfully and supports serial login, SSH over Ethernet, and an Xfce desktop session.

### Boot Log

![A](desktop-20260504.png)

Screen recording (from flashing image to logging into system):

[![asciicast](https://asciinema.org/a/nDo0ASizRAmC7YA6.svg)](https://asciinema.org/a/nDo0ASizRAmC7YA6)

```log
   ____              _ ____  ____  _  __
  |  _ \ _   _ _   _(_) ___||  _ \| |/ /
  | |_) | | | | | | | \___ \| | | | ' /
  |  _ <| |_| | |_| | |___) | |_| | . \
  |_| \_\\__,_|\__, |_|____/|____/|_|\_\
               |___/
                   -- Presented by ISCAS

  Debian GNU/Linux 13 (trixie) (kernel 6.6.137-th1520)

Linux revyos-lpi4a 6.6.137-th1520 #2026.05.01.09.26+cca7502e0 SMP Fri May  1 09:52:29 UTC 2026 riscv64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.

debian@revyos-lpi4a:~$ grep ^BUILD_ID= /etc/revyos-release
BUILD_ID=20260504_080619
debian@revyos-lpi4a:~$ findmnt -n -o SOURCE /
/dev/mmcblk0p4

```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
