# FreeBSD 14.0 HiFive Unmatched 版本测试报告

## 测试环境

### 操作系统信息

- 系统版本：FreeBSD 14.0
- 下载链接（USTC Mirror）：https://mirrors.ustc.edu.cn/freebsd/releases/riscv/riscv64/ISO-IMAGES/14.0/FreeBSD-14.0-RELEASE-riscv-riscv64-mini-memstick.img.xz
- 参考安装文档：https://wiki.freebsd.org/riscv/HiFiveUnmatched

### 硬件信息

- HiFive Unmatched Rev A
- microUSB 线缆一条（随 HiFive Unmatched 附赠）
- ATX 电源一个
- microSD 卡一张（Sandisk Extreme Pro 64G UHS-I），提前刷入 Freedom U SDK
- U 盘一个（Lexar S25 32G）

## 安装步骤

### 引导设备选择

确保拨码开关已调整为从 microSD 卡引导。若您未更改，出厂默认即为从 microSD 卡引导。

拨码开关应如下设置：`MSEL[3:0]=1011`

### 刷写 Freedom U SDK

从 [此处](https://github.com/sifive/freedom-u-sdk/releases/latest) 获取 demo-coreip-cli-unmatched.rootfs.wic.xz 镜像。

解压并将镜像写入 microSD 卡。其中 `/dev/sdc` 为 microSD 卡所在位置。

```bash
xz -dk demo-coreip-cli-unmatched.rootfs.wic.xz
sudo dd if=demo-coreip-cli-unmatched.rootfs.wic of=/dev/sdc status=progress
```

### 刷写安装镜像到 U 盘

解压镜像，并使用 `dd` 命令写入镜像到 microSD 卡。

```bash
xz -dk FreeBSD-14.0-RELEASE-riscv-riscv64-mini-memstick.img.xz
sudo dd if=FreeBSD-14.0-RELEASE-riscv-riscv64-mini-memstick.img of=/dev/sdc status=progress
```

### 登录系统

通过板载串口（使用 microUSB 线缆连接至其他计算机）登录系统。

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

系统正常启动，成功通过板载串口登录。

### 启动信息

![alt text](image.png)

![alt text](image-1.png)

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。