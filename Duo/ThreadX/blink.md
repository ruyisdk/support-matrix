# ThreadX Milk-V Duo Test Report

## Test Environment

### Operating System Information

- Build System Version: Ubuntu 22.04 LTS x86_64
- System Version: [ThreadX-to-RISC-V64](https://github.com/saicogn/ThreadX-to-RISC-V64), commit [53010e6](https://github.com/saicogn/ThreadX-to-RISC-V64/commit/53010e6b5e5916c5e84c4faf4d1a93ad960dd566)
- Source Code Link: [ThreadX-to-RISC-V64](https://github.com/saicogn/ThreadX-to-RISC-V64)
- Reference Installation Document: [Introduction](https://github.com/saicogn/ThreadX-to-RISC-V64/blob/main/README.md)

### Hardware Information

- Milk-V Duo 64M
- A USB Power Adapter
- A USB-A to C or USB C to C Cable
- A TF Card
- A USB to UART Debugger (e.g., CH340, CH341, FT2232, etc.)
- Three Dupont Wires
- Milk-V Duo pre-soldered with necessary pin headers for debugging

## Installation Steps

### Setup System Environment

```bash
sudo apt install -y pkg-config build-essential ninja-build automake autoconf libtool wget curl git gcc libssl-dev bc slib squashfs-tools android-sdk-libsparse-utils jq python3-distutils scons parallel tree python3-dev python3-pip device-tree-compiler ssh cpio fakeroot libncurses5 flex bison libncurses5-dev genext2fs rsync unzip dosfstools mtools tcl openssh-client cmake expect -y
```

### Download and Build

```bash
sudo apt-get install wget git make
git clone https://github.com/milkv-duo/duo-examples.git --depth=1
cd duo-examples
source envsetup.sh
cd mailbox-test
make
```

This will generate the `mailbox_test` executable.

If the process is not normal, please refer to the [Project Introduction](https://milkv.io/zh/docs/duo/getting-started/rtoscore) to troubleshoot.

### Deploy the Executable File

Copy the executable to the user's home directory.

```bash
chmod +x mailbox_test
./mailbox_test
```

The output in the serial port will be as follows.

```log
[root@milkv-duo]~# ./mailbox_test 
RT: [507.950049]prvQueueISR
RT: [507.952485]recv cmd(19) from C906B, param_ptr [0x00000002]
RT: [507.958306]recv cmd(19) from C906B...send [0x00000004] to C906B
C906B: cmd.param_ptr = 0x4
RT: [511.965433]prvQueueISR
RT: [511.967867]recv cmd(19) from C906B, param_ptr [0x00000003]
RT: [511.973689]recv cmd(19) from C906B...send [0x00000004] to C906B
C906B: cmd.param_ptr = 0x3
```

## Expected Results

The light turns on for three seconds and then turns off.

## Actual Results

The light turns on for three seconds and then turns off.

Video:

https://github.com/ruyisdk/support-matrix/assets/17025286/c0350c17-5e94-4c07-96f7-a6b3f66c531c

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Test successful.

