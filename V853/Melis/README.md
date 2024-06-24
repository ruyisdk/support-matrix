# Melis Allwinner V853 Development Board Test Report

## Test Environment

### Operating System Information

- Image Link: https://bbs.aw-ol.com/assets/uploads/files/1657169725953-e6e69a0f-5837-4840-99fe-8bc62c7abbf2-tina_v853-vision_uart0.img
- Reference Installation Documentation: https://v853.docs.aw-ol.com/

### Hardware Information

- Allwinner V853 Development Board

## Installation Steps

### Flashing the Image (SD Card)

Flash the image to the SD card:
```shell
dd if=1657169725953-e6e69a0f-5837-4840-99fe-8bc62c7abbf2-tina_v853-vision_uart0.img of=/dev/your/device bs=1M status=progress
```

Insert the card into the device to boot.

### Flashing the Image (Onboard eMMC)

Use LiveSuit software, select the image, then connect the development board to flash it.

For more information on LiveSuit, visit: https://linux-sunxi.org/LiveSuit

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

Connect to UART3 to view serial output.

## Expected Results

The system should boot normally, and the output viewable via the serial port.

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
