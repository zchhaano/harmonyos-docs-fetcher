# Rdb_DistributedConfig

```
typedef struct Rdb_DistributedConfig {...} Rdb_DistributedConfig
```

## 概述

支持设备PhonePC/2in1TabletTVWearable

记录表的分布式配置信息。

**起始版本：** 11

**相关模块：** [RDB](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb)

**所在头文件：** [relational_store.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-relational-store-h)

## 汇总

支持设备PhonePC/2in1TabletTVWearable 

### 成员变量

 支持设备PhonePC/2in1TabletTVWearable展开

| 名称 | 描述 |
| --- | --- |
| int version | 用于唯一标识Rdb_DistributedConfig结构的版本。 |
| bool isAutoSync | 表示该表是否支持自动同步。true表示该表支持自动同步和手动同步，false表示该表只支持手动同步，不支持自动同步。 |