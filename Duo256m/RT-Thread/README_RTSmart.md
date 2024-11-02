---
sys: rtthread
sys_ver: null
sys_var: smart

status: cfh
last_update: 2024-11-02
---

# RT-Thread Milk-V Duo 256M Test Report

## Test Environment

### Operating System Information

- Source Code Link:
  - https://github.com/RT-Thread/rt-thread
  - https://github.com/RT-Thread/userapps
- Reference Installation Document: https://github.com/RT-Thread/rt-thread/tree/master/bsp/cvitek
   - Toolchain: https://github.com/RT-Thread/toolchains-ci/releases/download/v1.7/riscv64-linux-musleabi_for_x86_64-pc-linux-gnu_latest.tar.bz2

### Hardware Information

- Milk-V Duo 256M
- A USB-A to C or USB C to C Cable
- A microSD Card
- A USB to UART Debugger (e.g., CH340, CH341, FT2232, etc.)

## Installation Steps

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

The value of the `The virtural address of kernel start (KERNEL_VADDR_START)` option in menuconfig needs to be set to `0xffffffc000200000` in order to make a compile-time assert happy. The kernel in the resulting image, however, fails to boot:

### Boot Log

```log
Starting kernel ...

[I/drv.pinmux] Pin Name = "UART0_RX", Func Type = 281, selected Func [0]

Unhandled Exception 13:Load Page Fault
[E/libcpu.trap] 
-------- [SEVER ERROR] --------
[E/libcpu.trap] Nested trap detected
[E/libcpu.trap] scause:0x000000000000000d,stval:0x0000000000000170,sepc:0xffffffc0002797f8

--------------Dump Registers-----------------
Function Registers:                                                                   
        ra(x1) = 0xffffffc0002797f0     user_sp = 0xffffffc0002a6bc0                  
        gp(x3) = 0xffffffc0002a5a18     tp(x4) = 0x0000000000000000                   
Temporary Registers:                                                                  
        t0(x5) = 0x8000000000000005     t1(x6) = 0x0000000000000008                   
        t2(x7) = 0x0000000000000000
        t3(x28) = 0x0000000000000000    t4(x29) = 0x0000000000000000
        t5(x30) = 0x0000000000000000    t6(x31) = 0x0000000000000000
Saved Registers:
        s0/fp(x8) = 0xffffffc0002a6bf0  s1(x9) = 0x0000000000000000
        s2(x18) = 0x0000000000000000    s3(x19) = 0x0000000000000000
        s4(x20) = 0x0000000000000000    s5(x21) = 0x0000000000000000
        s6(x22) = 0x0000000000000000    s7(x23) = 0x0000000000000000
        s8(x24) = 0x0000000000000000    s9(x25) = 0x0000000000000000
        s10(x26) = 0x0000000000000000   s11(x27) = 0x0000000000000000
Function Arguments Registers:
        a0(x10) = 0xffffffc0002ea208    a1(x11) = 0x0000000000000000
        a2(x12) = 0xffffffc0002631ac    a3(x13) = 0xffffffc0002a6c70
        a4(x14) = 0x0000000000000001    a5(x15) = 0x0000000000000000
        a6(x16) = 0x0000000000000000    a7(x17) = 0x0000000000000001
sstatus = 0x8000000201844100
        Supervisor Interrupt Disabled
        Last Time Supervisor Interrupt Disabled
        Last Privilege is Supervisor Mode
        Permit to Access User Page
        Not Permit to Read Executable-only Page
satp = 0x80000000000802e6
        Current Page Table(Physical) = 0x00000000802e6000
        Current ASID = 0x0000000000000000
        Mode = Page-based 39-bit Virtual Addressing Mode
-----------------Dump OK---------------------
shutdown...
```

It may be necessary to revert a specific commit in the RT-Thread repository to resolve this issue. See [RT-Thread/rt-thread#9608](https://github.com/RT-Thread/rt-thread/issues/9608) for more details.

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

CFH
