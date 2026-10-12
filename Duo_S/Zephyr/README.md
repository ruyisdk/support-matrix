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

- System Version: Zephyr 4.1.99 (commit 4788d883d554)
- Source Code Link: https://github.com/xingrz/zephyr/commit/4788d883d554d015470eff11883af610aeb6c2cd
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

### Fetch the RISC-V Toolchain

A freshly cloned SDK does not include `host-tools/gcc/`. Run the SDK's bundled script to download it first:
```bash
cd ~/duo-buildroot-sdk
./build/scripts/download_toolchain.sh

```

After the download completes, verify the toolchain exists:
```bash
ls -lh ~/duo-buildroot-sdk/host-tools/gcc/riscv64-linux-musl-x86_64/bin/riscv64-unknown-linux-musl-gcc
```

Check that the toolchain runs correctly:
```bash
~/duo-buildroot-sdk/host-tools/gcc/riscv64-linux-musl-x86_64/bin/riscv64-unknown-linux-musl-gcc --version
```

Once the toolchain is confirmed, proceed to U-Boot configuration and compilation.

### Modify U-Boot Board Initialization

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

### Sync Board Files into the U-Boot Source Tree

The SDK build script copies board-level files from `build/boards/.../u-boot/` into the U-Boot source tree. When building manually, this step must be done explicitly:
```bash
# Copy the board defconfig into the U-Boot source tree
cp ~/duo-buildroot-sdk/build/boards/cv181x/cv1813h_milkv_duos_sd/u-boot/cvitek_cv1813h_milkv_duos_sd_defconfig \
   ~/duo-buildroot-sdk/u-boot-2021.10/configs/

# Copy cvi_board_init.c into U-Boot's board directory
mkdir -p ~/duo-buildroot-sdk/u-boot-2021.10/board/cvitek/cv1813h_milkv_duos_sd/
cp ~/duo-buildroot-sdk/build/boards/cv181x/cv1813h_milkv_duos_sd/u-boot/cvi_board_init.c \
   ~/duo-buildroot-sdk/u-boot-2021.10/board/cvitek/cv1813h_milkv_duos_sd/

```

Verify that the two copies of the board init file are identical:
```bash 
diff -u \
  build/boards/cv181x/cv1813h_milkv_duos_sd/u-boot/cvi_board_init.c \
  u-boot-2021.10/board/cvitek/cv1813h_milkv_duos_sd/cvi_board_init.c
```

If the command produces no output and exits with status `0`, the two files are identical.

### Configure and Compile U-Boot

Configure U-Boot with the Duo S defconfig:
```bash 
cd ~/duo-buildroot-sdk/u-boot-2021.10

export CROSS_COMPILE="$HOME/duo-buildroot-sdk/host-tools/gcc/riscv64-linux-musl-x86_64/bin/riscv64-unknown-linux-musl-"

make O=build/cv1813h_milkv_duos_sd \
    ARCH=riscv \
    CROSS_COMPILE="$CROSS_COMPILE" \
    cvitek_cv1813h_milkv_duos_sd_defconfig
```

After configuration, remove the stale object file and its dependency record for `cvi_board_init.c`, to avoid mistaking a previous build's artifact for this build's output:

```bash
rm -f build/cv1813h_milkv_duos_sd/board/cvitek/cv1813h_milkv_duos_sd/cvi_board_init.o

rm -f build/cv1813h_milkv_duos_sd/board/cvitek/cv1813h_milkv_duos_sd/.cvi_board_init.o.cmd
```

Compile U-Boot:
```bash
make O=build/cv1813h_milkv_duos_sd \
    CROSS_COMPILE="$CROSS_COMPILE" \
    ARCH=riscv \
    CHIP=cv1813h \
    CVIBOARD=milkv_duos_sd \
    -j"$(nproc)"

```

After compilation, verify that `cvi_board_init.o` has been generated:
```bash
ls -lh build/cv1813h_milkv_duos_sd/board/cvitek/cv1813h_milkv_duos_sd/cvi_board_init.o

```

Also check the build dependencies to confirm that `cvi_board_init.c` was used in this build:
```bash
find build/cv1813h_milkv_duos_sd \
    -name '*.cmd' \
    -exec grep -H "cvi_board_init.c" {} \;

```

In addition, check the source file path in the build output to confirm the file that actually participated in the build is:

`u-boot-2021.10/board/cvitek/cv1813h_milkv_duos_sd/cvi_board_init.c`

### Generate U-Boot Raw Image

Manually generate `u-boot-raw.bin`:
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

#### Create a virtual environment:

```bash
python3 -m venv ~/zephyrproject/.venv
source ~/zephyrproject/.venv/bin/activate
pip install west

```

#### Fetch the specified version of the Zephyr source

Since the Milk-V DuoS support code has not yet been merged into the Zephyr mainline, the source must be obtained from the corresponding development repository and pinned to the tested commit:

`4788d883d554d015470eff11883af610aeb6c2cd`

Initialize the workspace and fetch dependencies:

```bash
west init ~/zephyrproject \
    -m https://github.com/xingrz/zephyr.git \
    --mr 4788d883d554d015470eff11883af610aeb6c2cd

cd ~/zephyrproject
west update

```

Confirm the Zephyr source is at the specified commit：
```bash
cd ~/zephyrproject/zephyr 
git rev-parse HEAD

```

Configure the environment:
```bash
west zephyr-export
pip install -r ~/zephyrproject/zephyr/scripts/requirements.txt

```

Confirm the output is `4788d883d554d015470eff11883af610aeb6c2cd`.

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

After a successful build, verify that the Zephyr image has been generated:

```bash
ls -lh ~/zephyrproject/zephyr/build/zephyr/zephyr.bin
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
