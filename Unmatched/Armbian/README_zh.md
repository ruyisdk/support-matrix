# Armbian Unmatched 测试报告

## 测试环境

### 操作系统信息

- 下载链接：https://www.armbian.com/sifive-unmatched/
    - https://github.com/armbian/community/releases/tag/25.2.0-trunk.266
        - Minimal: https://github.com/armbian/community/releases/download/25.2.0-trunk.266/Armbian_community_25.2.0-trunk.266_Unmatched_noble_edge_6.1.123_minimal.img.xz
        - Xfce: https://github.com/armbian/community/releases/download/25.2.0-trunk.266/Armbian_community_25.2.0-trunk.266_Unmatched_noble_edge_6.1.123_xfce_desktop.img.xz
    - Archive 版本：https://imola.armbian.com/archive/unmatched/archive/
- 参考安装文档：https://docs.armbian.com/User-Guide_Getting-Started/

### 硬件信息

- HiFive Unmatched Rev A
- microUSB 线缆一条（随 HiFive Unmatched 附赠）
- ATX 电源一个
- microSD 卡一张

## 安装步骤

### 烧写镜像

下载后，解压并烧写镜像：
```bash
unxz -k Armbian_community_25.2.0-trunk.266_Unmatched_noble_edge_6.1.123_minimal.img.xz
sudo dd if=Armbian_community_25.2.0-trunk.266_Unmatched_noble_edge_6.1.123_minimal.img of=/dev/your/sdcard bs=1M status=progress
```

### 登录系统

通过串口连接开发板。

启动后，系统会要求用户手动配置用户名、密码、时区、语言等。

Xfce 版本需要配置完成后方可进入桌面。

可通过串口配置。若接入了键盘和显示器，亦可通过键盘配置。

## 预期结果

开发板正常输出启动信息。

## 实际结果

两个版本均未能启动。

镜像中未集成 U-Boot，然而即使是已经刷写 U-Boot 至 SPI 并将系统烧录至 M.2 NVMe SSD 的情况，U-Boot 依然不能检测到 SSD 上的系统并正常启动。

Archive 中提供的 23.8.1 版本也有同样问题，未能启动。

### 启动信息

屏幕录像（从刷写系统到启动）：

N/A

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试失败 / CFH

## 其它说明

社区中已有 issue：https://github.com/armbian/community/issues/28

然而由于 Unmatched 是 Armbian 的 "Community maintained" 状态，即实际上不被 Armbian 官方支持，此 issue 已被关闭。