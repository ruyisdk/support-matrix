# RevyOS Sipeed Manufacturer Image Lichee Cluster 4A Test Report

## Test Environment

### System Information

- System Version: RevyOS 20230614-183009
- Download Link: [Lichee Cluster 4A Firmware](https://dl.sipeed.com/shareURL/LICHEE/LicheeCluster4A/04_Firmware/lpi4a/bin)
- Reference Installation Document: [Installation Guide](https://wiki.sipeed.com/hardware/zh/lichee/th1520/lc4a/lc4a.html)

### Hardware Information

- Lichee Cluster 4A 8G / 16G
- DC 12V Power Supply
- USB-A to A
    - or LPi4A Dock
- Network and Ethernet Cable (Ensure connection to BMC instead of switch)

## Installation Steps

*The following steps are based on flashing the image to board number one in the cluster*

### Connect to Corresponding SOM

Use an A to A cable to connect to the SOM.

### Flashing Image

Use `unxz` to extract the image.

```bash
unxz -k boot-20230614-182922.ext4.xz rootfs-20230614-183009.ext4.xz
```

Use `fastboot` to flash the image.
```bash
sudo ./fastboot flash ram u-boot-with-spl-lpi4a.bin
sudo ./fastboot reboot
sudo ./fastboot flash uboot u-boot-with-spl-lpi4a.bin
sudo ./fastboot flash boot boot-20230614-182922.ext4
sudo ./fastboot flash root rootfs-20230614-183009.ext4
```

### Logging into the System

Logging into the System via SOL (Serial Over LAN).

BMC Default Username: `root`

BMC Default Password: `0penBmc` **Note that it is `0` not `O`**

Connect via `ssh -p 2301 root@lichee-rv.local`

Default Username: `debian`
Default Password: `debian`

## Expected Results

The system starts up correctly, and you can log in via SOL (Serial Over LAN).

## Actual Results

The system starts up correctly, and you can log in via SOL (Serial Over LAN).

### Boot Log

Screen recording (from flashing the system to startup):

[![asciicast](https://asciinema.org/a/KwCIHjcPOuepxFiwUGhh7sLuh.svg)](https://asciinema.org/a/KwCIHjcPOuepxFiwUGhh7sLuh)

```log
Debian GNU/Linux 12 lc4aa0c8 ttyS0

lc4aa0c8 login: debian
Password: 
Linux lc4aa0c8 5.10.113-cluster #1 SMP PREEMPT 1 riscv64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Tue Apr  9 05:31:05 UTC 2024 on ttyS0
debian@lc4aa0c8:~$ uname -a
Linux lc4aa0c8 5.10.113-cluster #1 SMP PREEMPT 1 riscv64 GNU/Linux
debian@lc4aa0c8:~$ cat /etc/os-release 
PRETTY_NAME="Debian GNU/Linux 12 (bookworm)"
NAME="Debian GNU/Linux"
VERSION_ID="12"
VERSION="12 (bookworm)"
VERSION_CODENAME=bookworm
ID=debian
HOME_URL="https://www.debian.org/"
SUPPORT_URL="https://www.debian.org/support"
BUG_REPORT_URL="https://bugs.debian.org/"
debian@lc4aa0c8:~$ cat /etc/revyos-release 
20230614-183009
debian@lc4aa0c8:~$ 

```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
