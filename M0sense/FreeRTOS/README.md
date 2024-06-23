# FreeRTOS Demo M0sense Test Report

## Test Environment

### Operating System Information

- Build System: Arch Linux
- Source Code Link: [https://gitee.com/Sipeed/M0sense_BL702_example](https://gitee.com/Sipeed/M0sense_BL702_example)
- Reference Installation Document: [https://wiki.sipeed.com/hardware/zh/maixzero/sense/start.html](https://wiki.sipeed.com/hardware/zh/maixzero/sense/start.html)
- Toolchain: [https://gitee.com/bouffalolab/toolchain_gcc_sifive_linux](https://gitee.com/bouffalolab/toolchain_gcc_sifive_linux)

### Hardware Information

- Sipeed M0sense (BL702)
- A USB A to C or C to C cable

## Installation Steps

### Setting Up the Build Environment

```shell
sudo pacman -S gcc git base-devel
```

### Building FreeRTOS Demo

```shell
git clone https://gitee.com/Sipeed/M0sense_BL702_example.git
cd M0sense_BL702_example
git clone https://gitee.com/bouffalolab/bl_mcu_sdk
git clone https://gitee.com/bouffalolab/toolchain_gcc_sifive_linux
./build.sh patch
PATH=$PWD/toolchain_gcc_sifive_linux/bin:$PATH
gcc -I libs/uf2_format misc/utils/uf2_conv.c -o uf2_convert
./build.sh m0sense_apps/rtos_demos/single_button_control
```

Upon completion, the `uf2_demos` directory will contain the firmware in uf2 format.

```log
mx @ archlinux in ~/M0sense_BL702_example/uf2_demos |17:40:05  |main U:3 ?:2 ✗| 
$ ls
audio_recording.uf2  blink_baremetal.uf2  blink_rtos.uf2  hello_world.uf2  imu.uf2  lcd_flush.uf2  single_button_control.uf2
```

### Flashing the Image

Press and hold the BOOT button on the development board, then press the RESET button. It will appear as a USB mass storage device on your computer. Copy the `single_button_control.uf2` file generated in the previous step onto it.

After the upload is complete, the development board will automatically reboot to load the new firmware.

#### If the USB Storage Device Does Not Appear

Refer to [this guide](https://wiki.sipeed.com/hardware/zh/maixzero/sense/start.html#%E7%83%A7%E5%BD%95-bin-%E6%96%87%E4%BB%B6) on how to flash the firmware.

1. Download the flashing tool from Bouffalo's [official website](https://dev.bouffalolab.com/download).
2. Depending on your OS, run `BLDevCube`, `BLDevCube-macos`, or `BLDevCube-ubuntu`.
3. Short-circuit the `3V` and `BOOT` pins on the development board, then connect it to the computer.
4. Open the `BLDevCube` software, select `BL702`, and choose `MCU` mode.
5. Click `Refresh` and select the single available serial port (if no unique port is visible, reconnect the boot pin and the 3.3V pin and power cycle the M0sense to enter download mode), set the baud rate to `2000000`, and click `Create & Download`.
6. Reconnect the USB to activate the new firmware.
7. Now you can directly drag and drop the `.uf2` firmware to the development board as described above.

### Connecting the Development Board

Connect the development board via USB. A serial port will appear on your computer.

Baud Rate: 115200

Data Bits: 8

## Expected Results

Build successful, and upon pressing the BOOT button on the development board, the onboard LED changes color. The serial port outputs the LED color information.

## Actual Results

Build successful, and pressing the BOOT button on the development board causes the onboard LED to change color. The serial port outputs the LED color information.

[![asciicast](https://asciinema.org/a/MjevQgMAxbPcjP0Uj1RJdEdQl.svg)](https://asciinema.org/a/MjevQgMAxbPcjP0Uj1RJdEdQl)

### Boot Log

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
