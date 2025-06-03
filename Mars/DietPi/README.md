---
sys: dietpi
sys_ver: "9.12.1"
sys_var: null

status: basic
last_update: 2025-05-24
---

# DietPi Milk-V Mars Test Report

## Test Environment

### Operating System Information

- System Version: DietPi v9.12.1
- Download Link: <https://dietpi.com/downloads/images/testing/DietPi_VisionFive2-RISC-V-Trixie.img.xz>
- Reference Installation Document:
  - <https://milkv.io/zh/docs/mars/getting-started/boot>
  - <https://dietpi.com/blog/?p=2629>

### Hardware Information

- Milk-V Mars (8GB RAM)
- A USB power adapter and A USB-A to C or C to C cable
- A microSD card
- A USB to UART debugger (e.g., CH340, CH341, FT2232, etc.)

## Installation Steps

### Decompress and Flash Image to microSD Card

Use `xz` to decompress the image,  and then use `dd` command or `balenaEtcher` software to flash the image to the microSD card. (Assuming `/dev/sdc` is the microSD card device)

```bash
wget https://dietpi.com/downloads/images/testing/DietPi_VisionFive2-RISC-V-Trixie.img.xz

xz -d DietPi_VisionFive2-RISC-V-Trixie.img.xz

sudo dd if=DietPi_VisionFive2-RISC-V-Trixie.img of=/dev/sdc bs=1M status=progress

sync
```

### Boot Mode Selection

Milk-V Mars provides multiple boot modes after the hardware version V1.2, which can be configured via onboard dip switches before powering on; the board itself is also silk-screened for reference.

To boot the Armbian image, select the SPI Flash boot mode (`GPIO_0 = 0`, `GPIO_1 = 0`). Note that this mode may require you to update the firmware in the Flash beforehand.

### Logging into the System

Log into the system via the serial port.

Default Username: `root`

Default Password: `dietpi`

After entering the system, it will be connected to the network and start the update. If there is a network problem, the ip address of the network check command can be changed to `8.8.8.8` in the interactive interface.

## Expected Results

The system should boot up normally and allow login via the serial port.

## Actual Results

The system starts normally and the output is successfully viewed through the serial port.

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
 DietPi v9.12.1 : 17:21 - Sun 05/25/25
 ─────────────────────────────────────────────────────
 - LAN IP : 192.168.137.102 (eth0)
tee: /var/tmp/dietpi/logs/dietpi-firstrun-setup.log: No such file or directory

 DietPi-Update
─────────────────────────────────────────────────────
 Phase: Checking for available DietPi update

[.     ]PING 9.9.9.9 (9.9.9.9) 56(84) bytes of data.ctivity (2/2)

--- 9.9.9.9 ping statistics ---
1 packets transmitted, 0 received, 100% packet loss, time 0ms

[FAILED] DietPi-Update | Checking IPv4 network connectivity
 - Command: ping -4nc 1 -W 10 9.9.9.9
StarFive VisionFive 2 (riscv64) | IP: 192.168.137.102




  ┌──────────────────────────────────────────────────┤ DietPi-Update ├───────────────────────────────────────────────────┐
  │ Checking IPv4 network connectivity                                                                                   │
  │  - Command: ping -4nc 1 -W 10 9.9.9.9                                                                                │
  │  - Exit code: 1                                                                                                      │
  │  - DietPi version: v9.12.1 (MichaIng/master) | HW_MODEL: 81 | HW_ARCH: 11 | DISTRO: 8                                │
  │  - Error log:                                                                                                        │
  │ PING 9.9.9.9 (9.9.9.9) 56(84) bytes of data.                                                                         │
  │                                                                                                                      │
  │ --- 9.9.9.9 ping statistics ---                                                                                      │
  │ 1 packets transmitted, 0 received, 100% packet loss, time 0ms                                                        │
  │                                                                                                                      │
  │                    Retry               : Re-run the last command that failed                                         │
  │                    Double timeout      : Retry with doubled timeout for ping to wait for a reply                     │
  │                    Change IPv4 address : Change the IPv4 address used for this test                                  │
  │                    Network settings    : Enter dietpi-config network options                                         │
  │                    DietPi-Config       : Edit network, APT/NTP mirror settings etc                                   │
  │                    Open subshell       : Open a subshell to investigate or solve the issue                           │
  │                    Send report         : Upload bug report including system info to DietPi                           │
  │                    Print report        : Print bug report template for GitHub or forum                               │
  │                                        ●─ Devs only ───────────────────────────────────────────●                     │
  │                    Change command      : Adjust and rerun the command                                                │
  │                                                                                                                      │
  │                                                                                                                      │
  │                                  <Select>                                  <Exit>                                    │
  │                                                                                                                      │
  └──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
StarFive VisionFive 2 (riscv64) | IP: 192.168.137.102




  ┌──────────────────────────────────────────────────┤ DietPi-Update ├───────────────────────────────────────────────────┐
  │ Please enter/alter the command to be executed.                                                                       │
  │                                                                                                                      │
  │ NB: Please only use this solution if you know for sure that it will not cause follow up issues from the originating  │
  │ script. It will e.g. allow you to continue a certain software install, but if you edit the download link, the        │
  │ originating script might expect files which are not present.                                                         │
  │                                                                                                                      │
  │ Use this with caution!                                                                                               │
  │                                                                                                                      │
  │ ping -4nc 1 -W 10 8.8.8.8___________________________________________________________________________________________ │
  │                                  <Ok>                                      <Cancel>                                  │
  │                                                                                                                      │
  └──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘


[ INFO ] DietPi-Update | Executing alternative command: ping -4nc 1 -W 10 8.8.8.8
PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
64 bytes from 8.8.8.8: icmp_seq=1 ttl=112 time=29.1 ms

--- 8.8.8.8 ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 29.087/29.087/29.087/0.000 ms
[  OK  ] Alternative command execution | Completed
[  OK  ] DietPi-Update | Checking DNS resolver
[  OK  ] DietPi-TimeSync | systemctl stop systemd-timesyncd
[  OK  ] DietPi-TimeSync | mkdir -p /run/systemd/timesync
[ INFO ] DietPi-Update | Getting latest version from: https://raw.githubusercontent.com/MichaIng/DietPi/master/.update/version

[  OK  ] DietPi-Update | Got valid latest version: 9.12.1
[  OK  ] DietPi-Update | eval echo 1 > /boot/dietpi/.install_stage
[  OK  ] DietPi-Update | No update required, your DietPi installation is already up to date:
[ INFO ] DietPi-Update | Current version : v9.12.1
[ INFO ] DietPi-Update | Latest version  : v9.12.1
[ INFO ] DietPi-Update | Checking for new available live patches
[ INFO ] DietPi-Update | APT update, please wait...


[  OK  ] DietPi-Survey | Setting in /boot/dietpi.txt adjusted: SURVEY_OPTED_IN=0
[  OK  ] DietPi-Survey | Purging survey data
[ SUB1 ] DietPi-Services > restart
[  OK  ] DietPi-Services | restart : cron
 ─────────────────────────────────────────────────────
 DietPi v9.12.1 : 17:49 - Sun 05/25/25
 ─────────────────────────────────────────────────────
 - Device model : StarFive VisionFive 2 (riscv64)
 - CPU temp : 58 °C / 136 °F : Running warm, but safe
 - LAN IP : 192.168.137.102 (eth0)
 - MOTD : Open Beta v9.13 | Please help testing our upcoming release:
          https://github.com/MichaIng/DietPi/issues/7539
 ─────────────────────────────────────────────────────

 DietPi Team     : https://github.com/MichaIng/DietPi#the-dietpi-project-team
 Patreon Legends : Chris Gelatt, ADSB.im
 Website         : https://dietpi.com/ | https://x.com/DietPi_ | Bsky: @dietpi.com
 Contribute      : https://dietpi.com/contribute.html
 Web Hosting by  : https://myvirtualserver.com

 dietpi-launcher : All the DietPi programs in one place
 dietpi-config   : Feature rich configuration tool for your device
 dietpi-software : Select optimised software for installation
 htop            : Resource monitor
 cpu             : Shows CPU information and stats

root@DietPi:~# cat /etc/os-release
PRETTY_NAME="Debian GNU/Linux 13 (trixie)"
NAME="Debian GNU/Linux"
VERSION_ID="13"
VERSION="13 (trixie)"
VERSION_CODENAME=trixie
DEBIAN_VERSION_FULL=13.0
ID=debian
HOME_URL="https://www.debian.org/"
SUPPORT_URL="https://www.debian.org/support"
BUG_REPORT_URL="https://bugs.debian.org/"

root@DietPi:~# uname -a
Linux DietPi 6.1.97 #1 SMP Fri Jul  5 23:02:10 UTC 2024 riscv64 GNU/Linux

root@DietPi:~# cat /proc/cpuinfo
processor       : 0
hart            : 1
isa             : rv64imafdc
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x4210427

processor       : 1
hart            : 2
isa             : rv64imafdc
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x4210427

processor       : 2
hart            : 3
isa             : rv64imafdc
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x4210427

processor       : 3
hart            : 4
isa             : rv64imafdc
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x4210427
```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
