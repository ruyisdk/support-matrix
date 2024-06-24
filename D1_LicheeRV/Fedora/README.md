# Fedora 36 D1 Test Report

## Test Environment

### Operating System Information

- System Version: Fedora 36
- Download Link: [https://openkoji.iscas.ac.cn/pub/dl/riscv/Allwinner/Nezha_D1/images-release/Fedora/](https://openkoji.iscas.ac.cn/pub/dl/riscv/Allwinner/Nezha_D1/images-release/Fedora/)
- Reference Installation Document: [https://fedoraproject.org/wiki/Architectures/RISC-V/Allwinner/zh-cn](https://fedoraproject.org/wiki/Architectures/RISC-V/Allwinner/zh-cn)

### Hardware Information

- AWOL Nezha D1 / Sipeed Lichee RV Dock
- Power Adapter
- A microSD Card
- A USB to UART Debugger

## Installation Steps

### Flashing Image

Use `unzstd` to decompress the image.
Clear your sd card.
Use `dd` to flash the image to the microSD card.

```bash
unzstd /path/to/fedora.raw.zst
sudo wipefs -a /dev/your_device
sudo dd if=/path/to/fedora.raw of=/dev/your_device bs=1M status=progress
```

### Logging into the System

*System startup is relatively slow.*

Logging into to the system through the serial port.

Default Username: `root`
Default Password: `riscv`

## Expected Results

The system should boot normally and allow login via the onboard serial port.

## Actual Results

The system booted normally, successfully logged in via the onboard serial port, and was able to enter the desktop.

### Boot Log

Screen recording (flashing image):

[![asciicast](https://asciinema.org/a/yAMbaiYvBPLsyUPujOFey6zU3.svg)](https://asciinema.org/a/yAMbaiYvBPLsyUPujOFey6zU3)

Screen recording (system startup):

[![asciicast](https://asciinema.org/a/Evalgi6VgUvxs4gUmCtzC8n7j.svg)](https://asciinema.org/a/Evalgi6VgUvxs4gUmCtzC8n7j)

```log
Welcome to the Fedora RISC-V disk image
https://openkoji.iscas.ac.cn/koji/

Build date: Fri Jul 15 17:21:32 UTC 2022

Kernel 5.4.61 on an riscv64 (ttyS0)

The root password is 'riscv'.
root password logins are disabled in SSH starting Fedora.

If DNS isn’t working, try editing ‘/etc/yum.repos.d/fedora-riscv.repo’.

For updates and latest information read:
https://fedoraproject.org/wiki/Architectures/RISC-V

Fedora RISC-V
-------------
fedora-riscv login: root
Password: 
Last login: Sun Jul 17 00:20:39 on pts/0
[  194.914653] proc: Bad value for 'hidepid'
[root@fedora-riscv ~]# neofetch 
             .',;::::;,'.                                                                                                       
         .';:cccccccccccc:;,.            ----------------- 
      .;cccccccccccccccccccccc;.         OS: Fedora Linux 36 (Thirty Six) riscv64 
    .:cccccccccccccccccccccccccc:.       Host: sun20iw1p1 
  .;ccccccccccccc;.:dddl:.;ccccccc;.     Kernel: 5.4.61 
 .:ccccccccccccc;OWMKOOXMWd;ccccccc:.    Uptime: 3 mins 
.:ccccccccccccc;KMMc;cc;xMMc:ccccccc:.   Packages: 1546 (rpm) 
,cccccccccccccc;MMM.;cc;;WW::cccccccc,   Shell: bash 5.1.16 
:cccccccccccccc;MMM.;cccccccccccccccc:   Terminal: /dev/ttyS0 
:ccccccc;oxOOOo;MMM0OOk.;cccccccccccc:   CPU: (1) @ 1.008GHz 
cccccc:0MMKxdd:;MMMkddc.;cccccccccccc;   Memory: 313MiB / 1975MiB 
ccccc:XM0';cccc;MMM.;cccccccccccccccc'
ccccc;MMo;ccccc;MMW.;ccccccccccccccc;                            
ccccc;0MNc.ccc.xMMd:ccccccccccccccc;                             
cccccc;dNMWXXXWM0::cccccccccccccc:,
cccccccc;.:odl:.;cccccccccccccc:,.
:cccccccccccccccccccccccccccc:'.
.:cccccccccccccccccccccc:;,..
  '::cccccccccccccc::;,.

```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
