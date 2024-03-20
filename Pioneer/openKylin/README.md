# openKylin 2.0 alpha RISC-V 测试报告

## 测试环境

- 系统版本：openKylin 2.0 alpha RISC-V
- 下载链接：[[Google Drive](https://www.openkylin.top/downloads/)](https://www.openkylin.top/downloads/)
- 参考安装文档：[https://docs.openkylin.top/zh/%E7%A4%BE%E5%8C%BA%E5%BC%80%E5%8F%91%E6%8C%87%E5%8D%97/riscv%E4%B8%8A%E5%AE%89%E8%A3%85openKylin](https://docs.openkylin.top/zh/%E7%A4%BE%E5%8C%BA%E5%BC%80%E5%8F%91%E6%8C%87%E5%8D%97/riscv%E4%B8%8A%E5%AE%89%E8%A3%85openKylin)

### 硬件信息

- Milk-V Pioneer Box v1.1
- microSD 卡一张
- HDMI 线 + 显示器

## 安装步骤

### 刷写镜像

使用 `unxz` 解压镜像。
使用 `dd` 将镜像写入 microSD 卡。

```bash
unxz /path/to/openKylin.img.xz
sudo dd if=/path/to/openKylin.img of=/dev/your_device bs=1M status=progress
```

### 登录系统

通过图形界面登录系统。

默认用户名： `openKylin`
默认密码： `openkylin`

## 预期结果

系统正常启动，能够通过图形界面登录。

## 实际结果

系统正常启动，成功通过图形界面登录。

### 启动信息

![desktop_uname](./desktop_uname.png)

串口日志（从刷写镜像到启动系统）：
[![asciicast](https://asciinema.org/a/LrlBd3N4GZWvXRKHP8vikgTBF.svg)](https://asciinema.org/a/LrlBd3N4GZWvXRKHP8vikgTBF)


## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。