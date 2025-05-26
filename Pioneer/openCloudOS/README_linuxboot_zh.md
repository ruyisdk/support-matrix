# openCloudOS-Stream 23 Pioneer 测试报告

## 测试环境

### 操作系统信息

- 系统版本：openCloudOS-Stream 23
- 下载链接：[https://mirrors.opencloudos.tech/opencloudos-stream/releases/23/images/riscv64/sdcard/](https://mirrors.opencloudos.tech/opencloudos-stream/releases/23/images/riscv64/sdcard/)
  - 固件: [https://mirror.iscas.ac.cn/revyos/extra/images/sg2042/20241230/](https://mirror.iscas.ac.cn/revyos/extra/images/sg2042/20241230/)

### 硬件信息

- Milk-V Pioneer Box v1.3
- microSD 卡一张
- USB Type-C 数据线一根（用于连接板载串口）

## 安装步骤

### 刷写镜像

请下载linuxboot版本的镜像：[ocs_developer_sdcard-linuxboot.img.xz](https://mirrors.opencloudos.tech/opencloudos-stream/releases/23/images/riscv64/sdcard/ocs_developer_sdcard-linuxboot.img.xz)

使用 `xz` 解压镜像。
使用 `dd` 将镜像写入 microSD 卡。

```bash
xz -d ocs_developer_sdcard-linuxboot.img.xz
dd if=ocs_developer_sdcard-linuxboot.img of=/dev/your-device bs=4M status=progress
```


### 安装桌面环境

你需要在使用桌面环境之前更新 mesa 驱动。

```bash
sudo dnf update -y
```

```bash
sudo dnf install -y xorg-x11*
sudo dnf install -y gnome*
sudo dnf install -y gtk3 clutter-gtk xdg-user-dirs-gtk colord-gtk
```

我们强烈建议安装以下字体以获得更好的体验：

```bash
sudo dnf install -y google-noto-fonts-common google-noto-cjk-fonts-common google-noto-sans-cjk-sc-fonts google-noto-serif-sc-fonts
```

*如果您使用其他语言，请将 sc 字体更改为您的语言*

应用以下更改以启动默认进入桌面环境：

```bash
sudo systemctl set-default graphical.target
```


### 登录系统

通过串口登录系统。

默认用户名：`root`
默认密码：`riscv666!`


## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 预期结果

系统正常启动，能够通过串口登录。

## 实际结果

系统正常启动，成功通过串口登录。

### 启动信息


```log
riscv64 login:
riscv64 login: root
Password:
[root@riscv64 ~]# cat /etc/os-release 
NAME="OpenCloudOS Stream"
VERSION="23"
RELEASE="2410"
ID="opencloudos"
ID_LIKE="opencloudos"
VERSION_ID="23"
PLATFORM_ID="platform:ocs23"
PRETTY_NAME="OpenCloudOS Stream 23"
ANSI_COLOR="0;31"
CPE_NAME="cpe:/o:opencloudos:opencloudos:23"
HOME_URL="https://www.opencloudos.org/"
BUG_REPORT_URL="https://bugs.opencloudos.tech/"
[root@riscv64 ~]# cat /etc/opencloudos-release 
OpenCloudOS Stream release 23
[root@riscv64 ~]# lscpu
Architecture:          riscv64
  Byte Order:          Little Endian
CPU(s):                64
  On-line CPU(s) list: 0-63
NUMA:                  
  NUMA node(s):        4
  NUMA node0 CPU(s):   0-7,16-23
  NUMA node1 CPU(s):   8-15,24-31
  NUMA node2 CPU(s):   32-39,48-55
  NUMA node3 CPU(s):   40-47,56-63
[root@riscv64 ~]# uname -a
Linux riscv64.developer.ocs23 6.6.68 #1 SMP Thu Apr 10 17:26:47 CST 2025 riscv64 riscv64 riscv64 GNU/Linux     
```

串口日志（从刷写系统到启动系统）：

[![asciicast](https://asciinema.org/a/nm0tVIpV4py8HErxaQvSMYfEV.svg)](https://asciinema.org/a/nm0tVIpV4py8HErxaQvSMYfEV)

![desktop](./images/image.png)

## 测试结论

测试成功。