# Milk-V Jupiter 测试报告

## 测试环境

### 系统信息

- 下载链接：https://archive.spacemit.com/image/k1/version/bianbu/v3.0/
- 参考安装文档：https://milkv.io/zh/docs/jupiter/getting-started/boot

### 硬件信息

- Milk-V Jupiter (Key Stone K1/M1, 4G/8G/16G)
    - 本次测试的为 M1 + 16G 配置
- DC 12V 5.5*2.5mm 电源适配器，或 USB PD 电源（需要 12V 挡位），或 ATX 电源，任选其一
    - DC 电源推荐 12V 3A 或以上，如有 PCI-E 设备，供电需求较高时，建议使用 ATX 电源
    - 通过 `titanflasher` 或 `fastboot` 烧录时需要占用 USB Type-C 接口，此时 PD 供电不可用，需要 DC 或者 ATX 供电
    - 本次测试使用 DC 供电
- microSD 卡一张，或者 eMMC 模块，或者安装 NVMe SSD
    - 系统启动优先级为：`microSD > NVMe SSD > eMMC`
    - 从 SD 卡启动时不经过 SPI Flash
    - NVMe SSD 和 eMMC 都不存在时，`titanflasher` 工具只会烧录 U-Boot 等启动程序到 SPI Flash 中。
    - 本次测试使用 microSD 启动，型号为：Samsung Pro Ultimate 128GB
- USB to UART 调试器一个
    - 本次测试使用的调试器为 CH343P
- USB Type-C 线缆若干（取决于连接需求，至少预留一根用于烧录镜像）

## 安装步骤

### 刷写镜像（microSD 卡）

**请务必选择以 `.img.zip` 结尾的压缩包**

下载并解压镜像后，使用 `dd` 将镜像写入 microSD 卡。

```bash
unzip bianbu-25.04-minimal-k1-v3.0-release-20250725114639.img.zip
sudo dd if=bianbu-25.04-minimal-k1-v3.0-release-20250725114639.img of=/dev/<your-device> bs=1M status=progress
```

### 登录系统

通过串口登录系统。

默认用户名： `root`
默认密码： `bianbu`

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

系统正常启动，能够通过板载串口登录。

### 启动信息

[![asciicast](https://asciinema.org/a/P5ESOCw24RkgWlMo2ARyWUEiz.svg)](https://asciinema.org/a/P5ESOCw24RkgWlMo2ARyWUEiz)

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。
