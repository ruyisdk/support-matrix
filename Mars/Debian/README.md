---
sys: debian
sys_ver: "13.1"
provider: Community
status: basic
last_update: 2025-09-14
---

# Debian Trixie Milk-V Mars Test Report

## Test Environment

### Operating System Information

- System Version: Debian 13.1 (Trixie)
- Download Link:
  - debian-installer mini ISO: https://deb.debian.org/debian/dists/trixie/main/installer-riscv64/current/images/netboot/mini.iso
  - u-boot-starfive: http://deb.debian.org/debian/pool/main/u/u-boot/u-boot-starfive_2025.01-3_riscv64.deb
- Reference Installation Document: [Debian Wiki](https://wiki.debian.org/InstallingDebianOn/StarFive/VisionFiveV2)
- Milk-V's wiki (boot mode switch): https://milkv.io/docs/mars/getting-started/setup#boot-mode-switch

Currently there's no MIPI DSI or HDMI support (DC8200) from mainline (see [JH7110 upstream status](https://rvspace.org/en/project/JH7110_Upstream_Plan) page from StarFive), so no display/GUI support at the time.

You'll only be able to use the board from UART serial or SSH.

### Hardware Information

- Milk-V Mars (v1.2, 8GB RAM, other variant should also work)
- A USB power adapter
- A USB-A to C / C to C cable
- A microSD card
- A USB drive (at least 128MB to fit Debian's mini netboot ISO)
- A USB to UART debugger (e.g. CH340, CH341, CH343, FT2232, etc.)
- 3x dupont wires
- Internet connection via ethernet port
- A tooth pick or anything similar to flip the DIP switch ;)

## Installation Steps

Debian Wiki provides multiple installation methods.

For both U-Boot and the main OS, they can all boot from USB, network and serial.

U-Boot binary files are rather small in size and can easily boot over serial (X-MODEM or Y-MODEM), while the netboot ISO is quite large and can take (two) hours to load (which is painful and not really the recommended way).

However there's another catch: vendor U-Boot lacks USB support, so we cannot really update U-Boot over USB.

So the preferred way (if you were on vendor images before) be like:

Phase 1 (temporarily boot Debian U-Boot from RAM): Load U-Boot SPL over UART -> Load U-Boot proper over UART -> Reboot into Debian's U-Boot image 

Phase 2 (permanently flash Debian U-Boot into SPI Flash): Flash Debian's U-Boot SPL and U-Boot proper into SPI Flash -> Reboot into U-Boot again

Phase 3 (the actual debian-installer process): Boot debian-installer from USB media -> Install Debian -> Enjoy

Between each phase there might be DIP switch changes so please read carefully.

Before you begin: check out Milk-V documents on the boot mode switch. We need it set tu UART recovery mode first.

i.e. `GPIO0=GPIO1=1`

### Phase 1: Boot into Debian U-Boot

First you need to download Debian's U-Boot images.

If you already have an up and running Debian system, use `dpkg` to extract the binaries:

```shell
wget http://deb.debian.org/debian/pool/main/u/u-boot/u-boot-starfive_2025.01-3_riscv64.deb
dpkg -x u-boot-starfive_2025.01-3_riscv64.deb u-boot-starfive_2025.01-3_riscv64
```

If not, you can use 7-Zip or `ar` from `binutils`:

```shell
wget http://deb.debian.org/debian/pool/main/u/u-boot/u-boot-starfive_2025.01-3_riscv64.deb
# 7-Zip
7z x u-boot-starfive_2025.01-3_riscv64.deb
tar xvf data.tar
# ar
ar x u-boot-starfive_2025.01-3_riscv64.deb
tar xvf data.tar.xz
```

Make sure your board's boot mode select switch is set to UART recovery (both set to 0).

Now start a serial terminal with tools like `tio` or `minicom` (we'll use `tio` here).

(We're using CH343P here so it's `ttyACM` rather than `ttyUSB`, and be aware that `sudo` might be needed)

```shell
tio /dev/ttyACM0 -o 1
```

Now power on the board, you should see the board printing this:

```log
(C)StarFive
CC
```

Press `Ctrl+T` then `X`

```log
[15:50:16.277] Please enter which X modem protocol to use:
[15:50:16.277]  (0) XMODEM-1K send
[15:50:16.277]  (1) XMODEM-CRC send
[15:50:16.277]  (2) XMODEM-CRC receive
CCCCCCCCCC
```

Press `0`

```log
[15:50:17.644] Send file with XMODEM-1K
[15:50:17.644] Enter file name:
```

Enter: `u-boot-spl.bin.normal.out`

```log
[15:50:25.199] Sending file 'u-boot-spl.bin.normal.out'
[15:50:25.199] Press any key to abort transfer
................................................................................................................................................|
[15:50:39.047] Done

U-Boot SPL 2025.01-3 (Apr 08 2025 - 23:07:41 +0000)
DDR version: dc2e84f0.
Trying to boot from UART
C
```

Press `Ctrl+T` then `Y`

```log
[15:50:43.179] Send file with YMODEM
[19:50:43.179] Enter file name: 
```

Enter `u-boot.itb`

```log
[15:50:43.179] Send file with YMODEM
[15:50:45.975] Sending file 'u-boot.itb'
[15:50:45.975] Press any key to abort transfer
..........................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................|
[15:52:21.529] Done
Loaded 1024523 bytes


U-Boot 2025.01-3 (Apr 08 2025 - 23:07:41 +0000)

CPU:   sifive,u74-mc
Model: Milk-V Mars
DRAM:  8 GiB
Core:  133 devices, 26 uclasses, devicetree: board
WDT:   Not starting watchdog@13070000
MMC:   mmc@16010000: 0, mmc@16020000: 1
Loading Environment from SPIFlash... SF: Detected gd25lq128 with page size 256 Bytes, erase size 4 KiB, total 16 MiB
*** Warning - bad CRC, using default environment

StarFive EEPROM format v2

--------EEPROM INFO--------
Vendor : MILK-V
Product full SN: MARS-V11-2340-D008E000-00000FB6
data version: 0x2
PCB revision: 0xc1
BOM revision: A
Ethernet MAC0 address: 6c:cf:39:00:94:c3
Ethernet MAC1 address: 6c:cf:39:00:94:c4
--------EEPROM INFO--------

starfive_7110_pcie pcie@2b000000: Starfive PCIe bus probed.
starfive_7110_pcie pcie@2c000000: Starfive PCIe bus probed.
In:    serial@10000000
Out:   serial@10000000
Err:   serial@10000000
Net:   eth0: ethernet@16030000
starting USB...
Bus xhci_pci: Register 5000420 NbrPorts 5
Starting the controller
USB XHCI 1.00
scanning bus xhci_pci for devices... 2 USB Device(s) found
       scanning usb for storage devices... 0 Storage Device(s) found
Working FDT set to ff72da10
Hit any key to stop autoboot:  0
```

As prompted, hit any key to stop autoboot.

And we're in Debian's U-Boot and ready for phase 2.

### Phase 2: Flash Debian U-Boot into SPI Flash

Run `sf probe`:

```log
StarFive # sf probe
SF: Detected gd25lq128 with page size 256 Bytes, erase size 4 KiB, total 16 MiB
StarFive # 
```

Run `loady $loadaddr && sf update $loadaddr 0 $filesize`

```
StarFive # loady $loadaddr && sf update $loadaddr 0 $filesize
## Ready for binary (ymodem) download to 0x82000000 at 115200 bps...
C
```

Press `Ctrl+T` then `Y`

```log
[15:52:38.149] Send file with YMODEM
[15:52:38.149] Enter file name:
```

Enter `u-boot-spl.bin.normal.out`

```log
[15:52:41.925] Sending file 'u-boot-spl.bin.normal.out'
[15:52:41.925] Press any key to abort transfer
.................................................................................................................................................|
[15:52:59.538] Done
## Total Size      = 0x00023f4a = 147274 Bytes
## Start Addr      = 0x82000000
device 0 offset 0x0, size 0x23f4a
147274 bytes written, 0 bytes skipped in 0.628s, speed 238999 B/s
StarFive #
```

Run `loady $loadaddr && sf update $loadaddr 100000 $filesize`

```log
StarFive # loady $loadaddr && sf update $loadaddr 100000 $filesize
## Ready for binary (ymodem) download to 0x82000000 at 115200 bps...
C
```

Press `Ctrl+T` then `Y`

```log
[15:53:17.756] Send file with YMODEM
[15:53:17.756] Enter file name:
```

Enter `u-boot.itb`

```log
[15:53:20.837] Sending file 'u-boot.itb'
[15:53:20.837] Press any key to abort transfer
..........................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................|
[15:54:56.178] Done
## Total Size      = 0x000fa20b = 1024523 Bytes
## Start Addr      = 0x82000000
device 0 offset 0x100000, size 0xfa20b
925696 bytes written, 98827 bytes skipped in 6.490s, speed 161575 B/s
StarFive #
```

Now erase U-Boot env by running `env erase`:

```log
StarFive # env erase
Erasing Environment on SPIFlash... OK
StarFive #
Erasing Environment on SPIFlash... OK
StarFive #
```

Now Debian's U-Boot images are ready inside the SPI Flash.

Power off the board, change the DIP switch to QSPI NOR Flash boot, `GPIO0=GPIO1=0`, and we're ready for phase 3: the debian-installer.

### Phase 3: Boot from USB and install Debian

First, download the netboot mini ISO:

```shell
wget https://deb.debian.org/debian/dists/trixie/main/installer-riscv64/current/images/netboot/mini.iso
```

Insert your USB drive to your computer and write ISO to it.

> [!WARNING]
> All your data on the USB drive will be lost!
> Make sure to back them up before proceeding.

Assuming the drive is located at `/dev/sdX`:

```shell
sudo wipefs -af /dev/sdX
sudo dd if=mini.iso of=/dev/sdX bs=1M status=progress
sync; sudo eject /dev/sdX
```

Unplug the drive, plug it into Mars' USB 3.0 port, and power on the board.

> [!NOTE]
> There are 4 ports on the Mars.
> The two ports near the ethernet port sometimes might not pick up the drive.
> If this is the case, use the other two USB 3.0 ports, then rescan USB devices by running `usb reset` inside U-Boot.

```log
U-Boot SPL 2025.01-3 (Apr 08 2025 - 23:07:41 +0000)
DDR version: dc2e84f0.
Trying to boot from SPI


U-Boot 2025.01-3 (Apr 08 2025 - 23:07:41 +0000)

CPU:   sifive,u74-mc
Model: Milk-V Mars
DRAM:  8 GiB
Core:  133 devices, 26 uclasses, devicetree: board
WDT:   Not starting watchdog@13070000
MMC:   mmc@16010000: 0, mmc@16020000: 1
Loading Environment from SPIFlash... SF: Detected gd25lq128 with page size 256 Bytes, erase size 4 KiB, total 16 MiB
*** Warning - bad CRC, using default environment

StarFive EEPROM format v2                                                                                                                  

--------EEPROM INFO--------
Vendor : MILK-V
Product full SN: MARS-V11-2340-D008E000-00000FB6
data version: 0x2
PCB revision: 0xc1
BOM revision: A
Ethernet MAC0 address: 6c:cf:39:00:94:c3
Ethernet MAC1 address: 6c:cf:39:00:94:c4
--------EEPROM INFO--------

starfive_7110_pcie pcie@2b000000: Starfive PCIe bus probed.
starfive_7110_pcie pcie@2c000000: Starfive PCIe bus probed.
In:    serial@10000000
Out:   serial@10000000
Err:   serial@10000000
Net:   eth0: ethernet@16030000
starting USB...
Bus xhci_pci: Register 5000420 NbrPorts 5
Starting the controller
USB XHCI 1.00
scanning bus xhci_pci for devices... 3 USB Device(s) found
       scanning usb for storage devices... 1 Storage Device(s) found
Working FDT set to ff72da10
Hit any key to stop autoboot:  0
Card did not respond to voltage select! : -110
Failed to load EFI variables
** Booting bootflow '<NULL>' with efi_mgr
Booting: usb 0
```

The board should boot into GRUB and then the debian-installer.

If not, interrupt autoboot and manually run:

```shell
usb start
run bootcmd_usb0
```

And then it's the regular Debian installation process.

You may do any changes as you wish, but do note a few things:

- You'll probably want to disable **swap** if you're booting from microSD, which is very likely the case on Mars since there's no M.2 NVMe slot as the VisionFive 2.
- Choose "Yes" when the installer is asking you if you want to install EFI for removable media.
  - By doing so, GRUB will place an additional copy of GRUB to `EFI/BOOT/BOOTRISCV64.EFI` and U-Boot will pick it up automatically.

After the installation completes, if you want to read/edit U-Boot env variables, you may want to install `u-boot-tools` and place the following config to `/etc/fw_env.config`:

```
# Edit /etc/fw_env.config and set to content as below:

# NOR example
# MTD device name       Device offset   Env. size       Flash sector size       Number of sectors
/dev/mtd1               0x0000          0x10000         0x1000
```

### Logging into the System

Logging into the system via the serial port.

The username and password are set during the installation process so there are no default values here.

## Expected Results

The system should boot up normally and allow login via the serial port.

## Actual Results

The system starts normally and the output is successfully viewed through the serial port. 

### Boot Information

Full installation process + boot log: see the asciicast below.

[![asciicast](https://asciinema.org/a/faBiHx1pVS6YuStFiAn4oOuPW.svg)](https://asciinema.org/a/faBiHx1pVS6YuStFiAn4oOuPW)

Boot log:

```log
Loading Linux 6.12.43+deb13-riscv64 ...
Loading initial ramdisk ...
/dev/mmcblk1p2: clean, 29899/7766016 files, 872792/31043072 blocks

Debian GNU/Linux 13 mars ttyS0

mars login: mx
Password:
Linux mars 6.12.43+deb13-riscv64 #1 SMP Debian 6.12.43-1 (2025-08-27) riscv64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
mx@mars:~$ uname -a
Linux mars 6.12.43+deb13-riscv64 #1 SMP Debian 6.12.43-1 (2025-08-27) riscv64 GNU/Linux
mx@mars:~$ cat /etc/os-release
PRETTY_NAME="Debian GNU/Linux 13 (trixie)"
NAME="Debian GNU/Linux"
VERSION_ID="13"
VERSION="13 (trixie)"
VERSION_CODENAME=trixie
DEBIAN_VERSION_FULL=13.1
ID=debian
HOME_URL="https://www.debian.org/"
SUPPORT_URL="https://www.debian.org/support"
BUG_REPORT_URL="https://bugs.debian.org/"
mx@mars:~$ cat /etc/debian_version
13.1
mx@mars:~$ cat /proc/cpuinfo
processor       : 0
hart            : 1
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd_zba_zbb
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x4210427
hart isa        : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd_zba_zbb

processor       : 1
hart            : 2
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd_zba_zbb
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x4210427
hart isa        : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd_zba_zbb

processor       : 2
hart            : 3
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd_zba_zbb
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x4210427
hart isa        : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd_zba_zbb

processor       : 3
hart            : 4
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd_zba_zbb
mmu             : sv39
uarch           : sifive,u74-mc
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x4210427
hart isa        : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd_zba_zbb

mx@mars:~$ lscpu
Architecture:                riscv64
  Byte Order:                Little Endian
CPU(s):                      4
  On-line CPU(s) list:       0-3
Vendor ID:                   0x489
  Model name:                sifive,u74-mc
    CPU family:              0x8000000000000007
    Model:                   0x4210427
    Thread(s) per core:      1
    Core(s) per socket:      4
    Socket(s):               1
    CPU(s) scaling MHz:      100%
    CPU max MHz:             1500.0000
    CPU min MHz:             375.0000
Caches (sum of all):
  L1d:                       128 KiB (4 instances)
  L1i:                       128 KiB (4 instances)
  L2:                        2 MiB (1 instance)
NUMA:
  NUMA node(s):              1
  NUMA node0 CPU(s):         0-3
Vulnerabilities:
  Gather data sampling:      Not affected
  Indirect target selection: Not affected
  Itlb multihit:             Not affected
  L1tf:                      Not affected
  Mds:                       Not affected
  Meltdown:                  Not affected
  Mmio stale data:           Not affected
  Reg file data sampling:    Not affected
  Retbleed:                  Not affected
  Spec rstack overflow:      Not affected
  Spec store bypass:         Not affected
  Spectre v1:                Not affected
  Spectre v2:                Not affected
  Srbds:                     Not affected
  Tsa:                       Not affected
  Tsx async abort:           Not affected
  mx@mars:~$ sudo apt update; sudo apt install -y fastfetch
[sudo] password for mx:
Hit:1 http://mirror.nju.edu.cn/debian trixie InRelease
Hit:2 http://mirror.nju.edu.cn/debian trixie-updates InRelease
Hit:3 http://security.debian.org/debian-security trixie-security InRelease
All packages are up to date.
Installing:
  fastfetch

Installing dependencies:
  libyyjson0

Summary:
  Upgrading: 0, Installing: 2, Removing: 0, Not Upgrading: 0
  Download size: 669 kB
  Space needed: 1,879 kB / 117 GB available

Get:1 http://mirror.nju.edu.cn/debian trixie/main riscv64 libyyjson0 riscv64 0.10.0+ds-1+b1 [117 kB]
Get:2 http://mirror.nju.edu.cn/debian trixie/main riscv64 fastfetch riscv64 2.40.4+dfsg-1 [552 kB]
Fetched 669 kB in 0s (2,567 kB/s)
Selecting previously unselected package libyyjson0:riscv64.
(Reading database ... 26400 files and directories currently installed.)
Preparing to unpack .../libyyjson0_0.10.0+ds-1+b1_riscv64.deb ...
Unpacking libyyjson0:riscv64 (0.10.0+ds-1+b1) ...
Selecting previously unselected package fastfetch.
Preparing to unpack .../fastfetch_2.40.4+dfsg-1_riscv64.deb ...
Unpacking fastfetch (2.40.4+dfsg-1) ...
Setting up libyyjson0:riscv64 (0.10.0+ds-1+b1) ...
Setting up fastfetch (2.40.4+dfsg-1) ...
Processing triggers for man-db (2.13.1-1) ...
Processing triggers for libc-bin (2.41-12) ...
mx@mars:~$ fastfetch
        _,met$$$$$gg.          mx@mars
     ,g$$$$$$$$$$$$$$$P.       -------
   ,g$$P""       """Y$$.".     OS: Debian GNU/Linux 13 (trixie) riscv64
  ,$$P'              `$$$.     Host: Milk-V Mars
',$$P       ,ggs.     `$$b:    Kernel: Linux 6.12.43+deb13-riscv64
`d$$'     ,$P"'   .    $$$     Uptime: 1 min
 $$P      d$'     ,    $$P     Packages: 302 (dpkg)
 $$:      $$.   -    ,d$$'     Shell: bash 5.2.37
 $$;      Y$b._   _,d$P'       Terminal: vt220
 Y$$.    `.`"Y$$$$P"'          CPU: jh7110 (4) @ 1.50 GHz
 `$$b      "-.__               Memory: 308.27 MiB / 7.74 GiB (4%)
  `Y$$b                        Swap: Disabled
   `Y$$.                       Disk (/): 952.57 MiB / 116.00 GiB (1%) - ext4
     `$$b.                     Local IP (end0): 10.0.0.32/24
       `Y$$b.                  Locale: en_US.UTF-8
         `"Y$b._
             `""""

mx@mars:~$
```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
