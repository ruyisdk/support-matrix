# Deepin RISC-V preview Pioneer 测试报告

## 测试环境

### 操作系统信息

- 系统版本：Deepin 23 preview-20240517
- 下载链接：
    - 系统镜像：https://cdimage.deepin.com/RISC-V/preview-20240517-riscv64/deepin-sg2042-riscv64-stable-desktop-installer.tar.xz
        - SJTU 镜像：https://mirror.sjtu.edu.cn/deepin-cd/RISC-V/preview-20240517-riscv64/deepin-sg2042-riscv64-stable-desktop-installer.tar.xz
    - 固件：https://cdimage.deepin.com/RISC-V/preview-20240517-riscv64/sophgo-bootloader-multi-sg2042-dev.zip
        - SJTU 镜像：https://mirror.sjtu.edu.cn/deepin-cd/RISC-V/preview-20240517-riscv64/sophgo-bootloader-multi-sg2042-dev.zip
- 参考安装文档：https://cdimage.deepin.com/RISC-V/preview-20240517-riscv64/README.md

### 硬件信息

- Milk-V Pioneer v1.3
- microSD 卡一张（≥ 512M 即可）
- NVMe SSD 一个（出厂预装）
- 读卡器一个
- NVMe-USB 硬盘盒一个
- USB-A to C 或 C to C 线缆一根
- VGA/HDMI 显示器及对应线缆（本次测试使用了 HDMI 采集卡）
- USB 键盘&鼠标

## 安装步骤

### 解压并刷写镜像到 microSD 卡

使用 `tar` 和 `unzip` 分别解压系统镜像和固件。
使用 `dd` 将镜像写入 microSD 卡。

解压 `sophgo-bootloader-multi-sg2042-dev.zip`，将 `firmware_multi_sg2042-dev.img` 写入 microSD 卡。

抹除 NVMe SSD 上先前已存在的所有分区，重新创建一个 GPT 分区表，新建一个分区，将 ext4 格式的系统镜像写入到此分区。

下述 `/dev/sdX`、`/dev/sdY` 分别为 microSD 卡和 NVMe SSD，请自行变更。

```bash
unzip sophgo-bootloader-multi-sg2042-dev.zip
sudo wipefs -af /dev/sdX
sudo dd if=firmware_multi_sg2042-dev.img of=/dev/sdX bs=1M status=progress
sudo wipefs -af /dev/sdY
sudo fdisk /dev/sdY
# 依次输入 g，n，然后回车确认（三次），最后输入 w 将设置写入硬盘
tar xvf deepin-23-beige-preview-riscv64-sg2042-20240613-124856.tar.xz
sudo dd if=./deepin-sg2042-riscv64-stable-desktop-installer.root.ext4 of=/dev/sdY1 bs=4M status=progress
echo ", +" | sudo sfdisk -N 1 /dev/sdX
sudo resize2fs /dev/sdX1
```

### 登录系统

通过 GUI 登录系统。

登录后选择语言，选择键盘布局

默认用户名：`root`
默认密码：`deepin`

## 预期结果

系统正常启动，能够进入桌面。

## 实际结果

系统成功启动，能够进入设置向导，但无法完成设置流程，未能登录进桌面。

切换到其他 TTY (Ctrl + Alt + F2) 可以登录 Shell。

> 截图为 USB HDMI 采集卡捕获到的画面。

![](image/2024-07-31-15-14-17.png)

设置向导最后一步无法完成，会回到 TTY: 

![](image/2024-07-31-16-00-29.png)

tty 登录：

![](image/2024-07-31-15-14-08.png)

### 启动信息

N/A

屏幕截图：见上方。

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试失败。