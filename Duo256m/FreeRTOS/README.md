# BuildRoot Milk-V Duo 256M 测试报告

## 测试环境

### 操作系统信息

- 下载链接：https://github.com/milkv-duo/duo-buildroot-sdk/releases
- 参考安装文档：https://github.com/milkv-duo/duo-buildroot-sdk
    - FreeRTOS: https://milkv.io/zh/docs/duo/getting-started/rtoscore

### 硬件信息

- Milk-V Duo 256M
- USB-A to C 或 USB C to C 线缆一条
- microSD 卡一张
- USB to UART 调试器一个（如：CH340, CH341, FT2232 等）
- 可选：Milk-V Duo IOB（底板）

## 安装步骤

rtos 已经存在与 BuildRoot SDK 中。

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
/dev/loop16
```

接下来将下载好的镜像挂载，并将刚刚编译好的二进制复制进镜像：

```shell
sudo losetup /dev/loop16 milkv-duo256m-v1.1.0-2024-0410.img
sudo kpartx -av /dev/loop16
sudo mount /dev/mapper/loop16p2 /mnt
cp ~/duo-examples/mailbox-test/mailbox_test /mnt/root/
sudo umount /mnt
sudo kpartx -d /dev/loop1
sudo losetup -d /dev/loop16 
```

接下来刷入修改后的镜像：

```shell
sudo dd if=milkv-duo256m-v1.1.0-2024-0410.img of=/dev/sdc bs=4M status=progress oflag=direct
```

至此，存储卡准备完成。插入开发板，准备启动。

### 登录系统

通过串口登录系统。

默认用户名：`root`
默认密码： `milkv`

## 预期结果

系统正常启动，通过板载串口登录后运行 `mailbox_test` 二进制，板载蓝色 LED 灯先亮后灭。

（待机状态为蓝色 LED 闪烁）

## 实际结果

系统正常启动，成功通过板载串口登录，`mailbox_test` 运行正常，板载 LED 先亮后灭。

### 启动信息

```log
The authenticity of host '192.168.42.1 (192.168.42.1)' can't be established.
ED25519 key fingerprint is SHA256:JrNwim4ZPbnSw+aC9orl+VPBoRBkXxMatEDjRSq8SSw.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '192.168.42.1' (ED25519) to the list of known hosts.
root@192.168.42.1's password: 
[root@milkv-duo]~# ./mailbox_test 
C906B: cmd.param_ptr = 0x4
C906B: cmd.param_ptr = 0x3
[root@milkv-duo]~# exit

```

屏幕录像：
[![asciicast](https://asciinema.org/a/MhkD6TsSDQ9N0w4u2k6VUHn3s.svg)](https://asciinema.org/a/MhkD6TsSDQ9N0w4u2k6VUHn3s)

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

成功