# OH_AudioBuffer

```
typedef struct OH_AudioBuffer {...} OH_AudioBuffer
```

## 概述

支持设备PhonePC/2in1TabletTV

定义了音频数据的大小、类型、时间戳等配置信息。

**起始版本：** 10

**相关模块：** [AVScreenCapture](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avscreencapture)

**所在头文件：** [native_avscreen_capture_base.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-avscreen-capture-base-h)

## 汇总

支持设备PhonePC/2in1TabletTV 

### 成员变量

 支持设备PhonePC/2in1TabletTV展开

| 名称 | 描述 |
| --- | --- |
| uint8_t* buf | 音频buffer内存。 |
| int32_t size | 音频buffer内存大小。 |
| int64_t timestamp | 音频buffer时间戳。 |
| OH_AudioCaptureSourceType type | 音频录制源类型。 |