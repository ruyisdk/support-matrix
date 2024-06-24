# Report on RevyOS Lichee Cluster 4A Version Testing

## Test Environment

### System Information

- System Version: RevyOS (with mainline kernel)
- Download Links
  - System Image: [root-lpi4amain-20240127_105111.ext4.zst](https://mirror.iscas.ac.cn/revyos/extra/images/lpi4amain/20240127/root-lpi4amain-20240127_105111.ext4.zst)
  - Boot Image: [boot-lpi4amain-20240127_105111.ext4.zst](https://mirror.iscas.ac.cn/revyos/extra/images/lpi4amain/20240127/boot-lpi4amain-20240127_105111.ext4.zst)
  - U-Boot Image (8G RAM): [u-boot-with-spl-lc4a-main.bin](https://mirror.iscas.ac.cn/revyos/extra/images/lpi4amain/20240127/u-boot-with-spl-lc4a-main.bin)
  - U-Boot Image (16G RAM): [u-boot-with-spl-lc4a-16g-main.bin](https://mirror.iscas.ac.cn/revyos/extra/images/lpi4amain/20240127/u-boot-with-spl-lc4a-16g-main.bin)
- Reference Installation Document: https://revyos.github.io/

### Hardware Information

- Lichee Cluster 4A 8G / 16G
- DC 12V Power Supply
- USB-A to A
    - or LPi4A Dock
- Network and Ethernet Cable (connect to BMC, not a switch)

## Installation Steps

*The following steps are based on flashing to the first board in the cluster*

### Connect to the Corresponding SOM

Connect SOM using an A to A cable.

### Flash Image

Use `zstd` to decompress the image.

```bash
zstd -d boot-lpi4amain-20240127_105111.ext4.zst
zstd -d root-lpi4amain-20240127_105111.ext4.zst
```

Use `fastboot` to flash the image
```bash
sudo ./fastboot flash ram u-boot-with-spl-lc4a-main.bin
sudo ./fastboot reboot
sudo ./fastboot flash uboot u-boot-with-spl-lc4a-main.bin
sudo ./fastboot flash boot boot-lpi4amain-20240127_105111.ext4
sudo ./fastboot flash root root-lpi4amain-20240127_105111.ext4
```

### Logging into the System

Logging into the system via SOL (Serial Over LAN).

Default BMC username: `root`

Default BMC password: `0penBmc`  **Note: `0`, not `O`**

Connect using `ssh -p 2301 root@lichee-rv.local`

Default username: `debian`
Default password: `debian`

## Expected Results

The system boots up normally and can be accessed through SOL (Serial Over LAN).

## Actual Results

The system boots up normally and can be accessed through SOL (Serial Over LAN).

### Boot Log

Screen recording (from flashing the system to startup):

[![asciicast](https://asciinema.org/a/TVYy7DGHQR3O71I9BGJL0bECY.svg)](https://asciinema.org/a/TVYy7DGHQR3O71I9BGJL0bECY)

```log
Debian GNU/Linux 12 lpi4amain ttyS0

lpi4amain login: [   25.687999] platform aon:soc_lcd0_vdd18_en: deferred probe pending
[   25.694254] platform aon:soc_avdd28_rgb: deferred probe pending
[   25.700242] platform aon:soc_dovdd18_rgb: deferred probe pending
[   25.706303] platform aon:soc_avdd25_ir: deferred probe pending
[   25.712189] platform aon:soc_dovdd18_ir: deferred probe pending
[   25.718180] platform aon:soc_dvdd12_ir: deferred probe pending
[   25.724063] platform aon:soc_cam2_avdd25_ir: deferred probe pending
[   25.730376] platform aon:soc_cam2_dvdd12_ir: deferred probe pending
[   25.736694] platform aon:soc_cam2_dovdd18_ir: deferred probe pending
[   25.743102] platform aon:soc_dvdd12_rgb: deferred probe pending
[   25.749071] platform aon:soc_lcd0_vdd33_en: deferred probe pending
         Starting ssh.service - OpenBSD Secure Shell server...
[  OK  ] Started ssh.service - OpenBSD Secure Shell server.
[FAILED] Failed to listen on ssh.so…penBSD Secure Shell server socket.
See 'systemctl status ssh.socket' for details.
[  OK  ] Finished firstboot.service - FirstBoot.
[  OK  ] Reached target multi-user.target - Multi-User System.
[  OK  ] Reached target graphical.target - Graphical Interface.
         Starting systemd-update-ut… Record Runlevel Change in UTMP...
[  OK  ] Finished systemd-update-ut… - Record Runlevel Change in UTMP.

lpi4amain login: [   40.022409] soc_dovdd18_scan: disabling
[   40.026957] soc_dvdd12_scan: disabling
[   40.031410] soc_avdd28_scan_en: disabling

lpi4amain login: debian
Password: 

   ____              _ ____  ____  _  __
  |  _ \ _   _ _   _(_) ___||  _ \| |/ /
  | |_) | | | | | | | \___ \| | | | ' / 
  |  _ <| |_| | |_| | |___) | |_| | . \ 
  |_| \_\\__,_|\__, |_|____/|____/|_|\_\
               |___/                    
                   -- Presented by ISCAS

  Debian GNU/Linux 12 (bookworm) (kernel 6.7.1-lpi4a)

Linux lpi4amain 6.7.1-lpi4a #1 SMP Mon Jan 22 16:37:48 UTC 2024 riscv64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
debian@lpi4amain:~$ uname -a
Linux lpi4amain 6.7.1-lpi4a #1 SMP Mon Jan 22 16:37:48 UTC 2024 riscv64 GNU/Linux
debian@lpi4amain:~$ cat /etc/os-release 
PRETTY_NAME="Debian GNU/Linux 12 (bookworm)"
NAME="Debian GNU/Linux"
VERSION_ID="12"
VERSION="12 (bookworm)"
VERSION_CODENAME=bookworm
ID=debian
HOME_URL="https://www.debian.org/"
SUPPORT_URL="https://www.debian.org/support"
BUG_REPORT_URL="https://bugs.debian.org/"
debian@lpi4amain:~$ 

```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
