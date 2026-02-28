# ArkUI_NativeDialogAPI_2

```
typedef struct {...} ArkUI_NativeDialogAPI_2
```

## 概述

支持设备PhonePC/2in1TabletTVWearable

ArkUI提供的Native侧自定义弹窗接口集合。

**起始版本：** 15

**相关模块：** [ArkUI_NativeModule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule)

**所在头文件：** [native_dialog.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-dialog-h)

## 汇总

支持设备PhonePC/2in1TabletTVWearable 

### 成员变量

 支持设备PhonePC/2in1TabletTVWearable展开

| 名称 | 描述 |
| --- | --- |
| ArkUI_NativeDialogAPI_1 nativeDialogAPI1 | ArkUI提供的Native侧自定义弹窗接口集合，范围是 ArkUI_NativeDialogAPI_1 。 起始版本： 15 |

### 成员函数

 支持设备PhonePC/2in1TabletTVWearable展开

| 名称 | 描述 |
| --- | --- |
| int32_t (*setKeyboardAvoidDistance)(ArkUI_NativeDialogHandle handle, float distance, ArkUI_LengthMetricUnit unit) | 弹窗避让键盘后，和键盘之间距离。 |
| int32_t (*setLevelMode)(ArkUI_NativeDialogHandle handle, ArkUI_LevelMode levelMode) | 设置弹窗的显示层级。 |
| int32_t (*setLevelUniqueId)(ArkUI_NativeDialogHandle handle, int32_t uniqueId) | 设置弹窗显示层级页面下的节点id。 |
| int32_t (*setImmersiveMode)(ArkUI_NativeDialogHandle handle, ArkUI_ImmersiveMode immersiveMode) | 设置嵌入式弹窗蒙层的显示区域。 |

## 成员函数说明

支持设备PhonePC/2in1TabletTVWearable 

### setKeyboardAvoidDistance()

支持设备PhonePC/2in1TabletTVWearable

```
int32_t (*setKeyboardAvoidDistance)(ArkUI_NativeDialogHandle handle, float distance, ArkUI_LengthMetricUnit unit)
```

**描述：**

弹窗避让键盘后，和键盘之间距离。

 说明 

setKeyboardAvoidDistance方法需要在调用[show](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativedialogapi-1#show)方法之前调用。

**起始版本：** 15

**参数：**

 展开

| 参数项 | 描述 |
| --- | --- |
| ArkUI_NativeDialogHandle handle | 指向自定义弹窗控制器的指针。 |
| float distance | 避让键盘的距离，单位为vp。 |
| ArkUI_LengthMetricUnit unit | 避让距离的单位，参数类型 ArkUI_LengthMetricUnit 。 |

**返回：**

 展开

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。 ARKUI_ERROR_CODE_NO_ERROR 成功。 ARKUI_ERROR_CODE_CAPI_INIT_ERROR 接口初始化错误。 ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

### setLevelMode()

支持设备PhonePC/2in1TabletTVWearable

```
int32_t (*setLevelMode)(ArkUI_NativeDialogHandle handle, ArkUI_LevelMode levelMode)
```

**描述：**

设置弹窗的显示层级。

 说明 

setLevelMode方法需要在调用[show](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativedialogapi-1#show)方法之前调用。

**起始版本：** 15

**参数：**

 展开

| 参数项 | 描述 |
| --- | --- |
| ArkUI_NativeDialogHandle handle | 指向自定义弹窗控制器的指针。 |
| ArkUI_LevelMode levelMode | 显示层级的枚举值， 类型为 ArkUI_LevelMode 。 |

**返回：**

 展开

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。 ARKUI_ERROR_CODE_NO_ERROR 成功。 ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

### setLevelUniqueId()

支持设备PhonePC/2in1TabletTVWearable

```
int32_t (*setLevelUniqueId)(ArkUI_NativeDialogHandle handle, int32_t uniqueId)
```

**描述：**

设置弹窗显示层级页面下的节点id。

 说明 

setLevelUniqueId方法需要在调用[setLevelMode](/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativedialogapi-2#setlevelmode)方法之前调用。

**起始版本：** 15

**参数：**

 展开

| 参数项 | 描述 |
| --- | --- |
| ArkUI_NativeDialogHandle handle | 指向自定义弹窗控制器的指针。 |
| int32_t uniqueId | 指定节点id，会查找该节点所在页面，并将弹窗显示在该页面下。 |

**返回：**

 展开

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。 ARKUI_ERROR_CODE_NO_ERROR 成功。 ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |

### setImmersiveMode()

支持设备PhonePC/2in1TabletTVWearable

```
int32_t (*setImmersiveMode)(ArkUI_NativeDialogHandle handle, ArkUI_ImmersiveMode immersiveMode)
```

**描述：**

设置嵌入式弹窗蒙层的显示区域。

 说明 

setImmersiveMode方法需要在调用[show](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativedialogapi-1#show)方法之前调用。

**起始版本：** 15

**参数：**

 展开

| 参数项 | 描述 |
| --- | --- |
| ArkUI_NativeDialogHandle handle | 指向自定义弹窗控制器的指针。 |
| ArkUI_ImmersiveMode immersiveMode | 显示区域类型的枚举值， 类型为 ArkUI_ImmersiveMode 。 |

**返回：**

 展开

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。 ARKUI_ERROR_CODE_NO_ERROR 成功。 ARKUI_ERROR_CODE_PARAM_INVALID 函数参数异常。 |