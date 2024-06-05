# FreeRTOS CH32V103 PlatformIO Test Report

## Test Environment

### Operating System Information

- Source Code Link: https://github.com/Community-PIO-CH32V/ch32-pio-projects
- Reference Installation Document:
    - PlatformIO Core: https://docs.platformio.org/en/latest/core/installation/index.html
    - PlatformIO CH32V: https://pio-ch32v.readthedocs.io/en/latest/installation.html

### Hardware Information

- CH32V103C8T6-EVT-R1
- 1 USB to UART debugger
- 1 WCH-Link(E)

## Installation Steps

### Install PlatformIO Core

You can first check if the package manager includes [platformio-core](https://archlinux.org/packages/?name=platformio-core). If not, you can use the installation script:

```bash
curl -fsSL -o get-platformio.py https://raw.githubusercontent.com/platformio/platformio-core-installer/master/get-platformio.py
python3 get-platformio.py
```

### PlatformIO Environment Configuration

Install CH32V development environment:
```bash
pio pkg install -g -p https://github.com/Community-PIO-CH32V/platform-ch32v.git
```

Add udev rules and apply them (may need to adjust GROUP based on the distribution):
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

Clone the relevant repository:
```bash
git clone https://github.com/Community-PIO-CH32V/platform-ch32v.git
```

### Code Compilation

Compile the code using pio:
```bash
cd platform-ch32v/examples/blinky-freertos
pio run
```

### Flashing Image

After confirming the connection of WCH-Link(E) to the SWD debug port, use pio to flash the image:
```bash
pio run --target upload
```

If the flashing fails, you can try to specify it manually:
```bash
pio run -e your_board --target upload
```

#### Add Development Board Series

**Ignore this step if you are using the C8T6 series**
This is because other chips are not in the default chip list, so we need to manually add them. You can find the corresponding JSON name for your board in `platform-ch32v/boards`.
```bash
cat << EOF | tee -a platformio.ini
[env:your_board]
board = your_board
EOF
```

#### Common Issues

- Error: error writing to flash at address 0x00000000 at offset 0x00000000
    - This is caused by a low firmware version of WCH-Link. (See [important-notices](https://github.com/Community-PIO-CH32V/platform-ch32v?tab=readme-ov-file#important-notices)).
    - Please connect once with the [WCH-Link Utility](https://www.wch.cn/downloads/WCH-LinkUtility_ZIP.html) to update using CH-Link. **This tool is currently only available for Windows**
- Error: Read-Protect Status Currently Enabled
    - This is caused by write protection being enabled on the chip. In Windows, we can use the [WCH-Link Utility](https://www.wch.cn/downloads/WCH-LinkUtility_ZIP.html) to remove the protection. In Linux, OpenOCD can be used:
```bash
cd ~/.platformio/packages/tool-openocd-riscv-wch/bin
./openocd -f wch-riscv.cfg -c init -c halt -c "flash protect wch_riscv 0 last  off " -c exit
cd -
```

### Logging into the System

Connect to the development board through a serial port.

## Expected Results

The system should boot up normally, and information should be viewable through the onboard serial port.

## Actual Results

The system booted up normally, and information was viewable through the onboard serial port.

### Boot Log

Screen recording (from compilation to startup):
[![asciicast](https://asciinema.org/a/IstntoTjF0bRKSFrRoOWQ1Th9.svg)](https://asciinema.org/a/IstntoTjF0bRKSFrRoOWQ1Th9)

```log
SystemClk:72000000
DeviceID: 0000410f
FreeRTOS Kernel Version:V10.4.6
task2 entry
task1 entry
task1 entry
task2 entry
task1 entry
task1 entry

```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
