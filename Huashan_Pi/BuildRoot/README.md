# BuildRoot Huashan Pi Test Report

## Test Environment

### Operating System Information

- Download Link: https://github.com/zuoyi001/zue_sophpi-huashan
- Reference Installation Document: https://occ-oss-prod.oss-cn-hangzhou.aliyuncs.com/resource//1692610610938/%E7%8E%AF%E5%A2%83%E6%90%AD%E5%BB%BA-%E8%BD%AF%E4%BB%B6%E5%AE%89%E8%A3%85%E7%BC%96%E8%AF%91%E7%8E%AF%E5%A2%83%E6%90%AD%E5%BB%BA.pdf (Chinese), https://occ-oss-prod.oss-cn-hangzhou.aliyuncs.com/resource//1692610600110/%E5%BC%80%E5%8F%91%E6%8C%87%E5%8D%97-1.%E7%83%A7%E5%BD%95%E5%9B%BA%E4%BB%B6.pdf (Chinese)


### Hardware Information

- Huashan Pi
- A microSD card
- A USB to UART Debugger 

## Installation Steps

### Compiling SDK

Download the SDK:
```bash
git clone https://github.com/zuoyi001/zue_sophpi-huashan.git
cd zue_sophpi-huashan
```

Compile the SD card image:
```bash
sudo apt-get update
sudo apt-get install -y build-essential ninja-build automake autoconf libtool wget curl git gcc libssl-dev bc slib squashfs-tools android-sdk-libsparse-utils android-sdk-ext4-utils jq cmake python3-distutils tclsh scons parallel ssh-client tree python3-dev python3-pip device-tree-compiler ssh cpio fakeroot libncurses5 flex bison

cd cvi_media_sdk/
source build/cvisetup.sh 
defconfig cv1812h_wevb_0007a_emmc
build_all 
```

### Flashing Image

Format the SD card:
```bash
sudo mkfs.vfat -F 32 /dev/<your-device>
```

Copy the image to the SD card

```
.
├── fip.bin
├── boot.emmc (minimal Linux image)
├── rootfs.emmc (rootFS)
├── system.emmc (rw volumes)
├── cfg.emmc (config rw)
└── fw_payload_uboot.bin (bootloader + uboot)
``` 

After the card is inserted and powered on, it will automatically enter the upgrade, and after the upgrade is completed, it will stay in the uboot, and appear as
```
Saving Environment to MMC... Writing to MMC(0)... OK
```
Pull out the SD card and enter re to reboot into the system.

### Logging into the System

Logging into the system via the serial port.

## Expected Results

The system should boot up normally and allow login through the onboard serial port.

## Actual Results

CFT

### Boot Log

Screen recording (From flashing the image to logging into the system):

```log
```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

CFT
