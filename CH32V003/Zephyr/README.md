---
sys: zephyr
sys_ver: v4.1.0
sys_var: null

status: basic
last_update: 2025-06-10
---

# Zephyr CH32V003-EVT Test Report

## Test Environment

### Operating System Information

- Source Code: https://github.com/zephyrproject-rtos/zephyr/tree/main
  - Flashing tool: https://github.com/cnlohr/ch32fun/tree/master/minichlink
    - Precompiled binary: https://github.com/AlexanderMandera/minichlink-binaries/
- Reference Installation Document: https://docs.zephyrproject.org/latest/boards/wch/ch32v003evt/doc/index.html

### Hardware Information

- CH32V003-EVT
- WCH-Link Debugger

## Installation Steps

### Installing Zephyr

Create a virtual environment:

```bash
python3 -m venv ~/zephyrproject/.venv
source ~/zephyrproject/.venv/bin/activate
pip install west
```

Get Zephyr:
```bash
west init ~/zephyrproject
cd ~/zephyrproject
west update
```

Set up the environment:
```bash
west zephyr-export
pip install -r ~/zephyrproject/zephyr/scripts/requirements.txt
```

### Compiling the Code

Compile the code using west:
```bash
west build -p always -b ch32v003evt samples/basic/blinky

```

### Flashing the Image

Connect the board to WCH-Link:
VCC = VCC (do not power the board from the USB port at the same time)
GND = GND
SWDIO = PD1

Flash the image:
```bash
west flash --minichlink /path/to/minichlink
```

## Booting the system
Connect to the serial port as follows:

UART RX -> PD5
UART TX -> PD6

## Expected Results

The system should boot normally and allow viewing information via the onboard serial port.

## Actual Results

The system booted normally and viewing information via the onboard serial port was successful.

### Boot Log

```log
*** Booting Zephyr OS build v4.1.0-rc2-120-g4212408bf57e ***
LED state: OFF
LED state: ON
LED state: OFF
LED state: ON
LED state: OFF
LED state: ON
LED state: OFF
LED state: ON
LED state: OFF

```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
