---
product: Milk-V Jupiter
cpu: Key Stone K1/M1
cpu_core: SpacemiT X60
ram: 4G/8G/16G

vendor: milkv-jupiter
board_variant: [4g, 8g, 16g]
cpu_arch: [
    spacemit-x60,
]
---

# Milk-V Jupiter

## Test Environment

### Operating System Information

- Bianbu
  - Download Link: https://github.com/milkv-jupiter/jupiter-bianbu-build/releases
  - Reference Installation Document: https://milkv.io/zh/docs/jupiter/getting-started/boot
- openKylin 2.0-SP1
  - Download link: https://www.openkylin.top/downloads/index-cn.html
  - Reference installation document: https://docs.openkylin.top/zh/01_%E5%AE%89%E8%A3%85%E5%8D%87%E7%BA%A7%E6%8C%87%E5%8D%97/%E5%9C%A8riscv%E4%B8%8A%E5%AE%89%E8%A3%85/%E5%9C%A8LicheePi4A%E4%B8%8A%E5%AE%89%E8%A3%85openKylin

### Hardware Information

- Milk-V Jupiter

## Test Results

| Software Category    | Package Name | Test Results (Test Report) |
| -------------------- | ------------ | -------------------------- |
| Bianbu Image Boot    | N/A          | [Good](Bianbu)             |
| openKylin Image Boot | N/A          | [Failed](oK)               |

[Bianbu]: Bianbu/README.md
[oK]: openKylin/README.md
