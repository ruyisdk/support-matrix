# Ubuntu D1s Nezha 测试报告

## 测试环境

### 操作系统信息

- 系统版本：Ubuntu 24.10
- 下载链接：https://cdimage.ubuntu.com/releases/24.10/release/ubuntu-24.10-preinstalled-server-riscv64+nezha.img.xz
- 参考安装文档：https://canonical-ubuntu-boards.readthedocs-hosted.com/en/latest/how-to/pine64-star64/

### 硬件信息

- D1s NeZha
- microSD 卡一张
- USB to UART 调试器一个（如：CH340, CH341, FT2232 等）
- 杜邦线三根

## 安装步骤

### 解压并刷写镜像到 microSD 卡

假定 `/dev/sdc` 为存储卡。

```bash
xz -d ubuntu-25.04-preinstalled-server-riscv64+jh7110.img.xz
sudo dd if=ubuntu-25.04-preinstalled-server-riscv64+jh7110.img of=/dev/sdc bs=1m status=progress
```

### 登录系统

1. 将 microSD 卡插入开发板

2. 将启动项设为 microSD 卡 (参见 [选择启动项](https://canonical-ubuntu-boards.readthedocs-hosted.com/en/latest/how-to/pine64-star64/#boot-source-selection))

3. 使用 USB to UART 调试器连接到开发板上的 GPIO 引脚 (参见 [UART 控制台](https://canonical-ubuntu-boards.readthedocs-hosted.com/en/latest/how-to/pine64-star64/#uart-console))

4. 给开发板上电

5. 当看到 “Hit any key to stop autoboot” 字样时，按下 Enter

6. 使用一下命令重置 U-Boot 环境:

```bash
env default -f -a
env save
```

7. 给开发板重新上电

8. 等待以下输出，确认 cloud-init 已完成运行；这个服务负责生成 SSH 密钥并创建默认用户:

```log
[   35.682018] cloud-init[909]: Cloud-init v. 24.1.3-0ubuntu3 finished at Tue, 23 Apr 2024 07:44:59 +0000. Datasource DataSourceNoCloud [seed=/var/lib/cloud/seed/nocloud-net][dsmode=net].  Up 35.65 seconds
```

9. 使用用户名 `ubuntu` 和默认密码 `ubuntu`登陆

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