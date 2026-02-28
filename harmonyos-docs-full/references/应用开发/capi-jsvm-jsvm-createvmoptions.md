# JSVM_CreateVMOptions

```
typedef struct {...} JSVM_CreateVMOptions
```

## 概述

支持设备PhonePC/2in1TabletWearable

创建JavaScript虚拟机的选项。

**起始版本：** 11

**相关模块：** [JSVM](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm)

**所在头文件：** [jsvm_types.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-types-h)

## 汇总

支持设备PhonePC/2in1TabletWearable 

### 成员变量

 支持设备PhonePC/2in1TabletWearable展开

| 名称 | 描述 |
| --- | --- |
| size_t maxOldGenerationSize | 老年代内存大小上限。 |
| size_t maxYoungGenerationSize | 年轻代内存大小上限。 |
| size_t initialOldGenerationSize | 老年代内存大小初始值。 |
| size_t initialYoungGenerationSize | 年轻代内存大小初始值。 |
| const char* snapshotBlobData | 启动快照数据。 |
| size_t snapshotBlobSize | 启动快照数据的大小。 |
| bool isForSnapshotting | 虚拟机是否用于创建快照，为true，则虚拟机用于创建快照，为false，则虚拟机不用于创建快照。 |