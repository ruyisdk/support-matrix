---
sys: armbian
sys_ver: 23.8.1
sys_var: null

status: cfh
last_update: 2025-03-03
---

# Armbian MangoPi MQ Pro Test Report

## Test Environment

### Operating System Information

- Download Link: https://xogium.performanceservers.nl/archive/mangopi-mq/archive/Armbian_23.8.1_Mangopi-mq_jammy_edge_6.1.0-rc3_xfce_desktop.img.xz
- Reference Installation Document: https://mangopi.org/mqpro

### Hardware Information

- MangoPi MQ Pro
- Power Adapter
- A microSD card
- A USB to UART Debugger

## Installation Steps

### Flashing Image

Use `xz` to decompress the image.
Use `dd` to flash the image to the microSD card.

```bash
xz -kd /path/to/Armbian_22.08.0-trunk_Nezha_jammy_current_5.19.0_xfce_desktop.img.xz
sudo dd if=/path/to/Armbian_22.08.0-trunk_Nezha_jammy_current_5.19.0_xfce_desktop.img of=/dev/your_device bs=1M status=progress
```

### Logging into the System

Logging into the system via the serial port.

Default username: `root`
You will set a password on the first login.

## Expected Results

The system should boot normally and allow login via the onboard serial port.

## Actual Results

The system failed to boot normally due to an error with U-Boot.

### Boot Log

```log
U-Boot 2022.07-rc3-35470-gafc07cec42-dirty (Jun 26 2022 - 13:03:06 +0300)

CPU:   rv64imafdc
Model: Allwinner D1 Nezha
DRAM:  1 GiB
sunxi_set_gate: (CLK#24) unhandled
Core:  66 devices, 24 uclasses, devicetree: board
WDT:   Started watchdog@6011000 with servicing (16s timeout)
MMC:   mmc@4020000: 0, mmc@4021000: 1
Loading Environment from nowhere... OK
In:    serial@2500000
Out:   serial@2500000
Err:   serial@2500000
Net:   
Warning: ethernet@4500000 (eth0) using random MAC address - 96:1a:8a:62:24:8b
eth0: ethernet@4500000
Hit any key to stop autoboot:  0 
switch to partitions #0, OK
mmc0 is current device
Scanning mmc 0:1...
Found /boot/extlinux/extlinux.conf
Retrieving file: /boot/extlinux/extlinux.conf
1:      Armbian
Retrieving file: /boot/uInitrd
Retrieving file: /boot/Image
append: root=UUID=89038d48-9eef-4730-94fe-e7fe325e67e2 console=ttyS0,115200n8 console=tty0 earlycon=sbi cma=96M rootflags=data=writeback stmmaceth=chain_mode:1 rw rw no_console_suspend consoleblank=0 fsck.fix=yes fsck.repair=yes net.ifnames=0 splash plymouth.ignore-serial-consoles
Retrieving file: /boot/dtb/allwinner/sun20i-d1-nezha.dtb
Moving Image from 0x40040000 to 0x40200000, end=41ae6000
## Loading init Ramdisk from Legacy Image at 41c00000 ...
   Image Name:   uInitrd
   Image Type:   RISC-V Linux RAMDisk Image (gzip compressed)
   Data Size:    19879135 Bytes = 19 MiB
   Load Address: 00000000
   Entry Point:  00000000
   Verifying Checksum ... OK
ERROR: Did not find a cmdline Flattened Device Tree
Could not find a valid device tree
SCRIPT FAILED: continuing...
No EFI system partition
BootOrder not defined
EFI boot manager: Cannot load any image
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

Device 0: unknown device
sun8i_emac_eth_start: Timeout
missing environment variable: pxeuuid
Retrieving file: /boot/extlinux/pxelinux.cfg/01-96-1a-8a-62-24-8b
sun8i_emac_eth_start: Timeout
Retrieving file: /boot/extlinux/pxelinux.cfg/00000000
sun8i_emac_eth_start: Timeout
Retrieving file: /boot/extlinux/pxelinux.cfg/0000000
sun8i_emac_eth_start: Timeout
Retrieving file: /boot/extlinux/pxelinux.cfg/000000
sun8i_emac_eth_start: Timeout
Retrieving file: /boot/extlinux/pxelinux.cfg/00000
sun8i_emac_eth_start: Timeout
Retrieving file: /boot/extlinux/pxelinux.cfg/0000
sun8i_emac_eth_start: Timeout
Retrieving file: /boot/extlinux/pxelinux.cfg/000
sun8i_emac_eth_start: Timeout
Retrieving file: /boot/extlinux/pxelinux.cfg/00
sun8i_emac_eth_start: Timeout
Retrieving file: /boot/extlinux/pxelinux.cfg/0
sun8i_emac_eth_start: Timeout
Retrieving file: /boot/extlinux/pxelinux.cfg/default-riscv-sunxi-sunxi
sun8i_emac_eth_start: Timeout
Retrieving file: /boot/extlinux/pxelinux.cfg/default-riscv-sunxi
sun8i_emac_eth_start: Timeout
Retrieving file: /boot/extlinux/pxelinux.cfg/default-riscv
sun8i_emac_eth_start: Timeout
Retrieving file: /boot/extlinux/pxelinux.cfg/default
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
