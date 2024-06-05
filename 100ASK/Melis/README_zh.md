# Melis 100ASK-V853-PRO 测试报告

## 测试环境

### 操作系统信息

- 镜像链接：https://bbs.aw-ol.com/assets/uploads/files/1657169725953-e6e69a0f-5837-4840-99fe-8bc62c7abbf2-tina_v853-vision_uart0.img
- 参考文档：https://v853.docs.aw-ol.com/

### 硬件信息

- 100ASK-V853-PRO 开发板


## 安装步骤

### 刷写镜像（sd 卡）

将镜像刷写到 sd 卡：
```shell
dd if=1657169725953-e6e69a0f-5837-4840-99fe-8bc62c7abbf2-tina_v853-vision_uart0.img of=/dev/your/device bs=1M status=progress
```

将卡插入到设备启动。

### 刷写镜像（板载 EMMC）

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

连接 UART3 查看串口输出。

## 预期结果

系统正常启动，能够通过串口查看输出。

## 实际结果

系统正常启动，成功通过串口查看输出。

### 启动信息

屏幕录像：

```log
```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

CFT