---
sys: revyos
sys_ver: 20240720
sys_var: null

status: good
last_update: 2024-10-25
---

# RevyOS LPi4A Test Report

## Test Environment

### System Information

- System Version: RevyOS 20240720
- Download Link: [ISCAS mirror](https://mirror.iscas.ac.cn/revyos/extra/images/lpi4a/)
- Reference Installation Document: [Visit here](https://revyos.github.io/docs/)

### Hardware Information

- Lichee Pi 4A (16GB RAM + 128GB eMMFAQC)
- USB-C Power Adapter / DC Power Supply
- USB-UART Debugger

## Installation Steps

### Download and decompress image

Download the image, use `zstd` to decompress the image:
```shell
wget https://mirror.iscas.ac.cn/revyos/extra/images/lpi4a/20240720/boot-lpi4a-20240720_171951.ext4.zst
wget https://mirror.iscas.ac.cn/revyos/extra/images/lpi4a/20240720/u-boot-with-spl-lpi4a.bin
wget https://mirror.iscas.ac.cn/revyos/extra/images/lpi4a/20240720/root-lpi4a-20240720_171951.ext4.zst
zstd -d boot-lpi4a-20240720_171951.ext4.zst
zstd -d root-lpi4a-20240720_171951.ext4.zst

```

### Flash to onboard eMMC via `fastboot`

There are two ways to enter fastboot mode:

#### Use boot button to enter fastboot mode

Hold the **BOOT** button, then connect the USB-C cable (to your PC on the other side) to enter USB burning mode.

#### Use u-boot to enter fastboot mode

After entering the u-boot console, interrupt it, and use the following commands to enter fastboot mode:
```shell
fastboot usb 0
```

---

In Linux using `lsusb` you'll see a device like: `ID 2345:7654 T-HEAD USB download gadget`.

Use the following commands to flash the image.

```shell
sudo fastboot devices
sudo fastboot flash ram u-boot-with-spl-lpi4a.bin 
sudo fastboot reboot
sudo fastboot flash uboot u-boot-with-spl-lpi4a.bin
sudo fastboot flash boot boot-lpi4a-20240720_171951.ext4
sudo fastboot flash root root-lpi4a-20240720_171951.ext4

```

### Logging into the System

Logging into the system via serial console or graphical interface.

Default username: `debian`
Default password: `debian`

## Expected Results

The system boots up successfully and can be accessed via the serial console.

## Actual Results

The system boots up successfully and login via the serial console is successful.

### Boot Log

Screen recording (from flashing image to logging into system):

[![asciicast](https://asciinema.org/a/GLrnMuapSQwQ1DufMCtaRYnkY.svg)](https://asciinema.org/a/GLrnMuapSQwQ1DufMCtaRYnkY)

```log
revyos-lpi4a login: debian
Password: 
[  300.207430] audit: type=1100 audit(1703432525.400:211): pid=589 uid=0 auid=4294967295 ses=4294967295 msg='op=PAM:authen'
[  300.229172] audit: type=1101 audit(1703432525.400:212): pid=589 uid=0 auid=4294967295 ses=4294967295 msg='op=PAM:accoun'
[  300.250545] audit: type=1006 audit(1703432525.400:213): pid=589 uid=0 old-auid=4294967295 auid=1000 tty=ttyS0 old-ses=41

   ____              _ ____  ____  _  __
  |  _ \ _   _ _   _(_) ___||  _ \| |/ /
  | |_) | | | | | | | \___ \| | | | ' / 
  |  _ <| |_| | |_| | |___) | |_| | . \ 
  |_| \_\\__,_|\__, |_|____/|____/|_|\_\
               |___/                    
                   -- Presented by ISCAS

  Debian GNU/Linux 12 (bookworm) (kernel 5.10.113-th1520)

Linux revyos-lpi4a 5.10.113-th1520 #2024.07.20.13.28+d8f77de53 SMP PREEMPT Sat Jul 20 13:29:42 UTC  riscv64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
[  300.586878] audit: type=1130 audit(1703432525.776:214): pid=1 uid=0 auid=4294967295 ses=4294967295 msg='unit=user-runti'
[  300.648819] audit: type=1101 audit(1703432525.840:215): pid=2082 uid=0 auid=4294967295 ses=4294967295 msg='op=PAM:accou'
[  300.669416] audit: type=1103 audit(1703432525.840:216): pid=2082 uid=0 auid=4294967295 ses=4294967295 msg='op=PAM:setcr'
[  300.689717] audit: type=1006 audit(1703432525.840:217): pid=2082 uid=0 old-auid=4294967295 auid=1000 tty=(none) old-ses1
[  300.806560] audit: type=1105 audit(1703432525.996:218): pid=2082 uid=0 auid=1000 ses=3 msg='op=PAM:session_open grantor'
[  300.850013] audit: type=1334 audit(1703432526.040:219): prog-id=64 op=LOAD
[  300.856980] audit: type=1334 audit(1703432526.040:220): prog-id=64 op=UNLOAD
debian@revyos-lpi4a:~$ cat /etc/os-release 
PRETTY_NAME="Debian GNU/Linux 12 (bookworm)"
NAME="Debian GNU/Linux"
VERSION_ID="12"
VERSION="12 (bookworm)"
VERSION_CODENAME=bookworm
ID=debian
HOME_URL="https://www.debian.org/"
SUPPORT_URL="https://www.debian.org/support"
BUG_REPORT_URL="https://bugs.debian.org/"
debian@revyos-lpi4a:~$ uname -a
Linux revyos-lpi4a 5.10.113-th1520 #2024.07.20.13.28+d8f77de53 SMP PREEMPT Sat Jul 20 13:29:42 UTC  riscv64 GNU/Linux
debian@revyos-lpi4a:~$ cat /proc/cpuinfo 
processor       : 0
hart            : 0
isa             : rv64imafdcvsu
mmu             : sv39
cpu-freq        : 1.848Ghz
cpu-icache      : 64KB
cpu-dcache      : 64KB
cpu-l2cache     : 1MB
cpu-tlb         : 1024 4-ways
cpu-cacheline   : 64Bytes
cpu-vector      : 0.7.1

processor       : 1
hart            : 1
isa             : rv64imafdcvsu
mmu             : sv39
cpu-freq        : 1.848Ghz
cpu-icache      : 64KB
cpu-dcache      : 64KB
cpu-l2cache     : 1MB
cpu-tlb         : 1024 4-ways
cpu-cacheline   : 64Bytes
cpu-vector      : 0.7.1

processor       : 2
hart            : 2
isa             : rv64imafdcvsu
mmu             : sv39
cpu-freq        : 1.848Ghz
cpu-icache      : 64KB
cpu-dcache      : 64KB
cpu-l2cache     : 1MB
cpu-tlb         : 1024 4-ways
cpu-cacheline   : 64Bytes
cpu-vector      : 0.7.1

processor       : 3
hart            : 3
isa             : rv64imafdcvsu
mmu             : sv39
cpu-freq        : 1.848Ghz
cpu-icache      : 64KB
cpu-dcache      : 64KB
cpu-l2cache     : 1MB
cpu-tlb         : 1024 4-ways
cpu-cacheline   : 64Bytes
cpu-vector      : 0.7.1

```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
