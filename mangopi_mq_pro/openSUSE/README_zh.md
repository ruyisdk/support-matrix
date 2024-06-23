# Armbian MangoPi MQ Pro 测试报告

## 测试环境

### 操作系统信息

- 下载链接：https://download.opensuse.org/repositories/devel:/RISCV:/Factory:/Contrib:/AllwinnerD1/images/openSUSE-Tumbleweed-RISC-V-JeOS-mangopimqpro.riscv64.raw.xz
- 参考安装文档：https://en.opensuse.org/HCL:MangoPi_MQ-Pro

### 硬件信息

- MangoPi MQ Pro
- 电源适配器
- microSD 卡一张
- USB to UART 调试器一个

## 安装步骤

### 刷写镜像

使用 `xz` 解压镜像。
使用 `dd` 将镜像写入 microSD 卡。

```bash
xzcat openSUSE-Tumbleweed-RISC-V-JeOS-mangopimqpro.riscv64.raw.xz.raw.xz | dd bs=4M of=/dev/your/device iflag=fullblock oflag=direct status=progress; sync
```

### 登录系统

通过串口登录系统。

默认用户名： `root`
默认密码： `linux`

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