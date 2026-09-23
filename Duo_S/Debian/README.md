---
sys: debian
sys_ver: 1.9.6
sys_var: null
provider: Community

status: basic
last_update: 2026-09-08
---

# Debian Milk-V Duo S Test Report

## Test Environment

### Operating System Information

- System Version: Debian 13 (trixie), community image v1.9.6
- Download Link: https://github.com/scpcom/sophgo-sg200x-debian/releases/tag/v1.9.6
- Reference Installation Document: https://github.com/scpcom/sophgo-sg200x-debian

### Hardware Information

- Milk-V Duo S (512M, SG2000)
- A USB power adapter
- A USB-A to C or USB C to C cable for powering the development board
- A microSD card
- A USB card reader
- A USB to UART Debugger
- Three DuPont wires

## Installation Steps

### Using `dd` to Flash the Image to the microSD Card

```shell
lz4 -dk duos-e_sd.img.lz4
sudo dd if=duos-e_sd.img of=/dev/sdX bs=1M status=progress
```

### Logging into the System

Logging into the system via the serial port.

## Expected Results

The system boots up normally and allows login through the onboard serial port.

## Actual Results

The system boots up normally and login through the onboard serial port is successful.

### Boot Information

```log
         Starting systemd-random-seed.service - Load/Save OS Random Seed...
[   13.079265] systemd[1]: Failed to start systemd-sysctl.service - Apply Kernel Variables.
[FAILED] Failed to start systemd-sysctl.service - Apply Kernel Variables.
See 'systemctl status systemd-sysctl.service' for details.

Debian GNU/Linux 13 duos-1f79 ttyS0

duos-1f79 login: root
Password:
Linux duos-1f79 5.10.260-20260711-6+duos #1 PREEMPT Tue Jul 14 03:03:04 UTC 2026 riscv64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
root@duos-1f79:~# lscpu
Architecture:          riscv64
  Byte Order:          Little Endian
CPU(s):                1
  On-line CPU(s) list: 0
root@duos-1f79:~# uname -a
Linux duos-1f79 5.10.260-20260711-6+duos #1 PREEMPT Tue Jul 14 03:03:04 UTC 2026 riscv64 GNU/Linux
root@duos-1f79:~#

```

> During boot, `systemd-sysctl.service` failed to start. The cause has not been confirmed. Serial console login was successful in this test.

Screen recording:

[![asciicast](https://asciinema.org/a/x5lUx5XQO1zB9w2C.svg)](https://asciinema.org/a/x5lUx5XQO1zB9w2C)

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful. The system boots up normally and login through the onboard serial port is successful.
