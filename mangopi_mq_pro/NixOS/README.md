---
sys: NixOS
sys_ver: null
sys_var: null

status: basic
last_update: 2025-03-07
---

# NixOS MangoPi MQ Pro Test Report

## Test Environment

### Operating System Information

- System version: 22.11.20221014
- Source code link: https://github.com/chuangzhu/nixos-sun20iw1p1/releases/download/hdmi/nixos-sd-image-22.11.20221014.4428e23-riscv64-linux.img.zst
- Reference Installation Document: https://github.com/chuangzhu/nixos-sun20iw1p1/

### Hardware Information

- MangoPi MQ Pro
- A USB-A Power Adapter
- A USB-A to C Cable
- A microSD Card
- A microSD Card Reader
- A USB to UART Debugger (e.g., CH340, CH341, FT2232, etc.)
- Three DuPont Wires

## Installation Steps

### Decompress and Flash Image to microSD Card

```shell
zstd -d https://github.com/chuangzhu/nixos-sun20iw1p1/releases/download/hdmi/nixos-sd-image-22.11.20221014.4428e23-riscv64-linux.img.zst
dd if=/path/to/your/nixos-sd-image-22.11.20221014.4428e23-riscv64-linux.img of=/dev/your/device bs=4M status=progress
```

### Logging into the System

Logging into the system via the serial port.

No password are set and will automatically login by default.

## Expected Results

The system should boot normally and allow login via the onboard serial port.

## Actual Results

The system booted successfully and login via the onboard serial port was also successful.

### Boot Log

```log
<<< Welcome to NixOS 22.11.20221014.4428e23 (riscv64) - ttyS0 >>>
<<< WelcoThe "nixos" and "root" accounts have empty passwords.

An ssh daemon is runninme to NixOS 22.11g. You then must set a password
for either "root" or "nixos" with `passwd` or a.dd an ssh key
to /home/nixos/.ssh/authorized_keys be able to login.

If you need a wireless connection, type
`sudo systemctl start wpa_supplicant` and configure a
network using `wpa_cli`.20221014.4428e23 (riscv64) - hvc0 See the NixOS manual for details.


Run 'nixos-help' for the NixOS manual.

nixos login: nixos (automatic  >>>
The "nixos" and "login)

root" accounts have empty passwords.

An ssh daemon is running. You then must set a password
for either "root" or "nixos" with `passwd` or add an ssh key
to /home/nixos/.ssh/authorized_keys be able to login.

If you need a wireless connection, type
`sudo systemctl start wpa_supplicant` and configure a
network using `wpa_cli`. See the NixOS manual for details.


Run 'nixos-help' for the NixOS manual.

nixos login: nixos (automatic login)


[nixos@nixos:~]$ 
[nixos@nixos:~]$ uname -a
Linux nixos 5.18.0-rc1 #1-NixOS PREEMPT Tue Jan 1 00:00:00 UTC 1980 riscv64 GNU/Linux

[nixos@nixos:~]$ cat /etc/os-release 
BUG_REPORT_URL="https://github.com/NixOS/nixpkgs/issues"
BUILD_ID="22.11.20221014.4428e23"
DOCUMENTATION_URL="https://nixos.org/learn.html"
HOME_URL="https://nixos.org/"
ID=nixos
LOGO="nix-snowflake"
NAME=NixOS
PRETTY_NAME="NixOS 22.11 (Raccoon)"
SUPPORT_URL="https://nixos.org/community.html"
VERSION="22.11 (Raccoon)"
VERSION_CODENAME=raccoon
VERSION_ID="22.11"

[nixos@nixos:~]$ cat /proc/cpuinfo
processor       : 0
hart            : 0
isa             : rv64imafdc
mmu             : sv39
uarch           : thead,c906


[nixos@nixos:~]$ 

```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
