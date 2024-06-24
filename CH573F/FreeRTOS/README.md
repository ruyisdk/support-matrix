# FreeRTOS CH573F Official  Test Report

## Test Environment

### Operating System Information

- Source Code Link: [CH573EVT_ZIP](https://www.wch.cn/downloads/CH573EVT_ZIP.html)
- Reference Installation Document: [CH573EVT_ZIP](https://www.wch.cn/downloads/CH573EVT_ZIP.html)
    - wchisp: [wchisp GitHub Repository](https://github.com/ch32-rs/wchisp)
- Flashing Tool:
    - [wchisp GitHub Repository](https://github.com/ch32-rs/wchisp/)

### Hardware Information

- CH573F
- A USB to UART debugger
- A USB Type-C cable

## Installation Steps

### Flashing Image

The precompiled image is located at `EVT/EXAM/FreeRTOS/obj/FreeRTOS.hex`

After downloading and extracting the source code and wchisp tool, do not power on yet. **Continuously press** the boot(download) button and connect the board to the computer via Type-C cable.

Use the wchisp tool for flashing:
```bash
./wchisp flash EVT/EXAM/FreeRTOS/obj/FreeRTOS.hex

```

### Logging into the System

Connect to the development board via serial port.

## Expected Results

The system starts up correctly and information can be viewed through the onboard serial port.

## Actual Results

CFT

### Boot Log

Screen recording (from flashing to startup):
```log

```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

CFT
