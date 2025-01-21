# FreeRTOS Milk-V Duo 测试报告

## 测试环境

### 操作系统信息

* 构建系统：Ubuntu 22.04.5 LTS x86_64
* 系统版本：Duo-V1.1.4
* 下载链接：https://github.com/milkv-duo/duo-buildroot-sdk/releases
* 参考安装文档：https://github.com/milkv-duo/duo-buildroot-sdk
  * FreeRTOS：https://milkv.io/zh/docs/duo/getting-started/rtoscore

### 硬件信息

* Milk-V Duo 64M
* USB 电源适配器一个
* USB-A to C 或 USB C to C 线缆一条
* microSD 卡一张（大于1G）
* USB to UART 调试器一个（如：CH340, CH341, FT2232 等）
* 杜邦线三根
* Milk-V Duo 本体上预先焊接好调试所需的排针
* 可选：Milk-V Duo IOB（底板）

## 安装步骤

### 构建 mailbox-test 二进制

拉取 duo-examples 仓到本地并构建。

```shell
sudo apt-get install wget git make
git clone https://github.com/milkv-duo/duo-examples.git --depth=1
cd duo-examples
source envsetup.sh
cd mailbox-test
make
```

### 将构建出的二进制打包进镜像

首先，查询当前可用的 loop 设备：

```shell
sudo losetup -f
```

此处输出：

(输出的loop设备因不同设备而异)

```shell
$ sudo losetup -f
/dev/loop14
```

下载官方 Buildroot 镜像：

```shell
wget https://github.com/milkv-duo/duo-buildroot-sdk/releases/download/v1.1.4/milkv-duo-sd-v1.1.4.img.zip
unzip milkv-duo-sd-v1.1.4.img.zip
```

接下来将下载好的镜像挂载，并将刚刚编译好的二进制复制进镜像，并禁用blink.sh：

（Duo 的默认固件大核 Linux 系统会控制 LED 闪烁，这个是通过开机脚本实现的，在测试该程序的时候，需要将 LED 闪烁的脚本禁用）

```shell
sudo losetup /dev/loop14 milkv-duo-sd-v1.1.4.img
sudo kpartx -av /dev/loop14
sudo mount /dev/mapper/loop14p2 /mnt
cp ~/duo-examples/mailbox-test/mailbox_test /mnt/root/
sudo mv /mnt/mnt/system/blink.sh /mnt/mnt/system/blink.sh_backup
sudo umount /mnt
sudo kpartx -d /dev/loop14
sudo losetup -d /dev/loop14
```

接下来刷入修改后的镜像：

```shell
sudo dd if=milkv-duo-sd-v1.1.4.img of=/dev/your/device bs=1M status=progress
```

至此，存储卡准备完成。插入开发板，准备启动。

## 登录系统

通过串口登录系统

## 预期结果

系统正常启动，通过板载串口登录后运行 `mailbox_test` 二进制，板载蓝色 LED 灯先亮后灭。

## 实际结果

系统正常启动，成功通过板载串口登录，`mailbox_test` 运行正常，板载 LED 先亮后灭。

### 启动信息

```shell
[    2.661662] snsr_i2c snsr_i2c: i2c:-------hook 0                   
[    2.666687] snsr_i2c snsr_i2c: i2c:-------hook 1                  
[    2.672065] snsr_i2c snsr_i2c: i2c:-------hook 2                   
[    2.677348] snsr_i2c snsr_i2c: i2c:-------hook 3                   
[    2.682555] snsr_i2c snsr_i2c: i2c:-------hook 4                   
[    2.730079] vi_core_probe:203(): res-reg: start: 0xa000000, end: 0xa07ffff, .
[    2.739981] vi_core_probe:216(): irq(32) for isp get from platform driver.   
[    2.748046] vi_tuning_buf_setup:253(): tuning fe_addr[0]=0x81e9f490, be_addr0
[    2.759288] vi_tuning_buf_setup:253(): tuning fe_addr[1]=0x81e5f490, be_addr0
[    2.770463] vi_tuning_buf_setup:253(): tuning fe_addr[2]=0x81e7f490, be_addr0
[    2.781577] sync_task_init:177(): sync_task_init vi_pipe 0         
[    2.787548] sync_task_init:177(): sync_task_init vi_pipe 1         
[    2.793501] sync_task_init:177(): sync_task_init vi_pipe 2         
[    2.799943] vi_core_probe:252(): isp registered as cvi-vi          
[    2.854348] cvi_dwa_probe:487(): done with rc(0).                   
[    2.885812] cv180x-cooling cv180x_cooling: elems of dev-freqs=6     
[    2.892085] cv180x-cooling cv180x_cooling: dev_freqs[0]: 850000000 500000000 
[    2.899887] cv180x-cooling cv180x_cooling: dev_freqs[1]: 425000000 375000000 
[    2.907553] cv180x-cooling cv180x_cooling: dev_freqs[2]: 425000000 300000000 
[    2.915264] cv180x-cooling cv180x_cooling: Cooling device registered: cv180xg
[    2.950592] jpu ctrl reg pa = 0xb030000, va = (____ptrval____), size = 256   
[    2.958257] end jpu_init result = 0x0                               
[    3.075954] cvi_vc_drv_init result = 0x0                           
[    3.092349] sh (167): drop_caches: 3                                         
Starting app... 
                                                                       
[root@milkv-duo]~# ls                                                 
mailbox_test                                                           
[root@milkv-duo]~# ./mailbox_test                                    
RT: [20.143355]prvQueueISR                                            
RT: [20.145702]recv cmd(19) from C906B, param_ptr [0x00000002]         
RT: [20.151434]recv cmd(19) from C906B...send [0x00000004] to C906B   
C906B: cmd.param_ptr = 0x4                                             
RT: [24.158481]prvQueueISR                                            
RT: [24.160825]recv cmd(19) from C906B, param_ptr [0x00000003]         
RT: [24.166558]recv cmd(19) from C906B...send [0x00000004] to C906B   
C906B: cmd.param_ptr = 0x3                                             
[root@milkv-duo]~# 
```

### 屏幕录像：

[![asciicast](https://asciinema.org/a/fvzKYovafxRJfwMNilUDot5Yg.svg)](https://asciinema.org/a/fvzKYovafxRJfwMNilUDot5Yg)

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。