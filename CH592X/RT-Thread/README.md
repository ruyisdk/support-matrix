# RT-Thread CH592X Official  Test Report

## Test Environment

### Operating System Information

- Source Code Link: [CH592EVT_ZIP](https://www.wch.cn/downloads/CH592EVT_ZIP.html)
- Reference Installation Document: [CH592EVT_ZIP](https://www.wch.cn/downloads/CH592EVT_ZIP.html)
    - wchisp: [wchisp](https://github.com/ch32-rs/wchisp)
- Flashing Tool:
    - [wchisp](https://github.com/ch32-rs/wchisp/)

### Hardware Information

- CH592X-EVT-R1-1v0
- A USB to UART Debugger
- A USB Type-C Cable

## Installation Steps

### Flashing Image

The precompiled image is located at `EVT/EXAM/RT-Thread/obj/rt-thread-nano.hex`

After downloading and unzipping the source code and wchisp tool, do not power on immediately. **Continuously hold** the boot (download) button, then connect the board to the computer via Type-C cable.

Use the wchisp tool for burning:
```bash
./wchisp flash EVT/EXAM/RT-Thread/obj/rt-thread-nano.hex

```

### Logging into the System

Connect to the development board via a serial port.

## Expected Results

The system should start up normally, and information should be viewable through the onboard serial port.

## Actual Results

The system starts up normally, and information can be viewed through the onboard serial port.

### Boot Log

Screen recording (from flashing to startup):
[![asciicast](https://asciinema.org/a/Xxc0CepVpSfyC09MEVNL7Nljl.svg)](https://asciinema.org/a/Xxc0CepVpSfyC09MEVNL7Nljl)

```log
 \ | /
- RT -     Thread Operating System
 / | \     3.1.5 build Jan 16 2024
 2006 - 2020 Copyright by rt-thread team
task1
task2
msh >task2
task1
task2
task1

```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
