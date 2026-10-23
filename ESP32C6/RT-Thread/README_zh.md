# RT-Thread ESP32-C6 测试报告

## 测试环境

### 操作系统信息

- 源码：https://github.com/RT-Thread/rt-thread/tree/65d666e5bb1e6b6b555e565755ac0aabb4e9a02a
- 实测 commit：`65d666e5bb1e6b6b555e565755ac0aabb4e9a02a`（串口横幅为 5.3.1，不是 git 标签 `v5.3.1`）
- 已由 [RT-Thread/rt-thread#11836](https://github.com/RT-Thread/rt-thread/pull/11836) 合入
- BSP：`bsp/ESP/ESP32_C6`
- 工具链：乐鑫 RISC-V GCC 11.2.0（`riscv32-esp-elf-gcc`）
- 当时官方 `RT-Thread-packages/esp-idf` 没有 C6 的源码。编译用的是 https://github.com/cms19859230182-lang/esp-idf/tree/4fa003074a73774369d38123749fe64b7b4acbd3 ，克隆到 `packages/ESP-IDF-latest`。这里钉的是提交号而不是分支，因为 `bsp/esp32c6-scons` 的分支尖会往后挪。这就是 [RT-Thread-packages/esp-idf#17](https://github.com/RT-Thread-packages/esp-idf/pull/17)，没有合入。

### 硬件信息

- ESP32-C6-DevKitC-1
- 模组：ESP32-C6-WROOM-1，RISC-V，revision v0.2，8MB Flash
- UART0 在板子的 UART USB 口上，GPIO16 / GPIO17，CP210x，115200 8-N-1
- 烧录参数：DIO、8MB、80MHz，应用程序在 `0x10000`

默认镜像打开 GPIO、UART0 和 ADC。I2C、SPI、PWM、Wi-Fi、BLE 和 GDBStub 关闭。

## 安装步骤

### 编译

```
git clone https://github.com/RT-Thread/rt-thread.git
cd rt-thread
git checkout 65d666e5bb1e6b6b555e565755ac0aabb4e9a02a
cd bsp/ESP/ESP32_C6
```

把 esp-idf 那个 fork 钉到本次测试用的提交：

```
git clone https://github.com/cms19859230182-lang/esp-idf.git packages/ESP-IDF-latest
git -C packages/ESP-IDF-latest checkout 4fa003074a73774369d38123749fe64b7b4acbd3
git -C packages/ESP-IDF-latest rev-parse HEAD
```

`rev-parse HEAD` 必须打印 `4fa003074a73774369d38123749fe64b7b4acbd3`。对不上就停下来，不要编译；对上了再用 `riscv32-esp-elf-gcc` 11.2.0 执行 `scons`。

### 烧录

`builtin_imgs/bootloader.bin` 是 ESP32-C6 的 bootloader，不要换成 ESP32-C3 的。bootloader 写在 `0x0`，分区表写在 `0x8000`，`rtthread.bin` 写在 `0x10000`。

## 预期结果

开发板启动 RT-Thread。串口出现 5.3.1 横幅和 `msh >`。`help` 和 `version` 有回应。

## 实际结果

默认镜像进了 `msh`。`help` 和 `version` 有回应，`version` 是 5.3.1。`list timer` 里的 `current tick` 在增加。`free` 的 total 是 76704，已用堆大约 68904。

GPIO1 接 3.3V 为高，接 GND 为低。ADC1 通道 1（GPIO1）接 GND 读到 2167，接 3.3V 读到 4095。没有校准，所以地不是 0。

SPI2 回环把 GPIO7 和 GPIO2 短接，发出 `0xA5`，读回 `0xA5000000`，不是单字节对应，所以 SPI 仍不支持。这次不在默认镜像里。

打开 `BSP_ENABLE_GDBSTUB` 后，向地址 4 写一次，串口打出 `Entering gdb stub now.`。GDB 停在 `main`，PC 是 `0x42001c8c`，和 MEPC 相同。默认镜像关掉这个开关。

原始串口记录没有留档。上面的数字来自已经合入的那份 PR。

没有打开 Wi-Fi 和 BLE。

## 测试判断标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

默认镜像测试成功：串口 shell、GPIO1 和 ADC1。SPI、Wi-Fi 和 BLE 不在那份镜像里。
