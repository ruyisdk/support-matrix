# Milk-V Megrez 测试报告

## 测试环境

### 操作系统信息

- 下载链接：https://images.fedoravforce.org/Megrez
- 参考安装文档：https://milkv.io/zh/docs/megrez/getting-started/boot

### 硬件信息

- 开发板：Milk-V Megrez
- USB A to C / USB C to C 线缆
- SD 卡

## 安装步骤

### 烧写镜像

下载后，解压并烧写镜像（以下以 desktop 版为例）：
```bash
gzip -d fedora-disk-multi-desktops_eswin_eic7700-sda.raw.gz
sudo dd if=fedora-disk-multi-desktops_eswin_eic7700-sda.raw of=/dev/your/sdcard bs=1M status=progress
```

### 登录系统

通过串口登录系统。

默认用户名： `root`
默认密码： `riscv`

## 预期结果

开发板正常输出启动信息。

## 实际结果

CFT

### 启动信息

屏幕录像（从刷写系统到启动）：


```log
```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

CFT