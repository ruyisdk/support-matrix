# FreeRTOS ESP32-C3 Test Report

## Test Environment

### Operating System Information

- Source Code Link: https://github.com/espressif/esp-idf/tree/v5.4/examples/system/freertos/real_time_stats
- Reference Documents:
    - ESP32-C3: https://docs.espressif.com/projects/esp-idf/en/v5.4/esp32c3/

### Hardware Information

- LUATOS ESP32-C3
- One USB to UART Debugger

## Installation Steps

### Install ESP-IDF

The environment installation for ESP32-IDF can mainly refer to the official website link:
https://docs.espressif.com/projects/esp-idf/en/v5.4/esp32c3/get-started/index.html#get-started-how-to-get-esp-idf
Both graphical interface and command line development have good results.

### Prepare Project Repository
```bash
git clone https://github.com/espressif/esp-idf
```
### Compile Code
```bash
cd esp-idf/examples/system/freertos/real_time_stats
idf.py menuconfig
idf.py build
```
Adjust parameters in menuconfig according to the board used.

### Flash Image

After confirming the connection to esp32c3, flash the image.
In a Linux development environment, you may need to add and apply udev rules in advance (the GROUP may need to be changed depending on the distribution).
```bash
idf.py -p PORT flash monitor
```
(Replace PORT with the name of the serial port you want to use.)

(To exit the serial monitor, type Ctrl-].)

For the complete steps to configure and use ESP-IDF to build projects, refer to the Getting Started Guide.

### Observe Log

Connect the development board via serial port.

## Expected Result

The system starts normally, and information can be viewed through the onboard serial port.

## Actual Result

The system starts normally, and information can be viewed through the onboard serial port.

### Startup Information

Screen recording (from compilation to startup):

[![asciicast](https://asciinema.org/a/JGcZ72E7j5dNoPRrxqJNyzQQu.svg)](https://asciinema.org/a/JGcZ72E7j5dNoPRrxqJNyzQQu)
```log
| Task | Run Time | Percentage
| stats | 875 | 0%
| spin1 | 107595 | 10%
| spin2 | 107595 | 10%
| spin3 | 107594 | 10%
| spin4 | 107596 | 10%
| spin5 | 107627 | 10%
| spin0 | 107597 | 10%
| IDLE | 352937 | 35%
| main | Deleted
Real time stats obtained


Getting real time stats over 100 ticks
| Task | Run Time | Percentage
| stats | 605 | 0%
| spin0 | 109494 | 10%
| spin1 | 109493 | 10%
| spin5 | 109494 | 10%
| spin2 | 99502 | 9%
| spin3 | 99500 | 9%
| spin4 | 109529 | 10%
| IDLE | 362383 | 36%
Real time stats obtained
```

## Test Criteria

Test Success: The actual result matches the expected result.

Test Failure: The actual result does not match the expected result.

## Test Conclusion

Test Success