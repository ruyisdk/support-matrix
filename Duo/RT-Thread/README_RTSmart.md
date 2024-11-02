---
sys: rtthread
sys_ver: null
sys_var: smart

status: basic
last_update: 2024-11-02
---

# RT-Thread Milk-V Duo Test Report

## Test Environment

### Operating System Information

- Source Code Link: https://github.com/RT-Thread/rt-thread
- Reference Installation Document: https://github.com/RT-Thread/rt-thread/blob/master/bsp/cvitek/README.md

### Hardware Information

- Milk-V Duo 64M
- A USB Power Adapter
- A USB-A to C or USB C to C Cable
- A microSD Card
- A USB to UART Debugger (e.g., CH340, CH341, FT2232, etc.)
- Three Dupont Lines
- Headers pre-soldered on the Milk-V Duo for debugging purposes

## Installation Steps

### Preparing the System Environment

Install the required packages:

```shell
sudo apt install -y scons libncurses5-dev device-tree-compiler
```

Get the toolchain:

```shell
wget https://github.com/RT-Thread/toolchains-ci/releases/download/v1.7/riscv64-linux-musleabi_for_x86_64-pc-linux-gnu_latest.tar.bz2

tar -xjvf riscv64-linux-musleabi_for_x86_64-pc-linux-gnu_latest.tar.bz2
```

Update the following paths as needed:
```bash
export RTT_CC_PREFIX=riscv64-unknown-linux-musl-
export RTT_EXEC_PATH=/opt/riscv64-linux-musleabi_for_x86_64-pc-linux-gnu/bin
```

### Fetching the Source Code and Compiling the Firmware

```shell
git clone --depth=1 https://github.com/RT-Thread/rt-thread
cd rt-thread/bsp/cvitek/cv18xx_risc-v
# Generate configuration
scons --menuconfig
```

In menuconfig, please select `milkv-duo` under the `Board Type` option. Enter `RT-Thread Kernel` submenu ---> Select `Enable RT-Thread Smart (microkernel on kernel/userland)` to enable the RT-Smart kernel.

```shell
source ~/.env/env.sh
scons -j$(nproc) --verbose
cd ../
./combine-fip.sh $(pwd)/cv18xx_risc-v Image
```

`boot.sd` and `fip.bin` files will be generated in the `cvitek/output/milkv-duo` directory upon completion.

### Preparing the microSD Card

Clear the microSD card and create a FAT32 partition:
```shell
wipefs -af /path/to/your-card
mkfs.fat /path/to/your-card
```

Copy the generated `boot.sd` and `fip.bin` files onto the microSD card. The storage card is now ready to boot RT-Thread on the Duo.

### Logging into the System

Logging into the system via the serial port.

## Expected Results

The system should boot normally and allow login through the serial port.

## Actual Results

The system booted successfully, and login through the serial port was successful.

### Boot Log

```log
Boot from SD ...                                                                                                                    
switch to partitions #0, OK                                                                                                         
mmc0 is current device                                                                                                              
173704 bytes read in 10 ms (16.6 MiB/s)                                                                                             
## Loading kernel from FIT Image at 81400000 ...                                                                                    
   Using 'config-cv1800b_milkv_duo_sd' configuration                                                                                
   Trying 'kernel-1' kernel subimage                                                                                                
   Verifying Hash Integrity ... crc32+ OK                                                                                           
## Loading fdt from FIT Image at 81400000 ...                                                                                       
   Using 'config-cv1800b_milkv_duo_sd' configuration                                                                                
   Trying 'fdt-cv1800b_milkv_duo_sd' fdt subimage                                                                                   
   Verifying Hash Integrity ... sha256+ OK                                                                                          
   Booting using the fdt blob at 0x814255c4                                                                                         
   Uncompressing Kernel Image                                                                                                       
   Decompressing 424720 bytes used 58ms                                                                                             
   Loading Device Tree to 0000000081be5000, end 0000000081becb60 ... OK                                                             
                                                                                                                                    
Starting kernel ...                                                                                                                 
                                                                                                                                    
heap: [0x8029be68 - 0x8129be68]                                                                                                     
                                                                                                                                    
 \ | /                                                                                                                              
- RT -     Thread Smart Operating System                                                                                            
 / | \     5.1.0 build Mar 26 2024 05:52:37                                                                                         
 2006 - 2024 Copyright by RT-Thread team                                                                                            
Hello RT-Smart!                                                                                                                     
msh />  
```

Screen recording (from flashing the image to logging into the system):

[![asciicast](https://asciinema.org/a/gbDJeUr3mdHNxd3mXev7UpBGl.svg)](https://asciinema.org/a/gbDJeUr3mdHNxd3mXev7UpBGl)

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
