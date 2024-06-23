# FreeRTOS CH592X Official  Test Report

## Test Environment

### Operating System Information

- Source Code Link: https://www.wch.cn/downloads/CH592EVT_ZIP.html
- Reference Installation Document: https://www.wch.cn/downloads/CH592EVT_ZIP.html
    - wchisp: https://github.com/ch32-rs/wchisp
- Flashing Tool:
    - https://github.com/ch32-rs/wchisp/

### Hardware Information

- CH592X-EVT-R1-1v0
- A USB to UART Debugger
- A USB Type-C Cable

## Installation Steps

### Flashing Image

Pre-compiled image is located at `EVT/EXAM/FreeRTOS/obj/FreeRTOS.hex`

After downloading and extracting the source code and wchisp tool, **do not power on first**. Press and hold the boot(download) button, then connect the board to the computer via Type-C cable.

Use the wchisp tool for flashing:
```bash
./wchisp flash EVT/EXAM/FreeRTOS/obj/FreeRTOS.hex

```

### Logging into the System

Connect to the development board via serial port.

## Expected Results

The system should boot up properly, and information can be viewed through the onboard serial port.

## Actual Results

The system booted up correctly, and information can be viewed through the onboard serial port.

### Boot Log

Screen recording (from flashing to bootup):
[![asciicast](https://asciinema.org/a/dQb48LYxe4BpWMlXeT0AcSBa6.svg)](https://asciinema.org/a/dQb48LYxe4BpWMlXeT0AcSBa6)

```log
start.
      task2 entry 1
                   task1 entry 1
                                task1 entry 2
                                             task2 entry 2
                                                          task1 entry 1
                                                                       task1 entry 2
                                                                                    task2 entry 1

```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.

