# Ubuntu VisionFive 测试报告

## 测试环境

### 系统信息

- 系统版本：3.20.0_alpha20231219 (edge)
- 下载链接：https://dev.alpinelinux.org/~mps/riscv64/visionfive-v1-mmc.img.xz
- 参考安装文档：https://arvanta.net/alpine/alpine-on-visionfive/

### 硬件信息

- StarFive VisionFive
- 电源适配器
- microSD 卡一张
- USB to UART 调试器一个

## 安装步骤

### 刷写镜像

使用 `xz` 解压镜像。
使用 `dd` 将镜像写入 microSD 卡。

```bash
xz -d visionfive-v1-mmc.img.xz
dd if=visionfive-v1-mmc.img of=/dev/<your-device> 
```

### 登录系统

通过串口登录系统。
直接登录到 root,无密码。


## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

CFT

### 启动信息

```log

```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

CFT
