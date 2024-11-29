---
sys: rtthread
sys_ver: null
sys_var: smart

status: basic
last_update: 2024-11-29
---

# RT-Thread Milk-V Duo 256M Test Report

## Test Environment

### Operating System Information

- Source Code Link:
  - https://github.com/RT-Thread/rt-thread
  - Userapps: https://github.com/RT-Thread/userapps
- Reference Installation Document: https://github.com/RT-Thread/rt-thread/tree/master/bsp/cvitek
   - Toolchain: https://github.com/RT-Thread/toolchains-ci/releases/download/v1.7/riscv64-linux-musleabi_for_x86_64-pc-linux-gnu_latest.tar.bz2

### Hardware Information

- Milk-V Duo 256M
- A USB-A to C or USB C to C Cable
- A microSD Card
- A USB to UART Debugger (e.g., CH340, CH341, FT2232, etc.)

## Installation Steps

The following steps are tested on Arch Linux, but should be applicable to all major Linux distributions.

### Fetch Source Code and Compile Firmware

Obtain the toolchain and configure it:
```bash
wget https://github.com/RT-Thread/toolchains-ci/releases/download/v1.7/riscv64-linux-musleabi_for_x86_64-pc-linux-gnu_latest.tar.bz2

tar -xjvf riscv64-linux-musleabi_for_x86_64-pc-linux-gnu_latest.tar.bz2
```

Update the following paths as needed:
```bash
export RTT_CC_PREFIX=riscv64-unknown-linux-musl-
export RTT_EXEC_PATH=/opt/riscv64-linux-musleabi_for_x86_64-pc-linux-gnu/bin
```

Fetch dependencies:
```bash
sudo apt install -y scons libncurses5-dev device-tree-compiler
# or on Arch Linux: sudo pacman -S scons dtc ncurses 
```

```bash
git clone --depth=1 https://github.com/RT-Thread/rt-thread
cd rt-thread/bsp/cvitek/cv18xx_risc-v
# Generate configuration
scons --menuconfig
```

In menuconfig, please select `milkv-duo256m` under the `Board Type` option. Enter `RT-Thread Kernel` submenu ---> Select `Enable RT-Thread Smart (microkernel on kernel/userland)` to enable the RT-Smart kernel.

```bash
source ~/.env/env.sh
pkgs --update
scons -j$(nproc) --verbose
cd ../
./combine-fip.sh $(pwd)/cv18xx_risc-v Image
```

`boot.sd` and `fip.bin` files will be generated in the `cvitek/output/milkv-duo256m` directory upon completion.

### Fetch Source Code and Compile RT-Smart userapps

Fetch dependencies:
```bash
sudo apt install -y unzip xmake
```

Compile:
```bash
git clone https://github.com/RT-Thread/userapps.git
cd userapps
source env.sh
cd apps
xmake f -a riscv64gc
xmake -j$(nproc)
```

Build Image:
```bash
xmake smart-rootfs
xmake smart-image -f ext4 
```
The userapp image would be generated at `userapps/apps/build/ext4.img`.

### Prepare microSD Card

Clear the microSD card and create a FAT32 partition:
```shell
wipefs -af /path/to/your-card
mkfs.fat /path/to/your-card
```

Copy the generated `boot.sd` and `fip.bin` files onto the microSD card. The storage card is now ready to boot RT-Thread on the Duo 256M.

### Logging into the System

Log into the system via the serial port.

## Expected Results

The system boots up normally and allows login through the serial port.

## Actual Results

The system boots up normally and login through the serial port is successful.

### Boot Log

```log
Starting kernel ...

[I/drv.pinmux] Pin Name = "UART0_RX", Func Type = 281, selected Func [0]

[I/drv.pinmux] Pin Name = "UART0_TX", Func Type = 282, selected Func [0]

heap: [0x0xffffffc0002fb110 - 0x0xffffffc000afb110]

 \ | /
- RT -     Thread Smart Operating System
 / | \     5.2.0 build Nov 29 2024 12:03:11
 2006 - 2024 Copyright by RT-Thread team
lwIP-2.1.2 initialized!
[I/sal.skt] Socket Abstraction Layer initialize success.
[I/drivers.serial] Using /dev/ttyS0 as default console
Hello RT-Smart!
msh />

```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
