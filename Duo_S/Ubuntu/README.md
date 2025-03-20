---
sys: ubuntu
sys_ver: 22.04
sys_var: null

status: basic
last_update: 2025-03-18
---

# Ubuntu Milk-V Duo S Test Report

### Operating System Information

- System Version: Ubuntu 22.04
- Download Link: https://drive.google.com/file/d/1mkzLhvtjJup3GbgWKZdwL80PZMMXg7n1/view
- Reference Installation Document: https://xyzdims.com/3d-printers/misc-hardware-notes/iot-milk-v-duo-risc-v-esbc-running-linux/

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
sudo dd if=milkv-duo-256m-ubuntu-22.04-riscv64-v0.0.4-spiritdude.img of=/dev/your/device bs=1M status=progress
```

### Logging into the System

Logging into the system via the serial port.

## Expected Results

The system boots up normally and allows login through the onboard serial port.

## Actual Results

The system boots up normally and login through the onboard serial port is successful.

### Boot Information

```bash
[  OK  ] Started Message of the Day.
[  OK  ] Reached target Timer Units.
[  OK  ] Started dnsmasq - A lightw…t DHCP and caching DNS server.
[  OK  ] Reached target Host and Network Name Lookups.
[  OK  ] Started User Login Management.

Ubuntu 22.04 LTS milkv-duo ttyS0

milkv-duo login: root
Password:
Welcome to Ubuntu 22.04 LTS (GNU/Linux 5.10.4-tag- riscv64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

Last login: Tue Sep 19 16:57:30 UTC 2023 from 192.168.42.2 on pts/0
root@milkv-duo:~# neofetch
            .-/+oossssoo+/-.               root@milkv-duo
        `:+ssssssssssssssssss+:`           --------------
      -+ssssssssssssssssssyyssss+-         OS: Ubuntu 22.04 LTS riscv64
    .ossssssssssssssssssdMMMNysssso.       Host: Cvitek. CV181X ASIC. C906.
   /ssssssssssshdmmNNmmyNMMMMhssssss/      Kernel: 5.10.4-tag-
  +ssssssssshmydMMMMMMMNddddyssssssss+     Uptime: 29 secs
 /sssssssshNMMMyhhyyyyhmNMMMNhssssssss/    Packages: 245 (dpkg)
.ssssssssdMMMNhsssssssssshNMMMdssssssss.   Shell: bash 5.1.16
+sssshhhyNMMNyssssssssssssyNMMMysssssss+   Terminal: /dev/ttyS0
ossyNMMMNyMMhsssssssssssssshmmmhssssssso   CPU: (1)
ossyNMMMNyMMhsssssssssssssshmmmhssssssso   Memory: 39MiB / 240MiB
+sssshhhyNMMNyssssssssssssyNMMMysssssss+
.ssssssssdMMMNhsssssssssshNMMMdssssssss.
 /sssssssshNMMMyhhyyyyhdNMMMNhssssssss/
  +sssssssssdmydMMMMMMMMddddyssssssss+
   /ssssssssssshdmNNNNmyNMMMMhssssss/
    .ossssssssssssssssssdMMMNysssso.
      -+sssssssssssssssssyyyssss+-
        `:+ssssssssssssssssss+:`
            .-/+oossssoo+/-.

root@milkv-duo:~#
```
Screen recording:

[![asciicast](https://asciinema.org/a/ureP4abokF0DE8AIFQjcdB073.svg)](https://asciinema.org/a/ureP4abokF0DE8AIFQjcdB073)


## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
