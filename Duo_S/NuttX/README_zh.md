# NuttX on Milk-V Duo S 测试报告

## 测试环境

### 操作系统信息

- Debian Linux Image + U-Boot: https://github.com/Fishwaldo/sophgo-sg200x-debian/releases
- Toolchain: xPack https://github.com/xpack-dev-tools/riscv-none-elf-gcc-xpack/releases
- dtb file: https://github.com/lupyuen2/wip-nuttx/releases/download/sg2000-1/cv181x_milkv_duos_sd.dtb
- Reference Installation Document: https://nuttx.apache.org/docs/latest/quickstart/install.html

### 硬件信息

- Milk-V Duo S (512M, SG2000)
- USB-A to C 或 USB C to C 线缆一条，用于给开发板供电
- microSD 卡一张，用于启动
- USB 读卡器一个，用于为microSD烧录
- USB to UART 调试器一个（如：CP2102, FT2232 等，使用 CH340/341 系列开始会出现乱码，属于预期现象）
- 杜邦线三根，用于uart接口
- 网线一根，用于以太网接入（TFTP Boot 无法使用USB网络）

## 安装步骤

### 构建依赖安装

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

### 获取源码

```shell
mkdir nuttxspace
cd nuttxspace
git clone https://github.com/apache/nuttx.git nuttx
git clone https://github.com/apache/nuttx-apps apps
```

### 配置工具链并构建 NuttX

Nuttx 需要使用 xPack 工具链进行编译，首先获取工具链，从 Github 下载，自行改变版本以匹配你的系统：
```bash
wget https://github.com/xpack-dev-tools/riscv-none-elf-gcc-xpack/releases/download/v14.2.0-2/xpack-riscv-none-elf-gcc-14.2.0-2-linux-x64.tar.gz
tar -xvzf xpack-riscv-none-elf-gcc-14.2.0-2-linux-x64.tar.gz
```

/*建议将tar解压到/opt*/并将其添加到你的 PATH 中：
```bash
export PATH=/path/to/toolchain/you/untar:$PATH
```

接下来构建 Nuttx：
```shell
cd nuttx
tools/configure.sh milkv_duos:nsh
make -j$(nproc)
```
构建过程中如果遇到文件丢失，可以通过menuconfig配置选项
- 在(Top) → Library Routines → Select math library 选择是否使用数学库，及其路径
- 在(Top) → Library Routines → Builtin libclang_rt.profile选择是否启用llvm

接下来构建文件系统：
```bash
make export
pushd ../apps
tools/mkimport.sh -z -x ../nuttx/nuttx-export-*.tar.gz
make import
popd
genromfs -f initrd -d ../apps/bin -V "NuttXBootVol"

```

最后打包镜像：
```bash
head -c 65536 /dev/zero >/tmp/nuttx.pad
cat nuttx.bin /tmp/nuttx.pad initrd >Image-sg2000
```

### 从 TFTP Server 启动 NuttX RTOS

首先，烧录 Debian 镜像到存储卡。

```shell
wget https://github.com/Fishwaldo/sophgo-sg200x-debian/releases/download/v1.4.0/duos_sd.img.lz4
lz4 -d duos_sd.img.lz4
sudo dd if=duos_sd.img of=/dev/sdX bs=1M status=progress
```

至此，存储卡准备完成。将存储卡插入开发板。

在计算机上开启一个 TFTP Server。确保先前编译生成的 Image（位于 NuttX 源码目录下）和 dtb 均可被 TFTP Server 访问。

TFTP Server 配置请参考：[Arch Wiki/TFTP](https://wiki.archlinux.org/title/TFTP)。一般而言，可直接使用 tftpd:
```bash
systemctl start tftpd
```

若您是在 Windows 下，可考虑使用 [Tftpd64](http://tftpd32.jounin.net)。

将镜像文件和 dtb 下载到 tftp 文件夹，若使用 tftpd，其一般在 `/srv/tftp` 下：
```bash
wget https://github.com/lupyuen2/wip-nuttx/releases/download/sg2000-1/cv181x_milkv_duos_sd.dtb
cp Image-sg2000 /path/to/tftp/folder
cp cv181x_milkv_duos_sd.dtb /path/to/tftp/folder
```

接上 UART 调试线，给开发板上电，同时需要为开发板提供网络，在提示 `Hit any key to stop autoboot` 时按任意键打断 U-Boot，并手动配置 U-Boot 以从 TFTP 启动 NuttX：

若是 dhcp 方式获取 ip，需要先运行`dhcp`而后打断。

```shell
setenv tftp_server your_tftp_server_ip
dhcp ${kernel_addr_r} ${tftp_server}:Image-sg2000
tftpboot ${fdt_addr_r} ${tftp_server}:cv181x_milkv_duos_sd.dtb
fdt addr ${fdt_addr_r}
booti ${kernel_addr_r} - ${fdt_addr_r}
```

## 预期结果

系统正常启动，通过串口连接时能成功进入 NuttX Shell。

## 实际结果

系统正常启动，通过串口连接时能成功进入 NuttX Shell。

能够执行 `uname`, `ls`, `ostest` 等指令。

### 启动信息

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

屏幕录像：

[!bilibili](https://www.bilibili.com/video/BV1RMUeYjELe/?spm_id_from=333.999.0.0)


## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试通过。


