# ArkUI_AnimateCompleteCallback

```
typedef struct {...} ArkUI_AnimateCompleteCallback
```

## 概述

支持设备PhonePC/2in1TabletTVWearable

动画播放结束回调类型。

**起始版本：** 12

**相关模块：** [ArkUI_NativeModule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule)

**所在头文件：** [native_animate.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-animate-h)

## 汇总

支持设备PhonePC/2in1TabletTVWearable 

### 成员变量

 支持设备PhonePC/2in1TabletTVWearable展开

| 名称 | 描述 |
| --- | --- |
| ArkUI_FinishCallbackType type | 在动画中定义结束回调的类型。 |
| void* userData | 用于动画结束回调，传递用户自定义数据。 |

### 成员函数

 支持设备PhonePC/2in1TabletTVWearable展开

| 名称 | 描述 |
| --- | --- |
| void (*callback)(void* userData) | 动画播放结束回调。 |

## 成员函数说明

支持设备PhonePC/2in1TabletTVWearable 

### callback()

支持设备PhonePC/2in1TabletTVWearable

```
void (*callback)(void* userData)
```

**描述：**

动画播放结束回调。