---
sys: NixOS
sys_ver: null
sys_var: null

status: basic
last_update: 2024-12-20
---

# Nixos LicheePi RV Dock Test Report

## Test Environment

### Operating System Information

- Download link: https://github.com/chuangzhu/nixos-sun20iw1p1/releases
- Reference Installation Document: https://github.com/chuangzhu/nixos-sun20iw1p1

### Hardware Information

- Sipeed LicheePi RV Dock
- A USB-A Power Adapter
- A USB-A to C Cable
- A microSD Card
- A USB to UART Debugger (e.g., CH340, CH341, FT2232, etc.)
- Three DuPont Wires

## Installation Steps

### Flashing Image to microSD Card

Use `dd` to flash the image to the microSD card.

### Logging into the System

Logging into the system via the serial port.

No passwd. On first login, the system will prompt you to change the password.

## Expected Results

The system should boot normally and allow login via the onboard serial port.

## Actual Results

The system booted successfully and login via the onboard serial port was also successful.

### Boot Log

```log
<<< Welme to NixOS 22.11come to NixOS 22..11.20221014.4428e23 (riscv64) - ttyS0 >>>
The "nixos" and 20221014.4428e23"root" accounts have empty passwords.

An ssh daemon is running. You then must set a password
for either "roo (riscv64) - hvc0 >>>
t" or "nixos" with `passwd` or add an ssh key
to /home/nixos/.ssh/authorized_keys be able to loThe "nixos" and "root" accounts have empty passworgin.

If you need a wireless connection, type
`sudo systemctl start wpa_supplicant` and configure a
network using `wpa_cli`. See the NixOS mds.

An ssh daemon is running. You theanual for details.


Run 'nixos-help' for the NixOS manual.

nixos login: nixos (automatic login)

n must set a password
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
```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
