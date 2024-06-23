# RT-Thread Milk-V Duo Test Report

## Test Environment

### Operating System Information

- Build System Version: Ubuntu 20.04 LTS x86_64
- System Version: RT-Thread 5.1.0, commit [3ff4fe5](https://github.com/RT-Thread/rt-thread/commit/3ff4fe5395516eb734b2cead9cc50f35e54f6511)
- Source Code Link: https://github.com/RT-Thread/rt-thread
- Reference Installation Document: https://github.com/RT-Thread/rt-thread/tree/master/bsp/cvitek/cv1800b

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

Note: Please use Ubuntu 20.04. It is known that later versions might result in build failures.

You can use Docker or other container environments for the build.

Install the required packages:

```shell
sudo apt update && sudo apt install -y git gcc build-essential scons libncurses5-dev python3 python3-requests curl
```

Get the toolchain:

```shell
curl -LO https://github.com/RT-Thread/toolchains-ci/releases/download/v1.7/riscv64-linux-musleabi_for_x86_64-pc-linux-gnu_latest.tar.bz2
tar xvf riscv64-linux-musleabi_for_x86_64-pc-linux-gnu_latest.tar.bz2
export RTT_EXEC_PATH=~/riscv64-linux-musleabi_for_x86_64-pc-linux-gnu/bin
```

### Getting the Source Code and Compiling the Firmware

```shell
git clone --depth=1 https://github.com/RT-Thread/rt-thread
cd rt-thread/bsp/cvitek/cv1800b
scons --menuconfig
source ~/.env/env.sh
scons -j$(nproc) --verbose
cd ../
bash combine-fip.sh
```

After execution, two files, boot.sd and fip.bin, will be generated in the `cvitek` directory.

### Preparing the microSD Card

Wipe the microSD card (use `wipefs -af /path/to/your-card`) and create a FAT32 partition.

Copy the compiled boot.sd and fip.bin onto the microSD card. At this point, the card is ready to boot RT-Thread on the Duo.

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
