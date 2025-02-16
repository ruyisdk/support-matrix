---
sys: freertos
sys_ver: null
sys_var: null

status: basic
last_update: 2025-1-21


---

# FreeRTOS Milk-V Duo Test Report

## Test Environment

### Operating System Information

- Build System: Ubuntu 22.04.5 LTS x86_64
- System Version: Duo-V1.1.4
- Download Link: [Duo-Buildroot-SDK Releases](https://github.com/milkv-duo/duo-buildroot-sdk/releases)
- Reference Installation Document: [Duo-Buildroot-SDK](https://github.com/milkv-duo/duo-buildroot-sdk)
  - FreeRTOS: [FreeRTOS Core](https://milkv.io/zh/docs/duo/getting-started/rtoscore)

### Hardware Information

- Milk-V Duo 64M
- A USB Power Adapter
- A USB-A to C or USB C to C Cable
- A microSD Card
- A USB to UART Debugger (e.g., CH340, CH341, FT2232, etc.)
- Three Jumper Wires
- Milk-V Duo pre-soldered with necessary pins for debugging
- Optional: Milk-V Duo IOB (Baseboard)

## Installation Steps

### Building the mailbox-test Binary

Clone the duo-examples repository locally and build the binary.

```shell
sudo apt install -y wget git make
git clone https://github.com/milkv-duo/duo-examples --depth=1
cd duo-examples
source envsetup.sh
cd mailbox-test
make
```

### Packaging the Binary into the Image

First, check available loop devices:

```shell
sudo losetup -f
```

Sample Output:

(The output of the loop device varies depending on the device.)

```shell
$ sudo losetup -f
/dev/loop14
```

Download the official Buildroot SDK:

```shell
wget https://github.com/milkv-duo/duo-buildroot-sdk/releases/download/v1.1.4/milkv-duo-sd-v1.1.4.img.zip
unzip milkv-duo-sd-v1.1.4.img.zip
```

Next, mount the downloaded image, copy the compiled binary into the image, and disable `blink.sh`:

(The default firmware of Duo's big-core Linux system controls the LED blinking, which is implemented through a boot script. When testing the program, it is necessary to disable the LED blinking script.)

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

Then, flash the modified image:

```shell
sudo dd if=milkv-duo-sd-v1.1.4.img of=/dev/your/device bs=1M status=progress
```

At this stage, the storage card is prepared. Insert it into the development board and get ready to boot.

## Logging into the System

Logging into the system via the serial port.

## Expected Results

The system should boot normally. After logging in through the onboard serial port, the `mailbox_test` binary should run, causing the onboard blue LED to turn on and then off.

### Actual Results

The system booted successfully, logging in through the onboard serial port was successful, and the `mailbox_test` ran correctly with the onboard LED turning on and then off.

### Boot Log

```log
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

## Screen recording:

[![asciicast](https://asciinema.org/a/fvzKYovafxRJfwMNilUDot5Yg.svg)](https://asciinema.org/a/fvzKYovafxRJfwMNilUDot5Yg)

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.