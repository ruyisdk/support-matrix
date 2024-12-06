---
sys: debian
sys_ver: 11
sys_var: null

status: good
last_update: 2024-12-06
---

# Debian 11 D1 Test Report

## Test Environment

### Operating System Information

- System Version: Debian
- Download Link: [MEGA](https://mega.nz/folder/lx4CyZBA#PiFhY7oSVQ3gp2ZZ_AnwYA)
- Reference Installation Document: https://wiki.sipeed.com/hardware/en/lichee/RV/flash.html

### Hardware Information

- Sipeed Lichee RV Dock
- Power Adapter
- A microSD card
- A USB to UART Debugger

## Installation Steps

### Flashing Image

1. Run [PhoenixCard](https://dl.sipeed.com/shareURL/LICHEE/D1/Lichee_RV/tool),Click Image marked to choose your target firmware
2. We choose `Startup` marked
3. Click `Burn` marked to burn your target firmware into tf card
4. From Status bar marked to see your progress;If it's red when finishing this means it fails burning, then we should rerun `SD Card Formatter` to format the TF card to increase its success possibility.

### Logging into the System

Log into the system via the serial port.

Default Username: `root`
Default Password: `licheepi`

## Expected Results

The system should boot normally and allow login via the onboard serial port.

## Actual Results

The system booted successfully and login via the onboard serial port was also successful.

### Boot Log

```log
Debian GNU/Linux 11 sipeed ttyS0

sipeed login: root
Password: 
Linux sipeed 5.4.61 #217 PREEMPT Thu Dec 30 06:50:31 UTC 2021 riscv64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Mon May 24 06:56:42 UTC 2021 on ttyS0
root@sipeed:~# uname 
Message from syslogd@sipeed at May 24 06:57:35 ...
 kernel:[  102.178091] Oops [#6]

root@sipeed:~# uname -a
Linux sipeed 5.4.61 #217 PREEMPT Thu Dec 30 06:50:31 UTC 2021 riscv64 GNU/Linux
root@sipeed:~# cat /etc/os-release 
PRETTY_NAME="Debian GNU/Linux 11 (bullseye)"
NAME="Debian GNU/Linux"
VERSION_ID="11"
VERSION="11 (bullseye)"
VERSION_CODENAME=bullseye
ID=debian
HOME_URL="https://www.debian.org/"
SUPPORT_URL="https://www.debian.org/support"
BUG_REPORT_URL="https://bugs.debian.org/"
root@sipeed:~# 
Message from syslogd@sipeed at May 24 06:58:00 ...
 kernel:[  127.198571] Oops [#7]

root@sipeed:~# cat /proc/cpuinfo 
processor       : 0
hart            : 0
isa             : rv64imafdcvu
mmu             : sv39

root@sipeed:~# 
```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
