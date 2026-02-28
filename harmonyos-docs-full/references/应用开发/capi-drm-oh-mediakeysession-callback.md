# OH_MediaKeySession_Callback

```
typedef struct OH_MediaKeySession_Callback {...} OH_MediaKeySession_Callback
```

## 概述

支持设备PhonePC/2in1TabletWearable

OH_MediaKeySession_Callback结构体，用于监听密钥过期、密钥更改等事件，返回媒体密钥会话实例，适用多个媒体密钥会话解密场景。

**起始版本：** 12

**相关模块：** [Drm](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drm)

**所在头文件：** [native_mediakeysession.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-mediakeysession-h)

## 汇总

支持设备PhonePC/2in1TabletWearable 

### 成员变量

 支持设备PhonePC/2in1TabletWearable展开

| 名称 | 描述 |
| --- | --- |
| OH_MediaKeySession_EventCallback eventCallback | 正常事件回调，如密钥过期等。 |
| OH_MediaKeySession_KeyChangeCallback keyChangeCallback | 密钥更改事件的密钥更改回调。 |