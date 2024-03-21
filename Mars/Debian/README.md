# Debian on Milk-V Mars

## 测试环境

### 操作系统信息

- Debian bookworm/sid
  - 下载链接：https://github.com/milkv-mars/mars-buildroot-sdk/releases/
    - Milk-V 官方提供的 Debian 镜像，同时仓库中提供了 BuildRoot
  - 参考安装文档：https://milkv.io/zh/docs/mars/getting-started/boot

### 硬件开发板信息

- Milk-V Mars

## 安装步骤

### 刷写镜像

使用 `unzip` 解压镜像。
使用 `dd` 将镜像写入 microSD 卡。

其中，`/dev/sdc` 为存储卡对应设备。

```bash
unzip mars_debian-desktop_sdk-v3.6.1_sdcard_v1.0.6.img.zip
sudo dd if=mars_debian-desktop_sdk-v3.6.1_sdcard_v1.0.6.img of=/dev/sdc bs=1M status=progress
```

### 登录系统

通过串口登录系统。

默认用户名： `user`
默认密码： `milkv`

## 预期结果

系统正常启动，能够通过板载串口登录。能进入安装向导。