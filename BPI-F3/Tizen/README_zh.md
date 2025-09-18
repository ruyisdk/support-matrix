# Tizen Snapshot 香蕉派 BPI-F3 测试报告

## 测试环境

### 系统信息

- 系统版本：Tizen-Unified-X riscv64 Snapshot 20250917
- 下载链接：
  - boot 镜像：http://download.tizen.org/snapshots/TIZEN/Tizen/Tizen-Unified-X/reference/images/standard/tizen-boot-riscv64-bpif3/tizen-unified-x_20250918.035403_tizen-boot-riscv64-bpif3.tar.gz
  - platform 镜像：http://download.tizen.org/snapshots/TIZEN/Tizen/Tizen-Unified-X/reference/images/standard/tizen-headless-riscv64/tizen-unified-x_20250918.035403_tizen-headless-riscv64.tar.gz
- 参考安装文档：https://docs.tizen.org/platform/developing/flashing-rpi/

### 硬件信息

- 香蕉派 BPI-F3
- 电源适配器
- microSD 卡一张
- USB to UART 调试器一个

## 安装步骤

### 刷写镜像

安装 `pv`:

```bash
sudo apt-get install pv
```

获取 SD 卡刷写脚本：

```bash
git clone git://review.tizen.org/git/platform/kernel/tizen-fusing-scripts -b tizen
cd tizen-fusing-scripts
```

下载 boot 和 platform 镜像，无需解压：

```bash
wget http://download.tizen.org/snapshots/TIZEN/Tizen/Tizen-Unified-X/reference/images/standard/tizen-boot-riscv64-bpif3/tizen-unified-x_20250918.035403_tizen-boot-riscv64-bpif3.tar.gz
wget http://download.tizen.org/snapshots/TIZEN/Tizen/Tizen-Unified-X/reference/images/standard/tizen-headless-riscv64/tizen-unified-x_20250918.035403_tizen-headless-riscv64.tar.gz
# or use headed image instead of headless:
# wget http://download.tizen.org/snapshots/TIZEN/Tizen/Tizen-Unified-X/reference/images/standard/tizen-headed-riscv64/tizen-unified-x_20250918.035403_tizen-headed-riscv64.tar.gz

```

插入 SD 卡，运行刷写脚本：(`/dev/mmcblk0` 请替换为你的 SD 卡设备名)
```bash
sudo ./tizen-fusing-scripts/scripts/sd_fusing.py -d /dev/mmcblk0 -t bpif3 --format
sudo ./tizen-fusing-scripts/scripts/sd_fusing.py -d /dev/mmcblk0 -b tizen-unified-x_20250918.035403_tizen-boot-riscv64-bpif3.tar.gz  tizen-unified-x_20250917.211322_tizen-headless-riscv64.tar.gz  -t bpif3
```


### 登录系统

通过串口登录系统。

用户名：`root`

密码：`tizen`

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

CFT

### 启动信息


## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

CFT