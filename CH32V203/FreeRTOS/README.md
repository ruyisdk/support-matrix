# FreeRTOS CH32V203 Test Report

## Test Environment

### Operating System Information

- Source Code Link: [Community-PIO-CH32V/ch32-pio-projects](https://github.com/Community-PIO-CH32V/ch32-pio-projects)
- Reference Installation Document:
    - PlatformIO Core: [Installation Guide](https://docs.platformio.org/en/latest/core/installation/index.html)
    - PlatformIO CH32V: [Installation Guide](https://pio-ch32v.readthedocs.io/en/latest/installation.html)

### Hardware Information

- CH32V203C8T6-EVT-R0-1v0
- One USB to UART Debugger
- One WCH-Link(E)

## Installation Steps

### Install PlatformIO Core

You can first check if your package manager includes a package like [platformio-core](https://archlinux.org/packages/?name=platformio-core). If not, you can follow the installation script:

```bash
curl -fsSL -o get-platformio.py https://raw.githubusercontent.com/platformio/platformio-core-installer/master/get-platformio.py
python3 get-platformio.py
```

### PlatformIO Environment Configuration

Install the CH32V development environment:
```bash
pio pkg install -g -p https://github.com/Community-PIO-CH32V/platform-ch32v.git
```

Add udev rules and apply them (you may need to change GROUP based on the distribution):
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

Compile the code using pio:
```bash
cd platform-ch32v/examples/blinky-freertos
pio run
```

### Flashing Image

Once the WCH-Link(E) is connected to the SWD debug port, flash the image using pio:
```bash
pio run --target upload
```

If the flashing fails, you can also try manually specifying:
```bash
pio run -e your_board --target upload
```

#### Add Development Board Series

**Skip this if you are using the K8T6 series**
This is because other chips are not in the default chip list, so we need to add them manually.
You can find the corresponding json name for your board in `platform-ch32v/boards`.
```bash
cat << EOF | tee -a platformio.ini
[env:your_board]
board = your_board
EOF
```

#### Common Issues

- Error: error writing to flash at address 0x00000000 at offset 0x00000000
    - This is due to a low firmware version of WCH-Link (refer to [important-notices](https://github.com/Community-PIO-CH32V/platform-ch32v?tab=readme-ov-file#important-notices)).
    - Please use the [WCH-Link Utility](https://www.wch.cn/downloads/WCH-LinkUtility_ZIP.html) once connected to W2 with CH-Link to update automatically. **This tool is currently only available for Windows**
- Error: Read-Protect Status Currently Enabled
    - This is because the chip has write protection enabled. In Windows, you can disable it using the [WCH-Link Utility](https://www.wch.cn/downloads/WCH-LinkUtility_ZIP.html), and in Linux, you can use OpenOCD:
```bash
cd ~/.platformio/packages/tool-openocd-riscv-wch/bin
./openocd -f wch-riscv.cfg -c init -c halt -c "flash protect wch_riscv 0 last  off " -c exit
cd -
```

### Logging into the System

Connect to the development board via serial port.

## Expected Results

The system should boot properly, and information should be viewable through the onboard serial port.

## Actual Results

The system booted successfully, and information is viewable through the onboard serial port.

### Boot Log

Screen recording (from compilation to startup):
[![asciicast](https://asciinema.org/a/cykIASehMCNAffuHahF77DHbG.svg)](https://asciinema.org/a/cykIASehMCNAffuHahF77DHbG)

```log
SystemClk:96000000
DeviceID: 00000510
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

