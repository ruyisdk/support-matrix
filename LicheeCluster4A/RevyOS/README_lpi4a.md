# RevyOS Lichee Cluster 4A Version Testing Report

## Test Environment

### System Information

- System Version: RevyOS
- Reference Installation Document: [https://revyos.github.io/](https://revyos.github.io/)

### Hardware Information

- Lichee Cluster 4A 8G / 16G
- DC 12V Power Supply
- USB-A to A
    - or LPi4A Dock
- Network and Ethernet Cable (make sure to connect to BMC instead of a switch)

## Installation Steps

*The following steps are based on flashing to the first board in the cluster*

### Connect to the Corresponding SOM

Use an A to A cable to connect to the SOM.

### Use the `ruyi` CLI to Flash the Image to the Onboard eMMC

Install the [`ruyi`](https://github.com/ruyisdk/ruyi) package manager, run `ruyi device provision`, and follow the prompts.

Select the image according to LPi4A.

### Logging into the System

Logging into the System using SOL (Serial Over LAN).

BMC default username: `root`

BMC default password: `0penBmc`  **Note that it is `0` not `O`**

Connect via `ssh -p 2301 root@lichee-rv.local`

Default username: `debian`
Default password: `debian`

### Common Issues

If USB is not working, it may require a Linux device tree patch. You can download the [patch here](https://dl.sipeed.com/fileList/LICHEE/LicheeCluster4A/04_Firmware/lpi4a/src/linux/0001-arch-riscv-boot-dts-lpi4a-disable-i2c-io-expander-fo.patch).

If you prefer not to compile the dtb manually, you can extract the dtb (light-lpi4a.dtb) from the [precompiled image](https://dl.sipeed.com/shareURL/LICHEE/LicheeCluster4A/04_Firmware/lpi4a/bin) and replace the corresponding file in the boot directory.

## Expected Results

The system should boot up correctly, and you should be able to log in through SOL (Serial Over LAN).

## Actual Results

The system boots up correctly, and you can log in through SOL (Serial Over LAN).

### Boot Log

Screen recording (from flashing the system to startup):

[![asciicast](https://asciinema.org/a/G0poBmxPbBjIfpVOC1PW2xh9y.svg)](https://asciinema.org/a/G0poBmxPbBjIfpVOC1PW2xh9y)

```log
Debian GNU/Linux 12 lpi4a ttyS0

lpi4a login: 
lpi4a login: debian

Password: 

   ____              _ ____  ____  _  __
  |  _ \ _   _ _   _(_) ___||  _ \| |/ /
  | |_) | | | | | | | \___ \| | | | ' / 
  |  _ <| |_| | |_| | |___) | |_| | . \ 
  |_| \_\\__,_|\__, |_|____/|____/|_|\_\
               |___/                    
                   -- Presented by ISCAS

  Debian GNU/Linux 12 (bookworm) (kernel 5.10.113-lpi4a)

Linux lpi4a 5.10.113-lpi4a #2023.12.08.03.26+b8c5d3546 SMP PREEMPT Fri Dec 8 03:26:13 UTC 2 riscv64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Tue Feb 28 19:16:04 CST 2023 on ttyS0
debian@lpi4a:~$
debian@lpi4a:~$ uname -a
Linux lpi4a 5.10.113-lpi4a #2023.12.08.03.26+b8c5d3546 SMP PREEMPT Fri Dec 8 03:26:13 UTC 2 riscv64 GNU/Linux
debian@lpi4a:~$ cat /etc/os-release 
PRETTY_NAME="Debian GNU/Linux 12 (bookworm)"
NAME="Debian GNU/Linux"
VERSION_ID="12"
VERSION="12 (bookworm)"
VERSION_CODENAME=bookworm
ID=debian
HOME_URL="https://www.debian.org/"
SUPPORT_URL="https://www.debian.org/support"
BUG_REPORT_URL="https://bugs.debian.org/"
debian@lpi4a:~$ 

```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
