# Fedora 38 LPi4A 官方版本 测试报告

## 测试环境

### 系统信息

- 系统版本：Fedora 38
- 下载链接：[https://openkoji.iscas.ac.cn/pub/dl/riscv/T-Head/th1520_light/images/](https://openkoji.iscas.ac.cn/pub/dl/riscv/T-Head/th1520_light/images/)
- 参考安装文档：[https://fedoraproject.org/wiki/Architectures/RISC-V/T-Head](https://fedoraproject.org/wiki/Architectures/RISC-V/T-Head)
- fastboot 链接：
    - [https://pan.baidu.com/e/1xH56ZlewB6UOMlke5BrKWQ](https://pan.baidu.com/e/1xH56ZlewB6UOMlke5BrKWQ)
    - [https://mega.nz/folder/phoQlBTZ#cZeQ3qZ__pDvP94PT3_bGA](https://mega.nz/folder/phoQlBTZ#cZeQ3qZ__pDvP94PT3_bGA)

### 硬件信息

- Lichee Pi 4A (8G RAM + 64G eMMC)
- 电源适配器
- microSD 卡一张
- USB to UART 调试器一个

## 安装步骤

### 刷写镜像

使用 `unxz` 解压镜像。
使用 `dd` 将镜像写入 microSD 卡。

```bash
unxz /path/to/fedora.raw.xz
sudo dd if=/path/to/fedora.raw of=/dev/your_device bs=1M status=progress
```

### 刷写 bootloader

**注意：fedora 的 u-boot 在镜像中，上一步 dd 完镜像后，从 sd 卡中的 boot 分区提取！**
![u-boot](./u-boot.png)

进入 fastboot。
- 正式版确认 boot 拨码开关为 eMMC。
- 按动 BOOT 同时上电。
- （详见官方教程）
使用 fastboot 按命令烧录 u-boot。

```bash
sudo ./fastboot flash ram ./path/to/your/u-boot-with-spl_lpi4a.bin
sudo ./fastboot reboot
sleep 10
sudo ./fastboot flash uboot ./path/to/your/u-boot-with-spl_lpi4a.bin
```

### 登录系统

通过串口登录系统。

默认用户名： `root`
默认密码： `riscv`

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

系统正常启动，成功通过板载串口登录。能进入桌面。

### 启动信息

屏幕录像（从刷写镜像到登录系统）：

[![asciicast](https://asciinema.org/a/h2waHR5bazhEOeMYYxbbWUxBm.svg)](https://asciinema.org/a/h2waHR5bazhEOeMYYxbbWUxBm)

```log
Welcome to the Fedora RISC-V disk image
https://openkoji.iscas.ac.cn/koji/

Build date: Mon May 15 18:37:47 UTC 2023

Kernel 5.10.113 on an riscv64 (ttyS0)

The root password is 'riscv'.
root password logins are disabled in SSH starting Fedora.

If DNS isn’t working, try editing ‘/etc/yum.repos.d/fedora-riscv.repo’.

For updates and latest information read:
https://fedoraproject.org/wiki/Architectures/RISC-V

Fedora RISC-V
-------------
fedora-riscv login: root
Password: 
Last login: Wed May 10 20:03:42 on ttyS0
[root@fedora-riscv ~]# neofetch
             .',;::::;,'.                                                                                                       
         .';:cccccccccccc:;,.            ----------------- 
      .;cccccccccccccccccccccc;.         OS: Fedora Linux 38 (Xfce) riscv64 
    .:cccccccccccccccccccccccccc:.       Host: T-HEAD Light Lichee Pi 4A configuration for 8GB DDR board 
  .;ccccccccccccc;.:dddl:.;ccccccc;.     Kernel: 5.10.113 
 .:ccccccccccccc;OWMKOOXMWd;ccccccc:.    Uptime: 5 mins 
.:ccccccccccccc;KMMc;cc;xMMc:ccccccc:.   Packages: 2070 (rpm) 
,cccccccccccccc;MMM.;cc;;WW::cccccccc,   Shell: bash 5.2.15 
:cccccccccccccc;MMM.;cccccccccccccccc:   Resolution: 1920x1080 
:ccccccc;oxOOOo;MMM0OOk.;cccccccccccc:   Terminal: /dev/ttyS0 
cccccc:0MMKxdd:;MMMkddc.;cccccccccccc;   CPU: (4) 
ccccc:XM0';cccc;MMM.;cccccccccccccccc'   Memory: 217MiB / 7803MiB 
ccccc;MMo;ccccc;MMW.;ccccccccccccccc;
ccccc;0MNc.ccc.xMMd:ccccccccccccccc;                             
cccccc;dNMWXXXWM0::cccccccccccccc:,                              
cccccccc;.:odl:.;cccccccccccccc:,.
:cccccccccccccccccccccccccccc:'.
.:cccccccccccccccccccccc:;,..
  '::cccccccccccccc::;,.

```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。