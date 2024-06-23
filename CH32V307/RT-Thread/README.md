# RT-Thread CH32V307 Test Report

## Test Environment

### Operating System Information

- Source code link: [CH32V series project repository](https://github.com/Community-PIO-CH32V/ch32-pio-projects)
- Reference Installation Document:
    - PlatformIO Core: [Installation Guide](https://docs.platformio.org/en/latest/core/installation/index.html)
    - PlatformIO CH32V: [Installation Instructions](https://pio-ch32v.readthedocs.io/en/latest/installation.html)

### Hardware Information

- CH32V307V-EVT-R2-1v1
- A USB to UART debugger
- A WCH-Link(E)

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

Add udev rules and apply them (may need to change GROUP according to the distribution):
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

### Prepare Project Repository

Clone the relevant repositories:
```bash
git clone https://github.com/Community-PIO-CH32V/platform-ch32v.git
```

### Code Compilation

Compile the code using pio:
```bash
cd platform-ch32v/examples/hello-world-rt-thread
pio run
```

### Flashing Image

After confirming WCH-Link(E) is connected to the SWD debugging port, manually specify the development board using pio and then burn the code:
```bash
pio run -e your_board --target upload
```

#### Common Issues

- Error: error writing to flash at address 0x00000000 at offset 0x00000000
    - This is due to a low firmware version of WCH-Link. (See [important-notices](https://github.com/Community-PIO-CH32V/platform-ch32v?tab=readme-ov-file#important-notices)).
    - Please use the [WCH-Link Utility](https://www.wch.cn/downloads/WCH-LinkUtility_ZIP.html) to connect once with CH-Link on W2 to automatically update. **This tool is currently only available for Windows**
- Error: Read-Protect Status Currently Enabled
    - This is caused by the chip having write protection enabled. In Windows, we can use the [WCH-Link Utility](https://www.wch.cn/downloads/WCH-LinkUtility_ZIP.html) to disable protection. In Linux, OpenOCD can be used:
```bash
cd ~/.platformio/packages/tool-openocd-riscv-wch/bin
./openocd -f wch-riscv.cfg -c init -c halt -c "flash protect wch_riscv 0 last  off " -c exit
cd -
```

### Logging into the System

Connect to the development board via serial port.

## Expected Results

The system boots up successfully, and information can be viewed through the onboard serial port.

## Actual Results

The system boots up successfully, and information can be viewed through the onboard serial port.

### Boot Log

Screen recording (from compilation to boot):
[![asciicast](https://asciinema.org/a/1oVzw3PJ1k0wQM9HYsBR8q3hl.svg)](https://asciinema.org/a/1oVzw3PJ1k0wQM9HYsBR8q3hl)


```log
 \ | /
- RT -     Thread Operating System
 / | \     3.1.3 build Apr 25 2024
 2006 - 2019 Copyright by rt-thread team

 MCU: CH32V307
SystemClk:96000000
ChipID: 30700528
 www.wch.cn
msh >

```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
