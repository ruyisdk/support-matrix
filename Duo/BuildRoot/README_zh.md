# BuildRoot Milk-V Duo 测试报告

## 测试环境

### 操作系统信息

- 系统版本：Duo-V1.1.3
- 下载链接：https://github.com/milkv-duo/duo-buildroot-sdk/releases
- 参考安装文档：https://github.com/milkv-duo/duo-buildroot-sdk

### 硬件信息

- Milk-V Duo 64M
- USB-A to C 或 USB C to C 线缆一条
- microSD 卡一张

## 安装步骤

### 使用 `ruyi` CLI 刷写镜像到 microSD 卡

安装 [`ruyi`](https://github.com/ruyisdk/ruyi) 包管理器，运行 `ruyi device provision` 并按提示操作。

### 登录系统

通过串口登录系统。

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

系统正常启动，成功通过板载串口登录。

### 启动信息

```log
[root@milkv-duo]~# uname -a
Linux milkv-duo 5.10.4-tag- #1 PREEMPT Thu Aug 1 13:44:06 CST 2024 riscv64 GNU/Linux
[root@milkv-duo]~# cat /proc/cpuinfo 
processor	: 0
hart		: 0
isa		: rv64imafdvcsu
mmu		: sv39
```

屏幕录像（从刷写镜像到登录系统）：

[![asciicast](https://asciinema.org/a/1Vp9JeYdRiyORXXGFlx5F9JY0.svg)](https://asciinema.org/a/1Vp9JeYdRiyORXXGFlx5F9JY0)

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。