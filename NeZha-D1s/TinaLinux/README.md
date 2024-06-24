# Tina Linux D1s NeZha Test Report

## Test Environment

### Operating System Information

- Link: https://pan.baidu.com/s/1v55AKMFripaEu22tJ92lmw?pwd=awol (Password: awol)
- Reference Installation Document: https://d1s.docs.aw-ol.com/study/study_1tina/

### Hardware Information

- D1s NeZha
- A microSD card
- A USB to UART Debugger (e.g., CH340, CH341, FT2232, etc.)

## Installation Steps

### Packaging the Image

After downloading and extracting, prepare to compile the SDK:
```bash
source build/envsetup.sh
lunch
make -j$(nproc)
pack
```

### Flashing the Image

Using the LiveSuit software, select the image and connect the development board to flash it.

For LiveSuit download, see: https://linux-sunxi.org/LiveSuit

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

Login to the system via the serial port.

## Expected Results

The system should boot normally and allow login via the onboard serial port.

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
