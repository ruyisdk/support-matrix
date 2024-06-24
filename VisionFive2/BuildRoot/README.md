# BuildRoot VisionFive 2 Test Report

## Test Environment

### Operating System Information

- System Version: VisionFive 2 Software v5.11.3
- Download Link: https://github.com/starfive-tech/VisionFive2/releases
- Reference Installation Document: https://doc.rvspace.org/VisionFive2/SDK_Quick_Start_Guide/VisionFive2_SDK_QSG/running_sdk_on_visionfive_2.html

### Hardware Information

- StarFive VisionFive 2
- A USB power adapter
- A USB-A to C or C to C cable
- A microSD card
- A USB to UART debugger (e.g., CH340, CH341, FT2232, etc.)
- Three DuPont wires

## Installation Steps

### Flashing the Image to the microSD Card

Assuming `/dev/sdc` is the storage card.

```bash
sudo dd if=sdcard.img of=/dev/sdc bs=1M status=progress
```

### Boot Mode Selection

StarFive VisionFive 2 offers multiple boot modes, which can be configured via the onboard dip switches before powering on. The board itself has labeled silkscreen indications.

To start the factory BuildRoot image, choose the 1-bit QSPI Nor Flash mode (`RGPIO_0 = 0`, `RGPIO_1 = 0`). Note that this mode may require prior firmware updates in the Flash. If the boot is unsuccessful, please refer to the official documentation for firmware upgrade instructions: [Updating SPL and U-Boot](https://doc.rvspace.org/VisionFive2/Quick_Start_Guide/VisionFive2_QSG/spl_u_boot_0.html)

If you do not update the firmware, choose microSD card boot (`RGPIO_0 = 1`, `RGPIO_1 = 0`).

> Note: In this mode, there is a small probability of boot failure. If this occurs, the serial output may show information similar to the following:
>
>```log
>dwmci_s: Response Timeout.                                                                                            
>dwmci_s: Response Timeout.                                                                                            
>BOOT fail,Error is 0xffffffff
>```
>
> You can try repowering the development board or pressing the button near the USB Type-C power interface. This usually resolves the boot issue.

### Logging into the System

Log into the system via the serial port.

Default Username: `root`
Default Password: `starfive`

## Expected Results

The system should boot normally and allow login through the serial port.

## Actual Results

The system booted successfully and login via the serial port was successful.

### Boot Log

```log
Welcome to Buildroot
buildroot login: root
Password: 
# uname -a
Linux buildroot 5.15.0 #1 SMP Thu Mar 14 19:21:20 CST 2024 riscv64 GNU/Linux
# cat /etc/os-release 
NAME=Buildroot
VERSION=JH7110_VF2_515_v5.11.3
ID=buildroot
VERSION_ID=2021.11
PRETTY_NAME="Buildroot 2021.11"
#
```

Screen recording (From image flashing to system login):

[![asciicast](https://asciinema.org/a/EUliFJz2UOlHIxrZbK2mePVbS.svg)](https://asciinema.org/a/EUliFJz2UOlHIxrZbK2mePVbS)

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
