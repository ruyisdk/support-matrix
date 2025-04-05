---
sys: revyos
sys_ver: 20250123
sys_var: null

status: good
last_update: 2025-03-04
---

# RevyOS LPi4A Test Report

## Test Environment

### System Information

- System Version: RevyOS 20250123
- Download Link: [Nginx Directory](https://mirror.iscas.ac.cn/revyos/extra/images/lpi4a/20250123/)
- Reference Installation Document: [Visit here](https://revyos.github.io/docs/)

### Hardware Information

- Lichee Pi 4A (16GB RAM + 128GB eMMC)
- USB-C Power Adapter / DC Power Supply
- USB-UART Debugger

## Installation Steps

### Download and decompress image

Download the image, use `zstd` to decompress the image:

```shell
wget https://mirror.iscas.ac.cn/revyos/extra/images/lpi4a/20250123/u-boot-with-spl-lpi4a-16g-main.bin
wget https://mirror.iscas.ac.cn/revyos/extra/images/lpi4a/20250123/boot-lpi4a-20250123_195216.ext4.zst
wget https://mirror.iscas.ac.cn/revyos/extra/images/lpi4a/20250123/root-lpi4a-20250123_195216.ext4.zst
zstd -d boot-lpi4a-20250123_195216.ext4.zst
zstd -d root-lpi4a-20250123_195216.ext4.zst
```

### Flash to onboard eMMC via `fastboot`

#### Use boot button to enter fastboot mode

Hold the **BOOT** button, then connect the USB-C cable (to your PC on the other side) to enter USB burning mode.

Use the following commands to flash the image.

```shell
sudo fastboot devices
sudo fastboot flash ram u-boot-with-spl-lpi4a-16g-main.bin
sudo fastboot reboot
sudo fastboot flash uboot u-boot-with-spl-lpi4a-16g-main.bin
sudo fastboot flash boot boot-lpi4a-20250123_195216.ext4.zst
sudo fastboot flash root root-lpi4a-20250123_195216.ext4.zst
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

[![asciicast](https://asciinema.org/a/aG83MyK1jsHqWPD234Trl1GEp.svg)](https://asciinema.org/a/aG83MyK1jsHqWPD234Trl1GEp)

![A](A.jpg)

```log
   ____              _ ____  ____  _  __
  |  _ \ _   _ _   _(_) ___||  _ \| |/ /
  | |_) | | | | | | | \___ \| | | | ' / 
  |  _ <| |_| | |_| | |___) | |_| | . \ 
  |_| \_\\__,_|\__, |_|____/|____/|_|\_\
               |___/                    
                   -- Presented by ISCAS

  Debian GNU/Linux trixie/sid (kernel 6.6.73-th1520)

Linux revyos-lpi4a 6.6.73-th1520 #2025.01.22.09.36+39bfa82ff SMP Wed Jan 22 09:5
3:08 UTC 2025 riscv64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
[  131.605585] audit: type=1130 audit(1725224710.340:157): pid=1 uid=0 auid=4294
967295 ses=4294967295 subj=unconfined msg='unit=user-runtime-dir@1000 comm="syst
emd" exe="/usr/lib/systemd/systemd" hostname=? addr=? terminal=? res=success'
[  131.661424] audit: type=1101 audit(1725224710.396:158): pid=3275 uid=0 auid=4
294967295 ses=4294967295 subj=unconfined msg='op=PAM:accounting grantors=pam_per
mit acct="debian" exe="/usr/lib/systemd/systemd-executor" hostname=? addr=? term
inal=? res=success'
[  131.685342] audit: type=1103 audit(1725224710.396:159): pid=3275 uid=0 auid=4
294967295 ses=4294967295 subj=unconfined msg='op=PAM:setcred grantors=pam_permit
 acct="debian" exe="/usr/lib/systemd/systemd-executor" hostname=? addr=? termina
l=? res=success'                                     
[  131.707886] audit: type=1006 audit(1725224710.396:160): pid=3275 uid=0 subj=u
nconfined old-auid=4294967295 auid=1000 tty=(none) old-ses=4294967295 ses=3 res=
1
[  131.722134] audit: type=1300 audit(1725224710.396:160): arch=c00000f3 syscall
=64 success=yes exit=4 a0=7 a1=3fe1cc2a70 a2=4 a3=0 items=0 ppid=1 pid=3275 auid
=1000 uid=0 gid=0 euid=0 suid=0 fsuid=0 egid=0 sgid=0 fsgid=0 tty=(none) ses=3 c
omm="(systemd)" exe="/usr/lib/systemd/systemd-executor" subj=unconfined key=(nul
l)
debian@revyos-lpi4a:~$ 
```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.