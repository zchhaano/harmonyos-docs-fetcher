# DRM_MediaKeySystemDescription

```
typedef struct DRM_MediaKeySystemDescription {...} DRM_MediaKeySystemDescription
```

## 概述

支持设备PhonePC/2in1TabletWearable

DRM解决方案名称及其UUID的列表。

**起始版本：** 12

**相关模块：** [Drm](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drm)

**所在头文件：** [native_drm_common.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-drm-common-h)

## 汇总

支持设备PhonePC/2in1TabletWearable 

### 成员变量

 支持设备PhonePC/2in1TabletWearable展开

| 名称 | 描述 |
| --- | --- |
| char name[MAX_MEDIA_KEY_SYSTEM_NAME_LEN] | DRM插件的名称。 |
| uint8_t uuid[DRM_UUID_LEN] | UUID。 |