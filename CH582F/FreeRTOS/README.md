# FreeRTOS CH582F Test Report

## Test Environment

### Operating System Information

- Source Code Link: [CH32V PIO Projects](https://github.com/Community-PIO-CH32V/ch32-pio-projects)
- Reference Installation Document:
    - PlatformIO Core: [Installation Guide](https://docs.platformio.org/en/latest/core/installation/index.html)
    - PlatformIO CH32V: [Installation Guide](https://pio-ch32v.readthedocs.io/en/latest/installation.html)

### Hardware Information

- CH582F-EVT-R2-1v0-BC
- 1 x USB to UART Debugger
- 1 x USB Type-C Cable

## Installation Steps

### Install PlatformIO Core

You can first check if the package manager includes a package like [platformio-core](https://archlinux.org/packages/?name=platformio-core). If not, you can use the installation script:

```bash
curl -fsSL -o get-platformio.py https://raw.githubusercontent.com/platformio/platformio-core-installer/master/get-platformio.py
python3 get-platformio.py
```

### PlatformIO Environment Configuration

Install the CH32V development environment:
```bash
pio pkg install -g -p https://github.com/Community-PIO-CH32V/platform-ch32v.git
```

Add udev rules and apply them (you may need to change GROUP based on your distribution):
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
- For Debian-based systems:
```bash
sudo usermod -a -G dialout $USER
sudo usermod -a -G plugdev $USER
```
- For Arch-based systems:
```bash
sudo usermod -a -G uucp $USER
sudo usermod -a -G lock $USER
```

### Prepare Project Repository

Clone the relevant repositories:
```bash
git clone https://github.com/Community-PIO-CH32V/platform-ch32v.git
```

### Code Compilation

Use `pio` to compile the code:
```bash
cd platform-ch32v/examples/blinky-freertos-ch58x
pio run
```

### Flashing Image

Connect the development board to the computer using the Type-C cable, then press and hold the boot button while toggling the switch. Quickly execute:
```bash
pio run -e your_board --target upload
```


### Logging into the System

Connect to the development board via serial port.

## Expected Results

The system should boot up correctly, and information should be viewable via the onboard serial port.

## Actual Results

The system booted up correctly, and information was viewable via the onboard serial port.

### Boot Log

Screen recording (from compilation to boot):
[![asciicast](https://asciinema.org/a/ZGVaNo7NxIiI7lJA0w0cM6nCX.svg)](https://asciinema.org/a/ZGVaNo7NxIiI7lJA0w0cM6nCX)

```log
start.
      task2 entry 1
                   task1 entry 1
                                task1 entry 2
                                             task2 entry 2
                                                          task1 entry 1

```
## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
