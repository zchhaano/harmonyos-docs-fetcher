# Rdb_ProgressDetails

收起自动换行深色代码主题复制

```
typedef struct Rdb_ProgressDetails { ...} Rdb_ProgressDetails
```

## 概述

支持设备PhonePC/2in1TabletTVWearable

描述数据库整体执行端云同步任务上传和下载的统计信息。

**起始版本：** 11

**相关模块：** [RDB](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb)

**所在头文件：** [relational_store.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-relational-store-h)

## 汇总

支持设备PhonePC/2in1TabletTVWearable 

### 成员变量

 支持设备PhonePC/2in1TabletTVWearable展开

| 名称 | 描述 |
| --- | --- |
| int version | 用于唯一标识OH_TableDetails结构的版本。 |
| int schedule | 表示端云同步过程。 |
| int code | 表示端云同步过程的状态。 |
| int32_t tableLength | 表示端云同步的表的数量。 |