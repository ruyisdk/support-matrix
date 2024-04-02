# RevyOS Lichee Console 4A 版本测试报告

## 测试环境

### 操作系统信息

- 系统版本：RevyOS
- 下载链接：https://wiki.sipeed.com/hardware/zh/lichee/th1520/lcon4a/3_images.html
- 参考安装文档：https://wiki.sipeed.com/hardware/zh/lichee/th1520/lcon4a/4_burn_image.html

### 硬件信息

- Lichee Cluster 4A 8G / 16G

## 安装步骤

### 使用 `fastboot` 刷写镜像到板载 eMMC

下载并解压镜像后，使用 `fastboot` 烧录。

```bash
fastboot flash ram u-boot-with-spl-console.bin
fastboot reboot
fastboot flash uboot u-boot-with-spl-console.bin
fastboot flash boot boot.ext4
fastboot flash root root.ext4
```

### 登录系统

通过串口或图形界面登录系统。

默认镜像的帐号密码配置如下：

账户：`sipeed`，密码：`licheepi`

账户：`debian`，密码：`debian`

root 账户默认没有设置密码。

## 预期结果

系统正常启动，能够正常登录。

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