# FreeRTOS R128 EVT Development Kit Test Report

## Test Environment

### Operating System Information

- SDK Link:
    - https://r128.docs.aw-ol.com/r128/get_sdk/
- Precompiled Firmware for Testing: https://www.aw-ol.com/downloads/resources/126
- Reference Installation Document:
    - https://r128.docs.aw-ol.com/devkit/r128_evt/

### Hardware Information

- TinyVision Development Board

## Installation Steps

### Flashing the Image

After downloading the image, use the LiveSuit software to select the image and connect the development board for flashing.

For downloading LiveSuit, see: https://linux-sunxi.org/LiveSuit

#### LiveSuit

Download and build:
```bash
git clone https://github.com/linux-sunxi/sunxi-livesuite.git
apt-get install dkms
make
# If you are getting error that /lib/modules/4.4.50+/build is missing try adding symlink to the /usr/src/linux-headers-XXX, for example:
# sudo ln -s /usr/src/linux-headers-3.6-trunk-rpi/ /lib/modules/4.4.50+/build

cp awusb.ko /lib/modules/`uname -r`/kernel/
depmod -a
modprobe awusb
KERNEL=="aw_efex[0-9]*", MODE="0666"
udevadm control --reload-rules
```

Run:
```bash
./LiveSuit.sh
```

### Logging into the System

Connect UART3 to view the serial output.

## Expected Results

The system should boot normally, and the output should be visible through the serial port.

## Actual Results

CFT

### Boot Log

Screen recording:

```log
```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

CFT
