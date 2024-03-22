# Fedora 33 VisionFive 测试报告

## 测试环境

### 系统信息

- 系统版本：Fedora 33
- 下载链接：[https://fedora.starfivetech.com/pub/downloads/VisionFive-release/Fedora-riscv64-jh7100-developer-xfce-Rawhide-20211226-214100.n.0-sda.raw.zst](https://fedora.starfivetech.com/pub/downloads/VisionFive-release/Fedora-riscv64-jh7100-developer-xfce-Rawhide-20211226-214100.n.0-sda.raw.zst)
- 参考安装文档：[https://doc.rvspace.org/VisionFive/PDF/VisionFive_Quick_Start_Guide.pdf](https://doc.rvspace.org/VisionFive/PDF/VisionFive_Quick_Start_Guide.pdf)

### 硬件信息

- StarFive VisionFive
- 电源适配器
- microSD 卡一张
- USB to UART 调试器一个

## 安装步骤

### 刷写镜像

使用 `zstd` 解压镜像。
使用 `dd` 将镜像写入 microSD 卡。

```bash
zstd -d /path/to/fedora.raw.zst
sudo dd if=/path/to/fedora of=/dev/your-device bs=1M status=progress
```

### 登录系统

通过串口登录系统。

默认用户名： `root`
默认密码： `starfive`

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

系统正常启动，成功通过板载串口登录。

### 启动信息

屏幕录像（从刷写镜像到登录系统）：

[![asciicast](https://asciinema.org/a/wuaUJ0h23U1eWMFzoyQPLTvgp.svg)](https://asciinema.org/a/wuaUJ0h23U1eWMFzoyQPLTvgp)

```log
Build date: Tue Nov 16 23:07:46 UTC 2021

Kernel 5.15.10+ on an riscv64 (ttyS0)

The root password is 'starfive'.
root password logins are disabled in SSH starting Fedora 31.
User 'riscv' with password 'starfive' in 'wheel' group is provided.

To install new packages use 'dnf install ...'

To upgrade disk image use 'dnf upgrade --best'

If DNS isn’t working, try editing ‘/etc/yum.repos.d/fedora-riscv.repo’.

For updates and latest information read:
https://fedoraproject.org/wiki/Architectures/RISC-V

Fedora/RISC-V
-------------
Koji:               http://fedora.riscv.rocks/koji/
SCM:                http://fedora.riscv.rocks:3000/
Distribution rep.:  http://fedora.riscv.rocks/repos-dist/
Koji internal rep.: http://fedora.riscv.rocks/repos/
fedora-starfive login: root
Password: 
[  103.100371] systemd-xdg-autostart-generator[741]: Not generating service for XDG autostart app-gnome\x2dkeyring\x2dssh-autos.
[  103.115950] systemd-xdg-autostart-generator[741]: Not generating service for XDG autostart app-gnome\x2dkeyring\x2dpkcs11-au.
[  103.131975] systemd-xdg-autostart-generator[741]: Not generating service for XDG autostart app-xdg\x2duser\x2ddirs-autostart.
[  103.147007] systemd-xdg-autostart-generator[741]: Not generating service for XDG autostart app-gnome\x2dkeyring\x2dsecrets-a.
[  103.162696] systemd-xdg-autostart-generator[741]: Not generating service for XDG autostart app-xapp\x2dsn\x2dwatcher-autosta.
[  103.177879] systemd-xdg-autostart-generator[741]: Not generating service for XDG autostart app-gsettings\x2ddata\x2dconvert-.
[  103.193926] systemd-xdg-autostart-generator[741]: Not generating service for XDG autostart app-at\x2dspi\x2ddbus\x2dbus-auto.
[  103.210809] systemd-xdg-autostart-generator[741]: gnome-systemd-autostart-condition not found: No such file or directory
Last login: Tue Dec 21 01:25:23 on pts/0
[root@fedora-starfive ~]# neofetch 
          /:-------------:\                                                                                                     
       :-------------------::        -------------------- 
     :-----------/shhOHbmp---:\      OS: Fedora 33 (Rawhide) riscv64 
   /-----------omMMMNNNMMD  ---:     Host: StarFive VisionFive V1 
  :-----------sMMMMNMNMP.    ---:    Kernel: 5.15.10+ 
 :-----------:MMMdP-------    ---\   Uptime: 1 min 
,------------:MMMd--------    ---:   Packages: 2359 (rpm) 
:------------:MMMd-------    .---:   Shell: bash 5.0.17 
:----    oNMMMMMMMMMNho     .----:   Terminal: /dev/ttyS0 
:--     .+shhhMMMmhhy++   .------/   CPU: (2) 
:-    -------:MMMd--------------:    Memory: 221MiB / 7174MiB 
:-   --------/MMMd-------------;
:-    ------/hMMMy------------:                              
:-- :dMNdhhdNMMNo------------;                               
:---:sdNMMMMNds:------------:
:------:://:-------------::
:---------------------://

[root@fedora-starfive ~]# 

```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。