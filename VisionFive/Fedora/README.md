# Fedora 33 VisionFive Test Report

## Test Environment

### System Information

- System Version: Fedora 33
- Download Link: [https://fedora.starfivetech.com/pub/downloads/VisionFive-release/Fedora-riscv64-jh7100-developer-xfce-Rawhide-20211226-214100.n.0-sda.raw.zst](https://fedora.starfivetech.com/pub/downloads/VisionFive-release/Fedora-riscv64-jh7100-developer-xfce-Rawhide-20211226-214100.n.0-sda.raw.zst)
- Reference Installation Document: [https://doc.rvspace.org/VisionFive/PDF/VisionFive_Quick_Start_Guide.pdf](https://doc.rvspace.org/VisionFive/PDF/VisionFive_Quick_Start_Guide.pdf)

### Hardware Information

- StarFive VisionFive
- Power Adapter
- A microSD Card
- A USB to UART Debugger

## Installation Steps

### Flashing Image

Use `zstd` to decompress the image.
Use `dd` to flash the image to the microSD card.

```bash
zstd -d /path/to/fedora.raw.zst
sudo dd if=/path/to/fedora of=/dev/your-device bs=1M status=progress
```

### Logging into the System

Log into the system via the serial port.

Default Username: `root`
Default Password: `starfive`

## Expected Results

The system should boot normally and allow login via the onboard serial port.

## Actual Results

The system booted successfully and login via the onboard serial port was also successful.

### Boot Log

Screen recording (from flashing the image to logging into the system):

[![asciicast](https://asciinema.org/a/wuaUJ0h23U1eWMFzoyQPLTvgp.svg)](https://asciinema.org/a/wuaUJ0h23U1eWMFzoyQPLTvgp)

```log
Build date: Tue Nov 16 23:07:46 UTC 2021

Kernel 5.15.10+ on an riscv64 (ttyS0)

The root password is 'starfive'.
root password logins are disabled in SSH starting Fedora 31.
User 'riscv' with password 'starfive' in 'wheel' group is provided.

To install new packages use 'dnf install ...'

To upgrade disk image use 'dnf upgrade --best'

If DNS isn’t working, try editing ‘/etc/yum.repos.d/fedora-riscv.repo’.

For updates and latest information read:
https://fedoraproject.org/wiki/Architectures/RISC-V

Fedora/RISC-V
-------------
Koji:               http://fedora.riscv.rocks/koji/
SCM:                http://fedora.riscv.rocks:3000/
Distribution rep.:  http://fedora.riscv.rocks/repos-dist/
Koji internal rep.: http://fedora.riscv.rocks/repos/
fedora-starfive login: root
Password: 
[  103.100371] systemd-xdg-autostart-generator[741]: Not generating service for XDG autostart app-gnome\x2dkeyring\x2dssh-autos.
[  103.115950] systemd-xdg-autostart-generator[741]: Not generating service for XDG autostart app-gnome\x2dkeyring\x2dpkcs11-au.
[  103.131975] systemd-xdg-autostart-generator[741]: Not generating service for XDG autostart app-xdg\x2duser\x2ddirs-autostart.
[  103.147007] systemd-xdg-autostart-generator[741]: Not generating service for XDG autostart app-gnome\x2dkeyring\x2dsecrets-a.
[  103.162696] systemd-xdg-autostart-generator[741]: Not generating service for XDG autostart app-xapp\x2dsn\x2dwatcher-autosta.
[  103.177879] systemd-xdg-autostart-generator[741]: Not generating service for XDG autostart app-gsettings\x2ddata\x2dconvert-.
[  103.193926] systemd-xdg-autostart-generator[741]: Not generating service for XDG autostart app-at\x2dspi\x2ddbus\x2dbus-auto.
[  103.210809] systemd-xdg-autostart-generator[741]: gnome-systemd-autostart-condition not found: No such file or directory
Last login: Tue Dec 21 01:25:23 on pts/0
[root@fedora-starfive ~]# neofetch 
          /:-------------:\                                                                                                     
       :-------------------::        -------------------- 
     :-----------/shhOHbmp---:\      OS: Fedora 33 (Rawhide) riscv64 
   /-----------omMMMNNNMMD  ---:     Host: StarFive VisionFive V1 
  :-----------sMMMMNMNMP.    ---:    Kernel: 5.15.10+ 
 :-----------:MMMdP-------    ---\   Uptime: 1 min 
,------------:MMMd--------    ---:   Packages: 2359 (rpm) 
:------------:MMMd-------    .---:   Shell: bash 5.0.17 
:----    oNMMMMMMMMMNho     .----:   Terminal: /dev/ttyS0 
:--     .+shhhMMMmhhy++   .------/   CPU: (2) 
:-    -------:MMMd--------------:    Memory: 221MiB / 7174MiB 
:-   --------/MMMd-------------;
:-    ------/hMMMy------------:                              
:-- :dMNdhhdNMMNo------------;                               
:---:sdNMMMMNds:------------:
:------:://:-------------::
:---------------------://

[root@fedora-starfive ~]# 

```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
