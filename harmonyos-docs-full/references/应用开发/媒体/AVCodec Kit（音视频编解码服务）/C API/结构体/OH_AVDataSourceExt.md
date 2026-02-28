# OH_AVDataSourceExt

收起自动换行深色代码主题复制

```
typedef struct OH_AVDataSourceExt { ...} OH_AVDataSourceExt
```

## 概述

支持设备PhonePC/2in1TabletTVWearable

用户自定义数据源，回调支持通过userData传递用户自定义数据。

**起始版本：** 20

**相关模块：** [CodecBase](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-codecbase)

**所在头文件：** [native_avcodec_base.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-avcodec-base-h)

## 汇总

支持设备PhonePC/2in1TabletTVWearable 

### 成员变量

 支持设备PhonePC/2in1TabletTVWearable展开

| 名称 | 描述 |
| --- | --- |
| int64_t size | 数据源的总大小。 |
| OH_AVDataSourceReadAtExt readAt | 数据源的数据回调。 |