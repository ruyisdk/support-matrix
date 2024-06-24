# RT-Thread Nuclei DDR200T Test Report

## Test Environment

### Operating System Information

- Source Code Link: https://github.com/Community-PIO-CH32V/ch32-pio-projects
- Reference Documents:
    - PlatformIO Core: https://docs.platformio.org/en/latest/core/installation/index.html
    - PlatformIO ch32v: https://pio-ch32v.readthedocs.io/en/latest/installation.html

### Hardware Information

- Nuclei DDR200T Development Board

## Installation Steps

### Installing PlatformIO Core

First, check if your package manager includes a package like [platformio-core](https://archlinux.org/packages/?name=platformio-core). If not, you can use the installation script:

```bash
curl -fsSL -o get-platformio.py https://raw.githubusercontent.com/platformio/platformio-core-installer/master/get-platformio.py
python3 get-platformio.py
```

### Configuring the PlatformIO Environment

Install the Nuclei development environment:
```bash
pio pkg install --global --platform "nuclei/nuclei@^1.0.11"
```

Add udev rules and apply them (the GROUP might need to be adjusted depending on the distribution):
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

Add user group:
- Debian-based:
```bash
sudo usermod -a -G dialout $USER
sudo usermod -a -G plugdev $USER
```
- Arch-based:
```bash
sudo usermod -a -G uucp $USER
sudo usermod -a -G lock $USER
```

### Preparing the Project Repository

Clone the relevant repository:
```bash
git clone https://github.com/Nuclei-Software/platform-nuclei.git
```

### Compiling the Code

Compile the code using pio:
```bash
cd cd platform-nuclei/examples/rtthread_demo
pio run
```

### Flashing the Image

Once the WCH-Link(E) is connected to the SWD debugging port, use pio to flash the image:
```bash
pio run --target upload
```

pio will automatically detect the development board. If flashing is unsuccessful, you can try specifying it manually:
```bash
pio run -e hbird_eval --target upload
```

### Logging into the System

Connect to the board via the serial port.

## Expected Results

The system should boot normally and information should be viewable through the onboard serial port.

## Actual Results

CFT

### Boot Log

Screen recording (from compilation to startup):

```log
```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

CFT
