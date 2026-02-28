# ArkUI_NativeGestureAPI_2

收起自动换行深色代码主题复制

```
typedef struct { ...} ArkUI_NativeGestureAPI_2
```

## 概述

支持设备PhonePC/2in1TabletTVWearable

定义手势模块接口集合。

**起始版本：** 18

**相关模块：** [ArkUI_NativeModule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule)

**所在头文件：** [native_gesture.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-gesture-h)

## 汇总

支持设备PhonePC/2in1TabletTVWearable 

### 成员变量

 支持设备PhonePC/2in1TabletTVWearable展开

| 名称 | 描述 |
| --- | --- |
| ArkUI_NativeGestureAPI_1 * gestureApi1 | 指向ArkUI_NativeGestureAPI_1结构体的指针。 |

### 成员函数

 支持设备PhonePC/2in1TabletTVWearable展开

| 名称 | 描述 |
| --- | --- |
| int32_t (*setGestureInterrupterToNode)(ArkUI_NodeHandle node, void* userData,ArkUI_GestureInterruptResult (*interrupter)(ArkUI_GestureInterruptInfo* info)) | 设置手势中断事件的回调函数。 |

## 成员函数说明

支持设备PhonePC/2in1TabletTVWearable 

### setGestureInterrupterToNode()

支持设备PhonePC/2in1TabletTVWearable收起自动换行深色代码主题复制

```
int32_t (*setGestureInterrupterToNode)(ArkUI_NodeHandle node, void * userData, ArkUI_GestureInterruptResult (*interrupter)(ArkUI_GestureInterruptInfo* info))
```

**描述：**

设置手势中断事件的回调函数。

**参数：**

 展开

| 参数项 | 描述 |
| --- | --- |
| ArkUI_NodeHandle node | 需要被设置手势打断回调的ArkUI节点指针。 |
| void* userData | 用户自定义数据。 |
| ArkUI_GestureInterruptResult (*interrupter)( ArkUI_GestureInterruptInfo * info) | 打断回调，info返回手势打断数据。interrupter返回GESTURE_INTERRUPT_RESULT_CONTINUE，手势正常进行；返回GESTURE_INTERRUPT_RESULT_REJECT，手势打断。设置此参数为nullptr时将取消注册回调函数。 |

**返回：**

 展开

| 类型 | 说明 |
| --- | --- |
| int32_t | 0 - 成功。 401 - 参数错误。 |