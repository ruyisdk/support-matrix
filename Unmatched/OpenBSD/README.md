# OpenBSD 7.4 HiFive Unmatched 版本测试报告

## 测试环境

### 操作系统信息

- 系统版本：OpenBSD 7.4
- 下载链接（USTC Mirror）：https://mirrors.tuna.tsinghua.edu.cn/OpenBSD/7.4/riscv64/install74.img
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

使用 `dd` 命令写入镜像到 microSD 卡。

```bash
sudo dd if=install74.img of=/dev/sdc status=progress
```

### 登录系统

通过板载串口（使用 microUSB 线缆连接至其他计算机）登录系统。

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

系统正常启动，成功通过板载串口登录。

### 启动信息

![image](https://github.com/ruyisdk/ruyi/assets/17025286/1b1f5549-3be5-4d57-920d-a006c7f2e026)

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。