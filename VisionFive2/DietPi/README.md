---
sys: dietpi
sys_ver: v9.7.1 (MichaIng/master)
sys_var: null

status: basic
last_update: 2024-10-25
---

# DietPi VisionFive 2 Test Report

## Test Environment

### Operating System Information

- System Version: v9.7.1 (MichaIng/master)
- Download Link: https://dietpi.com/downloads/images/testing/DietPi_VisionFive2-RISC-V-Sid.img.xz
- Reference Installation Document: https://dietpi.com/blog/?p=2629

### Hardware Information

- StarFive VisionFive 2
- A USB Power Adapter
- A USB-A to C or C to C Cable
- A microSD Card
- A USB to UART Debugger (e.g., CH340, CH341, FT2232, etc.)
- Three Dupont Wires

## Installation Steps

### Decompress and Flash Image to microSD Card


```bash
xz -d DietPi_VisionFive2-RISC-V-Sid.img.xz
dd if=DietPi_VisionFive2-RISC-V-Sid.img of=/dev/<your-device> 
```

### Boot Mode Selection

StarFive VisionFive 2 offers various boot modes, which can be configured via onboard dip switches before powering on; there are also silk screen labels on the development board itself.

To boot the Dietpi image, you can select the 1-bit QSPI Nor Flash mode (i.e., `RGPIO_0 = 0`, `RGPIO_1 = 0`). Note that this mode may require a prior firmware update in the Flash. If your boot is unsuccessful, please refer to the official documentation for firmware upgrading: [Update SPL and U-Boot](https://doc.rvspace.org/VisionFive2/Quick_Start_Guide/VisionFive2_QSG/spl_u_boot_0.html)

### Logging into the System

Logging into the system via the serial port.

Username: `root`
Default Password: `dietpi`

## Expected Results

The system boots normally and allows login via the serial port.

## Actual Results

The system booted normally and login via the serial port was successful.

### Boot Log

```log
Debian GNU/Linux trixie/sid DietPi ttyS0

DietPi login: root
Password: 
Linux DietPi 6.1.97 #1 SMP Fri Jul  5 23:02:10 UTC 2024 riscv64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
 ─────────────────────────────────────────────────────
 DietPi v9.7.1 : 14:51 - Fri 10/25/24
 ─────────────────────────────────────────────────────
 - LAN IP : 192.168.31.87 (eth0)

 DietPi-Update
─────────────────────────────────────────────────────
 Phase: Checking for available DietPi update

[  OK  ] DietPi-Update | Checking IPv4 network connectivity
[  OK  ] DietPi-Update | Checking DNS resolver
[  OK  ] DietPi-TimeSync | systemctl start systemd-timesyncd
[ INFO ] DietPi-TimeSync | Waiting for time sync (1/60)
[ INFO ] DietPi-TimeSync | Waiting for time sync (2/60)
[ INFO ] DietPi-TimeSync | Waiting for time sync (3/60)
[ INFO ] DietPi-TimeSync | Waiting for time sync (4/60)
[ INFO ] DietPi-TimeSync | Waiting for time sync (5/60)
[ INFO ] DietPi-TimeSync | Waiting for time sync (6/60)
[ INFO ] DietPi-TimeSync | Waiting for time sync (7/60)
[  OK  ] DietPi-TimeSync | Time sync completed
[  OK  ] DietPi-TimeSync | systemctl stop systemd-timesyncd
[  OK  ] DietPi-TimeSync | mkdir -p /run/systemd/timesync
[ INFO ] DietPi-Update | Getting latest version from: https://raw.githubusercontent.com/MichaIng/DietPi/master/.update/version
[  OK  ] DietPi-Update | Got valid latest version: 9.8.0
[  OK  ] DietPi-Update | Update available:
[ INFO ] DietPi-Update | Current version : v9.7.1
[ INFO ] DietPi-Update | Latest version  : v9.8.0

 DietPi-Update
─────────────────────────────────────────────────────
 Phase: Checking for update pre-requirements

[  OK  ] DietPi-Update | DietPi-Userdata validation: /mnt/dietpi_userdata
[  OK  ] DietPi-Update | Free space check: path=/ | available=28171 MiB | required=100 MiB
[ SUB1 ] DietPi-Services > stop 
[  OK  ] DietPi-Services | stop : cron

 DietPi-Update
─────────────────────────────────────────────────────
 Phase: Applying pre-patches

[  OK  ] DietPi-Update | Downloading pre-patches
[  OK  ] DietPi-Update | Applying execute permission
[  OK  ] DietPi-Update | Successfully applied pre-patches

 DietPi-Update
StarFive VisionFive 2 (riscv64) | IP: 192.168.31.87 | Use up/down buttons to scr
│ APT update
│  - Command: apt-get -y -eany update
│  - Exit code: 100
│  - DietPi version: v9.7.1 (MichaIng/master) | HW_MODEL: 81 | HW_ARCH: 11 |
│ DISTRO: 8
root@DietPi:~# cat /etc/os-release 
PRETTY_NAME="Debian GNU/Linux trixie/sid"
NAME="Debian GNU/Linux"
VERSION_CODENAME=trixie
ID=debian
HOME_URL="https://www.debian.org/"
SUPPORT_URL="https://www.debian.org/support"
BUG_REPORT_URL="https://bugs.debian.org/"
root@DietPi:~# uname -a 
Linux DietPi 6.1.97 #1 SMP Fri Jul  5 23:02:10 UTC 2024 riscv64 GNU/Linux
```

Screen recording (logging into the system):
[![asciicast](https://asciinema.org/a/IMU31fDOjU2FgiYnFjriTaycE.svg)](https://asciinema.org/a/IMU31fDOjU2FgiYnFjriTaycE)

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
