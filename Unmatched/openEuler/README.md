# openEuler RISC-V 23.09 HiFive Unmatched Test Report

## Test Environment

### Operating System Information

- System Version: openEuler 23.09 RISC-V preview
- Download Link: https://mirror.iscas.ac.cn/openeuler-sig-riscv/openEuler-RISC-V/preview/openEuler-23.09-V1-riscv64/Unmatched/
- Reference Installation Document: https://mirror.iscas.ac.cn/openeuler-sig-riscv/openEuler-RISC-V/preview/openEuler-23.09-V1-riscv64/Unmatched/README.unmatched.txt

### Hardware Information

- HiFive Unmatched Rev A
- A microUSB cable (included with HiFive Unmatched)
- An ATX power supply
- A microSD card (Sandisk Extreme Pro 64G UHS-I)

## Installation Steps

### Boot Device Selection

Ensure the dip switch is set to boot from the microSD card. If not changed, the factory default is to boot from the microSD card.

The dip switch should be set as follows: `MSEL[3:0]=1011`

### Use `ruyi` CLI to Flash the Image to the microSD Card

Install the [`ruyi`](https://github.com/ruyisdk/ruyi) package manager, run `ruyi device provision`, and follow the prompts.

### Logging into the System

Log into the system via the onboard serial port (using the microUSB cable connected to another computer).

Default username: `openeuler` or `root`
Default password: `openEuler12#$`

## Expected Results

The system should boot normally and allow login through the onboard serial port.

## Actual Results

The system booted successfully and login through the onboard serial port was successful.

### Boot Log

```log
Welcome to 6.1.0-11.oe2309.riscv64                                                                                    
                                                                                                                      
System information as of time:  Mon Sep 18 08:03:17 AM CST 2023                                                       
                                                                                                                      
System load:    1.94                                                                                                  
Processes:      130                                                                                                   
Memory used:    1.2%                                                                                                  
Swap used:      0.0%                                                                                                  
Usage On:       16%                                                                                                   
Users online:   1                                                                                                     
To run a command as administrator(user "root"),use "sudo <command>".                                                  
[openeuler@openeuler-riscv64 ~]$
```

Screen recording (From flashing the image to logging):

[![asciicast](https://asciinema.org/a/GzU3kCzrnvFfJMU1cJH30knrx.svg)](https://asciinema.org/a/GzU3kCzrnvFfJMU1cJH30knrx)

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
