---
sys: rtthread
sys_ver: null
sys_var: null

status: basic
last_update: 2024-06-21
---

# RT-Thread Maix-I K210 Test Report

## Test Environment

### Operating System Information

- Source Link: https://github.com/RT-Thread/rt-thread/
- Reference Installation Document: https://github.com/RT-Thread/rt-thread/tree/master/bsp/k210
- Toolchain: https://github.com/xpack-dev-tools/riscv-none-embed-gcc-xpack/releases
    - kflash: https://github.com/kendryte/kflash.py

### Hardware Information

- Sipeed Maix-Bit (K210)

## Installation Steps

### Preparing the Source Code and Environment

Get the toolchain, download, and extract it.

Note: The official kendryte toolchain reports a floating-point type incompatibility error, while versions of the RISC-V toolchain prior to 8.2.0 have header file incompatibility issues. (See [installation document](https://github.com/RT-Thread/rt-thread/tree/master/bsp/k210))

Clone the repository and configure it:
```bash
git clone https://github.com/RT-Thread/rt-thread/
cd rt-thread/bsp/k210
scons --menuconfig
source ~/.env/env.sh
pkgs --update
```

In menuconfig, ensure the following options are correctly set:
> RT-Thread online packages --->
> > peripheral libraries and drivers --->
> > > Kendryte SDK --->
> > > > [*] kendryte K210 SDK

> RT-Thread Components --->  C++ features

Then open rtconfig.py, find line 18, and replace EXEC_PATH with the bin directory of your extracted toolchain.

### Compile the Code

Compile using scons:
```bash
scons --exec-path="path/to/toolchain/bin"
```

### Flashing the Image

Flash using k_flash, toolchain documentation can be found at: https://github.com/kendryte/kflash.py

```bash
pip install kflash
kflash -b 115200 -p /dev/ttyUSBx rtthread.bin
```

### Logging into the System

Connect to the development board via serial port.

## Expected Results

Build succeeds, and the development board outputs RT-Thread startup information normally.

## Actual Results

Build succeeded, and the development board output RT-Thread startup information normally.

### Boot Information

Screen recording (from flashing the system to startup):
[![asciicast](https://asciinema.org/a/UeYag1L9qPvAPgcuuWKMpF7ye.svg)](https://asciinema.org/a/UeYag1L9qPvAPgcuuWKMpF7ye)

```log
heap: [0x80076c43 - 0x80600000]

 \ | /
- RT -     Thread Operating System
 / | \     5.2.0 build Apr 18 2024 18:23:42
 2006 - 2024 Copyright by RT-Thread team
(rt_hw_interrupt_is_disabled()) assertion failed at function:rt_sched_post_ctx_switch, line number:1045 
[0] W/kernel.service: rt_hw_backtrace_frame_unwind is not implemented
please use: addr2line -e rtthread.elf -a -f 0x80013392[0] W/kernel.service: rt_hw_backtrace_frame_unwind is not implemented


```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful
