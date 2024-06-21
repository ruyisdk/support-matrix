
# Yocto BeagleV-Ahead Test Report

## Test Environment

### System Information

- Download Link: [Beagle Board Public Files](https://files.beagle.cc/file/beagleboard-public-2021/images/xuantie-yocto-1.1.2-20230610.zip)
- Refer to Installation Documentation: [BeagleV-Ahead Quick Start Guide](https://docs.beagleboard.org/latest/boards/beaglev/ahead/02-quick-start.html)

### Hardware Information

- BeagleV-Ahead
- USB-C Power Adapter / DC Power Supply
- USB-UART Debugger

## Installation Steps

### Flashing Image

Install fastboot:
```bash
sudo apt-get install android-sdk-platform-tools
```

Unzip the installation package. Run the automatic flashing script:

```bash
unzip xuantie-yocto-1.1.2-20230610.zip
sudo ./fastboot_emmc.sh
```

### Logging into the System

Logging into the system via serial port.

Default username: `root`
Default password: No password

## Expected Results

The system boots up correctly and can be accessed via onboard serial port.

## Actual Results

The system boots up correctly and can be accessed successfully via the onboard serial port.

### Boot Log

Screen recording (from flashing  the image to startup):

```log

```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

CFT
