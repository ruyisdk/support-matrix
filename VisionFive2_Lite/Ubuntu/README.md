---
sys: ubuntu
sys_ver: "24.04.5"
sys_var: null

status: basic
last_update: 2026-10-26
---

# Ubuntu 24.04.5 Test Report for VisionFive 2 Lite

## Test Environment

### Operating System Information

- OS version: Ubuntu 24.04.5 LTS
- System image: `ubuntu-24.04.5-preinstalled-server-riscv64+jh7110.img.xz`
- Download link: [Download Canonical-built Ubuntu for RISC-V Platforms | Ubuntu](https://ubuntu.com/download/risc-v/canonical-built#starfive-visionfive-2-lite)
- Reference installation document: https://canonical-ubuntu-boards.readthedocs-hosted.com/en/latest/how-to/starfive-visionfive-2/

### Hardware Information

- StarFive VisionFive 2 Lite
- Type-C power adapter
- Type-C data cable
- USB-to-TTL serial adapter
- Three Dupont wires

## Installation Steps

### Extract the System Image

Download the system image:

```
ubuntu-24.04.5-preinstalled-server-riscv64+jh7110.img.xz
```

Extract the corresponding `.img` file for flashing to eMMC.

### Connect the Serial Console and Enter Fastboot

Download and extract SFFB Tool:

```
https://files.waveshare.net/wiki/VisionFive2/SFFB_Tool_V1.0.7z
```

Prepare Tera Term as the serial terminal.

Connect the USB-to-TTL serial adapter to the corresponding serial pins on the VisionFive 2 Lite 40-pin header.

Board pins:

```
GND    TX    RX
```

Connect them to the following pins on the serial adapter, respectively:

```
GND    RX    TX
```

Connect the serial adapter to a USB port on the host computer, open Tera Term, and set the baud rate to:

```
115200
```

Power on the board and press any key in the serial terminal to interrupt autoboot and enter the U-Boot command line.

Run:

```
fastboot usb 0
```

The board enters Fastboot mode.

### Install the Driver and Flash the Image

Open Windows Device Manager and confirm that the following device appears:

```
USB Download Gadget
```

Select:

```
Update driver
→ Browse my computer for drivers
```

Select the following driver directory:

```
SFFB_Tool_V1.0\usb_driver
```

Complete the driver installation.

Open SFFB Tool, select the extracted system image, and click:

```
Start All
```

Or select:

```
Action → Run
```

Flashing begins.

Wait for the image transfer to complete, then power off the board.

### First Boot

Power on the VisionFive 2 Lite again, monitor the boot process through the serial console, and wait for the Ubuntu login prompt.

### Log In to the System

Log in through the serial console.

Default username:

```
ubuntu
```

Initial password:

```
ubuntu
```

At the first login, the system requires you to change the initial password. Follow the prompts to set your own new password.

## Expected Results

The system boots normally and allows login through the serial console.

## Actual Results

The system booted normally, and login through the serial console was successful.

### Boot Log

```
Ubuntu 24.04.5 LTS ubuntu ttyS0 

ubuntu login: ubuntu                                                            
Password:                           
Welcome to Ubuntu 24.04.5 LTS (GNU/Linux 7.0.0-31-generic riscv64)              
                                                                                
 * Documentation:  https://help.ubuntu.com                                      
 * Management:     https://landscape.canonical.com                              
 * Support:        https://ubuntu.com/pro                                       
                                                                                
 System information as of Tue Sep  8 03:00:04 UTC 2026                          
                                                                                
  System load:    1.04      Processes:             21                           
  Usage of /home: unknown   Users logged in:       0                            
  Memory usage:   3%        IPv4 address for eth0: 10.10.10.2                   
  Swap usage:     0%                                                            
                                                                                
Expanded Security Maintenance for Applications is not enabled.                  
                                                                                
0 updates can be applied immediately.                                           
                                                                                
Enable ESM Apps to receive additional future security updates.                  
See https://ubuntu.com/esm or run: sudo pro status                              
                                                                                
                                                                                
                                                                                
The programs included with the Ubuntu system are free software;                 
the exact distribution terms for each program are described in the              
individual files in /usr/share/doc/*/copyright.                                 
                                                                                
Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by            
applicable law.                                                                 
                                                                                
To run a command as administrator (user "root"), use "sudo <command>".          
See "man sudo_root" for details.                                                
                                                                                
ubuntu@ubuntu:~$ uname -a
Linux ubuntu 7.0.0-31-generic #31.1~24.04.1-Ubuntu SMP PREEMPT_DYNAMIC Tue Aug 25 15:43:59 UTC riscv64 riscv64 riscv64 GNU/Linux
ubuntu@ubuntu:~$ lscpu
Architecture:                riscv64
  Byte Order:                Little Endian
CPU(s):                      4
  On-line CPU(s) list:       0-3
NUMA:                        
  NUMA node(s):              1
  NUMA node0 CPU(s):         0-3
Vulnerabilities:             
  Gather data sampling:      Not affected
  Ghostwrite:                Not affected
  Indirect target selection: Not affected
  Itlb multihit:             Not affected
  L1tf:                      Not affected
  Mds:                       Not affected
  Meltdown:                  Not affected
  Mmio stale data:           Not affected
  Old microcode:             Not affected
  Reg file data sampling:    Not affected
  Retbleed:                  Not affected
  Spec rstack overflow:      Not affected
  Spec store bypass:         Not affected
  Spectre v1:                Not affected
  Spectre v2:                Not affected
  Srbds:                     Not affected
  Tsa:                       Not affected
  Tsx async abort:           Not affected
  Vmscape:                   Not affected
ubuntu@ubuntu:~$ cat /proc/cpuinfo
processor       : 0
hart            : 2
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zaamo_zalrsc_zca_zcd_zba_zbb
mmu             : sv39                                                                                                                                                                  uarchA Z for hel: sifive,u74-mc| NOR | Minicom 2.9 | VT102 | 脱机 | ttyUSB0                                                                                                             mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x4210427
hart isa        : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zaamo_zalrsc_zca_zcd_zba_zbb

processor       : 1
hart            : 1
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zaamo_zalrsc_zca_zcd_zba_zbb
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x4210427
hart isa        : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zaamo_zalrsc_zca_zcd_zba_zbb

processor       : 2
hart            : 3
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zaamo_zalrsc_zca_zcd_zba_zbb
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x4210427
hart isa        : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zaamo_zalrsc_zca_zcd_zba_zbb

processor       : 3
hart            : 4
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zaamo_zalrsc_zca_zcd_zba_zbb
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x4210427
hart isa        : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zaamo_zalrsc_zca_zcd_zba_zbb

ubuntu@ubuntu:~$ 
```

## Test Criteria

Test passed: The actual results match the expected results.

Test failed: The actual results do not match the expected results.

## Test Conclusion

Test passed.