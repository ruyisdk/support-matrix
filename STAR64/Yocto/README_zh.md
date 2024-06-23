# Yocto Star64 测试报告

## 测试环境

### 操作系统信息

- 下载链接：https://github.com/Fishwaldo/meta-pine64/releases/tag/v2.1
- 参考安装文档：https://github.com/Fishwaldo/meta-pine64

### 硬件信息

- 开发板：Star64
- USB A to C / USB C to C 线缆
- SD 卡

## 安装步骤

### 烧写镜像

下载后，解压并烧写镜像（以下以 plasma 版为例）：
```bash
wget https://github.com/Fishwaldo/meta-pine64/releases/download/v2.1/star64-image-plasma-star64.wic.bz2
bzip2 -kd star64-image-plasma-star64.wic.bz2
sudo dd if=star64-image-plasma-star64.wic of=/dev/your/sdcard bs=1M status=progress
```

### 登录系统

通过串口连接开发板。

启动后，系统会要求用户手动配置用户名、密码、时区、语言等。

Xfce 版本需要配置完成后方可进入桌面。

可通过串口配置。若接入了键盘和显示器，亦可通过键盘配置。

## 预期结果

开发板正常输出启动信息。

## 实际结果

CFT

### 启动信息

屏幕录像（从刷写系统到启动）：


```log
```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

CFT