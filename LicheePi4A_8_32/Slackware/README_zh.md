# Slackware LPi4A 测试报告

## 测试环境

### 系统信息

- 系统版本：Slackware 15
  - 下载链接：http://dl.slarm64.org/slackware/images/lichee_pi_4a/
  - 参考安装文档：http://dl.slarm64.org/slackware/images/lichee_pi_4a/README.TXT

### 硬件信息

- Lichee Pi 4A (8G RAM + 32G eMMC)
- 电源适配器
- USB to UART 调试器一个

## 安装步骤


### 刷写 bootloader

进入 fastboot。

- 按动 BOOT 同时上电。
- （详见官方教程）
  使用 fastboot 按命令烧录 u-boot。

```bash
sudo fastboot flash ram boot/u-boot-with-spl.bin
sudo fastboot reboot
sleep 10
sudo fastboot flash uboot boot/u-boot-with-spl.bin
```

### 刷写镜像

使用 `zstd` 解压镜像。
使用 `dd` 将镜像写入 microSD 卡。

```bash
zstd -d slarm64-current-riscv64-core-lichee_pi_4a-5.10.113-build-20230704.img
dd if=slarm64-current-riscv64-core-lichee_pi_4a-5.10.113-build-20230704.img of=/path/to/device bs=1M
```

### 登录系统

通过串口登录系统。

初次启动会要求设置用户以及 root 密码。

将系统从 SD 卡转移到 EMMC，运行脚本：transfer-to-disk

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

系统正常启动，成功通过板载串口登录。

### 启动信息

屏幕录像：

[![asciicast](https://asciinema.org/a/IFXmp9AC5dQPtugwmBSFxgsp2.svg)](https://asciinema.org/a/IFXmp9AC5dQPtugwmBSFxgsp2)

```log
[    3.176623] soc_cam2_dovdd18_ir GPIO handle specifies active low - ignored
[    3.184791] soc_cam2_dvdd12_ir GPIO handle specifies active low - ignored
[    3.218436] cpufreq: cpufreq_online: CPU0: Running at unlisted initial frequency: 750000 KHz, changing to: 800000 KHz
[    3.229565] cpu cpu0: finish to register cpufreq driver
[    3.235599] thead,light-aon-test aon:light-aon-test: Successfully registered
[    3.290129] debugfs: File 'SDOUT' in directory 'dapm' already present!
[    3.296889] debugfs: File 'Playback' in directory 'dapm' already present!
[    3.303704] debugfs: File 'Capture' in directory 'dapm' already present!
[    3.310443] debugfs: File 'Playback' in directory 'dapm' already present!
[    3.317253] debugfs: File 'Capture' in directory 'dapm' already present!
[    3.327110] [light_wdt_probe,327] register power off callback
[    3.332900] succeed to register light pmic watchdog
[    3.339896] input: gpio-keys as /devices/platform/gpio-keys/input/input0
[    3.347296] aw87519_pa 5-0058: aw87519_parse_dt: no reset gpio provided failed
[    3.354631] aw87519_pa 5-0058: aw87519_i2c_probe: failed to parse device tree node
[    3.362292] aw87519_pa: probe of 5-0058 failed with error -1
[    3.368119] cfg80211: Loading compiled-in X.509 certificates for regulatory database
[    3.378313] cfg80211: Loaded X.509 cert 'sforshee: 00b28ddf47aef9cea7'
[    3.385151] platform regulatory.0: Direct firmware load for regulatory.db failed with error -2
[    3.386269] clk: Not disabling unused clocks
[    3.393903] cfg80211: failed to load regulatory.db
[    3.398173] ALSA device list:
[    3.405974]   #0: Light-Sound-Card
[    3.416741] EXT4-fs (mmcblk1p2): mounted filesystem without journal. Opts: (null)
[    3.424376] VFS: Mounted root (ext4 filesystem) readonly on device 179:2.
[    3.434628] devtmpfs: mounted
[    3.437720] Freeing unused kernel memory: 304K
[    3.454450] Run /sbin/init as init process
[    3.503050] NOHZ tick-stop error: Non-RCU local softirq work is pending, handler #280!!!
[    3.511200] NOHZ tick-stop error: Non-RCU local softirq work is pending, handler #280!!!
[    3.674312] NOHZ tick-stop error: Non-RCU local softirq work is pending, handler #80!!!
[    3.682379] NOHZ tick-stop error: Non-RCU local softirq work is pending, handler #80!!!
[    3.690470] NOHZ tick-stop error: Non-RCU local softirq work is pending, handler #82!!!
[    3.698497] NOHZ tick-stop error: Non-RCU local softirq work is pending, handler #82!!!
[    3.706563] NOHZ tick-stop error: Non-RCU local softirq work is pending, handler #82!!!
[    3.714587] NOHZ tick-stop error: Non-RCU local softirq work is pending, handler #82!!!
[    4.088948] random: udevd: uninitialized urandom read (16 bytes read)
[    4.096521] random: udevd: uninitialized urandom read (16 bytes read)
[    4.103104] random: udevd: uninitialized urandom read (16 bytes read)
[    4.145295] udevd[299]: starting eudev-3.2.12
[    4.354725] NOHZ tick-stop error: Non-RCU local softirq work is pending, handler #280!!!
[    4.362847] NOHZ tick-stop error: Non-RCU local softirq work is pending, handler #280!!!
[    4.469173] dwc3-thead soc:usb@ffec03f000: light dwc3 probe ok!
[    4.941215] Galcore version 6.4.6.9.354872
[    4.962180] [drm] Initialized vivante 1.0.0 20170808 for ffecc80000.gc620 on minor 1
[    5.055569] xhci-hcd xhci-hcd.3.auto: xHCI Host Controller
[    5.061120] xhci-hcd xhci-hcd.3.auto: new USB bus registered, assigned bus number 1
[    5.069388] xhci-hcd xhci-hcd.3.auto: hcc params 0x0220fe65 hci version 0x110 quirks 0x0000000000010810
[    5.078883] xhci-hcd xhci-hcd.3.auto: irq 74, io mem 0xffe7040000
[    5.085725] hub 1-0:1.0: USB hub found
[    5.089563] hub 1-0:1.0: 1 port detected
[    5.093831] xhci-hcd xhci-hcd.3.auto: xHCI Host Controller
[    5.099356] xhci-hcd xhci-hcd.3.auto: new USB bus registered, assigned bus number 2
[    5.107048] xhci-hcd xhci-hcd.3.auto: Host supports USB 3.0 SuperSpeed
[    5.114164] hub 2-0:1.0: USB hub found
[    5.118046] hub 2-0:1.0: 1 port detected
[    5.358221] usb 1-1: new high-speed USB device number 2 using xhci-hcd
[    5.561901] hub 1-1:1.0: USB hub found
[    5.565902] hub 1-1:1.0: 5 ports detected
[    5.657109] usb 2-1: new SuperSpeed Gen 1 USB device number 2 using xhci-hcd
[    5.834107] hub 2-1:1.0: USB hub found
[    5.838196] hub 2-1:1.0: 4 ports detected
[    6.310217] usb 1-1.5: new high-speed USB device number 3 using xhci-hcd
[    6.373836] EXT4-fs (mmcblk1p2): Remounting file system with no journal so ignoring journalled data option
[    6.386893] EXT4-fs (mmcblk1p2): re-mounted. Opts: data=writeback,errors=remount-ro
[    6.515404] EXT4-fs (mmcblk1p1): mounted filesystem with ordered data mode. Opts: (null)
[    6.546260] Adding 131068k swap on /swap.  Priority:5 extents:1 across:131068k SS
[    6.631751] random: crng init done
[    6.635242] random: 4 urandom warning(s) missed due to ratelimiting


=======================================================================

if you want to transfer the system to SDcard to internal memory (eMMC or NAND),
follow transfer-to-disk

=======================================================================

slarm64 GNU/Linux (ttyS0)
Kernel 5.10.113 (riscv64)

lichee-pi-4a login: root
Password:
Last login: Thu Jan  1 00:00:50 on ttyS0
      _                   ___  ___
 ___ | | ___  ___  _____ |  _|| | |
|_ -|| || .'||  _||     || . ||_  |
|___||_||__,||_|  |_|_|_||___|  |_|
 _  _       _                     _    ___
| ||_| ___ | |_  ___  ___    ___ |_|  | | | ___
| || ||  _||   || -_|| -_|  | . || |  |_  || .'|
|_||_||___||_|_||___||___|  |  _||_|    |_||__,|
                            |_|

root@lichee-pi-4a:~# uname -a
Linux lichee-pi-4a 5.10.113 #1 SMP PREEMPT Mon Jul 3 23:20:15 EEST 2023 riscv64 GNU/Linux
root@lichee-pi-4a:~#
```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。
