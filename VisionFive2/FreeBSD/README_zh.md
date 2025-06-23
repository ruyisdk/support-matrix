# FreeBSD VisionFive 2 测试报告

## 测试环境

### 系统信息

- 系统版本：14.3-RELEASE
- 源码链接：https://github.com/robn/freebsd-vf2
- 参考安装文档：https://github.com/robn/freebsd-vf2

### 硬件信息

- StarFive VisionFive 2
- 电源适配器
- microSD 卡一张
- USB to UART 调试器一个

## 安装步骤

### 构建安装镜像

下列构建步骤需在 FreeBSD 系统下进行：

```bash
git clone https://github.com/robn/freebsd-vf2.git
cd freebsd-vf2
BASE_URL=https://download.freebsd.org/releases/ISO-IMAGES/14.3/ BASE_IMAGE=FreeBSD-14.3-RELEASE-riscv-riscv64-GENERICSD.img ./mkvf2img.sh
```

刷写生成的 `vf2.img` 到 sd 卡：

```bash
dd if=vf2.img of=/dev/your/device status=progress
```

### 启动系统
插入 microSD 卡,连接串口,使用 1-bit QSPI Nor Flash 模式(即：RGPIO_0 = 0, RGPIO_1 = 0)启动。
手动中断 u-boot 流程，并输入启动命令：

```bash
fatload mmc 1:1 0x48000000 dtb/starfive/starfive_visionfive2.dtb
fatload mmc 1:1 0x44000000 efi/boot/bootriscv64.efi
bootefi 0x44000000 0x48000000
```

当串口出现 `Hit [Enter] to boot immediately, or any other key for command prompt` 时，按下除 Enter 外的任意一个键进入 FreeBSD stage 3 bootloader prompt.

使用以下命令加载 rootfs:

```shell
load geom_uzip
load -t md_image /root.img.uzip
set vfs.root.mountfrom="ufs:/dev/md0.uzip"
boot
```

### 登录系统

通过串口登录系统。

用户名：`root`

密码：`root`

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

系统正常启动，但键盘输入时出现 `sbi_ecall_handler: Invalid error`， 无法进入系统。

### 启动信息

```log
Using DTB provided by EFI at 0x47f00000.
Kernel entry at 0xbe20002e...
Kernel args: (null)
clk u2_dw_i2c_clk_core already disabled
clk u2_dw_i2c_clk_apb already disabled
clk u5_dw_i2c_clk_core already disabled
clk u5_dw_i2c_clk_apb already disabled
---<<BOOT>>---
Copyright (c) 1992-2023 The FreeBSD Project.
Copyright (c) 1979, 1980, 1983, 1986, 1988, 1989, 1991, 1992, 1993, 1994
        The Regents of the University of California. All rights reserved.
FreeBSD is a registered trademark of The FreeBSD Foundation.
FreeBSD 14.3-RELEASE releng/14.3-n271432-8c9ce319fef7 GENERIC riscv
FreeBSD clang version 19.1.7 (https://github.com/llvm/llvm-project.git llvmorg-19.1.7-0-gcd708029e0b2)
VT: init without driver.
SBI: OpenSBI v1.2
SBI Specification Version: 1.0
CPU 0  : Vendor=SiFive Core=6/7/P200/X200-Series Processor (Hart 1)
  marchid=0x8000000000000007, mimpid=0x4210427
  MMU: 0x1<Sv39>
  ISA: 0x112d<Atomic,Compressed,Double,Float,Mult/Div>
  S-mode Extensions: 0
real memory  = 4294967296 (4096 MB)
avail memory = 3384913920 (3228 MB)
FreeBSD/SMP: Multiprocessor System Detected: 4 CPUs
CPU 1  : Vendor=SiFive Core=6/7/P200/X200-Series Processor (Hart 2)
CPU 2  : Vendor=SiFive Core=6/7/P200/X200-Series Processor (Hart 3)
CPU 3  : Vendor=SiFive Core=6/7/P200/X200-Series Processor (Hart 4)
arc4random: WARNING: initial seeding bypassed the cryptographic random device because it was not yet seeded and the knob 'bypass_before_seeding' was enabled.
random: entropy device external interface
kbd0 at kbdmux0
ofwbus0: <Open Firmware Device Tree>
simplebus0: <Flattened device tree simple bus> on ofwbus0
simple_mfd0: <Simple MFD (Multi-Functions Device)> mem 0x13030000-0x13030fff on simplebus0
sbi0: <RISC-V Supervisor Binary Interface>
intc0: <RISC-V Local Interrupt Controller> on ofwbus0
sbi_ipi0: <RISC-V SBI Inter-Processor Interrupts> on sbi0
plic0: <RISC-V PLIC> mem 0xc000000-0xfffffff irq 14,15,16,17,18,19,20,21,22 on simplebus0
timer0: <RISC-V Timer>
Timecounter "RISC-V Timecounter" frequency 4000000 Hz quality 1000
Event timer "RISC-V Eventtimer" frequency 4000000 Hz quality 1000
rcons0: <RISC-V console>
cpulist0: <Open Firmware CPU Group> on ofwbus0
cpu0: <Open Firmware CPU> on cpulist0
Timecounters tick every 1.000 msec
md0: Preloaded image </root.img.uzip> 792980992 bytes at 0xffffffc000c154c8
usb_needs_explore_all: no devclass
sbi_ipi0: using for IPIs
Release APs
Trying to mount root from ufs:/dev/md0.uzip []...
random: unblocking device.
Warning: no time-of-day clock registered, system time will not be set accurately
Setting hostuuid: 31374656-3031-3142-2d32-3331302d4430.
Setting hostid: 0x4c42e45b.
Starting file system checks:
Growing root partition to fill device
unhandled type: UZIP
growfs: requested size 5.9GB is equal to the current filesystem size 5.9GB
eval: cannot create /etc/hostid: Read-only file system
/etc/rc: WARNING: could not store hostuuid in /etc/hostid.
eval: cannot create /etc/machine-id: Read-only file system
/etc/rc: WARNING: could not store hostuuid in /etc/machine-id.
Mounting local filesystems:.
mkdir: /tmp/.diskless.f8e8f030e7c2100f2f6aa5327537c101a08e0482488ed8f9ac5f7ef7725fdaba: Read-only file system
ELF ldconfig path: /lib /usr/lib /usr/lib/compat
Setting hostname: generic.
Setting up harvesting: [CALLOUT],[UMA],[FS_ATIME],SWI,INTERRUPT,NET_NG,[NET_ETHER],NET_TUN,MOUSE,KEYBOARD,ATTACH,CACHED
Feeding entropy: dd: /entropy: Read-only file system
dd: /boot/entropy: Read-only file system
.
lo0: link state changed to UP
Starting Network: lo0.
lo0: flags=1008049<UP,LOOPBACK,RUNNING,MULTICAST,LOWER_UP> metric 0 mtu 16384
        options=680003<RXCSUM,TXCSUM,LINKSTATE,RXCSUM_IPV6,TXCSUM_IPV6>
        inet 127.0.0.1 netmask 0xff000000
        inet6 ::1 prefixlen 128
        inet6 fe80::1%lo0 prefixlen 64 scopeid 0x1
        groups: lo
        nd6 options=23<PERFORMNUD,ACCEPT_RTADV,AUTO_LINKLOCAL>
Starting devd.
add host 127.0.0.1: gateway lo0 fib 0: route already in table
add host ::1: gateway lo0 fib 0: route already in table
add net fe80::: gateway ::1
add net ff02::: gateway ::1
add net ::ffff:0.0.0.0: gateway ::1
add net ::0.0.0.0: gateway ::1
Updating motd:ln: /etc/motd: Read-only file system
.
Updating /var/run/os-release done.
Clearing /tmp (X related).
Creating and/or trimming log files.
Starting syslogd.
Mounting late filesystems:.
Starting cron.
Generating RSA host key.
Saving key "/etc/ssh/ssh_host_rsa_key" failed: Read-only file system
ssh-keygen: /etc/ssh/ssh_host_rsa_key.pub: No such file or directory
Generating ECDSA host key.
Saving key "/etc/ssh/ssh_host_ecdsa_key" failed: Read-only file system
ssh-keygen: /etc/ssh/ssh_host_ecdsa_key.pub: No such file or directory
Generating ED25519 host key.
Saving key "/etc/ssh/ssh_host_ed25519_key" failed: Read-only file system
ssh-keygen: /etc/ssh/ssh_host_ed25519_key.pub: No such file or directory
Performing sanity check on sshd configuration.
No host key files found
/etc/rc: WARNING: failed precmd routine for sshd
Starting background file system checks in 60 seconds.
mount: /dev/md0.uzip: Read-only file system
rm: /firstboot: Read-only file system

Mon Jun 23 00:46:25 UTC 2025

FreeBSD/riscv (generic) (rcons)

login: sbi_ecall_handler: Invalid error 114 for ext=0x2 func=0x0
sbi_ecall_handler: Invalid error 111 for ext=0x2 func=0x0
sbi_ecall_handler: Invalid error 111 for ext=0x2 func=0x0
sbi_ecall_handler: Invalid error 116 for ext=0x2 func=0x0
sbi_ecall_handler: Invalid error 13 for ext=0x2 func=0x0
sbi_ecall_handler: Invalid error 114 for ext=0x2 func=0x0
sbi_ecall_handler: Invalid error 111 for ext=0x2 func=0x0
sbi_ecall_handler: Invalid error 111 for ext=0x2 func=0x0
sbi_ecall_handler: Invalid error 116 for ext=0x2 func=0x0
sbi_ecall_handler: Invalid error 13 for ext=0x2 func=0x0

```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试失败。