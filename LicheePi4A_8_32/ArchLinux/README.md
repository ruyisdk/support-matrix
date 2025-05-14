---
sys: archlinux
sys_ver: null
sys_var: null

status: good
last_update: 2025-05-07
---

# Arch Linux LPi4A Test Report

## Test Environment

### System Information

- Download link: https://mirror.iscas.ac.cn/archriscv/images/
- u-boot and boot downloads (using revyos): https://mirror.iscas.ac.cn/revyos/extra/images/lpi4a/

### Hardware Information

- Lichee Pi 4A (8GB RAM + 32GB eMMC)
- A USB Power Adapter
- A USB-A to C or C to C Cable
- A USB to UART Debugger (e.g., CH340, CH341, FT2232, etc.)
- Three Dupont Wires


## Installation Steps

### Create rootfs

Since Arch Linux does not provide pre-packaged images but a rootfs, we need to create the image ourselves.

- Create a block device and file system
```bash
sudo dd if=/dev/zero of=rootfs.ext4 bs=1M count=6144 # Create a 6GB rootfs
sudo mkfs.ext4 rootfs.ext4
mkdir mnt
sudo mount ./rootfs.ext4 ./mnt
```

- Extract rootfs into the root directory
```bash
sudo tar -I zstd -xvf archriscv-2024-09-22.tar.zst -C mnt/
```

- Obtain the UUID of the file system
```bash
lsblk -o NAME,UUID
```

- Perform necessary updates, package installation, and adjustments in rootfs
```bash
sudo systemd-nspawn -D ./mnt --machine=archriscv

# The following commands are executed inside rootfs
pacman -Syu
# Install necessary packages such as vim here.
echo "UUID=<UUID> /  ext4  defaults  1  1 " >> /etc/fstab # Use the <UUID> obtained earlier
passwd # Set your root password!
exit
```

- Unmount rootfs
```bash
sudo umount ./mnt
```

### Flashing Bootloader

Extract the installation suite.
Flash u-boot and boot.

*Select whether you need 8GB version u-boot according to your hardware version*

```bash
zstd -d boot-lpi4a-20250420_084701.ext4.zst
sudo fastboot flash ram u-boot-with-spl-lpi4a-main_8gemmc.bin
sudo fastboot reboot
sudo fastboot flash uboot u-boot-with-spl-lpi4a-main_8gemmc.bin
sudo fastboot flash boot boot-lpi4a-20250420_084701.ext4
```

### Flashing Image

Flash the root partition into eMMC.

```bash
sudo fastboot flash root rootfs.ext4
```

### Logging into the System

Access the system via serial port.

Default username: `root`
Default password: the password you set earlier or use default `archriscv`.

### Install Desktop Environment

Take the example of installing xfce:

```
pacman -S xorg xfce4 ligthdm lightdm-gtk-greeter xfce4-goodies
systemctl enable --now ligthdm
```

## Expected Results

The system boots up successfully, allowing login via onboard serial port.

## Actual Results

The system boots up successfully, and login via onboard serial port is successful.

### Boot Log

![xfce](./desktop.jpg)

Screen recording:
[![asciicast](https://asciinema.org/a/7IKTyi434wlxfqY9sv0vfaZyt.svg)](https://asciinema.org/a/7IKTyi434wlxfqY9sv0vfaZyt)

```log
[  OK  ] Reached target Socket Units.
         Starting D-Bus System Message Bus...
[  OK  ] Started D-Bus System Message Bus.
[  OK  ] Reached target Basic System.
         Starting User Login Management...
         Starting Permit User Sessions...
[  OK  ] Finished Permit User Sessions.
[  OK  ] Started Getty on tty1.
[  OK  ] Started Serial Getty on ttyS0.
[  OK  ] Reached target Login Prompts.
[  OK  ] Started User Login Management.
[  OK  ] Reached target Multi-User System.
[  OK  ] Reached target Graphical Interface.

Arch Linux 6.6.82-th1520 (ttyS0)

archlinux login: root
Password: [   16.537320] platform pwm-backlight@0: deferred probe pending

[root@archlinux ~]# ls
Desktop
[root@archlinux ~]# neofetch
                   -`                    root@archlinux
                  .o+`                   --------------
                 `ooo/                   OS: Arch Linux riscv64
                `+oooo:                  Host: Sipeed Lichee Pi 4A
               `+oooooo:                 Kernel: 6.6.82-th1520
               -+oooooo+:                Uptime: 25 secs
             `/:-:++oooo+:               Packages: 425 (pacman)
            `/++++/+++++++:              Shell: bash 5.2.37
           `/++++++++++++++:             Terminal: /dev/ttyS0
          `/+++ooooooooooooo/`           CPU: (4) @ 1.848GHz
         ./ooosssso++osssssso+`          Memory: 90MiB / 7761MiB
        .oossssso-````/ossssss+`
       -osssssso.      :ssssssso.
      :osssssss/        osssso+++.
     /ossssssss/        +ssssooo/-
   `/ossssso+/:-        -:/+osssso+-
  `+sso+:-`                 `.-/+oso:
 `++:.                           `-/+/
 .`                                 `/

[root@archlinux ~]#
```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
