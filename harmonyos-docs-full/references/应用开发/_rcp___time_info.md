## 概述

支持设备PhonePC/2in1TabletTVWearable

响应计时信息。

它将在[Rcp_Response.timeInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___response#a57d437be63e686ada47b96b3126067d8)中被收集，[Rcp_TracingConfiguration.collectTimeInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___tracing_configuration#aded07a3d27e7524e18362082264b9b94)决定是否收集它。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview)

## 汇总

支持设备PhonePC/2in1TabletTVWearable 

### 成员变量

 支持设备PhonePC/2in1TabletTVWearable展开

| 名称 | 描述 |
| --- | --- |
| double totalTime | HTTP传输（包括名称解析、TCP连接等）的总时间（毫秒）。 |
| double nameLookUpTime | 从开始到解析远程主机名所用的时间（以毫秒为单位）。 |
| double connectTime | 从开始到完成与远程主机（或代理）的连接的时间（以毫秒为单位）。 |
| double preTransferTime | 从开始到传输即将开始所花费的时间（以毫秒为单位）。 |
| double fileTime | 从远程文件的上次修改时间开始的时间（以毫秒为单位）。 |
| double startTransferTime | 从开始到接收到第一个字节所花费的时间（以毫秒为单位）。 |
| double redirectTime | 所有重定向步骤（包括名称查找、连接等）所用的时间（毫秒）。 |
| double tlsHandshakeTime | 从开始到完成与远程主机（或代理）的TLS握手的时间（以毫秒为单位）。 |

## 结构体成员变量说明

支持设备PhonePC/2in1TabletTVWearable 

### connectTime

支持设备PhonePC/2in1TabletTVWearable收起自动换行深色代码主题复制

```
double Rcp_TimeInfo::connectTime
```

**描述**

从开始到完成与远程主机（或代理）的连接时间（以毫秒为单位）。

### fileTime

支持设备PhonePC/2in1TabletTVWearable收起自动换行深色代码主题复制

```
double Rcp_TimeInfo::fileTime
```

**描述**

从远程文件的上次修改时间开始的时间（以毫秒为单位）。

### nameLookUpTime

支持设备PhonePC/2in1TabletTVWearable收起自动换行深色代码主题复制

```
double Rcp_TimeInfo::nameLookUpTime
```

**描述**

从开始到解析远程主机名所用的时间（以毫秒为单位）。

### preTransferTime

支持设备PhonePC/2in1TabletTVWearable收起自动换行深色代码主题复制

```
double Rcp_TimeInfo::preTransferTime
```

**描述**

从开始到传输即将开始所花费的时间（以毫秒为单位）。

### redirectTime

支持设备PhonePC/2in1TabletTVWearable收起自动换行深色代码主题复制

```
double Rcp_TimeInfo::redirectTime
```

**描述**

所有重定向步骤（包括名称查找、连接等）所用的时间（毫秒）。

### startTransferTime

支持设备PhonePC/2in1TabletTVWearable收起自动换行深色代码主题复制

```
double Rcp_TimeInfo::startTransferTime
```

**描述**

从开始到接收到第一个字节所花费的时间（以毫秒为单位）。

### tlsHandshakeTime

支持设备PhonePC/2in1TabletTVWearable收起自动换行深色代码主题复制

```
double Rcp_TimeInfo::tlsHandshakeTime
```

**描述**

从开始到完成与远程主机（或代理）的TLS握手的时间（以毫秒为单位）。

### totalTime

支持设备PhonePC/2in1TabletTVWearable收起自动换行深色代码主题复制

```
double Rcp_TimeInfo::totalTime
```

**描述**

HTTP传输（包括名称解析、TCP连接等）的总时间（毫秒）。