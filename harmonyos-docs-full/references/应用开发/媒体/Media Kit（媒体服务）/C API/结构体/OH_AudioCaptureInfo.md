# OH_AudioCaptureInfo

```
typedef struct OH_AudioCaptureInfo {...} OH_AudioCaptureInfo
```

## 概述

支持设备PhonePC/2in1TabletTV

音频采样信息。

当audioSampleRate和audioChannels同时为0时，忽略该类型音频相关参数，不录制该类型音频数据。

**起始版本：** 10

**相关模块：** [AVScreenCapture](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avscreencapture)

**所在头文件：** [native_avscreen_capture_base.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-avscreen-capture-base-h)

## 汇总

支持设备PhonePC/2in1TabletTV 

### 成员变量

 支持设备PhonePC/2in1TabletTV展开

| 名称 | 描述 |
| --- | --- |
| int32_t audioSampleRate | 音频采样率，支持列表请查阅Audio Kit的 AudioSamplingRate 。 |
| int32_t audioChannels | 音频声道数。 |
| OH_AudioCaptureSourceType audioSource | 音频源。 |