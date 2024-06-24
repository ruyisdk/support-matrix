# Sipeed Maix-I

## Test Environment

### Operating System Information

- FreeRTOS (Kendryte K210 FreeRTOS SDK)
    - Source Code: https://github.com/kendryte/kendryte-freertos-sdk
    - Reference Installation Document: https://github.com/kendryte/kendryte-freertos-sdk
- RT-Thread
    - Source Code: https://github.com/RT-Thread/rt-thread/
    - Reference Installation Document: https://github.com/RT-Thread/rt-thread/tree/master/bsp/k210

### Hardware Information

- Sipeed Maix-Bit

## Test Results

| Software Category    | Package Name | Test Result (Test Report) |
| -------------------- | ------------ | ------------------------- |
| FreeRTOS Compilation | hello_world  | [Successful][FreeRTOS]    |
| RT-Thread            | N/A          | [Successful][RTThread]    |
| NuttX                | nsh          | [Successful][NuttX]       |

[FreeRTOS]: ./FreeRTOS/README.md
[RTThread]: ./RT-Thread/README.md
[NuttX]: ./NuttX/README.md
