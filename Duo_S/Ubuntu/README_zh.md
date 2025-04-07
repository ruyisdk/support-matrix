# Ubuntu Milk-V Duo S 测试报告

## 测试环境

### 操作系统信息

- 系统版本：Ubuntu 22.04
- 下载链接：https://drive.google.com/file/d/1mkzLhvtjJup3GbgWKZdwL80PZMMXg7n1/view
- 参考安装文档：https://xyzdims.com/3d-printers/misc-hardware-notes/iot-milk-v-duo-risc-v-esbc-running-linux/

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
sudo dd if=milkv-duo-256m-ubuntu-22.04-riscv64-v0.0.4-spiritdude.img of=/dev/your/device bs=1M status=progress
```

### 登录系统

通过串口登录系统。

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

系统正常启动，成功通过板载串口登录。

### 启动信息

```bash
[  OK  ] Started Message of the Day.
[  OK  ] Reached target Timer Units.
[  OK  ] Started dnsmasq - A lightw…t DHCP and caching DNS server.
[  OK  ] Reached target Host and Network Name Lookups.
[  OK  ] Started User Login Management.

Ubuntu 22.04 LTS milkv-duo ttyS0

milkv-duo login: root
Password:
Welcome to Ubuntu 22.04 LTS (GNU/Linux 5.10.4-tag- riscv64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

Last login: Tue Sep 19 16:57:30 UTC 2023 from 192.168.42.2 on pts/0
root@milkv-duo:~# neofetch
            .-/+oossssoo+/-.               root@milkv-duo
        `:+ssssssssssssssssss+:`           --------------
      -+ssssssssssssssssssyyssss+-         OS: Ubuntu 22.04 LTS riscv64
    .ossssssssssssssssssdMMMNysssso.       Host: Cvitek. CV181X ASIC. C906.
   /ssssssssssshdmmNNmmyNMMMMhssssss/      Kernel: 5.10.4-tag-
  +ssssssssshmydMMMMMMMNddddyssssssss+     Uptime: 29 secs
 /sssssssshNMMMyhhyyyyhmNMMMNhssssssss/    Packages: 245 (dpkg)
.ssssssssdMMMNhsssssssssshNMMMdssssssss.   Shell: bash 5.1.16
+sssshhhyNMMNyssssssssssssyNMMMysssssss+   Terminal: /dev/ttyS0
ossyNMMMNyMMhsssssssssssssshmmmhssssssso   CPU: (1)
ossyNMMMNyMMhsssssssssssssshmmmhssssssso   Memory: 39MiB / 240MiB
+sssshhhyNMMNyssssssssssssyNMMMysssssss+
.ssssssssdMMMNhsssssssssshNMMMdssssssss.
 /sssssssshNMMMyhhyyyyhdNMMMNhssssssss/
  +sssssssssdmydMMMMMMMMddddyssssssss+
   /ssssssssssshdmNNNNmyNMMMMhssssss/
    .ossssssssssssssssssdMMMNysssso.
      -+sssssssssssssssssyyyssss+-
        `:+ssssssssssssssssss+:`
            .-/+oossssoo+/-.

root@milkv-duo:~#
```

屏幕录像：

[![asciicast](https://asciinema.org/a/ureP4abokF0DE8AIFQjcdB073.svg)](https://asciinema.org/a/ureP4abokF0DE8AIFQjcdB073)


## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。
