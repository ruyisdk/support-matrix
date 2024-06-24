# Buildroot VisionFive 测试报告

## 测试环境

### 系统信息

- 系统版本：Buildroot
- 源码链接：https://buildroot.org/download.html
    - 截止本文编写时，Buildroot 的最新稳定 / LTS 版本为：[buildroot-2024.02.1](https://buildroot.org/downloads/buildroot-2024.02.1.tar.gz)
- 参考安装文档：https://gitlab.com/buildroot.org/buildroot/-/tree/master/board/visionfive?ref_type=heads
- 构建机系统：Arch Linux x86_64

### 硬件信息

- StarFive VisionFive (v1)
- 电源适配器
- USB A to C 或 C to C 线缆一条
- microSD 卡一张
- USB to UART 调试器一个

## 构建及刷写镜像

由于 VisionFive 的 Buildroot 已经主线化，直接从 Buildroot 获取源码即可构建出可用镜像。

### 准备构建环境

```shell
sudo pacman -S which sed make binutils diffutils gcc bash patch gzip bzip2 perl tar cpio unzip rsync file bc findutils wget
# 或者从 AUR 安装，需要 AUR Helper，如 yay, paru 等
# paru -S buildroot-meta
```

若您不使用 Arch Linux，请参考 [官方文档](https://buildroot.org/downloads/manual/manual.html#requirement) 安装所需依赖（注意，软件包名称可能不一致）。

### 构建镜像

```shell
wget https://buildroot.org/downloads/buildroot-2024.02.1.tar.gz
tar xvf buildroot-2024.02.1.tar.gz
cd buildroot-2024.02.1/
make visionfive_defconfig
make -j$(nproc)
```

Note: 请确保您的互联网连接正常，编译过程中会自动下载依赖。

构建结束后将在 `output/images` 生成 `sdcard.img` 镜像。

### 烧录镜像至 microSD 卡

使用 `dd` 将镜像写入 microSD 卡。

此处以 `/dev/sdc` 为存储卡位置。

```shell
sudo wipefs -af /dev/sdc
sudo dd if=~/buildroot-2024.02.1/output/images/sdcard.img of=/dev/sdc bs=1M status=progress oflag=direct
```

### 登录系统

通过串口登录系统。

默认用户名： `root`

默认密码：无，输入用户名后自动登录

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

系统正常启动，成功通过板载串口登录。

### 启动信息

```log
Welcome to Buildroot                                                                                                                
buildroot login: root                                                                                                               
# uname -a                                                                                                                          
Linux buildroot 6.0.0-visionfive #1 SMP Wed Mar 27 20:54:25 CST 2024 riscv64 GNU/Linux                                              
# starfive-drm soc:display-subsystem: [drm] Cannot find any crtc or sizes                                                           
# cat /etc/os-release                                                                                                               
NAME=Buildroot                                                                                                                      
VERSION=2024.02.1                                                                                                                   
ID=buildroot                                                                                                                        
VERSION_ID=2024.02.1                                                                                                                
PRETTY_NAME="Buildroot 2024.02.1"                                                                                                   
# 
```

屏幕录像（从刷写镜像到登录系统）：

[![asciicast](https://asciinema.org/a/jCbFkO6AUUriql5b1g7QzGuXD.svg)](https://asciinema.org/a/jCbFkO6AUUriql5b1g7QzGuXD)

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。