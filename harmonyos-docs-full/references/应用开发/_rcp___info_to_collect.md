## 概述

支持设备PhonePC/2in1TabletTVWearable

指定要收集的请求处理事件。可以通过响应对象检查收集的事件。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview)

## 汇总

支持设备PhonePC/2in1TabletTVWearable 

### 成员变量

 支持设备PhonePC/2in1TabletTVWearable展开

| 名称 | 描述 |
| --- | --- |
| bool textual | 是否收集未分类的文本事件。默认值为false。 |
| bool incomingHeader | 是否收集传入HTTP标头事件。默认值为false。 |
| bool outgoingHeader | 是否收集传出HTTP标头事件。默认值为false。 |
| bool incomingData | 是否收集有关传入HTTP数据的事件。默认值为false。 |
| bool outgoingData | 是否收集有关传出HTTP数据的事件。默认值为false。 |
| bool incomingSslData | 是否收集传入的SSL/TLS事件。默认值为false。 |
| bool outgoingSslData | 是否收集传出的SSL/TLS事件。默认值为false。 |

## 结构体成员变量说明

支持设备PhonePC/2in1TabletTVWearable 

### incomingData

支持设备PhonePC/2in1TabletTVWearable

```
bool Rcp_InfoToCollect::incomingData
```

**描述**

是否收集有关传入HTTP数据的事件。默认值为false。

### incomingHeader

支持设备PhonePC/2in1TabletTVWearable

```
bool Rcp_InfoToCollect::incomingHeader
```

**描述**

是否收集传入HTTP标头事件。默认值为false。

### incomingSslData

支持设备PhonePC/2in1TabletTVWearable

```
bool Rcp_InfoToCollect::incomingSslData
```

**描述**

是否收集传入的SSL/TLS事件。默认值为false。

### outgoingData

支持设备PhonePC/2in1TabletTVWearable

```
bool Rcp_InfoToCollect::outgoingData
```

**描述**

是否收集有关传出HTTP数据的事件。默认值为false。

### outgoingHeader

支持设备PhonePC/2in1TabletTVWearable

```
bool Rcp_InfoToCollect::outgoingHeader
```

**描述**

是否收集传出HTTP标头事件。默认值为false。

### outgoingSslData

支持设备PhonePC/2in1TabletTVWearable

```
bool Rcp_InfoToCollect::outgoingSslData
```

**描述**

是否收集传出的SSL/TLS事件。默认值为false。

### textual

支持设备PhonePC/2in1TabletTVWearable

```
bool Rcp_InfoToCollect::textual
```

**描述**

是否收集未分类的文本事件。默认值为false。