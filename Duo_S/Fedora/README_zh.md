# Fedora 41 Milk-V Duo 测试报告

## 测试环境

### 操作系统信息

- 系统版本：Fedora 41
- 下载链接：https://mirror.iscas.ac.cn/fedora-riscv/dl/Milk-V/DuoS/images/latest/
- 参考安装文档：https://fedoraproject.org/wiki/Architectures/RISC-V/Installing

> Note: 此镜像为社区开发者提供，非官方镜像。

### 硬件信息

- Milk-V Duo S
- USB 电源适配器一个
- USB-A to C 或 USB C to C 线缆一条
- microSD 卡一张
- USB to UART 调试器一个（如：CH340, CH341, FT2232 等）
- 杜邦线三根
- Milk-V Duo 本体上预先焊接好调试所需的排针
- 可选：Milk-V Duo IOB（底板）

## 安装步骤

### 使用 `dd` 刷写镜像到 microSD 卡

```shell
zcat milkv-duos-fedora-minimal.img.gz | sudo dd of=/dev/sdX bs=4M iflag=fullblock status=progress 
```

### 登录系统

通过串口登录系统。

用户名：`root`
密码：`riscv`

## 预期结果

系统正常启动，能够通过串口登录。

## 实际结果

系统正常启动，成功通过板载串口登录。

启动流程屏幕录像：

[![asciicast](https://asciinema.org/a/5dJWtw2u1EB1f78SyIeFJ4Jqd)](https://asciinema.org/a/5dJWtw2u1EB1f78SyIeFJ4Jqd)

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。
