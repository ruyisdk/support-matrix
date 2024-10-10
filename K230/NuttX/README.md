---
sys: nuttx
sys_ver: null
sys_var: null

status: basic
last_update: 2024-06-21
---

# NuttX CanMV K230 Test Report

## Test Environment

### Operating System Information

- Source Code Link: https://github.com/apache/nuttx
- Reference Installation Document: https://nuttx.apache.org/docs/latest/platforms/risc-v/k230/boards/canmv230/index.html
- Toolchain:
    - SDK: https://github.com/kendryte/k230_sdk
    - Boot Image: https://gitee.com/yf1972/filexfers/tree/canmv230-tools-for-nuttx-v1.2
    - SBI: https://github.com/yf13/k230osbi
    - Toolchain: https://github.com/xpack-dev-tools/riscv-none-elf-gcc-xpack
    - kflash: https://github.com/kendryte/kflash.py

### Hardware Information

- Development Board: Canaan Kendryte K230
- USB A to C / USB C to C cables
- SD card
- Network connection and TFTP server

## Installation Steps

### Preparing Source Code and Environment

Get the pre-built boot image:
```bash
wget https://gitee.com/yf1972/filexfers/releases/download/canmv230-tools-for-nuttx-v1.2/canmv230-opensbi-dtb.tar.xz
wget https://gitee.com/yf1972/filexfers/releases/download/canmv230-tools-for-nuttx-v1.2/canmv230-sdcard.img.xz
```

Get the toolchain:
```bash
wget https://github.com/xpack-dev-tools/riscv-none-elf-gcc-xpack/releases/download/v13.2.0-2/xpack-riscv-none-elf-gcc-13.2.0-2-linux-x64.tar.gz
tar -xvzf xpack-riscv-none-elf-gcc-13.2.0-2-linux-x64.tar.gz
export PATH=path/to/toolchain/bin:$PATH
```

Clone the repository and configure it:
```bash
mkdir nuttx && cd nuttx
git clone https://github.com/apache/nuttx.git nuttx
git clone https://github.com/apache/nuttx-apps.git apps
```

### Building NuttX

```bash
cd nuttx
make distclean
./tools/configure.sh canmv230:nsh
make -j$(nproc)
```

### Flashing the Image

Flash the SBI environment to the SD card:
```bash
unxz -k canmv230-sdcard.img.xz
sudo dd if=canmv230-sdcard.img of=/dev/your/device bs=1M status=progress
```

### Booting NuttX

Place the built nuttx.bin in the TFTP server, load and run it from the U-boot console (manually interrupt autoboot):
```bash
k230# usb start
k230# env edit serverip
env: your.tftp.server.ip
k230# dhcp
k230# ping $serverip
k230# tftp 8000000 nuttx.bin
k230# go 8000000
```

### Logging into the System

Connect to the development board via the serial port.

## Expected Results

Build successful, the development board outputs boot information normally.

## Actual Results

Build successful, the development board outputs boot information normally.

### Boot Information

Screen recording (from flashing system to booting):
[![asciicast](https://asciinema.org/a/wxzebwRRYH909rIlx69ISi3ar.svg)](https://asciinema.org/a/wxzebwRRYH909rIlx69ISi3ar)

```log
## Starting application at 0x08000000 ...
ABC
NuttShell (NSH) NuttX-12.5.1
nsh> cat /proc/version
NuttX version 12.5.1 6e941aed8b May  7 2024 10:24:29 canmv230:nsh
nsh> 
```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
