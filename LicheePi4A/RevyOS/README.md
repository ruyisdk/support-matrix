---
sys: revyos
sys_ver: 20250110
sys_var: null

status: good
last_update: 2025-01-13
---

# RevyOS LPi4A Test Report

## Test Environment

### System Information

- System Version: RevyOS 20250110
- Download Link: [ISCAS mirror](https://mirror.iscas.ac.cn/revyos/extra/images/lpi4a/)
- Reference Installation Document: [Visit here](https://revyos.github.io/docs/)

### Hardware Information

- Lichee Pi 4A (16GB RAM + 128GB eMMC)
- USB-C Power Adapter / DC Power Supply
- USB-UART Debugger

## Installation Steps

### Download and decompress image

Download the image, use `zstd` to decompress the image:
```shell
wget https://mirror.iscas.ac.cn/revyos/extra/images/lpi4a/20250110/boot-lpi4a-20250110_151339.ext4.zst
wget https://mirror.iscas.ac.cn/revyos/extra/images/lpi4a/20250110/u-boot-with-spl-lpi4a-16g-main.bin
wget https://mirror.iscas.ac.cn/revyos/extra/images/lpi4a/20250110/root-lpi4a-20250110_151339.ext4.zst
zstd -d boot-lpi4a-20250110_151339.ext4.zst
zstd -d root-lpi4a-20250110_151339.ext4.zst
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
sudo fastboot flash ram u-boot-with-spl-lpi4a-16g-main.bin
sudo fastboot reboot
sudo fastboot flash uboot u-boot-with-spl-lpi4a-16g-main.bin
sudo fastboot flash boot boot-lpi4a-20250110_151339.ext4
sudo fastboot flash root root-lpi4a-20250110_151339.ext4
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

[![asciicast](https://asciinema.org/a/4kw9rznzmMGsEdD2lSqJOSm3h.svg)](https://asciinema.org/a/4kw9rznzmMGsEdD2lSqJOSm3h)

```log

   ____              _ ____  ____  _  __
  |  _ \ _   _ _   _(_) ___||  _ \| |/ /
  | |_) | | | | | | | \___ \| | | | ' / 
  |  _ <| |_| | |_| | |___) | |_| | . \ 
  |_| \_\\__,_|\__, |_|____/|____/|_|\_\
               |___/                    
                   -- Presented by ISCAS

  Debian GNU/Linux trixie/sid (kernel 6.6.66-th1520)

Linux revyos-lpi4a 6.6.66-th1520 #2025.01.10.02.53+1c6721ec2 SMP Fri Jan 10 03:09:24 UTC 2025 riscv64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Mon Sep  2 05:03:30 2024
debian@revyos-lpi4a:~$ uname -a
Linux revyos-lpi4a 6.6.66-th1520 #2025.01.10.02.5

debian@revyos-lpi4a:~$ 3+1c6721ec2 SMP Fri Jan 10 03:09:24 UTC 2025 riscv64 GNU/Linux
debian@revyos-lpi4a:~$ cat /etc/os-release 
PRETTY_NAME="Debian GNU/Linux trixie/sid"
NAME="Debian GNU/Linux"
VERSION_CODENAME=trixie
ID=debian
HOME_URL="https://www.debian.org/"
SUPPORT_URL="https://www.debian.org/support"
BUG_REPORT_URL="https://bugs.debian.org/"
debian@revyos-lpi4a:~$ cat /proc/cpuinfo 
processor       : 0
hart            : 0
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_xtheadvector
mmu             : sv39
uarch           : thead,c910
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 1
hart            : 1
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_xtheadvector
mmu             : sv39
uarch           : thead,c910
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

processor       : 2
hart            : 2
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_xtheadvector
mmu             : sv39
uarch           : thead,c910
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

debian@revyos-lpi4a:~$ 

processor       : 3
hart            : 3
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_xtheadvector
mmu             : sv39
uarch           : thead,c910
mvendorid       : 0x5b7
marchid         : 0x0
mimpid          : 0x0

debian@revyos-lpi4a:~$ neofetch
       _,met$$$$$gg.          debian@revyos-lpi4a 
    ,g$$$$$$$$$$$$$$$P.       ------------------- 
  ,g$$P"     """Y$$.".        OS: Debian GNU/Linux trixie/sid riscv64 
 ,$$P'              `$$$.     Host: Sipeed Lichee Pi 4A 16G 
',$$P       ,ggs.     `$$b:   Kernel: 6.6.66-th1520 
`d$$'     ,$P"'   .    $$$    Uptime: 7 mins 
 $$P      d$'     ,    $$P    Packages: 1223 (dpkg) 
 $$:      $$.   -    ,d$$'    Shell: bash 5.2.32 
 $$;      Y$b._   _,d$P'      Resolution: 3840x2160 
 Y$$.    `.`"Y$$$$P"'         Terminal: /dev/pts/0 
 `$$b      "-.__              CPU: (4) @ 1.848GHz 
  `Y$$                        Memory: 357MiB / 15814MiB 
   `Y$$.
     `$$b.                                            
       `Y$$b.                                         
          `"Y$b._
              `"""

debian@revyos-lpi4a:~$ 
```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
