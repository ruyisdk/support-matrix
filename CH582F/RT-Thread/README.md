
# RT-Thread CH582F Test Report

## Test Environment

### Operating System Information

- Source code link: [Community-PIO-CH32V/ch32-pio-projects](https://github.com/Community-PIO-CH32V/ch32-pio-projects)
- Reference Installation Document:
    - PlatformIO Core: [Installation Guide](https://docs.platformio.org/en/latest/core/installation/index.html)
    - PlatformIO CH32V: [Installation Instructions](https://pio-ch32v.readthedocs.io/en/latest/installation.html)

### Hardware Information

- CH582F-EVT-R2-1v0-BC
- 1 USB to UART debugger
- 1 USB Type-C cable

## Installation Steps

### Installing PlatformIO Core

You can first check if the package manager includes a package like [platformio-core](https://archlinux.org/packages/?name=platformio-core). If not, you can install using the installation script:

```bash
curl -fsSL -o get-platformio.py https://raw.githubusercontent.com/platformio/platformio-core-installer/master/get-platformio.py
python3 get-platformio.py
```

### PlatformIO Environment Configuration

Install CH32V development environment:
```bash
pio pkg install -g -p https://github.com/Community-PIO-CH32V/platform-ch32v.git
```

Add udev rules and apply (may need to change GROUP according to the Linux distribution):
```bash
curl -fsSL https://raw.githubusercontent.com/platformio/platformio-core/develop/platformio/assets/system/99-platformio-udev.rules | sudo tee /etc/udev/rules.d/99-platformio-udev.rules
cat << EOF | sudo tee -a /etc/udev/rules.d/99-platformio-udev.rules
SUBSYSTEM=="usb", ATTR{idVendor}="1a86", ATTR{idProduct}=="8010", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}="4348", ATTR{idProduct}=="55e0", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}="1a86", ATTR{idProduct}=="8012", GROUP="plugdev"
EOF
sudo udevadm control --reload-rules
sudo udevadm trigger
```

Add user groups:
- Debian-based systems:
```bash
sudo usermod -a -G dialout $USER
sudo usermod -a -G plugdev $USER
```
- Arch-based systems:
```bash
sudo usermod -a -G uucp $USER
sudo usermod -a -G lock $USER
```

### Setting up Project Repository

Clone the relevant repositories:
```bash
git clone https://github.com/Community-PIO-CH32V/platform-ch32v.git
```

### Code Compilation

Compile the code using pio:
```bash
cd platform-ch32v/examples/hello-world-rt-thread-ch5xx
pio run
```

### Flashing Image

Connect the development board to the computer using the Type-C cable, press and hold the boot button, then quickly run:
```bash
pio run -e your_board --target upload
```

### Logging into the System

Connect to the development board via serial port.

## Expected Results

The system should start up successfully, and information should be viewable through the onboard serial port.

## Actual Results

The system started up successfully, and information was viewable through the onboard serial port.

### Boot Log

Screen recording (from compilation to boot):
[![asciicast](https://asciinema.org/a/kDeNAs3hbHNSUwWVhSR7raPMJ.svg)](https://asciinema.org/a/kDeNAs3hbHNSUwWVhSR7raPMJ)

```log
 \ | /
- RT -     Thread Operating System
 / | \     3.1.5 build Apr 25 2024
 2006 - 2020 Copyright by rt-thread team
task1
task2
msh >task2
task1
task2
task1
task2


```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
