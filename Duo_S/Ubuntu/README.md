---
sys: ubuntu
sys_ver: "24.04"
sys_var: null

status: basic
last_update: 2026-09-14
---

# Ubuntu Milk-V Duo S Test Report

## Test Environment

### Operating System Information

- System Version: Ubuntu 24.04 LTS
- Download Link: https://github.com/queenkjuul/milkv-duo-ubuntu/releases/tag/v7.0.6-qkj1
- Reference Installation Document: https://github.com/queenkjuul/milkv-duo-ubuntu/wiki/Building-the-System

> Note: This image is provided by community developers and is not an official image.

### Hardware Information

- Milk-V Duo S (512M, SG2000)
- A USB power adapter
- A USB-A to C or USB C to C cable for powering the development board
- A microSD card
- A USB card reader
- A USB to UART Debugger
    - Only CP210x series is recommeneded (e.g. CP2102/CP2104). Be aware you'll only get garbled text output on WCH CH340/341 series; you can still use other USB-UART chips like FT232 and CH343 series, although you might still get garbled output but only before U-Boot loads, this is expected. If UART isn't working at all please consider try another USB-UART adaptor.
- Three DuPont wires

## Installation Steps

### Using `dd` to Flash the Image to the microSD Card
```bash
sudo dd if=ubuntu-noble-milkv-duos.img of=/dev/sdX bs=1M status=progress
```
> Note: Replace `/dev/sdX` with the actual SD card device name.

### Logging into the System

Logging into the system via the serial port.

## Expected Results

The system boots up normally and allows login through the onboard serial port.

## Actual Results

The system boots up normally and login through the onboard serial port is successful.

### Boot Information

```bash
[  OK  ] Started dbus.service - D-Bus System Message Bus.
[  OK  ] Finished e2scrub_reap.service - Re…line ext4 Metadata Check Snapshots.
[  OK  ] Finished sysstat.service - Resets System Activity Logs.
[  OK  ] Finished milkv-usb.service - Milk-V Duo S USB OTG.

Ubuntu 24.04 LTS milkv-duos ttyS0

milkv-duos login: root
Password:
Welcome to Ubuntu 24.04 LTS (GNU/Linux 7.0.6-qkj1-duos riscv64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/pro
root@milkv-duos:~# neofetch
            .-/+oossssoo+/-.               root@milkv-duos
        `:+ssssssssssssssssss+:`           ---------------
      -+ssssssssssssssssssyyssss+-         OS: Ubuntu 24.04 LTS riscv64
    .ossssssssssssssssssdMMMNysssso.       Host: Milk-V Duo S
   /ssssssssssshdmmNNmmyNMMMMhssssss/      Kernel: 7.0.6-qkj1-duos
  +ssssssssshmydMMMMMMMNddddyssssssss+     Uptime: 1 min
 /sssssssshNMMMyhhyyyyhmNMMMNhssssssss/    Packages: 402 (dpkg)
.ssssssssdMMMNhsssssssssshNMMMdssssssss.   Shell: bash 5.2.21
+sssshhhyNMMNyssssssssssssyNMMMysssssss+   Terminal: /dev/ttyS0
ossyNMMMNyMMhsssssssssssssshmmmhssssssso   CPU: (1)
ossyNMMMNyMMhsssssssssssssshmmmhssssssso   Memory: 74MiB / 466MiB
+sssshhhyNMMNyssssssssssssyNMMMysssssss+
.ssssssssdMMMNhsssssssssshNMMMdssssssss.
 /sssssssshNMMMyhhyyyyhdNMMMNhssssssss/
  +sssssssssdmydMMMMMMMMddddyssssssss+
   /ssssssssssshdmNNNNmyNMMMMhssssss/
    .ossssssssssssssssssdMMMNysssso.
      -+sssssssssssssssssyyyssss+-
        `:+ssssssssssssssssss+:`
            .-/+oossssoo+/-.

root@milkv-duos:~#
```
Screen recording:

[![asciicast](https://asciinema.org/a/u4DNnLipiGEsxTl4.svg)](https://asciinema.org/a/u4DNnLipiGEsxTl4)


## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
