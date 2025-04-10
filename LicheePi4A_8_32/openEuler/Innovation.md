---
sys: openeuler
sys_ver: "25.03"
sys_var: Innovation

status: good
last_update: 2025-04-09
---

# openEuler RISC-V 25.03 LPi4A Test Report

## Test Environment

### System Information

- System Version: openEuler 25.03
- Download Link: https://repo.openeuler.org/openEuler-25.03/embedded_img/riscv64/lpi4a/
- Reference Installation Document: https://docs.openeuler.org/en/docs/24.03_LTS/docs/Installation/RISC-V-LicheePi4A.html

### Hardware Information

- Lichee Pi 4A (8G RAM + 32G eMMC)
- USB-C Power Adapter / DC Power Supply
- A USB-UART Debugger

## Installation Steps

### Download and decompress image

```shell
zstd -d openEuler-25.03-riscv64-lpi4a-base-boot.ext4.zst
zstd -d openEuler-25.03-riscv64-lpi4a-base-root.ext4.zst
```

### Flash to onboard eMMC via `fastboot`

By default the USB VID/PID of LPi4A are't in the udev rules, you might need to use `sudo` while using `fastboot`.

Hold the **BOOT** button, then connect the USB-C cable (to your PC on the other side) to enter USB burning mode.

In Windows using device manager, you'll see a device named `USB download gadget`.

In Linux using `lsusb` you'll see a device like: `ID 2345:7654 T-HEAD USB download gadget`.

Use the following commands to flash the image.

```shell
sudo fastboot devices
sudo fastboot flash ram u-boot-with-spl-lpi4a.bin
sudo fastboot reboot
# Wait a few seconds until the board reboots and reconnects to your PC

sudo fastboot flash uboot u-boot-with-spl-lpi4a.bin
sudo fastboot flash boot openEuler-25.03-riscv64-lpi4a-base-boot.ext4
sudo fastboot flash root openEuler-25.03-riscv64-lpi4a-base-root.ext4
```

### Logging into the System

Logging into the system via serial console.

Default username: `openeuler` or `root`
Default password: `openEuler12#$`

## Expected Results

The system boots up successfully and allows login via the serial console.

## Actual Results

The system boots up without issues, and both serial console login is successful.

### Boot Log

```log
[  OK  ] Started Network Manager.
[  OK  ] Reached target Network.
         Starting Network Manager Wait Online...
         Starting GSSAPI Proxy Daemon...
         Starting /etc/rc.d/rc.local Compatibility...
         Starting OpenSSH server daemon...
         Starting Dynamic System Tuning Daemon...
[  OK  ] Started Locale Service.
[  OK  ] Started OpenSSH server daemon.
[  OK  ] Started GSSAPI Proxy Daemon.
[  OK  ] Started /etc/rc.d/rc.local Compatibility.
         Starting Authorization Manager...
[  OK  ] Reached target NFS client services.
[  OK  ] Reached target Preparation for Remote File Systems.
[  OK  ] Reached target Remote File Systems.
         Starting Permit User Sessions...
[  OK  ] Finished Permit User Sessions.
[  OK  ] Started Deferred execution scheduler.
[  OK  ] Started Command Scheduler.
         Starting Hold until boot process finishes up...
         Starting Terminate Plymouth Boot Screen...
[   28.403427][  T865] fbcon: Taking over console

openEuler 25.03
Kernel 6.6.0-72.6.0.56.oe2503.riscv64 on an riscv64

openeuler-riscv64 login: [   38.074226][  T293] soc_dovdd18_scan: disabling
[   38.078981][  T293] soc_dvdd12_scan: disabling
[   38.083649][  T293] soc_avdd28_scan_en: disabling

openeuler-riscv64 login: openeuler
Password:

Authorized users only. All activities may be monitored and reported.


Welcome to 6.6.0-72.6.0.56.oe2503.riscv64

System information as of time:  Thu Jan  1 08:01:06 AM CST 1970

System load:    1.27
Memory used:    2.3%
Swap used:      0%
Usage On:       9%
Users online:   1
To run a command as administrator(user "root"),use "sudo <command>".
[openeuler@openeuler-riscv64 ~]$ uname -a
Linux openeuler-riscv64 6.6.0-72.6.0.56.oe2503.riscv64 #1 SMP PREEMPT Wed Mar 26 18:19:48 CST 2025 riscv64 riscv64 riscv64 GNU/Linux
[root@openeuler-riscv64 ~]# cat /etc/os-release
NAME="openEuler"
VERSION="25.03"
ID="openEuler"
VERSION_ID="25.03"
PRETTY_NAME="openEuler 25.03"
ANSI_COLOR="0;31"
```

[![asciicast](https://asciinema.org/a/Nn4LhNaZh1dkBpYnvgF6rD3La.svg)](https://asciinema.org/a/Nn4LhNaZh1dkBpYnvgF6rD3La)

### Install Desktop Environment

We'll take the example of Xfce installation here:

```
sudo dnf update
sudo dnf install dejavu-fonts liberation-fonts gnu-*-fonts google-*-fonts
sudo dnf install xorg-*
sudo dnf install xfwm4 xfdesktop xfce4-* xfce4-*-plugin network-manager-applet *fonts
sudo dnf install lightdm lightdm-gtk
echo 'user-session=xfce' >> /etc/lightdm/lightdm.conf.d/60-lightdm-gtk-greeter.conf
```

Enable display manager and set default GUI login method

```
sudo systemctl start lightdm

sudo systemctl enable lightdm
sudo systemctl set-default graphical.target
```

![xfce](xfce.jpg)

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
