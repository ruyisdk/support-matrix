# RT-Thread CH32V303 Test Report

## Test Environment

### Operating System Information

- Source Code Link: [https://github.com/Community-PIO-CH32V/ch32-pio-projects](https://github.com/Community-PIO-CH32V/ch32-pio-projects)
- Reference Installation Document:
    - PlatformIO Core: [https://docs.platformio.org/en/latest/core/installation/index.html](https://docs.platformio.org/en/latest/core/installation/index.html)
    - PlatformIO CH32V: [https://pio-ch32v.readthedocs.io/en/latest/installation.html](https://pio-ch32v.readthedocs.io/en/latest/installation.html)

### Hardware Information

- CH32V303VCT6-EVT-R0-1v0
- A USB to UART debugger
- A WCH-Link(E)

## Installation Steps

### Install PlatformIO Core

You can first check if your package manager includes a package like [platformio-core](https://archlinux.org/packages/?name=platformio-core). If not, you can use the installation script:

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
- Debian based systems:
```bash
sudo usermod -a -G dialout $USER
sudo usermod -a -G plugdev $USER
```
- Arch based systems:
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
cd platform-ch32v/examples/hello-world-rt-thread
pio run
```

### Flashing Image

Once WCH-Link(E) is connected to the SWD debugging port, use pio to flash the image:
```bash
pio run --target upload
```

If the flashing fails, you can try manually specifying:
```bash
pio run -e your_board --target upload
```

#### Add Development Board Series

**Ignore this if you are using the C8T6 series**
This is because other chips are not in the default chip list, so we need to add them manually.
You can find the corresponding JSON name of your board in `platform-ch32v/boards`.
```bash
cat << EOF | tee -a platformio.ini
[env:your_board]
board = your_board
EOF
```

#### Common Issues

- Error: error writing to flash at address 0x00000000 at offset 0x00000000
    - This is caused by a low version of the WCH-Link firmware. (See [important-notices](https://github.com/Community-PIO-CH32V/platform-ch32v?tab=readme-ov-file#important-notices)).
    - Please use the [WCH-Link Utility](https://www.wch.cn/downloads/WCH-LinkUtility_ZIP.html) to connect once to W2 with CH-Link to update automatically. **This tool is currently only available for Windows**
- Error: Read-Protect Status Currently Enabled
    - This is caused by the chip's write protection being enabled. On Windows, we can use the [WCH-Link Utility](https://www.wch.cn/downloads/WCH-LinkUtility_ZIP.html) to remove protection; on Linux, you can use OpenOCD:
```bash
cd ~/.platformio/packages/tool-openocd-riscv-wch/bin
./openocd -f wch-riscv.cfg -c init -c halt -c "flash protect wch_riscv 0 last  off " -c exit
cd -
```

### Logging into the System

Connect to the development board via the serial port.

## Expected Results

The system should boot up normally, with information via the onboard serial port.

## Actual Results

The system booted up normally, and startup information via the onboard serial port.

### Boot Log

Screen recording (from compilation to startup):
[![asciicast](https://asciinema.org/a/ZZzVWVgkR23b8Zu6MkHA7Ojwd.svg)](https://asciinema.org/a/ZZzVWVgkR23b8Zu6MkHA7Ojwd)

**The MCU in the log below is incorrect, it is because the example hardcodes that string. See [main.c#L:65](https://github.com/Community-PIO-CH32V/platform-ch32v/blob/d9663011522ffa485b465a2dcdcebafa3970bcd1/examples/hello-world-rt-thread/src/main.c#L65)**

The DeviceID shows that it is indeed running on the target board.
```log
 \ | /
- RT -     Thread Operating System
 / | \     3.1.3 build Apr 25 2024
 2006 - 2019 Copyright by rt-thread team

 MCU: CH32V307
SystemClk:96000000
ChipID: 30300514
 www.wch.cn
msh >

```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
