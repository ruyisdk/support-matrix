# openEuler RISC-V HiFive Unmatched 版本测试报告

## 测试环境

### 操作系统信息

- 系统版本：openEuler 24.09 testing, 20241105 (Xfce)
- 下载链接：https://mirror.iscas.ac.cn/openeuler-sig-riscv/openEuler-RISC-V/testing/20241105/v0.1/Unmatched/
- 参考安装文档：https://mirror.iscas.ac.cn/openeuler-sig-riscv/openEuler-RISC-V/testing/20241105/v0.1/Unmatched/README.Unmatched.txt

> [!NOTE]
> 此镜像为 openEuler RISC-V SIG 组自行发布的 CI/开发版本，非官方发布镜像。
> oERV SIG 正在开发新版本，截止目前为止，经测试，这是最后已知可在 Unmatched 实机启动的镜像。
> 更多信息请见 [此处](https://github.com/ruyisdk/support-matrix/issues/228#issuecomment-2785789283)。

### 硬件信息

- HiFive Unmatched Rev A
- microUSB 线缆一条（随 HiFive Unmatched 附赠）
- ATX 电源一个
- microSD 卡一张（Sandisk Extreme Pro 64G UHS-I）
- PCI-E 显卡一张
- USB 键盘&鼠标
- HDMI 显示器/采集卡，HDMI 线缆（显卡自带 VGA/DVI，亦可使用）
- M.2 NVMe SSD（可选）
    - 请参考安装文档进行操作。

## 安装步骤

### 引导设备选择

确保拨码开关已调整为从 microSD 卡引导。若您未更改，出厂默认即为从 microSD 卡引导。

拨码开关应如下设置：`MSEL[3:0]=1011`

### 使用 `dd` 刷写镜像到 microSD 卡

```shell
wget https://mirror.iscas.ac.cn/openeuler-sig-riscv/openEuler-RISC-V/testing/20241105/v0.1/Unmatched/openEuler-24.09-V1-xfce-unmatched-testing.img.zst
zstd -T0 -dkv openEuler-24.09-V1-xfce-unmatched-testing.img.zst
sudo dd if=openEuler-24.09-V1-xfce-unmatched-testing.img of=/dev/sdX bs=1M status=progress; sync
```

### 其它说明

安装文档中已提到使用 SSD 的启动方式，若板载 SPI Flash 已经刷入了主线 U-Boot，可仅修改 extlinux 中的硬盘配置，无须 microSD 卡即可启动。

注意需要更改 DIP 开关/启动模式。

主线 U-Boot 刷入具体步骤请参照 U-Boot 官方文档：https://docs.u-boot.org/en/latest/board/sifive/unmatched.html

### 登录系统

通过板载串口（使用 microUSB 线缆连接至其他计算机）登录系统。

默认用户名：`openeuler` 或 `root`
默认密码：`openEuler12#$`

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

系统正常启动，成功通过板载串口登录。

### 启动信息

```log
Welcome to 6.6.0-41.0.0.51.oe2409.riscv64

System information as of time:  Fri Jan 24 09:09:15 PM CST 2025

System load:    2.36
Memory used:    2.5%
Swap used:      0.0%
Usage On:       22%
IP address:     10.0.0.120
Users online:   2
To run a command as administrator(user "root"),use "sudo <command>".
[openeuler@openeuler-riscv64 ~]$
```
![](image/2025-01-24-21-44-34.png)

桌面体验测试报告请见 https://github.com/QA-Team-lo/oscompare/blob/main/openEuler/Unmatched/README.md。


## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。