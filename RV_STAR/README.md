---
product: RV-STAR
cpu: GD32VF103
cpu_core: Nuclei Bumblebee
ram: 32KB(SRAM)
---

# Nuclei RV-STAR

## Test Environment

### Operating System Information

- FreeRTOS/RT-Thread/ThreadX/μCOSIII
    - Source Code Link: https://github.com/Nuclei-Software/nuclei-sdk
    - Reference Installation Document: https://doc.nucleisys.com/nuclei_sdk/quickstart.html#build-run-and-debug-sample-application
- LiteOS
    - Source Code Link: https://github.com/riscv-mcu/kernel_liteos_m
    - Reference Installation Document: https://github.com/riscv-mcu/kernel_liteos_m/blob/nuclei/OpenHarmony-3.0-LTS/targets/riscv_nuclei_gd32vf103_soc_gcc/README.md
### Hardware Information

- RV-STAR Development Board (GD32VF103VBT6)

## Test Results

| Software Category | Package Name | Test Results (Test Report) |
| ----------------- | ------------ | -------------------------- |
| FreeRTOS          | N/A          | [Success][FreeRTOS]        |
| RT-Thread         | N/A          | [Success][RT-Thread]       |
| ThreadX           | N/A          | [Success][ThreadX]         |
| μC/OS-II          | N/A          | [Success][uCOSII]          |
| LiteOS            | N/A          | [Success][LiteOS]          |

[FreeRTOS]: ./FreeRTOS/README.md
[LiteOS]: ./LiteOS/README.md
[RT-Thread]: ./RT-Thread/README.md
[ThreadX]: ./ThreadX/README.md
[uCOSII]: ./uCOSII/README.md