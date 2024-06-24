# RT-Thread CH32V103C Test Report

## Test Environment

### Operating System Information

- Source Code Link: [CH32V GitHub Repository](https://github.com/Community-PIO-CH32V/ch32-pio-projects)
- Reference Installation Document:
    - PlatformIO Core: [Installation Guide](https://docs.platformio.org/en/latest/core/installation/index.html)
    - PlatformIO CH32V: [Installation Guide](https://pio-ch32v.readthedocs.io/en/latest/installation.html)

### Hardware Information

- CH32V103C8T6-EVT-R1
- 1 x USB to UART Debugger
- 1 x WCH-Link(E)


## Installation Steps

### Install PlatformIO Core

You can first check if there is a package like [platformio-core](https://archlinux.org/packages/?name=platformio-core) available in the package manager. If not, you can use the installation script:

```bash
curl -fsSL -o get-platformio.py https://raw.githubusercontent.com/platformio/platformio-core-installer/master/get-platformio.py
python3 get-platformio.py
```

### PlatformIO Environment Configuration

Install the CH32V development environment:
```bash
pio pkg install -g -p https://github.com/Community-PIO-CH32V/platform-ch32v.git
```

Add udev rules and apply (may need to change GROUP depending on the distribution):
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

Once the WCH-Link(E) is connected to the SWD debug port, flash the image using pio:
```bash
pio run --target upload
```

pio will automatically detect the development board. In case of unsuccessful flashing, you can also try manual specification:
```bash
pio run -e your_board --target upload
```

#### Adding Development Board Series

**If using the C8T6 series, please ignore**
This is because other chips are not in the default chip list, and we need to add them manually.
You can find the corresponding json name for your board in `platform-ch32v/boards`.
```bash
cat << EOF | tee -a platformio.ini
[env:your_board]
board = your_board
EOF
```

#### Common Issues

- Error: error writing to flash at address 0x00000000 at offset 0x00000000
    - This is due to the low firmware version of the WCH-Link. (See [important-notices](https://github.com/Community-PIO-CH32V/platform-ch32v?tab=readme-ov-file#important-notices)).
    - Please use the [WCH-Link Toolchain](https://www.wch.cn/downloads/WCH-LinkUtility_ZIP.html) to connect once to W2 with CH-Link for automatic update. **Currently, this tool is only available for Windows**
- Error: Read-Protect Status Currently Enabled
    - This is due to the chip's write protection being enabled. On Windows, we can use the [WCH-Link Toolchain](https://www.wch.cn/downloads/WCH-LinkUtility_ZIP.html) to disable protection, and on Linux, OpenOCD can be used:
```bash
cd ~/.platformio/packages/tool-openocd-riscv-wch/bin
./openocd -f wch-riscv.cfg -c init -c halt -c "flash protect wch_riscv 0 last  off " -c exit
cd -
```

### Logging into the System

Logging into the system via serial port.

## Expected Results

The system should boot up properly and allow connect via the onboard serial port.

## Actual Results

The system should boot up properly and allow connect via the onboard serial port.

### Boot Log

Screen recording (from compilation to startup):

[![asciicast](https://asciinema.org/a/sMyZu9dVD4q4BGA9FZbJDna3g.svg)](https://asciinema.org/a/sMyZu9dVD4q4BGA9FZbJDna3g)

**The MCU shown in the log below is incorrect, as the example hardcodes that string. See [main.c#L:65](https://github.com/Community-PIO-CH32V/platform-ch32v/blob/d9663011522ffa485b465a2dcdcebafa3970bcd1/examples/hello-world-rt-thread/src/main.c#L65)**
Based on the Device ID, it indeed running on a target board.
```log
 \ | /
- RT -     Thread Operating System
 / | \     3.1.3 build Apr 25 2024
 2006 - 2019 Copyright by rt-thread team

 MCU: CH32V307
SystemClk:72000000
DeviceID: 0000410f
 www.wch.cn
msh >

```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.

