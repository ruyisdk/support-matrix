# NuttX Star64 测试报告

## 测试环境

### 操作系统信息

- 预编译内核：https://github.com/lupyuen2/wip-pinephone-nuttx/releases/download/jh7110c-1.0.0/starfiveu.fit
- 源码链接：https://github.com/apache/nuttx
- 参考安装文档：https://nuttx.apache.org/docs/latest/platforms/risc-v/jh7110/boards/star64/index.html
- 工具链：
    - 启动镜像：https://github.com/starfive-tech/VisionFive2/releases/download/JH7110_VF2_515_v5.11.3/sdcard.img
    - DTB：https://github.com/starfive-tech/VisionFive2/releases
    - toolchain: https://github.com/sifive/freedom-tools/releases
    - kflash：https://github.com/kendryte/kflash.py

### 硬件信息

- Pine64 Star64
- microSD 卡一张
- DC 12V5A 圆头电源适配器
- USB to UART 调试器一个（如：CH340, CH341, FT2232 等）
- 杜邦线三根

## 安装步骤

### 使用预编译内核

```shell
wget https://github.com/lupyuen2/wip-pinephone-nuttx/releases/download/jh7110c-1.0.0/starfiveu.fit
```

### 手动编译

#### 准备源码及环境

获取工具链：
```bash
sudo apt install kconfig-frontends genromfs u-boot-tools
wget https://static.dev.sifive.com/dev-tools/freedom-tools/v2020.12/riscv64-unknown-elf-toolchain-10.2.0-2020.12.8-x86_64-linux-ubuntu14.tar.gz
tar -xvzf riscv64-unknown-elf-toolchain-10.2.0-2020.12.8-x86_64-linux-ubuntu14.tar.gz
export PATH=path/to/toolchain/bin:$PATH
```

clone 仓库并进行配置：
```bash
mkdir nuttx && cd nuttx
git clone -b nuttx-12.9.0 https://github.com/apache/nuttx.git nuttx
git clone -b nuttx-12.9.0 https://github.com/apache/nuttx-apps.git apps
```
#### 构建 NuttX

编译 nuttx.bin：
```bash
cd nuttx
./tools/configure.sh star64:nsh
make -j$(nproc)
riscv64-unknown-elf-objcopy -O binary nuttx nuttx.bin
```

构建文件系统：
```bash
make export
pushd ../apps
tools/mkimport.sh -z -x ../nuttx/nuttx-export-*.tar.gz
make import
popd
genromfs -f initrd -d ../apps/bin -V "NuttXBootVol"
```

编写 dtb 文件：
- 下载 dtb：
```bash
wget https://github.com/starfive-tech/VisionFive2/releases/download/JH7110_VF2_515_v5.11.3/jh7110-visionfive-v2.dtb
```
- 在 nuttx 文件夹下进行：
```bash
cat << EOF > nuttx.its
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
```

创建 fit：
```bash
mkimage -f nuttx.its -A riscv -O linux -T flat_dt starfiveu.fit
```

### 准备镜像

下载 StarFive 的官方 SD 卡镜像并烧写：
```bash
wget https://github.com/starfive-tech/VisionFive2/releases/download/JH7110_VF2_515_v5.11.3/sdcard.img
sudo dd if=sdcard.img of=/dev/your/device bs=1M status=progress
```

替换 fit 文件：
```bash
mkdir mnt
sudo mount /dev/your/sdcard/p3 mnt
sudo cp starfiveu.fit mnt/
sudo umount mnt
rm -r mnt
```

### 登录系统

将启动项设为 microSD 卡 (GPIO_0 = 1, GPIO_1 = 0；参见 [选择启动项](https://canonical-ubuntu-boards.readthedocs-hosted.com/en/latest/how-to/pine64-star64/#boot-source-selection))。

通过串口连接开发板。

## 预期结果

开发板正常输出启动信息。

## 实际结果

开发板正常输出启动信息。

### 启动信息

```log
U-Boot SPL 2021.10 (Jun 21 2023 - 13:42:04 +0800)
DDR version: dc2e84f0.
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


U-Boot 2021.10 (Jun 21 2023 - 13:42:04 +0800), Build: jenkins-github_visionfive2-15

CPU:   rv64imacu_zba_zbb
Model: StarFive VisionFive V2
DRAM:  8 GiB
MMC:   sdio0@16010000: 0, sdio1@16020000: 1
Loading Environment from SPIFlash... SF: Detected gd25lq128 with page size 256 Bytes, erase size 4 KiB, total 16 MiB
OK
StarFive EEPROM format v2

--------EEPROM INFO--------
Vendor : PINE64
Product full SN: STAR64V1-2310-D008E000-00000005
data version: 0x2
PCB revision: 0xc1
BOM revision: A
Ethernet MAC0 address: 6c:cf:39:00:75:61
Ethernet MAC1 address: 6c:cf:39:00:75:62
--------EEPROM INFO--------

In:    serial
Out:   serial
Err:   serial
Model: StarFive VisionFive V2
Net:   eth0: ethernet@16030000, eth1: ethernet@16040000
bootmode sd device 1/0
Hit any key to stop autoboot:  0
1579 bytes read in 7 ms (219.7 KiB/s)
Importing environment from 1/0 ...
switch to partitions #0, OK
mmc1 is current device
10232366 bytes read in 447 ms (21.8 MiB/s)
## Loading kernel from FIT Image at a0000000 ...
   Using 'nuttx' configuration
   Trying 'vmlinux' kernel subimage
     Description:  vmlinux
     Type:         Kernel Image
     Compression:  uncompressed
     Data Start:   0xa00000b4
     Data Size:    2097800 Bytes = 2 MiB
     Architecture: RISC-V
     OS:           Linux
     Load Address: 0x40200000
     Entry Point:  0x40200000
   Verifying Hash Integrity ... OK
## Loading fdt from FIT Image at a0000000 ...
   Using 'nuttx' configuration
   Trying 'fdt' fdt subimage
     Description:  unavailable
     Type:         Flat Device Tree
     Compression:  uncompressed
     Data Start:   0xa09b58bc
     Data Size:    50235 Bytes = 49.1 KiB
     Architecture: RISC-V
     Load Address: 0x46000000
     Hash algo:    sha256
     Hash value:   42767c996f0544f513280805b41f996446df8b3956c656bdbb782125ae8ffeec
   Verifying Hash Integrity ... sha256+ OK
   Loading fdt from 0xa09b58bc to 0x46000000
   Booting using the fdt blob at 0x46000000
## Loading loadables from FIT Image at a0000000 ...
   Trying 'ramdisk' loadables subimage
     Description:  buildroot initramfs
     Type:         RAMDisk Image
     Compression:  uncompressed
     Data Start:   0xa02003f0
     Data Size:    8082432 Bytes = 7.7 MiB
     Architecture: RISC-V
     OS:           Linux
     Load Address: 0x46100000
     Entry Point:  unavailable
     Hash algo:    sha256
     Hash value:   41cdaae1d74fbf5f03e1a9c52ca91a13b14efc3de12f6ad690cf7b45474703a7
   Verifying Hash Integrity ... sha256+ OK
   Loading loadables from 0xa02003f0 to 0x46100000
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
BC
NuttShell (NSH) NuttX-12.2.1-RC0
nsh> help
help usage:  help [-v] [<cmd>]

    .         break     dd        exit      kill      printf    sleep     uname
    [         cat       df        false     ls        ps        source    umount
    ?         cd        dmesg     fdinfo    mkdir     pwd       test      unset
    alias     cp        echo      free      mkrd      rm        time      uptime
    unalias   cmp       env       help      mount     rmdir     true      usleep
    basename  dirname   exec      hexdump   mv        set       truncate  xd
nsh> uname -a
NuttX 12.2.1-RC0 8605714 Aug  7 2023 16:20:45 risc-v star64
nsh> free
                   total       used       free    largest  nused  nfree
        Kmem:    2065400      14600    2050800    2049440     50      3
        Page:   20971520     643072   20328448   20328448
nsh>

```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。