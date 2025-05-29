---
sys: nuttx
sys_ver: null
sys_var: null

status: basic
last_update: 2025-05-29
---

# Apache NuttX Pine64 Ox64 Test Report

## Test Environment

### Operating System Information

- NuttX
  - Download Link: https://github.com/lupyuen/nuttx-bl602/releases/download/upstream-2024-10-01/nuttx.bin
    - Flashing Tool: https://github.com/spacemeowx2/blflash
  - Reference Installation Document: https://lupyuen.github.io/articles/flash#download-and-build-blflash

### Hardware Information

- Pine64 Pinecone BL602 Evaluation Board
- A Type-C cable

## Installation Steps

Install `blflash`:

```bash
cargo install blflash
```

Set the PineCone Jumper (IO 8) to the H Position before connecting to the computer.

Flash the firmware via `blflash`:
```
wget https://github.com/lupyuen/nuttx-bl602/releases/download/upstream-2024-10-01/nuttx.bin
sudo blflash flash nuttx.bin --port /dev/ttyUSB0
```

Set the PineCone Jumper (IO 8) to the L Position and press the RST button to reset.

## Booting the System

Connect to UART at `/dev/ttyUSB0`, with baud rate of 2000000.

## Expected Results

The system should start normally with serial output.

## Actual Results

The system started successfully, with serial output.

### Boot Information

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

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.

