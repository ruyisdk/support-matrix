# irradium LicheePi 4A 测试报告

## 测试环境

### 系统信息

- 系统版本：irradium 3.8
- 下载链接：
  - image: <https://mirror.serverion.com/irradium/images/lichee_pi_4a/irradium-3.8-riscv64-core-lichee_pi_4a-6.6.90-build-20250510.img.zst>
  - boot: <https://mirror.serverion.com/irradium/images/lichee_pi_4a/boot-20250510.tar.xz>
- 参考安装文档：<https://mirror.serverion.com/irradium/images/lichee_pi_4a/README.TXT>

### 硬件信息

- Lichee Pi 4A (16G RAM + 128G eMMC)
- 电源适配器
- USB to UART 调试器一个

## 安装步骤

### 刷写 bootloader

解压安装套件。
进入 fastboot 工具所在目录。
刷入 u-boot 与 boot。

```bash
zstd -d irradium-3.8-riscv64-core-lichee_pi_4a-6.6.90-build-20250510.img.zst
xz -d boot-20250510.tar.xz
sudo fastboot flash ram u-boot-with-spl-lpi4a(-16g).bin
sudo fastboot reboot
sudo fastboot flash uboot u-boot-with-spl-lpi4a(-16g).bin
```

### 刷写镜像

将 root 分区刷入 eMMC 中。

```bash
sudo fastboot flash root irradium-3.8-riscv64-core-lichee_pi_4a-6.6.90-build-20250510.img
```

### 登录系统

通过串口登录系统。

默认用户名： `root` (自动登录)

默认无密码

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

系统正常启动，成功通过板载串口登录。

### 启动信息

```log
CFT
```


## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

CFT
