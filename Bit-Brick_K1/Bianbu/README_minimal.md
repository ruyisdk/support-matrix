---
sys: bianbu
sys_ver: 2.2
sys_var: minimal

status: CFH
last_update: 2025-06-10
---

# Bianbu BIT-BRICK K1 Test Report

## Test Environment

### System Information

- System version: v2.2
- Download Links: https://archive.spacemit.com/image/k1/version/bianbu/v2.2/
- Reference Installation Document: https://docs.bit-brick.com/docs/k1/getting-started/preparation

### Hardware Information

- BIT-BRICK K1
- Power Adapter
- A microSD Card
- A USB to UART Debugger

## Installation Steps

### Flashing the Image (SD Card)

**Please make sure to choose the file ending with `.img.zip`**
After downloading and extracting the image, use `dd` to flash the image to the microSD card.

```bash
unzip bianbu-24.04-minimal-k1-v2.2-release-20250430181626.img.zip
sudo dd if=bianbu-24.04-minimal-k1-v2.2-release-20250430181626.img of=/dev/<your-device> bs=1M status=progress
```

### Logging into the System

Logging into the system via the serial port.

Default Username: `root`
Default Password: `bianbu`

## Expected Results

The system should boot up normally and allow login through the onboard serial port and through GUI.

## Actual Results

Boot failed upon a `hung_task` error.

### Boot Log

```log
[  242.724733] INFO: task swapper/0:1 blocked for more than 120 seconds.
[  242.731243]       Not tainted 6.6.63 #2.2.0.2
[  242.735657] "echo 0 > /proc/sys/kernel/hung_task_timeout_secs" disables this message.
[  242.743564] task:swapper/0       state:D stack:0     pid:1     ppid:0      flags:0x00000002
[  242.752008] Call Trace:
[  242.754478] [<ffffffff80fe0612>] __schedule+0x32e/0xa88
[  242.759778] [<ffffffff80fe0dba>] schedule+0x4e/0xd8
[  242.764687] [<ffffffff80fe5dba>] schedule_timeout+0x6e/0x168
[  242.770385] [<ffffffff80fe15e4>] __wait_for_common+0xd4/0x1c4
[  242.776175] [<ffffffff80fe1710>] wait_for_completion_timeout+0x18/0x20
[  242.782767] [<ffffffff80bdf32c>] mbox_send_message+0x8e/0xfe
[  242.788489] [<ffffffff80be5432>] spacemit_rproc_kick+0x38/0x92
[  242.794351] [<ffffffff80be4286>] rproc_virtio_notify+0x26/0x54
[  242.800240] [<ffffffff806f1870>] virtqueue_notify+0x16/0x2e
[  242.805866] [<ffffffff80be755a>] rpmsg_probe+0x362/0x3a4
[  242.811224] [<ffffffff806f1630>] virtio_dev_probe+0x13c/0x1d8
[  242.817041] [<ffffffff8082f5cc>] really_probe+0x8c/0x326
[  242.822403] [<ffffffff8082f8c8>] __driver_probe_device+0x62/0x110
[  242.828568] [<ffffffff8082f9ac>] driver_probe_device+0x36/0xba
[  242.834426] [<ffffffff8082faa2>] __device_attach_driver+0x72/0xd0
[  242.840581] [<ffffffff8082d81e>] bus_for_each_drv+0x5c/0xb2
[  242.846195] [<ffffffff8082fe6a>] __device_attach+0x84/0x158
[  242.851807] [<ffffffff808300e2>] device_initial_probe+0xe/0x16
[  242.857712] [<ffffffff8082e616>] bus_probe_device+0x86/0x88
[  242.863335] [<ffffffff8082bf04>] device_add+0x532/0x6ea
[  242.868609] [<ffffffff806f136a>] register_virtio_device+0x1c6/0x1ec
[  242.874929] [<ffffffff80be499c>] rproc_vdev_do_start+0xbc/0x1a6
[  242.880900] [<ffffffff80fdb528>] rproc_start_subdevices+0x24/0x56
[  242.887055] [<ffffffff80fdb81a>] rproc_start+0x9e/0xf8
[  242.892246] [<ffffffff80be12e8>] rproc_boot+0x26e/0x3d4
[  242.897516] [<ffffffff80be5894>] spacemit_rproc_probe+0x1ca/0x374
[  242.903660] [<ffffffff80831f86>] platform_probe+0x52/0xaa
[  242.909111] [<ffffffff8082f5cc>] really_probe+0x8c/0x326
[  242.914478] [<ffffffff8082f8c8>] __driver_probe_device+0x62/0x110
[  242.920622] [<ffffffff8082f9ac>] driver_probe_device+0x36/0xba
[  242.926501] [<ffffffff8082fbbc>] __driver_attach+0xbc/0x19e
[  242.932112] [<ffffffff8082d774>] bus_for_each_dev+0x58/0xa6
[  242.937749] [<ffffffff8082f05a>] driver_attach+0x1a/0x22
[  242.943075] [<ffffffff8082e842>] bus_add_driver+0xf6/0x1fe
[  242.948615] [<ffffffff80830a48>] driver_register+0x3e/0xd8
[  242.954155] [<ffffffff80831c82>] __platform_driver_register+0x1e/0x26
[  242.960678] [<ffffffff810392a6>] spacemit_rproc_driver_init+0x1a/0x22
[  242.967155] [<ffffffff800027aa>] do_one_initcall+0x36/0x218
[  242.972785] [<ffffffff81001452>] kernel_init_freeable+0x22c/0x296
[  242.978939] [<ffffffff80fded84>] kernel_init+0x26/0x116
[  242.984227] [<ffffffff80fe7816>] ret_from_fork+0xe/0x18
[  363.556737] INFO: task swapper/0:1 blocked for more than 241 seconds.
[  363.563247]       Not tainted 6.6.63 #2.2.0.2
[  363.567641] "echo 0 > /proc/sys/kernel/hung_task_timeout_secs" disables this message.
[  363.575516] task:swapper/0       state:D stack:0     pid:1     ppid:0      flags:0x00000002
[  363.583905] Call Trace:
[  363.586361] [<ffffffff80fe0612>] __schedule+0x32e/0xa88
[  363.591650] [<ffffffff80fe0dba>] schedule+0x4e/0xd8
[  363.596557] [<ffffffff80fe5dba>] schedule_timeout+0x6e/0x168
[  363.602237] [<ffffffff80fe15e4>] __wait_for_common+0xd4/0x1c4
[  363.608047] [<ffffffff80fe1710>] wait_for_completion_timeout+0x18/0x20
[  363.614613] [<ffffffff80bdf32c>] mbox_send_message+0x8e/0xfe
[  363.620322] [<ffffffff80be5432>] spacemit_rproc_kick+0x38/0x92
[  363.626201] [<ffffffff80be4286>] rproc_virtio_notify+0x26/0x54
[  363.632098] [<ffffffff806f1870>] virtqueue_notify+0x16/0x2e
[  363.637736] [<ffffffff80be755a>] rpmsg_probe+0x362/0x3a4
[  363.643084] [<ffffffff806f1630>] virtio_dev_probe+0x13c/0x1d8
[  363.648873] [<ffffffff8082f5cc>] really_probe+0x8c/0x326
[  363.654212] [<ffffffff8082f8c8>] __driver_probe_device+0x62/0x110
[  363.660356] [<ffffffff8082f9ac>] driver_probe_device+0x36/0xba
[  363.666246] [<ffffffff8082faa2>] __device_attach_driver+0x72/0xd0
[  363.672370] [<ffffffff8082d81e>] bus_for_each_drv+0x5c/0xb2
[  363.677985] [<ffffffff8082fe6a>] __device_attach+0x84/0x158
[  363.683612] [<ffffffff808300e2>] device_initial_probe+0xe/0x16
[  363.689510] [<ffffffff8082e616>] bus_probe_device+0x86/0x88
[  363.695122] [<ffffffff8082bf04>] device_add+0x532/0x6ea
[  363.700385] [<ffffffff806f136a>] register_virtio_device+0x1c6/0x1ec
[  363.706737] [<ffffffff80be499c>] rproc_vdev_do_start+0xbc/0x1a6
[  363.712687] [<ffffffff80fdb528>] rproc_start_subdevices+0x24/0x56
[  363.718835] [<ffffffff80fdb81a>] rproc_start+0x9e/0xf8
[  363.724009] [<ffffffff80be12e8>] rproc_boot+0x26e/0x3d4
[  363.729294] [<ffffffff80be5894>] spacemit_rproc_probe+0x1ca/0x374
[  363.735449] [<ffffffff80831f86>] platform_probe+0x52/0xaa
[  363.740878] [<ffffffff8082f5cc>] really_probe+0x8c/0x326
[  363.746255] [<ffffffff8082f8c8>] __driver_probe_device+0x62/0x110
[  363.752400] [<ffffffff8082f9ac>] driver_probe_device+0x36/0xba
[  363.758263] [<ffffffff8082fbbc>] __driver_attach+0xbc/0x19e
[  363.763857] [<ffffffff8082d774>] bus_for_each_dev+0x58/0xa6
[  363.769488] [<ffffffff8082f05a>] driver_attach+0x1a/0x22
[  363.774823] [<ffffffff8082e842>] bus_add_driver+0xf6/0x1fe
[  363.780342] [<ffffffff80830a48>] driver_register+0x3e/0xd8
[  363.785863] [<ffffffff80831c82>] __platform_driver_register+0x1e/0x26
[  363.792375] [<ffffffff810392a6>] spacemit_rproc_driver_init+0x1a/0x22
[  363.798865] [<ffffffff800027aa>] do_one_initcall+0x36/0x218
[  363.804469] [<ffffffff81001452>] kernel_init_freeable+0x22c/0x296
[  363.810630] [<ffffffff80fded84>] kernel_init+0x26/0x116
[  363.815916] [<ffffffff80fe7816>] ret_from_fork+0xe/0x18
[  484.388732] INFO: task swapper/0:1 blocked for more than 362 seconds.
[  484.395246]       Not tainted 6.6.63 #2.2.0.2
[  484.399619] "echo 0 > /proc/sys/kernel/hung_task_timeout_secs" disables this message.
[  484.407489] task:swapper/0       state:D stack:0     pid:1     ppid:0      flags:0x00000002
[  484.415929] Call Trace:
[  484.418386] [<ffffffff80fe0612>] __schedule+0x32e/0xa88
[  484.423646] [<ffffffff80fe0dba>] schedule+0x4e/0xd8
[  484.428542] [<ffffffff80fe5dba>] schedule_timeout+0x6e/0x168
[  484.434262] [<ffffffff80fe15e4>] __wait_for_common+0xd4/0x1c4
[  484.440039] [<ffffffff80fe1710>] wait_for_completion_timeout+0x18/0x20
[  484.446616] [<ffffffff80bdf32c>] mbox_send_message+0x8e/0xfe
[  484.452301] [<ffffffff80be5432>] spacemit_rproc_kick+0x38/0x92
[  484.458158] [<ffffffff80be4286>] rproc_virtio_notify+0x26/0x54
[  484.464046] [<ffffffff806f1870>] virtqueue_notify+0x16/0x2e
[  484.469693] [<ffffffff80be755a>] rpmsg_probe+0x362/0x3a4
[  484.475041] [<ffffffff806f1630>] virtio_dev_probe+0x13c/0x1d8
[  484.480840] [<ffffffff8082f5cc>] really_probe+0x8c/0x326
[  484.486199] [<ffffffff8082f8c8>] __driver_probe_device+0x62/0x110
[  484.492374] [<ffffffff8082f9ac>] driver_probe_device+0x36/0xba
[  484.498241] [<ffffffff8082faa2>] __device_attach_driver+0x72/0xd0
[  484.504375] [<ffffffff8082d81e>] bus_for_each_drv+0x5c/0xb2
[  484.510000] [<ffffffff8082fe6a>] __device_attach+0x84/0x158
[  484.515614] [<ffffffff808300e2>] device_initial_probe+0xe/0x16
[  484.521492] [<ffffffff8082e616>] bus_probe_device+0x86/0x88
[  484.527104] [<ffffffff8082bf04>] device_add+0x532/0x6ea
[  484.532378] [<ffffffff806f136a>] register_virtio_device+0x1c6/0x1ec
[  484.538678] [<ffffffff80be499c>] rproc_vdev_do_start+0xbc/0x1a6
[  484.544657] [<ffffffff80fdb528>] rproc_start_subdevices+0x24/0x56
[  484.550775] [<ffffffff80fdb81a>] rproc_start+0x9e/0xf8
[  484.555947] [<ffffffff80be12e8>] rproc_boot+0x26e/0x3d4
[  484.561223] [<ffffffff80be5894>] spacemit_rproc_probe+0x1ca/0x374
[  484.567335] [<ffffffff80831f86>] platform_probe+0x52/0xaa
[  484.572797] [<ffffffff8082f5cc>] really_probe+0x8c/0x326
[  484.578132] [<ffffffff8082f8c8>] __driver_probe_device+0x62/0x110
[  484.584265] [<ffffffff8082f9ac>] driver_probe_device+0x36/0xba
[  484.590157] [<ffffffff8082fbbc>] __driver_attach+0xbc/0x19e
[  484.595771] [<ffffffff8082d774>] bus_for_each_dev+0x58/0xa6
[  484.601363] [<ffffffff8082f05a>] driver_attach+0x1a/0x22
[  484.606698] [<ffffffff8082e842>] bus_add_driver+0xf6/0x1fe
[  484.612217] [<ffffffff80830a48>] driver_register+0x3e/0xd8
[  484.617749] [<ffffffff80831c82>] __platform_driver_register+0x1e/0x26
[  484.624241] [<ffffffff810392a6>] spacemit_rproc_driver_init+0x1a/0x22
[  484.630737] [<ffffffff800027aa>] do_one_initcall+0x36/0x218
[  484.636363] [<ffffffff81001452>] kernel_init_freeable+0x22c/0x296
[  484.642502] [<ffffffff80fded84>] kernel_init+0x26/0x116
[  484.647779] [<ffffffff80fe7816>] ret_from_fork+0xe/0x18
```


## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

Failed
