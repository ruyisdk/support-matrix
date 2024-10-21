---
sys: nuttx
sys_ver: null
sys_var: null

status: basic
last_update: 2024-06-21
---

# NuttX on Milk-V Duo S Test Report

## Test Environment

### Operating System Information

- Debian Linux Image + U-Boot: https://github.com/Fishwaldo/sophgo-sg200x-debian/releases
- Toolchain: xPack https://github.com/xpack-dev-tools/riscv-none-elf-gcc-xpack/releases
- dtb file: https://github.com/lupyuen2/wip-nuttx/releases/download/sg2000-1/cv181x_milkv_duos_sd.dtb
- Reference Installation Document: https://nuttx.apache.org/docs/latest/quickstart/install.html


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

Debian based:
```bash
sudo apt install \
bison flex gettext texinfo libncurses5-dev libncursesw5-dev xxd \
gperf automake libtool pkg-config build-essential gperf genromfs \
libgmp-dev libmpc-dev libmpfr-dev libisl-dev binutils-dev libelf-dev \
libexpat-dev gcc-multilib g++-multilib picocom u-boot-tools util-linux

sudo apt install kconfig-frontends
# pip install kconfiglib
```

Fedora / RPM based:
```bash
sudo dnf install \
bison flex gettext texinfo ncurses-devel ncurses ncurses-compat-libs \
gperf automake libtool pkgconfig @development-tools gperf genromfs \
gmp-devel mpfr-devel libmpc-devel isl-devel binutils-devel elfutils-libelf-devel \
expat-devel gcc-c++ g++ picocom uboot-tools util-linux

pip install kconfiglib
# Or install from source:
# git clone https://bitbucket.org/nuttx/tools.git
# cd tools/kconfig-frontends
# ./configure --enable-mconf --disable-nconf --disable-gconf --disable-qconf
# aclocal
# automake
# make
# sudo make install
```

Arch / pacman based:
```shell
sudo pacman -S --needed base-devel ncurses5-compat-libs gperf pkg-config gmp libmpc mpfr libelf expat picocom uboot-tools util-linux git wget libisl
# AUR packages only, use any AUR helper as you wish
paru -S kconfig-frontends genromfs
# yay -S kconfig-frontends genromfs
```

### Retrieve the Source Code

```shell
mkdir nuttxspace
cd nuttxspace
git clone https://github.com/apache/nuttx.git nuttx
git clone https://github.com/apache/nuttx-apps apps
```

### Configure Toolchain and Build NuttX

The xPack toolchain is needed for the compilation, get the toolchain first from the Github, suggest 13.3.0 version as it has been tested, change the version to match your system:
```bash
wget https://github.com/xpack-dev-tools/riscv-none-elf-gcc-xpack/releases/download/v11.5.0-1/xpack-riscv-none-elf-gcc-13.3.0-1-linux-x64.tar.gz
tar -xvzf xpack-riscv-none-elf-gcc-13.3.0-1-linux-x64.tar.gz
```

Export it into your PATH:
```bash
export PATH=/path/to/toolchain/you/untar:$PATH
```


Then, build the Nuttx kernel:
```shell
cd nuttx
tools/configure.sh milkv_duos:nsh
make -j$(nproc)
```

Then, build the file system:
```bash
make export
pushd ../apps
tools/mkimport.sh -z -x ../nuttx/nuttx-export-*.tar.gz
make import
popd
genromfs -f initrd -d ../apps/bin -V "NuttXBootVol"

```


Finally , padding the image:
```bash
head -c 65536 /dev/zero >/tmp/nuttx.pad
cat nuttx.bin /tmp/nuttx.pad initrd >Image-sg2000
```

### Booting NuttX RTOS from TFTP Server

First, flash the Debian image onto the storage card.

```shell
wget https://github.com/Fishwaldo/sophgo-sg200x-debian/releases/download/v1.4.0/duos_sd.img.lz4
lz4 -d duos_sd.img.lz4
sudo dd if=duos_sd.img of=/dev/sdX bs=1M status=progress
```

The storage card is now ready. Insert it into the development board.

Start a TFTP server on your computer. Ensure both the compiled Image (located in the NuttX source directory) and dtb are accessible by the TFTP server.

Refer to: [Arch Wiki/TFTP](https://wiki.archlinux.org/title/TFTP) for TFTP server configuration. Generally speaking, you can try tftpd:
```bash
systemctl start tftpd
```

On Windows, you may consider using [Tftpd64](http://tftpd32.jounin.net).

Put the image file and dtb file under the tftp service foder, like for tftpd, it's `/srv/tftp`:
```bash
wget https://github.com/lupyuen2/wip-nuttx/releases/download/sg2000-1/cv181x_milkv_duos_sd.dtb
cp Image-sg2000 /path/to/tftp/folder
cp cv181x_milkv_duos_sd.dtb /path/to/tftp/folder
```

Connect the UART debug cable, power on the development board, and press any key when prompted (`Hit any key to stop autoboot`) to interrupt U-Boot. Manually configure U-Boot to boot NuttX from TFTP:

If you need DHCP to get the IP address, run `dhcp` then interrupt the start procedure to maintain the ip address.

```shell
setenv tftp_server your_tftp_server_ip
dhcp ${kernel_addr_r} ${tftp_server}:Image-sg2000
tftpboot ${fdt_addr_r} ${tftp_server}:cv181x_milkv_duos_sd.dtb
fdt addr ${fdt_addr_r}
booti ${kernel_addr_r} - ${fdt_addr_r}
```


## Expected Results

The system should boot normally, and you should be able to access the NuttX shell via the serial connection.

## Actual Results

The system booted successfully, and the NuttX shell was accessible via the serial connection.

Commands like `uname`, `ls`, and `ostest` were executed successfully.

### Boot Information

Boot log:
```log
Starting kernel ...

ABC
NuttShell (NSH) NuttX-12.6.0-RC1
nsh> help
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
NuttX 12.6.0-RC1 98f5d6adc5 Jul 29 2024 00:32:01 risc-v milkv_duos
nsh> cat /proc/cpuinfo
processor       : 0
hart            : 0
isa             : rv64imafdc
mmu             : none
nsh> 
 

```


Screen recording:

Part 1:
[![asciicast](https://asciinema.org/a/8wvErVrySR04Ri18rPJ99qai9.svg)](https://asciinema.org/a/8wvErVrySR04Ri18rPJ99qai9)

Part 2:
[![asciicast](https://asciinema.org/a/loBvsK69TBtZmicjdzqHX2B9z.svg)](https://asciinema.org/a/loBvsK69TBtZmicjdzqHX2B9z)

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.