## 概述

支持设备PhonePC/2in1TabletTVWearable

监听不同HTTP事件的回调函数。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview)

## 汇总

支持设备PhonePC/2in1TabletTVWearable 

### 成员变量

 支持设备PhonePC/2in1TabletTVWearable展开

| 名称 | 描述 |
| --- | --- |
| Rcp_OnDataReceiveCallback onDataReceive | 收到响应体时的回调函数。 |
| Rcp_OnProgressCallback onUploadProgress | 上传时调用的回调函数。 |
| Rcp_OnProgressCallback onDownloadProgress | 下载时调用的回调函数。 |
| Rcp_OnHeaderReceiveCallback onHeaderReceive | 收到header时的回调函数。 |
| Rcp_OnVoidCallback onDataEnd | 传输结束时的回调函数。 |
| Rcp_OnVoidCallback onCanceled | 请求或会话被取消时的回调函数。 |

## 结构体成员变量说明

支持设备PhonePC/2in1TabletTVWearable 

### onCanceled

支持设备PhonePC/2in1TabletTVWearable

```
Rcp_OnVoidCallback Rcp_EventsHandler::onCanceled
```

**描述**

请求或会话被取消时的回调函数。

### onDataEnd

支持设备PhonePC/2in1TabletTVWearable

```
Rcp_OnVoidCallback Rcp_EventsHandler::onDataEnd
```

**描述**

传输结束时的回调函数。

### onDataReceive

支持设备PhonePC/2in1TabletTVWearable

```
Rcp_OnDataReceiveCallback Rcp_EventsHandler::onDataReceive
```

**描述**

收到响应体时的回调函数。

### onDownloadProgress

支持设备PhonePC/2in1TabletTVWearable

```
Rcp_OnProgressCallback Rcp_EventsHandler::onDownloadProgress
```

**描述**

下载时调用的回调函数。

### onHeaderReceive

支持设备PhonePC/2in1TabletTVWearable

```
Rcp_OnHeaderReceiveCallback Rcp_EventsHandler::onHeaderReceive
```

**描述**

收到header时的回调函数。

### onUploadProgress

支持设备PhonePC/2in1TabletTVWearable

```
Rcp_OnProgressCallback Rcp_EventsHandler::onUploadProgress
```

**描述**

上传时调用的回调函数。