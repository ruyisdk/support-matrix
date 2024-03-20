# RevyOS Pioneer 测试报告

## 测试环境

### 操作系统信息

- 系统版本：RevyOS 20240119
- 下载链接：[https://mirror.iscas.ac.cn/revyos/extra/images/sg2042/20240119/](https://mirror.iscas.ac.cn/revyos/extra/images/sg2042/20240119/)
- 参考安装文档：https://revyos.github.io/docs/

### 硬件信息

- Milk-V Pioneer Box v1.1
- microSD 卡一张
- HDMI 线 + 显示器

## 安装步骤

### 刷写镜像

使用 `zstd` 解压镜像。
使用 `dd` 将镜像写入 microSD 卡。

```bash
zstd -d /path/to/revyos.img.zstd
dd if=/path/to/revyos.img of=/dev/yout-device bs=4M status=progress
```

### 常见问题

- 若需要从 SD 卡启动，需要手动向其中添加 Fip.bin 和 ZSBL。

### 登录系统

通过图形界面登录系统。

默认用户名：`debian`
默认密码：`debian`

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 预期结果

系统正常启动，能够通过图形界面登录。

## 实际结果

系统正常启动，成功通过图形界面登录。

### 启动信息

![desktop_uname](./desktop_uname.png)

串口日志（从刷写系统到启动系统）：

[![asciicast](https://asciinema.org/a/voe4Uou1CvIP7u21inc3tfjAT.svg)](https://asciinema.org/a/voe4Uou1CvIP7u21inc3tfjAT)


## 测试结论

测试成功。