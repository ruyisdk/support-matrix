# Debian MangoPi MQ Pro 测试报告

## 测试环境

### 操作系统信息

- 下载链接：https://popolon.org/depots/RISC-V/D1/ovsienko/RVBoards_D1_Debian_lxde_img_linux_v0.4.1.img.zip
- 参考安装文档：https://popolon.org/depots/RISC-V/D1/ovsienko/_index.html

### 硬件信息

- MangoPi MQ Pro
- 电源适配器
- microSD 卡一张
- USB to UART 调试器一个

## 安装步骤

### 刷写镜像

使用 `unzip` 解压镜像。
使用 `dd` 将镜像写入 microSD 卡。

```bash
unzip /path/to/RVBoards_D1_Debian_lxde_img_linux_v0.4.1.img.zip
sudo dd if=/path/to/RVBoards_D1_Debian_lxde_img_linux_v0.4.1.img of=/dev/your_device bs=1M status=progress
```

### 登录系统

通过串口登录系统。

默认用户名：`root`
默认密码：`rvboards`

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