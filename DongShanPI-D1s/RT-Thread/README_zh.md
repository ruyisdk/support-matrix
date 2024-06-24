# RT-Thread DongshanPI-D1s 测试报告

## 测试环境

### 操作系统信息

- 下载链接：https://github.com/RT-Thread/rt-thread
- 参考安装文档：https://github.com/RT-Thread/rt-thread/blob/master/bsp/allwinner/d1s/README-MQ_zh.md

### 硬件信息

- DongshanPI-D1s
- microSD 卡一张
- USB to UART 调试器一个（如：CH340, CH341, FT2232 等）

## 安装步骤

### 下载代码

下载 RT-Thread 代码：
```bash
git clone https://github.com/RT-Thread/userapps.git
cd userapps
git clone -b rt-smart https://gitee.com/rtthread/rt-thread.git
```

配置工具链：
```bash
python3 get_toolchain.py riscv64
source smart-env.sh riscv64
```

编译内核：
```bash
scons --menuconfig
source ~/.env/env.sh
pkgs --update
```

### 烧写镜像

分区 SD 卡：前部留 8M 的空间以容纳 bootloadr：
```bash
sudo fdisk /dev/your/device
# 以下在fdisk中
o
n
p
1
16384
w
```

刷入系统到 sd 卡：
```bash
sudo dd if=boot0_sdcard_sun20iw1p1.bin of=/dev/your/device bs=1024 seek=8
sudo dd if=sd.bin of=/dev/your/device bs=1024 seek=56
```

### 登录系统

通过串口登录系统。

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

CFT

### 启动信息


屏幕录像（从刷写镜像到登录系统）：

```log
```


## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

CFT