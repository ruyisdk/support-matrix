---
product: Pine64 Oz64
cpu: SG2000
cpu_core: XuanTie C906 + ARM Cortex-A53
ram: 512MB
---

# Pine64 Oz64

## Test Environment

### Operating System Information

- Debian
  - Download Link: https://github.com/scpcom/sophgo-sg200x-debian/releases/tag/v1.6.10
  - Reference Installation Document: https://github.com/scpcom/sophgo-sg200x-debian
- NuttX
  - Precompiled Image: https://github.com/lupyuen2/wip-nuttx/releases/tag/sg2000c-1
  - Toolchain: xPack https://github.com/xpack-dev-tools/riscv-none-elf-gcc-xpack/releases
  - Reference Installation Document: https://nuttx.apache.org/docs/latest/quickstart/install.html
### Hardware Information

- Pine64 Oz64 (512MB, SG2000)

## Test Results

| Software Category | Package Name | Test Result (Test Report) |
| ----------------- | ------------ | ------------------------- |
| Debian Image Boot | N/A          | [Successful][Debian]      |
| NuttX Image Boot  | N/A          | [Successful][NuttX]       |

[Debian]: ./Debian/README.md
[NuttX]: ./NuttX/README.md
