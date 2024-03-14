# Debian K230 测试报告

## 测试环境

### 操作系统信息

- 系统版本：canmv_debian_sdcard_sdk_1.3
- 下载链接：https://kendryte-download.canaan-creative.com/developer/k230/canmv_debian_sdcard_sdk_1.3.img.gz

### 硬件信息

- 开发板：Canaan Kendryte K230

## 安装步骤

### 刷写镜像到 microSD 卡

使用 `dd` 刷入镜像到 microSD 卡。假设 microSD 卡设备为 `/dev/sdb`。

```bash
wget https://kendryte-download.canaan-creative.com/developer/k230/canmv_debian_sdcard_sdk_1.3.img.gz
gunzip -d canmv_debian_sdcard_sdk_1.3.img.gz
sudo dd if=canmv_debian_sdcard_sdk_1.3.img of=/dev/sdb bs=1M status=progress oflag=sync
```

### 登录系统

通过串口登录系统。

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

系统正常启动，成功通过板载串口登录。

### 启动信息

![Debian](image.png)