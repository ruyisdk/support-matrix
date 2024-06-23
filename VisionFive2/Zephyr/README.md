# Zephyr VisionFive 2 Test Report

## Test Environment

### System Information

- Host: Arch Linux
- Reference Installation Documentation: [https://docs.zephyrproject.org/latest/boards/starfive/visionfive2/doc/index.html](https://docs.zephyrproject.org/latest/boards/starfive/visionfive2/doc/index.html)

### Hardware Information

- StarFive VisionFive2
- Power Adapter
- A USB to UART Debugger

## Installation Steps

### Configuring the Zephyr Environment

*Environment configuration for other distributions can be found in the [Zephyr Official Documentation](https://docs.zephyrproject.org/latest/develop/getting_started/index.html)*

For Arch Linux, the environment can be installed directly from AUR:
```bash
yay -Syu python-west zephyr-sdk openocd
# paru -S python-west zephyr-sdk openocd pyocd
```

Next, set up the environment (replace the SDK path accordingly):
```bash
cp /usr/share/zephyr-sdk/zephyrrc ~/.zephyrrc
sudo cp /opt/zephyr-sdk/sysroots/x86_64-pokysdk-linux/usr/share/openocd/contrib/60-openocd.rules /etc/udev/rules.d/
sudo udevadm control --reload
source ~/zephyrproject/.venv/bin/activate
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
source ~/zephyrproject/.venv/bin/activate
west init ~/zephyrproject/
cd ~/zephyrproject/
west update
west zephyr-export
```

### Compiling spl_tools

Clone [https://github.com/starfive-tech/Tools.git](https://github.com/starfive-tech/Tools.git) and compile the spl_tool from it:
```bash
git clone https://github.com/starfive-tech/Tools.git
cd Tools/spl_tool
make
cd ../..
```

### Compiling the Example Program

Compile the example program and add the SPL header:
```bash
pip install -r ~/zephyrproject/zephyr/scripts/requirements.txt
west build -p always -b visionfive2 ~/zephyrproject/zephyr/samples/hello_world
Tools/spl_tool/spl_tool -c -f ~/zephyrproject/zephyr/build/zephyr/zephyr.bin
```

At this point, `zephyr.bin.normal.out` should be generated in `~/zephyrproject/zephyr/build/zephyr/`.

### Flashing and Running the Example Program

Set the VisionFive2 to boot from UART (both dip switches set to 1). If set correctly, you should see a UART output prompt: `CCCCCC...`.

Clone the following repositories in the working directory:

- vf2-loader tool [https://github.com/orangecms/vf2-loader.git](https://github.com/orangecms/vf2-loader.git)
- xmodem tool [https://github.com/orangecms/xmodem.rs.git](https://github.com/orangecms/xmodem.rs.git)

Switch xmodem.rs to the dev branch:
```bash
git clone https://github.com/orangecms/vf2-loader.git 
git clone https://github.com/orangecms/xmodem.rs.git
cd xmodem.rs
git checkout dev
cd ..
```

Navigate to the `vf2-loader` directory and copy the previously generated `zephyr.bin.normal.out` to the current directory:
```bash
cd vf2-loader
cp ~/zephyrproject/zephyr/build/zephyr/zephyr.bin.normal.out .
```

Connect UART and flash the image:
```bash
cargo run -- zephyr.bin.normal.out && minicom -D /dev/ttyUSB0
```

## Expected Results

The system should start normally and output "Hello World".

## Actual Results

The image was flashed via UART, but no output was seen.

Screen recording:
[![asciicast](https://asciinema.org/a/a2i4u5ryVYGEBo73UzswGGFAn.svg)](https://asciinema.org/a/a2i4u5ryVYGEBo73UzswGGFAn)

### Forum Post

https://forum.rvspace.org/t/no-output-while-trying-zephyr-on-visionfive-2/4243

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test failed.
