# Deepin preview LicheePi 4A 测试报告

## 测试环境

### 系统信息

- 系统版本：Deepin preview 20250122
- 下载链接：https://deepin-community.github.io/sig-deepin-ports/images/riscv/download
- 参考安装文档：https://cdimage.deepin.com/RISC-V/preview-20240517-riscv64/README.md
- 桌面环境: DDE（镜像内预装）

### 硬件信息

- Lichee Pi 4A (8G RAM + 32GB eMMC)
- 电源适配器
- Type-C 数据线一个

## 安装步骤

### 获取镜像

下载安装镜像并解压。

```bash
wget https://ci.deepin.com/repo/deepin/deepin-ports/cdimage/20250122/riscv64/deepin-25-beige-preview-riscv64-th1520-20250122-113934.tar.xz
tar -xvf deepin-25-beige-preview-riscv64-th1520-20250122-113934.tar.xz
```

### 获取 u-boot

官方压缩包内不附带 u-boot，需要自己获取，地址为：https://cdimage.deepin.com/RISC-V/preview-20240815-riscv64/uboot-th1520-revyos.zip

此处使用 8G RAM 版本，采用 8G 版本的 u-boot。在此请根据实际情况选择。

如果使用 8GB 版本的 LicheePi 4A，请使用 `light_lpi4a/u-boot-with-spl.bin`

如果使用 16GB 版本的 LicheePi 4A，请使用 `light_lpi4a_16g/u-boot-with-spl.bin`

```bash
wget https://cdimage.deepin.com/RISC-V/preview-20240815-riscv64/uboot-th1520-revyos.zip
unzip uboot-th1520-revyos.zip
```

### 烧录镜像

使用 `fastboot` 烧录镜像。

```bash
sudo fastboot flash ram light_lpi4a/u-boot-with-spl.bin
sudo fastboot reboot
sudo fastboot flash uboot light_lpi4a/u-boot-with-spl.bin
sudo fastboot flash boot deepin-th1520-riscv64-25-desktop-installer.boot.ext4
sudo fastboot flash root deepin-th1520-riscv64-25-desktop-installer.root.ext4
```

### 登录系统

默认用户名：`root`
密码：`deepin`

初次启动会进入安装界面，自行创建用户。

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

系统正常启动，成功通过板载串口登录。能进入桌面。

### 启动信息

```log
Deepin GNU/Linux 23 deepin-riscv64-th1520 ttyS0

deepin-riscv64-th1520 login: root
Password:
Verification successful
Linux deepin-riscv64-th1520 5.10.113-th1520-revyos-510 #1 SMP PREEMPT Tue Aug 27 10:05:53 UTC 2024 riscv64
Welcome to deepin 25 GNU/Linux

    * Homepage: https://www.deepin.org/

    * Bugreport: https://bbs.deepin.org/


root@deepin-riscv64-th1520:~# uname -a
Linux deepin-riscv64-th1520 5.10.113-th1520-revyos-510 #1 SMP PREEMPT Tue Aug 27 10:05:53 UTC 2024 riscv64 GNU/Linux
root@deepin-riscv64-th1520:~# cat /etc/os-release
PRETTY_NAME="Deepin 25"
NAME="Deepin"
VERSION_CODENAME=beige
ID=deepin
HOME_URL="https://www.deepin.org/"
BUG_REPORT_URL="https://bbs.deepin.org"
VERSION_ID="25"
VERSION="25"
root@deepin-riscv64-th1520:~# lscpu
Architecture:          riscv64
  Byte Order:          Little Endian
CPU(s):                4
  On-line CPU(s) list: 0-3
root@deepin-riscv64-th1520:~#
```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。
