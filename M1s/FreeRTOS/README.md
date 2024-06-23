# FreeRTOS Sipeed M1s Dock Test Report

## Test Environment

### Operating System Information

- Download links:
    - SDK: https://gitee.com/Sipeed/M1s_BL808_SDK
    - Examples: https://gitee.com/Sipeed/M1s_BL808_example
    - Flashing Tool: https://dev.bouffalolab.com/download
- Reference Installation Document: https://wiki.sipeed.com/hardware/zh/maix/m1s/other/start.html

### Hardware Information

- Sipeed M1s Dock
- A Type-C cable

## Installation Steps

### Clone SDK and Toolchain

Clone the relevant repositories to your working directory:
```bash
git clone https://gitee.com/Sipeed/M1s_BL808_example.git
git clone https://gitee.com/sipeed/M1s_BL808_SDK.git
```

Get the toolchain:
```bash
mkdir -p M1s_BL808_SDK/toolchain
cd M1s_BL808_SDK/toolchain
git clone https://gitee.com/wonderfullook/m1s_toolchain.git
mv m1s_toolchain Linux_x86_64
cd ../../
```

Set the environment variables:
```bash
cd M1s_BL808_SDK
export BL_SDK_PATH=$(pwd)
cd ..
```

### Compile Code

Compile the hello_world example:
```bash
cd M1s_BL808_example/c906_app
./build.sh hello_world
```

### USB Method for Flashing the Program

Use the Type-C cable to connect your computer to the C port marked **OTG**; you should see a new USB drive appear on your computer:
```log
[66939.561779] usb-storage 3-2:1.0: USB Mass Storage device detected
[66939.562424] scsi host0: usb-storage 3-2:1.0
[66940.569292] scsi 0:0:0:0: Direct-Access     Bouffalo Product          0.01 PQ: 0 ANSI: 2
[66940.570788] sd 0:0:0:0: [sda] 2048 4096-byte logical blocks: (8.39 MB/8.00 MiB)
[66940.570915] sd 0:0:0:0: [sda] Write Protect is off
[66940.570917] sd 0:0:0:0: [sda] Mode Sense: 03 00 00 00
[66940.571039] sd 0:0:0:0: [sda] No Caching mode page found
[66940.571040] sd 0:0:0:0: [sda] Assuming drive cache: write through
[66940.574351]  sda: sda1
[66940.574557] sd 0:0:0:0: [sda] Attached SCSI removable disk

```

Move `d0fw.bin` from the `build_out` directory to the detected USB drive, replacing the device name as needed:
```bash
mkdir mnt
sudo mount /dev/sda1 mnt
sudo mv build_out/d0fw.bin mnt/
sudo umount mnt
rm -r mnt
```

### Serial Method for Flashing the Program

Use the Type-C cable to connect your computer to the C port marked **UART**.

Build the firmware:
```bash
cd M1s_BL808_example/e907_app
./build.sh firmware
```

After downloading the flashing tool, use the tool corresponding to your system to flash the firmware.

Once powered, hold down the boot button, press reset, and then release the boot button.

### Connect to Serial Port

Connect the Type-C cable to the C port marked **UART**.

## Expected Results

The system should boot normally, with serial output.

## Actual Results

The system booted normally, with serial output.

### Boot Information

```log
Starting bl808 now....
Heap Info: 63460 KB @ [0x0x0000000050206f28 ~ 0x0x0000000054000000]
[OS] Starting aos_loop_proc task...
[OS] Start c906 xram handle...
[OS] Starting OS Scheduler...
init ring:0,tx:0x0000000022020140,rx:0x0000000000000000
init ring:2,tx:0x0000000022021340,rx:0x0000000022020340
init ring:3,tx:0x0000000022022540,rx:0x0000000022022340
init ring:4,tx:0x0000000022022840,rx:0x0000000022022740
init ring:5,tx:0x0000000000000000,rx:0x0000000000000000
Init CLI with event Driven
hello, world!
hello, world!
hello, world!

```

Screen Recording:

[![asciicast](https://asciinema.org/a/nYT21u4uOzQ7d7k5KF2Ge6633.svg)](https://asciinema.org/a/nYT21u4uOzQ7d7k5KF2Ge6633)

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
