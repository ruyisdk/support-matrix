# RevyOS LPi4A 版本测试报告

## 测试环境

### 操作系统信息

- 系统版本：RevyOS 20251226
- 发行版：Debian GNU/Linux trixie/sid（riscv64）
- 内核版本：6.6.119-th1520
- 下载链接：[Nginx Directory](https://fast-mirror.isrc.ac.cn/revyos/extra/images/lpi4a/20251226/)
- 参考安装文档：https://revyos.github.io/docs/

### 硬件信息

- Lichee Pi 4A (16G RAM + 128G eMMC)
- USB-C 电源适配器 / DC 电源一个
- HDMI 显示器一个
- USB 键盘和鼠标一套

## 安装步骤

### 下载并解压镜像

下载镜像，使用 `zstd` 解压镜像（请根据 20251226 目录下实际文件名替换 `XXX` 部分）：

```shell
wget https://fast-mirror.isrc.ac.cn/revyos/extra/images/lpi4a/20251226/u-boot-with-spl-lpi4a-16g-main.bin
wget https://fast-mirror.isrc.ac.cn/revyos/extra/images/lpi4a/20251226/boot-lpi4a-20251226_XXX.ext4.zst
wget https://fast-mirror.isrc.ac.cn/revyos/extra/images/lpi4a/20251226/root-lpi4a-20251226_XXX.ext4.zst

zstd -d boot-lpi4a-20251226_XXX.ext4.zst
zstd -d root-lpi4a-20251226_XXX.ext4.zst
```

### 通过 `fastboot` 刷写到板载 eMMC

#### 使用 BOOT 按钮进入 fastboot 模式

按住 **BOOT** 按钮，然后连接 USB-C 线（另一端连接 PC）进入 USB 烧录模式。

使用以下命令刷写镜像（同样请根据实际文件名调整）：

```shell
sudo fastboot devices
sudo fastboot flash ram u-boot-with-spl-lpi4a-16g-main.bin
sudo fastboot reboot
sudo fastboot flash uboot u-boot-with-spl-lpi4a-16g-main.bin
sudo fastboot flash boot boot-lpi4a-20251226_XXX.ext4
sudo fastboot flash root root-lpi4a-20251226_XXX.ext4
```

### 登录系统

本次测试通过 **显示器 + 键盘 + 鼠标** 进入图形界面登录系统，未使用串口。

- 默认用户名：`debian`
- 默认密码：`debian`

登录流程：

1. 上电启动，等待系统进入图形登录界面。
2. 在登录界面输入用户名 `debian` 和密码 `debian`。
3. 成功进入桌面环境。

## 预期结果

系统正常启动，能够通过图形界面登录桌面环境。

## 实际结果

系统正常启动，成功通过图形界面登录桌面环境。

### 启动信息

启动和桌面截图：
![C](C.PNG)

## 测试判定标准

- 测试成功：实际结果与预期结果相符。
- 测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。