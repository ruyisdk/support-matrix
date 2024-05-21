# Bianbu 香蕉派 BPI-F3 测试报告

## 测试环境

### 系统信息

- 下载链接：
  - 百度网盘：https://pan.baidu.com/s/1zvFkX92f5gpZdKjP-vGJvA?pwd=8888 (pincode: 8888)
  - 谷歌网盘：https://drive.google.com/drive/folders/1kCHiMwjnhvZaRBy5vkj6UlPeAlpRQ14P?usp=sharing
- 参考安装文档：https://docs.banana-pi.org/en/BPI-F3/GettingStarted_BPI-F3

### 硬件信息

- 香蕉派 BPI-F3
- 电源适配器
- microSD 卡一张
- USB to UART 调试器一个

## 安装步骤

### 刷写镜像（sd 卡）

下载并解压镜像后，使用 `dd` 将镜像写入 microSD 卡。

```bash
xz -kd Armbian-bpi-SpacemiT_24.5.0-trunk_Bananapif3_noble_legacy_6.1.15_xfce_desktop.img.xz
sudo dd if=/path/to/Armbian-bpi-SpacemiT_24.5.0-trunk_Bananapif3_noble_legacy_6.1.15_xfce_desktop.img of=/dev/your-device bs=1M status=progress
```

### 登录系统

通过串口登录系统。

默认用户名： `root`

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

系统正常启动，成功通过板载串口登录。

### 启动信息

屏幕录像（从刷写镜像到登录系统）：


```log
```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

CFT