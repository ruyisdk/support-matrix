# Buildroot VisionFive Test Report

## Test Environment

### System Information

- System Version: Buildroot
- Source Code Link: [Buildroot Download](https://buildroot.org/download.html)
    - As of the time of writing, the latest stable/LTS version of Buildroot is: [buildroot-2024.02.1](https://buildroot.org/downloads/buildroot-2024.02.1.tar.gz)
- Reference Installation Document: [VisionFive Buildroot Documentation](https://gitlab.com/buildroot.org/buildroot/-/tree/master/board/visionfive?ref_type=heads)
- Build Machine OS: Arch Linux x86_64

### Hardware Information

- StarFive VisionFive (v1)
- Power Adapter
- A USB A to C or C to C Cable
- A microSD Card
- A USB to UART Debugger

## Building and Flashing the Image

Since VisionFive’s Buildroot support is upstreamed, you can directly fetch the source code from Buildroot to build the functional image.

### Preparing the Build Environment

```shell
sudo pacman -S which sed make binutils diffutils gcc bash patch gzip bzip2 perl tar cpio unzip rsync file bc findutils wget
# Or using package form AUR
# paru -S buildroot-meta
```

If you are not using Arch Linux, refer to the [official documentation](https://buildroot.org/downloads/manual/manual.html#requirement) to install the necessary dependencies (note that the names of the packages might differ).

### Building the Image

```shell
wget https://buildroot.org/downloads/buildroot-2024.02.1.tar.gz
tar xvf buildroot-2024.02.1.tar.gz
cd buildroot-2024.02.1/
make visionfive_defconfig
make -j$(nproc)
```

Note: Ensure you have a stable internet connection; dependencies will be downloaded automatically during the compilation.

After the build, an `sdcard.img` image will be created in the `output/images` directory.

### Flashing the Image to the microSD Card

Use `dd` to write the image to the microSD card.

Here, we assume the storage card is located at `/dev/sdc`.

```shell
sudo wipefs -af /dev/sdc
sudo dd if=~/buildroot-2024.02.1/output/images/sdcard.img of=/dev/sdc bs=1M status=progress oflag=direct
```

### Logging into the System

Logging into the system via the serial port.

Default username: `root`

Default password: none, login is automatic after entering the username.

## Expected Results

The system should boot normally and allow login through the onboard serial port.

## Actual Results

The system booted successfully and login through the onboard serial port was also successful.

### Boot Log

```log
Welcome to Buildroot                                                                                                                
buildroot login: root                                                                                                               
# uname -a                                                                                                                          
Linux buildroot 6.0.0-visionfive #1 SMP Wed Mar 27 20:54:25 CST 2024 riscv64 GNU/Linux                                              
# starfive-drm soc:display-subsystem: [drm] Cannot find any crtc or sizes                                                           
# cat /etc/os-release                                                                                                               
NAME=Buildroot                                                                                                                      
VERSION=2024.02.1                                                                                                                   
ID=buildroot                                                                                                                        
VERSION_ID=2024.02.1                                                                                                                
PRETTY_NAME="Buildroot 2024.02.1"                                                                                                   
# 
```

Screen recording (from flashing the image to logging into the system):

[![asciicast](https://asciinema.org/a/jCbFkO6AUUriql5b1g7QzGuXD.svg)](https://asciinema.org/a/jCbFkO6AUUriql5b1g7QzGuXD)

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
