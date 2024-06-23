# Ubuntu BeagleV-Fire Test Report

## Test Environment

### System Information

- Download Link: [BeagleV-Fire Ubuntu Image](https://files.beagle.cc/file/beagleboard-public-2021/images/beaglev-fire-ubuntu-23.04-20231121.zip)
- Reference Installation Document: [BeagleV Fire Flashing Guide](https://docs.beagleboard.org/latest/boards/beaglev/fire/demos-and-tutorials/flashing-board.html)

### Hardware Information

- BeagleV-Fire
- USB-C Power Adapter / DC Power Supply
- USB-UART Debugger

## Installation Steps

### Flashing Gatware Module

**In theory, the Gatware should be pre-flashed and ready to use out of the box.**

### Gatware Upgrade

**The Gatware upgrade can be directly performed in the pre-installed Linux on the board**, refer to [official documentation](https://docs.beagleboard.org/latest/boards/beaglev/fire/demos-and-tutorials/gateware/upgrade-gateware.html)

Upon accessing the Linux command line (via SSH, UART, etc.)
```bash
sudo apt install bbb.io-gateware
sudo apt update
sudo apt upgrade
cd /usr/share/beagleboard/gateware
. ./change-gateware.sh default
```

### Flashing Gatware

Download FlashPro Express from here:
https://www.microchip.com/en-us/products/fpgas-and-plds/fpga-and-soc-design-tools/programming-and-debug

Once downloaded, proceed with the installation:
```bash
./launch_installer.sh
```

Launch the software:
```bash
/home/$(user)/microchip/Program_Debug_v202X.Y/Program_Debug_Tool/bin/FPExpress
```

Download FlashProExpress.zip, which contains the necessary project files (*.job)

Create a project and flash (connect to the development board):
![alt text](image.png)
- Select working file
- Choose project location
- Confirm

![alt text](image-1.png)
- Choose the Program action
- Click execute

### Flashing Image

Connect the computer to the development board using both serial port and USB cables.

Once the DDR Training loading bar appears, interrupt the boot by pressing any key \[a-zA-Z0-9\], then proceed manually:
```bash
>> mmc
>> usbdmsc
```

A new storage device should appear on your computer. Burn the image into it:
```bash
sudo dd if=sdcard.img of=/dev/your/device bs=1M status=progress
```

### Logging into the System

Access the system via serial port.

Default username: `root`
Default password: None

## Expected Results

The system should boot up normally, allowing login via the onboard serial port.

## Actual Results

CFT

### Boot Log

Screen recording (from flashing the image to system login):


```log

```


## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

CFT
