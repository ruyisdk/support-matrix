# FreeBSD MangoPi MQ Pro Test Report

## Test Environment

### Operating System Information

- Download Link: https://github.com/freebsd-d1/freebsd-d1
- Reference Installation Document: https://github.com/freebsd-d1/freebsd-d1

### Hardware Information

- MangoPi MQ Pro
- Power Adapter
- A microSD card
- A USB to UART Debugger

## Installation Steps

### Flashing Image

Clone the repository and generate the image:

```bash
gmake
dd if=freebsd-d1.img of=/dev/your/device
```

### Logging into the System

Logging into the system via the serial port.

Default username: `root`
You will set the password on the first login.

## Expected Results

The system boots up normally and allows login through the onboard serial port.

## Actual Results

CFT

### Boot Log

Screen recording (From flashing image to login):

```log
```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

CFT
