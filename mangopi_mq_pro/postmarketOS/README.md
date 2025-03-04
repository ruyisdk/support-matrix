---
sys: pmos
sys_ver: null
sys_var: null

status: basic
last_update: 2025-03-04
---

# postmarketOS MangoPi MQ Pro Test Report

## Test Environment

### Operating System Information

- Download link (pmbootstrap): https://wiki.postmarketos.org/wiki/Pmbootstrap
- Reference Installation Document: https://wiki.postmarketos.org/index.php?title=MangoPi_MQ-Pro_(mangopi-mq-pro)&direction=prev&oldid=46021

### Hardware Information

- MangoPi MQ Pro
- Power Adapter
- A microSD card
- A USB to UART Debugger

## Installation Steps

### Install via `pmbootstrap`

Get `pmbootstrap`, e.g. under Arch Linux:
```bash
pacman -S pmbootstrap
```

Bootstrap and flash the system via `pmbootstrap`:
```bash
pmbootstrap init
pmbootstrap install --sdcard=/dev/sdX
pmbootstrap shutdown
```

Various configurations would also be made in the above process. Remember to select the target vendor as `mangopi`, and the target board as `mq-pro`。

### Logging into the System

Logging into to the system via the serial port.

Username and password should be set during installation.

## Expected Results

The system should boot up normally and allow login via the onboard serial port.

## Actual Results

The system booted up normally and login via the onboard serial port was also successful.

The system comes with built-in CDC-NCM which enables serial networking.

### Boot Log

```log
   OpenRC 0.60 is starting up Linux 6.1.0-rc3 (riscv64)

 * /proc is already mounted
 * /run/openrc: creating directory
 * /run/lock: creating directory
 * /run/lock: correcting owner
zram swap: activating with size: 732 MB
 * Caching service dependencies ... [ ok ]
 * Clock skew detected with '/etc/init.d'
 * Adjusting mtime of '/run/openrc/deptree' to Tue Mar  4 13:37:15 2025

 * WARNING: clock skew detected!
 * Remounting devtmpfs on /dev ... [ ok ]
 * Mounting /dev/mqueue ... [ ok ]
 * Mounting /dev/shm ... [ ok ]
 * Mounting debug filesystem ... [ ok ]
 * Mounting config filesystem ... [ ok ]
 * Mounting persistent storage (pstore) filesystem ... [ ok ]
 * Mounting efivarfs filesystem ... [ ok ]
 * Starting udev ... [ ok ]
 * Generating a rule to create a /dev/root symlink ... [ ok ]
 * Populating /dev with existing devices through uevents ... [ ok ]
 * Waiting for uevents to be processed ... [ ok ]
 * WARNING: clock skew detected!
 * Loading modules ... [ ok ]
 * Setting system clock using the hardware clock [UTC] ... [ ok ]
 * Checking local filesystems  ... [ ok ]
 * Remounting filesystems ... [ ok ]
 * Mounting local filesystems ... [ ok ]
 * Configuring kernel parameters ... [ ok ]
 * Creating user login records ... [ ok ]
 * Cleaning /tmp directory ... [ ok ]
 * Setting hostname ... [ ok ]
 * Starting logbookd ...Cannot restore /var/log/logbookd.db
 [ ok ]
 * WARNING: clock skew detected!
 * Activating swap file ...Configured swap file size is 0, skipping creation.
 [ ok ]
 * /run/dbus: creating directory
 * /run/dbus: correcting owner
 * Starting System Message Bus ... [ ok ]
 * Your kernel lacks nftables support, please load
 * appropriate modules and try again.
 * ERROR: nftables failed to start
 * Starting haveged ... [ ok ]
 * Could not find a wireless interface
 * /var/run/wpa_supplicant: creating directory
 * Starting WPA Supplicant ... [ ok ]
 * Starting networkmanager ... [ ok ]
 * Starting chronyd ... [ ok ]
 * Starting kill-pbsplash ...killall: pbsplash: no process killed
 * start-stop-daemon: failed to start `/usr/bin/killall'
 * Failed to start kill-pbsplash
 [ !! ]
 * ERROR: kill-pbsplash failed to start
 * Restoring rfkill configuration ... [ ok ]
 * Starting sleep-inhibitor ... [ ok ]
ssh-keygen: generating new host keys: RSA ECDSA ED25519 
 * Starting sshd ... [ ok ]
 * Activating swap devices ... [ ok ]
zram swap: activating with size: 732 MB
 * Loading zram module...
 [ ok ]
 * Swap->zram0
 [ ok ]
 * Starting local ... [ ok ]

Welcome to postmarketOS
Kernel 6.1.0-rc3 on an riscv64 (/dev/ttyS0)
mangopi-mq-pro login: root
Password: 
Login incorrect
mangopi-mq-pro login: user
Password: 
Welcome to postmarketOS! o/

This distribution is based on Alpine Linux.
First time using postmarketOS? Make sure to read the cheatsheet in the wiki:

-> https://postmarketos.org/cheatsheet

You may change this message by editing /etc/motd.
mangopi-mq-pro:~$ uname -a
Linux mangopi-mq-pro 6.1.0-rc3 #1 Wed Jul 31 00:22:22 UTC 2024 riscv64 Linux
mangopi-mq-pro:~$ cat /etc/os-release
PRETTY_NAME="postmarketOS edge"
NAME="postmarketOS"
VERSION_ID="edge"
VERSION="edge"
ID="postmarketos"
ID_LIKE="alpine"
HOME_URL="https://www.postmarketos.org/"
SUPPORT_URL="https://gitlab.postmarketos.org/postmarketOS"
BUG_REPORT_URL="https://gitlab.postmarketos.org/postmarketOS/pmaports/issues"
LOGO="postmarketos-logo"
ANSI_COLOR="0;32"
mangopi-mq-pro:~$ ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
2: usb0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP qlen 1000
    link/ether (redacted) brd ff:ff:ff:ff:ff:ff
    inet 172.16.42.1/16 brd 172.16.255.255 scope global noprefixroute usb0
       valid_lft forever preferred_lft forever
    inet6 (redacted) scope link noprefixroute 
       valid_lft forever preferred_lft forever
mangopi-mq-pro:~$ 
```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
