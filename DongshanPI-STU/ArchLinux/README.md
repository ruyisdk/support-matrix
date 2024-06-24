# Arch Linux DongshanPI-Nezha STU Test Report

## Test Environment

### Operating System Information

- System Version: Initial Release
- Packaging Script: https://github.com/sehraf/d1-riscv-arch-image-builder

### Hardware Information

- DongshanPI-Nezha ST
- A Type-C power cable
- A UART to USB debugger
- An SD card

## Installation Steps

### Using Packaging Script

For Arch Linux, install dependencies as follows:
```bash
pacman -Sy riscv64-linux-gnu-gcc swig cpio python3 python-setuptools base-devel bc arch-install-scripts qemu-user-static qemu-user-static-binfmt
```

The community has created an automatic Arch Linux packaging script. If you intend to use it, you can skip all the installation steps below.

Clone the corresponding repository:
```bash
git clone https://github.com/sehraf/d1-riscv-arch-image-builder.git
cd d1-riscv-arch-image-builder
```

Modify `DEVICE_TREE` in `consts.sh` based on your specific board, for example:
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
+export DEVICE_TREE=sun20i-d1-dongshan-nezha-stu
 
 # folder to mount rootfs
 export MNT="${PWD}/mnt"

```

Run `1_compile.sh` to compile the image;
Run `2_create_sd.sh /dev/your/device` to write it to the SD card.

Note: If automatically configuring the rootfs, you need: `arch-install-scripts`, `qemu-user-static-bin (AUR)`, `binfmt-qemu-static (AUR)`. If this step is not required, set `USE_CHROOT` to 0 in `consts.sh`.

```bash
./1_compile.sh
./2_create_sd.sh /dev/your/device
```

**If `USE_CHROOT` is enabled (default is enabled), it will automatically chroot into the image for configuration. It's recommended to install basic applications like vim at this step.**

### Logging into the System

Logging into the system via the serial port.

Default username: `root`
Default password: `archriscv`

## Expected Results

The system should boot normally and allow login via the onboard serial port.

## Actual Results

CFT

### Boot Log

Screen recording (from flashing image to logging into the system):

```log

```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

CFT
