# FreeRTOS CH32V307 Test Report

## Test Environment

### Operating System Information

- Source Code Link: [https://github.com/Community-PIO-CH32V/ch32-pio-projects](https://github.com/Community-PIO-CH32V/ch32-pio-projects)
- Reference Installation Document:
    - PlatformIO Core: [https://docs.platformio.org/en/latest/core/installation/index.html](https://docs.platformio.org/en/latest/core/installation/index.html)
    - PlatformIO CH32V: [https://pio-ch32v.readthedocs.io/en/latest/installation.html](https://pio-ch32v.readthedocs.io/en/latest/installation.html)

### Hardware Information

- CH32V307V-EVT-R2-1v1
- A USB to UART Debugger
- A WCH-Link(E)

## Installation Steps

### Install PlatformIO Core

You can first check if the package manager includes a package like [platformio-core](https://archlinux.org/packages/?name=platformio-core). If not, you can install it using the installation script:

```bash
curl -fsSL -o get-platformio.py https://raw.githubusercontent.com/platformio/platformio-core-installer/master/get-platformio.py
python3 get-platformio.py
```

### PlatformIO Environment Configuration

Install CH32V development environment:
```bash
pio pkg install -g -p https://github.com/Community-PIO-CH32V/platform-ch32v.git
```

Add udev rules and apply (may need to change GROUP according to the distribution):
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

Compile the code using pio:
```bash
cd platform-ch32v/examples/blinky-freertos
pio run
```

### Flashing Image

After confirming the connection of WCH-Link(E) to the SWD debug port, manually specify the development board using pio and burn the image:
```bash
pio run -e your_board --target upload
```

#### Common Issues

- **Error: error writing to flash at address 0x00000000 at offset 0x00000000**
    - This is due to the low firmware version of WCH-Link. (See [important-notices](https://github.com/Community-PIO-CH32V/platform-ch32v?tab=readme-ov-file#important-notices)).
    - Please use [WCH-Link Utility](https://www.wch.cn/downloads/WCH-LinkUtility_ZIP.html) to connect once with W2 and CH-Link to update automatically. **This tool currently only has a Windows version.**
- **Error: Read-Protect Status Currently Enabled**
    - This is caused by the write protection enabled on the chip. On Windows, we can use [WCH-Link Utility](https://www.wch.cn/downloads/WCH-LinkUtility_ZIP.html) to remove the protection, and on Linux, OpenOCD can be used:
```bash
cd ~/.platformio/packages/tool-openocd-riscv-wch/bin
./openocd -f wch-riscv.cfg -c init -c halt -c "flash protect wch_riscv 0 last  off " -c exit
cd -
```

### Logging into the System

Connect to the development board via serial port.

## Expected Results

The system starts normally, and information can be viewed via the onboard serial port.

## Actual Results

The system starts normally, and information can be viewed via the onboard serial port.

### Boot Log

Screen recording (from compilation to startup):
[![asciicast](https://asciinema.org/a/NZ9udm2pNnA11dERnWfv0Nld9.svg)](https://asciinema.org/a/NZ9udm2pNnA11dERnWfv0Nld9)

```log
SystemClk:96000000
ChipID: 30700528
FreeRTOS Kernel Version:V10.4.6
task2 entry
task1 entry
task1 entry
task2 entry
task1 entry
task1 entry
task2 entry
task1 entry
task1 entry
task2 entry
```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
