---
sys: netbsd
sys_ver: null
sys_var: null

status: basic
last_update: 2025-07-13
---

# NetBSD Star64 Test Report

## Test Environment

### System Information

- System Version: NetBSD-current
- Download Link: [riscv64.img.gz](https://nyftp.netbsd.org/pub/NetBSD-daily/HEAD/latest/riscv-riscv64/binary/gzimg/)
(The required dtb files are included in the image)

### Hardware Information

- Pine64 Star64
- A microSD card
- DC 12V5A Barrel power adapter
- A USB to UART Debugger (e.g., CH340, CH341, FT2232, etc.)
- Three Dupont wires

## Installation Steps

### Flashing the Installation Image

Use `gzip` to decompress the image.
Use `dd` or `balenaEtcher` to flash the image to the microSD card.

```bash
sudo dd if=riscv64.img of=/dev/<your-device> bs=1M status=progress
```

### Booting the System

Insert the microSD card, connect the serial port, and use 1-bit QSPI Nor Flash mode (i.e. RGPIO_0 = 0, RGPIO_1 = 0) to boot.

In case of malfunctioning u-boot, try reflashing the SPI as documented in https://doc.rvspace.org/VisionFive2/Quick_Start_Guide/VisionFive2_SDK_QSG/updating_spl_and_u_boot%20-%20vf2.html, before resetting the environment variables with `env default -f -a; env save`.

Manually interrupt the u-boot process and input the boot command:

```bash
load mmc 1:1 ${fdt_addr_r} dtb/starfive/jh7110-pine64-star64.dtb
load mmc 1:1 ${kernel_addr_r} efi/boot/bootriscv64.efi
bootefi ${kernel_addr_r} ${fdt_addr_r}
```

Enter the auto install mode, reboot and re-enter the above startup commands if need to reboot.

### Persist Uboot

```bash
env default -a -f
setenv bootcmd "load mmc 1:1 ${fdt_addr_r} dtb/starfive/jh7110-pine64-star64.dtb; load mmc 1:1 ${kernel_addr_r} efi/boot/bootriscv64.efi; bootefi ${kernel_addr_r} ${fdt_addr_r}"
saveenv
```

### Logging into the System

Log into system as root, without password.

## Expected Results

The system should boot normally and allow login via the onboard serial port.

## Actual Results

The system booted successfully and login via the onboard serial port was also successful.

### Boot Log

```log
Thu Jun 19 22:00:55 UTC 2025
Starting root file system check:
/dev/rdk1: file system is clean; not checking
Not resizing / (NAME=netbsd-root): already correct size
Starting devpubd.
Setting sysctl variables:
ddb.onpanic: 1 -> 0
Starting file system checks:
/dev/rdk0: 49 files, 80246 free (80246 clusters)
random_seed: /var/db/entropy-file: Not present; creating
Saved entropy to /var/db/entropy-file.
Waiting for entropy...done
Setting tty flags.
Starting network.
Hostname: riscv64
IPv6 mode: host
Configuring network interfaces:.
Adding interface aliases:.
Waiting for duplicate address detection to finish...
Starting dhcpcd.
[   6.4699787] eqos0: link state DOWN (was UNKNOWN)
Starting mdnsd.
mDNSResponder: Default: mDNSResponder (Engineering Build) starting
mDNSResponder: Default: AdvertiseInterface: Advertising for ifname lo0
mDNSResponder: State: mDNS_Register_internal: adding to active record list -- name: riscv64.local. (704163d3),     4 riscv64.local. Addr 127.0.0.1
mDNSResponder: Default: Initialized RRSet for    4 riscv64.local. Addr 127.0.0.1
mDNSResponder: Default: RRSet:                3ff82d9960
mDNSResponder: State: mDNS_Register_internal: adding to active record list -- name: 1.0.0.127.in-addr.arpa. (f25c923e),    15 1.0.0.127.in-addr.arpa. PTR riscv64.local.
mDNSResponder: mDNS: Interface not represented in list; marking active and retriggering queries - ifid: -131231744, ifname: lo0, ifaddr: 127.0.0.1
mDNSResponder: mDNS: Interface probe will be delayed - ifname: lo0, ifaddr: 127.0.0.1, probe delay: 512
mDNSResponder: mDNS: Setting AnnounceOwner
mDNSResponder: Default: RestartRecordGetZoneData: ResourceRecords
mDNSResponder: Default: uDNS_SetupDNSConfig: CountOfUnicastDNSServers 0
mDNSResponder: Default:   7: Listening for incoming Unix Domain Socket client requests
mDNSResponder: mDNS: [Q0] mDNS_StartQuery_internal START -- qname: lb._dns-sd._udp.local. (622a68c2), qtype: PTR
mDNSResponder: State: mDNS_Register_internal: adding to active record list -- name: r._dns-sd._udp.local. (4b0e6013),     7 r._dns-sd._udp.local. PTR local.
mDNSResponder: Default: RR Auth now using 1 objects
mDNSResponder: State: mDNS_Register_internal: adding to active record list -- name: b._dns-sd._udp.local. (e7a357e3),     7 b._dns-sd._udp.local. PTR local.
mDNSReBuilding databases: dev, utmp, utmpx, services.
Starting syslogd.
Mounting all file systems...
Jun 19 22:01:01 riscv64 mDNSResponder: mDNS: Sending mDNS message failed - mStatus: -65562
Clearing temporary files.
Checking quotas: done.
Setting securelevel: kern.securelevel: 0 -> 1
Starting virecover.
Starting local daemons:.
Updating motd.
Starting ntpd.
ssh-keygen: 256 SHA256:5KeQhqeIGP/7ZgHKh4pZL/yO2wLmh7U5+8sWnq1BL0A root@riscv64 (ECDSA)
ssh-keygen: 256 SHA256:rs/i1niczU3vaEmQrOO9r6BQCVg+CTzzAaHr/XTDW8s root@riscv64 (ED25519)
ssh-keygen: 3072 SHA256:KoqbvHkwveHEduJKmnKutZOft9Rn1D79o7pezPm4qWY root@riscv64 (RSA)
Starting sshd.
Jun 19 22:01:31 riscv64 syslogd[870]: last message repeated 3 times
postfix: rebuilding /etc/mail/aliases (missing /etc/mail/aliases.db)
Starting postfix.
postfix/postlog: starting the Postfix mail system
Starting inetd.
Starting cron.
Configuring TLS trust anchors.
Thu Jun 19 22:02:03 UTC 2025

NetBSD/riscv (riscv64) (constty)

login: root
Jun 19 22:03:33 riscv64 login: ROOT LOGIN (root) on tty constty
Copyright (c) 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003,
    2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013,
    2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023,
    2024, 2025
    The NetBSD Foundation, Inc.  All rights reserved.
Copyright (c) 1982, 1986, 1989, 1991, 1993
    The Regents of the University of California.  All rights reserved.

NetBSD 10.99.14 (GENERIC64) #0: Thu Jun 19 22:00:54 UTC 2025

Welcome to NetBSD!

This is a development snapshot of NetBSD for testing -- user beware!

Bug reports: https://www.NetBSD.org/support/send-pr.html
Donations to the NetBSD Foundation: https://www.NetBSD.org/donations/
We recommend that you create a non-root account and use su(1) for root access.
riscv64# uname -a
NetBSD riscv64 10.99.14 NetBSD 10.99.14 (GENERIC64) #0: Thu Jun 19 22:00:54 UTC 2025  mkrepro@mkrepro.NetBSD.org:/usr/src/sys/arch/riscv/compile/GENERIC64 riscv
riscv64# sysctl kern.ostype kern.osrelease kern.version
kern.ostype = NetBSD
kern.osrelease = 10.99.14
kern.version = NetBSD 10.99.14 (GENERIC64) #0: Thu Jun 19 22:00:54 UTC 2025
        mkrepro@mkrepro.NetBSD.org:/usr/src/sys/arch/riscv/compile/GENERIC64

riscv64#
```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
