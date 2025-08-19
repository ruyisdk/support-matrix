# FreeRTOS Sipeed M1s Dock 测试报告

## 测试环境

### 操作系统信息

- 下载链接：
    - SDK：https://gitee.com/Sipeed/M1s_BL808_SDK
    - examples：https://gitee.com/Sipeed/M1s_BL808_example
    - 烧录工具：https://dev.bouffalolab.com/download
- 参考安装文档：https://wiki.sipeed.com/hardware/zh/maix/m1s/other/start.html

### 硬件信息

- Sipeed M1s Dock
- type-c 线一根

## 安装步骤

### 获取 SDK 和工具链

clone 相关仓库到工作目录：
```bash
git clone https://gitee.com/Sipeed/M1s_BL808_example.git
git clone https://gitee.com/sipeed/M1s_BL808_SDK.git
```

获取工具链：
```bash
mkdir -p M1s_BL808_SDK/toolchain
cd M1s_BL808_SDK/toolchain
git clone https://gitee.com/wonderfullook/m1s_toolchain.git
mv m1s_toolchain Linux_x86_64
cd ../../
```

配置环境变量：
```bash
cd M1s_BL808_SDK
export BL_SDK_PATH=$(pwd)
cd ..
```

### 编译

编译 hello_world 例程：
```bash
cd M1s_BL808_example/c906_app
./build.sh hello_world
```

### U 盘方式刷写程序

使用 type-c 线连接电脑和**标有 OTG**的 C 口，能看到电脑新插入了一个 U 盘：
```log
[66939.561779] usb-storage 3-2:1.0: USB Mass Storage device detected
[66939.562424] scsi host0: usb-storage 3-2:1.0
[66940.569292] scsi 0:0:0:0: Direct-Access     Bouffalo Product          0.01 PQ: 0 ANSI: 2
[66940.570788] sd 0:0:0:0: [sda] 2048 4096-byte logical blocks: (8.39 MB/8.00 MiB)
[66940.570915] sd 0:0:0:0: [sda] Write Protect is off
[66940.570917] sd 0:0:0:0: [sda] Mode Sense: 03 00 00 00
[66940.571039] sd 0:0:0:0: [sda] No Caching mode page found
[66940.571040] sd 0:0:0:0: [sda] Assuming drive cache: write through
[66940.574351]  sda: sda1
[66940.574557] sd 0:0:0:0: [sda] Attached SCSI removable disk

```

将 build_out 下 d0fw.bin 移动到检测到的 U 盘中，根据实际替换下面的设备名：
```bash
mkdir mnt
sudo mount /dev/sdX1 mnt
sudo mv build_out/d0fw.bin mnt/
sudo umount mnt
rm -r mnt
```

### 串口方式刷写程序

使用 type-c 线连接电脑和**标有 UART**的 C 口

构建 firmware：
```bash
cd M1s_BL808_example/e907_app
./build.sh firmware
```

下载烧录工具后使用对应系统的工具烧录。

上电后，先按住 boot，再按 rst，再松开 boot。

### 连接串口

将 type-c 线连接到**标有 UART**的 C 口。

## 预期结果

系统正常启动，能够看到串口输出。

## 实际结果

系统正常启动，能够看到串口输出。

### 启动信息

```log
Starting bl808 now....
Heap Info: 63460 KB @ [0x0x0000000050206f28 ~ 0x0x0000000054000000]
[OS] Starting aos_loop_proc task...
[OS] Start c906 xram handle...
[OS] Starting OS Scheduler...
init ring:0,tx:0x0000000022020140,rx:0x0000000000000000
init ring:2,tx:0x0000000022021340,rx:0x0000000022020340
init ring:3,tx:0x0000000022022540,rx:0x0000000022022340
init ring:4,tx:0x0000000022022840,rx:0x0000000022022740
init ring:5,tx:0x0000000000000000,rx:0x0000000000000000
Init CLI with event Driven
hello, world!
hello, world!
hello, world!

```

屏幕录像：

[![asciicast](https://asciinema.org/a/nYT21u4uOzQ7d7k5KF2Ge6633.svg)](https://asciinema.org/a/nYT21u4uOzQ7d7k5KF2Ge6633)

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。