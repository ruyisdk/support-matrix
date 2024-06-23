# NuttX on Milk-V Duo S Test Report

## Test Environment

### Operating System Information

- Build System: Arch Linux
- Debian Linux Image + U-Boot: https://github.com/Fishwaldo/sophgo-sg200x-debian/releases/tag/v1.1.0
- Source Links:
    - NuttX: https://github.com/lupyuen2/wip-nuttx/tree/sg2000
    - NuttX Apps: https://github.com/lupyuen2/wip-nuttx-apps/tree/sg2000
- Toolchain: xPack (installed using [xpm](https://xpack.github.io/xpm/install/), see the [Configure Toolchain](#configure-toolchain) section below)
- Reference Installation Document: https://github.com/lupyuen/nuttx-sg2000

The NuttX SG2000 port is still under development and currently requires booting through TFTP.

### Hardware Information

- Milk-V Duo S (512M, SG2000)
- A USB Power Adapter
- A USB-A to C or USB C to C cable for powering the development board
- A microSD card
- A USB card reader
- A USB to UART Debugger (e.g., CP2102, FT2232, etc. Be aware that WCH CH340/341 series will cause garbled text output, DO NOT USE)
- Three DuPont wires
- Ethernet access for TFTP Boot

## Installation Steps

### Install Build Dependencies

```shell
sudo pacman -S --needed base-devel ncurses5-compat-libs gperf pkg-config gmp libmpc mpfr libelf expat picocom uboot-tools util-linux git wget libisl
# Don't use Arch repo's gcc toolchain for now
sudo pacman -Rnscu riscv64-elf-gcc
# AUR packages only, use any AUR helper as you wish
paru -S kconfig-frontends genromfs
# yay -S kconfig-frontends genromfs
```

### Retrieve the Source Code

```shell
git clone -b sg2000 https://github.com/lupyuen2/wip-nuttx nuttx
git clone -b sg2000 https://github.com/lupyuen2/wip-nuttx-apps apps
cd nuttx
git pull && git status && hash1=`git rev-parse HEAD`
pushd ../apps
git pull && git status && hash2=`git rev-parse HEAD`
popd
echo NuttX Source: https://github.com/apache/nuttx/tree/$hash1 >nuttx.hash
echo NuttX Apps: https://github.com/apache/nuttx-apps/tree/$hash2 >>nuttx.hash
```

### Configure Toolchain and Build NuttX

> **Note**
> When using the `riscv64-elf-gcc` toolchain from the Arch Linux repositories, compilation may stop due to a missing `math.h`. Use the xPack toolchain to avoid this issue.
>
> Install the xPack toolchain into the NuttX directory using `xpm`.

```shell
sudo pacman -S npm
sudo npm install --global xpm@latest
cd nuttx
xpm init
xpm install @xpack-dev-tools/riscv-none-elf-gcc@latest --verbose
export PATH=$PWD/xpacks/.bin:$PATH
tools/configure.sh ox64:nsh
pushd ../nuttx
make -j$(nproc)

## Build Apps Filesystem
make -j$(nproc) export
pushd ../apps
./tools/mkimport.sh -z -x ../nuttx/nuttx-export-*.tar.gz
make -j$(nproc) import
popd

## Return to previous folder
popd

## Remove previous files if not building the first time
# rm /tmp/nuttx.pad Image nuttx.S init.S hello.S

## Generate Initial RAM Disk
genromfs -f initrd -d ../apps/bin -V "NuttXBootVol"

## Show the size
riscv64-unknown-elf-size nuttx

## Export the Binary Image to `nuttx.bin`
riscv64-unknown-elf-objcopy \
  -O binary \
  nuttx \
  nuttx.bin

## Prepare a Padding with 64 KB of zeroes
head -c 65536 /dev/zero >/tmp/nuttx.pad

## Append Padding and Initial RAM Disk to NuttX Kernel
cat nuttx.bin /tmp/nuttx.pad initrd \
  >Image

## Copy the config
cp .config nuttx.config

## Dump the disassembly to nuttx.S
riscv64-unknown-elf-objdump \
  --syms --source --reloc --demangle --line-numbers --wide \
  --debugging \
  nuttx \
  >nuttx.S \
  2>&1

## Dump the init disassembly to init.S
riscv64-unknown-elf-objdump \
  --syms --source --reloc --demangle --line-numbers --wide \
  --debugging \
  ../apps/bin/init \
  >init.S \
  2>&1

## Dump the hello disassembly to hello.S
riscv64-unknown-elf-objdump \
  --syms --source --reloc --demangle --line-numbers --wide \
  --debugging \
  ../apps/bin/hello \
  >hello.S \
  2>&1

## Copy NuttX Image to TFTP Server
scp Image tftpserver:/tftpboot/Image
ssh tftpserver ls -l /tftpboot/Image
```

### Booting NuttX RTOS from TFTP Server

First, flash the Debian image onto the storage card.

```shell
unzip milkv-duos-sd-v1.1.0-2024-0410.img.zip
sudo dd if=milkv-duos-sd-v1.1.0-2024-0410.img of=/dev/sdX bs=1M status=progress
```

Next, we will use the pre-included U-Boot and dtb from the image. Mount the first FAT partition of the freshly flashed storage card and copy the dtb file:

```shell
sudo mount /dev/sdX1 /mnt
cp /mnt/fdt/linux-image-duos-5.10.4-20240329-1+/cv181x_milkv_duos_sd.dtb ~/
sudo umount /mnt
```

The storage card is now ready. Insert it into the development board.

Start a TFTP server on your computer. Ensure both the compiled Image (located in the NuttX source directory) and dtb are accessible by the TFTP server.

Refer to: [Arch Wiki/TFTP](https://wiki.archlinux.org/title/TFTP) for TFTP server configuration.

On Windows, you may consider using [Tftpd64](http://tftpd32.jounin.net).

Connect the UART debug cable, power on the development board, and press any key when prompted (`Hit any key to stop autoboot`) to interrupt U-Boot. Manually configure U-Boot to boot NuttX from TFTP:

```shell
setenv tftp_server your_tftp_server_ip
dhcp ${kernel_addr_r} ${tftp_server}:Image
tftpboot ${fdt_addr_r} ${tftp_server}:cv181x_milkv_duos_sd.dtb
booti ${kernel_addr_r} ${ramdisk_addr_r}:${ramdisk_size} ${fdt_addr_r}
```

## Expected Results

The system should boot normally, and you should be able to access the NuttX shell via the serial connection.

## Actual Results

The system booted successfully, and the NuttX shell was accessible via the serial connection.

Commands like `uname`, `ls`, and `ostest` were executed successfully.

### Boot Information

<details><summary>Boot log</summary>

```log
C.SCS/0/0.WD.URPL.SDI/25000000/6000000.BS/SD.PS.SD/0x0/0x1000/0x1000/0.PE.BS.SD/0x1000/0x8200/0x8200/0.BE.J.
FSBL Jb2829:gbeb1483-dirty:2024-04-24T11:25:09+00:00
st_on_reason=d0000
st_off_reason=0
P2S/0x1000/0xc00a200.
SD/0x9200/0x1000/0x1000/0.P2E.
DPS/0xa200/0x2000.
SD/0xa200/0x2000/0x2000/0.DPE.
DDR init.
ddr_param[0]=0x78075562.
pkg_type=1
D2_4_1
DDR3-4G-BGA
Data rate=1866.
DDR BIST PASS
PLLS/OD.
C2S/0xc200/0x9fe00000/0x200.
SD/0xc200/0x200/0x200/0.RSC.
C2E.
MS/0xc400/0x80000000/0x1b000.
SD/0xc400/0x1b000/0x1b000/0.ME.
L2/0x27400.
SD/0x27400/0x200/0x200/0.L2/0x414d3342/0xcafe3814/0x80200000/0x37a00/0x37a00
COMP/1.
SD/0x27400/0x37a00/0x37a00/0.DCP/0x80200020/0x1000000/0x81900020/0x37a00/1.
DCP/0x752d0/0.
Loader_2nd loaded.
Switch RTC mode to xtal32k
Jump to monitor at 0x80000000.
OPENSBI: next_addr=0x80200020 arg1=0x80080000
OpenSBI v0.9
   ____                    _____ ____ _____
  / __ \                  / ____|  _ \_   _|
 | |  | |_ __   ___ _ __ | (___ | |_) || |
 | |  | | '_ \ / _ \ '_ \ \___ \|  _ < | |
 | |__| | |_) |  __/ | | |____) | |_) || |_
  \____/| .__/ \___|_| |_|_____/|____/_____|
        | |
        |_|

Platform Name             : Milk-V DuoS
Platform Features         : mfdeleg
Platform HART Count       : 1
Platform IPI Device       : clint
Platform Timer Device     : clint
Platform Console Device   : uart8250
Platform HSM Device       : ---
Platform SysReset Device  : ---
Firmware Base             : 0x80000000
Firmware Size             : 132 KB
Runtime SBI Version       : 0.3

Domain0 Name              : root
Domain0 Boot HART         : 0
Domain0 HARTs             : 0*
Domain0 Region00          : 0x0000000074000000-0x000000007400ffff (I)
Domain0 Region01          : 0x0000000080000000-0x000000008003ffff ()
Domain0 Region02          : 0x0000000000000000-0xffffffffffffffff (R,W,X)
Domain0 Next Address      : 0x0000000080200020
Domain0 Next Arg1         : 0x0000000080080000
Domain0 Next Mode         : S-mode
Domain0 SysReset          : yes

Boot HART ID              : 0
Boot HART Domain          : root
Boot HART ISA             : rv64imafdcvsux
Boot HART Features        : scounteren,mcounteren,time
Boot HART PMP Count       : 16
Boot HART PMP Granularity : 4096
Boot HART PMP Address Bits: 38
Boot HART MHPM Count      : 8
Boot HART MHPM Count      : 8
Boot HART MIDELEG         : 0x0000000000000222
Boot HART MEDELEG         : 0x000000000000b109


U-Boot 2021.10-ga57aa1f2-dirty (Apr 24 2024 - 11:24:46 +0000) cvitek_cv181x

DRAM:  510 MiB
gd->relocaddr=0x9fbc7000. offset=0x1f9c7000
set_rtc_register_for_power
MMC:   cv-sd@4310000: 0, wifi-sd@4320000: 1
Loading Environment from nowhere... OK
In:    serial
Out:   serial
Err:   serial
Net:
Warning: ethernet@4070000 (eth0) using random MAC address - 66:a9:0b:51:a2:68
eth0: ethernet@4070000
Hit any key to stop autoboot:  0
cv181x_c906# setenv tftp_server 10.0.0.189
cv181x_c906# dhcp ${kernel_addr_r} ${tftp_server}:Image
Speed: 100, full duplex
BOOTP broadcast 1
BOOTP broadcast 2
BOOTP broadcast 3
BOOTP broadcast 4
DHCP client bound to address 10.0.0.210 (3037 ms)
Using ethernet@4070000 device
TFTP from server 10.0.0.189; our IP address is 10.0.0.210
Filename 'Image'.
Load address: 0x80200000
Loading: #################################################################
         #################################################################
         #################################################################
         #################################################################
         #################################################################
         #################################################################
         #################################################################
         #################################################################
         #################################################################
         #################################################################
         #################################################################
         #################################################################
         #################################################################
         #################################################################
         #################################################################
         #################################################################
         #################
         6.3 MiB/s
done
Bytes transferred = 15512152 (ecb258 hex)
cv181x_c906# tftpboot ${fdt_addr_r} ${tftp_server}:cv181x_milkv_duos_sd.dtb
Speed: 100, full duplex
Using ethernet@4070000 device
TFTP from server 10.0.0.189; our IP address is 10.0.0.210
Filename 'cv181x_milkv_duos_sd.dtb'.
Load address: 0x81200000
Loading: ##
         4.1 MiB/s
done
Bytes transferred = 21575 (5447 hex)
cv181x_c906# booti ${kernel_addr_r} ${ramdisk_addr_r}:${ramdisk_size} ${fdt_addr_r}
## Flattened Device Tree blob at 81200000
   Booting using the fdt blob at 0x81200000
   Loading Ramdisk to 9fe00000, end 9fe00000 ... OK
   Loading Device Tree to 000000009f276000, end 000000009f27e446 ... OK

Starting kernel ...

123ABCnx_start: Entry
uart_register: Registering /dev/console
uart_register: Registering /dev/ttyS0
work_start_lowpri: Starting low-priority kernel worker thread(s)
nxtask_activate: lpwork pid=1,TCB=0x80409130
nxtask_activate: AppBringUp pid=2,TCB=0x80409740
nx_start_application: Starting init task: /system/bin/init
elf_symname: Symbol has no name
elf_symvalue: SHN_UNDEF: Failed to get symbol name: -3
elf_relocateadd: Section 2 reloc 1: Undefined symbol[0] has no name: -3
nxtask_activate: /system/bin/init pid=3,TCB=0x8040b8c0
nxtask_exit: AppBringUp pid=2,TCB=0x80409740

NuttShell (NSH) NuttX-12.4.0
nsh> nx_start: CPU0: Beginning Idle Loop

nsh> help
posix_spawn: pid=0xc0202968 path=help file_actions=0xc0202970 attr=0xc0202978 argv=0xc0202a18
exec_internal: ERROR: Failed to load program 'help': -2
nxposix_spawn_exec: ERROR: exec failed: 2
help usage:  help [-v] [<cmd>]

    .           cp          exit        mkdir       rmdir       umount
    [           cmp         expr        mkrd        set         unset
    ?           dirname     false       mount       sleep       uptime
    alias       dd          fdinfo      mv          source      usleep
    unalias     df          free        pidof       test        xd
    basename    dmesg       help        printf      time
    break       echo        hexdump     ps          true
    cat         env         kill        pwd         truncate
    cd          exec        ls          rm          uname
nsh> uname -a
posix_spawn: pid=0xc0202968 path=uname file_actions=0xc0202970 attr=0xc0202978 argv=0xc0202a18
exec_internal: ERROR: Failed to load program 'uname': -2
nxposix_spawn_exec: ERROR: exec failed: 2
NuttX 12.4.0 122c717447 May  9 2024 17:51:20 risc-v ox64
nsh> ls
posix_spawn: pid=0xc0202968 path=ls file_actions=0xc0202970 attr=0xc0202978 argv=0xc0202a18
exec_internal: ERROR: Failed to load program 'ls': -2
nxposix_spawn_exec: ERROR: exec failed: 2
/:
 dev/
 proc/
 system/
nsh> ls /dev/
posix_spawn: pid=0xc0202968 path=ls file_actions=0xc0202970 attr=0xc0202978 argv=0xc0202a18
exec_internal: ERROR: Failed to load program 'ls': -2
nxposix_spawn_exec: ERROR: exec failed: 2
/dev:
 console
 null
 ram0
 ttyS0
 zero
nsh> cat /proc/cpuinfo
posix_spawn: pid=0xc0202968 path=cat file_actions=0xc0202970 attr=0xc0202978 argv=0xc0202a18
exec_internal: ERROR: Failed to load program 'cat': -2
nxposix_spawn_exec: ERROR: exec failed: 2
processor       : 0
hart            : 0
isa             : rv64imafdc
mmu             : none
nsh> free
posix_spawn: pid=0xc0202968 path=free file_actions=0xc0202970 attr=0xc0202978 argv=0xc0202a18
exec_internal: ERROR: Failed to load program 'free': -2
nxposix_spawn_exec: ERROR: exec failed: 2
                 total       used       free    maxused    maxfree  nused  nfree
      Kmem:    2065400      14248    2051152      77016    2048992     35      3
      Page:   20971520     647168   20324352   20324352
nsh> ostest
posix_spawn: pid=0xc0202968 path=ostest file_actions=0xc0202970 attr=0xc0202978 argv=0xc0202a18
elf_symname: Symbol has no name
elf_symvalue: SHN_UNDEF: Failed to get symbol name: -3
elf_relocateadd: Section 2 reloc 1: Undefined symbol[0] has no name: -3
nxtask_activate: ostest pid=6,TCB=0x80409740
stdio_test: write fd=1
stdio_test: Standard I/O Check: printf
stdio_test: write fd=2
stdio_test: Standard I/O Check: fprintf to stderr
ostest_main: putenv(Variable1=BadValue3)
ostest_main: setenv(Variable1, GoodValue1, TRUE)
ostest_main: setenv(Variable2, BadValue1, FALSE)
ostest_main: setenv(Variable2, GoodValue2, TRUE)
ostest_main: setenv(Variable3, GoodValue3, FALSE)
ostest_main: setenv(Variable3, BadValue2, FALSE)
show_variable: Variable=Variable1 has value=GoodValue1
show_variable: Variable=Variable2 has value=GoodValue2
show_variable: Variable=Variable3 has value=GoodValue3
posix_spawn: pid=0xc020276c path=ostest file_actions=0 attr=0xc0202770 argv=0xc0202788
elf_symname: Symbol has no name
elf_symvalue: SHN_UNDEF: Failed to get symbol name: -3
elf_relocateadd: Section 2 reloc 1: Undefined symbol[0] has no name: -3
nxtask_activate: ostest pid=7,TCB=0x8040c830
ostest_main: Started user_main at PID=7

user_main: Begin argument test
user_main: Started with argc=5
user_main: argv[0]="user_main"
user_main: argv[1]="Arg1"
user_main: argv[2]="Arg2"
user_main: argv[3]="Arg3"
user_main: argv[4]="Arg4"

End of test memory usage:
VARIABLE  BEFORE   AFTER
======== ======== ========
arena       80ff8    80ff8
ordblks         2        2
mxordblk    7cff0    7cff0
uordblks     2688     2688
fordblks    7e970    7e970

user_main: getopt() test
getopt():  Simple test
getopt():  Invalid argument
getopt():  Missing optional argument
getopt_long():  Simple test
getopt_long():  No short options
getopt_long():  Argument for --option=argument
getopt_long():  Invalid long option
getopt_long():  Mixed long and short options
getopt_long():  Invalid short option
getopt_long():  Missing optional arguments
getopt_long_only():  Mixed long and short options
getopt_long_only():  Single hyphen long options

End of test memory usage:
VARIABLE  BEFORE   AFTER
======== ======== ========
arena       80ff8    80ff8
ordblks         2        2
mxordblk    7cff0    7cff0
uordblks     2688     2688
fordblks    7e970    7e970

user_main: libc tests

End of test memory usage:
VARIABLE  BEFORE   AFTER
======== ======== ========
arena       80ff8    80ff8
ordblks         2        2
mxordblk    7cff0    7cff0
uordblks     2688     2688
fordblks    7e970    7e970
show_variable: Variable=Variable1 has value=GoodValue1
show_variable: Variable=Variable2 has value=GoodValue2
show_variable: Variable=Variable3 has value=GoodValue3
show_variable: Variable=Variable1 has no value
show_variable: Variable=Variable2 has value=GoodValue2
show_variable: Variable=Variable3 has value=GoodValue3

End of test memory usage:
VARIABLE  BEFORE   AFTER
======== ======== ========
arena       80ff8    80ff8
ordblks         2        3
mxordblk    7cff0    7cff0
uordblks     2688     2668
fordblks    7e970    7e990
show_variable: Variable=Variable1 has no value
show_variable: Variable=Variable2 has no value
show_variable: Variable=Variable3 has no value

End of test memory usage:
VARIABLE  BEFORE   AFTER
======== ======== ========
arena       80ff8    80ff8
ordblks         3        2
mxordblk    7cff0    7cff0
uordblks     2668     2588
fordblks    7e990    7ea70

user_main: setvbuf test
setvbuf_test: Test NO buffering
setvbuf_test: Using NO buffering
setvbuf_test: Test default FULL buffering
setvbuf_test: Using default FULL buffering
setvbuf_test: Test FULL buffering, buffer size 64
setvbuf_test: Using FULL buffering, buffer size 64
setvbuf_test: Test FULL buffering, pre-allocated buffer
setvbuf_test: Using FULL buffering, pre-allocated buffer
setvbuf_test: Test LINE buffering, buffer size 64
setvbuf_test: Using LINE buffering, buffer size 64
setvbuf_test: Test FULL buffering, pre-allocated buffer
setvbuf_test: Using FULL buffering, pre-allocated buffer

End of test memory usage:
VARIABLE  BEFORE   AFTER
======== ======== ========
arena       80ff8    80ff8
ordblks         2        2
mxordblk    7cff0    7cff0
uordblks     2588     2588
fordblks    7ea70    7ea70

user_main: /dev/null test
dev_null: Read 0 bytes from /dev/null
dev_null: Wrote 1024 bytes to /dev/null

End of test memory usage:
VARIABLE  BEFORE   AFTER
======== ======== ========
arena       80ff8    80ff8
ordblks         2        2
mxordblk    7cff0    7cff0
uordblks     2588     2588
fordblks    7ea70    7ea70

user_main: mutex test
Initializing mutex
pthread_mutex_init: mutex=0xc0101588 attr=0
pthread_mutex_init: Returning 0
Starting thread 1
nxtask_activate: ostest pid=10,TCB=0x80409af0
pthread_mutex_timedlock: mutex=0xc0101588
pthread_mutex_timedlock: Returning 0
Starting thread 2
nxtask_activate: ostest pid=12,TCB=0x8040e3b0
pthread_mutex_timedlock: mutex=0xc0101588
pthread_mutex_unlock: mutex=0xc0101588
pthread_mutex_unlock: Returning 0
pthread_mutex_timedlock: Returning 0
pthread_mutex_timedlock: mutex=0xc0101588
pthread_mutex_unlock: mutex=0xc0101588
pthread_mutex_unlock: Returning 0
pthread_mutex_timedlock: Returning 0
pthread_mutex_timedlock: mutex=0xc0101588
pthread_mutex_unlock: mutex=0xc0101588
pthread_mutex_unlock: Returning 0
pthread_mutex_timedlock: Returning 0
pthread_mutex_timedlock: mutex=0xc0101588
pthread_mutex_unlock: mutex=0xc0101588
pthread_mutex_unlock: Returning 0
pthread_mutex_timedlock: Returning 0
pthread_mutex_timedlock: mutex=0xc0101588
pthread_mutex_unlock: mutex=0xc0101588
pthread_mutex_unlock: Returning 0
pthread_mutex_timedlock: mutex=0xc0101pt588
hread_mutex_timedlock: Returning 0
pthread_mutex_unlock: mutex=0xc0101588
pthread_mutex_unlock: Returning 0
pthread_mutex_timedlock: mutex=0xcpthread_mutex_timedlock: Returning 0
0101588
pthread_mutex_unlock: mutex=0xc0101588
pthread_mutex_unlock: Returning 0
pthread_mutex_timedlock: mutex=0xc0101588
pthread_mutex_timedlock: Returning 0
pthread_mutex_unlock: mutex=0xc0101588
pthread_mutex_unlock: Returning 0
pthread_mutex_timedlock: mutex=0xc0101588
pthread_mutex_timedlock: Returning 0
pthread_mutex_unlock: mutex=0xc0101588
pthread_mutex_unlock: Returning 0
pthread_mutex_timedlock: mutex=0xc0101588
pthread_mutex_timedlock: Returning 0
pthread_mutex_unlock: mutex=0xc0101588
pthread_mutex_unlock: Returning 0
pthread_mutex_timedlock: mutex=0xc0101588
pthread_mutex_timedlock: Returning 0
pthread_mutex_unlock: mutex=0xc0101588
pthread_mutex_unlock: Returningpthread_mutex_timedlock: Returning 0
 0
pthread_mutex_timedlock: mutex=0xc0101588
pthread_mutex_unlock: mutex=0xc0101588
pthread_mutex_unlock: Returpthread_mutex_timedlock: Returning 0
ning 0
pthread_mutex_timedlock: mutex=0xc0101588
pthread_mutex_unlock: mutex=0xc0101588
pthread_mutex_unlock: Returning 0
pthread_mutex_timedlock: Returpthread_mutex_timedlock: mutex=0xc0101588
ning 0
pthread_mutex_unlock: mutex=0xc0101588
pthread_mutex_unlock: Returning 0
pthread_mutex_timedlock: Returning 0
pthread_mutex_timedlock: mutex=0xc0101588
pthread_mutex_unlock: mutex=0xc0101588
pthread_mutex_unlock: Returning 0
pthread_mutex_timedlock: Returning 0
pthread_mutex_timedlock: mutex=0xc0101588
pthread_mutex_unlock: mutex=0xc0101588
pthread_mutex_unlock: Returning 0
pthread_mutex_timedlock: mutex=0xc0101588
pthread_mutex_timedlock: Returning 0
pthread_mutex_unlock: mutex=0xc0101588
pthread_mutex_unlock: Returning 0
pthread_mutex_timedlock: mutex=0xc0101pthread_mutex_timedlock: Returning 0
588
pthread_mutex_unlock: mutex=0xc0101588
pthread_mutex_unlock: Returning 0
pthread_mutex_timedlock: mutpthread_mutex_timedlock: Returning 0
ex=0xc0101588
pthread_mutex_unlock: mutex=0xc0101588
pthread_mutex_unlock: Returning 0
pthread_mutex_timedlock: mutex=0xc0101588
pthread_mutex_timedlock: Returning 0
pthread_mutex_unlock: mutex=0xc0101588
pthread_mutex_unlock: Returning 0
pthread_mutex_timedlock: mutex=0xc0101588
pthread_mutex_timedlock: Returning 0
pthread_mutex_unlock: mutex=0xc0101588
pthread_mutex_unlock: Returning 0
pthread_mutex_timedlock: mutex=0xc0101588
pthread_mutex_timedlock: Returning 0
pthread_mutex_unlock: mutex=0xc0101588
pthread_mutex_unlock: Returning 0
pthread_mutex_timedlock: Returning 0
pthread_mutex_timedlock: mutex=0xc0101588
pthread_mutex_unlock: mutex=0xc0101588
pthread_mutex_unlock: Returningpthread_mutex_timedlock: Returning 0
 0
pthread_mutex_timedlock: mutex=0xc0101588
pthread_mutex_unlock: mutex=0xc0101588
pthread_mutex_unlock: Rpthread_mutex_timedlock: Returning 0eturning 0
pthread_mutex_timedlock: mutex=0xc0101588

pthread_mutex_unlock: mutex=0xc0101588
pthread_mutex_unlock: Returning 0
pthread_mutex_timedlock: Retpthread_mutex_timedlock: mutex=0xc0101588
urning 0
pthread_mutex_unlock: mutex=0xc0101588
pthread_mutex_unlock: Returning 0
pthread_mutex_timedlock: Returning 0
pthread_mutex_timedlock: mutex=0xc0101588
pthread_mutex_unlock: mutex=0xc0101588
pthread_mutex_timedlock: Returning 0
pthread_mutex_unlock: Returning 0
pthread_mutex_timedlock: mutex=0xc0101588
pthread_mutex_unlock: mutex=0xc0101588
pthread_mutex_unlock: Returning 0
pthread_mutex_timedlock: mutex=0xc0101588
pthread_mutex_timedlock: Returning 0
pthread_mutex_unlock: mutex=0xc0101588
pthread_mutex_unlock: Returning 0
pthread_mutex_timedlock: mutex=0xc0101588
pthread_mutex_timedlock: Returning 0
pthread_mutex_unlock: mutex=0xc0101588
pthread_mutex_unlock: Returning 0
pthread_mutex_timedlock: mutex=pthread_mutex_timedlock: Returning 0
0xc0101588
pthread_mutex_unlock: mutex=0xc0101588
pthread_mutex_unlock: Returning 0
pthread_mutex_timedlock: mutex=0xc0101588
pthread_mutex_timedlock: Returning 0
pthread_mutex_unlock: mutex=0xc0101588
pthread_mutex_unlock: Returning 0
pthread_mutex_timedlock: mutex=0xc0101588
pthread_mutex_timedlock: Returning 0
pthread_mutex_unlock: mutex=0xc0101588
pthread_mutex_unlock: Returning 0
pthread_mutex_timedlock: mutex=0xc0101588
pthread_mutex_timedlock: Returning 0
pthread_mutex_unlock: mutex=0xc0101588
pthread_mutex_unlock: Returning 0
pthread_mutex_timedlock: Returning 0
pthread_mutex_timedlock: mutex=0xc0101588
pthread_mutex_unlock: mutex=0xc0101588
pthread_mutex_unlock: Returningpthread_mutex_timedlock: Returning 0
 0
pthread_mutex_timedlock: mutex=0xc0101588
pthread_mutex_unlock: mutex=0xc0101588
pthread_mutex_unlock: Retpthread_mutex_timedlock: Returning 0
urning 0
pthread_mutex_timedlock: mutex=0xc0101588
pthread_mutex_unlock: mutex=0xc0101588
pthread_mutex_unlock: Returning 0
pthread_mutex_timedlock: Rpthread_mutex_timedlock: mutex=0xc0101588
eturning 0
pthread_mutex_unlock: mutex=0xc0101588
pthread_mutex_unlock: Returning 0
pthread_mutex_timedlock: Returning 0
pthread_mutex_timedlock: mutex=0xc0101588
pthread_mutex_unlock: mutex=0xc0101588
pthread_mutex_unlock: Returning 0
pthread_mutex_timedlock: Returning 0
pthread_mutex_timedlock: mutex=0xc0101588
pthread_mutex_unlock: mutex=0xc0101588
pthread_mutex_unlock: Returning 0
pthread_mutex_timedlock: mutex=0xc010158pthread8
_mutex_timedlock: Returning 0
pthread_mutex_unlock: mutex=0xc0101588
pthread_mutex_unlock: Returning 0
pthread_mutex_timedlock: mutex=0xc010158pthread_mutex_timedlock: Returning 0
8
pthread_mutex_unlock: mutex=0xc0101588
pthread_mutex_unlock: Returning 0
pthread_mutex_timedlock:pthread_mutex_timedlock: Returning 0
 mutex=0xc0101588
pthread_mutex_unlock: mutex=0xc0101588
pthread_mutex_unlock: Returning 0
pthread_mutex_timedlock: mpthread_mutex_timedlock: Returning 0
utex=0xc0101588
pthread_mutex_unlock: mutex=0xc0101588
pthread_mutex_unlock: Returning 0
pthread_mutex_timedlock: mutex=0xc0101588
pthread_mutex_timedlock: Returning 0
pthread_mutex_unlock: mutex=0xc0101588
pthread_mutex_unlock: Returning 0
pthread_mutex_timedlock: mutex=0xc0101588
pthread_mutex_timedlock: Returning 0
pthread_mutex_unlock: mutex=0xc0101588
pthread_mutex_unlock: Returning 0
pthread_mutex_timedlock: Returning 0
pthread_mutex_timedlock: mutex=0xc0101588
pthread_mutex_unlock: mutex=0xc0101588
pthread_mutex_unlock: Returning pthread_mutex_timedlock: Returning 0
0
pthread_mutex_timedlock: mutex=0xc0101588
pthread_mutex_unlock: mutex=0xc0101588
pthread_mutex_unlock:pthread_mutex_timedlock: Returning 0
 Returning 0
pthread_mutex_timedlock: mutex=0xc0101588
pthread_mutex_unlock: mutex=0xc0101588
pthread_mutex_unlock: Returning 0
pthread_mutex_timedlockpthread_mutex_timedlock: mutex=0xc0101588
: Returning 0
pthread_mutex_unlock: mutex=0xc0101588
pthread_mutex_unlock: Returning 0
pthread_mutex_timedlock: Returning 0
pthread_mutex_timedlock: mutex=0xc0101588
pthread_mutex_unlock: mutex=0xc0101588
pthread_mutex_unlock: Returning 0
pthread_mutex_timedlock: Returning 0
pthread_mutex_timedlock: mutex=0xc0101588
pthread_mutex_unlock: mutex=0xc0101588
pthread_mutex_unlock: Returning 0
pthread_mutex_timedlock: mutex=0xc0101pthre588
ad_mutex_timedlock: Returning 0
pthread_mutex_unlock: mutex=0xc0101588
pthread_mutex_unlock: Returning 0
pthread_mutex_timedlock: mutex=0xc01pthread_mutex_timedlock: Returning 0
01588
pthread_mutex_unlock: mutex=0xc0101588
pthread_mutex_unlock: Returning 0
pthread_mutex_timedlock:pthread_mutex_timedlock: Returning 0
 mutex=0xc0101588
pthread_mutex_unlock: mutex=0xc0101588
pthread_mutex_unlock: Returning 0
pthread_mutex_timedlock: mutex=0xc0101588
pthread_mutex_timedlock: Returning 0
pthread_mutex_unlock: mutex=0xc0101588
pthread_mutex_unlock: Returning 0
pthread_mutex_timedlock: mutex=0xc0101588
pthread_mutex_timedlock: Returning 0
pthread_mutex_unlock: mutex=0xc0101588
pthread_mutex_unlock: Returning 0
pthread_mutex_timedlock: mutex=0xc0101588
pthread_mutex_timedlock: Returning 0
pthread_mutex_unlock: mutex=0xc0101588
pthread_mutex_unlock: Returning 0
pthread_mutex_timedlock: Returning 0
pthread_mutex_timedlock: mutex=0xc0101588
pthread_mutex_unlock: mutex=0xc0101588
pthread_mutex_unlock: Returnipthread_mutex_timedlock: Returning 0
ng 0
pthread_mutex_timedlock: mutex=0xc0101588
pthread_mutex_unlock: mutex=0xc0101588
pthread_mutex_unlock: Returning 0
pthread_mutex_timedlock: Returningpthread_mutex_timedlock: mutex=0xc0101588
 0
pthread_mutex_unlock: mutex=0xc0101588
pthread_mutex_unlock: Returning 0
pthread_mutex_timedlock: Returning 0
pthread_mutex_timedlock: mutex=0xc0101588
pthread_mutex_unlock: mutex=0xc0101588
pthread_mutex_timedlock: Returning 0
pthread_mutex_unlock: Returning 0
pthread_mutex_timedlock: mutex=0xc0101588
pthread_mutex_unlock: mutex=0xc0101588
pthread_mutex_unlock: Returning 0
pthread_mutex_timedlock: Returning 0
nx_pthread_exit: exit_value=0
pthread_completejoin: pid=10 exit_value=0
nxtask_exit: ostest pid=10,TCB=0x80409af0
riscv_exception: EXCEPTION: Load access fault. MCAUSE: 0000000000000005, EPC: 000000008021890e, MTVAL: 0000000000000000
riscv_exception: Segmentation fault in PID 7: ostest
pthread_completejoin: pid=12 exit_value=0xffffffffffffffff
nxtask_exit: ostest pid=7,TCB=0x8040c830
ostest_main: Exiting with status -1
nxtask_exit: ostest pid=6,TCB=0x80409740
nsh>
```

</details>

Screen recording:

[![asciicast](https://asciinema.org/a/P4kzXcnL4g0A0LIiiOLtsG779.svg)](https://asciinema.org/a/P4kzXcnL4g0A0LIiiOLtsG779)

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.