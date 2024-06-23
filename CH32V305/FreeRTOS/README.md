# FreeRTOS CH32V305 Test Report

## Test Environment

### Operating System Information

- Source Code Link: [Community-PIO-CH32V/ch32-pio-projects](https://github.com/Community-PIO-CH32V/ch32-pio-projects)
- Reference Installation Document:
    - PlatformIO Core: [PlatformIO Core Installation Guide](https://docs.platformio.org/en/latest/core/installation/index.html)
    - PlatformIO CH32V: [ch32v Installation Guide](https://pio-ch32v.readthedocs.io/en/latest/installation.html)

### Hardware Information

- CH32V305FBP6-EVT-R0-1v0
- A USB to UART debugger
- A WCH-Link(E)

## Installation Steps

### Install PlatformIO Core

You can first check if the package manager includes a package like [platformio-core](https://archlinux.org/packages/?name=platformio-core). If not, you can use the following installation script:

```bash
curl -fsSL -o get-platformio.py https://raw.githubusercontent.com/platformio/platformio-core-installer/master/get-platformio.py
python3 get-platformio.py
```

### PlatformIO Environment Configuration

Install CH32V development environment:
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
cd platform-ch32v/examples/blinky-freertos
pio run
```

### Flashing Image

Once the WCH-Link(E) is connected to the SWD debug port, use pio to flash the image:
```bash
pio run --target upload
```

pio will automatically detect the development board. If flashing is unsuccessful, you can try manually specifying:
```bash
pio run -e your_board --target upload
```

#### Add Development Board

**If you are using the FBP6 series, please ignore this step**
This is because other chips are not in the default chip list, so we need to add them manually. You can find the corresponding json name for your board in `platform-ch32v/boards`.
```bash
cat << EOF | tee -a platformio.ini
[env:your_board]
board = your_board
EOF
```

#### FBP6 Flashing Issue

This is due to the debug pins of FBP6 being interconnected with UART, making the debug port unusable when running programs that use UART internally. See details at: [WCH Official Forum Post](https://www.wch.cn/bbs/thread-100647-1.html)

To resolve, **WCH-LinkE** needs to use nRST for flash erase, documented at: [WCH-LinkE User Guide](https://www.wch.cn/uploads/file/20230227/1677463712756616.pdf)


#### Common Issues

- Error: error writing to flash at address 0x00000000 at offset 0x00000000
    - This is caused by a low firmware version of WCH-Link. (Refer to [important-notices](https://github.com/Community-PIO-CH32V/platform-ch32v?tab=readme-ov-file#important-notices)).
    - Use the [WCH-Link Utility](https://www.wch.cn/downloads/WCH-LinkUtility_ZIP.html) to connect once to W2 with CH-Link for automatic update. **Currently only available for Windows**
- Error: Read-Protect Status Currently Enabled
    - This is due to write protection being enabled on the chip. On Windows, you can use the [WCH-Link Utility](https://www.wch.cn/downloads/WCH-LinkUtility_ZIP.html) to remove protection, on Linux, you can use OpenOCD:
```bash
cd ~/.platformio/packages/tool-openocd-riscv-wch/bin
./openocd -f wch-riscv.cfg -c init -c halt -c "flash protect wch_riscv 0 last  off " -c exit
cd -
```


### Logging into the System

Connect to the development board via a serial port.

For FBP6 connection instructions, refer to: [WCH Official Forum Post](https://www.wch.cn/bbs/thread-100647-1.html)

## Expected Results

The system boots up normally, and information can be viewed through the onboard serial port.

## Actual Results

The system boots up normally, and information can be viewed through the onboard serial port.

### Booting Information

Screen recording (from compilation to bootup):
[![asciicast](https://asciinema.org/a/fRz5r929znlm3kaiFEWpa8dLp.svg)](https://asciinema.org/a/fRz5r929znlm3kaiFEWpa8dLp)

```log
SystemClk:96000000
ChipID: 30520518
FreeRTOS Kernel Version:V10.4.6
task2 entry
task1 entry
task1 entry

```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
