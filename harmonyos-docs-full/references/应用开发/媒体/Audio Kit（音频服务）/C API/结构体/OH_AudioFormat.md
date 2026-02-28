# OH_AudioFormat

收起自动换行深色代码主题复制

```
typedef struct { ...} OH_AudioFormat
```

## 概述

支持设备PhonePC/2in1Tablet

定义音频编创的音频流信息，用于描述基本音频格式。

**起始版本：** 22

**相关模块：** [OHAudioSuite](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohaudiosuite)

**所在头文件：** [native_audio_suite_base.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audio-suite-base-h)

## 汇总

支持设备PhonePC/2in1Tablet 

### 成员变量

 支持设备PhonePC/2in1Tablet展开

| 名称 | 描述 |
| --- | --- |
| OH_Audio_SampleRate samplingRate | 音频流采样率。 |
| OH_AudioChannelLayout channelLayout | 音频流声道布局，当前只支持CH_LAYOUT_MONO 和 CH_LAYOUT_STEREO。 |
| uint32_t channelCount | 音频流声道个数，当前只支持1声道和2声道。 |
| OH_Audio_EncodingType encodingType | 音频流编码类型。 |
| OH_Audio_SampleFormat sampleFormat | 音频流采样格式。 |