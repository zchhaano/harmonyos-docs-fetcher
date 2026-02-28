# ArkUI_ExpectedFrameRateRange

```
typedef struct {...} ArkUI_ExpectedFrameRateRange
```

## 概述

支持设备PhonePC/2in1TabletTVWearable

设置动画的期望帧率。

**起始版本：** 12

**相关模块：** [ArkUI_NativeModule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule)

**所在头文件：** [native_animate.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-animate-h)

## 汇总

支持设备PhonePC/2in1TabletTVWearable 

### 成员变量

 支持设备PhonePC/2in1TabletTVWearable展开

| 名称 | 描述 |
| --- | --- |
| uint32_t min | 期望的最小帧率，单位为帧/秒（fps）。 |
| uint32_t max | 期望的最大帧率，单位为帧/秒（fps）。 |
| uint32_t expected | 期望的最优帧率，单位为帧/秒（fps）。 |