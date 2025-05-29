---
sys: armbian
sys_ver: 25.2.0-trunk.124
sys_var: null

status: cfh
last_update: 2025-04-07

# Due to the complexcity in armbian mirror naming, we needs to provide the download link for sync tools in the metadata.
link: https://github.com/armbian/community/releases/download/25.2.0-trunk.124/Armbian_community_25.2.0-trunk.124_Star64_noble_edge_5.15.0_xfce_desktop.img.xz
---

# Armbian Star64 Test Report

## Test Environment

### Operating System Information

- Download Link: https://github.com/armbian/community/releases/download/25.2.0-trunk.124/Armbian_community_25.2.0-trunk.124_Star64_noble_edge_5.15.0_xfce_desktop.img.xz
- Reference Installation Document: https://www.hackster.io/lupyuen/rtos-on-a-risc-v-sbc-star64-jh7110-apache-nuttx-2a7429

### Hardware Information

- Development Board: Star64
- USB A to C / USB C to C Cable
- SD Card

## Installation Steps

### Flashing Image

After downloading, unzip and flash the image (using the xfce version as an example):
```bash
unxz -k Armbian_community_25.2.0-trunk.124_Star64_noble_edge_5.15.0_xfce_desktop.img.xz
sudo dd if=Armbian_community_25.2.0-trunk.124_Star64_noble_edge_5.15.0_xfce_desktop.img of=/dev/your/sdcard bs=1M status=progress
```

### Logging into the System

Connect to the development board via the serial port.

Upon startup, the system will prompt the user to manually configure the username, password, timezone, language, etc.

The Xfce version requires configuration completion before entering the desktop environment.

Configuration can be done via the serial port. If a keyboard and monitor are connected, it can also be done via the keyboard.

## Expected Results

The system boots up normally, and information can be viewed through the onboard serial port.

## Actual Results

Image fails to boot with `Boot failed (err=-14)`.

### Boot Log

```log

U-Boot 2025.01-1~0ubuntu2 (Feb 27 2025 - 17:08:21 +0000)

CPU:   sifive,u74-mc
Model: Pine64 Star64
DRAM:  8 GiB
Core:  158 devices, 29 uclasses, devicetree: board
WDT:   Not starting watchdog@13070000
MMC:   mmc@16010000: 0, mmc@16020000: 1
Loading Environment from SPIFlash... SF: Detected gd25lq128 with page size 256 Bytes, erase size 4 KiB, total 16 MiB
OK
StarFive EEPROM format v2

--------EEPROM INFO--------
Vendor : PINE64
Product full SN: STAR64V1-2310-D008E000-00000005
data version: 0x2
PCB revision: 0xc1
BOM revision: A
Ethernet MAC0 address: 6c:cf:39:00:75:61
Ethernet MAC1 address: 6c:cf:39:00:75:62
--------EEPROM INFO--------

starfive_7110_pcie pcie@9c0000000: Starfive PCIe bus probed.
In:    serial@10000000
Out:   serial@10000000
Err:   serial@10000000
Net:   eth0: ethernet@16030000, eth1: ethernet@16040000
starting USB...
No USB controllers found
resetting USB...
No USB controllers found
Working FDT set to ff71ca10
Hit any key to stop autoboot:  0
Card did not respond to voltage select! : -110
Cannot persist EFI variables without system partition
** Booting bootflow '<NULL>' with efi_mgr
Loading Boot0000 'mmc 1' failed
EFI boot manager: Cannot load any image
Boot failed (err=-14)
Card did not respond to voltage select! : -110
** Booting bootflow 'mmc@16020000.bootdev.part_1' with extlinux
1:      Armbian_community
Retrieving file: /boot/Image
Retrieving file: /boot/uInitrd
bootarg overflow 265+0+0+1 > 256
Boot failed (err=-14)
No USB controllers found
ethernet@16030000 Waiting for PHY auto negotiation to complete......... TIMEOUT !
phy_startup() failed: -110
FAILED: -110
ethernet@16040000 Waiting for PHY auto negotiation to complete......... TIMEOUT !
phy_startup() failed: -110
FAILED: -110
BOOTP broadcast 1
BOOTP broadcast 2
BOOTP broadcast 3
BOOTP broadcast 4

```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test failed.