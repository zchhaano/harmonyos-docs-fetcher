## 概述

支持设备PhonePC/2in1TabletTVWearable

请求追踪配置。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview)

## 汇总

支持设备PhonePC/2in1TabletTVWearable 

### 成员变量

 支持设备PhonePC/2in1TabletTVWearable展开

| 名称 | 描述 |
| --- | --- |
| bool verbose | 请求运行时是否记录详细日志。默认值为false。如果设置了infoToCollect中的选项，则自动启用。 |
| Rcp_InfoToCollect infoToCollect | 指定要收集的请求处理事件。可以通过响应对象检查收集的事件。 |
| bool collectTimeInfo | 是否收集请求计时信息。默认值为false。 |
| Rcp_EventsHandler httpEventsHandler | 监听不同HTTP事件的回调函数。 |

## 结构体成员变量说明

支持设备PhonePC/2in1TabletTVWearable 

### collectTimeInfo

支持设备PhonePC/2in1TabletTVWearable

```
bool Rcp_TracingConfiguration::collectTimeInfo
```

**描述**

是否收集请求计时信息。默认值为false。

### httpEventsHandler

支持设备PhonePC/2in1TabletTVWearable

```
Rcp_EventsHandler Rcp_TracingConfiguration::httpEventsHandler
```

**描述**

监听不同HTTP事件的回调函数。

### infoToCollect

支持设备PhonePC/2in1TabletTVWearable

```
Rcp_InfoToCollect Rcp_TracingConfiguration::infoToCollect
```

**描述**

指定要收集的请求处理事件。可以通过响应对象检查收集的事件。

### verbose

支持设备PhonePC/2in1TabletTVWearable

```
bool Rcp_TracingConfiguration::verbose
```

**描述**

请求运行时是否记录详细日志。默认值为false。如果设置了infoToCollect中的选项，则自动启用。