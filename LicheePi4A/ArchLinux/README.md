# Arch Linux LPi4A Test Report

## Test Environment

### System Information

- Download link: [https://mirror.iscas.ac.cn/archriscv/images/](https://mirror.iscas.ac.cn/archriscv/images/)
- u-boot and boot downloads (using revyos): [https://mirror.iscas.ac.cn/revyos/extra/images/lpi4a/20231210/](https://mirror.iscas.ac.cn/revyos/extra/images/lpi4a/)
- fastboot download: [https://gitee.com/thead-yocto/light_deploy_images](https://gitee.com/thead-yocto/light_deploy_images)
- Reference Installation Document:
    - [ArchWiki](https://wiki.archlinux.org/title/General_recommendations)

### Hardware Information

- Lichee Pi 4A (8GB RAM + 64GB eMMC)
- Power Adapter
- USB to UART debugger

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
sudo tar -I zstd -xvf archriscv-2023-12-13.tar.zst -C mnt/
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
echo "UUID=$UUID /  ext4  defaults  1  1 " >> /etc/fstab # Use the $UUID obtained earlier
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

*Select whether you need 16GB version according to your hardware version*

```bash
zstd -d boot-lpi4a-20231210_134926.ext4.zst
sudo ./fastboot flash ram ./path/to/u-boot-with-spl-lpi4a.bin
sudo ./fastboot reboot
sudo ./fastboot flash uboot ./path/to/u-boot-with-spl-lpi4a.bin
sudo ./fastboot flash boot boot-lpi4a-20231210_134926.ext4
```

### Flashing Image

Flash the root partition into eMMC.

```bash
sudo ./fastboot flash root rootfs.ext4
```

### Logging into the System

Access the system via serial port.

Default username: `root`
Default password: the password you set earlier.

## Expected Results

The system boots up successfully, allowing login via onboard serial port.

## Actual Results

The system boots up successfully, and login via onboard serial port is successful.

### Boot Log

Screen recording (from creating rootfs to logging into the system):
[![asciicast](https://asciinema.org/a/7Ywwvlg1kdyAyTa9hiUOnv4yN.svg)](https://asciinema.org/a/7Ywwvlg1kdyAyTa9hiUOnv4yN)

```log
Arch Linux 5.10.113-yocto-standard (ttyS0)

archlinux login: root
Password: 
Last login: Sat Mar  9 10:04:36 on ttyS0
[root@archlinux ~]# neofetch 
                   -`                                                                                                           
                  .o+`                   -------------- 
                 `ooo/                   OS: Arch Linux riscv64 
                `+oooo:                  Host: T-HEAD Light Lichee Pi 4A configuration for 8GB DDR board 
               `+oooooo:                 Kernel: 5.10.113-lpi4a 
               -+oooooo+:                Uptime: 3 mins 
             `/:-:++oooo+:               Packages: 283 (pacman) 
            `/++++/+++++++:              Shell: bash 5.2.26 
           `/++++++++++++++:             Resolution: 1920x1080 
          `/+++ooooooooooooo/`           Terminal: /dev/ttyS0 
         ./ooosssso++osssssso+`          CPU: (4) @ 1.848GHz 
        .oossssso-````/ossssss+`         Memory: 84MiB / 7687MiB 
       -osssssso.      :ssssssso.
      :osssssss/        osssso+++.                               
     /ossssssss/        +ssssooo/-                               
   `/ossssso+/:-        -:/+osssso+-
  `+sso+:-`                 `.-/+oso:
 `++:.                           `-/+/
 .`                                 `/
```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
