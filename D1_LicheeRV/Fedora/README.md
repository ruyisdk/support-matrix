# Fedora 36 D1 测试报告

## 测试环境

### 系统信息

- 系统版本：Fedora 36
- 下载链接：[https://openkoji.iscas.ac.cn/pub/dl/riscv/Allwinner/Nezha_D1/images-release/Fedora/](https://openkoji.iscas.ac.cn/pub/dl/riscv/Allwinner/Nezha_D1/images-release/Fedora/)
- 参考安装文档：[https://fedoraproject.org/wiki/Architectures/RISC-V/Allwinner/zh-cn](https://fedoraproject.org/wiki/Architectures/RISC-V/Allwinner/zh-cn)

### 硬件信息

- AWOL Nezha D1 / Sipeed Lichee RV Dock
- 电源适配器
- microSD 卡一张
- USB to UART 调试器一个

## 安装步骤

### 刷写镜像

使用 `unzstd` 解压镜像。
清空你的 sd 卡。
使用 `dd` 将镜像写入 microSD 卡。

```bash
unzstd /path/to/fedora.raw.zst
sudo wipefs -a /dev/your_device
sudo dd if=/path/to/fedora.raw of=/dev/your_device bs=1M status=progress
```

### 登录系统

*系统启动较为缓慢。*

通过串口登录系统。

默认用户名： `root`
默认密码： `riscv`

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

系统正常启动，成功通过板载串口登录。能进入桌面。

### 启动信息

屏幕录像（刷写镜像）：

[![asciicast](https://asciinema.org/a/yAMbaiYvBPLsyUPujOFey6zU3.svg)](https://asciinema.org/a/yAMbaiYvBPLsyUPujOFey6zU3)

屏幕录像（启动系统）：

[![asciicast](https://asciinema.org/a/Evalgi6VgUvxs4gUmCtzC8n7j.svg)](https://asciinema.org/a/Evalgi6VgUvxs4gUmCtzC8n7j)

```log
Welcome to the Fedora RISC-V disk image
https://openkoji.iscas.ac.cn/koji/

Build date: Fri Jul 15 17:21:32 UTC 2022

Kernel 5.4.61 on an riscv64 (ttyS0)

The root password is 'riscv'.
root password logins are disabled in SSH starting Fedora.

If DNS isn’t working, try editing ‘/etc/yum.repos.d/fedora-riscv.repo’.

For updates and latest information read:
https://fedoraproject.org/wiki/Architectures/RISC-V

Fedora RISC-V
-------------
fedora-riscv login: root
Password: 
Last login: Sun Jul 17 00:20:39 on pts/0
[  194.914653] proc: Bad value for 'hidepid'
[root@fedora-riscv ~]# neofetch 
             .',;::::;,'.                                                                                                       
         .';:cccccccccccc:;,.            ----------------- 
      .;cccccccccccccccccccccc;.         OS: Fedora Linux 36 (Thirty Six) riscv64 
    .:cccccccccccccccccccccccccc:.       Host: sun20iw1p1 
  .;ccccccccccccc;.:dddl:.;ccccccc;.     Kernel: 5.4.61 
 .:ccccccccccccc;OWMKOOXMWd;ccccccc:.    Uptime: 3 mins 
.:ccccccccccccc;KMMc;cc;xMMc:ccccccc:.   Packages: 1546 (rpm) 
,cccccccccccccc;MMM.;cc;;WW::cccccccc,   Shell: bash 5.1.16 
:cccccccccccccc;MMM.;cccccccccccccccc:   Terminal: /dev/ttyS0 
:ccccccc;oxOOOo;MMM0OOk.;cccccccccccc:   CPU: (1) @ 1.008GHz 
cccccc:0MMKxdd:;MMMkddc.;cccccccccccc;   Memory: 313MiB / 1975MiB 
ccccc:XM0';cccc;MMM.;cccccccccccccccc'
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