# Ubuntu BeagleV-Fire 测试报告

## 测试环境

### 操作系统信息

- 下载链接：https://files.beagle.cc/file/beagleboard-public-2021/images/beaglev-fire-ubuntu-23.04-20231121.zip
- 参考安装文档：https://docs.beagleboard.org/latest/boards/beaglev/fire/demos-and-tutorials/flashing-board.html

### 硬件信息

- BeagleV-Fire
- USB-C 电源适配器 / DC 电源一个
- USB-UART 调试器一个

## 安装步骤

### 刷写 Gatware 模块

**理论上 Gatware 已经刷写好，开箱即用。**

### 升级 Gatware

**升级 Gatware 可直接在板上自带 Linux 中进行**，见[官方文档](https://docs.beagleboard.org/latest/boards/beaglev/fire/demos-and-tutorials/gateware/upgrade-gateware.html)

进入 Linux 命令行后（SSH、UART 等均可）
```bash
sudo apt install bbb.io-gateware
sudo apt update
sudo apt upgrade
cd /usr/share/beagleboard/gateware
. ./change-gateware.sh default
```

### 刷写 Gatware

在这里下载 FlashPro Express：
https://www.microchip.com/en-us/products/fpgas-and-plds/fpga-and-soc-design-tools/programming-and-debug

解压后安装：
```bash
./launch_installer.sh
```

运行软件：
```bash
/home/$(user)/microchip/Program_Debug_v202X.Y/Program_Debug_Tool/bin/FPExpress
```

下载 FlashProExpress.zip，其中包含所需的工程文件（ *.job）

创建工程并刷写（连接开发板）：
![alt text](image.png)
- 选择工作文件
- 选择工程地点
- 确认

![alt text](image-1.png)
- 选择 Program 动作
- 点击执行

### 烧写镜像

同时使用串口和 USB 线连接电脑，打开串口连接开发板。

在出现 DDR Training 的加载条后，按动 \[a-zA-Z0-9\] 的任意键打断启动，然后手动进行：
```bash
>> mmc
>> usbdmsc
```

你应当看到电脑上连接了一个新的存储设备。将镜像刷入：
```bash
sudo dd if=sdcard.img of=/dev/your/device bs=1M status=progress
```

### 登录系统

通过串口登录系统。

默认用户名： `root`
默认密码：无密码

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
