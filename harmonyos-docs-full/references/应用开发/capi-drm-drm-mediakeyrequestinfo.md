# DRM_MediaKeyRequestInfo

收起自动换行深色代码主题复制

```
typedef struct DRM_MediaKeyRequestInfo { ...} DRM_MediaKeyRequestInfo
```

## 概述

支持设备PhonePC/2in1TabletWearable

媒体密钥请求信息。

**起始版本：** 11

**相关模块：** [Drm](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drm)

**所在头文件：** [native_drm_common.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-drm-common-h)

## 汇总

支持设备PhonePC/2in1TabletWearable 

### 成员变量

 支持设备PhonePC/2in1TabletWearable展开

| 名称 | 描述 |
| --- | --- |
| DRM_MediaKeyType type | 密钥类型。 |
| int32_t initDataLen | 初始数据长度。 |
| uint8_t initData[MAX_INIT_DATA_LEN] | base64解码后格式为PSSH的初始数据。 |
| char mimeType[MAX_MIMETYPE_LEN] | 媒体上下文的mime类型。 |
| uint32_t optionsCount | 选项数据计数。 |
| char optionName[MAX_MEDIA_KEY_REQUEST_OPTION_COUNT][MAX_MEDIA_KEY_REQUEST_OPTION_NAME_LEN] | 选项名称集合。 |
| char optionData[MAX_MEDIA_KEY_REQUEST_OPTION_COUNT][MAX_MEDIA_KEY_REQUEST_OPTION_DATA_LEN] | 选项数据集合。 |