# openEuler RISC-V 23.09 VisionFive 2 Test Report

## Test Environment

### Operating System Information

- System Version: openEuler 23.09 RISC-V preview
- Download Link: https://mirror.iscas.ac.cn/openeuler-sig-riscv/openEuler-RISC-V/preview/openEuler-23.09-V1-riscv64/VisionFive2/
- Reference Installation Document: https://gitee.com/openeuler/RISC-V/blob/master/release/openEuler-23.03/Installation_Book/Visionfive2/README.md

### Hardware Information

- StarFive VisionFive 2
- A USB power adapter
- A USB-A to C or C to C cable
- A microSD card
- A USB to UART debugger (e.g., CH340, CH341, FT2232)
- Three DuPont lines

## Installation Steps

### Flashing the Image to microSD Card using `ruyi` CLI

Install the [`ruyi`](https://github.com/ruyisdk/ruyi) package manager, run `ruyi device provision`, and follow the instructions.

### Boot Mode Selection

StarFive VisionFive 2 provides multiple boot modes, configurable via the onboard dip switch before powering on. Refer to the StarFive [official documentation](https://doc.rvspace.org/VisionFive2/Quick_Start_Guide/VisionFive2_SDK_QSG/boot_mode_settings.html).

The board itself also has silkscreen labels.

To boot the openEuler image, select the 1-bit QSPI Nor Flash mode (`RGPIO_0 = 0`, `RGPIO_1 = 0`). Note that this mode might require prior firmware updates in the Flash, detailed in the official documentation: [Updating SPL and U-Boot](https://doc.rvspace.org/VisionFive2/Quick_Start_Guide/VisionFive2_QSG/spl_u_boot_0.html).

If not updating the firmware, choose microSD card boot (`RGPIO_0 = 1`, `RGPIO_1 = 0`).

> Note: In this mode, there is a small chance of boot failure. If boot fails, serial output might show information similar to the following:
>
> ```log
>dwmci_s: Response Timeout.                                                                                            
>dwmci_s: Response Timeout.                                                                                            
>BOOT fail,Error is 0xffffffff
>```
>
> You can try re-powering the development board or pressing the button near the USB Type-C power interface. This usually resolves the boot issue.

### Logging into the System

Log into the system via the serial port.

Default Username: `openeuler` or `root`  
Default Password: `openEuler12#$`

## Expected Results

The system should boot normally and allow login through the graphical interface.

## Actual Results

The system booted normally and login through the graphical interface was successful.

### Boot Log

Screen recording (from flashing the image to system login):
[![asciicast](https://asciinema.org/a/A3KitOgctHGhyUvkUd2a8LwsH.svg)](https://asciinema.org/a/A3KitOgctHGhyUvkUd2a8LwsH)

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
