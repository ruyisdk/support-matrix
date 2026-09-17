# openEuler CoM260 Kit 版本测试报告

## 测试环境

### 操作系统信息

- 系统版本：openEuler 24.03 LTS SP4（RVA23-OLK-generic）
- 下载链接：
  - 系统镜像：[openEuler-24.03-LTS-SP4-RVA23-OLK-generic.img.zst](https://dl-cdn.openeuler.openatom.cn/openEuler-24.03-LTS-SP4/embedded_img/riscv64/spacemit/com260/openEuler-24.03-LTS-SP4-RVA23-OLK-generic.img.zst)
  - 镜像校验文件：[openEuler-24.03-LTS-SP4-RVA23-OLK-generic.img.zst.sha256sum](https://dl-cdn.openeuler.openatom.cn/openEuler-24.03-LTS-SP4/embedded_img/riscv64/spacemit/com260/openEuler-24.03-LTS-SP4-RVA23-OLK-generic.img.zst.sha256sum)
  - 引导包：[bl-spacemit-k3-RVA23.tar.zst](https://dl-cdn.openeuler.openatom.cn/openEuler-24.03-LTS-SP4/embedded_img/riscv64/spacemit/com260/bl-spacemit-k3-RVA23.tar.zst)
  - 引导包校验文件：[bl-spacemit-k3-RVA23.tar.zst.sha256sum](https://dl-cdn.openeuler.openatom.cn/openEuler-24.03-LTS-SP4/embedded_img/riscv64/spacemit/com260/bl-spacemit-k3-RVA23.tar.zst.sha256sum)
- 参考安装文档：https://www.spacemit.com/community/document/info?lang=zh&nodepath=hardware/eco/k3_com260/com260_user_guide.md

### 硬件信息

- CoM260 Kit，16GB 内存 / 128GB 存储
- DC 供电（机身标注）：19V / 2.37A 或 12V / 5A
- USB 转 TTL 串口模块及杜邦线
- SD/TF 卡及 USB 读卡器，或 U 盘；存储介质容量须大于解压后的镜像
- 网络和网线

## 安装步骤

*针对上述 openEuler SP4 文件在 CoM260 Kit 上的完整官方安装流程尚未确认。*

### 下载烧录工具

在 Ubuntu 主机安装下载和解压工具：

```bash
sudo apt install wget zstd
```

### 烧写镜像

以下步骤在 Ubuntu 主机上，通过 USB 读卡器将系统镜像写入 SD/TF 卡，也适用于 U 盘。后面的 SD 卡启动步骤以板上已有可运行的 U-Boot 为前提。

1. 创建工作目录，下载系统镜像、引导包及各自的校验文件：

   ```bash
   mkdir -p openeuler-com260
   cd openeuler-com260
   wget -c https://dl-cdn.openeuler.openatom.cn/openEuler-24.03-LTS-SP4/embedded_img/riscv64/spacemit/com260/openEuler-24.03-LTS-SP4-RVA23-OLK-generic.img.zst
   wget -c https://dl-cdn.openeuler.openatom.cn/openEuler-24.03-LTS-SP4/embedded_img/riscv64/spacemit/com260/openEuler-24.03-LTS-SP4-RVA23-OLK-generic.img.zst.sha256sum
   wget -c https://dl-cdn.openeuler.openatom.cn/openEuler-24.03-LTS-SP4/embedded_img/riscv64/spacemit/com260/bl-spacemit-k3-RVA23.tar.zst
   wget -c https://dl-cdn.openeuler.openatom.cn/openEuler-24.03-LTS-SP4/embedded_img/riscv64/spacemit/com260/bl-spacemit-k3-RVA23.tar.zst.sha256sum
   ```

2. 在该目录校验下载文件，确认两项均输出 `OK` 后再继续：

   ```bash
   sha256sum -c openEuler-24.03-LTS-SP4-RVA23-OLK-generic.img.zst.sha256sum
   sha256sum -c bl-spacemit-k3-RVA23.tar.zst.sha256sum
   ```

3. 解压镜像，保留原压缩包：

   ```bash
   zstd -dk openEuler-24.03-LTS-SP4-RVA23-OLK-generic.img.zst
   ```

4. 将 SD/TF 卡插入 USB 读卡器后连接 Ubuntu 主机，或连接 U 盘。查看设备列表，按容量和型号确认目标存储介质：

   ```bash
   lsblk -o NAME,TRAN,SIZE,MODEL,FSTYPE,MOUNTPOINTS
   ```

   后续命令中的 `/dev/sdX` 均须替换为目标卡或 U 盘的实际整盘设备路径。内置读卡器也可能显示为 `/dev/mmcblkN`，其分区为 `/dev/mmcblkNp1` 等，须按 `lsblk` 输出替换。烧写会清空所选存储介质的全部数据。

5. 逐一卸载目标存储介质上已挂载的分区。以下以第 1 分区为例，执行时按 `lsblk` 输出替换为实际分区路径；若没有已挂载的分区则跳过：

   ```bash
   sudo umount /dev/sdX1
   ```

6. 将解压后的 `.img` 文件写入整张卡或整个 U 盘。`of` 指向 `/dev/sdX` 这样的整盘设备，不能填 `/dev/sdX1` 这样的分区：

   ```bash
   sudo dd if=openEuler-24.03-LTS-SP4-RVA23-OLK-generic.img of=/dev/sdX bs=4M status=progress conv=fsync
   ```

7. 等待 `dd` 无报错完成并返回命令提示符，再同步数据并弹出存储介质：

   ```bash
   sync
   sudo eject /dev/sdX
   ```

   弹出成功后，将 SD/TF 卡从读卡器取出，在开发板断电时插入板载 TF-Card 接口，位置参见[板卡指南第 5.12 节](https://github.com/spacemit-com/docs-product/blob/main/zh/k3_com260/com260_user_guide.md#512-tf-card-接口)。使用 U 盘时则连接 USB-A 接口。

### 登录系统

按下图摆放开发板：USB 和网口朝下，排针在上方。以下位置从排针左端向右数，使用 3 根杜邦线连接 USB 转 TTL 模块：

![CoM260 Kit 按键排针](./boot-pins.png)

| 从左向右数的位置 | CoM260 信号 | USB 转 TTL 模块 |
| --- | --- | --- |
| 第 6 根 | `GND` | `GND` |
| 第 9 根 | `UART_TXD` | `RXD` |
| 第 10 根 | `UART_RXD` | `TXD` |

接线前确认串口信号电平匹配，并在开发板断电时按模块针脚标注接线。模块的 `VCC` 不接，开发板通过 DC 电源供电，模块的 USB 端连接 Mac 或 Linux 主机。

**Mac 主机：**

安装 [Homebrew](https://brew.sh/) 后，使用以下命令安装 `tio`：

```bash
brew install tio
```

在 Mac 终端查找串口设备：

```bash
find /dev -maxdepth 1 -name 'cu.*'
```

若出现多个设备，可对比插入 USB 转 TTL 模块前后的输出，确定新增的设备。以下以 `/dev/cu.usbserial-1140` 为示例串口名，执行时请替换为实际查找到的设备名：

```bash
tio -b 115200 /dev/cu.usbserial-1140
```

**Linux 主机：**

在 Ubuntu / Debian 上安装 `tio`：

```bash
sudo apt update
sudo apt install tio
```

其他 Linux 发行版请使用对应的包管理器安装 `tio`。

在 Linux 终端查找串口设备：

```bash
find /dev -maxdepth 1 \( -name 'ttyUSB*' -o -name 'ttyACM*' \)
```

若出现多个设备，可对比插入 USB 转 TTL 模块前后的输出，确定新增的设备。以下以 `/dev/ttyUSB0` 为示例串口名，执行时请替换为实际查找到的设备名：

```bash
sudo tio -b 115200 /dev/ttyUSB0
```

`tio` 默认使用 `8N1`，流控关闭。

**从 SD/TF 卡启动（待验证）：**

[openEuler SP3 官方说明](https://www.openeuler.org/zh/blog/20260317-RISC-V/20260317-RISC-V.html)提到 CoM260 支持 SD 卡及通过 `extlinux.conf` 启动。以下结合该启动方式与现有 U-Boot 接口整理，尚未使用本次 SP4 镜像完成验证。

1. 确认已烧写的卡插在板载 TF-Card 接口，连接串口终端，给开发板上电，在自动启动倒计时期间按键进入 U-Boot 的 `=>` 提示符。以下 MMC 命令操作板载卡槽；通过 USB 读卡器连接的卡属于 USB 存储设备。
2. 查看 MMC 控制器列表。以下以设备 `0` 为例，执行时按实际 SD 卡控制器编号替换：

   ```text
   mmc list
   mmc dev 0
   mmc rescan
   mmc info
   part list mmc 0
   ```

   确认卡及分区表均识别成功后再继续。

3. 查看启动分区，以下以第 `1` 分区为例，执行时按实际分区号替换。确认存在 `extlinux/extlinux.conf` 及其引用的内核、initramfs 和设备树文件：

   ```text
   ls mmc 0:1 /
   ```

4. 确认启动配置使用的设备树目录下存在 `spacemit/k3_com260.dtb` 后，在当前 U-Boot 会话中指定该文件，并扫描 SD 卡上的启动配置：

   ```text
   setenv fdtfile spacemit/k3_com260.dtb
   bootflow scan -lb mmc0
   ```

   `mmc0` 对应 MMC 设备 `0`，控制器编号不同时需相应修改。环境变量修改仅对当前会话生效。[U-Boot bootflow 文档](https://docs.u-boot.org/en/v2022.10/usage/cmd/bootflow.html)中，`-l` 表示列出启动项，`-b` 表示尝试启动；系统正常启动及串口登录仍待验证。

### 常见问题

Type-C 接口用于数据传输和固件烧录，不为开发板供电；需通过 DCIN 接入电源。

## 预期结果

系统正常启动，能够通过串口登录系统。

## 实际结果

CFT

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

CFT
