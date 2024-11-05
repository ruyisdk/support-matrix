---
sys: freertos
sys_ver: null
sys_var: null

status: basic
last_update: 2024-11-05
---

# FreeRTOS Milk-V Duo Test Report

## Test Environment

### Operating System Information

- Build System: Ubuntu 22.04.3 LTS x86_64
- System Version: Duo-V1.1.3
- Download Link: [Duo-Buildroot-SDK Releases](https://github.com/milkv-duo/duo-buildroot-sdk/releases)
- Reference Installation Document: [Duo-Buildroot-SDK](https://github.com/milkv-duo/duo-buildroot-sdk)
    - FreeRTOS: [FreeRTOS Core](https://milkv.io/zh/docs/duo/getting-started/rtoscore)

### Hardware Information

- Milk-V Duo 64M
- A USB Power Adapter
- A USB-A to C or USB C to C Cable
- A microSD Card
- A USB to UART Debugger (e.g., CH340, CH341, FT2232, etc.)
- Three Jumper Wires
- Milk-V Duo pre-soldered with necessary pins for debugging
- Optional: Milk-V Duo IOB (Baseboard)

## Installation Steps

### Building the mailbox-test Binary

Clone the duo-examples repository locally and build the binary.

```shell
sudo apt install -y wget git make
git clone https://github.com/milkv-duo/duo-examples --depth=1
cd duo-examples
source envsetup.sh
cd mailbox-test
make
```
#### Packaging the Binary into the Image

First, check available loop devices:

```shell
sudo losetup -f
```

Sample Output:

```shell
$ sudo losetup -f
/dev/loop0
```

Download the official Buildroot SDK:

```shell
wget https://github.com/milkv-duo/duo-buildroot-sdk/releases/download/v1.1.3/milkv-duo-sd-v1.1.3-2024-0930.img.zip
unzip milkv-duo-sd-v1.1.3-2024-0930.img.zip
```

Next, mount the downloaded image and copy the compiled mailbox_test binary into the image:

```shell
sudo losetup /dev/loop0 milkv-duo-sd-v1.1.3-2024-0930.img
sudo kpartx -av /dev/loop0
sudo mount /dev/mapper/loop0p2 /mnt
cp ~/duo-examples/mailbox-test/mailbox_test /mnt/root/
sudo umount /mnt
sudo kpartx -d /dev/loop0
sudo losetup -d /dev/loop0
```

Then, flash the modified image:

```shell
sudo dd if=milkv-duo-sd-v1.1.3-2024-0930.img of=/dev/sdc bs=4M status=progress
```

At this stage, the storage card is prepared. Insert it into the development board and get ready to boot.

### Logging into the System

Logging into the system via the serial port.

## Expected Results

The system should boot normally. After logging in through the onboard serial port, the `mailbox_test` binary should run, causing the onboard blue LED to turn on and then off.

(In standby mode, the blue LED should blink)

## Actual Results

The system booted successfully, logging in through the onboard serial port was successful, and the `mailbox_test` ran correctly with the onboard LED turning on and then off.

### Boot Log

```log
[    2.629875] sync_task_init:177(): sync_task_init vi_pipe 0
[    2.635850] sync_task_init:177(): sync_task_init vi_pipe 1
[    2.641810] sync_task_init:177(): sync_task_init vi_pipe 2
[    2.648237] vi_core_probe:252(): isp registered as cvi-vi
[    2.701678] cvi_dwa_probe:487(): done with rc(0).
[    2.731805] cv180x-cooling cv180x_cooling: elems of dev-freqs=6
[    2.738146] cv180x-cooling cv180x_cooling: dev_freqs[0]: 850000000 500000000
[    2.745950] cv180x-cooling cv180x_cooling: dev_freqs[1]: 425000000 375000000
[    2.753585] cv180x-cooling cv180x_cooling: dev_freqs[2]: 425000000 300000000
[    2.761332] cv180x-cooling cv180x_cooling: Cooling device registered: cv180x_cooling
[    2.795351] jpu ctrl reg pa = 0xb030000, va = (____ptrval____), size = 256
[    2.803013] end jpu_init result = 0x0
[    2.928217] cvi_vc_drv_init result = 0x0
[    2.943974] sh (165): drop_caches: 3
Starting app...

[root@milkv-duo]~# ls
mailbox_test
[root@milkv-duo]~# ./mailbox_test 
RT: [44.439088]prvQueueISR
RT: [44.441435]recv cmd(19) from C906B, param_ptr [0x00000002]
RT: [44.447166]recv cmd(19) from C906B...send [0x00000004] to C906B
C906B: cmd.param_ptr = 0x4
RT: [48.454192]prvQueueISR
RT: [48.456537]recv cmd(19) from C906B, param_ptr [0x00000003]
RT: [48.462270]recv cmd(19) from C906B...send [0x00000004] to C906B
C906B: cmd.param_ptr = 0x3
[root@milkv-duo]~# 
```

Screen recording:

[![asciicast](https://asciinema.org/a/IANV6OK3PCAMO3L7hcx11ngck.svg)](https://asciinema.org/a/IANV6OK3PCAMO3L7hcx11ngck)

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
