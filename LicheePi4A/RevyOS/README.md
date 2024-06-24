# RevyOS LPi4A Test Report

## Test Environment

### System Information

- System Version: RevyOS 20231210
- Download Link: [ISCAS mirror](https://mirror.iscas.ac.cn/revyos/extra/images/lpi4a/)
- Reference Installation Document: [Visit here](https://revyos.github.io/docs/)

### Hardware Information

- Lichee Pi 4A (16GB RAM + 128GB eMMFAQC)
- USB-C Power Adapter / DC Power Supply
- USB-UART Debugger

## Installation Steps

### Using the `ruyi` CLI to Flash Image to Onboard eMMC

Install the [`ruyi`](https://github.com/ruyisdk/ruyi) package manager, run `ruyi device provision`, and follow the prompts.

### Logging into the System

Logging into the system via serial console or graphical interface.

Default username: `debian`
Default password: `debian`

## Expected Results

The system boots up successfully and can be accessed via the serial console.

## Actual Results

The system boots up successfully and login via the serial console is successful.

### Boot Log

```log
Debian GNU/Linux 12 lpi4a ttyS0

lpi4a login: debian
Password: 

   ____              _ ____  ____  _  __
  |  _ \ _   _ _   _(_) ___||  _ \| |/ /
  | |_) | | | | | | | \___ \| | | | ' / 
  |  _ <| |_| | |_| | |___) | |_| | . \ 
  |_| \_\\__,_|\__, |_|____/|____/|_|\_\
               |___/                    
                   -- Presented by ISCAS

  Debian GNU/Linux 12 (bookworm) (kernel 5.10.113-lpi4a)

Linux lpi4a 5.10.113-lpi4a #2023.12.08.03.26+b8c5d3546 SMP PREEMPT Fri Dec 8 03:26:13 UTC 2 riscv64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
debian@lpi4a:~$ [   55.898441] es8156_set_bias_level codec_uninit_sequence

debian@lpi4a:~$ uname -a
Linux lpi4a 5.10.113-lpi4a #2023.12.08.03.26+b8c5d3546 SMP PREEMPT Fri Dec 8 03:26:13 UTC 2 riscv64 GNU/Linux
debian@lpi4a:~$ cat /proc/cpu-i[   64.361096] es8156_set_bias_level codec_uninit_sequence
^C
debian@lpi4a:~$ cat /proc/cpuinfo 
processor       : 0
hart            : 0
isa             : rv64imafdcvsu
mmu             : sv39
cpu-freq        : 1.848Ghz
cpu-icache      : 64KB
cpu-dcache      : 64KB
cpu-vector      : 0.7.1

processor       : 1
hart            : 1
isa             : rv64imafdcvsu
mmu             : sv39
cpu-freq        : 1.848Ghz
cpu-icache      : 64KB
cpu-dcache      : 64KB
cpu-l2cache     : 1MB
cpu-tlb         : 1024 4-ways
cpu-cacheline   : 64Bytes
cpu-vector      : 0.7.1

processor       : 2
hart            : 2
isa             : rv64imafdcvsu
mmu             : sv39
cpu-freq        : 1.848Ghz
cpu-icache      : 64KB
cpu-dcache      : 64KB
cpu-l2cache     : 1MB
cpu-tlb         : 1024 4-ways
cpu-cacheline   : 64Bytes
cpu-vector      : 0.7.1

processor       : 3
hart            : 3
isa             : rv64imafdcvsu
mmu             : sv39
cpu-freq        : 1.848Ghz
cpu-icache      : 64KB
cpu-dcache      : 64KB
cpu-l2cache     : 1MB
cpu-tlb         : 1024 4-ways
cpu-cacheline   : 64Bytes                                               
cpu-vector      : 0.7.1                                                   |
                                                                        |
debian@lpi4a:~$ cat /etc/os-release                                     
PRETTY_NAME="Debian GNU/Linux 12 (bookworm)"
NAME="Debian GNU/Linux"
VERSION_ID="12"
VERSION="12 (bookworm)"
VERSION_CODENAME=bookworm
ID=debian
HOME_URL="https://www.debian.org/"
SUPPORT_URL="https://www.debian.org/support"
BUG_REPORT_URL="https://bugs.debian.org/"
debian@lpi4a:~$ cat /etc/revyos-release 
BUILD_ID=20231210_134926
BUILD_DATE=20231210
RELEASE_ID=20231210
COMMIT_ID=d3a91ee19e6d4da2f941b47d0187b18f0127e926
RUNNER_ID=7158219074
debian@lpi4a:~$
```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.
