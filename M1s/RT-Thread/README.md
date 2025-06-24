---
sys: rtthread
sys_ver: null
sys_var: null

status: cfh
last_update: 2025-06-24
---

# RT-Thread Sipeed M1s Dock Test Report

## Test Environment

### Operating System Information

- Download Link: https://github.com/DongshanPI/buildroot_dongshannezhastu
- Reference Installation Document: https://github.com/RT-Thread/rt-thread/tree/master/bsp/bouffalo_lab/bl808
- toolchain:
  - riscv64-unknown-elf-: https://occ-oss-prod.oss-cn-hangzhou.aliyuncs.com/resource//1695015854856/Xuantie-900-gcc-elf-newlib-x86_64-V2.6.1-20220906.tar.gz
  - riscv64-unknown-linux-musl-: https://github.com/RT-Thread/toolchains-ci/releases/download/v1.9/Xuantie-900-gcc-linux-6.6.0-musl64-x86_64-V3.0.2.tar.gz

### Hardware Information

- Sipeed M1s Dock
- a Type-C cable

## Installation Steps

### Compiling the Firmwarehh

Clone repo:
```bash
git clone https://github.com/RT-Thread/rt-thread
cd rt-thread/bsp/bouffalo_lab/bl808
git submodule update --init --recursive
git submodule update --recursive --remote
```

m0 and lp using compiler `riscv64-unknown-elf-gcc`

Download the toolchain and configure env variables:
```bash
wget https://occ-oss-prod.oss-cn-hangzhou.aliyuncs.com/resource//1695015854856/Xuantie-900-gcc-elf-newlib-x86_64-V2.6.1-20220906.tar.gz
sudo tar -zxvf Xuantie-900-gcc-elf-newlib-x86_64-V2.6.1-20220906.tar.gz -C /opt

export RTT_CC="gcc"
export RTT_CC_PREFIX=riscv64-unknown-elf-
export RTT_EXEC_PATH=/opt/Xuantie-900-gcc-elf-newlib-x86_64-V2.6.1/bin
```

#### m0

Compile:
```bash
scons -C m0 -j$(nproc)
```

If the compilation is successful, the `m0/rtthread.elf` and `m0/rtthread_m0.bin` files will be generated.


#### lp

Compile:
```bash
scons -C lp -j$(nproc)
```

If the compilation is successful, the `lp/rtthread.elf` and `lp/rtthread_lp.bin` files will be generated.

#### d0

d0 using compiler `riscv64-unknown-linux-musl-gcc`

Download the toolchain and configure env variables:
```bash
wget https://github.com/RT-Thread/toolchains-ci/releases/download/v1.9/Xuantie-900-gcc-linux-6.6.0-musl64-x86_64-V3.0.2.tar.gz
sudo tar -zxvf Xuantie-900-gcc-linux-6.6.0-musl64-x86_64-V3.0.2.tar.gz -C /opt

export RTT_CC="gcc"
export RTT_CC_PREFIX=riscv64-unknown-linux-musl-
export RTT_EXEC_PATH=/opt/riscv64-linux-musleabi_for_x86_64-pc-linux-gnu/bin
```

Compile:
```bash
scons -C d0 -j$(nproc)
```

Use `merge_rtsmart.py` merge `hw.dtb.5M`, `spl_bl808_d0.bin`, `opensbi_v0.6.bin` and `rtthread_d0.bin` into the final flash file `whole_img_d0.bin`:
```bash
cd d0
python merge_rtsmart.py
```

### Flashing Image

Use `dd` to flash the image to the SD card:
```bash
sudo dd if=dongshannezhastu-sdcard.img of=/dev/your/device bs=1M status=progress
```

### Logging into the System

Login to the system via the serial port.

## Expected Results

The system should boot up normally and allow login through the onboard serial port.

## Actual Results

Firmware for lp and d0 cannot be compiled:

```log
❯ scons -C lp -j$(nproc)
scons: Reading SConscript files ...

scons: *** missing SConscript file 'build/kernel/libcpu/risc-v/t-head/e9xx/SConscript'
File "/home/aisuneko/Documents/Project/rt-thread/libcpu/risc-v/SConscript", line 23, in <module>

❯ scons -C d0 -j$(nproc)
scons: Entering directory `/home/aisuneko/Documents/Project/rt-thread/bsp/bouffalo_lab/bl808/d0'
scons: Reading SConscript files ...
Newlib version: 3.2.0
scons: Entering directory `/home/aisuneko/Documents/Project/rt-thread/components/lwp/vdso/user/arch/risc-v'
scons: Reading SConscript files ...
scons: done reading SConscript files.
scons: Building targets ...
riscv64-unknown-elf-gcc -o vdso_sys.os -c -march=rv64imafdc -mabi=lp64 -mcmodel=medany -Wall -Wno-cpp -std=gnu99 -fdiagnostics-color=always -fPIC -O2 -I . -I /home/aisuneko/Documents/Project/rt-thread/components/lwp/vdso/user/arch/risc-v/../../.. -fPIC vdso_sys.c
In file included from ./vdso_sys.h:19,
                 from vdso_sys.c:17:
/home/aisuneko/Documents/Project/rt-thread/components/lwp/vdso/user/arch/risc-v/../../../vdso_datapage.h:34:22: error: 'CLOCK_TAI' undeclared here (not in a function)
   34 | #define VDSO_BASES  (CLOCK_TAI + 1)
      |                      ^~~~~~~~~
/home/aisuneko/Documents/Project/rt-thread/components/lwp/vdso/user/arch/risc-v/../../../vdso_datapage.h:59:30: note: in expansion of macro 'VDSO_BASES'
   59 |     struct timespec basetime[VDSO_BASES];
      |                              ^~~~~~~~~~
vdso_sys.c: In function '__rt_vdso_getcoarse':
vdso_sys.c:47:18: error: 'CLOCK_MONOTONIC_RAW' undeclared (first use in this function)
   47 |     if (clock != CLOCK_MONOTONIC_RAW)
      |                  ^~~~~~~~~~~~~~~~~~~
vdso_sys.c:47:18: note: each undeclared identifier is reported only once for each function it appears in
In file included from vdso_sys.c:17:
vdso_sys.c: In function '__vdso_clock_gettime_common':
/home/aisuneko/Documents/Project/rt-thread/components/lwp/vdso/user/arch/risc-v/../../../vdso_datapage.h:36:23: error: 'CLOCK_REALTIME_COARSE' undeclared (first use in this function); did you mean 'CLOCK_REALTIME'?
   36 |              BIT_MASK(CLOCK_REALTIME_COARSE))
      |                       ^~~~~~~~~~~~~~~~~~~~~
./vdso_sys.h:24:41: note: in definition of macro 'likely'
   24 | #define likely(x)   __builtin_expect(!!(x), 1)
      |                                         ^
/home/aisuneko/Documents/Project/rt-thread/components/lwp/vdso/user/arch/risc-v/../../../vdso_datapage.h:36:14: note: in expansion of macro 'BIT_MASK'
   36 |              BIT_MASK(CLOCK_REALTIME_COARSE))
      |              ^~~~~~~~
vdso_sys.c:81:22: note: in expansion of macro 'VDSO_REALTIME'
   81 |     if (likely(msk & VDSO_REALTIME))
      |                      ^~~~~~~~~~~~~
In file included from ./vdso_sys.h:18,
                 from vdso_sys.c:17:
/home/aisuneko/Documents/Project/rt-thread/components/lwp/vdso/user/arch/risc-v/../../../vdso_datapage.h:37:35: error: 'CLOCK_MONOTONIC' undeclared (first use in this function)
   37 | #define VDSO_MONOTIME   (BIT_MASK(CLOCK_MONOTONIC)   | \
      |                                   ^~~~~~~~~~~~~~~
/home/aisuneko/Documents/Project/rt-thread/components/lwp/vdso/user/arch/risc-v/../../../vdso_config.h:22:38: note: in definition of macro 'BIT_MASK'
   22 | #define BIT_MASK(nr)        ((1) << (nr))
      |                                      ^~
vdso_sys.c:83:20: note: in expansion of macro 'VDSO_MONOTIME'
   83 |     else if (msk & VDSO_MONOTIME)
      |                    ^~~~~~~~~~~~~
/home/aisuneko/Documents/Project/rt-thread/components/lwp/vdso/user/arch/risc-v/../../../vdso_datapage.h:38:23: error: 'CLOCK_MONOTONIC_COARSE' undeclared (first use in this function)
   38 |              BIT_MASK(CLOCK_MONOTONIC_COARSE)        | \
      |                       ^~~~~~~~~~~~~~~~~~~~~~
/home/aisuneko/Documents/Project/rt-thread/components/lwp/vdso/user/arch/risc-v/../../../vdso_config.h:22:38: note: in definition of macro 'BIT_MASK'
   22 | #define BIT_MASK(nr)        ((1) << (nr))
      |                                      ^~
vdso_sys.c:83:20: note: in expansion of macro 'VDSO_MONOTIME'
   83 |     else if (msk & VDSO_MONOTIME)
      |                    ^~~~~~~~~~~~~
/home/aisuneko/Documents/Project/rt-thread/components/lwp/vdso/user/arch/risc-v/../../../vdso_datapage.h:39:23: error: 'CLOCK_MONOTONIC_RAW' undeclared (first use in this function)
   39 |              BIT_MASK(CLOCK_MONOTONIC_RAW)           | \
      |                       ^~~~~~~~~~~~~~~~~~~
/home/aisuneko/Documents/Project/rt-thread/components/lwp/vdso/user/arch/risc-v/../../../vdso_config.h:22:38: note: in definition of macro 'BIT_MASK'
   22 | #define BIT_MASK(nr)        ((1) << (nr))
      |                                      ^~
vdso_sys.c:83:20: note: in expansion of macro 'VDSO_MONOTIME'
   83 |     else if (msk & VDSO_MONOTIME)
      |                    ^~~~~~~~~~~~~
/home/aisuneko/Documents/Project/rt-thread/components/lwp/vdso/user/arch/risc-v/../../../vdso_datapage.h:40:23: error: 'CLOCK_BOOTTIME' undeclared (first use in this function); did you mean 'CLOCK_REALTIME'?
   40 |              BIT_MASK(CLOCK_BOOTTIME))
      |                       ^~~~~~~~~~~~~~
/home/aisuneko/Documents/Project/rt-thread/components/lwp/vdso/user/arch/risc-v/../../../vdso_config.h:22:38: note: in definition of macro 'BIT_MASK'
   22 | #define BIT_MASK(nr)        ((1) << (nr))
      |                                      ^~
vdso_sys.c:83:20: note: in expansion of macro 'VDSO_MONOTIME'
   83 |     else if (msk & VDSO_MONOTIME)
      |                    ^~~~~~~~~~~~~
vdso_sys.c:87:1: warning: control reaches end of non-void function [-Wreturn-type]
   87 | }
      | ^
scons: *** [vdso_sys.os] Error 1
scons: building terminated because of errors.
CalledProcessError: Command '['scons', '-C', '/home/aisuneko/Documents/Project/rt-thread/components/lwp/vdso/user/arch/risc-v']' returned non-zero exit status 2.:
  File "/home/aisuneko/Documents/Project/rt-thread/bsp/bouffalo_lab/bl808/d0/SConstruct", line 36:
    objs = PrepareBuilding(env, RTT_ROOT, has_libcpu = False)
  File "/home/aisuneko/Documents/Project/rt-thread/bsp/bouffalo_lab/bl808/d0/../../../../tools/building.py", line 408:
    objs.extend(SConscript(Rtt_Root + '/components/SConscript',
  File "/usr/lib/python3.13/site-packages/SCons/Script/SConscript.py", line 687:
    return method(*args, **kw)
  File "/usr/lib/python3.13/site-packages/SCons/Script/SConscript.py", line 623:
    return _SConscript(self.fs, *files, **subst_kw)
  File "/usr/lib/python3.13/site-packages/SCons/Script/SConscript.py", line 281:
    exec(compile(scriptdata, scriptname, 'exec'), call_stack[-1].globals)
  File "/home/aisuneko/Documents/Project/rt-thread/components/SConscript", line 15:
    objs = objs + SConscript(os.path.join(item, 'SConscript'))
  File "/usr/lib/python3.13/site-packages/SCons/Script/SConscript.py", line 687:
    return method(*args, **kw)
  File "/usr/lib/python3.13/site-packages/SCons/Script/SConscript.py", line 623:
    return _SConscript(self.fs, *files, **subst_kw)
  File "/usr/lib/python3.13/site-packages/SCons/Script/SConscript.py", line 281:
    exec(compile(scriptdata, scriptname, 'exec'), call_stack[-1].globals)
  File "/home/aisuneko/Documents/Project/rt-thread/components/lwp/SConscript", line 57:
    group = group + SConscript(os.path.join('vdso', 'SConscript'))
  File "/usr/lib/python3.13/site-packages/SCons/Script/SConscript.py", line 687:
    return method(*args, **kw)
  File "/usr/lib/python3.13/site-packages/SCons/Script/SConscript.py", line 623:
    return _SConscript(self.fs, *files, **subst_kw)
  File "/usr/lib/python3.13/site-packages/SCons/Script/SConscript.py", line 281:
    exec(compile(scriptdata, scriptname, 'exec'), call_stack[-1].globals)
  File "/home/aisuneko/Documents/Project/rt-thread/components/lwp/vdso/SConscript", line 41:
    result = subprocess.run(command, env=process_env, check=True)
  File "/usr/lib/python3.13/subprocess.py", line 577:
    raise CalledProcessError(retcode, process.args,

```

### Boot Log

```log
```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

CFH
