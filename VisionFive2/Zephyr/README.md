# Zephyr VisionFive 2 测试报告

## 测试环境

### 系统信息

- Host: Arch Linux
- 参考安装文档：[https://docs.zephyrproject.org/latest/boards/starfive/visionfive2/doc/index.html](https://docs.zephyrproject.org/latest/boards/starfive/visionfive2/doc/index.html)

### 硬件信息

- StarFive VisionFive2
- 电源适配器
- USB to UART 调试器一个

## 安装步骤

### 配置 Zephyr 环境

*其余发行版环境配置见：[Zephyr 官方文档](https://docs.zephyrproject.org/latest/develop/getting_started/index.html)*

对于 Arch Linux，环境可以直接从 AUR 安装：
```bash
yay -Syu python-west zephyr-sdk openocd
# paru -S python-west zephyr-sdk openocd pyocd
```

接下来搭建环境（注意替换 SDK 路径）：
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

### 编译 spl_tools

clone [https://github.com/starfive-tech/Tools.git](https://github.com/starfive-tech/Tools.git) 并编译其中的 spl_tool

```bash
git clone https://github.com/starfive-tech/Tools.git
cd Tools/spl_tool
make
cd ../..
```

### 编译示例程序

编译示例程序并添加 SPL 头：

```bash
pip install -r ~/zephyrproject/zephyr/scripts/requirements.txt
west build -p always -b visionfive2 ~/zephyrproject/zephyr/samples/hello_world
Tools/spl_tool/spl_tool -c -f ~/zephyrproject/zephyr/build/zephyr/zephyr.bin
```

此时应在 `~/zephyrproject/zephyr/build/zephyr/` 下生成了 `zephyr.bin.normal.out`。

### 烧录并运行示例程序

将 VisionFive2 的启动方式设置为从 UART 启动（两个拨码开关都为 1），若正确应能看到 UART 输出提示：`CCCCCC...`

在工作目录下 clone 以下仓库：

- vf2-loader tool [https://github.com/orangecms/vf2-loader.git](https://github.com/orangecms/vf2-loader.git)
- xmodem tool [https://github.com/orangecms/xmodem.rs.git](https://github.com/orangecms/xmodem.rs.git)

将 xmodem.rs 切到 dev 分支

```bash
git clone https://github.com/orangecms/vf2-loader.git 
git clone https://github.com/orangecms/xmodem.rs.git
cd xmodem.rs
git checkout dev
cd ..
```

cd 进 `vf2-loader` 目录，并将之前生成的 `zephyr.bin.normal.out` 拷贝到当前目录：

```bash
cd vf2-loader
cp ~/zephyrproject/zephyr/build/zephyr/zephyr.bin.normal.out .
```

连接 UART，烧录镜像：

```bash
cargo run -- zephyr.bin.normal.out && minicom -D /dev/ttyUSB0
```

## 预期结果

系统正常启动，输出 Hello World 信息。

## 实际结果

UART 刷入，但未看到任何输出。

屏幕记录：
[![asciicast](https://asciinema.org/a/a2i4u5ryVYGEBo73UzswGGFAn.svg)](https://asciinema.org/a/a2i4u5ryVYGEBo73UzswGGFAn)

### 论坛帖

https://forum.rvspace.org/t/no-output-while-trying-zephyr-on-visionfive-2/4243

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试失败。
