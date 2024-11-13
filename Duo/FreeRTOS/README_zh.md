# FreeRTOS Milk-V Duo 测试报告

## 测试环境

### 操作系统信息

- 构建系统：Ubuntu 22.04.3 LTS x86_64
- 系统版本：Duo-V1.1.3
- 下载链接：https://github.com/milkv-duo/duo-buildroot-sdk/releases
- 参考安装文档：https://github.com/milkv-duo/duo-buildroot-sdk
    - FreeRTOS: https://milkv.io/zh/docs/duo/getting-started/rtoscore

### 硬件信息

- Milk-V Duo 64M
- USB 电源适配器一个
- USB-A to C 或 USB C to C 线缆一条
- microSD 卡一张
- USB to UART 调试器一个（如：CH340, CH341, FT2232 等）
- 杜邦线三根
- Milk-V Duo 本体上预先焊接好调试所需的排针
- 可选：Milk-V Duo IOB（底板）

## 安装步骤


### 构建 mailbox-test 二进制

拉取 duo-examples 仓到本地并构建。

```shell
sudo apt install -y wget git make
git clone https://github.com/milkv-duo/duo-examples --depth=1
cd duo-examples
source envsetup.sh
cd mailbox-test
make
```
#### 将构建出的二进制打包进镜像

首先，查询当前可用的 loop 设备：

```shell
sudo losetup -f
```

此处输出：

```shell
$ sudo losetup -f
/dev/loop0
```

下载官方 Buildroot 镜像：

```shell
wget https://github.com/milkv-duo/duo-buildroot-sdk/releases/download/v1.1.3/milkv-duo-sd-v1.1.3-2024-0930.img.zip
unzip milkv-duo-sd-v1.1.3-2024-0930.img.zip
```

接下来将下载好的镜像挂载，并将刚刚编译好的二进制复制进镜像：

```shell
sudo losetup /dev/loop0 milkv-duo-sd-v1.1.3-2024-0930.img
sudo kpartx -av /dev/loop0
sudo mount /dev/mapper/loop0p2 /mnt
cp ~/duo-examples/mailbox-test/mailbox_test /mnt/root/
sudo umount /mnt
sudo kpartx -d /dev/loop0
sudo losetup -d /dev/loop0
```

接下来刷入修改后的镜像：

```shell
sudo dd if=milkv-duo-sd-v1.1.3-2024-0930.img of=/dev/your/device bs=4M status=progress
```

至此，存储卡准备完成。插入开发板，准备启动。

### 登录系统

通过串口登录系统。

## 预期结果

系统正常启动，通过板载串口登录后运行 `mailbox_test` 二进制，板载蓝色 LED 灯先亮后灭。

（待机状态为蓝色 LED 闪烁）

## 实际结果

系统正常启动，成功通过板载串口登录，`mailbox_test` 运行正常，板载 LED 先亮后灭。

### 启动信息

```log
[    2.629875] sync_task_init:177(): sync_task_init vi_pipe 0
[    2.635850] sync_task_init:177(): sync_task_init vi_pipe 1
[    2.641810] sync_task_init:177(): sync_task_init vi_pipe 2
[    2.648237] vi_core_probe:252(): isp registered as cvi-vi
[    2.701678] cvi_dwa_probe:487(): done with rc(0).
[    2.731805] cv180x-cooling cv180x_cooling: elems of dev-freqs=6
[    2.738146] cv180x-cooling cv180x_cooling: dev_freqs[0]: 850000000 500000000
[    2.745950] cv180x-cooling cv180x_cooling: dev_freqs[1]: 425000000 375000000
[    2.753585] cv180x-cooling cv180x_cooling: dev_freqs[2]: 425000000 300000000
[    2.761332] cv180x-cooling cv180x_cooling: Cooling device registered: cv180x_cooling
[    2.795351] jpu ctrl reg pa = 0xb030000, va = (____ptrval____), size = 256
[    2.803013] end jpu_init result = 0x0
[    2.928217] cvi_vc_drv_init result = 0x0
[    2.943974] sh (165): drop_caches: 3
Starting app...

[root@milkv-duo]~# ls
mailbox_test
[root@milkv-duo]~# ./mailbox_test 
RT: [44.439088]prvQueueISR
RT: [44.441435]recv cmd(19) from C906B, param_ptr [0x00000002]
RT: [44.447166]recv cmd(19) from C906B...send [0x00000004] to C906B
C906B: cmd.param_ptr = 0x4
RT: [48.454192]prvQueueISR
RT: [48.456537]recv cmd(19) from C906B, param_ptr [0x00000003]
RT: [48.462270]recv cmd(19) from C906B...send [0x00000004] to C906B
C906B: cmd.param_ptr = 0x3
[root@milkv-duo]~# 
```

屏幕录像：

[![asciicast](https://asciinema.org/a/IANV6OK3PCAMO3L7hcx11ngck.svg)](https://asciinema.org/a/IANV6OK3PCAMO3L7hcx11ngck)

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。