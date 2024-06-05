# BuildRoot Milk-V Duo 256M Test Report

## Test Environment

### Operating System Information

- Download Link: https://github.com/milkv-duo/duo-buildroot-sdk/releases
- Reference Installation Document: https://github.com/milkv-duo/duo-buildroot-sdk
    - FreeRTOS: https://milkv.io/zh/docs/duo/getting-started/rtoscore

### Hardware Information

- Milk-V Duo 256M
- One USB-A to C or USB-C to C Cable
- One microSD card
- One USB to UART Debugger (e.g., CH340, CH341, FT2232)
- Optional: Milk-V Duo IOB (Baseboard)

## Installation Steps

RTOS is included in the BuildRoot SDK.

### Building the mailbox-test Binary

Clone the duo-examples repository locally and build it.

```shell
sudo apt install -y wget git make
git clone https://github.com/milkv-duo/duo-examples --depth=1
cd duo-examples
source envsetup.sh
cd mailbox-test
make
```

#### Copy the Built Binary into the Image

First, check the current available loop devices:

```shell
sudo losetup -f
```

The output should be:

```shell
$ sudo losetup -f
/dev/loop16
```

Next, mount the downloaded image and copy the compiled binary into it:

```shell
sudo losetup /dev/loop16 milkv-duo256m-v1.1.0-2024-0410.img
sudo kpartx -av /dev/loop16
sudo mount /dev/mapper/loop16p2 /mnt
cp ~/duo-examples/mailbox-test/mailbox_test /mnt/root/
sudo umount /mnt
sudo kpartx -d /dev/loop1
sudo losetup -d /dev/loop16 
```

Then flash the modified image:

```shell
sudo dd if=milkv-duo256m-v1.1.0-2024-0410.img of=/dev/sdc bs=4M status=progress oflag=direct
```

At this point, the storage card is ready. Insert it into the development board and prepare to boot.

### Logging into the System

Logging into the system via the serial port.

Default Username: `root`
Default Password: `milkv`

## Expected Results

The system boots normally, and after logging in through the onboard serial port, running the `mailbox_test` binary will cause the onboard blue LED to light up and then turn off.

(Standby state: blue LED blinks)

## Actual Results

The system booted normally, successfully logged in via the onboard serial port. The `mailbox_test` ran successfully, and the onboard LED lit up and then turned off.

### Boot Log

```log
The authenticity of host '192.168.42.1 (192.168.42.1)' can't be established.
ED25519 key fingerprint is SHA256:JrNwim4ZPbnSw+aC9orl+VPBoRBkXxMatEDjRSq8SSw.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '192.168.42.1' (ED25519) to the list of known hosts.
root@192.168.42.1's password: 
[root@milkv-duo]~# ./mailbox_test 
C906B: cmd.param_ptr = 0x4
C906B: cmd.param_ptr = 0x3
[root@milkv-duo]~# exit

```

Screen recording:
[![asciicast](https://asciinema.org/a/MhkD6TsSDQ9N0w4u2k6VUHn3s.svg)](https://asciinema.org/a/MhkD6TsSDQ9N0w4u2k6VUHn3s)

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.

