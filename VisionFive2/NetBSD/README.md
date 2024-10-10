---
sys: netbsd
sys_ver: 10.99.12
sys_var: null

status: basic
last_update: 2024-10-07
---

# NetBSD VisionFive 2 Test Report

## Test Environment

### System Information

- System Version: NetBSD-current
- Download Link: [riscv64.img.gz](https://nyftp.netbsd.org/pub/NetBSD-daily/HEAD/latest/riscv-riscv64/binary/gzimg/)
(The required dtb files are included in the image)

### Hardware Information

- StarFive VisionFive 2
- Power Adapter
- A microSD Card
- A USB to UART Debugger

## Installation Steps

### Flashing the Installation Image

Use `gzip` to decompress the image.
Use `dd` or `balenaEtcher` to flash the image to the microSD card.

```bash
sudo dd if=riscv64.img of=/dev/<your-device> bs=1M status=progress
```

### Booting the System

Insert the microSD card, connect the serial port, and use 1-bit QSPI Nor Flash mode (i.e. RGPIO_0 = 0, RGPIO_1 = 0) to boot.

Manually interrupt the u-boot process and input the boot command:

```bash
load mmc 1:1 ${fdt_addr_r} dtb/starfive/jh7110-starfive-visionfive-2-v1.3b.dtb
load mmc 1:1 ${kernel_addr_r} efi/boot/bootriscv64.efi
bootefi ${kernel_addr_r} ${fdt_addr_r}
```

Enter the auto install mode, reboot and re-enter the above startup commands if need to reboot.

### Persist Uboot

```bash
env default -a -f
setenv bootcmd "load mmc 1:1 ${fdt_addr_r} dtb/starfive/jh7110-starfive-visionfive-2-v1.3b.dtb; load mmc 1:1 ${kernel_addr_r} efi/boot/bootriscv64.efi; bootefi ${kernel_addr_r} ${fdt_addr_r}"
saveenv
```

### Logging into the System
Log into system as root,without password. 

## Expected Results

The system should boot normally and allow login via the onboard serial port.

## Actual Results

The system booted successfully and login via the onboard serial port was also successful.
But can't connect ethernet.

### Boot Log

```log
login: root
Oct  2 21:59:19 riscv64 login: ROOT LOGIN (root) on tty constty
Last login: Wed Oct  2 21:23:53 2024 on constty
Copyright (c) 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003,
    2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013,
    2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023,
    2024
    The NetBSD Foundation, Inc.  All rights reserved.
Copyright (c) 1982, 1986, 1989, 1991, 1993
    The Regents of the University of California.  All rights reserved.

NetBSD 10.99.12 (GENERIC64) #0: Wed Oct  2 21:21:26 UTC 2024

Welcome to NetBSD!

This is a development snapshot of NetBSD for testing -- user beware!

Bug reports: https://www.NetBSD.org/support/send-pr.html
Donations to the NetBSD Foundation: https://www.NetBSD.org/donations/
-- UNSAFE KEYS WARNING:

        The ssh host keys on this machine have been generated with
        not enough entropy configured, so they may be predictable.

        To fix, follow the "Adding entropy" section in the entropy(7)
        man page.  After this machine has enough entropy, re-generate
        the ssh host keys by running:

                /etc/rc.d/sshd keyregen
We recommend that you create a non-root account and use su(1) for root access.
riscv64# uname -a
NetBSD riscv64 10.99.12 NetBSD 10.99.12 (GENERIC64) #0: Wed Oct  2 21:21:26 UTC 2024  mkrepro@mkrepro.NetBSD.org:/usr/src/sys/arch/riscv/compile/GENERIC64 riscv
riscv64# sysctl kern.ostype kern.osrelease kern.version
kern.ostype = NetBSD
kern.osrelease = 10.99.12
kern.version = NetBSD 10.99.12 (GENERIC64) #0: Wed Oct  2 21:21:26 UTC 2024
        mkrepro@mkrepro.NetBSD.org:/usr/src/sys/arch/riscv/compile/GENERIC64

```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
