# Deepin RISC-V preview Pioneer 测试报告

## 测试环境

### 操作系统信息

- 系统版本：Deepin 23 preview-20240815
- 下载链接：
    - 系统镜像：https://ci.deepin.com/repo/deepin/deepin-ports/cdimage/20240815/riscv64/deepin-23-beige-preview-riscv64-sg2042-20240815-125146.tar.xz
    - 固件：https://ci.deepin.com/repo/deepin/deepin-ports/cdimage/latest/riscv64/bootloaders/sophgo-bootloader-single-sg2042-dev.zip
- 参考安装文档：https://deepin-community.github.io/sig-deepin-ports/docs/install/riscv/sg2042

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
使用 `dd` 将固件写入 microSD 卡。

解压 `sophgo-bootloader-multi-sg2042-dev.zip`，将 `firmware_single_sg2042-dev.img` 写入 microSD 卡。

抹除 NVMe SSD 上先前已存在的所有分区，重新创建一个 GPT 分区表，新建一个分区，将 ext4 格式的系统镜像写入到此分区。

下述 `/dev/sdX`、`/dev/sdY` 分别为 microSD 卡和 NVMe SSD，请自行变更。

```bash
unzip sophgo-bootloader-single-sg2042-dev.zip
sudo wipefs -af /dev/sdX
sudo dd if=firmware_single_sg2042-dev.img of=/dev/sdX bs=1M status=progress
sudo wipefs -af /dev/sdY
sudo fdisk /dev/sdY
# 依次输入 g，n，然后回车确认（三次），最后输入 w 将设置写入硬盘
tar xvf deepin-23-beige-preview-riscv64-sg2042-20240613-124856.tar.xz
# 注意是写入 sdY 的第一个分区 sdY1 而不是直接写入 sdY 全盘
sudo dd if=./deepin-sg2042-riscv64-stable-desktop-installer.root.ext4 of=/dev/sdY1 bs=4M status=progress
echo ", +" | sudo sfdisk -N 1 /dev/sdX
sudo resize2fs /dev/sdX1
```

### 登录系统

安装好 SSD 后，开机进入首次启动向导。

设置向导最后完成后会回到 TTY，稍等片刻会自动进入桌面。

## 预期结果

系统正常启动，能够进入桌面。

## 实际结果

系统成功启动，能够进入设置向导，能够进入桌面。

### 启动信息

> 截图为 USB HDMI 采集卡捕获到的画面。

![](image/2025-01-25-01-42-43.png)

![](image/2025-01-25-01-50-13.png)

![](image/2025-01-25-01-50-21.png)

桌面体验测试报告参见 https://github.com/QA-Team-lo/oscompare/blob/main/Deepin/Pioneer/README.md。

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。