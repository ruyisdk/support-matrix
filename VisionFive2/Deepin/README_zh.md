# Debian VisionFive 2 版本测试报告

## 测试环境

### 操作系统信息

- 系统版本：Deepin 23 preview
- 下载链接：https://cdimage.deepin.com/RISC-V/preview-20240613-riscv64/deepin-23-beige-preview-riscv64-visionfive2-20240613-125619.tar.xz
- 参考安装文档：https://cdimage.deepin.com/RISC-V/VisionFive-v2-image/README.txt

### 硬件信息

- StarFive VisionFive 2
- USB 电源适配器一个
- USB-A to C 或 C to C 线缆一条
- microSD 卡一张
- USB to UART 调试器一个（如：CH340, CH341, FT2232 等）
- 杜邦线三根

## 安装步骤

### 解压并刷写镜像到 microSD 卡

假定 `/dev/sda` 为存储卡。

```bash
tar -xvf deepin-23-beige-preview-riscv64-visionfive2-20240613-125619.tar.xz
sudo dd if=deepin-visionfive2-riscv64-stable-desktop-installer.img of=/dev/sda bs=1M status=progress
```

#### Issue: Kernel panic

如果你看到了类似于：
```log
Kernel panic - not syncing: VFS: Unable to mount root fs on unknown-block(0,0)
```

你需要手动修复镜像中的启动文件。运行 `blkid`，应当出现如下 log：
```log
/dev/sda4: LABEL="root" UUID="4c4bc538-15f7-4687-8509-d02d23d09b15" BLOCK_SIZE="4096" TYPE="ext4" PARTLABEL="root" PARTUUID="a8a69a6c-a25e-4d7a-939c-f539566a1fdd"
/dev/sda2: PARTLABEL="uboot" PARTUUID="f8dee89e-c53b-48ef-bb3f-ff25b8a25cbf"
/dev/sda3: UUID="847A-3FD4" BLOCK_SIZE="512" TYPE="vfat" PARTLABEL="image" PARTUUID="d1acffb2-3c52-4b50-a25e-63330675c57f"
/dev/sda1: PARTLABEL="spl" PARTUUID="a4afe21c-10a5-4111-a88e-639128d69b2c"
```

记下第四分区的 PARTUUID，如上是 `a8a69a6c-a25e-4d7a-939c-f539566a1fdd`。

挂载第三分区，修改 extlinux/extlinux.conf 文件。将其中的 `root=LABEL=root` 替换为 `root=PARTUUID=$(your partuuid)`

解挂载后重新在开发板上启动，现在它应该正常了。


### 引导模式选择

StarFive VisionFive 2 提供了多种引导模式，可在上电前通过板载拨码开关进行配置；开发板本体上亦有丝印标注。

为了启动原厂 Debian 镜像，可以选择 1-bit QSPI Nor Flash 模式（即：`RGPIO_0 = 0`, `RGPIO_1 = 0`）。注意，此模式可能需要提前更新 Flash 内的固件，若您启动不成功，请参考官方文档进行固件升级：[更新 SPL 和 U-Boot](https://doc.rvspace.org/VisionFive2/Quick_Start_Guide/VisionFive2_QSG/spl_u_boot_0.html)

若不更新固件，请选择 microSD 卡引导（即：`RGPIO_0 = 1`, `RGPIO_1 = 0`）。

> 注意，此模式下有小概率出现启动失败的情况，如遇到启动失败，串口输出类似如下信息：
>
>```log
>dwmci_s: Response Timeout.                                                                                            
>dwmci_s: Response Timeout.                                                                                            
>BOOT fail,Error is 0xffffffff
>```
>
> 您可以尝试重新给开发板上电，或点按一下 USB Type-C 供电接口附近的按钮。通常这可以解决无法启动的问题。

### 登录系统

通过串口登录系统。

默认用户名：`root`
默认密码：`deepin`

## 预期结果

系统正常启动，能够通过串口登录。

## 实际结果

修改启动配置后，系统正常启动，成功通过串口登录。

### 启动信息

```log
Deepin GNU/Linux 23 deepin-riscv64-visionfive2 ttyS0

deepin-riscv64-visionfive2 login: root
Password:
Verification successful
Linux deepin-riscv64-visionfive2 6.6.20-visionfive2-66y #1 SMP Tue May 28 03:46:53 UTC 2024 riscv64
Welcome to Deepin 23 GNU/Linux

    * Homepage:https://www.deepin.org/

    * Bugreport:https://bbs.deepin.org/


root@deepin-riscv64-visionfive2:~# uname -a
Linux deepin-riscv64-visionfive2 6.6.20-visionfive2-66y #1 SMP Tue May 28 03:46:53 UTC 2024 riscv64 GNU/Linux
root@deepin-riscv64-visionfive2:~# cat /etc/os
os-release  os-version  ostree/     
root@deepin-riscv64-visionfive2:~# cat /etc/os-release 
PRETTY_NAME="Deepin 23"
NAME="Deepin"
VERSION_ID="23"
VERSION="23"
ID=Deepin
HOME_URL="https://www.deepin.org/"
BUG_REPORT_URL="https://bbs.deepin.org"
VERSION_CODENAME=beige

```

屏幕录像（从刷写镜像到登录系统）：
[![asciicast](https://asciinema.org/a/oZhyQXdhDgf2uzT8EZSshqcim.svg)](https://asciinema.org/a/oZhyQXdhDgf2uzT8EZSshqcim)

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试部分成功。