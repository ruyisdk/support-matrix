# NuttX Pine64 Ox64 测试报告

## 测试环境

### 操作系统信息

- 下载链接：https://github.com/lupyuen/nuttx-bl602/releases/download/upstream-2024-10-01/nuttx.bin
  - 烧录工具：https://github.com/spacemeowx2/blflash
- 参考安装文档：https://lupyuen.github.io/articles/flash#download-and-build-blflash

### 硬件信息

- Pine64 Pinecone BL602 Evaluation Board
- Type-C 线一根

## 安装步骤

安装 blflash:

```bash
cargo install blflash
```

将开发板上的 IO8 短接帽接至 "H" 位置并连接至电脑。

使用 blflash 刷写固件：

```
wget https://github.com/lupyuen/nuttx-bl602/releases/download/upstream-2024-10-01/nuttx.bin
sudo blflash flash nuttx.bin --port /dev/ttyUSB0
```

将开发板上的 IO8 短接帽接至 "L" 位置并按 RST 键复位。

## 启动系统

连接到 `/dev/ttyUSB0` 查看串口输出，注意设置波特率为 2000000。

## 预期结果

系统正常启动，能够看到串口输出。

## 实际结果

系统正常启动，能够看到串口输出。

### 启动信息

```log
Registering /dev/gpio0
Registering /dev/gpio1
Disable the interrupt
Registering /dev/gpio2
frequency=400000, actual=0
nbits=8
mode=0

NuttShell (NSH) NuttX-12.6.0-RC1
nsh> uname -a
NuttX 12.6.0-RC1 8153307da5 Oct  1 2024 00:48:59 risc-v bl602evb
nsh> help
help usage:  help [-v] [<cmd>]

    ?        cat      help     ls       uname

Builtin Apps:
    getprime      hello         sensortest    timer
    gpio          nsh           sh
nsh> hello
Hello, World!!
nsh> sensortest
sensortest [arguments...] <command>
        [-h      ]  sensortest commands help
        [-i <val>]  The output data period of sensor in us
                    default: 1000000
        [-b <val>]  The maximum report latency of sensor in us
                    default: 0
        [-n <val>]  The number of output data
                    default: 0
 Commands:
        <sensor_node_name> ex, accel0(/dev/uorb/sensor_accel0)
nsh> getprime
Set thread priority to 10
Set thread policy to SCHED_RR
Start thread #0
thread #0 started, looking for primes < 10000, doing 10 run(s)
thread #0 finished, found 1230 primes, last one was 9973
Done
getprime took 2300 msec
nsh>

```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。