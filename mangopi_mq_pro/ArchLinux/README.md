# Arch Linux MangoPi MQ Pro Test Report

## Test Environment

### Operating System Information

- Download Link:
    - Image Builder: https://github.com/sehraf/d1-riscv-arch-image-builder
    - U-Boot: https://github.com/smaeul/u-boot.git
    - RootFS: https://archriscv.felixc.at
- Reference Installation Document: https://github.com/sehraf/d1-riscv-arch-image-builder

### Hardware Information

- MangoPi MQ Pro
- Power Adapter
- A microSD card
- A USB to UART Debugger

## Installation Steps

### Install Dependencies

Use Arch Linux to install dependencies as follows:
```bash
pacman -Sy riscv64-linux-gnu-gcc swig cpio python3 python-setuptools base-devel bc arch-install-scripts qemu-user-static qemu-user-static-binfmt
```

### Select dtb File

After download the builder, modify consts.sh:
```bash
git clone https://github.com/sehraf/d1-riscv-arch-image-builder.git
cd d1-riscv-arch-image-builder
vim consts.sh
```

Select dtb:
```diff
diff --git a/consts.sh b/consts.sh
index 11e51cd..6fc61d5 100644
--- a/consts.sh
+++ b/consts.sh
@@ -25,7 +25,7 @@ export KERNEL='defconfig'
 # sun20i-d1-lichee-rv
 # sun20i-d1-mangopi-mq-pro
 # sun20i-d1-nezha
-export DEVICE_TREE=sun20i-d1-lichee-rv-dock
+export DEVICE_TREE=sun20i-d1-mangopi-mq-pro
 
 # folder to mount rootfs
 export MNT="${PWD}/mnt"

```

### Generate Image

Run `1_compile.sh`:
```bash
./1_compile.sh
```

### Flash Image

Run `2_create_sd.sh`:

```bash
2_create_sd.sh /dev/your/device
```

### Logging into the System

Logging into to the system via the serial port.

Default Username: `root`
Default Password: `archriscv`

## Expected Results

The system should boot up normally and allow login via the onboard serial port.

## Actual Results

CFT

### Boot Log

Screen recording (From flashing the image to logging in):

```log
```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

CFT
