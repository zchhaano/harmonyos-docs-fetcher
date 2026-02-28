# DRM_Statistics

```
typedef struct DRM_Statistics {...} DRM_Statistics
```

## 概述

支持设备PhonePC/2in1TabletWearable

MediaKeySystem的度量信息。

**起始版本：** 11

**相关模块：** [Drm](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drm)

**所在头文件：** [native_drm_common.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-drm-common-h)

## 汇总

支持设备PhonePC/2in1TabletWearable 

### 成员变量

 支持设备PhonePC/2in1TabletWearable展开

| 名称 | 描述 |
| --- | --- |
| uint32_t statisticsCount | 度量计数。 |
| char statisticsName[MAX_STATISTICS_COUNT][MAX_STATISTICS_NAME_LEN] | 度量信息名称集合。 |
| char statisticsDescription[MAX_STATISTICS_COUNT][MAX_STATISTICS_BUFFER_LEN] | 度量信息描述集合。 |