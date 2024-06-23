# FreeBSD MangoPi MQ Pro 测试报告

## 测试环境

### 操作系统信息

- 下载链接：https://github.com/freebsd-d1/freebsd-d1
- 参考安装文档：https://github.com/freebsd-d1/freebsd-d1

### 硬件信息

- MangoPi MQ Pro
- 电源适配器
- microSD 卡一张
- USB to UART 调试器一个

## 安装步骤

### 刷写镜像

clone 仓库并生成镜像：

```bash
gmake
dd if=freebsd-d1.img of=/dev/your/device
```

### 登录系统

通过串口登录系统。

默认用户名：`root`
第一次后会设置密码

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