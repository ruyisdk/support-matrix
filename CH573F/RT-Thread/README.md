# RT-Thread CH573F Official  Test Report

## Test Environment

### Operating System Information

- Source Code Link: [CH573EVT_ZIP](https://www.wch.cn/downloads/CH573EVT_ZIP.html)
- Reference Installation Document: [CH573EVT_ZIP](https://www.wch.cn/downloads/CH573EVT_ZIP.html)
    - wchisp: [Github Link](https://github.com/ch32-rs/wchisp)
- Flashing Tool:
    - [wchisp Github Repository](https://github.com/ch32-rs/wchisp/)

### Hardware Information

- CH573F
- One USB to UART debugger
- One USB Type-C cable

## Installation Steps

### Flashing Image

The precompiled image is located at `EVT/EXAM/RT-Thread/obj/rt-thread-nano.hex`

After downloading and extracting the source code and wchisp tool, do not power on. **Continuously hold** the boot (download) button and connect the board to the computer using the Type-C cable.

Use the wchisp tool for flashing:
```bash
./wchisp flash EVT/EXAM/RT-Thread/obj/rt-thread-nano.hex

```

### Logging into the System

Connect to the development board via serial port.

## Expected Results

The system should boot up normally, and information can be viewed through the onboard serial port.

## Actual Results

The system booted up normally, and information could be viewed through the onboard serial port.

### Boot Up Information

Screen recording (from flashing to booting up):

```log

```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

CFT

