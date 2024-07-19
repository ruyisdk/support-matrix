# Milk-V Jupiter 测试报告

## 测试环境

### 系统信息

- 下载链接：https://github.com/milkv-jupiter/jupiter-bianbu-build/releases
- 参考安装文档：https://milkv.io/zh/docs/jupiter/getting-started/boot

### 硬件信息

- Milk-V Jupiter
- DC 电源适配器或 USB PD 电源
- microSD 卡一张，或者安装 eMMC 模块
- USB to UART 调试器一个

## 安装步骤

### 刷写镜像（microSD 卡）

**请务必选择以 `.img.zip` 结尾的压缩包**

下载并解压镜像后，使用 `dd` 将镜像写入 microSD 卡。

注意有两个 ZIP 分卷 zip.001 和 zip.002，需要全部下载才能解压镜像。

```bash
sudo dd if=/path/to/milkv-jupiter-bianbu-23.10-desktop-k1-v1.0.8-release-2024-0716.img of=/dev/sdX bs=1M status=progress
```

### 登录系统

通过串口登录系统。

默认用户名： `root`
默认密码： `milkv`

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

CFT

### 启动信息

CFT

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

CFT