# FreeRTOS LicheeRV Nano Test Report

## Test Environment

### Operating System Information

- System Version: 20240401
- Download Link: https://github.com/sipeed/LicheeRV-Nano-Build/releases
- Reference Installation Document: https://github.com/sipeed/LicheeRV-Nano-Build/releases

### Hardware Information

- LicheeRV Nano
- A Type-C power cable
- A UART to USB debugger

## Installation Steps

FreeRTOS on the LicheeRV Nano is integrated within the Linux SDK and interacts with the Linux system using a mailbox.

### Viewing FreeRTOS Device

FreeRTOS communicates with Linux through a mailbox, which can be found in `/dev` as `cvi-rtos-cmdqu`.

### Logging into the System

Logging into the system via the serial port.

Default Username: `root`
Default Password: `root`

## Expected Results

The system should boot normally, and the RTOS device should be visible.

## Actual Results

The system booted normally, and the RTOS device was visible.

### Boot Log

```log

Welcome to Linux
licheervnano-b6c0 login: root
licheervnano-b6c0 login: root
Password: 
# ls /dev/ | grep rtos
cvi-rtos-cmdqu
# 

```

Screen Recording:

[![asciicast](https://asciinema.org/a/zG1HsQyGWkGTVHFI74Nwhxcv8.svg)](https://asciinema.org/a/zG1HsQyGWkGTVHFI74Nwhxcv8)

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
