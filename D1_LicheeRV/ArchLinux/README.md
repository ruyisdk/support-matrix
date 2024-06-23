# Arch Linux LicheeRV / AWOL Nezha D1 Test Report

## Test Environment

### Operating System Information

- System Version: Initial Release
- Packaging Script: https://github.com/sehraf/d1-riscv-arch-image-builder

### Hardware Information

- Nezha D1
- A Type-C Power Cable
- A UART to USB Debugger
- SD Card

## Installation Steps

### Using the Packaging Script

Install dependencies on Arch Linux as follows:
```bash
pacman -Sy riscv64-linux-gnu-gcc swig cpio python3 python-setuptools base-devel bc arch-install-scripts qemu-user-static qemu-user-static-binfmt
```

The community has created an automated script for packaging Arch Linux. If you would like to use it, you can skip all the following installation steps.

Clone the corresponding repository:
```bash
git clone https://github.com/sehraf/d1-riscv-arch-image-builder.git
cd d1-riscv-arch-image-builder
```

Modify `DEVICE_TREE` in `consts.sh` according to your specific board, for example, the Lichee RV:
```diff
diff --git a/consts.sh b/consts.sh
index 11e51cd..0b990ad 100644
--- a/consts.sh
+++ b/consts.sh
@@ -25,7 +25,7 @@ export KERNEL='defconfig'
 # sun20i-d1-lichee-rv
 # sun20i-d1-mangopi-mq-pro
 # sun20i-d1-nezha
-export DEVICE_TREE=sun20i-d1-lichee-rv-dock
+export DEVICE_TREE=sun20i-d1-lichee-rv
 
 # folder to mount rootfs
 export MNT="${PWD}/mnt"

```

Run `1_compile.sh` to compile the image;
Run `2_create_sd.sh /dev/your/device` to burn it to the SD card.

Note: If you want to auto-configure the rootfs, you need: `arch-install-scripts`, `qemu-user-static-bin (AUR)`, `binfmt-qemu-static (AUR)`. If this step is not required, set `USE_CHROOT` in `consts.sh` to 0.

```bash
./1_compile.sh
./2_create_sd.sh /dev/your/device
```

**If USE_CHROOT is enabled (default is enabled), it will automatically chroot into the image for configuration. It is recommended to install basic applications like vim during this step.**

### Logging into the System

Logging into the system via the serial port.

Default Username: `root`
Default Password: `archriscv`

## Expected Results

The system should boot normally and allow login via the onboard serial port.

## Actual Results

The system booted successfully and login via the onboard serial port was also successful.

### Boot Log

Screen recording (from flashing the image to logging into the system):
[![asciicast](https://asciinema.org/a/D86o9kqp6phQBswrEEBt4rwyv.svg)](https://asciinema.org/a/D86o9kqp6phQBswrEEBt4rwyv)

```log
Arch Linux 6.8.0 (ttyS0)

licheerv login: root
Password: 
[root@licheerv ~]# neofetch
                   -`                                                                                                      
                  .o+`                   ------------- 
                 `ooo/                   OS: Arch Linux riscv64 
                `+oooo:                  Host: Allwinner D1 Nezha 
               `+oooooo:                 Kernel: 6.8.0 
               -+oooooo+:                Uptime: 1 min 
             `/:-:++oooo+:               Packages: 119 (pacman) 
            `/++++/+++++++:              Shell: bash 5.2.26 
           `/++++++++++++++:             Terminal: /dev/ttyS0 
          `/+++ooooooooooooo/`           CPU: (1) 
         ./ooosssso++osssssso+`          Memory: 55MiB / 970MiB 
        .oossssso-````/ossssss+`
       -osssssso.      :ssssssso.                                
      :osssssss/        osssso+++.                               
     /ossssssss/        +ssssooo/-
   `/ossssso+/:-        -:/+osssso+-
  `+sso+:-`                 `.-/+oso:
 `++:.                           `-/+/
 .`                                 `/

[root@licheerv ~]# 

```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful
