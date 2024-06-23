# Ubuntu on Microchip Polarfire SoC FPGA Icicle Kit

## Test Environment

### Hardware Information

- Microchip Polarfire SoC FPGA Icicle Kit development board
- Original 12V 5A DC 5.5*2.1mm power adapter (comes with US standard plug, requires an adapter/replacement with national standard plug for use in mainland China)
- Two micro-USB to USB-A cables (included), used for connecting USB-UART, updating FPGA/HSS, and flashing images to the onboard eMMC
- (Optional) An SD card (not recommended to use microSD with adapter, it may not be recognized; ensure the card is not write-protected)

### Operating System Information

- Ubuntu 24.04
    - Download link: https://cdimage.ubuntu.com/releases/24.04/release/
        - TUNA Mirror: https://mirror.tuna.tsinghua.edu.cn/ubuntu-cdimage/releases/noble/release/ubuntu-24.04-preinstalled-server-riscv64+icicle.img.xz
    - Reference Installation Document: https://wiki.ubuntu.com/RISC-V/PolarFire%20SoC%20FPGA%20Icicle%20Kit

### Other Information

- Icicle Kit Reference Design Release v2024.02
    - Download link: https://github.com/polarfire-soc/icicle-kit-reference-design/releases/tag/v2024.02
- FlashPro Express v2024.1 (packaged in Programming and Debug Tools)
    - Download link (requires login): https://www.microchip.com/en-us/products/fpgas-and-plds/fpga-and-soc-design-tools/programming-and-debug/lab

## (Optional, Recommended) Update FPGA Design and Hart Software Services (HSS)

### Installing FlashPro Express Tool

Visit the mentioned download link and download according to your operating system. 

> Note: There is a login barrier, you need to register and log in to download.
> 
> Fill in the email and other information to register for free.

This tool supports:

- Windows 10/11
- RHEL/CentOS 7.x, RHEL/CentOS 8.0-8.2
- OpenSUSE Leap 42.3 (SLES 12.3)
- Ubuntu 18.04 LTS, 20.04.3 LTS, and 22.04.1 LTS

I used Windows 11 Home x64, although the installer will prompt an unsupported system, it works fine.

Once downloaded, run and follow the default installation process. In Linux, first use `chmod +x` to grant executable permissions, then execute. Root permissions may be required.

### Update FPGA Design & HSS

Ubuntu from kernel 5.19 depends on Icicle Kit Reference Design v2022.10 or newer versions.

Download the latest version from GitHub:

https://github.com/polarfire-soc/icicle-kit-reference-design/releases

Download the `MPFS_ICICLE_BASE_DESIGN_yyyy_mm.zip` file and extract for later use.

Use the microUSB cable to connect the development board to the computer.

The development board has two microUSB interfaces, connect to the `J33` interface near the power switch to flash the FPGA, as shown in the figure below.

![Connectors](https://github.com/polarfire-soc/polarfire-soc-documentation/blob/master/reference-designs-fpga-and-development-kits/images/icicle-kit-user-guide/icicle-kit-connectors.png?raw=true)

Open FlashPro Express, click the top left menu `Project -> New Job Project`

![](./images/image.png)

Select the previously extracted `MPFS_ICICLE_BASE_DESIGN`, plug in the 12V power, power on the board, then click OK:

![alt text](./images/image-1.png)

At this point, the FPGA should be recognized. Ensure the dropdown menu on the left is set to `PROGRAM`, click `RUN` to start flashing the FPGA.

![alt text](./images/image-2.png)

A green prompt indicates success:

![alt text](./images/image-3.png)

## Flashing the Image

Polarfire SoC FPGA Icicle Kit supports booting from onboard eMMC or SD card.

By default, it prioritizes the SD card. If the SD card is missing or fails to boot, it will boot from the onboard eMMC.

### Flashing the Image to eMMC

Connect the microUSB cable to the USB OTG interface near the SD card slot, marked `J19`.

Connect the USB UART near the Ethernet interface, marked `J11`.

Your computer will recognize it as a CP2108 USB to UART. If this is the only USB to UART on your computer, four serial ports will be recognized.

On Windows, four COM ports will appear, on Linux, /dev/ttyUSB{0,1,2,3} will appear, as shown below:

![alt text](./images/image-4.png)

`Interface 0` is for `HSS` output, `Interface 1` is for U-Boot and Linux console output.

In Linux, they correspond to the first and second serial ports respectively.

| Serial Port Function    | Windows     | Linux        |
|-------------------------|-------------|--------------|
| HSS Console             | Interface 0 | /dev/ttyUSB0 |
| U-Boot & Linux Console  | Interface 1 | /dev/ttyUSB1 |

To flash an image to eMMC, connect to the `HSS` console, during startup (when prompted `Press a key to enter CLI, ESC to skip`) press any key to interrupt.

Enter: 
```
mmc
usbdmsc
```
It will prompt `Waiting for USB Host to connect`.

At this point, your computer should recognize a USB mass storage device. Use Win32DiskImager/Rufus/USBImager/dd and other tools to write the image directly.

After writing the image, press Ctrl+C in the HSS console to exit USB storage mode. The image flashing is complete.

### Flashing the Image to SD Card

Directly use Rufus/Win32DiskImager/dd and other tools to write the image to the SD card.

```shell
xzcat ubuntu-24.04-preinstalled-server-riscv64+icicle.img.xz | sudo dd of=/dev/sdX bs=4M iflag=fullblock status=progress 
```

## Booting the Development Board

Power on the development board. The second serial port will display the boot information.

> On the first boot, Ubuntu will invoke `cloud-init`. Limited by the performance of the development board, startup may take several minutes, which is expected.

Username: `ubuntu`

Password: `ubuntu`

You will be prompted to change the password upon first login, follow the instructions.

## Expected Results

The system should boot normally and allow login through the serial console.

## Actual Results

The system booted successfully and login through the serial console was also successful.

### Boot Log

Screen recording (from eMMC flashing to login):

[![asciicast](https://asciinema.org/a/ECbt7b3ltAF29zFjDDgW9NUnU.svg)](https://asciinema.org/a/ECbt7b3ltAF29zFjDDgW9NUnU)

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.

## Reference Documents

- [PolarFire SoC Software Tool Flow](https://github.com/polarfire-soc/polarfire-soc-documentation/blob/master/knowledge-base/polarfire-soc-software-tool-flow.md)
- [MPFS Icicle Kit User Guide](https://github.com/polarfire-soc/polarfire-soc-documentation/blob/master/reference-designs-fpga-and-development-kits/icicle-kit-user-guide.md)
- [Updating MPFS Kit](https://github.com/polarfire-soc/polarfire-soc-documentation/blob/master/reference-designs-fpga-and-development-kits/updating-mpfs-kit.md)
- Under CC BY 4.0 license, by Microchip Technology Inc. and its subsidiaries
