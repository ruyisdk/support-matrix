---
sys: ubuntu
sys_ver: 25.04
sys_var: null

status: basic
last_update: 2025-04-19
---

# Ubuntu 25.04 VisionFive 2 Version Test Report

## Test Environment

### Operating System Information

- System Version: Ubuntu 25.04
- Download Link: https://ubuntu.com/download/risc-v
- Reference Installation Document: https://wiki.ubuntu.com/RISC-V/StarFive%20VisionFive%202

### Hardware Information

- StarFive VisionFive 2
- A USB power adapter
- A USB-A to C or C to C cable
- A microSD card
- A USB to UART debugger (e.g., CH340, CH341, FT2232, etc.)
- Three Dupont wires

## Installation Steps

### Decompress and Flash Image to microSD Card

```bash
xzcat ubuntu-25.04-preinstalled-server-riscv64+jh7110.img.xz | sudo dd bs=1M conv=fsync of=/dev/<your-device>
```

### Boot Mode Selection

The StarFive VisionFive 2 offers multiple boot modes, configurable via onboard dip switches prior to powering on. Refer to the StarFive [official documentation](https://doc.rvspace.org/VisionFive2/Quick_Start_Guide/VisionFive2_SDK_QSG/boot_mode_settings.html).

The board also has silk-screen labels for guidance.

To boot the Ubuntu image, select the SDIO3.0 mode (i.e., `RGPIO_0 = 1`, `RGPIO_1 = 0`).

### First boot

Insert the SD card and power on the board.Enter the U-Boot console by pressing enter when seeing the "Hit any key to stop autoboot:" message to reset the environment:

```
env default -f -a
env save
```

Power cycle the board. When booting the first time wait until you see an output line confirming that cloud-init has finished. Cloud init is responsible for generating the SSH keys and setting the default password. The line to wait for will look similar to
``` log
[   42.864196] cloud-init[648]: Cloud-init v. 24.4~3+really24.3.1-0ubuntu4 finished at Fri, 04 Oct 2024 15:38:08 +0000. Datasource DataSourceNoCloud [seed=/var/lib/cloud/seed/nocloud-net].  Up 42.85 seconds
```

### Logging into the System

Login to the system via the serial port.

Default username: `ubuntu`
Default password: `ubuntu`

Upon first login, you will be prompted to change the default password.

## Expected Results

The system should boot normally and allow login via the serial port.

## Actual Results

The system booted normally, and login via the serial port was successful.

### Boot log

```log
ubuntu login: ubuntu
Password:
You are required to change your password immediately (administrator enforced).
Changing password for ubuntu.
Current password:
New password:
Retype new password:
Welcome to Ubuntu 25.04 (GNU/Linux 6.14.0-13-generic riscv64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/pro

 System information as of Tue Apr 15 02:59:18 UTC 2025

  System load:    1.02      Processes:             27
  Usage of /home: unknown   Users logged in:       0
  Memory usage:   2%        IPv4 address for eth0: 10.10.10.2
  Swap usage:     0%

0 updates can be applied immediately.



The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

To run a command as administrator (user "root"), use "sudo <command>".
See "man sudo_root" for details.

ubuntu@ubuntu:~$ uname -a
Linux ubuntu 6.14.0-13-generic #13.2-Ubuntu SMP PREEMPT_DYNAMIC Sun Apr  6 05:26:54 UTC 2025 riscv64 riscv64 riscv64 GNU/Linux
ubuntu@ubuntu:~$ lscpu
Architecture:             riscv64
  Byte Order:             Little Endian
CPU(s):                   4
  On-line CPU(s) list:    0-3
Vendor ID:                0x489
  Model name:             sifive,u74-mc
    CPU family:           0x8000000000000007
    Model:                0x4210427
    Thread(s) per core:   1
    Core(s) per socket:   4
    Socket(s):            1
    CPU(s) scaling MHz:   100%
    CPU max MHz:          1500.0000
    CPU min MHz:          375.0000
Caches (sum of all):
  L1d:                    128 KiB (4 instances)
  L1i:                    128 KiB (4 instances)
  L2:                     2 MiB (1 instance)
NUMA:
  NUMA node(s):           1
  NUMA node0 CPU(s):      0-3
Vulnerabilities:
  Gather data sampling:   Not affected
  Ghostwrite:             Not affected
  Itlb multihit:          Not affected
  L1tf:                   Not affected
  Mds:                    Not affected
  Meltdown:               Not affected
  Mmio stale data:        Not affected
  Reg file data sampling: Not affected
  Retbleed:               Not affected
  Spec rstack overflow:   Not affected
  Spec store bypass:      Not affected
  Spectre v1:             Not affected
  Spectre v2:             Not affected
  Srbds:                  Not affected
  Tsx async abort:        Not affected
ubuntu@ubuntu:~$ cat /proc/cpuinfo
processor       : 0
hart            : 4
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd_zba_zbb
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x4210427
hart isa        : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd_zba_zbb

processor       : 1
hart            : 1
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd_zba_zbb
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x4210427
hart isa        : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd_zba_zbb

processor       : 2
hart            : 2
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd_zba_zbb
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x4210427
hart isa        : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd_zba_zbb

processor       : 3
hart            : 3
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd_zba_zbb
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x4210427
hart isa        : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd_zba_zbb

ubuntu@ubuntu:~$

```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
