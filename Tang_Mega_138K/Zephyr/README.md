# Zephyr Tang Mega 138K Pro Test Report

## Test Environment

### Operating System Information

- Build System: Linux
- FreeRTOS
- Source Code Download Link: https://cdn.gowinsemi.com.cn/RiscV_AE350_SOC_V1.1.zip
    - Bitstream: https://github.com/sipeed/TangMega-138KPro-example
- Reference Installation Document: https://cdn.gowinsemi.com.cn/MUG1029-1.1_Gowin_RiscV_AE350_SOC%E8%BD%AF%E4%BB%B6%E7%BC%96%E7%A8%8B%E7%94%A8%E6%88%B7%E6%89%8B%E5%86%8C.pdf
- Reference Design Document: https://cdn.gowinsemi.com.cn/MUG1031-1.1_Gowin_RiscV_AE350_SOC%E7%A1%AC%E4%BB%B6%E8%AE%BE%E8%AE%A1%E7%94%A8%E6%88%B7%E6%89%8B%E5%86%8C.pdf

### Hardware Information

- FreeRTOS Tang Mega 138K Pro Dock
- A Type A to C Cable
- A UART Cable
- Power supply come with the board

## Installation Steps

**The following example uses a Linux system for the build. For Windows, install the AE350 SOC RDS and perform the same operations in the provided Cygwin environment, unless otherwise specified.**

*If IDE functionality is not needed, a Windows build does not require an RDS License.*

### Copy Code

Zephyr code is located in the source archive at ref_design/MCU_RefDesign/ae350_zephyr. Extract it to your workspace.

### Build Code

Navigate to the code directory and set environment variables:
```bash
source zephyr-env.sh
export ZEPHYR_TOOLCHAIN_VARIANT='cross-compile
```

Set the cross-compilation toolchain, preferably using nds32le-elf-mculib-v5:
```bash
export CROSS_COMPILE=path/to/nds32le-elf-mculib-v5/bin/riscv32-elf-
```

For Windows, this file is located in the toolchains directory of the RDS installation.

Navigate to the hello_world directory:
```bash
cd samples/hello_world
```

Prepare the build files:
```bash
mkdir build
cd build
cmake -DBOARD=adp_xc7k_ae350 ../
```

Graphically configure build options: `make menuconfig`

Build the source code: `make`

### Obtain FPGA Bitstream

**The Tang Mega 138K supports this feature only in the commercial version**

The FPGA project can use the demo provided by Sipeed, located in the ae350_customized_demo directory of the [TangMega-138KPro-example](https://github.com/sipeed/TangMega-138KPro-example). The bitstream has already been compiled and does not need regeneration.

### Download Bitstream

Connect the FPGA and use the GowinCloud software to download the bitstream.

### Flash Program

Use programmer.exe located in the flash directory of the RDS for flashing. Set up as follows:
- External Flash Mode 5AT
- exFlash C Bin Erase, Program 5AT
- Start address: 0x600000

If there is no output after flashing, try re-downloading the bitstream.

### Connect UART

The default UART2 is bound to:
```
IO_LOC "UART2_TXD" U16;     //1
IO_LOC "UART2_RXD" V16;     //2
```

### Log into the System

Log into the system via the serial port.

## Expected Results

The system should boot normally and allow login through the onboard serial port.

## Actual Results

Compiled and flashed the image successfully, but there is no output from the serial port.

### Boot Log

N/A

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

CFH
