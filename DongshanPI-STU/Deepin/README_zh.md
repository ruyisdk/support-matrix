# Deepin DongshanPI-Nezha STU 测试报告

## 测试环境

### 系统信息

- 系统版本：Deepin 23 beige 20221209
- 下载链接：https://github.com/deepin-community/deepin-riscv-board/releases/download/v20221209/deepin-d1-20221208175445.img.zst.0
- 参考安装文档：https://github.com/deepin-community/deepin-riscv-board/

### 硬件信息

- DongshanPI-Nezha STU
- 电源适配器
- microSD 卡一张

## 安装步骤

### 刷写镜像

使用 `dd` 将镜像写入 microSD 卡。

```bash
sudo dd if=deepin-d1-20221208175445.img of=/dev/your_device bs=1M status=progress
```

### 登录系统

通过串口或图形界面登录系统。

串口默认用户名：`root`
密码：`Riscv2022#`

GUI 默认用户名：`deepin`
密码：`deepin`

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

系统正常启动，成功通过板载串口登录。
有视频输出，可以进入桌面，但需等待较长时间且十分卡顿，基本无法使用。

### 启动信息

```log
Deepin GNU/Linux
Deepin GNU/Linux 23 deepin-riscv  23 deepin-riscv ttyS0

deepin-riscv login: hvc0

deepin-riscv login: root
Password:
Verification successful
Linux deepin-riscv 6.1.0-rc3+ #1 PREEMPT Thu Dec  8 17:52:42 UTC 2022 riscv64
Welcome to Deepin 23 GNU/Linux

    * Homepage:https://www.deepin.org/

    * Bugreport:https://bbs.deepin.org/


root@deepin-riscv:~# [  190.417842] fbcon: Deferring console take-over
[  190.422420] sun4i-drm display-engine: [drm] fb0: sun4i-drmdrmfb frame buffer device
[  191.959682] enter sun20i_d1_hdmi_phy_config
[  191.970283] enter sun20i_d1_hdmi_phy_enable
[  191.982312] [sun20i_d1_hdmi_phy_enable]:phy_rcalend2d_status
[  191.994318] [sun20i_d1_hdmi_phy_enable]:pll_lock_status
[  192.006308] [sun20i_d1_hdmi_phy_enable]:tx_ready_status

root@deepin-riscv:~# uname -a
Linux deepin-riscv 6.1.0-rc3+ #1 PREEMPT Thu Dec  8 17:52:42 UTC 2022 riscv64 GNU/Linux
root@deepin-riscv:~# cat /etc/os-release
PRETTY_NAME="Deepin 23"
NAME="Deepin"
VERSION_ID="23"
VERSION="23"
ID=Deepin
HOME_URL="https://www.deepin.org/"
BUG_REPORT_URL="https://bbs.deepin.org"
VERSION_CODENAME=beige
root@deepin-riscv:~#

```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。
