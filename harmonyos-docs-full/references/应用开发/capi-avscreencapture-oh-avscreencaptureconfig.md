# OH_AVScreenCaptureConfig

```
typedef struct OH_AVScreenCaptureConfig {...} OH_AVScreenCaptureConfig
```

## 概述

支持设备PhonePC/2in1TabletTV

屏幕录制配置参数。

**起始版本：** 10

**相关模块：** [AVScreenCapture](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avscreencapture)

**所在头文件：** [native_avscreen_capture_base.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-avscreen-capture-base-h)

## 汇总

支持设备PhonePC/2in1TabletTV 

### 成员变量

 支持设备PhonePC/2in1TabletTV展开

| 名称 | 描述 |
| --- | --- |
| OH_CaptureMode captureMode | 屏幕录制的模式。 |
| OH_DataType dataType | 屏幕录制流的数据格式。 |
| OH_AudioInfo audioInfo | 音频录制参数。 |
| OH_VideoInfo videoInfo | 视频录制参数。 |
| OH_RecorderInfo recorderInfo | 录制文件参数，当数据格式为OH_CAPTURE_FILE时必须设置。 |