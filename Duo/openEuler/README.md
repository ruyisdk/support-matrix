# openEuler 23.03 riscv64 Milk-V Duo 测试报告

## 测试环境

### 操作系统信息

- 系统版本：openEuler 23.03 riscv64
- 下载链接：
    - buildroot: https://github.com/milkv-duo/duo-buildroot-sdk.git
    - rootfs: https://mirror.iscas.ac.cn/openeuler-sig-riscv/openEuler-RISC-V/preview/openEuler-23.03-V1-riscv64/openeuler-rootfs.tar.gz
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
docker exec -it duodocker /bin/bash -c "cd /home/work && cat /etc/issue && ./build.sh milkv-duo"
```

#### 添加 rootfs

拷贝编译好的镜像：

```bash
cd ..
cp duo-buildroot-sdk/out/milkv-duo-20240326-1620.img .
```

写入到 sd 卡中

```bash
sudo dd if=milkv-duo-20240326-1620.img of=/dev/your-device bs=1M status=progress
```

开始准备替换 rootfs。由于原镜像 rootfs 空间不够，需要重新分区。由于我们不用到原有的 rootfs，直接删除原分区即可：
```bash
sudo fdisk /dev/your-device

# 以下在 fdisk 中
d
3
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
sudo losetup -f -P milkv-duo-20240326-1620.img
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

## 预期结果

系统正常启动，能够通过串口登录。

## 实际结果

系统正常启动，成功通过串口登录。

### 启动信息

屏幕录像（跳过编译，从创建镜像到登录系统）：

[![asciicast](https://asciinema.org/a/eoIznNZpjPZSb9mI2NE4wwdzQ.svg)](https://asciinema.org/a/eoIznNZpjPZSb9mI2NE4wwdzQ)

```log
openEuler 23.03
Kernel 5.10.4-tag- on an riscv64

openeuler-riscv64 login: root
Password: 
Last failed login: Thu Jan  1 08:00:58 CST 1970 on ttyS0
There were 2 failed login attempts since the last successful login.


Welcome to 5.10.4-tag-

System information as of time:  Thu Jan  1 08:00:30 CST 1970

System load:    1.68
Processes:      70
Memory used:    61.2%
Swap used:      0.0%
Usage On:       3%
Users online:   1


[root@openeuler-riscv64 ~]# ./neofetch 
                 `.cc.`                                                                                                         
             ``.cccccccc..`                ---------------------- 
          `.cccccccccccccccc.`             OS: openEuler 23.03 riscv64 
      ``.cccccccccccccccccccccc.``         Host: Milk-V Duo 
   `..cccccccccccccccccccccccccccc..`      Kernel: 5.10.4-tag- 
`.ccccccccccccccc/++/ccccccccccccccccc.`   Uptime: 35 secs 
.cccccccccccccccmNMMNdo+oso+ccccccccccc.   Shell: bash 5.1.9 
.cccccccccc/++odms+//+mMMMMm/:+syso/cccc   Terminal: /dev/ttyS0 
.cccccccccyNNMMMs:::/::+o+/:cdMMMMMmcccc   CPU: (1) 
.ccccccc:+NmdyyhNNmNNNd:ccccc:oyyyo:cccc   Memory: 38MiB / 54MiB 
.ccc:ohdmMs:cccc+mNMNmyccccccccccccccccc
.cc/NMMMMMo////:c:///:cccccccccccccccccc                           
.cc:syysyNMNNNMNyccccccccccccccccccccccc                           
.cccccccc+MMMMMNyc:/+++/cccccccccccccccc
.cccccccccohhhs/comMMMMNhccccccccccccccc
.ccccccccccccccc:MMMMMMMM/cccccccccccccc
.ccccccccccccccccsNNNNNd+cccccccccccccc.
`..cccccccccccccccc/+/:cccccccccccccc..`
   ``.cccccccccccccccccccccccccccc.``
       `.cccccccccccccccccccccc.`
          ``.cccccccccccccc.``
              `.cccccccc.`
                 `....`

[root@openeuler-riscv64 ~]# uname -a
Linux openeuler-riscv64 5.10.4-tag- #1 PREEMPT Tue Mar 26 16:08:05 CST 2024 riscv64 riscv64 riscv64 GNU/Linux
[root@openeuler-riscv64 ~]# cat /etc/os-release 
NAME="openEuler"
VERSION="23.03"
ID="openEuler"
VERSION_ID="23.03"
PRETTY_NAME="openEuler 23.03"
ANSI_COLOR="0;31"

[root@openeuler-riscv64 ~]# 
```



## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。