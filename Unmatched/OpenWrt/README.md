# OpenWrt 23.05.2 HiFive Unmatched Test Report

## Test Environment

### Operating System Information

- System Version: OpenWrt 23.05.2
- Download Link (OpenWrt Firmware Selector): https://firmware-selector.openwrt.org/?version=23.05.2&target=sifiveu%2Fgeneric&id=sifive_unmatched
- Reference Installation Document: https://openwrt.org/docs/techref/hardware/soc/soc.sifive

> In OpenWrt Firmware Selector, you can customize the system image online, adding necessary pre-installed packages. For this test, we used an **unmodified** original image provided by the `ruyi` package manager.

### Hardware Information

- HiFive Unmatched Rev A
- A microUSB cable (included with HiFive Unmatched)
- An ATX power supply
- A microSD card (Sandisk Extreme Pro 64G UHS-I)

## Installation Steps

### Boot Device Selection

Ensure the DIP switch is set to boot from the microSD card. If you haven't changed it, the default factory setting is to boot from the microSD card.

The DIP switch should be set as follows: `MSEL[3:0]=1011`

### Using `ruyi` CLI to Flash the Image to the microSD Card

Install the [`ruyi`](https://github.com/ruyisdk/ruyi) package manager, run `ruyi device provision`, and follow the prompts.

### Logging into the System

Log into the system via the onboard serial port (using a microUSB cable to connect to another computer).

## Expected Results

The system should boot up normally, allowing login through the onboard serial port.

## Actual Results

The system booted successfully, and login through the onboard serial port was successful.

### Boot Log

```log
[    3.585478] init: - preinit -
[    4.187220] random: jshn: uninitialized urandom read (4 bytes read)
[    4.211546] random: jshn: uninitialized urandom read (4 bytes read)
[    4.227475] random: jshn: uninitialized urandom read (4 bytes read)
[    4.276587] macb 10090000.ethernet eth0: PHY [10090000.ethernet-ffffffff:00] driver [Generic PHY] (irq=POLL)
[    4.285668] macb 10090000.ethernet eth0: configuring for phy/gmii link mode
Press the [f] key and hit [enter] to enter failsafe mode
Press the [1], [2], [3] or [4] key and hit [enter] to select the debug level
[    6.372369] mount_root: mounting /dev/root
[    6.385001] EXT4-fs (mmcblk0p4): re-mounted. Opts: (null). Quota mode: disabled.
[    6.442366] urandom-seed: Seed file not found (/etc/urandom.seed)
[    6.496980] procd: - early -
[    7.136220] procd: - ubus -
[    7.169138] random: ubusd: uninitialized urandom read (4 bytes read)
[    7.187663] random: ubusd: uninitialized urandom read (4 bytes read)
[    7.193446] random: ubusd: uninitialized urandom read (4 bytes read)
[    7.200886] procd: - init -
Please press Enter to activate this console.
[    7.526267] kmodloader: loading kernel modules from /etc/modules.d/*
[    7.540236] i2c_dev: i2c /dev entries driver
[    7.609264] hwmon hwmon0: temp1_input not attached to any thermal zone
[    7.615055] hwmon hwmon0: temp2_input not attached to any thermal zone
[    7.956942] PPP generic driver version 2.4.2
[    7.961025] NET: Registered PF_PPPOX protocol family
[    7.969043] kmodloader: done loading kernel modules from /etc/modules.d/*
[    8.000916] urngd: v1.0.2 started.
[    8.187850] random: crng init done
[    8.190467] random: 24 urandom warning(s) missed due to ratelimiting
[   14.796276] macb 10090000.ethernet eth0: PHY [10090000.ethernet-ffffffff:00] driver [Generic PHY] (irq=POLL)
[   14.805440] macb 10090000.ethernet eth0: configuring for phy/gmii link mode
[   14.813676] br-lan: port 1(eth0) entered blocking state
[   14.818128] br-lan: port 1(eth0) entered disabled state
[   14.823658] device eth0 entered promiscuous mode



BusyBox v1.36.1 (2023-11-14 13:38:11 UTC) built-in shell (ash)

  _______                     ________        __
 |       |.-----.-----.-----.|  |  |  |.----.|  |_
 |   -   ||  _  |  -__|     ||  |  |  ||   _||   _|
 |_______||   __|_____|__|__||________||__|  |____|
          |__| W I R E L E S S   F R E E D O M
 -----------------------------------------------------
 OpenWrt 23.05.2, r23630-842932a63d
 -----------------------------------------------------
=== WARNING! =====================================
There is no root password defined on this device!
Use the "passwd" command to set up a new password
in order to prevent unauthorized SSH logins.
--------------------------------------------------
root@OpenWrt:/# cat /etc/o
odhcp6c.user     openwrt_release  opkg.conf        os-release
odhcp6c.user.d/  openwrt_version  opkg/
root@OpenWrt:/# cat /etc/os-release 
NAME="OpenWrt"
VERSION="23.05.2"
ID="openwrt"
ID_LIKE="lede openwrt"
PRETTY_NAME="OpenWrt 23.05.2"
VERSION_ID="23.05.2"
HOME_URL="https://openwrt.org/"
BUG_URL="https://bugs.openwrt.org/"
SUPPORT_URL="https://forum.openwrt.org/"
BUILD_ID="r23630-842932a63d"
OPENWRT_BOARD="sifiveu/generic"
OPENWRT_ARCH="riscv64_riscv64"
OPENWRT_TAINTS=""
OPENWRT_DEVICE_MANUFACTURER="OpenWrt"
OPENWRT_DEVICE_MANUFACTURER_URL="https://openwrt.org/"
OPENWRT_DEVICE_PRODUCT="Generic"
OPENWRT_DEVICE_REVISION="v0"
OPENWRT_RELEASE="OpenWrt 23.05.2 r23630-842932a63d"
root@OpenWrt:/# cat /proc/cpuinfo 
processor       : 0
hart            : 1
isa             : rv64imafdc
mmu             : sv39
uarch           : sifive,u74-mc
                                                                        
processor       : 1                                                       
hart            : 2                                                     
isa             : rv64imafdc                                            
mmu             : sv39
uarch           : sifive,u74-mc

processor       : 2
hart            : 3
isa             : rv64imafdc
mmu             : sv39
uarch           : sifive,u74-mc

processor       : 3
hart            : 4
isa             : rv64imafdc
mmu             : sv39
uarch           : sifive,u74-mc

root@OpenWrt:/#
```

Screen recording (From flashing the image to logging into the system):

[![asciicast](https://asciinema.org/a/cAMBxvAP8iqIrdf1xCiQ3clJP.svg)](https://asciinema.org/a/cAMBxvAP8iqIrdf1xCiQ3clJP)

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
