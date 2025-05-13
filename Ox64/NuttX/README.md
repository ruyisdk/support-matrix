---
sys: nuttx
sys_ver: null
sys_var: null

status: basic
last_update: 2025-05-13
---

# Apache NuttX Pine64 Ox64 Test Report

## Test Environment

### Operating System Information

- Download Link: https://github.com/lupyuen2/wip-nuttx/releases/download/gpio2-1/Image
  - SDK: https://github.com/bouffalolab/bl_mcu_sdk
  - Flashing Tool: https://openbouffalo.org/static-assets/bldevcube/BouffaloLabDevCube-v1.8.3.zip
- Reference Installation Document: https://www.hackster.io/lupyuen/8-risc-v-sbc-on-a-real-time-operating-system-ox64-nuttx-474358

### Hardware Information

- Pine64 Ox64
- A Type-C or microUSB cable
- A UART debugger (CH340G preferred, *avoid* CP2102)
- A microSD card
- A microSD card reader

## Installation Steps

### Get the Image

Download and extract the precompiled image and firmware:
```bash
wget https://github.com/openbouffalo/buildroot_bouffalo/releases/download/v1.0.1/bl808-linux-pine64_ox64_full_defconfig.tar.gz
tar -xvf bl808-linux-pine64_ox64_full_defconfig.tar.gz
cd bl808-linux-pine64_ox64_full_defconfig/firmware
xz -d sdcard-pine64_ox64_full_defconfig.img.xz
```

### Flashing the Firmware via UART

Power on the board through either the microUSB or Type-C port while holding down the BOOT button. Connect GPIO ports 14 and 15 to your debugger's RX and TX, respectively - This is the "Flashing UART".

Download the flashing tool and use the appropriate version for your system to flash the firmware. Make sure your BLDevCube binary is of version 1.8.3 **or lower**.

Enter the MCU tab and set the parameters as shown below:

M0: Group: group0, Image Addr: `0x58000000`, and choose `m0_lowload_bl808_m0.bin` from the above archive

D0: Group: group0, Image Addr: `0x58100000`, and choose `d0_lowload_bl808_d0.bin` from the above archive

Choose your UART port correspondingly and set the "Uart Rate" to 2000000.

Click "Create & Download" and wait for it to complete.

![](mcu.png)

Next, Enter the IOT tab and set the parameters as shown below:

Enable "Single Download", set address to `0x800000` and choose `bl808-firmware.bin` from the above archive.

Click "Create & Download" and wait for it to complete.

![](iot.png)
### Replace the kernel in the image

Download the NuttX kernel:
```shell
wget https://github.com/lupyuen2/wip-nuttx/releases/download/gpio2-1/Image
```

Mount the above image and replace its kernel (`/boot/Image`) with the NuttX kernel. e.g.:

```shell
sudo losetup /dev/loop14 sdcard-pine64_ox64_full_defconfig.img
sudo kpartx -av /dev/loop14
sudo mount /dev/mapper/loop14p2 /mnt
sudo mv Image /mnt/root/
sudo umount /mnt
sudo kpartx -d /dev/loop14
sudo losetup -d /dev/loop14
```

### Flash the image to SD card

```shell
dd if=sdcard-pine64_ox64_full_defconfig.img of=/dev/your/device status=progress
```

### Boot

Insert the SD card, and connect GPIO ports 32 and 31 to your debugger's RX and TX, respectively - This is the "Serial Console UART". Remember to set the baud rate to 2000000.

## Expected Results

The system should start normally with serial output.

## Actual Results

The system started successfully, with serial output.

### Boot Information

```log
Starting kernel ...

ABC
bl808_gpiowrite: regaddr=0x20000938, clear=0x1000000

bl808_gpiowrite: regaddr=0x20000938, set=0x1000000

bl808_gpiowrite: regaddr=0x20000938, clear=0x1000000

NuttShell (NSH) NuttX-12.4.0-RC0
nsh> ls
/:
 dev/
 proc/
 system/
nsh> help
help usage:  help [-v] [<cmd>]

    .           cp          exit        mkdir       rmdir       umount
    [           cmp         expr        mkrd        set         unset
    ?           dirname     false       mount       sleep       uptime
    alias       dd          fdinfo      mv          source      usleep
    unalias     df          free        pidof       test        xd
    basename    dmesg       help        printf      time
    break       echo        hexdump     ps          true
    cat         env         kill        pwd         truncate
    cd          exec        ls          rm          uname
nsh> uname
NuttX
nsh> uname -a
NuttX 12.4.0-RC0 904b955-dirty Feb 12 2024 14:32:26 risc-v ox64
nsh>

```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.

