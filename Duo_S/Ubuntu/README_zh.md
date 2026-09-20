# Ubuntu Milk-V Duo S 测试报告

## 测试环境

### 操作系统信息

- 系统版本：Ubuntu 24.04 LTS
- 下载链接：https://github.com/queenkjuul/milkv-duo-ubuntu/releases/tag/v7.0.6-qkj1
- 参考安装文档：https://github.com/queenkjuul/milkv-duo-ubuntu/wiki/Building-the-System

### 硬件信息

- Milk-V Duo S (512M, SG2000)
- USB 电源适配器一个
- USB-A to C 或 USB C to C 线缆一条，用于给开发板供电
- microSD 卡一张
- USB 读卡器一个
- USB to UART 调试器一个
    - 仅推荐使用 CP210x 系列如 CP2102/CP2104，注意不可使用 CH340/341 系列，会输出乱码；FT232/CH343P 等其他串口调试器在启动至 U-Boot 之前也会出现乱码，启动后可正常使用，这是预期结果，如果持续只能得到乱码输出请尝试更换使用 CP210x 系列芯片的调试器
- 杜邦线三根

## 安装步骤

### 使用 `dd` 刷写镜像到 microSD 卡

```shell
sudo dd if=ubuntu-noble-milkv-duos.img of=/dev/sdX bs=1M status=progress
```
> 注：请将 `/dev/sdX` 替换为实际 SD 卡设备名。

### 登录系统

通过串口登录系统。

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

系统正常启动，成功通过板载串口登录。

### 启动信息

```bash
[  OK  ] Started dbus.service - D-Bus System Message Bus.
[  OK  ] Finished e2scrub_reap.service - Re…line ext4 Metadata Check Snapshots.
[  OK  ] Finished sysstat.service - Resets System Activity Logs.
[  OK  ] Finished milkv-usb.service - Milk-V Duo S USB OTG.

Ubuntu 24.04 LTS milkv-duos ttyS0

milkv-duos login: root
Password:
Welcome to Ubuntu 24.04 LTS (GNU/Linux 7.0.6-qkj1-duos riscv64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/pro
root@milkv-duos:~# neofetch
            .-/+oossssoo+/-.               root@milkv-duos
        `:+ssssssssssssssssss+:`           ---------------
      -+ssssssssssssssssssyyssss+-         OS: Ubuntu 24.04 LTS riscv64
    .ossssssssssssssssssdMMMNysssso.       Host: Milk-V Duo S
   /ssssssssssshdmmNNmmyNMMMMhssssss/      Kernel: 7.0.6-qkj1-duos
  +ssssssssshmydMMMMMMMNddddyssssssss+     Uptime: 1 min
 /sssssssshNMMMyhhyyyyhmNMMMNhssssssss/    Packages: 402 (dpkg)
.ssssssssdMMMNhsssssssssshNMMMdssssssss.   Shell: bash 5.2.21
+sssshhhyNMMNyssssssssssssyNMMMysssssss+   Terminal: /dev/ttyS0
ossyNMMMNyMMhsssssssssssssshmmmhssssssso   CPU: (1)
ossyNMMMNyMMhsssssssssssssshmmmhssssssso   Memory: 74MiB / 466MiB
+sssshhhyNMMNyssssssssssssyNMMMysssssss+
.ssssssssdMMMNhsssssssssshNMMMdssssssss.
 /sssssssshNMMMyhhyyyyhdNMMMNhssssssss/
  +sssssssssdmydMMMMMMMMddddyssssssss+
   /ssssssssssshdmNNNNmyNMMMMhssssss/
    .ossssssssssssssssssdMMMNysssso.
      -+sssssssssssssssssyyyssss+-
        `:+ssssssssssssssssss+:`
            .-/+oossssoo+/-.

root@milkv-duos:~#
```

屏幕录像：

[![asciicast](https://asciinema.org/a/u4DNnLipiGEsxTl4.svg)](https://asciinema.org/a/u4DNnLipiGEsxTl4)


## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。
