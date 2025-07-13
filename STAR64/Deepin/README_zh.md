# Deepin Star64 测试报告

## 测试环境

### 操作系统信息

- 下载链接：https://github.com/deepin-community/deepin-riscv-board/releases/download/v20221209/deepin-visionfive-2-20221208180420.img.zst.0
- 参考安装文档：https://cdimage.deepin.com/RISC-V/VisionFive-v2-image/README.txt

### 硬件信息

- Pine64 Star64
- microSD 卡一张
- DC 12V5A 圆头电源适配器
- USB to UART 调试器一个（如：CH340, CH341, FT2232 等）
- 杜邦线三根

## 安装步骤

### 解压并刷写镜像到 microSD 卡

```bash
zstd -d https://github.com/deepin-community/deepin-riscv-board/releases/download/v20221209/deepin-visionfive-2-20221208180420.img.zst.0
sudo dd if=https://github.com/deepin-community/deepin-riscv-board/releases/download/v20221209/deepin-visionfive-2-20221208180420.img of=/dev/your/device bs=1M status=progress
```

### 引导模式选择

Pine64 Star64 提供了多种引导模式，可在上电前通过板载拨码开关进行配置；开发板本体上亦有丝印标注。参见 [选择启动项](https://canonical-ubuntu-boards.readthedocs-hosted.com/en/latest/how-to/pine64-star64/#boot-source-selection)。

为了启动镜像，可以选择 SPI Flash 模式（即：`GPIO_0 = 0`, `GPIO_1 = 0`）。注意，此模式可能需要提前更新 Flash 内的固件，若您启动不成功，请参考官方文档进行固件升级：[更新 SPL 和 U-Boot](https://doc.rvspace.org/VisionFive2/Quick_Start_Guide/VisionFive2_QSG/spl_u_boot_0.html)

若不更新固件，请选择 microSD 卡引导（即：`GPIO_0 = 1`, `GPIO_1 = 0`）。

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

系统正常启动，成功通过串口登录。

### 启动信息

```log
Deepin GNU/Linux 23 deepin-riscv hvc0

deepin-riscv login: Deepin GNU/Linux 23 deepin-riscv ttyS0

deepin-riscv login: [   35.717007] mipi_0p9: disabling

deepin-riscv login: root
Password:
Password verification failed, 4 chances left

Login incorrect
deepin-riscv login: root
Password:
Verification successful
Linux deepin-riscv 5.15.0+ #1 SMP Thu Dec 8 17:49:21 UTC 2022 riscv64
Welcome to Deepin 23 GNU/Linux

    * Homepage:https://www.deepin.org/

    * Bugreport:https://bbs.deepin.org/


root@deepin-riscv:~# uname -a
Linux deepin-riscv 5.15.0+ #1 SMP Thu Dec 8 17:49:21 UTC 2022 riscv64 GNU/Linux
root@deepin-riscv:~# cat /etc/os-release
PRETTY_NAME="Deepin 23"
NAME="Deepin"
VERSION_ID="23"
VERSION="23"
ID=Deepin
HOME_URL="https://www.deepin.org/"
BUG_REPORT_URL="https://bbs.deepin.org"
VERSION_CODENAME=beige
root@deepin-riscv:~# cat /proc/cpuinfo
processor       : 0
hart            : 1
isa             : rv64imafdc
mmu             : sv39
uarch           : sifive,u74-mc

processor       : 1
hart            : 2
isa             : rv64imafdc
mmu             : sv39
uarch           : sifive,u74-mc

processor       : 2
hart            : 3
isa             : rv64imafdc
mmu             : sv39
uarch           : sifive,u74-mc

processor       : 3
hart            : 4
isa             : rv64imafdc
mmu             : sv39
uarch           : sifive,u74-mc

root@deepin-riscv:~#

```


## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。