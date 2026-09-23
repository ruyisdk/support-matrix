---
sys: zephyr
sys_ver: 4.1.99
sys_var: null

status: basic
last_update: 2026-09-21
---

# Zephyr MilkV DuoS Test Report

## Test Environment

### Operating System Information

- System Version: Zephyr 4.1.99
- Source Code Link: https://github.com/xingrz/zephyr/tree/milkv-duo/hwmv2/dev
- Reference Installation Document:
    - https://docs.zephyrproject.org/latest/develop/getting_started/index.html
    - https://github.com/milkv-duo/duo-buildroot-sdk

### Hardware Information

- Milk-V Duo S
- A USB C to C cable
- A USB to UART Debugger
- Three DuPont wires
- SD Card

## Installation Steps

### Create and Compile BuildRoot

Follow the official tutorial to obtain the source code:
```bash
git clone https://github.com/milkv-duo/duo-buildroot-sdk.git --depth=1

```

Modify `build/boards/cv181x/cv1813h_milkv_duos_sd/u-boot/cvi_board_init.c` to remove all pre-mapped pins, keeping only the UART1 (A19/A18) configuration:
```c
int cvi_board_init(void)
{
        PINMUX_CONFIG(JTAG_CPU_TMS, UART1_TX);  // A19
        PINMUX_CONFIG(JTAG_CPU_TCK, UART1_RX);  // A18

        set_rtc_register_for_power();

        return 0;
}

```

Verify that the SDK's bundled RISC-V toolchain exists:
```bash
ls ~/duo-buildroot-sdk/host-tools/gcc/riscv64-linux-musl-x86_64/bin/riscv64-unknown-linux-musl-gcc

```

Compile U-Boot:
```bash 
cd ~/duo-buildroot-sdk/u-boot-2021.10

make O=build/cv1813h_milkv_duos_sd \
    CROSS_COMPILE=$HOME/duo-buildroot-sdk/host-tools/gcc/riscv64-linux-musl-x86_64/bin/riscv64-unknown-linux-musl- \
    ARCH=riscv \
    CHIP=cv1813h \
    CVIBOARD=milkv_duos_sd \
    -j$(nproc)

```

After compilation, u-boot-raw.bin is actually a copy of u-boot.bin in the SDK build flow. Generate it manually:
```bash 
cp build/cv1813h_milkv_duos_sd/u-boot.bin \
   build/cv1813h_milkv_duos_sd/u-boot-raw.bin

ls -lh build/cv1813h_milkv_duos_sd/u-boot-raw.bin

```

### Flash BuildRoot Image

Download the standard BuildRoot image from Milk-V's official Releases:
```bash 
wget https://github.com/milkv-duo/duo-buildroot-sdk/releases/download/v1.1.4/milkv-duos-sd-v1.1.4.img.zip
unzip milkv-duos-sd-v1.1.4.img.zip

```

Flash it:
```bash 
sudo dd if=milkv-duos-sd-v1.1.4.img of=/dev/sdX bs=1M status=progress
sync

```

### Install Zephyr

Create a virtual environment:

```bash
python3 -m venv ~/zephyrproject/.venv
source ~/zephyrproject/.venv/bin/activate
pip install west

```

Note: Since it has not been merged into the main branch yet, use a specific repository to obtain Zephyr:
```bash
west init ~/zephyrproject -m https://github.com/xingrz/zephyr.git
cd ~/zephyrproject
west update

```

Configure the environment:
```bash
west zephyr-export
pip install -r ~/zephyrproject/zephyr/scripts/requirements.txt

```

### Code Compilation

Compile the code using west:
```bash
west build -p always -b milkv_duos/sg2000/c906_1 samples/hello_world

```

To make `hello_world` print in a loop for easier observation, modify `samples/hello_world/src/main.c`:
```c
#include <zephyr/kernel.h>

int main(void)
{
        while (1) {
                printk("Hello World! %s\n", CONFIG_BOARD_TARGET);
                k_msleep(1000);
        }
        return 0;
}

```

Then rebuild:
```bash
west build -p always -b milkv_duos/sg2000/c906_1 samples/hello_world

```

### Merge fip.bin

Mount the SD card with the flashed BuildRoot image, and back up the original fip.bin:
```bash
sudo mount /dev/sdX1 /mnt/sdcard
sudo cp /mnt/sdcard/fip.bin /mnt/sdcard/fip.bin.bak

```

Incrementally replace U-Boot and the small-core firmware:
```bash
sudo python3 ~/duo-buildroot-sdk/fsbl/plat/cv181x/fiptool.py \
    -v genfip /mnt/sdcard/fip.bin \
    --OLD_FIP=/mnt/sdcard/fip.bin \
    --LOADER_2ND=$HOME/duo-buildroot-sdk/u-boot-2021.10/build/cv1813h_milkv_duos_sd/u-boot-raw.bin \
    --BLCP_2ND=$HOME/zephyrproject/zephyr/build/zephyr/zephyr.bin

sync
sudo umount /mnt/sdcard

```

### Connect Serial Port

Zephyr uses UART1 :
- A19 (Pin 18) — TX
- A18 (Pin 22) — RX
- GND (Pin 6/14/20/25)

## Expected Results

The system should boot normally and information should be viewable via the onboard serial port.

## Actual Results

The system booted successfully and information was viewable via the onboard serial port.

### Boot Information

```log
*** Booting Zephyr OS build 4788d883d554 ***
Hello World! milkv_duos/sg2000/c906_1
Hello World! milkv_duos/sg2000/c906_1
Hello World! milkv_duos/sg2000/c906_1
Hello World! milkv_duos/sg2000/c906_1
Hello World! milkv_duos/sg2000/c906_1
Hello World! milkv_duos/sg2000/c906_1
Hello World! milkv_duos/sg2000/c906_1
Hello World! milkv_duos/sg2000/c906_1
Hello World! milkv_duos/sg2000/c906_1
Hello World! milkv_duos/sg2000/c906_1
Hello World! milkv_duos/sg2000/c906_1
...

```

Screen recording :

[![asciicast](https://asciinema.org/a/XN5DravPePYddw20.svg)](https://asciinema.org/a/XN5DravPePYddw20)

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
