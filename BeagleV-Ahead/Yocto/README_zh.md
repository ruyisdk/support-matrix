# Yocto BeagleV-Ahead 测试报告

## 测试环境

### 操作系统信息

- 下载链接：https://files.beagle.cc/file/beagleboard-public-2021/images/xuantie-yocto-1.1.2-20230610.zip
- 参考安装文档：https://docs.beagleboard.org/latest/boards/beaglev/ahead/02-quick-start.html

### 硬件信息

- BeagleV-Ahead
- USB-C 电源适配器 / DC 电源一个
- USB-UART 调试器一个

## 安装步骤

### 刷写镜像

安装 fastboot：
```bash
sudo apt-get install android-sdk-platform-tools
```

解压安装套件。运行自动刷写脚本：

```bash
unzip xuantie-yocto-1.1.2-20230610.zip
sudo ./fastboot_emmc.sh
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
