# Armbian LPi4A 测试报告

## 测试环境

### 系统信息

- 系统版本：Ubuntu 20.04 LTS 
- 下载链接：[https://github.com/chainsx/armbian-riscv-build/tree/main](https://github.com/chainsx/armbian-riscv-build/tree/main)
    - u-boot: [https://github.com/chainsx/thead-u-boot/actions](https://github.com/chainsx/thead-u-boot/actions)
- 参考安装文档：[https://github.com/chainsx/armbian-riscv-build/blob/main/doc/licheepi-4a-install-guide_ch.md](https://github.com/chainsx/armbian-riscv-build/blob/main/doc/licheepi-4a-install-guide_ch.md)
- fastboot 链接：
    - [https://pan.baidu.com/e/1xH56ZlewB6UOMlke5BrKWQ](https://pan.baidu.com/e/1xH56ZlewB6UOMlke5BrKWQ)
    - [https://mega.nz/folder/phoQlBTZ#cZeQ3qZ__pDvP94PT3_bGA](https://mega.nz/folder/phoQlBTZ#cZeQ3qZ__pDvP94PT3_bGA)

### 硬件信息

- Lichee Pi 4A (8G RAM + 64G eMMC)
- 电源适配器
- microSD 卡一张
- USB to UART 调试器一个

## 安装步骤

### 刷写镜像

使用 `unxz` 解压镜像。
使用 `dd` 将镜像写入 microSD 卡。

```bash
unxz /path/to/Armbian.img.xz
sudo dd if=/path/to/Armbian.img of=/dev/your_device bs=1M status=progress
```

### 刷写 bootloader

进入 fastboot。
- 正式版确认 boot 拨码开关为 eMMC。
- 按动 BOOT 同时上电。
- （详见官方教程）
使用 fastboot 按命令烧录 u-boot。

```bash
sudo ./fastboot flash ram ./path/to/your/lpi4a-$(ram_size)-u-boot-with-spl.bin
sudo ./fastboot reboot
sleep 10
sudo ./fastboot flash uboot ./path/to/your/lpi4a-$(ram_size)-u-boot-with-spl.bin
```

### 登录系统

通过串口登录系统。

初次启动会要求设置用户及密码。

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

系统正常启动，成功通过板载串口登录。

### 启动信息

屏幕录像（从刷写镜像到登录系统）：

[![asciicast](https://asciinema.org/a/CPXNwT3yJUG4wHDKdWGucbHm9.svg)](https://asciinema.org/a/CPXNwT3yJUG4wHDKdWGucbHm9)

```log
Welcome to ARMBIAN! 

Documentation: https://docs.armbian.com | Community: https://forum.armbian.com

Create root password: *****
Repeat root password: *****
Rejected - it is too short. Try again [3].
Create root password: ********
Repeat root password: ********

Choose default system command shell:

1) bash
2) zsh

Shell: BASH

Creating a new user account. Press <Ctrl-C> to abort

Desktop environment will not be enabled if you abort the new user creation

Please provide a username (eg. your first name): ^C
Disabling user account creation procedure

root@licheepi-4a:~# neofetch 
            .-/+oossssoo+/-.                                                                                                    
        `:+ssssssssssssssssss+:`           ---------------- 
      -+ssssssssssssssssssyyssss+-         OS: Ubuntu 20.04 LTS riscv64 
    .ossssssssssssssssssdMMMNysssso.       Host: T-HEAD Light Lichee Pi 4A configuration for 8GB DDR board 
   /ssssssssssshdmmNNmmyNMMMMhssssss/      Kernel: 5.10.113-thead-g052b22ef8baf 
  +ssssssssshmydMMMMMMMNddddyssssssss+     Uptime: 1 min 
 /sssssssshNMMMyhhyyyyhmNMMMNhssssssss/    Packages: 1283 (dpkg) 
.ssssssssdMMMNhsssssssssshNMMMdssssssss.   Shell: bash 5.0.16 
+sssshhhyNMMNyssssssssssssyNMMMysssssss+   Terminal: /dev/ttyS0 
ossyNMMMNyMMhsssssssssssssshmmmhssssssso   CPU: (4) @ 1.848GHz 
ossyNMMMNyMMhsssssssssssssshmmmhssssssso   Memory: 165MiB / 7705MiB 
+sssshhhyNMMNyssssssssssssyNMMMysssssss+
.ssssssssdMMMNhsssssssssshNMMMdssssssss.                           
 /sssssssshNMMMyhhyyyyhdNMMMNhssssssss/                            
  +sssssssssdmydMMMMMMMMddddyssssssss+
   /ssssssssssshdmNNNNmyNMMMMhssssss/
    .ossssssssssssssssssdMMMNysssso.
      -+sssssssssssssssssyyyssss+-
        `:+ssssssssssssssssss+:`
            .-/+oossssoo+/-.


```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。