# Deepin preview LPi4A 测试报告

## 测试环境

### 系统信息

- 系统版本：Deepin preview 20240603
- 下载链接：https://cdimage.deepin.com/RISC-V/preview-20240613-riscv64/deepin-23-beige-preview-riscv64-lpi4a-20240613-122949.tar.xz
- 参考安装文档：https://cdimage.deepin.com/RISC-V/preview-20240517-riscv64/README.md

### 硬件信息

- Lichee Pi 4A (8G RAM + 32GB eMMC)
- 电源适配器
- USB to UART 调试器一个

## 安装步骤

### 获取 u-boot

官方压缩包内不附带 u-boot，需要自己获取，地址为：https://cdimage.deepin.com/RISC-V/beta3-20240205-riscv64/lpi4a/index.html

根据 ram 大小自行选择是否需要 16g 的版本。

### 刷写 bootloader

解压安装套件。
刷入 u-boot 与 boot。

```bash
tar -xvf deepin-23-beige-preview-riscv64-lpi4a-20240613-122949.tar.xz
sudo fastboot flash ram u-boot-with-spl.bin
sudo fastboot reboot
sudo fastboot flash uboot u-boot-with-spl.bin
sudo fastboot flash boot deepin-lpi4a-riscv64-stable-desktop-installer.boot.ext4
```

### 刷写镜像

将 root 分区刷入 eMMC 中。

```bash
sudo fastboot flash root deepin-lpi4a-riscv64-stable-desktop-installer.root.ext4
```

### 登录系统

重启系统后可见安装界面。

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

系统正常启动，成功通过板载串口登录。

### 启动信息

屏幕录像（登录系统）：
[![asciicast](https://asciinema.org/a/8EfjIFC3FLJBBwgOG8nZod4q7.svg)](https://asciinema.org/a/8EfjIFC3FLJBBwgOG8nZod4q7)

![startup](./startup.png)

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。
