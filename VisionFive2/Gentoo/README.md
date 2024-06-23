# Gentoo VisionFive 2 Test Report

## Test Environment

### Operating System Information

- System Version: gentoo.img.bz2
- Download Link: [Google Drive](https://drive.google.com/file/d/10TDsk2FwZDJv3yJvDAfCam5Wf9ibS6Eg/view?usp=sharing)
- Reference Installation Document: [Forum Link](https://forum.rvspace.org/t/experimental-gentoo-image/1807)

> This image is provided by community developers and is not an official release.

### Hardware Information

- StarFive VisionFive 2
- A USB power adapter
- A USB-A to C or C to C cable
- A microSD card
- A USB to UART debugger (e.g., CH340, CH341, FT2232, etc.)
- Three Dupont wires

## Installation Steps

### Decompress and Flash the Image to the microSD Card

Assuming `/dev/sdc` is the storage card.

```bash
bzcat gentoo.img.bz2 | sudo dd of=/dev/sdc iflag=fullblock bs=4M status=progress
```

### Boot Mode Selection

StarFive VisionFive 2 offers various boot modes, configurable via onboard dip switches before powering on. The specific modes are labeled on the development board.

To boot the Gentoo image, select the 1-bit QSPI Nor Flash mode (i.e., `RGPIO_0 = 0`, `RGPIO_1 = 0`). Note that this mode may require prior firmware updates in the Flash. If the boot is unsuccessful, refer to the official documentation for firmware updates: [Update SPL and U-Boot](https://doc.rvspace.org/VisionFive2/Quick_Start_Guide/VisionFive2_QSG/spl_u_boot_0.html)

### Logging into the System

Logging into the system via the serial port.

Username: `root`
No password.

## Expected Results

The system should boot normally and allow login via the serial port.

## Actual Results

The system booted successfully and login via the serial port was successful.

### Boot Log

```log
root@StarFive ~ # uname -a                                                                                                          
Linux StarFive 5.15.0-starfive #1 SMP Mon Feb 27 14:03:14 EST 2023 riscv64 GNU/Linux                                                
root@StarFive ~ # cat /etc/os-release                                                                                               
NAME=Gentoo                                                                                                                         
ID=gentoo                                                                                                                           
PRETTY_NAME="Gentoo Linux"                                                                                                          
ANSI_COLOR="1;32"                                                                                                                   
HOME_URL="https://www.gentoo.org/"                                                                                                  
SUPPORT_URL="https://www.gentoo.org/support/"                                                                                       
BUG_REPORT_URL="https://bugs.gentoo.org/"                                                                                           
VERSION_ID="2.13"                                                                                                                   
root@StarFive ~ #
```

Screen recording (from flashing the image to logging into the system):

[![asciicast](https://asciinema.org/a/HYfHc1I7NtPlUkfSuY7W1cy5e.svg)](https://asciinema.org/a/HYfHc1I7NtPlUkfSuY7W1cy5e)

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
