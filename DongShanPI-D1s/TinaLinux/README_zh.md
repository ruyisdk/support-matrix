# Tina Linux DongshanPI-D1s 测试报告

## 测试环境

### 操作系统信息

- 下载链接：https://gitlab.com/dongshanpi/tools/-/raw/main/tina_d1s-nezha_sd_uart0.zip
- 参考安装文档：https://dongshanpi.com/DongshanPI-D1s/03-1_FlashSystem/

### 硬件信息

- DongshanPI-D1s
- microSD 卡一张
- USB to UART 调试器一个（如：CH340, CH341, FT2232 等）

## 安装步骤

### 烧写镜像

下载并解压后，使用 dd 将镜像烧写到 SD 卡：
```bash
sudo dd if=tina_d1s-nezha_sd_uart0.img of=/dev/your/device bs=1M status=progress
```

### 登录系统

通过串口登录系统。

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

CFT

### 启动信息


屏幕录像（从刷写镜像到登录系统）：

```log
```


## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

CFT