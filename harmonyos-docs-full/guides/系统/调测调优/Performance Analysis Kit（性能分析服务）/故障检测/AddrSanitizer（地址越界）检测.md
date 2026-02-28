## 简介

地址越界问题是指访问了不合法的地址，导致程序运行出现异常，通常表现为应用崩溃（Crash），其故障原因为释放后使用（use after free）、重复释放（double-free）、栈溢出（stack-overflow）、堆溢出（heap-overflow）等。由于应用崩溃日志信息有限且非崩溃第一现场，地址越界问题定位较为困难，一般依赖ASan、HWASan、GWP-ASan等检测工具以获取更多内存操作信息。从API13开始推荐[使用HWASan检测工具](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-stability-hwasan-detection)进行地址越界问题的分析。

## 常见越界类型与影响

常见地址越界类型和影响可参看[地址越界经典问题类型](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-stability-address-sanitizer-catagory)。

## 地址越界检测原理

检测原理和使用方法可参看[地址越界类问题检测](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-stability-ram-detection)。

## 日志获取方式

地址越界日志和进程崩溃日志一致，都是由Faultlogger模块进行管理，可通过以下方式获取：

**方式一：通过DevEco Studio获取日志**

DevEco Studio会收集设备/data/log/faultlog/faultlogger/路径下的进程崩溃故障日志到FaultLog下，根据进程名和故障和时间分类显示。获取日志的方法参见：[DevEco Studio使用指南-FaultLog](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-fault-log)。

**方式二：通过HiAppEvent接口订阅**

HiAppEvent给开发者提供了故障订阅接口，详见[HiAppEvent介绍](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-intro)。参考[订阅地址越界事件（ArkTS）](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-address-sanitizer-events-arkts)或[订阅地址越界事件（C/C++）](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-address-sanitizer-events-ndk)完成地址越界事件订阅，并通过事件的[external_log](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-address-sanitizer-events#params字段说明)字段读取故障日志文件内容。

**方式三：通过hdc获取日志，需打开开发者选项**

在运行态，日志默认都落盘至 /data/log/faultlog/faultlogger 下。在开发者选项打开的情况下，开发者可以通过hdc file recv /data/log/faultlog/faultlogger D:\命令导出故障日志到本地，故障日志文件名格式为[检测器类型]-[bundleName]-[uid]-[happenedTime].log。

## 日志规格

### ASan日志规格

ASan日志规格如下，标题头会展示设备信息，故障发生时间，故障进程和故障原因等。日志详细描述了越界访问的地址（0x007fffd59768）、访问大小（WRITE of size 4）、发生的线程和进程信息。通过调用栈，展现了导致此次越界的函数调用路径，列出各个调用层的地址及对应的模块和偏移，帮助开发者快速定位代码位置。日志还提供影子内存（Shadow bytes）跟踪内存状态，帮助确认访问是否合法。同时，日志列出了进程的内存空间映射，帮助分析越界地址所处的具体内存区域。

以下为具体示例：

 收起自动换行深色代码主题复制

```
Device info:XXX <- 设备信息 Build info:XXX-XXXX x.x.x.xx(xxxxxxx) <- 版本信息 Fingerprint:77cdc69cef714391a08c7cb1ceec8b8f9b02900fc6588e4231c2f8750b2bf330 <- 特征信息 Timestamp:xxxx-xx-xx xx:xx:xx.xxx <- 时间戳 Module name:com.example.sampleapplication <- 模块名 Version:1.0.0 <- 版本号 Pid:62642 <- 进程号 Uid:20020185 <- 用户ID Reason:stack-buffer-overflow <- 触发原因 ==appspawn==11766==AddressSanitizer: WARNING: unexpected format specifier in printf interceptor: %{ (reported once per process) ================================================================= ==appspawn==11766==ERROR: AddressSanitizer: stack-buffer-overflow on address 0x007fffd59768 at pc 0x007c7e718f54 bp 0x007fffd59710 sp 0x007fffd59708 <- 问题概述 WRITE of size 4 at 0x007fffd59768 thread T0 (e.myapplication) <- 越界大小 #0 0x7c7e718f50  (/data/storage/el1/bundle/libs/arm64/libentry.so+0x58f50) (BuildId: 5e1d4fe4b589921373e51615051105e455462c5f) <- 调用栈信息 #1 0x7b5710235c  (/system/lib64/platformsdk/libace_napi.z.so+0x4235c) (BuildId: e6ee1d59b23d2b0d1e746549da572967) #2 0x7b74ee79a4  (/system/lib64/module/arkcompiler/stub.an+0x4f89a4) #3 0x7b749fa8c0  (/system/lib64/module/arkcompiler/stub.an+0xb8c0) Address 0x007fffd59768 is located in stack of thread T0 (e.myapplication) at offset 72 in frame #0 0x7c7e718de4  (/data/storage/el1/bundle/libs/arm64/libentry.so+0x58de4) (BuildId: 5e1d4fe4b589921373e51615051105e455462c5f) This frame has 1 object(s): [32, 72) 'a' (line 66) <== Memory access at offset 72 overflows this variable HINT: this may be a false positive if your program uses some custom stack unwind mechanism, swapcontext or vfork (longjmp and C++ exceptions *are* supported) SUMMARY: AddressSanitizer: stack-buffer-overflow (/data/storage/el1/bundle/libs/arm64/libentry.so+0x58f50) (BuildId: 5e1d4fe4b589921373e51615051105e455462c5f) Shadow bytes around the buggy address:  <-影子内存信息 0x001ffffab290: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 0x001ffffab2a0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 0x001ffffab2b0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 0x001ffffab2c0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 0x001ffffab2d0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 =>0x001ffffab2e0: 00 00 00 00 f1 f1 f1 f1 00 00 00 00 00[f3]f3 f3 0x001ffffab2f0: f3 f3 f3 f3 00 00 00 00 00 00 00 00 00 00 00 00 0x001ffffab300: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 0x001ffffab310: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 0x001ffffab320: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 0x001ffffab330: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 Shadow byte legend (one shadow byte represents 8 application bytes): Addressable:           00 Partially addressable: 01 02 03 04 05 06 07 Heap left redzone:       fa Freed heap region:       fd Stack left redzone:      f1 Stack mid redzone:       f2 Stack right redzone:     f3 Stack after return:      f5 Stack use after scope:   f8 Global redzone:          f9 Global init order:       f6 Poisoned by user:        f7 Container overflow:      fc Array cookie:            ac Intra object redzone:    bb ASan internal:           fe Left alloca redzone:     ca Right alloca redzone:    cb ==appspawn==11766==ABORTING ==appspawn==11766==Process memory map follows: <- 故障时进程的内存空间 0x000ffffff000-0x001200000000 [anon:low shadow] 0x001200000000-0x001400000000 [anon:shadow gap] 0x001400000000-0x001f6ccb1000 [anon:high shadow] 0x001f6ccb1000-0x001f6cd28000 0x001f6cd28000-0x001f6e87c000 [anon:high shadow] 0x001f6e87c000-0x001f6e89c000 0x001f6e89c000-0x001f6e89d000 [anon:high shadow]
```

### HWASan日志规格

HWASan日志在格式上与ASan相近，也会在标题中展示设备信息、故障发生时间、故障进程及触发原因等关键信息。日志会详细记录越界访问的地址（如0x0002013c0100）和访问大小（如WRITE of size 4）。同时会记录发生时的线程和进程信息。完整的调用栈会展示触发越界的函数执行路径，列出各层地址、所属模块及偏移，便于开发者快速定位代码位置。不同于ASan的是，HWASan还会输出指针与内存块的标签（tags），并通过对比标签来辅助判断是否存在非法访问。

 收起自动换行深色代码主题复制

```
```

### MemDebug日志规格

MemDebug采用隔离区加投毒填充的机制，并复用HWASan的Tag校验的检测工具，对于Double Free类问题，其日志规格和HWASan一致。

 收起自动换行深色代码主题复制

```
```

对于Use-After-Free（Write）类问题，日志在问题概述部分会有所不同。示例输出如下：

 收起自动换行深色代码主题复制

```
ptrBeg was re-written after free 0x000100946540[1], 0x000100946548 5555555500000009:5555555555555555
```

其中，0x000100946540问题内存块起始地址，[1]为检测出问题的内存基于起始地址的8字节偏移数，0x000100946548为实际被修改的地址，5555555500000009:5555555555555555表示内存中的内容被修改后的实际值和预期值的对比。在该信息之后，日志还会输出对应内存块的释放堆栈和分配堆栈，调用栈的格式与HWASan日志一致，此处不再赘述。

### GWP-ASan日志规格

GWP-ASan的日志格式较为简洁，以下示例为典型的Use-After-Free问题日志，包含内存块的分配、释放及违规访问的调用栈信息。

 收起自动换行深色代码主题复制

```
Device info:XXX <- 设备信息 Build info:XXX-XXXX x.x.x.xx(xxxxxxx) <- 版本信息 Fingerprint:c41391f9c18acc1121ea519ffdba5698bfb5342ae7125e20ebf2865e31249f1a<- 特征信息 Timestamp:xxxx-xx-xx xx:xx:xx.xxx <- 时间戳 Module name:com.example.sampleapplication <- 模块名 Version:1.0.0 <- 版本号 Pid:13305<- 进程号 Uid:20020181 <- 用户ID Reason:GWP-ASAN <- Reason固定为GWP-ASAN *** GWP-ASan detected a memory error *** Use After Free at 0x5b46ddaff0 (0 bytes into a 16-byte allocation at 0x5b46ddaff0) by thread 13305 here: <- 问题概述，描述了一个UAF问题 #0 0x5c474f049c (/data/storage/xxxxxx.so+0x3049c) <- 调用栈信息 #1 0x5c474fa8c0 (/data/storage/xxxxxx.so+0x3a8c0) #2 0x5c474fa870 (/data/storage/xxxxxx.so+0x3a870) #3 0x5c474fa834 (/data/storage/xxxxxx.so+0x3a834) #4 0x5c474fa7d4 (/data/storage/xxxxxx.so+0x3a7d4) #5 0x5c474fa4a0 (/data/storage/xxxxxx.so+0x3a4a0) #6 0x5b2d444c04 (/system/lib64/platformsdk/libace_napi.z.so+0x44c04) #7 0x5b401d484c #8 0x5b3fc11d7c #9 0xfffffffffffffffe 0x5b46ddaff0 was deallocated by thread 13305 here: <- 问题概述，此处是释放的栈 #0 0x5aa0c0be2c (/lib/ld-musl-aarch64.so.1+0x13de2c) <- 调用栈信息 #1 0x5aa0c0b97c (/lib/ld-musl-aarch64.so.1+0x13d97c) #2 0x5c474f0494 (/data/storage/xxxxxx.so+0x30494) #3 0x5c474fa8c0 (/data/storage/xxxxxx.so+0x3a8c0) #4 0x5c474fa870 (/data/storage/xxxxxx.so+0x3a870) #5 0x5c474fa834 (/data/storage/xxxxxx.so+0x3a834) #6 0x5c474fa7d4 (/data/storage/xxxxxx.so+0x3a7d4) #7 0x5c474fa4a0 (/data/storage/xxxxxx.so+0x3a4a0) #8 0x5b2d444c04 (/system/lib64/xxxxxx.so+0x44c04) #9 0x5b401d484c #10 0x5b3fc11d7c #11 0xfffffffffffffffe 0x5b46ddaff0 was allocated by thread 13305 here: <- 问题概述，此处是申请的栈 #0 0x5aa0c0be2c (/lib/ld-musl-aarch64.so.1+0x13de2c) <- 调用栈信息 #1 0x5aa0c0b77c (/lib/ld-musl-aarch64.so.1+0x13d77c) #2 0x5aa0c22e5c (/lib/ld-musl-aarch64.so.1+0x154e5c) #3 0x5c474f047c (/data/storage/xxxxxx.so+0x3047c) #4 0x5c474fa8c0 (/data/storage/xxxxxx.so+0x3a8c0) #5 0x5c474fa870 (/data/storage/xxxxxx.so+0x3a870) #6 0x5c474fa834 (/data/storage/xxxxxx.so+0x3a834) #7 0x5c474fa7d4 (/data/storage/xxxxxx.so+0x3a7d4) #8 0x5c474fa4a0 (/data/storage/xxxxxx.so+0x3a4a0) #9 0x5b2d444c04 (/system/lib64/xxxxxx.so+0x44c04) #10 0x5b401d484c #11 0x5b3fc11d7c #12 0xfffffffffffffffe * End GWP-ASan report *
```