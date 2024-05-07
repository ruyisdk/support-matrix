# NuttX on Milk-V Duo S

## 测试环境

### 操作系统信息

- 构建系统：Arch Linux
- Debian Linux 镜像 + U-Boot：https://github.com/Fishwaldo/sophgo-sg200x-debian/releases/tag/v1.1.0
- 源码链接
    - NuttX: https://github.com/lupyuen2/wip-nuttx/tree/sg2000
    - NuttX Apps: https://github.com/lupyuen2/wip-nuttx-apps/tree/sg2000
- 工具链：xPack（使用 [xpm](https://xpack.github.io/xpm/install/) 安装，见下文 [配置工具链](#配置工具链) 章节）
- 参考安装文档；https://github.com/lupyuen/nuttx-sg2000

NuttX SG2000 移植仍在进行中，目前需要通过 TFTP 启动。

### 硬件信息

- Milk-V Duo S (512M, SG2000)
- USB 电源适配器一个
- USB-A to C 或 USB C to C 线缆一条，用于给开发板供电
- microSD 卡一张
- USB 读卡器一个
- USB to UART 调试器一个（如：CP2102, FT2232 等，注意不可使用 CH340/341 系列，会出现乱码）
- 杜邦线三根
- 以太网接入，用于 TFTP Boot

## 安装步骤

### 构建依赖安装

```shell
sudo pacman -S --needed base-devel ncurses5-compat-libs gperf pkg-config gmp libmpc mpfr libelf expat picocom uboot-tools util-linux git wget libisl
# AUR packages only, use any AUR helper as you wish
paru -S kconfig-frontends genromfs
# yay -S kconfig-frontends genromfs
```

### 获取源码

```shell
git clone --b sg2000 https://github.com/lupyuen2/wip-nuttx nuttx
git clone --b sg2000 https://github.com/lupyuen2/wip-nuttx-apps apps
cd nuttx
git pull && git status && hash1=`git rev-parse HEAD`
pushd ../apps
git pull && git status && hash2=`git rev-parse HEAD`
popd
echo NuttX Source: https://github.com/apache/nuttx/tree/$hash1 >nuttx.hash
echo NuttX Apps: https://github.com/apache/nuttx-apps/tree/$hash2 >>nuttx.hash
```

### 配置工具链并构建 NuttX

> [!Note]
> 使用 Arch Linux 软件源提供的 `riscv64-elf-gcc` 工具链时，可能会在编译过程中报缺少 `math.h` 而中断编译。使用 xPack 工具链以规避此问题。
>
> 使用 `xpm` 安装 xPack 工具链到 NuttX 目录。

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

### 从 TFTP Server 启动 NuttX RTOS

首先，烧录 Debian 镜像到存储卡。

```shell
unzip milkv-duos-sd-v1.1.0-2024-0410.img.zip
sudo dd if=milkv-duos-sd-v1.1.0-2024-0410.img of=/dev/sdX bs=1M status=progress
```

接下来会使用镜像中自带的 U-Boot 和 dtb。挂载刚刚烧录好的存储卡的第一个 FAT 分区，复制里面的 dtb：

```shell
sudo mount /dev/sdX1 /mnt
cp /mnt/fdt/linux-image-duos-5.10.4-20240329-1+/cv181x_milkv_duos_sd.dtb ~/
```

将存储卡插入开发板。

在计算机上开启一个 TFTP Server。确保先前编译生成的 Image（位于 NuttX 源码目录下）和 dtb 均可被 TFTP Server 访问。

TFTP Server 配置请参考：[Arch Wiki/TFTP](https://wiki.archlinux.org/title/TFTP)

若您是在 Windows 下，可使用 [Tftpd64](http://tftpd32.jounin.net)。

接上 UART 调试线，给开发板上电，启动时打断 U-Boot，并手动配置 U-Boot 以从 TFTP 启动 NuttX：

```shell
setenv tftp_server your_tftp_server_ip
dhcp ${kernel_addr_r} ${tftp_server}:Image
tftpboot ${fdt_addr_r} ${tftp_server}:cv181x_milkv_duos_sd.dtb
booti ${kernel_addr_r} ${ramdisk_addr_r}:${ramdisk_size} ${fdt_addr_r}
```

## 预期结果

系统正常启动，串口输出 123。

## 实际结果

系统正常启动，串口输出 123。

### 启动信息

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
Warning: ethernet@4070000 (eth0) using random MAC address - 3e:16:f7:e0:6e:6c
eth0: ethernet@4070000
Hit any key to stop autoboot:  0
cv181x_c906# setenv tftp_server 10.0.0.189
cv181x_c906# dhcp ${kernel_addr_r} ${tftp_server}:Image
Speed: 100, full duplex
BOOTP broadcast 1
BOOTP broadcast 2
BOOTP broadcast 3
BOOTP broadcast 4
DHCP client bound to address 10.0.0.225 (3013 ms)
Using ethernet@4070000 device
TFTP from server 10.0.0.189; our IP address is 10.0.0.225
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
         ###############
         5.5 MiB/s
done
Bytes transferred = 15477329 (ec2a51 hex)
cv181x_c906# tftpboot ${fdt_addr_r} ${tftp_server}:cv181x_milkv_duos_sd.dtb
Speed: 100, full duplex
Using ethernet@4070000 device
TFTP from server 10.0.0.189; our IP address is 10.0.0.225
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

123
```

屏幕录像：

[![asciicast](https://asciinema.org/a/TpjMi4tpcibu0HCYVJXCLTN3n.svg)](https://asciinema.org/a/TpjMi4tpcibu0HCYVJXCLTN3n)

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试通过。