# DRM_PsshInfo

```
typedef struct DRM_PsshInfo {...} DRM_PsshInfo
```

## 概述

支持设备PhonePC/2in1TabletWearable

DRM内容保护系统专用头（Protection System Specific Header）信息。

**起始版本：** 11

**相关模块：** [Drm](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drm)

**所在头文件：** [native_drm_common.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-drm-common-h)

## 汇总

支持设备PhonePC/2in1TabletWearable 

### 成员变量

 支持设备PhonePC/2in1TabletWearable展开

| 名称 | 描述 |
| --- | --- |
| uint8_t uuid[DRM_UUID_LEN] | UUID的PSSH信息。 |
| int32_t dataLen | PSSH数据长度。 |
| uint8_t data[MAX_PSSH_DATA_LEN] | PSSH数据。 |