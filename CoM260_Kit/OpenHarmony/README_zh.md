# OpenHarmony CoM260 Kit 版本测试报告

## 测试环境

### 操作系统信息

- 系统版本：SpacemiT OpenHarmony 6.1 CoM260 normal V1.0
- 下载链接：https://archive.spacemit.com/image/k1/version/openharmony/k3_oh6.1/com260/spacemit-k3-oh61-com260-normal-V1.0-20260515.zip
- 参考安装文档：https://www.spacemit.com/community/document/info?lang=zh&nodepath=hardware/eco/k3_com260/com260_user_guide.md

### 硬件信息

- CoM260 Kit，16GB 内存 / 128GB 存储
- DC 供电（机身标注）：19V / 2.37A 或 12V / 5A
- USB Type-C 数据线
- USB 转 TTL 串口模块及杜邦线
- 母对母杜邦线 × 1（用于进入烧录模式）
- 网络和网线

## 安装步骤

*以下在 Ubuntu（x86_64）上使用 TITANTOOLS 通过 USB 刷写镜像。*

### 下载烧录工具

根据[刷机工具使用手册](https://www.spacemit.com/community/document/info?lang=zh&nodepath=tools/user_guide/flasher_user_guide.md)下载 [TITANTOOLS FOR LINUX X64 (64-BIT) (APPIMAGE)](https://cloud.spacemit.com/prod-api/release/download/tools?token=titantools_for_linux_64BIT_APPIMAGE)，在下载目录赋予执行权限并启动：

```bash
chmod +x titantools_for_linux-2.2.0-Rc.AppImage
./titantools_for_linux-2.2.0-Rc.AppImage
```

### 进入烧录模式

准备 1 根母对母杜邦线。按下图摆放开发板：USB 接口和网口朝下，按键排针位于上方。以下位置均从图中排针的左端向右数。

![CoM260 Kit 按键排针](./boot-pins.png)

| 从左向右数的位置 | 短接信号 | 用途 |
| --- | --- | --- |
| 第 3 根与第 4 根引脚 | `FC_REC` ↔ `GND` | 选择烧录模式 |

短接时，将同一根母对母杜邦线的两端分别套在对应的 2 根引脚上。

- **设备未上电**，处于关机状态时：

    1. 拔掉 CoM260 DC 电源。
    2. Type-C 也先拔掉。
    3. 将杜邦线的一端接第 3 根引脚 `FC_REC`，另一端接第 4 根引脚 `GND`，保持连接。
    4. 插入 DC 电源，给 CoM260 上电。
    5. 等 1～2 秒。
    6. 从排针上拔掉杜邦线，解除第 3、4 根引脚之间的短接。
    7. 用支持数据传输的 Type-C 线连接 CoM260 和 Ubuntu 主机。

### 烧写镜像

1. 下载上述镜像，在 TITANTOOLS 中选择“研发工具”→“单机烧录”。
2. 点击“扫描设备”，选择 CoM260 对应的设备。
3. 选择“本地文件”，加载 `spacemit-k3-oh61-com260-normal-V1.0-20260515.zip`，等待工具解压完成。

   ![TITANTOOLS 选择本地镜像](./titantools-select-image.png)

4. 点击“开始刷机”，等待烧录完成后，重新给开发板上电。

   ![TITANTOOLS 正在烧写固件](./titantools-flashing.png)

### 登录系统

按上方引脚图摆放开发板：USB 和网口朝下，排针在上方。以下位置从排针左端向右数，使用 3 根杜邦线连接 USB 转 TTL 模块：

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

连接串口后，给已完成烧录的开发板上电，通过串口终端查看启动输出。原镜像默认启动失败，无法进入系统；本次按“启动信息”中的临时引导方式启动后，按回车即可进入 `root` shell，未要求输入用户名和密码。

### 常见问题

Type-C 接口用于数据传输和烧录，不为开发板供电；需通过 DCIN 接入电源。

## 预期结果

系统正常启动，能够通过串口登录系统。

## 实际结果

系统未能正常启动，无法通过串口登录系统。

### 启动信息

原镜像默认启动失败日志（节选）：

```log
[   4.391] Try to boot from scsi0 ...
[   4.394] product_name: k3_com260_ifx
[   4.395] match dtb by product_nameeeeeeee: /k3_com260_ifx.dtb
[   4.401] select /k3_com260_ifx.dtb to load
[   4.405] Loading kernel...
[   4.453] 33835008 bytes read in 45 ms (717.1 MiB/s)
[   4.455] Loading dtb...
[   4.458] Failed to load '/k3_com260_ifx.dtb'
[   4.462] load dtb from bootfs fail, use built-in dtb
[   4.467] Loading ramdisk ...
[   4.475] 3423793 bytes read in 6 ms (544.2 MiB/s)
No FDT memory address configured. Please configure
the FDT address via "fdt addr <address>" command.
Aborting!
[   4.486] Moving Image from 0x140000000 to 0x102200000, end=1042d5000
[   4.499]    Loading Ramdisk to 3fba2e000, end 3fbd71e31 ... OK
[   4.502] Device tree not found or missing FDT support
### ERROR ### Please RESET the board ###
```

临时引导验证：

本次在上电出现 U-Boot 启动信息时，通过串口连续发送 `s` 和空格，打断自动启动并进入 `=>` 提示符，然后执行以下命令：

```text
ls scsi 0:1 /
load scsi 0:1 ${fdt_addr_r} /k3_com260.dtb
fdt addr ${fdt_addr_r}
fdt print / model
fdt print / compatible
setenv dtb_env 'setenv dtb_name /k3_com260.dtb'
run bootcmd
```

本次预先用 `fdt addr` 选择了设备树进行检查，随后 `run bootcmd` 加载了内核、设备树和 ramdisk，但走到 `bootm` 分支并报错，返回 `=>` 提示符：

```log
Wrong Image Format for bootm command
ERROR: can't get kernel image!
```

接着显式执行以下命令，使用已加载的镜像启动：

```text
booti ${kernel_addr_r} ${ramdisk_combo} ${fdt_addr_r}
```

内核成功启动后，在串口终端按回车，获取到以下系统信息：

```log
# id
uid=0(root) gid=2000(shell) groups=2000(shell),1007(log),3009(readproc)
# uname -a
Linux localhost 6.18.3 #1 SMP PREEMPT_DYNAMIC Fri May 15 12:39:35 CST 2026 riscv64 Toybox
# param get const.ohos.fullname
OpenHarmony-6.1.0.31
```

桌面截图：

原镜像默认启动时因缺少 `/k3_com260_ifx.dtb` 而失败。以下为在 U-Boot 中临时指定镜像内已有的 `/k3_com260.dtb` 并启动内核后显示的 OpenHarmony 桌面；本次未保存 U-Boot 环境，尚未验证重启后能否自动进入系统。

![临时指定设备树启动后的 OpenHarmony 桌面](./openharmony-desktop.png)

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试失败 / CFH
