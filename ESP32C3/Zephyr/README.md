# Zephyr ESP32-C3 Test Report

## Test Environment
Ubuntu 20.04

### Operating System Information

- Source Code Link: https://github.com/zephyrproject-rtos/zephyr/tree/main/samples/hello_world
            https://docs.zephyrproject.org/latest/boards/luatos/esp32c3_luatos_core/doc/index.html
- Reference Documents:
    - ESP32-C3: https://www.espressif.com/en/support/documents/technical-documents?keys=esp32-c3

### Hardware Information

- LUATOS ESP32-C3
- One USB to UART Debugger

## Installation Steps

### Install Zephyr
Configure the Zephyr environment according to the Zephyr documentation: https://docs.zephyrproject.org/latest/develop/getting_started/index.html

### Prepare Project Repository
```bash
cd zephyr
```
### Compile Code
```bash
west build -b esp32c3_luatos_core --sysbuild samples/hello_world
```

### Flash Image

After confirming the connection to esp32c3, flash the image.
In a Linux development environment, you may need to add and apply udev rules in advance (the GROUP may need to be changed depending on the distribution).
```bash
west flash
west espressif monitor
```
(To exit the serial monitor, type Ctrl-].)

### Observe Log

Connect the development board via serial port.

## Expected Result

The system starts normally, and information can be viewed through the onboard serial port.

## Actual Result

Basic

### Startup Information
Screen recording (from compilation to startup):
[![asciicast](https://asciinema.org/a/NWBb9aYkRNBGzoq83srOwMxg5.svg)](https://asciinema.org/a/NWBb9aYkRNBGzoq83srOwMxg5)
```log
*** Booting Zephyr OS build v4.0.0-3624-ge658bc1b2baa ***
Hello World! esp32c3_luatos_core/esp32c3
```

## Test Criteria

Test Success: The actual result matches the expected result.

Test Failure: The actual result does not match the expected result.

## Test Conclusion

Test Success