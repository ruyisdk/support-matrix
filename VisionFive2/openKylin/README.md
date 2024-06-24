# openKylin 1.0.1 VisionFive 2 Test Report

## Test Environment

### Operating System Information

- System Version: openKylin 1.0.1 
- Download Link: https://www.openkylin.top/downloads/index-cn.html 
- Reference Installation Document: https://docs.openkylin.top/zh/%E7%A4%BE%E5%8C%BA%E5%BC%80%E5%8F%91%E6%8C%87%E5%8D%97/riscv%E4%B8%8A%E5%AE%89%E8%A3%85openKylin

### Hardware Information

- StarFive VisionFive 2
- A USB Power Adapter
- A USB-A to C or C to C Cable
- A microSD Card
- A USB to UART Debugger (e.g., CH340, CH341, FT2232, etc.)
- Three Dupont Wires

## Installation Steps

### Unzipping and Flashing Image to microSD Card

Assume `/dev/sdc` is the storage card.

```bash
xz -d openKylin-1.0.1-visionfive2-riscv64.img.xz 
sudo dd if=openKylin-1.0.1-visionfive2-riscv64.img of=/dev/sdc bs=1M status=progress
```

### Boot Mode Selection

StarFive VisionFive 2 offers multiple boot modes, which can be configured via the onboard dip switch before powering on; the board itself has silkscreen labels.

To boot the openKylin image, select the 1-bit QSPI Nor Flash mode (i.e., `RGPIO_0 = 0`, `RGPIO_1 = 0`). Note that this mode may require updating the firmware within the Flash beforehand. If the boot fails, please refer to the official documentation for firmware upgrade instructions: [Updating SPL and U-Boot](https://doc.rvspace.org/VisionFive2/Quick_Start_Guide/VisionFive2_QSG/spl_u_boot_0.html)

### Logging into the System

Logging into the system via the serial port.

Default username: `openkylin` 
Default password: `openkylin$`

## Expected Results

The system should boot normally and allow login through the graphical interface.

## Actual Results

The system booted successfully and login through the graphical interface was successful.

### Boot Log

Screen recording (from flashing image to system login):

```log
openkylin@openkylin:~$ cat /proc/cpuinfo 
processor       : 0
hart            : 1
isa             : rv64imafdc
mmu             : sv39
isa-ext         : 
uarch           : sifive,u74-mc

processor       : 1
hart            : 2
isa             : rv64imafdc
mmu             : sv39
isa-ext         : 
uarch           : sifive,u74-mc

processor       : 2
hart            : 3
isa             : rv64imafdc
mmu             : sv39
isa-ext         : 
uarch           : sifive,u74-mc

processor       : 3
hart            : 4
isa             : rv64imafdc
mmu             : sv39
isa-ext         : 
uarch           : sifive,u74-mc

openkylin@openkylin:~$ uname -a
Linux openkylin 5.15.0 #1 SMP Fri Sep 1 11:22:00 CST 2023 riscv64 riscv64 riscv64 GNU/Linux
openkylin@openkylin:~$ cat /etc/os-release 
NAME="openKylin"
FULL_NAME="openKylin"
VERSION="1.0.1 (yangtze)"
VERSION_US="1.0.1 (yangtze)"
ID=openkylin
PRETTY_NAME="openKylin 1.0.1"
VERSION_ID="1.0.1"
HOME_URL="https://www.openkylin.top/"
VERSION_CODENAME=yangtze
PRODUCT_FEATURES=3
openkylin@openkylin:~$
```

Screen recording (from flashing to boot):

[![asciicast](https://asciinema.org/a/qoDqBWFEJlBPhIBva66HFGzd9.svg)](https://asciinema.org/a/qoDqBWFEJlBPhIBva66HFGzd9)
