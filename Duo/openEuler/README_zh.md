# openEuler 23.09 riscv64 Milk-V Duo 测试报告

## 测试环境

### 操作系统信息

- 系统版本：openEuler 23.09 riscv64
- 下载链接：
    - buildroot: https://github.com/milkv-duo/duo-buildroot-sdk.git
    - rootfs: https://mirror.iscas.ac.cn/openeuler-sig-riscv/openEuler-RISC-V/preview/openEuler-23.09-V1-riscv64/openeuler-rootfs.tar.gz
- 参考安装文档：https://blog.inuyasha.love/linuxeveryday/33.html

> Note: 此镜像以 rootfs 方式提供

### 硬件信息

- Milk-V Duo 64M
- USB 电源适配器一个
- microSD 卡一张
- USB to UART 调试器一个（如：CH340, CH341, FT2232 等）
- 杜邦线三根
- Milk-V Duo 本体上预先焊接好调试所需的排针
- 可选：Milk-V Duo IOB（底板）

## 安装步骤

### 构建镜像

#### 编译 buildroot

clone buildroot 以构建镜像
```bash
git clone https://github.com/milkv-duo/duo-buildroot-sdk.git
cd duo-buildroot-sdk/
```

修改 kernel 配置
```bash
cat <<EOF >> build/boards/cv180x/cv1800b_milkv_duo_sd/linux/cvitek_cv1800b_milkv_duo_sd_defconfig
# for openEuler
CONFIG_CGROUPS=y
CONFIG_CGROUP_FREEZER=y
CONFIG_CGROUP_PIDS=y
CONFIG_CGROUP_DEVICE=y
CONFIG_CPUSETS=y
CONFIG_PROC_PID_CPUSET=y
CONFIG_CGROUP_CPUACCT=y
CONFIG_PAGE_COUNTER=y
CONFIG_MEMCG=y
CONFIG_CGROUP_SCHED=y
CONFIG_NAMESPACES=y
CONFIG_OVERLAY_FS=y
CONFIG_AUTOFS4_FS=y
CONFIG_SIGNALFD=y
CONFIG_TIMERFD=y
CONFIG_EPOLL=y
CONFIG_IPV6=y
CONFIG_FANOTIFY
EOF
```

修改 memmap.py 第 43 行为 0

```bash
vim build/boards/cv180x/cv1800b_milkv_duo_sd/memmap.py

ION_SIZE = 0
```

在 Docker 进行编译（推荐）
```bash
docker run -itd --name duodocker -v $(pwd):/home/work milkvtech/milkv-duo:latest /bin/bash
docker exec -it duodocker /bin/bash -c "cd /home/work && cat /etc/issue && ./build.sh milkv-duo-sd"
```

#### 添加 rootfs

拷贝编译好的镜像：

```bash
cd ..
cp duo-buildroot-sdk/out/milkv-duo-sd-20241106-0012.img .
```

写入到 sd 卡中

```bash
sudo dd if=milkv-duo-sd-20241106-0012.img of=/dev/your-device bs=1M status=progress
```

开始准备替换 rootfs。由于原镜像 rootfs 空间不够，需要重新分区。由于我们不用到原有的 rootfs，直接删除原700M左右的rootfs分区，并在原处新建即可：
```bash
sudo fdisk /dev/your-device

# 以下在 fdisk 中
d
2
n
p
2
# 最开始的扇区
# 最后的一个扇区，否则默认会只有 700M 左右
w

# 以下应回到bash
sudo mkfs.ext4 /dev/your-device-p2
```

注：接下来新 rootfs 会被挂在到 mnt，原 rootfs 会被挂载到 mnt2

接下来将 rootfs 解压到我们新创建的分区中：
```bash
mkdir mnt
mkdir mnt2
sudo mount /dev/your-device-p2 mnt
sudo tar -zxvf /path/to/openeuler-rootfs.tar.gz -C mnt
```

接下来挂载原镜像并拷贝一些必要的文件（以下的回环设备请根据实际情况更改）：
```bash
sudo losetup -f -P milkv-duo-sd-20241106-0012.img
sudo mount /dev/loop0p2 mnt2
sudo cp -r mnt2/mnt/system mnt/mnt
sudo cp mnt2/etc/run_usb.sh mnt/etc/
sudo cp mnt2/etc/uhubon.sh mnt/etc/
sudo cp mnt2/etc/init.d/S99user mnt/etc/init.d/
```

接下来准备进入镜像，先创建 DNS 解析：
```bash
echo "nameserver 8.8.8.8" | sudo tee mnt/etc/resolv.conf
```

然后进入镜像：
```bash
chroot mnt
# 更好的也可以使用 arch-chroot mnt
```

安装一些必要的包（如 dhcp 等）：
```bash
dnf install dhcp
cat <<EOF >> /etc/dhcp/dhcpd.conf
subnet 192.168.42.0 netmask 255.255.255.0 {
        option routers 192.168.42.1;
        range 192.168.42.100 192.168.42.200;
}
EOF
```

umount
```bash
exit
sudo umount mnt
sudo umount mnt2
```

### 登录系统

注意 RNDIS 不一定可用，建议备上串口。

通过串口登录系统。

用户名：`root`
密码：`openEuler12#$`

> 注意：Duo 性能较弱，可能会在登录提示处假死数分钟后才进入系统

## 预期结果

系统正常启动，能够通过串口登录。

## 实际结果

系统正常启动，成功通过串口登录。

### 启动信息

屏幕录像（跳过编译，从创建镜像到登录系统）：

[![asciicast](https://asciinema.org/a/eoIznNZpjPZSb9mI2NE4wwdzQ.svg)](https://asciinema.org/a/eoIznNZpjPZSb9mI2NE4wwdzQ)

```log
[  OK  ] Started Show Plymouth Boot Screen.
[  OK  ] Started Forward Password R…s to Plymouth Directory Watch.
[  OK  ] Reached target Path Units.
[  OK  ] Reached target Basic System.
         Starting NTP client/server...
         Starting D-Bus System Message Bus...
         Starting Restore /run/initramfs on shutdown...
         Starting Update RTC With System Clock...
         Starting irqbalance daemon...
[  OK  ] Started libstoragemgmt plug-in server daemon.
         Starting Authorization Manager...
[  OK  ] Started Hardware RNG Entropy Gatherer Daemon.
         Starting Self Monitoring a…g Technology (SMART) Daemon...
         Starting OpenSSH ecdsa Server Key Generation...
         Starting OpenSSH ed25519 Server Key Generation...
         Starting OpenSSH rsa Server Key Generation...
         Starting User Login Management...
         Starting Run a configured … scripts at system startup....
[  OK  ] Started D-Bus System Message Bus.
[  OK  ] Finished Restore /run/initramfs on shutdown.
[  OK  ] Finished Update RTC With System Clock.
[  OK  ] Started irqbalance daemon.
[  OK  ] Finished OpenSSH ecdsa Server Key Generation.
[  OK  ] Finished OpenSSH ed25519 Server Key Generation.
[  OK  ] Reached target Sound Card.
[  OK  ] Started Self Monitoring an…ing Technology (SMART) Daemon.
[  OK  ] Started NTP client/server.
[  OK  ] Started Authorization Manager.
         Starting firewalld - dynamic firewall daemon...
[  OK  ] Finished Run a configured …ap scripts at system startup..
[  OK  ] Started User Login Management.
[  OK  ] Started PC/SC Smart Card Daemon.
[  OK  ] Started firewalld - dynamic firewall daemon.
[  OK  ] Reached target Preparation for Network.
         Starting Network Manager...
[  OK  ] Finished OpenSSH rsa Server Key Generation.
[  OK  ] Reached target sshd-keygen.target.
[  OK  ] Stopped firewalld - dynamic firewall daemon.
         Starting firewalld - dynamic firewall daemon...
[  OK  ] Started Network Manager.
[  OK  ] Reached target Network.
         Starting Network Manager Wait Online...
         Starting GSSAPI Proxy Daemon...
         Starting /etc/rc.d/rc.local Compatibility...
         Starting OpenSSH server daemon...
         Starting Dynamic System Tuning Daemon...
[  OK  ] Started /etc/rc.d/rc.local Compatibility.
[  OK  ] Started GSSAPI Proxy Daemon.
[  OK  ] Reached target NFS client services.
[  OK  ] Reached target Preparation for Remote File Systems.
[  OK  ] Reached target Remote File Systems.
         Starting Hostname Service...
         Starting Permit User Sessions...
[  OK  ] Started OpenSSH server daemon.
[  OK  ] Finished Permit User Sessions.
[  OK  ] Started Deferred execution scheduler.
[  OK  ] Started Command Scheduler.
         Starting Hold until boot process finishes up...
         Starting Terminate Plymouth Boot Screen...
[  OK  ] Finished Hold until boot process finishes up.
[  OK  ] Finished Terminate Plymouth Boot Screen.

openEuler 23.09
Kernel 5.10.4-tag- on an riscv64

openeuler-riscv64 login: root
openEuler12#$
Password: 
login: timed out after 60[FAILED] Failed to start Dynamic System Tuning Daemon.
[FAILED] Failed to start firewalld - dynamic firewall daemon.
[  275.471596] bm-dwmac 4070000.ethernet end0: PHY [stmmac-0:00] driver [Generic PHY] (irq=POLL)
[  275.564174] dwmac1000: Master AXI performs any burst length
[  275.612691] bm-dwmac 4070000.ethernet end0: No Safety Features support found
[  275.658329] bm-dwmac 4070000.ethernet end0: IEEE 1588-2002 Timestamp supported
[  275.746979] bm-dwmac 4070000.ethernet end0: configuring for phy/rmii link mode

openEuler 23.09
Kernel 5.10.4-tag- on an riscv64

openeuler-riscv64 login: root
Password: 


Welcome to 5.10.4-tag-

System information as of time:  Mon Sep 18 08:06:49 CST 2023

System load:    8.62
Processes:      67
Memory used:    79.0%
Swap used:      0.0%
Usage On:       7%
Users online:   1


[root@openeuler-riscv64 ~]# ./neofetch
-bash: ./neofetch: No such file or directory
[root@openeuler-riscv64 ~]# uname -a
Linux openeuler-riscv64 5.10.4-tag- #1 PREEMPT Tue Nov 5 23:54:15 CST 2024 riscv64 riscv64 riscv64 GNU/Linux
[root@openeuler-riscv64 ~]# cat /etc/os-release
NAME="openEuler"
VERSION="23.09"
ID="openEuler"
VERSION_ID="23.09"
PRETTY_NAME="openEuler 23.09"
ANSI_COLOR="0;31"

[root@openeuler-riscv64 ~]# 

```



## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。