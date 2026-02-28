## 概述

支持设备PhonePC/2in1TabletTVWearable

响应的二进制数据接收回调函数。可以通过[HMS_Rcp_SetRequestOnBinaryDataRecvCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview#section207321113884)为请求设置相应回调函数。

**起始版本：** 5.0.1(13)

**相关模块：** [RemoteCommunication](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview)

## 汇总

支持设备PhonePC/2in1TabletTVWearable 

### 成员变量

 支持设备PhonePC/2in1TabletTVWearable展开

| 名称 | 描述 |
| --- | --- |
| Rcp_OnBinaryReceiveCallbackFunc callback | 请求过程中接收二进制数据的回调函数。 |
| void * usrObject | 用户定义的对象，在回调函数中使用。 |

## 结构体成员变量说明

支持设备PhonePC/2in1TabletTVWearable 

### callback

支持设备PhonePC/2in1TabletTVWearable

```
Rcp_OnBinaryReceiveCallbackFunc Rcp_OnBinaryReceiveCallback::callback
```

**描述**

二进制数据接收回调函数。

### usrObject

支持设备PhonePC/2in1TabletTVWearable

```
void* Rcp_OnBinaryReceiveCallback::usrObject
```

**描述**

用户定义的对象，在回调函数中使用。