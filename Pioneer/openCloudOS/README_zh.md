# openCloudOS-Stream 23 Pioneer 测试报告

## 测试环境

### 操作系统信息

- 系统版本：openCloudOS-Stream 23
- 下载链接：[http://43.139.5.209/sdcard-img/](http://43.139.5.209/sdcard-img/)
  - 固件: [https://mirror.iscas.ac.cn/revyos/extra/images/sg2042/20241230/](https://mirror.iscas.ac.cn/revyos/extra/images/sg2042/20241230/)
- 参考安装文档：[readme.md](http://43.139.5.209/sdcard-img/readme.md)

### 硬件信息

- Milk-V Pioneer Box v1.3
- microSD 卡一张
- USB Type-C 数据线一根（用于连接板载串口）

## 安装步骤

### 刷写镜像

使用 `xz` 解压镜像。
使用 `dd` 将镜像写入 microSD 卡。

```bash
xz -d ocs_developer_sdcard-0.2.img.xz
dd if=ocs_developer_sdcard-0.2.img of=/dev/yout-device bs=4M status=progress
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
[root@riscv64 ~]# uname -a
Linux riscv64.developer.ocs23 6.6.68 #1 SMP Thu Apr 10 17:26:47 CST 2025 riscv64 riscv64 riscv64 GNU/Linux
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
[root@riscv64 ~]# fastfetch 
        #####            root@riscv64
       #######           ------------
       ##O#O##           OS: OpenCloudOS Stream 23 riscv64
       #######           Host: Sophgo Mango
     ###########         Kernel: Linux 6.6.68
    #############        Uptime: 2 mins
   ###############       Packages: 1366 (rpm)
   ################      Shell: bash 5.2.15
  #################      Display (DELL U2719DS): 2048x1080 @ 60 Hz in 27" [External]
#####################    Cursor: Adwaita
#####################    Terminal: vt220
  #################      CPU: mango (64)
                         GPU: AMD Radeon HD 6450/7450/8450 / R5 230 OEM [Discrete]
                         Memory: 1.49 GiB / 124.91 GiB (1%)
                         Swap: Disabled
                         Disk (/): 4.72 GiB / 11.16 GiB (42%) - ext4
                         Local IP (enP2p197s0): 192.168.36.39/22
                         Locale: en_US.UTF-8

                                                 
                                                 
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
[root@riscv64 ~]# 
```

串口日志（从刷写系统到启动系统）：

[![asciicast](https://asciinema.org/a/xGlmsQEUP3IgJDbllh85yLaKA.svg)](https://asciinema.org/a/xGlmsQEUP3IgJDbllh85yLaKA)


## 测试结论

测试成功。