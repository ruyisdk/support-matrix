---
sys: nuttx
sys_ver: null
sys_var: null

status: basic
last_update: 2024-06-21
---

# NuttX Maix-I K210 Test Report

## Test Environment

### Operating System Information

- Source code link: https://github.com/apache/nuttx
- Reference Installation Document: https://nuttx.apache.org/docs/latest/platforms/risc-v/k210/boards/maix-bit/index.html
- Toolchain:
    - toolchain: https://static.dev.sifive.com/dev-tools/riscv64-unknown-elf-gcc-8.3.0-2019.08.0-x86_64-linux-ubuntu14.tar.gz
    - openOCD (for debugging if needed): https://github.com/kendryte/openocd-kendryte 
    - kflash: https://github.com/kendryte/kflash.py

### Hardware Information

- Sipeed Maix-Bit (K210)

## Installation Steps

### Preparing Source Code and Environment

Get the toolchain, download and unpack.
```bash
wget https://static.dev.sifive.com/dev-tools/riscv64-unknown-elf-gcc-8.3.0-2019.08.0-x86_64-linux-ubuntu14.tar.gz
tar -xzvf riscv64-unknown-elf-gcc-8.3.0-2019.08.0-x86_64-linux-ubuntu14.tar.gz
export PATH=path/to/toolchain/bin:$PATH
```

Clone the repository and configure:
```bash

mkdir nuttx && cd nuttx
git clone https://github.com/apache/nuttx.git nuttx
git clone https://github.com/apache/nuttx-apps.git apps
```

### Compile the Code

```bash
cd nuttx
make distclean
./tools/configure.sh maix-bit:nsh
make V=1
```

### Flashing the Image

Use kflash for flashing, refer to the toolchain documentation: https://github.com/kendryte/kflash.py

```bash
pip install kflash
kflash -b 115200 -p /dev/ttyUSBx nuttx.bin
```

### Logging into the System

Connect to the development board via serial port.

## Expected Results

Build succeeds, and the development board outputs startup information normally.

## Actual Results

Build succeeded, and the development board output startup information normally.

### Boot Information

Screen recording (from flashing the system to startup):
[![asciicast](https://asciinema.org/a/WlWIs9g3WqjlO9zX9t0pq2ZPU.svg)](https://asciinema.org/a/WlWIs9g3WqjlO9zX9t0pq2ZPU)

```log
NuttShell (NSH) NuttX-12.5.1
nsh> cat /proc/version
NuttX version 12.5.1 6e941aed8b-dirty May  7 2024 09:51:35 maix-bit:nsh
nsh>
```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
