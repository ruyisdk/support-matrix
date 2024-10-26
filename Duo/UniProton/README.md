---
sys: uniproton
sys_ver: null
sys_var: null

status: basic
last_update: 2024-10-26
---

# UniProton Milk-V Duo Test Report

## Test Environment

### Operating System Information

- System Version: openEuler 23.03
- Download Link: https://share.weiyun.com/0gIkzesF
- Reference Installation Document: https://github.com/openeuler-riscv/duo-buildroot-sdk/blob/develop/uni_pedestal/WORK.md

> Note: This image is provided by community developers and is not an official image.

### Hardware Information

- Milk-V Duo 64M
- A USB power adapter
- A USB-A to C or USB-C to C cable
- A microSD card
- A USB to UART debugger (e.g., CH340, CH341, FT2232, etc.)
- Three DuPont wires
- The Milk-V Duo has pre-soldered pin headers required for debugging
- Optional: Milk-V Duo IOB (baseboard)

## Installation Steps

### Flashing the Image to microSD Card Using `dd`

```shell
sudo dd if=oe2303_uniproton.img of=/dev/sdc bs=4M iflag=fullblock status=progress 
```

### Logging into the System

Log into the system via the serial port.

Username: `root`
Password: `openEuler12#$`

### Usage

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

Use `screen /dev/ttyRPMSG0` to get in Uniproton，type `help` for help。

## Expected Results

The system should boot normally and allow login via the serial port.

## Actual Results

The system boots normally and allow login via the serial port.
