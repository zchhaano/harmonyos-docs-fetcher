# DRM_MediaKeySystemInfo

```
typedef struct DRM_MediaKeySystemInfo {...} DRM_MediaKeySystemInfo
```

## 概述

支持设备PhonePC/2in1TabletWearable

加密媒体内容的DRM信息。

**起始版本：** 11

**相关模块：** [Drm](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drm)

**所在头文件：** [native_drm_common.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-drm-common-h)

## 汇总

支持设备PhonePC/2in1TabletWearable 

### 成员变量

 支持设备PhonePC/2in1TabletWearable展开

| 名称 | 描述 |
| --- | --- |
| uint32_t psshCount | PSSH计数。 |
| DRM_PsshInfo psshInfo[MAX_PSSH_INFO_COUNT] | PSSH信息。 |