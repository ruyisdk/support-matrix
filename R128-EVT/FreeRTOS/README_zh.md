# FreeRTOS R128 EVT 开发套件 测试报告

## 测试环境

### 操作系统信息

- SDK 链接：
    - https://r128.docs.aw-ol.com/r128/get_sdk/
- 测试预编译固件：https://www.aw-ol.com/downloads/resources/126
- 参考文档：
    - https://r128.docs.aw-ol.com/devkit/r128_evt/

### 硬件信息

- TinyVision 开发板


## 安装步骤

### 烧写镜像

下载镜像后，使用 LiveSuit 软件，选择镜像后，连接开发板刷写。

LiveSuit 获取见：https://linux-sunxi.org/LiveSuit

#### LiveSuit

下载并构建：
```bash
git clone https://github.com/linux-sunxi/sunxi-livesuite.git
apt-get install dkms
make
# If you are getting error that /lib/modules/4.4.50+/build is missing try adding symlink to the /usr/src/linux-headers-XXX, for example:
# sudo ln -s /usr/src/linux-headers-3.6-trunk-rpi/ /lib/modules/4.4.50+/build

cp awusb.ko /lib/modules/`uname -r`/kernel/
depmod -a
modprobe awusb
KERNEL=="aw_efex[0-9]*", MODE="0666"
udevadm control --reload-rules
```

运行：
```bash
./LiveSuit.sh
```

### 登录系统

连接 UART3 查看串口输出。

## 预期结果

系统正常启动，能够通过串口查看输出。

## 实际结果

CFT

### 启动信息

屏幕录像：

```log
```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

CFT