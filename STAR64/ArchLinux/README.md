---
sys: archlinux
sys_ver: null
sys_var: null
provider: Community
status: cfh
last_update: 2025-05-26
---

# Arch Linux Pine64 Star64 Test Report

## Test Environment

### Operating System Information

- Source code Link: https://github.com/yogo1212/arch-linux-star64
- Reference Installation Document: https://github.com/yogo1212/arch-linux-star64

### Hardware Information

- Pine64 Star64
- A microSD card
- DC 12V5A Barrel power adapter
- A USB to UART Debugger (e.g., CH340, CH341, FT2232, etc.)
- Three Dupont wires

## Installation Steps

### Building and Flashing the Image

Pull repository, build and flash the image (e.g. under an existing Arch Linux install):
```bash
git clone https://github.com/yogo1212/arch-linux-star64.git
cd arch-linux-star64
mkdir build
make
dd if=./build/star64.img of=/dev/your/device bs=1M status=progress
# or:
# make DEV_OR_IMG=/dev/your/device
```

### Logging into the System

Connect to the development board via the serial port.

## Expected Results

The system boots up normally, and information can be viewed through the onboard serial port.

## Actual Results

Image fails to boot with `Boot failed (err=-14)`.

### Boot Log

```log
U-Boot 2025.07-rc2-00085-g92da174fc636 (May 26 2025 - 16:02:32 +0800)

CPU:   sifive,u74-mc
Model: Pine64 Star64
DRAM:  8 GiB
Core:  160 devices, 29 uclasses, devicetree: board
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
Register 2000820 NbrPorts 2
Starting the controller
USB XHCI 1.00
Bus usb@0: 4 USB Device(s) found
       scanning usb for storage devices... 0 Storage Device(s) found
Working FDT set to ff71a300
Hit any key to stop autoboot:  0
Card did not respond to voltage select! : -110
Cannot persist EFI variables without system partition
** Booting bootflow '<NULL>' with efi_mgr
Loading Boot0000 'mmc 1' failed
EFI boot manager: Cannot load any image
Boot failed (err=-14)
Card did not respond to voltage select! : -110
ethernet@16030000 Waiting for PHY auto negotiation to complete....
```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test failed.
