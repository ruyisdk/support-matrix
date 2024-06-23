# RevyOS Meles 版本测试报告

## 测试环境

### 操作系统信息

- 系统版本：root-meles-20231210_134926.ext4.tar.gz
- 下载链接：https://github.com/milkv-meles/meles-images/releases
- 参考安装文档：https://milkv.io/zh/docs/meles/getting-started/boot

### 硬件信息

- Milk-V Meles 4GB/8GB
- eMMC 模组 > 16GB
- USB A to C 线缆一条
- 可选：USB-TTL 调试器一个
- 可选：键盘、显示器、鼠标（测试图形界面）

## 安装步骤

### 使用 `fastboot` 刷写镜像至开发板

从 [GitHub release](https://github.com/milkv-meles/meles-images/releases) 下载系统镜像和 U-Boot SPL。

u-boot-with-spl 版本选择：
- 4GB 版本 -> u-boot-with-spl-**single**rank.bin
- 8GB 版本 -> u-boot-with-spl-**dual**rank.bin

按住开发板 GPIO 接口附近的下载按钮并将开发板连接至计算机。

检查连接状态：

```shell
$ lsusb | grep T-HEAD
Bus 001 Device 045: ID 2345:7654 T-HEAD USB download gadget
```

接下来使用 `fastboot` 刷写镜像。

如果出现 `fastboot` 不识别设备、无法刷写等情况，请检查设备连接，并尝试以特权用户身份（`sudo`）执行 `fastboot`。

```shell
fastboot flash ram u-boot-with-spl-dualrank.bin
fastboot reboot
fastboot flash uboot u-boot-with-spl-dualrank.bin
fastboot flash boot boot.ext4
tar xvf root-meles-20231210_134926.ext4.tar.gz
fastboot flash root root-meles-20231210_134926.ext4
```

### 登录系统

通过串口或图形界面登录系统。

默认用户名：`debian`
默认密码：`debian`

## 预期结果

系统正常启动，能够通过串口登录。

## 实际结果

CFT

### 启动信息

CFT

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

CFT