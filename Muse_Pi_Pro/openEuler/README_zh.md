# SpacemiT Muse Pi Pro, openEuler 24.03-LTS-SP1 测试报告

## 系统信息

- 下载链接：https://images.oerv.ac.cn/board?uri=products/spacemit/muse_pi_pro.json&name=MUSE+Pi+Pro
- 安装文档参考：https://developer.spacemit.com/documentation?token=EIk1wVY9NinD95kMsw0cFM89npd
- 安装文档参考：https://images.oerv.ac.cn/board?uri=products/spacemit/muse_pi_pro.json&name=MUSE+Pi+Pro

### 硬件信息

- SpacemiT Muse Pi Pro 开发板
- USB 充电器
- USB Type-C 数据线
- UART to USB 调试线
- microSD 卡

## 安装步骤

### 刷写固件

原版 Muse Pi Pro 使用 UEFI 作为固件，但 openEuler 使用 U-Boot 和 BootSTD 作为固件。因此，我们需要将固件刷写到 Muse Pi Pro 的 SPI NOR flash 中。

下载固件并解压。然后，使用 `fastboot` 将固件刷写到 SPI NOR flash 中。

```bash
wget https://repo.tarsier-infra.isrc.ac.cn/openEuler-RISC-V/testing/spacemit_k1_20250421/spacemit_k1_fw.tar.zst
tar -xvf spacemit_k1_fw.tar.zst
```

在 USB Type-A 端口下方，可以看到三个按键。让以网口朝上，从上到下，分别是 **PWR**、**RST** 和 **FDL**。你需要在上电/复位时按住 **FDL** 按键，进入 fastboot 模式。你应该能在系统中看到 dfu-device：

```log
❯ sudo fastboot devices
dfu-device       DFU download
```

然后，使用 `fastboot` 将固件刷写到 SPI NOR flash 中。

```bash
fastboot stage FSBL.bin
fastboot continue
sleep 1 # wait for 1s
fastboot stage u-boot.itb
fastboot continue
sleep 1 # wait for 1s
fastboot flash mtd partition.json
fastboot flash mtd-bootinfo bootinfo_spinor.bin
fastboot flash mtd-fsbl FSBL.bin
fastboot flash mtd-opensbi fw_dynamic.itb
fastboot flash mtd-uboot u-boot.itb
```

**注：这将会擦除原有的 UEFI 固件。如何恢复 UEFI 固件将在后面介绍。**

### 刷写镜像到 SD 卡

使用 `dd` 将镜像刷写到 microSD 卡中。

```bash
wget https://repo.tarsier-infra.isrc.ac.cn/openEuler-RISC-V/testing/spacemit_k1_20250421/openEuler-24.03-LTS-SP1-base-spacemit_k1-testing.img.zst
zstd -d openEuler-24.03-LTS-SP1-base-spacemit_k1-testing.img.zst
```

```bash
sudo dd if=openEuler-24.03-LTS-SP1-base-spacemit_k1-testing.img of=/dev/your-device bs=1M status=progress
```

请将 `/dev/your-device` 替换为实际的 microSD 卡设备名称。请务必仔细检查设备名称，以免覆盖自己的磁盘。

### 启动系统

通过串口登陆系统。

默认用户名：`root`/`openeuler`
默认密码：`openEuler12#$`

### 恢复 UEFI 固件


为了恢复 UEFI 固件，你需要将原版 UEFI 固件刷写到 SPI NOR flash 中。你可以在 spacemit bianbu 系统中找到固件。你可以在以下链接找到镜像：
[https://archive.spacemit.com/image/k1/version/bianbu-computer-uefi/](https://archive.spacemit.com/image/k1/version/bianbu-computer-uefi/)

下载固件并解压。然后，使用 `fastboot` 将固件刷写到 SPI NOR flash 中。

```bash
sudo fastboot stage factory/FSBL.bin
sudo fastboot continue
sleep 1 # Wait for 1 sec
sudo fastboot stage edk2.itb
sudo fastboot continue
sleep 1 # wait for 1s
fastboot flash mtd partition_2M.json
fastboot flash mtd-bootinfo factory/bootinfo_spinor.bin
fastboot flash mtd-fsbl factory/FSBL.bin
fastboot flash mtd-env env.bin
fastboot flash mtd-opensbi fw_dynamic.itb
fastboot flash mtd-uboot edk2.itb
```

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

系统正常启动，成功通过板载串口登录。

### 启动信息

串口录制（从刷写镜像到启动）：
[![asciicast](https://asciinema.org/a/UPkandKkjpEHPjdGBsl9CMXjt.svg)](https://asciinema.org/a/UPkandKkjpEHPjdGBsl9CMXjt)

```log
openEuler 24.03 (LTS-SP1)
Kernel 6.6.63-0.0.0.23.oe2403sp1.riscv64 on an riscv64

Activate the web console with: systemctl enable --now cockpit.socket

openeuler-riscv64 login: root
Password: 


Welcome to 6.6.63-0.0.0.23.oe2403sp1.riscv64

System information as of time:  Sat Jan  1 08:00:39 CST 2000

System load:    3.06
Memory used:    1.0%
Swap used:      0.0%
Usage On:       3%
Users online:   1


[root@openeuler-riscv64 ~]# uname -a
Linux openeuler-riscv64 6.6.63-0.0.0.23.oe2403sp1.riscv64 #1 SMP PREEMPT Sun Apr 20 10:21:48 UTC 2025 riscv64 riscv64 riscv64 GNU/Linux
[root@openeuler-riscv64 ~]# cat /etc/os-release 
NAME="openEuler"
VERSION="24.03 (LTS-SP1)"
ID="openEuler"
VERSION_ID="24.03"
PRETTY_NAME="openEuler 24.03 (LTS-SP1)"
ANSI_COLOR="0;31"

[root@openeuler-riscv64 ~]# lscpu
Architecture:          riscv64
  Byte Order:          Little Endian
CPU(s):                8
  On-line CPU(s) list: 0-7
Model name:            Spacemit(R) X60
  Thread(s) per core:  1
  Core(s) per socket:  8
  Socket(s):           1
  Frequency boost:     disabled
  CPU(s) scaling MHz:  100%
  CPU max MHz:         1600.0000
  CPU min MHz:         614.4000
Caches (sum of all):   
  L1d:                 256 KiB (8 instances)
  L1i:                 256 KiB (8 instances)
  L2:                  1 MiB (2 instances)
NUMA:                  
  NUMA node(s):        1
  NUMA node0 CPU(s):   0-7
```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

成功
