# RT-Thread CH32V208 Test Report

## Test Environment

### Operating System Information

- Source Code Link: [Community-PIO-CH32V/ch32-pio-projects](https://github.com/Community-PIO-CH32V/ch32-pio-projects)
- Reference Installation Document:
    - PlatformIO Core: [PlatformIO Installation Guide](https://docs.platformio.org/en/latest/core/installation/index.html)
    - PlatformIO CH32V: [Installation Guide](https://pio-ch32v.readthedocs.io/en/latest/installation.html)

### Hardware Information

- CH32V208WBU6-EVT-R0-1v4
- 1 USB to UART debugger
- 1 WCH-Link(E)

## Installation Steps

### Install PlatformIO Core

You can first check if the package manager includes [platformio-core](https://archlinux.org/packages/?name=platformio-core) package. If not, you can use the installation script:

```bash
curl -fsSL -o get-platformio.py https://raw.githubusercontent.com/platformio/platformio-core-installer/master/get-platformio.py
python3 get-platformio.py
```

### PlatformIO Environment Configuration

Install CH32V development environment:
```bash
pio pkg install -g -p https://github.com/Community-PIO-CH32V/platform-ch32v.git
```

Add udev rules and apply them (may need to change the GROUP based on the distribution):
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

Once WCH-Link(E) is connected to the SWD debug port, use pio to flash the image:
```bash
pio run --target upload
```

pio will automatically detect the development board. If flashing is unsuccessful, you can try to specify manually:
```bash
pio run -e your_board --target upload
```

#### Add Development Board Series

**If using the CBU6 series, please ignore**
This is because other chips are not in the default chip list, so we need to add them manually.
You can find the corresponding json file for your board in `platform-ch32v/boards`.
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

Connect to the development board via serial port.

## Expected Results

The system should start up normally, and information should be viewable through the onboard serial port.

## Actual Results

The system starts up normally, and information can be viewed through the onboard serial port.

### Boot Log

Screen recording (from compilation to startup):
[![asciicast](https://asciinema.org/a/u5gol37jO8PPqklUk7TCKHcTo.svg)](https://asciinema.org/a/u5gol37jO8PPqklUk7TCKHcTo)

**The MCU in the log below is incorrect, as the example hardcoded that string. See [main.c#L:65](https://github.com/Community-PIO-CH32V/platform-ch32v/blob/d9663011522ffa485b465a2dcdcebafa3970bcd1/examples/hello-world-rt-thread/src/main.c#L65) for reference.** The DeviceID confirms that it is indeed running on the target board.
```log
 \ | /
- RT -     Thread Operating System
 / | \     3.1.3 build Apr 25 2024
 2006 - 2019 Copyright by rt-thread team

 MCU: CH32V307
SystemClk:96000000
DeviceID: 0000051c
 www.wch.cn
msh >

```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
