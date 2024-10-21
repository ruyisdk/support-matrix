---
sys: freertos
sys_ver: null
sys_var: null

status: basic
last_update: 2024-06-21
---

# FreeRTOS Sipeed M0s Dock Test Report

## Test Environment

### Operating System Information

- Download Link: https://github.com/sipeed/M0S_BL616_example
    - Toolchain: https://gitee.com/bouffalolab/toolchain_gcc_t-head_linux
- Reference Installation Document: https://github.com/sipeed/M0S_BL616_example
    - https://bl-mcu-sdk.readthedocs.io/zh-cn/latest/get_started/get_started.html

### Hardware Information

- Sipeed M0s Dock
- Type-C cable

## Installation Steps

### Clone SDK and Toolchain

Clone the relevant repositories to the working directory:
```bash
git clone https://github.com/sipeed/M0S_BL616_example.git
git clone https://gitee.com/bouffalolab/toolchain_gcc_t-head_linux.git
```

Set up the environment:
```bash
export PATH=path/to/toolchain_gcc_t-head_linux/bin:$PATH
```

### Compile the Code

Compile the FreeRTOS examples:
```bash
cd M0S_BL616_example/examples/freertos
make CHIP=bl616 BOARD=bl616dk
```

### Flash the Program

Connect your computer and the device using the Type-C cable.

First, press and hold the boot button, then connect the Type-C cable to power up the device.

After that:
```bash
make flash CHIP=bl616 COMX=/dev/ttyACM0 # Change com on your machine
```

### Connect to Serial Port

The serial port to be connected is located next to the Type-C port, with a baud rate of 2000000.

## Expected Results

The system should boot normally, with startup log via the serial port.

## Actual Results

The system booted successfully, with startup log via the serial port.

### Boot Information

```log
  ____               __  __      _       _       _     
 |  _ \             / _|/ _|    | |     | |     | |    
 | |_) | ___  _   _| |_| |_ __ _| | ___ | | __ _| |__  
 |  _ < / _ \| | | |  _|  _/ _` | |/ _ \| |/ _` | '_ \ 
 | |_) | (_) | |_| | | | || (_| | | (_) | | (_| | |_) |
 |____/ \___/ \__,_|_| |_| \__,_|_|\___/|_|\__,_|_.__/ 

Build:11:07:19,Apr 28 2024
Copyright (c) 2022 Bouffalolab team
flash init fail!!!
=========== flash cfg ==============
jedec id   0x000000
mid            0xC8
iomode         0x11
clk delay      0x00
clk invert     0x03
read reg cmd0  0x05
read reg cmd1  0x35
write reg cmd0 0x01
write reg cmd1 0x31
qe write len   0x01
cread support  0x00
cread code     0x20
burst wrap cmd 0x77
=====================================
dynamic memory init success,heap size = 187 Kbyte 
sig1:ffffffff
sig2:0000f32f
cgen1:9f7ffffd
[I][MAIN] [OS] Starting consumer task...
[I][MAIN] [OS] Starting producer task...
[I][MAIN] Consumer task enter 
[I][MAIN] Producer task enter 
[I][MAIN] Consumer task start 
[I][MAIN] begin to loop /home/lw/Work/plct/boards/m0s/M0S_BL616_example/examples/freertos/main.c
[I][MAIN] Consumer get:
[I][MAIN] Producer task start 
[I][MAIN] Producer generates:101
[I][MAIN] Consumer get:101
[I][MAIN] Producer generates:102
[I][MAIN] Consumer get:102
[I][MAIN] Producer generates:103
[I][MAIN] Consumer get:103
[I][MAIN] Producer generates:104
[I][MAIN] Consumer get:104
[I][MAIN] Producer generates:105
[I][MAIN] Consumer get:105



```

Screen recording:

[![asciicast](https://asciinema.org/a/zH5ndg9eZTbjEHEkWFfAxVNQk.svg)](https://asciinema.org/a/zH5ndg9eZTbjEHEkWFfAxVNQk)

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
