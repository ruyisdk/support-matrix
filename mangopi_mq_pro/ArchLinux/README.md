---
sys: archlinux
sys_ver: null
sys_var: null

status: cft
last_update: 2024-06-21
---

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

Also modify `1_compile.sh` to address an issue similar to https://github.com/The-OpenROAD-Project/OpenROAD/issues/6451:

```diff
diff --git a/1_compile.sh b/1_compile.sh
index 4fcbc7c..bf62caf 100755
--- a/1_compile.sh
+++ b/1_compile.sh
@@ -80,6 +80,7 @@ if [ ! -f "${OUT_DIR}/u-boot-sunxi-with-spl.bin" ]; then
     clean_dir ${DIR}

     git clone --depth 1 "${SOURCE_UBOOT}" -b "${TAG_UBOOT}"
+    sed -i 's/SWIG_Python_AppendOutput/SWIG_AppendOutput/g' u-boot/scripts/dtc/pylibfdt/libfdt.i_shipped
     cd ${DIR}
     pin_commit "${COMMIT_UBOOT}"
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

**If `USE_CHROOT` is enabled (by default), it will automatically chroot into the image for configuration. It's recommended to install basic applications like vim at this step.**

### Logging into the System

Logging into to the system via the serial port.

Default Username: `root`
Default Password: `archriscv`

## Expected Results

The system should boot up normally and allow login via the onboard serial port.

## Actual Results

The system failed to boot normally due to an error with U-Boot.

### Boot Log

```log
U-Boot 2022.10-dirty (Mar 04 2025 - 12:39:02 +0800) Allwinner Technology

DRAM:  1 GiB
sunxi_set_gate: (CLK#24) unhandled
Core:  54 devices, 20 uclasses, devicetree: separate
WDT:   Started watchdog@6011000 with servicing every 1000ms (16s timeout)
MMC:   mmc@4020000: 0, mmc@4021000: 1
Loading Environment from FAT... PLL reg = 0xf8216300, freq = 1200000000
Unable to use mmc 0:1...
In:    serial@2500000
Out:   serial@2500000
Err:   serial@2500000
Net:
Warning: ethernet@4500000 (eth0) using random MAC address - 52:e9:78:d2:2a:ec
eth0: ethernet@4500000
starting USB...
Bus usb@4101000: USB EHCI 1.00
Bus usb@4101400: USB OHCI 1.0
Bus usb@4200000: USB EHCI 1.00
Bus usb@4200400: USB OHCI 1.0
scanning bus usb@4101000 for devices... 1 USB Device(s) found
scanning bus usb@4101400 for devices... 1 USB Device(s) found
scanning bus usb@4200000 for devices... 1 USB Device(s) found
scanning bus usb@4200400 for devices... 1 USB Device(s) found
       scanning usb for storage devices... 0 Storage Device(s) found
Hit any key to stop autoboot:  0
PLL reg = 0xf8216300, freq = 1200000000
switch to partitions #0, OK
mmc0 is current device
Scanning mmc 0:1...
Card did not respond to voltage select! : -110
** Bad device specification host 0 **
Couldn't find partition host 0:0
Cannot read EFI system partition
BootOrder not defined
EFI boot manager: Cannot load any image

Device 0: unknown device
sun8i_emac_eth_start: Timeout
missing environment variable: pxeuuid
Retrieving file: pxelinux.cfg/01-52-e9-78-d2-2a-ec
sun8i_emac_eth_start: Timeout
Retrieving file: pxelinux.cfg/00000000
sun8i_emac_eth_start: Timeout
Retrieving file: pxelinux.cfg/0000000
sun8i_emac_eth_start: Timeout
Retrieving file: pxelinux.cfg/000000
sun8i_emac_eth_start: Timeout
Retrieving file: pxelinux.cfg/00000
sun8i_emac_eth_start: Timeout
Retrieving file: pxelinux.cfg/0000
sun8i_emac_eth_start: Timeout
Retrieving file: pxelinux.cfg/000
sun8i_emac_eth_start: Timeout
Retrieving file: pxelinux.cfg/00
sun8i_emac_eth_start: Timeout
Retrieving file: pxelinux.cfg/0
sun8i_emac_eth_start: Timeout
Retrieving file: pxelinux.cfg/default-riscv-sunxi-sunxi
sun8i_emac_eth_start: Timeout
Retrieving file: pxelinux.cfg/default-riscv-sunxi
sun8i_emac_eth_start: Timeout
Retrieving file: pxelinux.cfg/default-riscv
sun8i_emac_eth_start: Timeout
Retrieving file: pxelinux.cfg/default
sun8i_emac_eth_start: Timeout
Config file not found
sun8i_emac_eth_start: Timeout
sun8i_emac_eth_start: Timeout
=>

```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test failed.