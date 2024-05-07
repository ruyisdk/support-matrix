# Sipeed Maix-I

## 测试环境

### 操作系统信息

- FreeRTOS (Kendryte K210 FreeRTOS SDK)
    - 源码链接：https://github.com/kendryte/kendryte-freertos-sdk
    - 参考安装文档：https://github.com/kendryte/kendryte-freertos-sdk
- RT-Thread
    - 源码链接：https://github.com/RT-Thread/rt-thread/
    - 参考安装文档：https://github.com/RT-Thread/rt-thread/tree/master/bsp/k210

### 硬件开发板信息

- Sipeed Maix-Bit

## 测试结果

| 软件分类      | 软件包名    | 测试结果（测试报告） |
|--------------|-------------|------------------|
| FreeRTOS 编译 | hello_world | [成功][FreeRTOS]   |
| RT-Thread    | N/A         | [成功][RTThread]   |
| NuttX        | nsh         | [成功][NuttX]      |

[FreeRTOS]: ./FreeRTOS/README.md
[RTThread]: ./RT-Thread/README.md
[NuttX]: ./NuttX/README.md
