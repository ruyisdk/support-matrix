# NetBSD VisionFive 2 测试报告

## 测试环境

### 系统信息

- 系统版本: NetBSD-current 
- 下载链接: [riscv64.img.gz](https://nyftp.netbsd.org/pub/NetBSD-daily/HEAD/latest/riscv-riscv64/binary/gzimg/)
(镜像内自带所需 dtb 文件)

### 硬件信息

- StarFive VisionFive 2
- 电源适配器
- microSD 卡一张
- USB to UART 调试器一个

## 安装步骤

使用 `gzip` 解压镜像。
使用 `dd` 或`balenaEtcher`等工具将镜像写入 microSD 卡

```bash
sudo dd if=riscv64.img of=/dev/<your-device> bs=1M status=progress
```

### 启动系统
插入 microSD 卡,连接串口,使用 1-bit QSPI Nor Flash 模式(即：RGPIO_0 = 0, RGPIO_1 = 0)启动

手动中断 u-boot 流程，并输入启动命令:

```bash
load mmc 1:1 ${fdt_addr_r} dtb/starfive/jh7110-starfive-visionfive-2-v1.3b.dtb
load mmc 1:1 ${kernel_addr_r} efi/boot/bootriscv64.efi
bootefi ${kernel_addr_r} ${fdt_addr_r}
```

进入自动安装状态,需要重启时重新输入上述启动命令

### 持久化 uboot

```bash
env default -a -f
setenv bootcmd "load mmc 1:1 ${fdt_addr_r} dtb/starfive/jh7110-starfive-visionfive-2-v1.3b.dtb; load mmc 1:1 ${kernel_addr_r} efi/boot/bootriscv64.efi; bootefi ${kernel_addr_r} ${fdt_addr_r}"
saveenv
```

### 登录系统
直接登入 root,无需密码

## 预期结果

系统正常启动，能够通过板载串口登录

## 实际结果

系统正常启动，成功通过板载串口登录

### 启动信息

```log
login: root
Oct  2 21:59:19 riscv64 login: ROOT LOGIN (root) on tty constty
Last login: Wed Oct  2 21:23:53 2024 on constty
Copyright (c) 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003,
    2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013,
    2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023,
    2024
    The NetBSD Foundation, Inc.  All rights reserved.
Copyright (c) 1982, 1986, 1989, 1991, 1993
    The Regents of the University of California.  All rights reserved.

NetBSD 10.99.12 (GENERIC64) #0: Wed Oct  2 21:21:26 UTC 2024

Welcome to NetBSD!

This is a development snapshot of NetBSD for testing -- user beware!

Bug reports: https://www.NetBSD.org/support/send-pr.html
Donations to the NetBSD Foundation: https://www.NetBSD.org/donations/
-- UNSAFE KEYS WARNING:

        The ssh host keys on this machine have been generated with
        not enough entropy configured, so they may be predictable.

        To fix, follow the "Adding entropy" section in the entropy(7)
        man page.  After this machine has enough entropy, re-generate
        the ssh host keys by running:

                /etc/rc.d/sshd keyregen
We recommend that you create a non-root account and use su(1) for root access.
riscv64# uname -a
NetBSD riscv64 10.99.12 NetBSD 10.99.12 (GENERIC64) #0: Wed Oct  2 21:21:26 UTC 2024  mkrepro@mkrepro.NetBSD.org:/usr/src/sys/arch/riscv/compile/GENERIC64 riscv
riscv64# sysctl kern.ostype kern.osrelease kern.version
kern.ostype = NetBSD
kern.osrelease = 10.99.12
kern.version = NetBSD 10.99.12 (GENERIC64) #0: Wed Oct  2 21:21:26 UTC 2024
        mkrepro@mkrepro.NetBSD.org:/usr/src/sys/arch/riscv/compile/GENERIC64

```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功
