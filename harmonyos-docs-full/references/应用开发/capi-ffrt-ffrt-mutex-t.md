# ffrt_mutex_t

```
typedef struct {...} ffrt_mutex_t
```

## 概述

支持设备PhonePC/2in1TabletTVWearable

FFRT互斥锁结构。

**起始版本：** 10

**相关模块：** [FFRT](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ffrt)

**所在头文件：** [type_def.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-type-def-h)

## 汇总

支持设备PhonePC/2in1TabletTVWearable 

### 成员变量

 支持设备PhonePC/2in1TabletTVWearable展开

| 名称 | 描述 |
| --- | --- |
| uint32_t storage[(ffrt_mutex_storage_size + sizeof(uint32_t) - 1) / sizeof(uint32_t)] | FFRT互斥锁所占空间 |