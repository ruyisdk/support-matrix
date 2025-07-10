---
sys: pmos
sys_ver: null
sys_var: null

status: cfh
last_update: 2025-06-12
---

# postmarketOS Sipeed M1s Dock Test Report

## Test Environment

### Operating System Information

- BuildRoot
  - Download Link: https://github.com/openbouffalo/buildroot_bouffalo/releases/download/v1.0.1/bl808-linux-pine64_ox64_full_defconfig.tar.gz
    - SDK: https://github.com/bouffalolab/bl_mcu_sdk
    - Flashing Tool: https://openbouffalo.org/static-assets/bldevcube/BouffaloLabDevCube-v1.8.3.zip
    - pmbootstrap: https://wiki.postmarketos.org/wiki/Pmbootstrap
  - Reference Installation Document: https://wiki.postmarketos.org/wiki/Sipeed_M1s_DOCK_(sipeed-m1sdock)

### Hardware Information

- Sipeed M1s Dock
- A Type-C cable

## Installation Steps

### Get the Image

Download and extract the precompiled image and firmware:
```bash
wget https://github.com/openbouffalo/buildroot_bouffalo/releases/download/v1.0.1/bl808-linux-pine64_ox64_full_defconfig.tar.gz
tar -xvf bl808-linux-pine64_ox64_full_defconfig.tar.gz
cd bl808-linux-pine64_ox64_full_defconfig/firmware
```

### Flashing the Firmware via UART

Power on the board through the Type-C UART port while holding down the BOOT button.

Download the flashing tool and use the appropriate version for your system to flash the firmware. Make sure your BLDevCube binary is of version 1.8.3 **or lower**.

Enter the MCU tab and set the parameters as shown below:

M0: Group: group0, Image Addr: `0x58000000`, and choose `m0_lowload_bl808_m0.bin` from the above archive

D0: Group: group0, Image Addr: `0x58100000`, and choose `d0_lowload_bl808_d0.bin` from the above archive

Choose the UART port with a **larger** device number among the two ports labeled with "(PROG)" correspondingly and set the "Uart Rate" to 2000000.

Click "Create & Download" and wait for it to complete.

![](mcu.png)

Next, Enter the IOT tab and set the parameters as shown below:

Enable "Single Download", set address to `0x800000` and choose `bl808-firmware.bin` from the above archive.

Click "Create & Download" and wait for it to complete.

![](iot.png)

### Install the system to SD card via `pmbootstrap`

Get `pmbootstrap`, e.g. under Arch Linux:
```bash
pacman -S pmbootstrap
```

Bootstrap and flash the system via `pmbootstrap`:
```bash
pmbootstrap init
pmbootstrap install --sdcard=/dev/sdX
pmbootstrap shutdown
```

Various configurations would also be made in the above process. Remember to select the target vendor as `sipeed`, and the target board as `m1sdock`。

### Boot

Insert the SD card, and power on the board through the Type-C UART port.

## Expected Results

The system should start normally with serial output.

## Actual Results

U-Boot is unable to detect the SD card used for booting.

### Boot Information

```log
[I][]
[I][]   ____                   ____               __  __      _
[I][]  / __ \                 |  _ \             / _|/ _|    | |
[I][] | |  | |_ __   ___ _ __ | |_) | ___  _   _| |_| |_ __ _| | ___
[I][] | |  | | '_ \ / _ \ '_ \|  _ < / _ \| | | |  _|  _/ _` | |/ _ \
[I][] | |__| | |_) |  __/ | | | |_) | (_) | |_| | | | || (_| | | (_) |
[I][]  \____/| .__/ \___|_| |_|____/ \___/ \__,_|_| |_| \__,_|_|\___/
[I][]        | |
[I][]        |_|
[I][]
[I][] Powered by BouffaloLab
[I][] Build:11:52:04,Mar  6 2023
[I][] Copyright (c) 2023 OpenBouffalo team
[I][] Copyright (c) 2022 Bouffalolab team
[I][] dynamic memory init success,heap s[I][LowLoad] D0 start...
[I][LowLoad] low_load start...
[I][LowLoad] Header at 0x5d5ff000
[I][LowLoad] Section dtb(1) - Start 0x5d5ff100, Size 14314
[I][LowLoad] Copying DTB to 0x51ff8000...0x51ffb7ea
[I][LowLoad] Done!
[I][LowLoad] Section OpenSBI(2) - Start 0x5d60f100, Size 109864
[I][LowLoad] Copying OpenSBI to 0x3ef80000...0x3ef9ad28
[I][LowLoad] Done!
[I][LowLoad] Section Kernel(3) - Start 0x5d62f100, Size 315597
[I][LowLoad] Uncompressing Kernel to 0x50000000...
[I][LowLoad] Done!
[I][LowLoad] CRC: 00000000
[I][LowLoad] load time: 61310 us
[I][LowLoad] Setting PMP
[I][LowLoad] Booting OpenSBI at 0x000000003ef80000 with DTB at 0x51ff8000

OpenSBI v1.2
   ____                    _____ ____ _____
  / __ \                  / ____|  _ \_   _|
 | |  | |_ __   ___ _ __ | (___ | |_) || |
 | |  | | '_ \ / _ \ '_ \ \___ \|  _ < | |
 | |__| | |_) |  __/ | | |____) | |_) || |_
  \____/| .__/ \___|_| |_|_____/|____/_____|
        | |
        |_|

Platform Name             : Pine64 Ox64 (D0)
Platform Features         : medeleg
Platform HART Count       : 1
Platform IPI Device       : aclint-mswi
Platform Timer Device     : aclint-mtimer @ 1000000Hz
Platform Console Device   : bflb_uart
Platform HSM Device       : ---
Platform PMU Device       : ---
Platform Reboot Device    : ---
Platform Shutdown Device  : ---
Firmware Base             : 0x3ef80000
Firmware Size             : 200 KB
Runtime SBI Version       : 1.0

Domain0 Name              : root
Domain0 Boot HART         : 0
Domain0 HARTs             : 0*
Domain0 Region00          : 0x00000000e4008000-0x00000000e400bfff (I)
Domain0 Region01          : 0x00000000e4000000-0x00000000e4007fff (I)
Domain0 Region02          : 0x000000003ef80000-0x000000003efbffff ()
Domain0 Region03          : 0x0000000000000000-0xffffffffffffffff (R,W,X)
Domain0 Next Address      : 0x0000000050000000
Domain0 Next Arg1         : 0x0000000051ff8000
Domain0 Next Mode         : S-mode
Domain0 SysReset          : yes

Boot HART ID              : 0
Boot HART Domain          : root
Boot HART Priv Version    : v1.11
Boot HART Base ISA        : rv64imafdcvx
Boot HART ISA Extensions  : time
Boot HART PMP Count       : 8
Boot HART PMP Granularity : 4096
Boot HART PMP Address Bits: 38
Boot HART MHPM Count      : 8
Boot HART MIDELEG         : 0x0000000000000222
Boot HART MEDELEG         : 0x000000000000b109


U-Boot 2023.04-rc2 (Mar 06 2023 - 11:48:40 +0000)

DRAM:  64 MiB
Core:  36 devices, 17 uclasses, devicetree: board
MMC:   mmc@20060000: 0
Loading Environment from FAT... Card did not respond to voltage select! : -110
** Bad device specification mmc 0 **
Loading Environment from nowhere... OK
In:    serial@30002000
Out:   serial@30002000
Err:   serial@30002000
Net:
Warning: emac@20070000 (eth0) using random MAC address - da:20:0d:12:b7:5e
eth0: emac@20070000
Hit any key to stop autoboot:  0
Card did not respond to voltage select! : -110
Card did not respond to voltage select! : -110
Card did not respond to voltage select! : -110
BOOTP broadcast 1
BOOTP broadcast 2

```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.

