---
sys: nuttx
sys_ver: "12.9.0"
sys_var: null

status: basic
last_update: 2025-04-26
---

# NuttX Milk-V Mars Test Report

## Test Environment

### Hardware Information

- Development Board: Milk-V Mars (8GB RAM)
- Other Hardware:
  - A USB power adapter and A USB-A to C or C to C cable
  - A microSD card
  - A USB to UART debugger (e.g., CH340, CH341, FT2232, etc.)

### Operating System Information

- OS Version: NuttX 12.9.0
- Download Link:
  - <https://nuttx.apache.org/download/>
  - <https://www.apache.org/dyn/closer.lua/nuttx/12.9.0/apache-nuttx-12.9.0.tar.gz>
  - <https://www.apache.org/dyn/closer.lua/nuttx/12.9.0/apache-nuttx-apps-12.9.0.tar.gz>
- Reference Installation Document:
  - <https://milkv.io/zh/docs/mars/getting-started/boot>
  - <https://nuttx.apache.org/docs/latest/platforms/risc-v/jh7110/boards/star64/index.html>

## Installation Steps

### Flashing the Image

Use `gzip` command to decompress the image,  and then use `dd` command or `balenaEtcher` software to flash the image to the microSD card.

Here, `/dev/sdc` corresponds to the storage device.

```bash
wget https://downloads.openwrt.org/releases/24.10.1/targets/starfive/generic/openwrt-24.10.1-starfive-generic-visionfive2-v1.3b-ext4-sdcard.img.gz

gzip -d openwrt-24.10.1-starfive-generic-visionfive2-v1.3b-ext4-sdcard.img.gz

sudo dd if=openwrt-24.10.1-starfive-generic-visionfive2-v1.3b-ext4-sdcard.img of=/dev/sdX bs=1M status=progress

sync
```

### Prepare the environment and toolchain

```bash
saicogn@saicogn:~$ mkdir nuttx_mars && cd nuttx_mars

saicogn@saicogn:~/nuttx_mars$ sudo apt install bison flex gettext texinfo libncurses5-dev libncursesw5-dev xxd git gperf automake libtool pkg-config build-essential gperf genromfs libgmp-dev libmpc-dev libmpfr-dev libisl-dev binutils-dev libelf-dev libexpat1-dev gcc-multilib g++-multilib picocom u-boot-tools util-linux

saicogn@saicogn:~/nuttx_mars$ sudo apt install kconfig-frontends

saicogn@saicogn:~/nuttx_mars$ wget https://static.dev.sifive.com/dev-tools/freedom-tools/v2020.12/riscv64-unknown-elf-toolchain-10.2.0-2020.12.8-x86_64-linux-ubuntu14.tar.gz

saicogn@saicogn:~/nuttx_mars$ tar -xvf riscv64-unknown-elf-toolchain-10.2.0-2020.12.8-x86_64-linux-ubuntu14.tar.gz

saicogn@saicogn:~/nuttx_mars/$ export PATH=/home/saicogn/nuttx_mars/riscv64-unknown-elf-toolchain-10.2.0-2020.12.8-x86_64-linux-ubuntu14/bin:$PATH

saicogn@saicogn:~/nuttx_mars/$ riscv64-unknown-elf-gcc -v
Using built-in specs.
COLLECT_GCC=riscv64-unknown-elf-gcc
COLLECT_LTO_WRAPPER=/home/saicogn/nuttx_mars/riscv64-unknown-elf-toolchain-10.2.0-2020.12.8-x86_64-linux-ubuntu14/bin/../libexec/gcc/riscv64-unknown-elf/10.2.0/lto-wrapper
Target: riscv64-unknown-elf
Configured with: /scratch/jenkins/workspace/tpp-freedom-tools/tpp03--build-binary-packages--parameterized/obj/x86_64-linux-ubuntu14/build/riscv64-unknown-elf-gcc/riscv-gcc/configure --target=riscv64-unknown-elf --host=x86_64-linux-gnu --prefix=/scratch/jenkins/workspace/tpp-freedom-tools/tpp03--build-binary-packages--parameterized/obj/x86_64-linux-ubuntu14/install/riscv64-unknown-elf-gcc-10.2.0-2020.12.8-x86_64-linux-ubuntu14 --with-pkgversion='SiFive GCC-Metal 10.2.0-2020.12.8' --with-bugurl=https://github.com/sifive/freedom-tools/issues --disable-shared --disable-threads --enable-languages=c,c++ --enable-tls --with-newlib --with-sysroot=/scratch/jenkins/workspace/tpp-freedom-tools/tpp03--build-binary-packages--parameterized/obj/x86_64-linux-ubuntu14/install/riscv64-unknown-elf-gcc-10.2.0-2020.12.8-x86_64-linux-ubuntu14/riscv64-unknown-elf --with-native-system-header-dir=/include --disable-libmudflap --disable-libssp --disable-libquadmath --disable-libgomp --disable-nls --disable-tm-clone-registry --src=../riscv-gcc --with-system-zlib --enable-checking=yes --enable-multilib --with-abi=lp64d --with-arch=rv64imafdc CFLAGS=-O2 CXXFLAGS=-O2 'CFLAGS_FOR_TARGET=-Os -mcmodel=medany' 'CXXFLAGS_FOR_TARGET=-Os -mcmodel=medany'
Thread model: single
Supported LTO compression algorithms: zlib
gcc version 10.2.0 (SiFive GCC-Metal 10.2.0-2020.12.8) 
```

### Download the source code and extract them to obtain the directories of `nuttx` and `apps`

```bash
saicogn@saicogn:~/nuttx_mars$ curl -L https://www.apache.org/dyn/closer.lua/nuttx/12.9.0/apache-nuttx-apps-12.9.0.tar.gz?action=download -o nuttx-apps-12.9.0.tar.gz

saicogn@saicogn:~/nuttx_mars$ curl -L https://www.apache.org/dyn/closer.lua/nuttx/12.9.0/apache-nuttx-12.9.0.tar.gz?action=download -o nuttx-12.9.0.tar.gz

saicogn@saicogn:~/nuttx_mars$ tar -xvf nuttx-12.9.0.tar.gz 

saicogn@saicogn:~/nuttx_mars$ tar -xvf nuttx-apps-12.9.0.tar.gz
```

### Build the NuttX image

1. Build the NuttX kernel file `nuttx.bin`.

    ```bash
    saicogn@saicogn:~/nuttx_mars$ cd nuttx

    saicogn@saicogn:~/nuttx_mars/nuttx$ make distclean

    saicogn@saicogn:~/nuttx_mars/nuttx$ tools/configure.sh star64:nsh
        Copy files
    Select CONFIG_HOST_LINUX=y
    Refreshing...
    ...
    mkkconfig in /home/saicogn/nuttx_mars/apps
    #
    # configuration written to .config
    #
    saicogn@saicogn:~/nuttx_mars/nuttx$ 

    saicogn@saicogn:~/nuttx_mars/nuttx$ make
    Create version.h
    LN: platform/board to /home/saicogn/nuttx_mars/apps/platform/dummy
    Register: hello
    Register: init
    Register: sh
    Register: getprime
    CPP:  /home/saicogn/nuttx_mars/nuttx/boards/risc-v/jh7110/star64/scripts/ld.script-> /home/saicogn/nuttx_mars/nuttx/boards/risc-v/jLD: nuttx
    Memory region         Used Size  Region Size  %age Used
              kflash:      177940 B         2 MB      8.48%
              ksram:         32 KB         2 MB      1.56%
              pgram:          0 GB         4 MB      0.00%
            ramdisk:          0 GB        16 MB      0.00%
    CP: nuttx.hex

    saicogn@saicogn:~/nuttx_mars/nuttx$ file nuttx
    nuttx: ELF 64-bit LSB executable, UCB RISC-V, RVC, double-float ABI, version 1 (SYSV), statically linked, with debug_info, not stripped

    saicogn@saicogn:~/nuttx_mars/nuttx$ riscv64-unknown-elf-objcopy -O binary nuttx nuttx.bin
    ```

2. Build the NuttX Apps Filesystem `initrd` as the Initial RAM Disk.

    ```bash
    saicogn@saicogn:~/nuttx_mars/nuttx$ make export

    saicogn@saicogn:~/nuttx_mars/nuttx$ pushd ../apps
    ~/nuttx_mars/apps ~/nuttx_mars/nuttx

    saicogn@saicogn:~/nuttx_mars/apps$ tools/mkimport.sh -z -x ../nuttx/nuttx-export-*.tar.gz

    saicogn@saicogn:~/nuttx_mars/apps$ make import
    
    saicogn@saicogn:~/nuttx_mars/apps$ popd
    ~/nuttx_mars/nuttx

    saicogn@saicogn:~/nuttx_mars/nuttx$ genromfs -f initrd -d ../apps/bin -V "NuttXBootVol"

    saicogn@saicogn:~/nuttx_mars/nuttx$ file initrd
    initrd: romfs filesystem, version 1 1028928 bytes, named NuttXBootVol.
    ```

3. Download the official Device Tree file to generate the NuttX `Flat Image Tree (FIT)` image file.
    - Download Device Tree file `.dtb`.

        ```bash
        saicogn@saicogn:~/nuttx_mars/nuttx$ wget https://github.com/starfive-tech/VisionFive2/releases/download/JH7110_VF2_515_v5.11.3/jh7110-visionfive-v2.dtb
        ```

    - Inside the nuttx folder, create a FIT description text file named `nuttx.its` with the following content.

        ```bash
        saicogn@saicogn:~/nuttx_mars/nuttx$ cat << EOF > nuttx.its
        /dts-v1/;

        / {
          description = "NuttX FIT image";
          #address-cells = <2>;

          images {
            vmlinux {
              description = "vmlinux";
              data = /incbin/("./nuttx.bin");
              type = "kernel";
              arch = "riscv";
              os = "linux";
              load = <0x0 0x40200000>;
              entry = <0x0 0x40200000>;
              compression = "none";
            };

            ramdisk {
              description = "buildroot initramfs";
              data = /incbin/("./initrd");
              type = "ramdisk";
              arch = "riscv";
              os = "linux";
              load = <0x0 0x46100000>;
              compression = "none";
              hash-1 {
                algo = "sha256";
              };
            };

            fdt {
              data = /incbin/("./jh7110-visionfive-v2.dtb");
              type = "flat_dt";
              arch = "riscv";
              load = <0x0 0x46000000>;
              compression = "none";
              hash-1 {
                algo = "sha256";
              };
            };
          };

          configurations {
            default = "nuttx";

            nuttx {
              description = "NuttX";
              kernel = "vmlinux";
              fdt = "fdt";
              loadables = "ramdisk";
            };
          };
        };
        EOF

        saicogn@saicogn:~/nuttx_mars/nuttx$ file nuttx.its 
        uttx.its: Device Tree File (v1), ASCII text
        ```

    - Use `mkimage` of U-Boot to package the NuttX Kernel, Initial RAM Disk and Device Tree into a Flat Image Tree file `starfiveu.fit`.

      ```bash
      saicogn@saicogn:~/nuttx_mars/nuttx$ mkimage -f nuttx.its -A riscv -O linux -T flat_dt starfiveu.fit

      FIT description: NuttX FIT image
      Created:         Fri Apr 25 16:20:00 2025
      Image 0 (vmlinux)
        Description:  vmlinux
        Created:      Fri Apr 25 16:20:00 2025
        Type:         Kernel Image
        Compression:  uncompressed
        Data Size:    2098704 Bytes = 2049.52 KiB = 2.00 MiB
        Architecture: RISC-V
        OS:           Linux
        Load Address: 0x40200000
        Entry Point:  0x40200000
      Image 1 (ramdisk)
        Description:  buildroot initramfs
        Created:      Fri Apr 25 16:20:00 2025
        Type:         RAMDisk Image
        Compression:  uncompressed
        Data Size:    1029120 Bytes = 1005.00 KiB = 0.98 MiB
        Architecture: RISC-V
        OS:           Linux
        Load Address: 0x46100000
        Entry Point:  unavailable
        Hash algo:    sha256
        Hash value:   97908d825b8efa8413a1094bd659c9ebe3283309e995062da40030ce6f0b1aff
      Image 2 (fdt)
        Description:  unavailable
        Created:      Fri Apr 25 16:20:00 2025
        Type:         Flat Device Tree
        Compression:  uncompressed
        Data Size:    52430 Bytes = 51.20 KiB = 0.05 MiB
        Architecture: RISC-V
        Load Address: 0x46000000
        Hash algo:    sha256
        Hash value:   9537d7c8ea049fa11e59710e7eb3dcbf79cf028829bda12709552c0ffc3a646f
      Default Configuration: 'nuttx'
      Configuration 0 (nuttx)
        Description:  NuttX
        Kernel:       vmlinux
        FDT:          fdt
        Loadables:    ramdisk        
        
      saicogn@saicogn:~/nuttx_mars/nuttx$ file starfiveu.fit 
      starfiveu.fit: Device Tree Blob version 17, size=3182154, boot CPU=0, string block size=118, DT structure block size=3181076
      ```

### Write the official image to the MicroSD card and replace its FIT file with NuttX

1. Download and write the official image to the MicroSD card.

    Use `dd` command or `balenaEtcher` software to flash the image to the microSD card.

    Here, `/dev/sdc` corresponds to the storage device.

    ```bash
    saicogn@saicogn:~/nuttx_mars/nuttx$ wget https://github.com/starfive-tech/VisionFive2/releases/download/JH7110_VF2_515_v5.11.3/sdcard.img

    sudo dd if=sdcard.img of=/dev/sdX bs=1M status=progress

    sync
    ```

2. Mount the MicroSD card and replace the `starfiveu.fit` file in the third partition with the file generated above.

    If the MicroSD card is not automatically mounted, it needs to be manually mounted using `mount`

    ```bash
    sudo mount /dev/your/sdcard/partition3 /media/saicogn/
    ```

    Overwrite the `starfiveu.fit` file

    ```bash
    saicogn@saicogn:~/nuttx_mars/nuttx$ df -ha
    Filesystem      Size  Used Avail Use% Mounted on
    /dev/sdc3       292M  3.1M  289M   2% /media/saicogn/F01E-258D
    /dev/sdc4       459M  272M  159M  64% /media/saicogn/rootfs

    saicogn@saicogn:~/nuttx_mars/nuttx$ ls /media/saicogn/F01E-258D/ -lh
    total 135M
    -rw-r--r-- 1 saicogn saicogn 1.3K Mar 15  2024  jh7110_uEnv.txt
    -rw-r--r-- 1 saicogn saicogn 135M Mar 15  2024  starfiveu.fit
    drwxr-xr-x 2 saicogn saicogn 8.0K Apr 26  2025 'System Volume Information'
    -rw-r--r-- 1 saicogn saicogn 1.5K Mar 15  2024  vf2_nvme_uEnv.txt
    -rw-r--r-- 1 saicogn saicogn 1.3K Mar 15  2024  vf2_uEnv.txt

    saicogn@saicogn:~/nuttx_mars/nuttx$ cp starfiveu.fit /media/saicogn/F01E-258D/ -f

    saicogn@saicogn:~/nuttx_mars/nuttx$ ls /media/saicogn/F01E-258D/ -lh
    total 3.1M
    -rw-r--r-- 1 saicogn saicogn 1.3K Mar 15  2024  jh7110_uEnv.txt
    -rw-r--r-- 1 saicogn saicogn 3.1M Apr 25 23:19  starfiveu.fit
    drwxr-xr-x 2 saicogn saicogn 8.0K Apr 26  2025 'System Volume Information'
    -rw-r--r-- 1 saicogn saicogn 1.5K Mar 15  2024  vf2_nvme_uEnv.txt
    -rw-r--r-- 1 saicogn saicogn 1.3K Mar 15  2024  vf2_uEnv.txt

    saicogn@saicogn:~/nuttx_mars/nuttx$ sync
    ```

### Logging into the System

Logging into the system via the serial port.

Default username: `root` (automatic login)

No password by default

Since the image does not have SPL and U-Boot, the dip switch of the board needs to be set to `00` in order to use the built-in SPL and U-Boot in the SPI-Flash on the board to boot the OpenWrt image in the MicroSD card.

## Expected Results

The system should boot normally, allowing login via the onboard serial port.

## Actual Results

The system starts normally and the output is successfully viewed through the serial port.

### Boot Information

```log
U-Boot SPL 2021.10 (Mar 14 2024 - 19:21:18 +0800)
LPDDR4: 8G version: g8ad50857.
Trying to boot from MMC2

OpenSBI v1.2
   ____                    _____ ____ _____
  / __ \                  / ____|  _ \_   _|
 | |  | |_ __   ___ _ __ | (___ | |_) || |
 | |  | | '_ \ / _ \ '_ \ \___ \|  _ < | |
 | |__| | |_) |  __/ | | |____) | |_) || |_
  \____/| .__/ \___|_| |_|_____/|___/_____|
        | |
        |_|

Platform Name             : StarFive VisionFive V2
Platform Features         : medeleg
Platform HART Count       : 5
Platform IPI Device       : aclint-mswi
Platform Timer Device     : aclint-mtimer @ 4000000Hz
Platform Console Device   : uart8250
Platform HSM Device       : ---
Platform PMU Device       : ---
Platform Reboot Device    : pm-reset
Platform Shutdown Device  : pm-reset
Platform Suspend Device   : ---
Firmware Base             : 0x40000000
Firmware Size             : 392 KB
Firmware RW Offset        : 0x40000
Runtime SBI Version       : 1.0

Domain0 Name              : root
Domain0 Boot HART         : 1
Domain0 HARTs             : 0*,1*,2*,3*,4*
Domain0 Region00          : 0x0000000002000000-0x000000000200ffff M: (I,R,W) S/U: ()
Domain0 Region01          : 0x0000000040000000-0x000000004003ffff M: (R,X) S/U: ()
Domain0 Region02          : 0x0000000040040000-0x000000004007ffff M: (R,W) S/U: ()
Domain0 Region03          : 0x0000000000000000-0xffffffffffffffff M: (R,W,X) S/U: (R,W,X)
Domain0 Next Address      : 0x0000000040200000
Domain0 Next Arg1         : 0x0000000042200000
Domain0 Next Mode         : S-mode
Domain0 SysReset          : yes
Domain0 SysSuspend        : yes

Boot HART ID              : 1
Boot HART Domain          : root
Boot HART Priv Version    : v1.11
Boot HART Base ISA        : rv64imafdcbx
Boot HART ISA Extensions  : none
Boot HART PMP Count       : 8
Boot HART PMP Granularity : 4096
Boot HART PMP Address Bits: 34
Boot HART MHPM Count      : 2
Boot HART MIDELEG         : 0x0000000000000222
Boot HART MEDELEG         : 0x000000000000b109


U-Boot 2021.10 (Mar 14 2024 - 19:21:18 +0800), Build: jenkins-github_visionfive2-23

CPU:   rv64imacu_zba_zbb
Model: StarFive VisionFive V2
DRAM:  8 GiB
MMC:   sdio0@16010000: 0, sdio1@16020000: 1
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

In:    serial
Out:   serial
Err:   serial
Model: StarFive VisionFive V2
Net:   eth0: ethernet@16030000, eth1: ethernet@16040000
Hit any key to stop autoboot:  0
switch to partitions #0, OK
mmc1 is current device
Try booting from MMC1 ...
1235 bytes read in 7 ms (171.9 KiB/s)
3182154 bytes read in 146 ms (20.8 MiB/s)
## Loading kernel from FIT Image at 60000000 ...
   Using 'nuttx' configuration
   Trying 'vmlinux' kernel subimage
     Description:  vmlinux
     Type:         Kernel Image
     Compression:  uncompressed
     Data Start:   0x600000b4
     Data Size:    2098704 Bytes = 2 MiB
     Architecture: RISC-V
     OS:           Linux
     Load Address: 0x40200000
     Entry Point:  0x40200000
   Verifying Hash Integrity ... OK
## Loading fdt from FIT Image at 60000000 ...
   Using 'nuttx' configuration
   Trying 'fdt' fdt subimage
     Description:  unavailable
     Type:         Flat Device Tree
     Compression:  uncompressed
     Data Start:   0x602fbc44
     Data Size:    52430 Bytes = 51.2 KiB
     Architecture: RISC-V
     Load Address: 0x46000000
     Hash algo:    sha256
     Hash value:   9537d7c8ea049fa11e59710e7eb3dcbf79cf028829bda12709552c0ffc3a646f
   Verifying Hash Integrity ... sha256+ OK
   Loading fdt from 0x602fbc44 to 0x46000000
   Booting using the fdt blob at 0x46000000
## Loading loadables from FIT Image at 60000000 ...
   Trying 'ramdisk' loadables subimage
     Description:  buildroot initramfs
     Type:         RAMDisk Image
     Compression:  uncompressed
     Data Start:   0x60200778
     Data Size:    1029120 Bytes = 1005 KiB
     Architecture: RISC-V
     OS:           Linux
     Load Address: 0x46100000
     Entry Point:  unavailable
     Hash algo:    sha256
     Hash value:   97908d825b8efa8413a1094bd659c9ebe3283309e995062da40030ce6f0b1aff
   Verifying Hash Integrity ... sha256+ OK
   Loading loadables from 0x60200778 to 0x46100000
   Loading Kernel Image
Booting kernel in
## Flattened Device Tree blob at 46000000
   Booting using the fdt blob at 0x46000000
   Using Device Tree in place at 0000000046000000, end 000000004600ffff

Starting kernel ...

clk u2_dw_i2c_clk_core already disabled
clk u2_dw_i2c_clk_apb already disabled
clk u5_dw_i2c_clk_core already disabled
clk u5_dw_i2c_clk_apb already disabled
ABC
NuttShell (NSH) NuttX-12.9.0
nsh> 

nsh> cd /proc

nsh> cat cpuinfo
processor       : 0
hart            : 0
isa             : rv64imafdc
mmu             : none

nsh> cat version
NuttX version 12.9.0 7c95e3c613 Apr 25 2025 01:45:35 star64:nsh

nsh> help
help usage:  help [-v] [<cmd>]

    .           cp          exit        ls          rm          uname
    [           cmp         expr        mkdir       rmdir       umount
    ?           dirname     false       mkrd        set         unset
    alias       dd          fdinfo      mount       sleep       uptime
    unalias     df          free        mv          source      usleep
    basename    dmesg       help        pidof       test        watch
    break       echo        hexdump     printf      time        xd
    cat         env         kill        ps          true        wait
    cd          exec        pkill       pwd         truncate

nsh> ps
  PID GROUP PRI POLICY   TYPE    NPX STATE    EVENT     SIGMASK            STACK    USED FILLED COMMAND
    0     0   0 FIFO     Kthread   - Ready              0000000000000000 0003056 0000760  24.8%  Idle_Task
    1     0 100 RR       Kthread   - Waiting  Semaphore 0000000000000000 0001968 0000736  37.3%  lpwork 0x40400100 0x40400148
    3     3 100 RR       Task      - Running            0000000000000000 0003008 0001880  62.5%  /system/bin/init
```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
