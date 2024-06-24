# BuildRoot Milk-V Duo Test Report

## Test Environment

### Operating System Information

- System Version: Duo-V1.0.7
- Download Link: https://github.com/milkv-duo/duo-buildroot-sdk/releases
- Reference Installation Document: https://github.com/milkv-duo/duo-buildroot-sdk

### Hardware Information

- Milk-V Duo 64M
- A USB power adapter
- A USB-A to C or USB C to C cable
- A microSD card
- A USB to UART debugger (e.g., CH340, CH341, FT2232, etc.)
- Three Dupont wires
- Pins pre-soldered on the Milk-V Duo for debugging

## Installation Steps

### Using `ruyi` CLI to Flash the Image to the microSD Card

Install the [`ruyi`](https://github.com/ruyisdk/ruyi) package manager, run `ruyi device provision`, and follow the prompts.

### Logging into the System

Logging into the system via the serial port.

## Expected Results

The system boots up normally and allows login through the onboard serial port.

## Actual Results

The system booted successfully and login via the onboard serial port was also successful.

### Boot Log

```log
[root@milkv-duo]~# uname -a                                                                                                                                             
Linux milkv-duo 5.10.4-tag- #1 PREEMPT Sat Dec 23 12:29:13 CST 2023 riscv64 GNU/Linux                                                                                   
[root@milkv-duo]~# cat /proc/cpuinfo                                                                                                                                    
processor       : 0                                                                                                                                                     
hart            : 0                                                                                                                                                     
isa             : rv64imafdvcsu                                                                                                                                         
mmu             : sv39                                                                                                                                                  
                                                                                                                                                                        
[root@milkv-duo]~# 
```

Screen recording (from flashing the image to system login):

[![asciicast](https://asciinema.org/a/rsenSOJwdlmUXcJ8sQwubPgtr.svg)](https://asciinema.org/a/rsenSOJwdlmUXcJ8sQwubPgtr)

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
