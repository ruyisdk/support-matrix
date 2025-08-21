# Bianbu 荔枝派 Lichee Pi 3A 测试报告

## 测试环境

### 系统信息

- 系统版本：v3.0-minimal
- 下载链接：https://archive.spacemit.com/image/k1/version/bianbu/v3.0/
- 参考安装文档：https://wiki.sipeed.com/hardware/zh/lichee/K1/lpi3a/1_intro.html

### 硬件信息

- 荔枝派 Lichee Pi 3A
- 电源适配器
- USB to UART 调试器
- microSD 卡一张（如果刷写到 SD 卡）
- Type-C 数据线（用于 fastboot 刷写）

## 安装步骤

### 刷写镜像（SD 卡）

**请务必选择以 `.img.zip` 结尾的压缩包**
下载并解压镜像后，使用 `dd` 将镜像写入 microSD 卡。

```bash
unzip bianbu-25.04-minimal-k1-v3.0-release-20250725114639.img.zip
sudo dd if=/path/to/bianbu-25.04-minimal-k1-v3.0-release-20250725114639.img of=/dev/your-device bs=1M status=progress
```

### 刷写镜像（eMMC）

**请务必选择不包含 `img` 的压缩包**
下载并解压镜像后，使用 `fastboot` 将镜像刷写到 eMMC。

> 注意：下面的步骤可能需要使用 `sudo`。
> 否则 `fastboot` 可能不会正确识别设备，因为默认的 USB VID/PID 不在 udev 规则内。

```bash
❯ fastboot devices
dfu-device       DFU download
```

```bash
fastboot stage factory/FSBL.bin
fastboot continue
# Wait for 1 sec
fastboot stage u-boot.itb
fastboot continue
# Wait for 1 sec
fastboot flash gpt partition_universal.json
fastboot flash bootinfo factory/bootinfo_emmc.bin
fastboot flash fsbl factory/FSBL.bin
fastboot flash env env.bin
fastboot flash opensbi fw_dynamic.itb
fastboot flash uboot u-boot.itb
fastboot flash bootfs bootfs.ext4
fastboot flash rootfs rootfs.ext4
```

### 登录系统

通过串口登录系统。

默认用户名： `root`
默认密码： `bianbu`

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

系统在启动时出现 kernel panic，无法正常启动。

### 启动信息

在启动时发生了 kernel panic，发生在 `spacemit_snd_sspa_pdev_probe` 中。

系统无法正常启动。

屏幕录制：
[![asciicast](https://asciinema.org/a/dqzTfBfJ2rfdJXsYzqK7PrTaB.svg)](https://asciinema.org/a/dqzTfBfJ2rfdJXsYzqK7PrTaB)

```log
[    6.477047] enter spacemit_snd_sspa_pdev_probe                                                                       
[    6.496425] Unable to handle kernel NULL pointer dereference at virtual address 0000000000000090                     
[    6.505347] Oops [#1]                                                                                                
[    6.507617] Modules linked in:                                                                                       
[    6.510697] CPU: 3 PID: 1 Comm: swapper/0 Not tainted 6.6.63 #2.2.6.3                                                
[    6.517190] Hardware name: SiPEED LPi3A Board (DT)                                                                   
[    6.522013] epc : spacemit_snd_pcm_new+0x186/0x280                                                                   
[    6.526860]  ra : spacemit_snd_pcm_new+0x172/0x280                                                                   
[    6.531666] epc : ffffffff80c7ac98 ra : ffffffff80c7ac84 sp : ffffffc800073900                                       
[    6.538953]  gp : ffffffff82101ba8 tp : ffffffd900388000 t0 : ffffffff81a9e888                                       
[    6.546219]  t1 : 0000000000000004 t2 : 0000000000000000 s0 : ffffffc800073990                                       
[    6.553496]  s1 : 0000000000000000 a0 : 0000000000000000 a1 : 000000000000011b                                       
[    6.560771]  a2 : 0000000000000000 a3 : 0000000000000000 a4 : ffffffd900388000                                       
[    6.568047]  a5 : 0000000000000000 a6 : 0000000000002683 a7 : 0000000052464e43                                       
[    6.575333]  s2 : 0000000000000002 s3 : fffffffffffff000 s4 : 0000000000000800                                       
[    6.582598]  s5 : 0000000000000400 s6 : ffffffff815c9950 s7 : ffffffd902538540                                       
[    6.589864]  s8 : ffffffd9051d4840 s9 : ffffffd904b23600 s10: 0000000000000002                                       
[    6.597129]  s11: ffffffd9025385c0 t3 : ffffffffffffffff t4 : ffffffff82107fc8                                       
[    6.604395]  t5 : 0000000000000040 t6 : ffffffd90507637d                                                             
[    6.609738] status: 0000000200000120 badaddr: 0000000000000090 cause: 000000000000000d                               
[    6.617710] [<ffffffff80c7ac98>] spacemit_snd_pcm_new+0x186/0x280                                                    
[    6.623836] [<ffffffff80c64de8>] snd_soc_pcm_component_new+0x24/0x90                                                 
[    6.630238] [<ffffffff80c6a46e>] soc_new_pcm+0x47e/0x600                                                             
[    6.635585] [<ffffffff80c5af40>] snd_soc_bind_card+0x8c4/0xa5c                                                       
[    6.641466] [<ffffffff80c5b1be>] snd_soc_register_card+0xe6/0xf8                                                     
[    6.647537] [<ffffffff80c6a764>] devm_snd_soc_register_card+0x40/0x86 
[    6.654039] [<ffffffff80c7bdea>] asoc_simple_card_probe+0x16a/0x250                                                  
[    6.660338] [<ffffffff808537c8>] platform_probe+0x52/0xb6                                                            
[    6.665779] [<ffffffff80850e3c>] really_probe+0x8c/0x326                                                             
[    6.671134] [<ffffffff80851138>] __driver_probe_device+0x62/0x112                                                    
[    6.677277] [<ffffffff8085121e>] driver_probe_device+0x36/0xba                                                       
[    6.683153] [<ffffffff8085140e>] __driver_attach+0x9a/0x1a2                                                          
[    6.688754] [<ffffffff8084f022>] bus_for_each_dev+0x58/0xa6                                                          
[    6.694370] [<ffffffff808508d6>] driver_attach+0x1a/0x22                                                             
[    6.699714] [<ffffffff808500d6>] bus_add_driver+0xf6/0x1fe                                                           
[    6.705233] [<ffffffff808522a8>] driver_register+0x40/0xda                                                           
[    6.710762] [<ffffffff808534ec>] __platform_driver_register+0x1c/0x24                                                
[    6.717263] [<ffffffff80c7b988>] spacemit_snd_card_init+0x1a/0x22                                                    
[    6.723398] [<ffffffff800027c2>] do_one_initcall+0x36/0x222                                                          
[    6.729023] [<ffffffff81001422>] kernel_init_freeable+0x21c/0x286                                                    
[    6.735169] [<ffffffff80ff66d8>] kernel_init+0x1e/0x116                                                              
[    6.740446] [<ffffffff80fff192>] ret_from_fork+0xe/0x18                                                              
[    6.745707] Code: b783 0d0c 6bdc cb89 4789 4481 13e3 f8f9 b783 108c (6bdc) ffb5                                      
[    6.753203] ---[ end trace 0000000000000000 ]---                                                                     
[    6.757872] Kernel panic - not syncing: Attempted to kill init! exitcode=0x0000000b                                  
[    6.765578] SMP: stopping secondary CPUs                                                                             
[    6.769528] ---[ end Kernel panic - not syncing: Attempted to kill init! exitcode=0x0000000b ]--- 
```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试失败。