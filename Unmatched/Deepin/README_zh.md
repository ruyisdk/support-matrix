# Deepin HiFive Unmatched 测试报告

## 测试环境

### 系统信息

- 系统版本：Deepin
- 下载链接：https://cdimage.deepin.com/RISC-V/Unmatched-image/deepin-sifive.7z
- 参考安装文档：https://cdimage.deepin.com/RISC-V/Unmatched-image/README.txt


### 硬件信息

- HiFive Unmatched Rev A
- microUSB 线缆一条（随 HiFive Unmatched 附赠）
- ATX 电源一个
- NVME 硬盘

## 安装步骤

### 刷写镜像

**该镜像并不适用于 SD 卡，需要 NVME 硬盘**

使用 `7z` 解压镜像。
使用 `dd` 将镜像写入 microSD 卡。

```bash
7z e deepin-sifive.7z
sudo dd if=deepin-sifive.img of=/dev/your/device bs=1M status=progress
```

### 登录系统

通过串口登录系统。

默认用户名： `root`
默认密码： `Riscv2022#`

默认用户名： `deepin`
默认密码： `deepin`

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