---
sys: debian
sys_ver: trixie/sid
sys_var: null

status: basic
last_update: 2025-04-10
---

# Debian trixie/sid HiFive Unmatched Test Report

## Test Environment

### Operating System Information

- System Version: Debian trixie/sid
- Download Link: https://github.com/yuzibo/Unmatched-Debian-image/releases/tag/0.0.5-beta
- Reference Installation Document
    - https://wiki.debian.org/InstallingDebianOn/SiFive/%20HiFiveUnmatched
    - https://github.com/yuzibo/Unmatched-Debian-image

### Hardware Information

- HiFive Unmatched Rev A
- A microUSB cable (comes with HiFive Unmatched)
- An ATX power supply
- A microSD card (if you prefer U-Boot on microSD)
- A M.2 NVMe SSD
    - M.2 NVMe to USB enclosure to flash the image

## Installation Steps

For HiFive Unmatched there are multiple ways to boot, according to the [software reference manual](https://www.sifive.com/document-file/hifive-unmatched-software-reference-manual).

For this Debian image, two options we can use:
- Use the U-Boot image from the GitHub release page, flash it to the microSD card, DIP switch set to `MSEL[3:0]=1011` (which is the factory default)
- Manually compile mainline U-Boot, flash it to SPI Flash, DIP switch set to `MSEL[3:0]=0110`
    - Requires an OS already installed and is capable of flashing SPI
    - See U-Boot's documentation here: https://docs.u-boot.org/en/latest/board/sifive/unmatched.html

### U-Boot on microSD

`/dev/sdX` is the location of the microSD card, `/dev/sdY` is the location of M.2 NVMe SSD, please adjust accordingly.

```bash
wget https://github.com/yuzibo/Unmatched-Debian-image/releases/download/0.0.5-beta/sd-uboot.img.xz \
     https://github.com/yuzibo/Unmatched-Debian-image/releases/download/0.0.5-beta/nvme-rootfs.img.xz
xz -dkv sd-uboot.img.xz
xz -dkv nvme-rootfs.img.xz
sudo dd if=sd-uboot.img of=/dev/sdX bs=1M status=progress
sudo dd if=nvme-rootfs.img of=/dev/sdY bs=1M status=progress
sync
sudo eject /dev/sdX; sudo eject /dev/sdY
```

Now, install both the microSD card and NVMe SSD to the board.

Make sure the DIP switches are correctly set: `MSEL[3:0]=1011`

### U-Boot on SPI Flash

Assuming you already have an OS up and running on Unmatched.

You need to manually build U-Boot.

#### Building U-Boot

Below is only a rough guideline: you'll need to install required packages, and configure toolchains (both cross build and native build are okay).

For full documentation please check out U-Boot's official website: https://docs.u-boot.org/en/latest/board/sifive/unmatched.html

```shell
git clone https://github.com/riscv/opensbi.git
pushd opensbi
make PLATFORM=generic -j$(nproc)
popd
wget https://github.com/u-boot/u-boot/archive/refs/tags/v2025.04.tar.gz
tar xvf v2025.04.tar.gz
cd u-boot-2025.04
export OPENSBI=../opensbi/build/platform/generic/firmware/fw_dynamic.bin
make sifive_unmatched_defconfig
make -j$(nproc)
```

#### Flash the images

The following steps are from the official U-Boot documentation.

```shell
sgdisk --clear -a 1 \
    --new=1:40:2087     --change-name=1:spl   --typecode=1:5B193300-FC78-40CD-8002-E86C45580B47 \
    --new=2:2088:10279  --change-name=2:uboot --typecode=2:2E54B353-1271-4842-806F-E436D6AF6985 \
    --new=3:10280:10535 --change-name=3:env   --typecode=3:3DE21764-95BD-54BD-A5C3-4ABE786F38A8 \
    /dev/mtdblock0
dd if=spl/u-boot-spl.bin of=/dev/mtdblock0 bs=4096 seek=5 conv=sync
dd if=u-boot.itb  of=/dev/mtdblock0 bs=4096 seek=261 conv=sync
```

On another computer, flash the Debian image into NVMe SSD:

```shell
wget https://github.com/yuzibo/Unmatched-Debian-image/releases/download/0.0.5-beta/nvme-rootfs.img.xz
xz -dkv nvme-rootfs.img.xz
sudo dd if=nvme-rootfs.img of=/dev/sdY bs=1M status=progress
sync
sudo eject /dev/sdX; sudo eject /dev/sdY
```

Now power off the board, install the NVMe SSD with Debian image flashed, change DIP switch to `MSEL[3:0]=0110` and then power on the board.

### Logging into the System

Logging into the system via the onboard serial port (using the microUSB cable connected to another computer).

Default username: `rv`
Default password: `rv`

#### Resizing partition

The root partition by default is not automatically resized.

Do as the following:

```log
rv@unmatched:~$ sudo fdisk /dev/nvme0n1

Welcome to fdisk (util-linux 2.40.4).
Changes will remain in memory only, until you decide to write them.
Be careful before using the write command.

GPT PMBR size mismatch (6291455 != 250069679) will be corrected by write.
This disk is currently in use - repartitioning is probably a bad idea.
It's recommended to umount all file systems, and swapoff all swap
partitions on this disk.


Command (m for help): e
Partition number (1-4, default 4): 4

New <size>{K,M,G,T,P} in bytes or <size>S in sectors (default 118.8G): <Enter>

Partition 4 has been resized.

Command (m for help): w
The partition table has been altered.
Syncing disks.

rv@unmatched:~$ sudo resize2fs /dev/nvme0n1p4
[  178.683726] EXT4-fs (nvme0n1p4): resizing filesystem from 681979 to 31154257 blocks
resize2fs 1.47.2 (1-Jan-2025)
Filesystem at /dev/nvme0n1p4 is mounted on /; on-line resizing required
old_desc_blocks = 1, new_desc_blocks = 15
[  179.016304] EXT4-fs (nvme0n1p4): resized filesystem to 31154257
The filesystem on /dev/nvme0n1p4 is now 31154257 (4k) blocks long.

rv@unmatched:~$ df -hT
Filesystem     Type      Size  Used Avail Use% Mounted on
udev           devtmpfs  7.8G     0  7.8G   0% /dev
tmpfs          tmpfs     1.6G  376K  1.6G   1% /run
/dev/nvme0n1p4 ext4      117G  541M  112G   1% /
tmpfs          tmpfs     7.9G     0  7.9G   0% /dev/shm
tmpfs          tmpfs     5.0M     0  5.0M   0% /run/lock
tmpfs          tmpfs     7.9G     0  7.9G   0% /tmp
tmpfs          tmpfs     1.0M     0  1.0M   0% /run/credentials/systemd-journald.service
/dev/nvme0n1p3 ext4      358M   69M  266M  21% /boot
tmpfs          tmpfs     1.0M     0  1.0M   0% /run/credentials/getty@tty1.service
tmpfs          tmpfs     1.0M     0  1.0M   0% /run/credentials/serial-getty@ttySIF0.service
tmpfs          tmpfs     1.6G  4.0K  1.6G   1% /run/user/1000
rv@unmatched:~$ 
```

## Expected Results

The system boots normally and allows login through the onboard serial port.

## Actual Results

The system booted successfully, and login through the onboard serial port was also successful.

### Boot Log

```log
Debian GNU/Linux trixie/sid unmatched ttySIF0

unmatched login: rv
Password:
Linux unmatched 6.12.17-riscv64 #1 SMP Debian 6.12.17-1 (2025-03-01) riscv64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
rv@unmatched:~$ fastfetch
        _,met$$$$$gg.          rv@unmatched
     ,g$$$$$$$$$$$$$$$P.       ------------
   ,g$$P""       """Y$$.".     OS: Debian GNU/Linux trixie/sid riscv64
  ,$$P'              `$$$.     Host: SiFive HiFive Unmatched A00
',$$P       ,ggs.     `$$b:    Kernel: Linux 6.12.17-riscv64
`d$$'     ,$P"'   .    $$$     Uptime: 50 seconds
 $$P      d$'     ,    $$P     Packages: 186 (dpkg)
 $$:      $$.   -    ,d$$'     Shell: bash 5.2.37
 $$;      Y$b._   _,d$P'       Terminal: vt220
 Y$$.    `.`"Y$$$$P"'          CPU: fu740-c000 (4)
 `$$b      "-.__               Memory: 294.54 MiB / 15.60 GiB (2%)
  `Y$$b                        Swap: Disabled
   `Y$$.                       Disk (/): 545.80 MiB / 2.49 GiB (21%) - ext4
     `$$b.                     Local IP (end0): 10.0.0.117/24
       `Y$$b.                  Locale: C
         `"Y$b._
             `""""

rv@unmatched:~$ uname -a
Linux unmatched 6.12.17-riscv64 #1 SMP Debian 6.12.17-1 (2025-03-01) riscv64 GNU/Linux
rv@unmatched:~$ cat /proc/cpuinfo
processor       : 0
hart            : 2
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd
mmu             : sv39
uarch           : sifive,bullet0
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x20181004
hart isa        : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd

processor       : 1
hart            : 1
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd
mmu             : sv39
uarch           : sifive,bullet0
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x20181004
hart isa        : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd

processor       : 2
hart            : 3
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd
mmu             : sv39
uarch           : sifive,bullet0
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x20181004
hart isa        : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd

processor       : 3
hart            : 4
isa             : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd
mmu             : sv39
uarch           : sifive,bullet0
mvendorid       : 0x489
marchid         : 0x8000000000000007
mimpid          : 0x20181004
hart isa        : rv64imafdc_zicntr_zicsr_zifencei_zihpm_zca_zcd

rv@unmatched:~$ cat /etc/os-release
PRETTY_NAME="Debian GNU/Linux trixie/sid"
NAME="Debian GNU/Linux"
VERSION_CODENAME=trixie
ID=debian
HOME_URL="https://www.debian.org/"
SUPPORT_URL="https://www.debian.org/support"
BUG_REPORT_URL="https://bugs.debian.org/"
rv@unmatched:~$ cat /etc/deb
debconf.conf    debian_version
rv@unmatched:~$ cat /etc/debian_version
trixie/sid
```

#### Screen records

U-Boot on SPI Flash:

[![asciicast](https://asciinema.org/a/xmS1RmYMMmQXyhUF0a0xnVK2I.svg)](https://asciinema.org/a/xmS1RmYMMmQXyhUF0a0xnVK2I)

U-Boot on microSD:

(Note the boot failure from MMC is normal, `bootflow` will automatically scan the next available boot device, which is NVMe in this case.)

[![asciicast](https://asciinema.org/a/348eO3lu9rQqsZyMyZvFzAA4U.svg)](https://asciinema.org/a/348eO3lu9rQqsZyMyZvFzAA4U)

> [!NOTE]  
> Even though we only tested CLI and marked this report as `basic` support for now, that's only because we're not using a dGPU this time.
> If you plug in an appropriate GPU that the system supports, e.g. AMD ones, it's very likely you can get video output.
> You'll need to install desktop and GPU related packages, of course.

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
