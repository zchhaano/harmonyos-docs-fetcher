## 概述

支持设备PhonePC/2in1TabletTVWearable

媒体会话定义，可用于设置元数据、播放状态信息等操作。

**引用文件：** <multimedia/av_session/native_avsession.h>

**库：** libohavsession.so

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 13

**相关模块：** [OHAVSession](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohavsession)

## 汇总

支持设备PhonePC/2in1TabletTVWearable 

### 结构体

 支持设备PhonePC/2in1TabletTVWearable展开

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| AVSession_PlaybackPosition | AVSession_PlaybackPosition | 媒体播放位置的相关属性。 |
| OH_AVSession | OH_AVSession | 播控会话对象定义。可以用OH_AVSession_Create创建一个会话对象。 |

### 枚举

 支持设备PhonePC/2in1TabletTVWearable展开

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| AVSession_Type | AVSession_Type | 会话类型。 |
| AVSession_PlaybackState | AVSession_PlaybackState | 媒体播放状态的相关属性。 |
| AVSession_LoopMode | AVSession_LoopMode | 媒体播放循环模式。 |
| AVSession_ControlCommand | AVSession_ControlCommand | 播控命令。 |
| AVSessionCallback_Result | AVSessionCallback_Result | 回调执行的结果。 |

### 函数

 支持设备PhonePC/2in1TabletTVWearable展开

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| typedef AVSessionCallback_Result (*OH_AVSessionCallback_OnCommand)(OH_AVSession* session, AVSession_ControlCommand command, void* userData) | OH_AVSessionCallback_OnCommand | 通用的执行播控命令的回调。 |
| typedef AVSessionCallback_Result (*OH_AVSessionCallback_OnFastForward)(OH_AVSession* session, uint32_t seekTime, void* userData) | OH_AVSessionCallback_OnFastForward | 快进的回调。 |
| typedef AVSessionCallback_Result (*OH_AVSessionCallback_OnRewind)(OH_AVSession* session, uint32_t seekTime, void* userData) | OH_AVSessionCallback_OnRewind | 快退的回调。 |
| typedef AVSessionCallback_Result (*OH_AVSessionCallback_OnSeek)(OH_AVSession* session, uint64_t seekTime, void* userData) | OH_AVSessionCallback_OnSeek | 进度调节的回调。 |
| typedef AVSessionCallback_Result (*OH_AVSessionCallback_OnSetLoopMode)(OH_AVSession* session, AVSession_LoopMode curLoopMode, void* userData) | OH_AVSessionCallback_OnSetLoopMode | 设置循环模式的回调。 |
| typedef AVSessionCallback_Result (*OH_AVSessionCallback_OnToggleFavorite)(OH_AVSession* session, const char* assetId, void* userData) | OH_AVSessionCallback_OnToggleFavorite | 收藏的回调。 |
| AVSession_ErrCode OH_AVSession_Create(AVSession_Type sessionType, const char* sessionTag,const char* bundleName, const char* abilityName, OH_AVSession** avsession) | - | 创建会话对象。 |
| AVSession_ErrCode OH_AVSession_Destroy(OH_AVSession* avsession) | - | 销毁会话对象。 |
| AVSession_ErrCode OH_AVSession_Activate(OH_AVSession* avsession) | - | 激活会话。 |
| AVSession_ErrCode OH_AVSession_Deactivate(OH_AVSession* avsession) | - | 取消激活媒体会话。 |
| AVSession_ErrCode OH_AVSession_GetSessionType(OH_AVSession* avsession, AVSession_Type* sessionType) | - | 获取会话类型。 |
| AVSession_ErrCode OH_AVSession_GetSessionId(OH_AVSession* avsession, const char** sessionId) | - | 获取会话id。 |
| AVSession_ErrCode OH_AVSession_SetAVMetadata(OH_AVSession* avsession, OH_AVMetadata* avmetadata) | - | 设置媒体元数据。 |
| AVSession_ErrCode OH_AVSession_SetPlaybackState(OH_AVSession* avsession, AVSession_PlaybackState playbackState) | - | 设置播放状态。 |
| AVSession_ErrCode OH_AVSession_SetPlaybackPosition(OH_AVSession* avsession, AVSession_PlaybackPosition* playbackPosition) | - | 设置播放位置。 |
| AVSession_ErrCode OH_AVSession_SetFavorite(OH_AVSession* avsession, bool favorite) | - | 设置收藏状态。 |
| AVSession_ErrCode OH_AVSession_SetLoopMode(OH_AVSession* avsession, AVSession_LoopMode loopMode) | - | 设置循环模式。 |
| AVSession_ErrCode OH_AVSession_RegisterCommandCallback(OH_AVSession* avsession,AVSession_ControlCommand command, OH_AVSessionCallback_OnCommand callback, void* userData) | - | 注册通用播控的回调。 |
| AVSession_ErrCode OH_AVSession_UnregisterCommandCallback(OH_AVSession* avsession, AVSession_ControlCommand command, OH_AVSessionCallback_OnCommand callback) | - | 取消注册通用播控的回调。 |
| AVSession_ErrCode OH_AVSession_RegisterForwardCallback(OH_AVSession* avsession, OH_AVSessionCallback_OnFastForward callback, void* userData) | - | 注册快进的回调。 |
| AVSession_ErrCode OH_AVSession_UnregisterForwardCallback(OH_AVSession* avsession, OH_AVSessionCallback_OnFastForward callback) | - | 取消注册快进的回调。 |
| AVSession_ErrCode OH_AVSession_RegisterRewindCallback(OH_AVSession* avsession, OH_AVSessionCallback_OnRewind callback, void* userData) | - | 注册快退的回调。 |
| AVSession_ErrCode OH_AVSession_UnregisterRewindCallback(OH_AVSession* avsession, OH_AVSessionCallback_OnRewind callback) | - | 取消注册快退的回调。 |
| AVSession_ErrCode OH_AVSession_RegisterSeekCallback(OH_AVSession* avsession, OH_AVSessionCallback_OnSeek callback, void* userData) | - | 注册跳转的回调。 |
| AVSession_ErrCode OH_AVSession_UnregisterSeekCallback(OH_AVSession* avsession, OH_AVSessionCallback_OnSeek callback) | - | 取消注册跳转的回调。 |
| AVSession_ErrCode OH_AVSession_RegisterSetLoopModeCallback(OH_AVSession* avsession, OH_AVSessionCallback_OnSetLoopMode callback, void* userData) | - | 注册设置循环模式的回调。 |
| AVSession_ErrCode OH_AVSession_UnregisterSetLoopModeCallback(OH_AVSession* avsession, OH_AVSessionCallback_OnSetLoopMode callback) | - | 取消注册设置循环模式的回调。 |
| AVSession_ErrCode OH_AVSession_RegisterToggleFavoriteCallback(OH_AVSession* avsession, OH_AVSessionCallback_OnToggleFavorite callback, void* userData) | - | 设置收藏的回调。 |
| AVSession_ErrCode OH_AVSession_UnregisterToggleFavoriteCallback(OH_AVSession* avsession, OH_AVSessionCallback_OnToggleFavorite callback) | - | 取消设置收藏的回调。 |

## 枚举类型说明

支持设备PhonePC/2in1TabletTVWearable 

### AVSession_Type

支持设备PhonePC/2in1TabletTVWearable

```
enum AVSession_Type
```

**描述**

会话类型。

**起始版本：** 13

 展开

| 枚举项 | 描述 |
| --- | --- |
| SESSION_TYPE_AUDIO = 0 | 音频。 |
| SESSION_TYPE_VIDEO = 1 | 视频。 |
| SESSION_TYPE_VOICE_CALL = 2 | 音频通话。 |
| SESSION_TYPE_VIDEO_CALL = 3 | 视频通话。 |

### AVSession_PlaybackState

支持设备PhonePC/2in1TabletTVWearable

```
enum AVSession_PlaybackState
```

**描述**

媒体播放状态的相关属性。

**起始版本：** 13

 展开

| 枚举项 | 描述 |
| --- | --- |
| PLAYBACK_STATE_INITIAL = 0 | 初始状态。 |
| PLAYBACK_STATE_PREPARING = 1 | 准备状态。 |
| PLAYBACK_STATE_PLAYING = 2 | 正在播放。 |
| PLAYBACK_STATE_PAUSED = 3 | 暂停。 |
| PLAYBACK_STATE_FAST_FORWARDING = 4 | 快进。 |
| PLAYBACK_STATE_REWINDED = 5 | 快退。 |
| PLAYBACK_STATE_STOPPED = 6 | 停止。 |
| PLAYBACK_STATE_COMPLETED = 7 | 播放完成。 |
| PLAYBACK_STATE_RELEASED = 8 | 释放。 |
| PLAYBACK_STATE_ERROR = 9 | 错误。 |
| PLAYBACK_STATE_IDLE = 10 | 空闲。 |
| PLAYBACK_STATE_BUFFERING = 11 | 缓冲。 |
| PLAYBACK_STATE_MAX = 12 | 最大状态。（当state为12时，返回错误码401） |

### AVSession_LoopMode

支持设备PhonePC/2in1TabletTVWearable

```
enum AVSession_LoopMode
```

**描述**

媒体播放循环模式。

**起始版本：** 13

 展开

| 枚举项 | 描述 |
| --- | --- |
| LOOP_MODE_SEQUENCE = 0 | 顺序播放。 |
| LOOP_MODE_SINGLE = 1 | 单曲循环。 |
| LOOP_MODE_LIST = 2 | 表单循环。 |
| LOOP_MODE_SHUFFLE = 3 | 随机播放。 |
| LOOP_MODE_CUSTOM = 4 | 自定义播放。 |

### AVSession_ControlCommand

支持设备PhonePC/2in1TabletTVWearable

```
enum AVSession_ControlCommand
```

**描述**

播控命令。

**起始版本：** 13

 展开

| 枚举项 | 描述 |
| --- | --- |
| CONTROL_CMD_INVALID = -1 | 无效控制命令。 |
| CONTROL_CMD_PLAY = 0 | 播放命令。 |
| CONTROL_CMD_PAUSE = 1 | 暂停命令。 |
| CONTROL_CMD_STOP = 2 | 停止命令。 |
| CONTROL_CMD_PLAY_NEXT = 3 | 播放下一首命令。 |
| CONTROL_CMD_PLAY_PREVIOUS = 4 | 播放上一首命令。 |

### AVSessionCallback_Result

支持设备PhonePC/2in1TabletTVWearable

```
enum AVSessionCallback_Result
```

**描述**

回调执行的结果。

**起始版本：** 13

 展开

| 枚举项 | 描述 |
| --- | --- |
| AVSESSION_CALLBACK_RESULT_SUCCESS = 0 | 执行成功。 |
| AVSESSION_CALLBACK_RESULT_FAILURE = -1 | 执行失败。 |

## 函数说明

支持设备PhonePC/2in1TabletTVWearable 

### OH_AVSessionCallback_OnCommand()

支持设备PhonePC/2in1TabletTVWearable

```
typedef AVSessionCallback_Result (*OH_AVSessionCallback_OnCommand)(OH_AVSession* session,AVSession_ControlCommand command, void* userData)
```

**描述**

通用的执行播控命令的回调。

**起始版本：** 13

### OH_AVSessionCallback_OnFastForward()

支持设备PhonePC/2in1TabletTVWearable

```
typedef AVSessionCallback_Result (*OH_AVSessionCallback_OnFastForward)(OH_AVSession* session,uint32_t seekTime, void* userData)
```

**描述**

快进的回调。

**起始版本：** 13

### OH_AVSessionCallback_OnRewind()

支持设备PhonePC/2in1TabletTVWearable

```
typedef AVSessionCallback_Result (*OH_AVSessionCallback_OnRewind)(OH_AVSession* session,uint32_t seekTime, void* userData)
```

**描述**

快退的回调。

**起始版本：** 13

### OH_AVSessionCallback_OnSeek()

支持设备PhonePC/2in1TabletTVWearable

```
typedef AVSessionCallback_Result (*OH_AVSessionCallback_OnSeek)(OH_AVSession* session,uint64_t seekTime, void* userData)
```

**描述**

进度调节的回调。

**起始版本：** 13

### OH_AVSessionCallback_OnSetLoopMode()

支持设备PhonePC/2in1TabletTVWearable

```
typedef AVSessionCallback_Result (*OH_AVSessionCallback_OnSetLoopMode)(OH_AVSession* session,AVSession_LoopMode curLoopMode, void* userData)
```

**描述**

设置循环模式的回调。

**起始版本：** 13

### OH_AVSessionCallback_OnToggleFavorite()

支持设备PhonePC/2in1TabletTVWearable

```
typedef AVSessionCallback_Result (*OH_AVSessionCallback_OnToggleFavorite)(OH_AVSession* session,const char* assetId, void* userData)
```

**描述**

收藏的回调。

**起始版本：** 13

### OH_AVSession_Create()

支持设备PhonePC/2in1TabletTVWearable

```
AVSession_ErrCode OH_AVSession_Create(AVSession_Type sessionType, const char* sessionTag,const char* bundleName, const char* abilityName, OH_AVSession** avsession)
```

**描述**

创建会话对象。

**起始版本：** 13

**参数：**

 展开

| 参数项 | 描述 |
| --- | --- |
| AVSession_Type sessionType | 会话类型 AVSession_Type 。 |
| const char* sessionTag | 会话标签。 |
| const char* bundleName | 创建会话的包名。 |
| const char* abilityName | 创建会话的ability名。 |
| OH_AVSession ** avsession | 返回的媒体会话对象。 |

**返回：**

 展开

| 类型 | 说明 |
| --- | --- |
| AVSession_ErrCode | AV_SESSION_ERR_SUCCESS：函数执行成功。 AV_SESSION_ERR_INVALID_PARAMETER： 1.参数sessionType无效。 2.参数sessionTag为nullptr。 3.参数bundleName为nullptr。 4.参数abilityName为nullptr。 5.参数avsession为nullptr。 |

### OH_AVSession_Destroy()

支持设备PhonePC/2in1TabletTVWearable

```
AVSession_ErrCode OH_AVSession_Destroy(OH_AVSession* avsession)
```

**描述**

销毁会话对象。

**起始版本：** 13

**参数：**

 展开

| 参数项 | 描述 |
| --- | --- |
| OH_AVSession * avsession | 媒体会话对象。 |

**返回：**

 展开

| 类型 | 说明 |
| --- | --- |
| AVSession_ErrCode | AV_SESSION_ERR_SUCCESS：函数执行成功。 AV_SESSION_ERR_INVALID_PARAMETER：参数avsession为nullptr。 |

### OH_AVSession_Activate()

支持设备PhonePC/2in1TabletTVWearable

```
AVSession_ErrCode OH_AVSession_Activate(OH_AVSession* avsession)
```

**描述**

激活会话。

**起始版本：** 13

**参数：**

 展开

| 参数项 | 描述 |
| --- | --- |
| OH_AVSession * avsession | 媒体会话对象。 |

**返回：**

 展开

| 类型 | 说明 |
| --- | --- |
| AVSession_ErrCode | AV_SESSION_ERR_SUCCESS：函数执行成功。 AV_SESSION_ERR_INVALID_PARAMETER：参数avsession为nullptr。 AV_SESSION_ERR_SERVICE_EXCEPTION：会话服务异常。 |

### OH_AVSession_Deactivate()

支持设备PhonePC/2in1TabletTVWearable

```
AVSession_ErrCode OH_AVSession_Deactivate(OH_AVSession* avsession)
```

**描述**

取消激活媒体会话。

**起始版本：** 13

**参数：**

 展开

| 参数项 | 描述 |
| --- | --- |
| OH_AVSession * avsession | 媒体会话对象。 |

**返回：**

 展开

| 类型 | 说明 |
| --- | --- |
| AVSession_ErrCode | AV_SESSION_ERR_SUCCESS：函数执行成功。 AV_SESSION_ERR_INVALID_PARAMETER：参数avsession为nullptr。 AV_SESSION_ERR_SERVICE_EXCEPTION：会话服务异常。 |

### OH_AVSession_GetSessionType()

支持设备PhonePC/2in1TabletTVWearable

```
AVSession_ErrCode OH_AVSession_GetSessionType(OH_AVSession* avsession, AVSession_Type* sessionType)
```

**描述**

获取会话类型。

**起始版本：** 13

**参数：**

 展开

| 参数项 | 描述 |
| --- | --- |
| OH_AVSession * avsession | 媒体会话对象。 |
| AVSession_Type * sessionType | 返回的会话类型。 |

**返回：**

 展开

| 类型 | 说明 |
| --- | --- |
| AVSession_ErrCode | AV_SESSION_ERR_SUCCESS：函数执行成功。 AV_SESSION_ERR_SERVICE_EXCEPTION：会话服务异常，获取session type错误。 AV_SESSION_ERR_INVALID_PARAMETER： 1.参数avsession为nullptr。 2.参数sessionType为nullptr。 |

### OH_AVSession_GetSessionId()

支持设备PhonePC/2in1TabletTVWearable

```
AVSession_ErrCode OH_AVSession_GetSessionId(OH_AVSession* avsession, const char** sessionId)
```

**描述**

获取会话id。

**起始版本：** 13

**参数：**

 展开

| 参数项 | 描述 |
| --- | --- |
| OH_AVSession * avsession | 媒体会话对象。 |
| const char** sessionId | 返回的会话类型id。 |

**返回：**

 展开

| 类型 | 说明 |
| --- | --- |
| AVSession_ErrCode | AV_SESSION_ERR_SUCCESS：函数执行成功。 AV_SESSION_ERR_INVALID_PARAMETER： 1.参数avsession为nullptr。 2.参数sessionId为nullptr。 |

### OH_AVSession_SetAVMetadata()

支持设备PhonePC/2in1TabletTVWearable

```
AVSession_ErrCode OH_AVSession_SetAVMetadata(OH_AVSession* avsession, OH_AVMetadata* avmetadata)
```

**描述**

设置媒体元数据。

**起始版本：** 13

**参数：**

 展开

| 参数项 | 描述 |
| --- | --- |
| OH_AVSession * avsession | 媒体会话对象。 |
| OH_AVMetadata * avmetadata | 设置媒体元数据信息。 |

**返回：**

 展开

| 类型 | 说明 |
| --- | --- |
| AVSession_ErrCode | AV_SESSION_ERR_SUCCESS：函数执行成功。 AV_SESSION_ERR_SERVICE_EXCEPTION：会话服务异常。 AV_SESSION_ERR_INVALID_PARAMETER： 1.参数avsession为nullptr。 2.参数avmetadata为nullptr。 |

### OH_AVSession_SetPlaybackState()

支持设备PhonePC/2in1TabletTVWearable

```
AVSession_ErrCode OH_AVSession_SetPlaybackState(OH_AVSession* avsession,AVSession_PlaybackState playbackState)
```

**描述**

设置播放状态。

**起始版本：** 13

**参数：**

 展开

| 参数项 | 描述 |
| --- | --- |
| OH_AVSession * avsession | 媒体会话对象。 |
| AVSession_PlaybackState playbackState | 播放状态。 |

**返回：**

 展开

| 类型 | 说明 |
| --- | --- |
| AVSession_ErrCode | AV_SESSION_ERR_SUCCESS：函数执行成功。 AV_SESSION_ERR_SERVICE_EXCEPTION：会话服务异常。 AV_SESSION_ERR_INVALID_PARAMETER： 1.参数avsession为nullptr。 2.参数playbackState无效。 |

### OH_AVSession_SetPlaybackPosition()

支持设备PhonePC/2in1TabletTVWearable

```
AVSession_ErrCode OH_AVSession_SetPlaybackPosition(OH_AVSession* avsession,AVSession_PlaybackPosition* playbackPosition)
```

**描述**

设置播放位置。

**起始版本：** 13

**参数：**

 展开

| 参数项 | 描述 |
| --- | --- |
| OH_AVSession * avsession | 媒体会话对象。 |
| AVSession_PlaybackPosition * playbackPosition | 播放位置对象。 |

**返回：**

 展开

| 类型 | 说明 |
| --- | --- |
| AVSession_ErrCode | AV_SESSION_ERR_SUCCESS：函数执行成功。 AV_SESSION_ERR_SERVICE_EXCEPTION：会话服务异常。 AV_SESSION_ERR_INVALID_PARAMETER： 1.参数avsession为nullptr。 2.参数playbackPosition为nullptr。 |

### OH_AVSession_SetFavorite()

支持设备PhonePC/2in1TabletTVWearable

```
AVSession_ErrCode OH_AVSession_SetFavorite(OH_AVSession* avsession, bool favorite)
```

**描述**

设置收藏状态。

**起始版本：** 13

**参数：**

 展开

| 参数项 | 描述 |
| --- | --- |
| OH_AVSession * avsession | 媒体会话对象。 |
| bool favorite | 收藏状态，true表示收藏，false表示取消收藏。 |

**返回：**

 展开

| 类型 | 说明 |
| --- | --- |
| AVSession_ErrCode | AV_SESSION_ERR_SUCCESS：函数执行成功。 AV_SESSION_ERR_SERVICE_EXCEPTION：会话服务异常。 AV_SESSION_ERR_INVALID_PARAMETER：参数avsession为nullptr。 |

### OH_AVSession_SetLoopMode()

支持设备PhonePC/2in1TabletTVWearable

```
AVSession_ErrCode OH_AVSession_SetLoopMode(OH_AVSession* avsession, AVSession_LoopMode loopMode)
```

**描述**

设置循环模式。

**起始版本：** 13

**参数：**

 展开

| 参数项 | 描述 |
| --- | --- |
| OH_AVSession * avsession | 媒体会话对象。 |
| AVSession_LoopMode loopMode | 循环模式。 |

**返回：**

 展开

| 类型 | 说明 |
| --- | --- |
| AVSession_ErrCode | AV_SESSION_ERR_SUCCESS：函数执行成功。 AV_SESSION_ERR_SERVICE_EXCEPTION：会话服务异常。 AV_SESSION_ERR_INVALID_PARAMETER： 1.参数avsession为nullptr。 2.参数loopMode无效。 |

### OH_AVSession_RegisterCommandCallback()

支持设备PhonePC/2in1TabletTVWearable

```
AVSession_ErrCode OH_AVSession_RegisterCommandCallback(OH_AVSession* avsession,AVSession_ControlCommand command, OH_AVSessionCallback_OnCommand callback, void* userData)
```

**描述**

注册通用播控的回调。

**起始版本：** 13

**参数：**

 展开

| 参数项 | 描述 |
| --- | --- |
| OH_AVSession * avsession | 媒体会话对象。 |
| AVSession_ControlCommand command | 播控的控制命令。 |
| OH_AVSessionCallback_OnCommand callback | 控制命令的回调。 |
| void* userData | 指向通过回调函数传递的应用数据指针。 |

**返回：**

 展开

| 类型 | 说明 |
| --- | --- |
| AVSession_ErrCode | AV_SESSION_ERR_SUCCESS：函数执行成功。 AV_SESSION_ERR_CODE_COMMAND_INVALID：控制命令无效。 AV_SESSION_ERR_SERVICE_EXCEPTION：会话服务异常。 AV_SESSION_ERR_INVALID_PARAMETER： 1.参数avsession为nullptr。 2.参数callback为nullptr。 |

### OH_AVSession_UnregisterCommandCallback()

支持设备PhonePC/2in1TabletTVWearable

```
AVSession_ErrCode OH_AVSession_UnregisterCommandCallback(OH_AVSession* avsession,AVSession_ControlCommand command, OH_AVSessionCallback_OnCommand callback)
```

**描述**

取消注册通用播控的回调。

**起始版本：** 13

**参数：**

 展开

| 参数项 | 描述 |
| --- | --- |
| OH_AVSession * avsession | 媒体会话对象。 |
| AVSession_ControlCommand command | 播控的控制命令。 |
| OH_AVSessionCallback_OnCommand callback | 控制命令的回调。 |

**返回：**

 展开

| 类型 | 说明 |
| --- | --- |
| AVSession_ErrCode | AV_SESSION_ERR_SUCCESS：函数执行成功。 AV_SESSION_ERR_CODE_COMMAND_INVALID：控制命令无效。 AV_SESSION_ERR_SERVICE_EXCEPTION：会话服务异常。 AV_SESSION_ERR_INVALID_PARAMETER： 1.参数avsession为nullptr。 2.参数callback为nullptr。 |

### OH_AVSession_RegisterForwardCallback()

支持设备PhonePC/2in1TabletTVWearable

```
AVSession_ErrCode OH_AVSession_RegisterForwardCallback(OH_AVSession* avsession,OH_AVSessionCallback_OnFastForward callback, void* userData)
```

**描述**

注册快进的回调。

**起始版本：** 13

**参数：**

 展开

| 参数项 | 描述 |
| --- | --- |
| OH_AVSession * avsession | 媒体会话对象。 |
| OH_AVSessionCallback_OnFastForward callback | 快进命令的回调。 |
| void* userData | 指向通过回调函数传递的应用数据指针。 |

**返回：**

 展开

| 类型 | 说明 |
| --- | --- |
| AVSession_ErrCode | AV_SESSION_ERR_SUCCESS：函数执行成功。 AV_SESSION_ERR_SERVICE_EXCEPTION：会话服务异常。 AV_SESSION_ERR_INVALID_PARAMETER： 1.参数avsession为nullptr。 2.参数callback为nullptr。 |

### OH_AVSession_UnregisterForwardCallback()

支持设备PhonePC/2in1TabletTVWearable

```
AVSession_ErrCode OH_AVSession_UnregisterForwardCallback(OH_AVSession* avsession,OH_AVSessionCallback_OnFastForward callback)
```

**描述**

取消注册快进的回调。

**起始版本：** 13

**参数：**

 展开

| 参数项 | 描述 |
| --- | --- |
| OH_AVSession * avsession | 媒体会话对象。 |
| OH_AVSessionCallback_OnFastForward callback | 快进命令的回调。 |

**返回：**

 展开

| 类型 | 说明 |
| --- | --- |
| AVSession_ErrCode | AV_SESSION_ERR_SUCCESS：函数执行成功。 AV_SESSION_ERR_SERVICE_EXCEPTION：会话服务异常。 AV_SESSION_ERR_INVALID_PARAMETER： 1.参数avsession为nullptr。 2.参数callback为nullptr。 |

### OH_AVSession_RegisterRewindCallback()

支持设备PhonePC/2in1TabletTVWearable

```
AVSession_ErrCode OH_AVSession_RegisterRewindCallback(OH_AVSession* avsession,OH_AVSessionCallback_OnRewind callback, void* userData)
```

**描述**

注册快退的回调。

**起始版本：** 13

**参数：**

 展开

| 参数项 | 描述 |
| --- | --- |
| OH_AVSession * avsession | 媒体会话对象。 |
| OH_AVSessionCallback_OnRewind callback | 快退命令的回调。 |
| void* userData | 指向通过回调函数传递的应用数据指针。 |

**返回：**

 展开

| 类型 | 说明 |
| --- | --- |
| AVSession_ErrCode | AV_SESSION_ERR_SUCCESS：函数执行成功。 AV_SESSION_ERR_SERVICE_EXCEPTION：会话服务异常。 AV_SESSION_ERR_INVALID_PARAMETER： 1.参数avsession为nullptr。 2.参数callback为nullptr。 |

### OH_AVSession_UnregisterRewindCallback()

支持设备PhonePC/2in1TabletTVWearable

```
AVSession_ErrCode OH_AVSession_UnregisterRewindCallback(OH_AVSession* avsession,OH_AVSessionCallback_OnRewind callback)
```

**描述**

取消注册快退的回调。

**起始版本：** 13

**参数：**

 展开

| 参数项 | 描述 |
| --- | --- |
| OH_AVSession * avsession | 媒体会话对象。 |
| OH_AVSessionCallback_OnRewind callback | 快退命令的回调。 |

**返回：**

 展开

| 类型 | 说明 |
| --- | --- |
| AVSession_ErrCode | AV_SESSION_ERR_SUCCESS：函数执行成功。 AV_SESSION_ERR_SERVICE_EXCEPTION：会话服务异常。 AV_SESSION_ERR_INVALID_PARAMETER： 1.参数avsession为nullptr。 2.参数callback为nullptr。 |

### OH_AVSession_RegisterSeekCallback()

支持设备PhonePC/2in1TabletTVWearable

```
AVSession_ErrCode OH_AVSession_RegisterSeekCallback(OH_AVSession* avsession,OH_AVSessionCallback_OnSeek callback, void* userData)
```

**描述**

注册跳转的回调。

**起始版本：** 13

**参数：**

 展开

| 参数项 | 描述 |
| --- | --- |
| OH_AVSession * avsession | 媒体会话对象。 |
| OH_AVSessionCallback_OnSeek callback | 跳转命令的回调。 |
| void* userData | 指向通过回调函数传递的应用数据指针。 |

**返回：**

 展开

| 类型 | 说明 |
| --- | --- |
| AVSession_ErrCode | AV_SESSION_ERR_SUCCESS：函数执行成功。 AV_SESSION_ERR_SERVICE_EXCEPTION：会话服务异常。 AV_SESSION_ERR_INVALID_PARAMETER： 1.参数avsession为nullptr。 2.参数callback为nullptr。 |

### OH_AVSession_UnregisterSeekCallback()

支持设备PhonePC/2in1TabletTVWearable

```
AVSession_ErrCode OH_AVSession_UnregisterSeekCallback(OH_AVSession* avsession,OH_AVSessionCallback_OnSeek callback)
```

**描述**

取消注册跳转的回调。

**起始版本：** 13

**参数：**

 展开

| 参数项 | 描述 |
| --- | --- |
| OH_AVSession * avsession | 媒体会话对象。 |
| OH_AVSessionCallback_OnSeek callback | 跳转命令的回调。 |

**返回：**

 展开

| 类型 | 说明 |
| --- | --- |
| AVSession_ErrCode | AV_SESSION_ERR_SUCCESS：函数执行成功。 AV_SESSION_ERR_SERVICE_EXCEPTION：会话服务异常。 AV_SESSION_ERR_INVALID_PARAMETER： 1.参数avsession为nullptr。 2.参数callback为nullptr。 |

### OH_AVSession_RegisterSetLoopModeCallback()

支持设备PhonePC/2in1TabletTVWearable

```
AVSession_ErrCode OH_AVSession_RegisterSetLoopModeCallback(OH_AVSession* avsession,OH_AVSessionCallback_OnSetLoopMode callback, void* userData)
```

**描述**

注册设置循环模式的回调。

**起始版本：** 13

**参数：**

 展开

| 参数项 | 描述 |
| --- | --- |
| OH_AVSession * avsession | 媒体会话对象。 |
| OH_AVSessionCallback_OnSetLoopMode callback | 设置循环模式命令的回调。 |
| void* userData | 指向通过回调函数传递的应用数据指针。 |

**返回：**

 展开

| 类型 | 说明 |
| --- | --- |
| AVSession_ErrCode | AV_SESSION_ERR_SUCCESS：函数执行成功。 AV_SESSION_ERR_SERVICE_EXCEPTION：会话服务异常。 AV_SESSION_ERR_INVALID_PARAMETER： 1.参数avsession为nullptr。 2.参数callback为nullptr。 |

### OH_AVSession_UnregisterSetLoopModeCallback()

支持设备PhonePC/2in1TabletTVWearable

```
AVSession_ErrCode OH_AVSession_UnregisterSetLoopModeCallback(OH_AVSession* avsession,OH_AVSessionCallback_OnSetLoopMode callback)
```

**描述**

取消注册设置循环模式的回调。

**起始版本：** 13

**参数：**

 展开

| 参数项 | 描述 |
| --- | --- |
| OH_AVSession * avsession | 媒体会话对象。 |
| OH_AVSessionCallback_OnSetLoopMode callback | 设置循环模式命令的回调。 |

**返回：**

 展开

| 类型 | 说明 |
| --- | --- |
| AVSession_ErrCode | AV_SESSION_ERR_SUCCESS：函数执行成功。 AV_SESSION_ERR_SERVICE_EXCEPTION：会话服务异常。 AV_SESSION_ERR_INVALID_PARAMETER： 1.参数avsession为nullptr。 2.参数callback为nullptr。 |

### OH_AVSession_RegisterToggleFavoriteCallback()

支持设备PhonePC/2in1TabletTVWearable

```
AVSession_ErrCode OH_AVSession_RegisterToggleFavoriteCallback(OH_AVSession* avsession,OH_AVSessionCallback_OnToggleFavorite callback, void* userData)
```

**描述**

设置收藏的回调。

**起始版本：** 13

**参数：**

 展开

| 参数项 | 描述 |
| --- | --- |
| OH_AVSession * avsession | 媒体会话对象。 |
| OH_AVSessionCallback_OnToggleFavorite callback | 设置收藏命令的回调。 |
| void* userData | 指向通过回调函数传递的应用数据指针。 |

**返回：**

 展开

| 类型 | 说明 |
| --- | --- |
| AVSession_ErrCode | AV_SESSION_ERR_SUCCESS：函数执行成功。 AV_SESSION_ERR_SERVICE_EXCEPTION：会话服务异常。 AV_SESSION_ERR_INVALID_PARAMETER： 1.参数avsession为nullptr。 2.参数callback为nullptr。 |

### OH_AVSession_UnregisterToggleFavoriteCallback()

支持设备PhonePC/2in1TabletTVWearable

```
AVSession_ErrCode OH_AVSession_UnregisterToggleFavoriteCallback(OH_AVSession* avsession,OH_AVSessionCallback_OnToggleFavorite callback)
```

**描述**

取消设置收藏的回调。

**起始版本：** 13

**参数：**

 展开

| 参数项 | 描述 |
| --- | --- |
| OH_AVSession * avsession | 媒体会话对象。 |
| OH_AVSessionCallback_OnToggleFavorite callback | 设置收藏命令的回调。 |

**返回：**

 展开

| 类型 | 说明 |
| --- | --- |
| AVSession_ErrCode | AV_SESSION_ERR_SUCCESS：函数执行成功。 AV_SESSION_ERR_SERVICE_EXCEPTION：会话服务异常。 AV_SESSION_ERR_INVALID_PARAMETER： 1.参数avsession为nullptr。 2.参数callback为nullptr。 |