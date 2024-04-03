# Fedura 38 Lichee Cluster 4A 版本测试报告

## 测试环境

### 操作系统信息

- 系统版本：Fedora 38
- 下载链接：[https://openkoji.iscas.ac.cn/pub/dl/riscv/T-Head/th1520_light/images/](https://openkoji.iscas.ac.cn/pub/dl/riscv/T-Head/th1520_light/images/)
- 参考安装文档：[https://fedoraproject.org/wiki/Architectures/RISC-V/T-Head](https://fedoraproject.org/wiki/Architectures/RISC-V/T-Head)
- fastboot 链接：
    - [https://pan.baidu.com/e/1xH56ZlewB6UOMlke5BrKWQ](https://pan.baidu.com/e/1xH56ZlewB6UOMlke5BrKWQ)
    - [https://mega.nz/folder/phoQlBTZ#cZeQ3qZ__pDvP94PT3_bGA](https://mega.nz/folder/phoQlBTZ#cZeQ3qZ__pDvP94PT3_bGA)

### 硬件信息

- Lichee Cluster 4A 8G / 16G
- DC 12V 电源
- USB-A to A
    - 或 LPi4A 底板
- microSD 卡一张
- 网络和网线（注意连接到 BMC 而非交换机）

## 安装步骤

*以下以刷写到集群中一号板为例*

*注意 Fedora 系统从 sd 卡而非 eMMC 启动，需要插卡*

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

```bash
sudo ./fastboot flash ram ./path/to/your/u-boot-with-spl_lpi4a.bin
sudo ./fastboot reboot
sleep 10
sudo ./fastboot flash uboot ./path/to/your/u-boot-with-spl_lpi4a.bin
```

### 登录系统

通过 SOL (Serial Over LAN) 登录系统。

BMC 默认用户名：`root`

BMC 默认密码：`0penBmc` **注意是 `0` 而不是 `O`**

通过 `ssh -p 2301 root@lichee-rv.local` 连接

默认用户名： `root`
默认密码： `riscv`

### 常见问题

若无法使用 USB，是因为 Linux 设备树需要 patch。[patch 下载](https://dl.sipeed.com/fileList/LICHEE/LicheeCluster4A/04_Firmware/lpi4a/src/linux/0001-arch-riscv-boot-dts-lpi4a-disable-i2c-io-expander-fo.patch)

## 预期结果

系统正常启动，能够通过 SOL (Serial Over LAN) 登录。

## 实际结果

系统正常启动，能够通过 SOL (Serial Over LAN) 登录。

### 启动信息

屏幕录像（从刷写系统到启动）：

[![asciicast](https://asciinema.org/a/OTu3SKCoCpADbc4AMNJNOjjoQ.svg)](https://asciinema.org/a/OTu3SKCoCpADbc4AMNJNOjjoQ)


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
fedora-riscv login: [   85.830881] systemd-journald[337]: Oldest entry in /var/log/journal/605fc8e09e9a4453ae8bd14351948ca9/system.journal is older than the configured file retention duration (1month), suggesting rotation.
[   85.850848] systemd-journald[337]: /var/log/journal/605fc8e09e9a4453ae8bd14351948ca9/system.journal: Journal header limits reached or header out-of-date, rotating.
root
Password: 
[root@fedora-riscv ~]# neofetch 
             .',;::::;,'.                root@fedora-riscv 
         .';:cccccccccccc:;,.            ----------------- 
      .;cccccccccccccccccccccc;.         OS: Fedora Linux 38 (Xfce) riscv64 
    .:cccccccccccccccccccccccccc:.       Host: T-HEAD Light Lichee Pi 4A configuration for 8GB DDR board 
  .;ccccccccccccc;.:dddl:.;ccccccc;.     Kernel: 5.10.113 
 .:ccccccccccccc;OWMKOOXMWd;ccccccc:.    Uptime: 2 mins 
.:ccccccccccccc;KMMc;cc;xMMc:ccccccc:.   Packages: 2070 (rpm) 
,cccccccccccccc;MMM.;cc;;WW::cccccccc,   Shell: bash 5.2.15 
:cccccccccccccc;MMM.;cccccccccccccccc:   Resolution: 1024x768 
:ccccccc;oxOOOo;MMM0OOk.;cccccccccccc:   Terminal: /dev/ttyS0 
cccccc:0MMKxdd:;MMMkddc.;cccccccccccc;   CPU: (4) 
ccccc:XM0';cccc;MMM.;cccccccccccccccc'   Memory: 185MiB / 7803MiB
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