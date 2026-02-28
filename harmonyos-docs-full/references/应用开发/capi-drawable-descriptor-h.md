## 概述

 支持设备PhonePC/2in1TabletTVWearable

提供NativeDrawableDescriptor接口的类型定义。

**引用文件：** <arkui/drawable_descriptor.h>

**库：** libace_ndk.z.so

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**相关模块：** [ArkUI_NativeModule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule)

**相关示例：** [DrawableDescriptorSample](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkUISample/DrawableDescriptorSample)

## 汇总

 支持设备PhonePC/2in1TabletTVWearable  

### 结构体

 支持设备PhonePC/2in1TabletTVWearable 展开

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| ArkUI_DrawableDescriptor | ArkUI_DrawableDescriptor | 定义DrawableDescriptor对象。 |
| OH_PixelmapNative | - | 使用Image Kit定义的Native侧的OH_PixelmapNative对象。 |
| OH_PixelmapNative* | OH_PixelmapNativeHandle | 定义OH_PixelmapNative对象指针类型。 |
| ArkUI_Node | - | 定义ArkUI native组件实例对象。 起始版本： 22 |
| ArkUI_Node* | ArkUI_NodeHandle | 定义ArkUI native组件实例对象指针定义。 起始版本： 22 |
| ArkUI_DrawableDescriptor_AnimationController | ArkUI_DrawableDescriptor_AnimationController | 定义DrawableDescriptor动图控制器对象。 起始版本： 22 |

### 枚举

 支持设备PhonePC/2in1TabletTVWearable 展开

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| DrawableDescriptor_AnimationStatus | DrawableDescriptor_AnimationStatus | 定义DrawableDescriptor动图的播放状态。 |

### 函数

 支持设备PhonePC/2in1TabletTVWearable 展开

| 名称 | 描述 |
| --- | --- |
| ArkUI_DrawableDescriptor* OH_ArkUI_DrawableDescriptor_CreateFromPixelMap(OH_PixelmapNativeHandle pixelMap) | 使用PixelMap创建DrawableDescriptor对象。 |
| ArkUI_DrawableDescriptor* OH_ArkUI_DrawableDescriptor_CreateFromAnimatedPixelMap(OH_PixelmapNativeHandle* array, int32_t size) | 使用PixelMap图片数组创建DrawableDescriptor对象。 |
| void OH_ArkUI_DrawableDescriptor_Dispose(ArkUI_DrawableDescriptor* drawableDescriptor) | 销毁DrawableDescriptor对象指针。 |
| OH_PixelmapNativeHandle OH_ArkUI_DrawableDescriptor_GetStaticPixelMap(ArkUI_DrawableDescriptor* drawableDescriptor) | 获取PixelMap图片对象指针。 |
| OH_PixelmapNativeHandle* OH_ArkUI_DrawableDescriptor_GetAnimatedPixelMapArray(ArkUI_DrawableDescriptor* drawableDescriptor) | 获取用于播放动画的PixelMap图片数组数据。 |
| int32_t OH_ArkUI_DrawableDescriptor_GetAnimatedPixelMapArraySize(ArkUI_DrawableDescriptor* drawableDescriptor) | 获取用于播放动画的PixelMap图片数组数据。 |
| void OH_ArkUI_DrawableDescriptor_SetAnimationDuration(ArkUI_DrawableDescriptor* drawableDescriptor, int32_t duration) | 设置PixelMap图片数组播放总时长。 |
| int32_t OH_ArkUI_DrawableDescriptor_GetAnimationDuration(ArkUI_DrawableDescriptor* drawableDescriptor) | 获取PixelMap图片数组播放总时长。 |
| void OH_ArkUI_DrawableDescriptor_SetAnimationIteration(ArkUI_DrawableDescriptor* drawableDescriptor, int32_t iteration) | 设置PixelMap图片数组播放次数。 |
| int32_t OH_ArkUI_DrawableDescriptor_GetAnimationIteration(ArkUI_DrawableDescriptor* drawableDescriptor) | 获取PixelMap图片数组播放次数。 |
| int32_t OH_ArkUI_DrawableDescriptor_SetAnimationFrameDurations(ArkUI_DrawableDescriptor* drawableDescriptor, uint32_t* durations, size_t size) | 设置动图中的单帧播放时间。 |
| int32_t OH_ArkUI_DrawableDescriptor_GetAnimationFrameDurations(ArkUI_DrawableDescriptor* drawableDescriptor, uint32_t* durations, size_t* size) | 获取动图中的单帧播放时间。 |
| int32_t OH_ArkUI_DrawableDescriptor_SetAnimationAutoPlay(ArkUI_DrawableDescriptor* drawableDescriptor, uint32_t autoPlay) | 设置动图是否自动播放。 |
| int32_t OH_ArkUI_DrawableDescriptor_GetAnimationAutoPlay(ArkUI_DrawableDescriptor* drawableDescriptor, uint32_t* autoPlay) | 获取动图是否自动播放。 |
| int32_t OH_ArkUI_DrawableDescriptor_CreateAnimationController(ArkUI_DrawableDescriptor* drawableDescriptor, ArkUI_NodeHandle node, ArkUI_DrawableDescriptor_AnimationController** controller) | 创建动图控制器。 |
| void OH_ArkUI_DrawableDescriptor_DisposeAnimationController( ArkUI_DrawableDescriptor_AnimationController* controller) | 销毁动图控制器。 |
| int32_t OH_ArkUI_DrawableDescriptor_StartAnimation(ArkUI_DrawableDescriptor_AnimationController* controller) | 从首帧开始播放。 |
| int32_t OH_ArkUI_DrawableDescriptor_StopAnimation(ArkUI_DrawableDescriptor_AnimationController* controller) | 停止动图播放并回到首帧。 |
| int32_t OH_ArkUI_DrawableDescriptor_ResumeAnimation(ArkUI_DrawableDescriptor_AnimationController* controller) | 从当前帧恢复动图播放。 |
| int32_t OH_ArkUI_DrawableDescriptor_PauseAnimation(ArkUI_DrawableDescriptor_AnimationController* controller) | 暂停动图的播放，保持在当前帧。 |
| int32_t OH_ArkUI_DrawableDescriptor_GetAnimationStatus(ArkUI_DrawableDescriptor_AnimationController* controller, DrawableDescriptor_AnimationStatus* status) | 获取动图的播放状态。 |

## 枚举类型说明

 支持设备PhonePC/2in1TabletTVWearable  

### DrawableDescriptor_AnimationStatus

 支持设备PhonePC/2in1TabletTVWearable收起自动换行深色代码主题复制

```
enum DrawableDescriptor_AnimationStatus
```

**描述：**

定义DrawableDescriptor动图的播放状态。

**起始版本：** 22

  展开

| 枚举项 | 描述 |
| --- | --- |
| DRAWABLE_DESCRIPTOR_ANIMATION_STATUS_INITIAL = 0 | 动画初始状态。 |
| DRAWABLE_DESCRIPTOR_ANIMATION_STATUS_RUNNING = 1 | 动画处于播放状态。 |
| DRAWABLE_DESCRIPTOR_ANIMATION_STATUS_PAUSED = 2 | 动画处于暂停状态。 |
| DRAWABLE_DESCRIPTOR_ANIMATION_STATUS_STOPPED = 3 | 动画处于停止状态。 |

## 函数说明

 支持设备PhonePC/2in1TabletTVWearable  

### OH_ArkUI_DrawableDescriptor_CreateFromPixelMap()

 支持设备PhonePC/2in1TabletTVWearable收起自动换行深色代码主题复制

```
ArkUI_DrawableDescriptor* OH_ArkUI_DrawableDescriptor_CreateFromPixelMap (OH_PixelmapNativeHandle pixelMap)
```

**描述：**

使用[PixelMap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-pixelmap)创建DrawableDescriptor对象。

**起始版本：** 12

**参数：**

  展开

| 参数项 | 描述 |
| --- | --- |
| OH_PixelmapNativeHandle pixelMap | PixelMap对象指针。 |

**返回：**

  展开

| 类型 | 说明 |
| --- | --- |
| ArkUI_DrawableDescriptor * | 返回DrawableDescriptor对象指针。 |

### OH_ArkUI_DrawableDescriptor_CreateFromAnimatedPixelMap()

 支持设备PhonePC/2in1TabletTVWearable收起自动换行深色代码主题复制

```
ArkUI_DrawableDescriptor* OH_ArkUI_DrawableDescriptor_CreateFromAnimatedPixelMap (OH_PixelmapNativeHandle* array , int32_t size)
```

**描述：**

使用PixelMap图片数组创建DrawableDescriptor对象。

**起始版本：** 12

**参数：**

  展开

| 参数项 | 描述 |
| --- | --- |
| OH_PixelmapNativeHandle * array | PixelMap图片数组对象指针。 |
| int32_t size | PixelMap图片数组大小。 |

**返回：**

  展开

| 类型 | 说明 |
| --- | --- |
| ArkUI_DrawableDescriptor * | 返回DrawableDescriptor对象指针。 |

### OH_ArkUI_DrawableDescriptor_Dispose()

 支持设备PhonePC/2in1TabletTVWearable收起自动换行深色代码主题复制

```
void OH_ArkUI_DrawableDescriptor_Dispose (ArkUI_DrawableDescriptor* drawableDescriptor)
```

**描述：**

销毁DrawableDescriptor对象指针。

**起始版本：** 12

**参数：**

  展开

| 参数项 | 描述 |
| --- | --- |
| ArkUI_DrawableDescriptor * drawableDescriptor | DrawableDescriptor对象指针。 |

### OH_ArkUI_DrawableDescriptor_GetStaticPixelMap()

 支持设备PhonePC/2in1TabletTVWearable收起自动换行深色代码主题复制

```
OH_PixelmapNativeHandle OH_ArkUI_DrawableDescriptor_GetStaticPixelMap (ArkUI_DrawableDescriptor* drawableDescriptor)
```

**描述：**

获取PixelMap图片对象指针。

**起始版本：** 12

**参数：**

  展开

| 参数项 | 描述 |
| --- | --- |
| ArkUI_DrawableDescriptor * drawableDescriptor | DrawableDescriptor对象指针。 |

**返回：**

  展开

| 类型 | 说明 |
| --- | --- |
| OH_PixelmapNativeHandle | PixelMap对象指针。 |

### OH_ArkUI_DrawableDescriptor_GetAnimatedPixelMapArray()

 支持设备PhonePC/2in1TabletTVWearable收起自动换行深色代码主题复制

```
OH_PixelmapNativeHandle* OH_ArkUI_DrawableDescriptor_GetAnimatedPixelMapArray (ArkUI_DrawableDescriptor* drawableDescriptor)
```

**描述：**

获取用于播放动画的PixelMap图片数组数据。

**起始版本：** 12

**参数：**

  展开

| 参数项 | 描述 |
| --- | --- |
| ArkUI_DrawableDescriptor * drawableDescriptor | DrawableDescriptor对象指针。 |

**返回：**

  展开

| 类型 | 说明 |
| --- | --- |
| OH_PixelmapNativeHandle * | PixelMap图片数组指针。 |

### OH_ArkUI_DrawableDescriptor_GetAnimatedPixelMapArraySize()

 支持设备PhonePC/2in1TabletTVWearable收起自动换行深色代码主题复制

```
int32_t OH_ArkUI_DrawableDescriptor_GetAnimatedPixelMapArraySize (ArkUI_DrawableDescriptor* drawableDescriptor)
```

**描述：**

获取用于播放动画的PixelMap图片数组数据。

**起始版本：** 12

**参数：**

  展开

| 参数项 | 描述 |
| --- | --- |
| ArkUI_DrawableDescriptor * drawableDescriptor | DrawableDescriptor对象指针。 |

**返回：**

  展开

| 类型 | 说明 |
| --- | --- |
| int32_t | PixelMap图片数组大小。 |

### OH_ArkUI_DrawableDescriptor_SetAnimationDuration()

 支持设备PhonePC/2in1TabletTVWearable收起自动换行深色代码主题复制

```
void OH_ArkUI_DrawableDescriptor_SetAnimationDuration (ArkUI_DrawableDescriptor* drawableDescriptor, int32_t duration)
```

**描述：**

设置PixelMap图片数组播放总时长。

**起始版本：** 12

**参数：**

  展开

| 参数项 | 描述 |
| --- | --- |
| ArkUI_DrawableDescriptor * drawableDescriptor | DrawableDescriptor对象指针。 |
| int32_t duration | 播放总时长，单位毫秒。 |

### OH_ArkUI_DrawableDescriptor_GetAnimationDuration()

 支持设备PhonePC/2in1TabletTVWearable收起自动换行深色代码主题复制

```
int32_t OH_ArkUI_DrawableDescriptor_GetAnimationDuration (ArkUI_DrawableDescriptor* drawableDescriptor)
```

**描述：**

获取PixelMap图片数组播放总时长。

**起始版本：** 12

**参数：**

  展开

| 参数项 | 描述 |
| --- | --- |
| ArkUI_DrawableDescriptor * drawableDescriptor | DrawableDescriptor对象指针。 |

**返回：**

  展开

| 类型 | 说明 |
| --- | --- |
| int32_t | 播放总时长，单位毫秒。 |

### OH_ArkUI_DrawableDescriptor_SetAnimationIteration()

 支持设备PhonePC/2in1TabletTVWearable收起自动换行深色代码主题复制

```
void OH_ArkUI_DrawableDescriptor_SetAnimationIteration (ArkUI_DrawableDescriptor* drawableDescriptor, int32_t iteration)
```

**描述：**

设置PixelMap图片数组播放次数。

**起始版本：** 12

**参数：**

  展开

| 参数项 | 描述 |
| --- | --- |
| ArkUI_DrawableDescriptor * drawableDescriptor | DrawableDescriptor对象指针。 |
| int32_t iteration | 播放次数。 |

### OH_ArkUI_DrawableDescriptor_GetAnimationIteration()

 支持设备PhonePC/2in1TabletTVWearable收起自动换行深色代码主题复制

```
int32_t OH_ArkUI_DrawableDescriptor_GetAnimationIteration (ArkUI_DrawableDescriptor* drawableDescriptor)
```

**描述：**

获取PixelMap图片数组播放次数。

**起始版本：** 12

**参数：**

  展开

| 参数项 | 描述 |
| --- | --- |
| ArkUI_DrawableDescriptor * drawableDescriptor | DrawableDescriptor对象指针。 |

**返回：**

  展开

| 类型 | 说明 |
| --- | --- |
| int32_t | 播放次数。 |

### OH_ArkUI_DrawableDescriptor_SetAnimationFrameDurations()

 支持设备PhonePC/2in1TabletTVWearable收起自动换行深色代码主题复制

```
int32_t OH_ArkUI_DrawableDescriptor_SetAnimationFrameDurations (ArkUI_DrawableDescriptor* drawableDescriptor, uint32_t * durations, size_t size)
```

**描述：**

设置动图中的单帧播放时间。

**起始版本：** 22

**参数：**

  展开

| 参数项 | 描述 |
| --- | --- |
| ArkUI_DrawableDescriptor * drawableDescriptor | DrawableDescriptor对象指针。 |
| uint32_t* durations | 动图中的单帧播放时间数组，单位毫秒。 不设置则按照总时间播放。设置的优先级高于duration，即同时设置了 duration 和frameDurations时，duration不生效。 数组大小必须与PixelMap图片数组大小相同。 每帧播放时间取值范围：[0, +∞)。 |
| size_t size | 数组大小。 |

**返回：**

  展开

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。 ARKUI_ERROR_CODE_NO_ERROR 成功。 ARKUI_ERROR_CODE_PARAM_INVALID 输入参数错误。 |

### OH_ArkUI_DrawableDescriptor_GetAnimationFrameDurations()

 支持设备PhonePC/2in1TabletTVWearable收起自动换行深色代码主题复制

```
int32_t OH_ArkUI_DrawableDescriptor_GetAnimationFrameDurations (ArkUI_DrawableDescriptor* drawableDescriptor, uint32_t * durations, size_t * size)
```

**描述：**

获取动图中的单帧播放时间。

**起始版本：** 22

**参数：**

  展开

| 参数项 | 描述 |
| --- | --- |
| ArkUI_DrawableDescriptor * drawableDescriptor | DrawableDescriptor对象指针。 |
| uint32_t* durations | 动图中的单帧播放时间数组。 |
| size_t* size | 数组大小。 |

**返回：**

  展开

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。 ARKUI_ERROR_CODE_NO_ERROR 成功。 ARKUI_ERROR_CODE_PARAM_INVALID 输入参数错误。 |

### OH_ArkUI_DrawableDescriptor_SetAnimationAutoPlay()

 支持设备PhonePC/2in1TabletTVWearable收起自动换行深色代码主题复制

```
int32_t OH_ArkUI_DrawableDescriptor_SetAnimationAutoPlay (ArkUI_DrawableDescriptor* drawableDescriptor, uint32_t autoPlay)
```

**描述：**

设置动图是否自动播放。

**起始版本：** 22

**参数：**

  展开

| 参数项 | 描述 |
| --- | --- |
| ArkUI_DrawableDescriptor * drawableDescriptor | DrawableDescriptor对象指针。 |
| uint32_t autoPlay | 是否自动播放。 1表示自动播放，0表示不自动播放。 默认值为1。 |

**返回：**

  展开

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。 ARKUI_ERROR_CODE_NO_ERROR 成功。 ARKUI_ERROR_CODE_PARAM_INVALID 输入参数错误。 |

### OH_ArkUI_DrawableDescriptor_GetAnimationAutoPlay()

 支持设备PhonePC/2in1TabletTVWearable收起自动换行深色代码主题复制

```
int32_t OH_ArkUI_DrawableDescriptor_GetAnimationAutoPlay (ArkUI_DrawableDescriptor* drawableDescriptor, uint32_t * autoPlay)
```

**描述：**

获取动图是否自动播放。

**起始版本：** 22

**参数：**

  展开

| 参数项 | 描述 |
| --- | --- |
| ArkUI_DrawableDescriptor * drawableDescriptor | DrawableDescriptor对象指针。 |
| uint32_t* autoPlay | 是否自动播放。 |

**返回：**

  展开

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。 ARKUI_ERROR_CODE_NO_ERROR 成功。 ARKUI_ERROR_CODE_PARAM_INVALID 输入参数错误。 |

### OH_ArkUI_DrawableDescriptor_CreateAnimationController()

 支持设备PhonePC/2in1TabletTVWearable收起自动换行深色代码主题复制

```
int32_t OH_ArkUI_DrawableDescriptor_CreateAnimationController (ArkUI_DrawableDescriptor* drawableDescriptor, ArkUI_NodeHandle node, ArkUI_DrawableDescriptor_AnimationController** controller)
```

**描述：**

创建动图控制器。

**起始版本：** 22

**参数：**

  展开

| 参数项 | 描述 |
| --- | --- |
| ArkUI_DrawableDescriptor * drawableDescriptor | DrawableDescriptor对象指针。 |
| ArkUI_NodeHandle node | 组件节点指针。 |
| ArkUI_DrawableDescriptor_AnimationController ** controller | DrawableDescriptor动图控制器对象指针。 |

**返回：**

  展开

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。 ARKUI_ERROR_CODE_NO_ERROR 成功。 ARKUI_ERROR_CODE_PARAM_INVALID 输入参数错误。 |

### OH_ArkUI_DrawableDescriptor_DisposeAnimationController()

 支持设备PhonePC/2in1TabletTVWearable收起自动换行深色代码主题复制

```
void OH_ArkUI_DrawableDescriptor_DisposeAnimationController (ArkUI_DrawableDescriptor_AnimationController* controller)
```

**描述：**

销毁动图控制器。

**起始版本：** 22

**参数：**

  展开

| 参数项 | 描述 |
| --- | --- |
| ArkUI_DrawableDescriptor_AnimationController * controller | DrawableDescriptor动图控制器对象指针。 |

### OH_ArkUI_DrawableDescriptor_StartAnimation()

 支持设备PhonePC/2in1TabletTVWearable收起自动换行深色代码主题复制

```
int32_t OH_ArkUI_DrawableDescriptor_StartAnimation (ArkUI_DrawableDescriptor_AnimationController* controller) ;
```

**描述：**

从首帧开始播放。

**起始版本：** 22

**参数：**

  展开

| 参数项 | 描述 |
| --- | --- |
| ArkUI_DrawableDescriptor_AnimationController * controller | DrawableDescriptor动图控制器对象指针。 |

**返回：**

  展开

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。 ARKUI_ERROR_CODE_NO_ERROR 成功。 ARKUI_ERROR_CODE_PARAM_INVALID 输入参数错误。 |

### OH_ArkUI_DrawableDescriptor_StopAnimation()

 支持设备PhonePC/2in1TabletTVWearable收起自动换行深色代码主题复制

```
int32_t OH_ArkUI_DrawableDescriptor_StopAnimation (ArkUI_DrawableDescriptor_AnimationController* controller) ;
```

**描述：**

停止动图播放并回到首帧。

**起始版本：** 22

**参数：**

  展开

| 参数项 | 描述 |
| --- | --- |
| ArkUI_DrawableDescriptor_AnimationController * controller | DrawableDescriptor动图控制器对象指针。 |

**返回：**

  展开

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。 ARKUI_ERROR_CODE_NO_ERROR 成功。 ARKUI_ERROR_CODE_PARAM_INVALID 输入参数错误。 |

### OH_ArkUI_DrawableDescriptor_ResumeAnimation()

 支持设备PhonePC/2in1TabletTVWearable收起自动换行深色代码主题复制

```
int32_t OH_ArkUI_DrawableDescriptor_ResumeAnimation (ArkUI_DrawableDescriptor_AnimationController* controller) ;
```

**描述：**

从当前帧恢复动图播放。

**起始版本：** 22

**参数：**

  展开

| 参数项 | 描述 |
| --- | --- |
| ArkUI_DrawableDescriptor_AnimationController * controller | DrawableDescriptor动图控制器对象指针。 |

**返回：**

  展开

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。 ARKUI_ERROR_CODE_NO_ERROR 成功。 ARKUI_ERROR_CODE_PARAM_INVALID 输入参数错误。 |

### OH_ArkUI_DrawableDescriptor_PauseAnimation()

 支持设备PhonePC/2in1TabletTVWearable收起自动换行深色代码主题复制

```
int32_t OH_ArkUI_DrawableDescriptor_PauseAnimation (ArkUI_DrawableDescriptor_AnimationController* controller) ;
```

**描述：**

暂停动图的播放，保持在当前帧。

**起始版本：** 22

**参数：**

  展开

| 参数项 | 描述 |
| --- | --- |
| ArkUI_DrawableDescriptor_AnimationController * controller | DrawableDescriptor动图控制器对象指针。 |

**返回：**

  展开

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。 ARKUI_ERROR_CODE_NO_ERROR 成功。 ARKUI_ERROR_CODE_PARAM_INVALID 输入参数错误。 |

### OH_ArkUI_DrawableDescriptor_GetAnimationStatus()

 支持设备PhonePC/2in1TabletTVWearable收起自动换行深色代码主题复制

```
int32_t OH_ArkUI_DrawableDescriptor_GetAnimationStatus (ArkUI_DrawableDescriptor_AnimationController* controller, DrawableDescriptor_AnimationStatus* status) ;
```

**描述：**

获取动图的播放状态。

**起始版本：** 22

**参数：**

  展开

| 参数项 | 描述 |
| --- | --- |
| ArkUI_DrawableDescriptor_AnimationController * controller | DrawableDescriptor动图控制器对象指针。 |
| DrawableDescriptor_AnimationStatus * status | DrawableDescriptor动图的播放状态。 |

**返回：**

  展开

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码。 ARKUI_ERROR_CODE_NO_ERROR 成功。 ARKUI_ERROR_CODE_PARAM_INVALID 输入参数错误。 |