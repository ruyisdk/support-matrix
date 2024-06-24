# RT-Thread CH32V203 Test Report

## Test Environment

### Operating System Information

- Source code link: https://github.com/Community-PIO-CH32V/ch32-pio-projects
- Reference Installation Document:
    - PlatformIO Core: https://docs.platformio.org/en/latest/core/installation/index.html
    - PlatformIO CH32V: https://pio-ch32v.readthedocs.io/en/latest/installation.html

### Hardware Information

- CH32V203G6U6-EVT-R0-1v0
- A USB to UART debugger
- A WCH-Link(E)

## Installation Steps

### Install PlatformIO Core

You can first check if the package manager contains the [platformio-core](https://archlinux.org/packages/?name=platformio-core) package. If not, you can install using the installation script:

```bash
curl -fsSL -o get-platformio.py https://raw.githubusercontent.com/platformio/platformio-core-installer/master/get-platformio.py
python3 get-platformio.py
```

### PlatformIO Environment Configuration

Install CH32V development environment:
```bash
pio pkg install -g -p https://github.com/Community-PIO-CH32V/platform-ch32v.git
```

Add udev rules and apply (you may need to change GROUP according to the distribution):
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
- Debian series:
```bash
sudo usermod -a -G dialout $USER
sudo usermod -a -G plugdev $USER
```
- Arch series:
```bash
sudo usermod -a -G uucp $USER
sudo usermod -a -G lock $USER
```

### Prepare Project Repository

Clone relevant repositories:
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

Ensure WCH-Link(E) is connected to the SWD debug port, then use pio to flash the image:
```bash
pio run --target upload
```

If the flashing is unsuccessful, you can try manually specifying:
```bash
pio run -e your_board --target upload
```

#### Add Development Board Series

**If you are using the C8T6 series, please ignore this step.**
This is because other chips are not included in the default chip list, so we need to add them manually.
You can find the json file corresponding to your board in `platform-ch32v/boards`.
```bash
cat << EOF | tee -a platformio.ini
[env:your_board]
board = your_board
EOF
```

#### Common Issues

- Error: error writing to flash at address 0x00000000 at offset 0x00000000
    - This is due to the low firmware version of WCH-Link. (See [important-notices](https://github.com/Community-PIO-CH32V/platform-ch32v?tab=readme-ov-file#important-notices)).
    - Please connect WCH-Link once using the [WCH-Link Utility](https://www.wch.cn/downloads/WCH-LinkUtility_ZIP.html) on Windows to automatically update. **Currently, this tool is only available for Windows.**
- Error: Read-Protect Status Currently Enabled
    - This is caused by the chip's write protection being enabled. On Windows, we can use the [WCH-Link Utility](https://www.wch.cn/downloads/WCH-LinkUtility_ZIP.html) to disable protection, and on Linux, OpenOCD can be used to disable protection:
```bash
cd ~/.platformio/packages/tool-openocd-riscv-wch/bin
./openocd -f wch-riscv.cfg -c init -c halt -c "flash protect wch_riscv 0 last  off " -c exit
cd -
```

### Logging into the System

Connect to the development board via serial port.

## Expected Results

The system should boot up normally, and information should be viewable through the onboard serial port.

## Actual Results

The system booted up normally, and information was viewable through the onboard serial port.

### Boot Log

Screen recording (from compile to startup):
[![asciicast](https://asciinema.org/a/JIVraodV8i3W0YDnv8yLk2zLq.svg)](https://asciinema.org/a/JIVraodV8i3W0YDnv8yLk2zLq)

**The MCU shown in the log below is incorrect, as the example hardcodes that string. See [main.c#L:65](https://github.com/Community-PIO-CH32V/platform-ch32v/blob/d9663011522ffa485b465a2dcdcebafa3970bcd1/examples/hello-world-rt-thread/src/main.c#L65)**
The DeviceID confirms that it is indeed running on the target board.
```log
 \ | /
- RT -     Thread Operating System
 / | \     3.1.3 build Apr 25 2024
 2006 - 2019 Copyright by rt-thread team

 MCU: CH32V307
SystemClk:96000000
DeviceID: 00000510
 www.wch.cn
msh >

```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
