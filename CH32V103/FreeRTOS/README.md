# FreeRTOS CH32V103C Official Example Test Report

## Test Environment

### Operating System Information

- Source Code Link: [CH32V103EVT_ZIP](https://www.wch.cn/downloads/CH32V103EVT_ZIP.html)
- Reference Installation Document: Official documentation is located inside the compressed package
    - PlatformIO Documentation: [Community-PIO-CH32V](https://github.com/Community-PIO-CH32V/platform-ch32v)
- Toolchain: [Mounriver Toolchain Download](http://mounriver.com/download)
    - WCH-Link Toolchain: [WCH-Link Utility ZIP](https://www.wch.cn/downloads/WCH-LinkUtility_ZIP.html)

### Hardware Information

- CH32V103C8T6-EVT-R1
- One USB to UART Debugger
- One WCH-Link(E)

## Installation Steps

### Prepare Build Environment

Extract the source code and toolchain into the working directory.

Since the official example does not come with a Makefile or any build scripts but uses the official IDE for building, if you want to use the toolchain directly, download this modified [Makefile](./Makefile) and place it in the source code folder under `EVB/EXAM/FreeRTOS/FreeRTOS`.

Modify the toolchain paths in the obtained Makefile by replacing the content in `TOOL_CHAIN_PATH` and `OPENOCD_PATH`.

Proceed with `make prepare` to copy necessary code.

### Build Image

If the Makefile is configured correctly, executing `make` should automatically build the image.

#### Possible Issues

- Symbol `__freertos_irq_stack_top` not found:
    - Manually copy the link script from ../FreeRTOS.bak/Ld to the current directory.

### Flashing Image

If the configuration is correct, executing `make flash` should automatically flash the image.

#### Common Issues

- Error: error writing to flash at address 0x00000000 at offset 0x00000000
    - This is due to a low firmware version of WCH-Link. (Refer to [important-notices](https://github.com/Community-PIO-CH32V/platform-ch32v?tab=readme-ov-file#important-notices)).
    - Use the [WCH-Link Toolchain](https://www.wch.cn/downloads/WCH-LinkUtility_ZIP.html) to connect to W2 once with CH-Link for automatic update. **This tool is currently available only for Windows**.
- Error: Read-Protect Status Currently Enabled
    - This is caused by write protection enabled on the chip. On Windows, we can use the [WCH-Link Toolchain](https://www.wch.cn/downloads/WCH-LinkUtility_ZIP.html) to disable protection. On Linux, we can use OpenOCD:
```bash
cd path/to/openocd/bin
./openocd -f wch-riscv.cfg -c init -c halt -c "flash protect wch_riscv 0 last  off " -c exit
cd -
```

### System Login

Connect to the development board via serial port.

## Expected Results

Successful build with the development board displaying OS information correctly.

## Actual Results

Successful build with the development board correctly displaying OS information.

### Boot Log

Screen recording (from system flashing to start):
[![asciicast](https://asciinema.org/a/uml0eDGjJXKoaFuPn2K1D2WSv.svg)](https://asciinema.org/a/uml0eDGjJXKoaFuPn2K1D2WSv)

```log
SystemClk:72000000
ChipID:2500410f
FreeRTOS Kernel Version:V10.4.6
```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.

