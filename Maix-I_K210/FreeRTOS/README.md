# FreeRTOS Maix-I K210 Test Report

## Test Environment

### Operating System Information

- Build System: Ubuntu 22.04.4 LTS (Docker)
- Source Code: [kendryte-freertos-sdk](https://github.com/kendryte/kendryte-freertos-sdk)
- Reference Installation Document: [kendryte-freertos-sdk](https://github.com/kendryte/kendryte-freertos-sdk)
- Toolchain: [kendryte-gnu-toolchain](https://github.com/kendryte/kendryte-gnu-toolchain/releases/tag/v8.2.0-20190409)

### Hardware Information

- Sipeed Maix-Bit (K210)

## Installation Steps

### Create Docker Environment

```shell
sudo docker run -it --name ubuntu2204 ubuntu:22.04
```

All following operations are carried out in the root shell of Ubuntu 22.04.4 LTS Docker.

### Prepare Build Environment

```shell
apt update
apt install -y cmake git curl bzip2
cd /opt
curl -LO https://github.com/kendryte/kendryte-gnu-toolchain/releases/download/v8.2.0-20190409/kendryte-toolchain-ubuntu-amd64-8.2.0-20190409.tar.bz2
tar xvf kendryte-toolchain-ubuntu-amd64-8.2.0-20190409.tar.bz2
cd
```

### Build hello_world

Clone the FreeRTOS repository locally and build.

```shell
git clone --depth=1 https://github.com/kendryte/kendryte-freertos-sdk
cd kendryte-freertos-sdk
mkdir build && cd build
cmake .. -DPROJ=hello_world -DTOOLCHAIN=/opt/kendryte-toolchain/bin
make -j$(nproc)
```

Once the build is complete, the source directory will contain the files `hello_world` and `hello_world.bin`.

```log
[100%] Linking C executable hello_world                                             
Generating .bin file ...                                                            
[100%] Built target hello_world                                                     
root@4b1ebf5f94f4:~/kendryte-freertos-sdk/build# file hello_world
hello_world: ELF 64-bit LSB executable, UCB RISC-V, RVC, single-float ABI, version 1 (SYSV), statically linked, with debug_info, not stripped
```

### Flash Image

Use k_flash to perform the flash, you can refer to the toolchain documentation here: [kflash.py](https://github.com/kendryte/kflash.py)

```bash
pip install kflash
kflash -b 115200 -p /dev/ttyUSBx hello_world.bin
```

### Logging into the System

Connect to the development board via the serial port.

## Expected Results

The build should succeed, and the development board should output the Hello World message as expected.

## Actual Results

The build was successful, and the development board correctly output the Hello World message.

### Boot Information

Screen recording (From flashing image to system startup):
[![asciicast](https://asciinema.org/a/uml0eDGjJXKoaFuPn2K1D2WSv.svg)](https://asciinema.org/a/uml0eDGjJXKoaFuPn2K1D2WSv)

```log
Hello World
```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
