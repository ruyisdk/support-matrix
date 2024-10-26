# Fedora 38 Milk-V Duo 测试报告

## 测试环境

### 操作系统信息

- 系统版本：openEuler 23.03
- 下载链接：https://share.weiyun.com/0gIkzesF
- 参考安装文档：https://github.com/openeuler-riscv/duo-buildroot-sdk/blob/develop/uni_pedestal/WORK.md

> Note: 此镜像为社区开发者提供，非官方镜像。

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

### 使用 `dd` 刷写镜像到 microSD 卡

```shell
sudo dd if=oe2303_uniproton.img of=/dev/sdc bs=4M iflag=fullblock status=progress 
```

### 登录系统

通过串口登录系统。

用户名：`root`
密码：`openEuler12#$`

### 使用方法

```
[root@openeuler-riscv64 ~]# mica --help
usage: mica [-h] {create,start,stop,rm,status,gdb} ...

Query or send control commands to the micad.

positional arguments:
  {create,start,stop,rm,status,gdb}
                        the command to execute
    create              Create a new mica client
    start               Start a client
    stop                Stop a client
    rm                  Remove a client
    status              query the mica client status
    gdb                 Start GDB client

options:
  -h, --help            show this help message and exit
[root@openeuler-riscv64 ~]# mica status
Name                          Assigned CPU        State               Service
uniproton                     2                   Offline
[root@openeuler-riscv64 ~]# mica start uniproton
starting uniproton...
[  200.483901] mcs: mcs_mmap: want /dev/mcs address: 83140000 want size 20000 to process mem 3fd5e53000
[  200.494008] mcs: mcs_mmap: want /dev/mcs address: 830fb000 want size 2000 to process mem 3fd7174000
[  200.516319] mcs: mcs_mmap: want /dev/mcs address: 83000000 want size fd000 to process mem 3fd5e7e000
[  200.531638] mcs: start booting clientos on cpu2(83000000)
[  200.537558] rtos_cmd_qu send
d  2[Un0iPro0t.on 549] 0:5tr6a3p]_ ertntroy ss_pc m0xd0_0q000u0 008se3ffnfed
 0
[UniProton 10] :do_irq irqn=61
[UniProton 11] :prvQueueISR
[Uni[ Pro t2o00n 1.25] 5:t4r2a2p2_en]tr ymc sp 0s:x0 00r00e0c00e8i3fvffeded0
ii[UocntiPlro cmtond  13t]o : dso_ireq nid rqnip=61
 :prtnioP rcotpuon 1(4]2)
    vQueueISR
UniProton : uart init done[UniProton 1] :pass bss init test!
[UniPr[o t o20n0 .2] :57pa96ss86] da rta toins_ict mtde_qst!u 
send
[  200.586525] mcs: received ioctl cmd to send ipi to cpu(2)
[  200.592454] rtos_cmd_qu send
start uniproton successfully!
[root@openeuler-riscv64 ~]# [UniProton 3] :[cvi_spinlock_init] succeess
[UniProton 4] :rtos cmdqu init done!
[UniProton 5] :a packeg cmd_id don't register 3
[UniProton 6] :a packeg cmd_id don't register 3
[  @201@@@.5@0@5@@326@@@@]@ rt@@@@os@@@_i@@@rq@@_h@a#n+=d=le+r# @@ir@@@q=@@@@39@@@@
@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@%*-:..:...:=*%@@@@@@@@@@@@@@@@@@@@
.5@@@@@@@@@@@@@@@@%#=:...-+#@@#=:...-+#@@@@@@@@@@[ @ 2@@@@01@@
@ @236@0@6@]@ @m@c@s@@: @r@e@c@ei@%+-ve...:d =*%ip@@i @f@r@o@@@m %*cl-i:e.n.t: =*%os@@@@
 @@@@@@@@
@@@@@@@@@@@%*=:...-+#@@@@@@@@@@@@@@@@#+-...:+#@@@@@@@@@@
@@@@@@@@#+-...:=#%@@@@@@@@@@@@@@@@@@@@@@%*=:..:-*%@@@@@@
@@@@@*=:...-*%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#+-...:=#@@@
@@@@=..:+#@@@@@@@=+++++++++*%@@@@@@@@@@@@@@@@@@%*=:..+@@
@@@%.::%@@@@@@@@+ ...    ....-%@@@@@@@@@@@@@@@@@@@*..:@@
@@@%::.%@@@@@@@@:::.=****=:::.:@@@@@@@@@@@@@@@@@@@*..-@@
@@@%.:.%@@@@@@@+.:.-@@@@@@:.::.%@@@@@@@@@@@@@@@@@@*..-@@
@@@%.:.%@@@@@@@:.:.=*+++=:.:..=@@@@@@@@@@@@@@@@@@@*..-@@
@@@%.:.%@@@@@@+.:.:-::. ..:.:+@@@@@@@@@@@@@@@@@@@@*..-@@
@@@%.:.%@@@@@@:.:.#@@@%+.::.=@@@@@@@@@@@@@@@@@@@@@*..-@@
@@@%.:.%@@@@@+.:.=@@@@@@*:.:.-@@************#%@@@@*..-@@
@@@%.:.%@@@@@::::%@@@@@@@%-...:%@%@@@@@#***#%%@@@@*..-@@
@@@%.:.%@@@@=.:.+@@@@@@@@@@+++++@@@@@@%***#@@@@@@@*..-@@
@@@%.:.%@@@@%%%%@@@@@@@@@@@@%*##*@@@@#***%@@@@@@@@*..-@@
@@@%.:.%@@@@@@@@@@@@@@@@@@@@@%****%@#***%@@@@@@@@@*..-@@
@@@%.:.%@@@@@@@@@@@@@@@@@@@@@@@#******#@@@@@@@@@@@*.::@@
@@@@-..-*%@@@@@@@@@@@@@@@@@@@@@@%****#@@@@@@@@@@#+:..+@@
@@@@@+-...:=#@@@@@@@@@@@@@@@@@@@@@#*%@@@@@@@%*=:..:-*@@@
@@@@@@@%*=:...-+%@@@@@@@@@@@@@@@@@@%@@@@@#+-...:+#@@@@@@
@@@@@@@@@@@#+-...:=*%@@@@@@@@@@@@@@@@%*=:..:=*%@@@@@@@@@
@@@@@@@@@@@@@@%#=:...-+#@@@@@@@@@@#+:...-+#@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@%*-...:=*%@@%*-...:=*%@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@#+:...::...-+#@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@%*-:-=*%@@@@@@@@@@@@@@@@@@@@@@@
[root@openeuler-riscv64 ~]# mica status
Name                          Assigned CPU        State               Service
uniproton                     2                   Running             rpmsg-tty(/dev/ttyRPMSG0) rpmsg-rpc
```

使用 `screen /dev/ttyRPMSG0` 进入 Uniproton，输入 `help` 获取帮助。

## 预期结果

系统正常启动，能够通过串口登录。

## 实际结果

系统正常启动，能够通过串口登录。
