# Tina Linux D1s NeZha 测试报告

## 测试环境

### 操作系统信息

- 链接：https://pan.baidu.com/s/1v55AKMFripaEu22tJ92lmw?pwd=awol 提取码：awol
- 参考安装文档：https://d1s.docs.aw-ol.com/study/study_1tina/

### 硬件信息

- D1s NeZha
- microSD 卡一张
- USB to UART 调试器一个（如：CH340, CH341, FT2232 等）

## 安装步骤

### 打包镜像

下载并解压后，准备编译 SDK：
```bash
source build/envsetup.sh
lunch
make -j$(nproc)
pack
```

### 烧写镜像

使用 LiveSuit 软件，选择镜像后，连接开发板刷写。

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