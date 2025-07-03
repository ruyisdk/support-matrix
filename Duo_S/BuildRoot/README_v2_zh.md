# BuildRoot (v2) Milk-V Duo S 测试报告

## 测试环境

### 操作系统信息

- 系统版本：DuoS-V2.0.1 (musl 版本)
- 下载链接：https://github.com/milkv-duo/duo-buildroot-sdk-v2/releases/
- 参考安装文档：https://github.com/milkv-duo/duo-buildroot-sdk-v2

### 硬件信息

- Milk-V Duo S (512M, SG2000)
- USB 电源适配器一个
- USB-A to C 或 USB C to C 线缆一条，用于给开发板供电
- microSD 卡一张
- USB 读卡器一个
- USB to UART 调试器一个（如：CP2102, FT2232 等，注意不可使用 CH340/341 系列，会出现乱码）
- 杜邦线三根

## 安装步骤

###  下载 Duo S 镜像并解压

```bash
wget https://github.com/milkv-duo/duo-buildroot-sdk-v2/releases/download/v2.0.1/milkv-duos-musl-riscv64-sd_v2.0.1.img.zip
unzip milkv-duos-musl-riscv64-sd_v2.0.1.img.zip
```

###  刷写镜像

使用 `dd` 命令将镜像刷写到 SD 卡：

```bash
sudo dd if=milkv-duos-musl-riscv64-sd_v2.0.1.img of=/dev/your/device bs=1M status=progress
```

### 登录系统

通过串口登录系统。

## 预期结果

系统正常启动，能够通过板载串口和ssh登录。

## 实际结果

系统正常启动，成功通过板载串口与ssh登录。

### 启动信息

> 出现 aic8800 insmod 失败是因为测试时使用的是不带 Wi-Fi 芯片的 Duo S。
>
> 这是正常情况。

```log
[    3.465078] vpss_start_handler:5143(): handler for dev(1) started
[    3.512876] cvi-mipi-tx mipi_tx: IRQ index 0 not found
[    3.524770] cvi-mipi-tx mipi_tx: vbat irq(-6)
[    3.529815] cvi-mipi-tx mipi_tx: reset gpio pin(354) active(0)
[    3.536143] cvi-mipi-tx mipi_tx: power ctrl gpio pin(353) active(1)
[    3.542892] cvi-mipi-tx mipi_tx: pwm gpio pin(352) active(1)
[    3.569852] cv181x-cooling cv181x_cooling: elems of dev-freqs=6
[    3.576099] cv181x-cooling cv181x_cooling: dev_freqs[0]: 850000000 500000000
[    3.583900] cv181x-cooling cv181x_cooling: dev_freqs[1]: 425000000 375000000
[    3.591486] cv181x-cooling cv181x_cooling: dev_freqs[2]: 425000000 300000000
[    3.599164] cv181x-cooling cv181x_cooling: Cooling device registered: cv181x_cooling
[    3.628687] [INFO] Register SBM IRQ ###################################
[    3.628715] [INFO] pvctx->s_sbm_irq = 37
[    3.643789] jpu ctrl reg pa = 0xb030000, va = (____ptrval____), size = 256
[    3.655437] end jpu_init result = 0x0
[    3.750599] cvi_vc_drv_init result = 0x0
[    3.821737] sh (192): drop_caches: 3
Starting app...
insmod: can't insert '/mnt/system/ko/aic8800_fdrv.ko': No such device
[root@milkv-duo]~# uname -a
Linux milkv-duo 5.10.4-tag- #1 PREEMPT Fri May 30 14:51:54 CST 2025 riscv64 GNU/Linux
[root@milkv-duo]~# cat /proc/cpuinfo
processor       : 0
hart            : 0
isa             : rv64imafdvcsu
mmu             : sv39
```

屏幕录像：

[![asciicast](https://asciinema.org/a/MRJsh4hLcH9HsXDixX6lJzdZx.svg)](https://asciinema.org/a/MRJsh4hLcH9HsXDixX6lJzdZx)

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。
