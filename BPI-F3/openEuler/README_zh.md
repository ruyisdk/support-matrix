# openEuler/oERV 香蕉派 BPI-F3 测试报告

## 测试环境

### 系统信息

- 系统版本：openEuler RISC-V 20241231
- 下载链接：https://mirror.iscas.ac.cn/openeuler-sig-riscv/openEuler-RISC-V/testing/20241231/v0.5/k1/
- 参考安装文档：https://docs.banana-pi.org/en/BPI-F3/GettingStarted_BPI-F3

### 硬件信息

- 香蕉派 BPI-F3
- 电源适配器
- microSD 卡一张
- USB to UART 调试器一个

## 安装步骤

### 刷写镜像（sd 卡）

下载并解压镜像后，使用 `dd` 将镜像写入 microSD 卡。

```bash
tar -xvf openEuler-Mega24.03SP1-V1-xfce-k1-testing.img.zst
sudo dd if=openEuler-Mega24.03SP1-V1-xfce-k1-testing.img of=/dev/sdX bs=4M status=progress
```

### 登录系统

通过串口登录系统。

默认用户名：`root` 或 `openeuler`
默认密码：`openEuler12#$`

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

插入存储卡，对开发板上电后串口无输出，HDMI 无输出，无法进入系统。

### 启动信息

无输出。

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试失败。
