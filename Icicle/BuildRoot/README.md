# Buildroot Icicle Kit Test Report

## Test Environment

### System Information

### Operating System Information

- System Version: Buildroot
- Source Code Link: https://buildroot.org/download.html
    - As of the writing of this report, the latest stable / LTS version of Buildroot is: [buildroot-2024.02.2](https://buildroot.org/downloads/buildroot-2024.02.2.tar.gz)
- Reference Installation Document: https://gitlab.com/buildroot.org/buildroot/-/tree/master/board/visionfive?ref_type=heads
- Build Machine System: Arch Linux x86_64

### Hardware Information

- Microchip Polarfire SoC FPGA Icicle Kit Development Board
- Original 12V 5A DC 5.5*2.1mm Power Adapter (Original cable comes with US plug; if using in mainland China, an adapter or national standard cable is required)
- Two micro-USB to USB-A cables (included with the product), used for connecting USB-UART, updating FPGA/HSS, and flashing the image to onboard eMMC
- (Optional) An SD card (Using microSD with an adapter is not recommended as it might not be recognized; also, ensure the storage card is not write-protected)

## Building and Flashing the Image

Since the PolarFire SoC FPGA Icicle Kit has been mainlined into Buildroot, you can directly obtain the source code from Buildroot to build a usable image.

### Preparing the Build Environment

```shell
sudo pacman -S which sed make binutils diffutils gcc bash patch gzip bzip2 perl tar cpio unzip rsync file bc findutils wget
# Or using package from AUR
# paru -S buildroot-meta
```

If you are not using Arch Linux, please refer to the [official documentation](https://buildroot.org/downloads/manual/manual.html#requirement) to install the necessary dependencies (note that package names may vary).

### Building the Image

```shell
wget https://buildroot.org/downloads/buildroot-2024.02.2.tar.gz
tar xvf buildroot-2024.02.2.tar.gz
cd buildroot-2024.02.2/
make microchip_mpfs_icicle_defconfig
make -j$(nproc)
```

Note: Ensure that you have a stable internet connection as dependencies will be downloaded automatically during the build process.

Upon completion, an `sdcard.img` image will be generated in the `output/images` directory.

### (Optional) Updating FPGA Design and Hart Software Services (HSS)

This step is not mandatory; if you encounter issues, you may try updating the FPGA and HSS.

Refer to the steps mentioned in the [Ubuntu](../Ubuntu/README.md) documentation for updates.

### Flashing the Image

The PolarFire SoC FPGA Icicle Kit supports booting from the onboard eMMC or an SD card.

By default, it prioritizes the SD card. If the SD card is not present or SD card boot fails, it boots from the onboard eMMC.

### Flashing the Image to eMMC

Connect the microUSB cable to the USB OTG port near the SD card slot, silkscreen `J19`.

Connect the USB UART near the Ethernet port, silkscreen `J11`.

Your computer will recognize a CP2108 USB to UART. If this is the only USB to UART on your computer, it will recognize four serial ports.

On Windows, four COM ports will appear, while on Linux, they will be /dev/ttyUSB{0,1,2,3}.

Among these, `Interface 0` provides `HSS` output, and `Interface 1` provides U-Boot and Linux console output.

On Linux systems, these correspond to the first and second serial ports, respectively.

| Serial Port Function   | Windows     | Linux        |
|------------------------|-------------|--------------|
| HSS Console            | Interface 0 | /dev/ttyUSB0 |
| U-Boot & Linux Console | Interface 1 | /dev/ttyUSB1 |

To flash the image to eMMC, connect to the `HSS` console. During startup (when prompted `Press a key to enter CLI, ESC to skip`), press any key to interrupt the startup process.

Enter:

```
mmc
usbdmsc
```

It will prompt `Waiting for USB Host to connect`.

At this point, a USB mass storage device should appear on your computer. You can now use Win32DiskImager/Rufus/USBImager/dd or similar tools to directly write the image.

After flashing the image, press Ctrl+C in the HSS console to exit USB storage mode. This completes the image flashing process.

### Flashing the Image to SD Card

Simply use Rufus/Win32DiskImager/dd or similar tools to write the image to an SD card.

```shell
sudo dd if=sdcard.img of=/dev/sdX bs=1M status=progress
```

### Logging into the System

Log into the system via serial port.

Default Username: `root`

Default Password: None, login occurs automatically after entering the username

## Expected Results

The system should boot normally and allow login via the onboard serial port.

## Actual Results

The system booted successfully and login via the onboard serial port was also successful.

### Boot Log

```log
Welcome to Buildroot
mpfs_icicle login: root
# uname -a
Linux mpfs_icicle 6.1.74-linux4microchip+fpga-2024.02 #1 SMP Mon May 13 18:29:54 CST 2024 riscv64 GNU/Linux
# cat /etc/os-release
NAME=Buildroot
VERSION=2024.02.2
ID=buildroot
VERSION_ID=2024.02.2
PRETTY_NAME="Buildroot 2024.02.2"
# cat /proc/cpuinfo
processor       : 0
hart            : 1
isa             : rv64imafdc
mmu             : sv39
uarch           : sifive,u54-mc
mvendorid       : 0x1cf
marchid         : 0x1
mimpid          : 0x0

processor       : 1
hart            : 2
isa             : rv64imafdc
mmu             : sv39
uarch           : sifive,u54-mc
mvendorid       : 0x1cf
marchid         : 0x1
mimpid          : 0x0

processor       : 2
hart            : 3
isa             : rv64imafdc
mmu             : sv39
uarch           : sifive,u54-mc
mvendorid       : 0x1cf
marchid         : 0x1
mimpid          : 0x0

processor       : 3
hart            : 4
isa             : rv64imafdc
mmu             : sv39
uarch           : sifive,u54-mc
mvendorid       : 0x1cf
marchid         : 0x1
mimpid          : 0x0

#
```

Screen recording (from image flashing to login):

[![asciicast](https://asciinema.org/a/js18pAh0YMTp0g9bQD1tXsBgH.svg)](https://asciinema.org/a/js18pAh0YMTp0g9bQD1tXsBgH)

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
