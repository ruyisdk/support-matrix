# Zephyr Longan Nano Test Report

## Test Environment

### Operating System Information

- Source Code: https://github.com/zephyrproject-rtos/zephyr/tree/main
- Reference Installation Document: https://docs.zephyrproject.org/latest/develop/getting_started/index.html

### Hardware Information

- Longan Nano
- A USB to UART Debugger
- A Type-C Cable

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
west build -p always -b longan_nano samples/basic/blinky

```

### Flashing the Image

Hold down the boot button, then press reset, and release the boot button.
Flash using the USB port:
```bash
west flash --runner dfu-util

```

## Expected Results

The system should boot normally and allow viewing information via the onboard serial port.

## Actual Results

The system booted normally and viewing information via the onboard serial port was successful.

### Boot Log

Screen recording (From compilation to boot):
[![asciicast](https://asciinema.org/a/Kz2OGHEaRjIODgvzJWO5dPTWm.svg)](https://asciinema.org/a/Kz2OGHEaRjIODgvzJWO5dPTWm)

```log
*** Booting Zephyr OS build v3.6.0-1803-gf419ea799099 ***
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
