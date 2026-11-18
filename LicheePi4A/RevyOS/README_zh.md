# RevyOS LPi4A 版本测试报告

## 测试环境

### 操作系统信息

- 系统版本：RevyOS 20260504
- 下载链接：[Nginx Directory](https://fast-mirror.isrc.ac.cn/revyos/extra/images/lpi4a/20260504/)
- 参考安装文档：https://revyos.github.io/docs/

### 硬件信息

- Lichee Pi 4A (8G RAM + 32G eMMC)
- USB-C 电源适配器 / DC 电源一个
- USB-UART 调试器一个

## 安装步骤

### 下载并解压镜像

下载镜像，使用 `zstd` 解压镜像：

```shell
wget https://fast-mirror.isrc.ac.cn/revyos/extra/images/lpi4a/20260504/u-boot-with-spl-lpi4a.bin
wget https://fast-mirror.isrc.ac.cn/revyos/extra/images/lpi4a/20260504/boot-lpi4a-20260504_080619.ext4.zst
wget https://fast-mirror.isrc.ac.cn/revyos/extra/images/lpi4a/20260504/root-lpi4a-20260504_080619.ext4.zst
zstd -d boot-lpi4a-20260504_080619.ext4.zst
zstd -d root-lpi4a-20260504_080619.ext4.zst
```

### 通过 `fastboot` 刷写到板载 eMMC

#### 使用 boot 按钮进入 fastboot 模式

按住 **BOOT** 按钮，然后连接 USB-C 线（另一端连接 PC）进入 USB 烧录模式。

使用以下命令刷写镜像。

```shell
sudo fastboot devices
sudo fastboot flash ram u-boot-with-spl-lpi4a.bin
sudo fastboot reboot
sudo fastboot flash uboot u-boot-with-spl-lpi4a.bin
sudo fastboot flash boot boot-lpi4a-20260504_080619.ext4
sudo fastboot flash root root-lpi4a-20260504_080619.ext4
```

### 登录系统

通过串口或图形界面登录系统。

默认用户名：`debian`
默认密码：`debian`
> 接入网络前，请先通过串口或本地桌面登录，运行 `passwd` 为默认账户设置独有密码。

## 预期结果

系统正常启动，能够通过串口登录。

## 实际结果

系统正常启动，串口和 SSH 登录成功，有线网络和 Xfce 桌面可用。

### 启动信息

![A](desktop-20260504.png)

屏幕录制（从刷写镜像到登录系统）：

[![asciicast](https://asciinema.org/a/nDo0ASizRAmC7YA6.svg)](https://asciinema.org/a/nDo0ASizRAmC7YA6)

```log
   ____              _ ____  ____  _  __
  |  _ \ _   _ _   _(_) ___||  _ \| |/ /
  | |_) | | | | | | | \___ \| | | | ' /
  |  _ <| |_| | |_| | |___) | |_| | . \
  |_| \_\\__,_|\__, |_|____/|____/|_|\_\
               |___/
                   -- Presented by ISCAS

  Debian GNU/Linux 13 (trixie) (kernel 6.6.137-th1520)

Linux revyos-lpi4a 6.6.137-th1520 #2026.05.01.09.26+cca7502e0 SMP Fri May  1 09:52:29 UTC 2026 riscv64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.

debian@revyos-lpi4a:~$ grep ^BUILD_ID= /etc/revyos-release
BUILD_ID=20260504_080619
debian@revyos-lpi4a:~$ findmnt -n -o SOURCE /
/dev/mmcblk0p4

```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。
