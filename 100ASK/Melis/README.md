# Melis 100ASK-V853-PRO Test Report

## Test Environment

### System Information

- Image Link: https://bbs.aw-ol.com/assets/uploads/files/1657169725953-e6e69a0f-5837-4840-99fe-8bc62c7abbf2-tina_v853-vision_uart0.img
- Reference Installation Document: https://v853.docs.aw-ol.com/

### Hardware Information

- 100ASK-V853-PRO Development Board

## Installation Steps

### Flashing Image (SD Card)

Flash the image to an SD card:
```shell
dd if=1657169725953-e6e69a0f-5837-4840-99fe-8bc62c7abbf2-tina_v853-vision_uart0.img of=/dev/your/device bs=1M status=progress
```

Insert the card into the device and boot it up.

### Flashing Image (Onboard EMMC)

Use LiveSuit software, select the image, and connect the development board for flashing.

For LiveSuit setup, refer to: https://linux-sunxi.org/LiveSuit

#### LiveSuit

Download and build:
```bash
git clone https://github.com/linux-sunxi/sunxi-livesuite.git
apt-get install dkms
make
# If you are getting error that /lib/modules/4.4.50+/build is missing,
# try adding symlink to the /usr/src/linux-headers-XXX, for example:
# sudo ln -s /usr/src/linux-headers-3.6-trunk-rpi/ /lib/modules/4.4.50+/build

cp awusb.ko /lib/modules/`uname -r`/kernel/
depmod -a
modprobe awusb
KERNEL=="aw_efex[0-9]*", MODE="0666"
udevadm control --reload-rules
```

To run:
```bash
./LiveSuit.sh
```

### Logging into the System

Connect to UART3 to view serial output.

## Expected Results

System should boot up normally, with output visible through the serial port.

## Actual Results

System booted up successfully, and output was visible through the serial port.

### Boot Log

Screen recording:

```log
```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

CFT
