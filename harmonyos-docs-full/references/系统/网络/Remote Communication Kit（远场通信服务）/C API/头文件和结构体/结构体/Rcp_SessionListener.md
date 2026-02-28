## 概述

支持设备PhonePC/2in1TabletTVWearable

关闭或取消会话事件的回调函数。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview)

## 汇总

支持设备PhonePC/2in1TabletTVWearable 

### 成员变量

 支持设备PhonePC/2in1TabletTVWearable展开

| 名称 | 描述 |
| --- | --- |
| void(* onClosed )(void) | 此函数在 Rcp_Session 关闭时调用此函数。 |
| void(* onCanceled )(void) | 此函数在 Rcp_Session 取消时调用此函数。 |

## 结构体成员变量说明

支持设备PhonePC/2in1TabletTVWearable 

### onCanceled

支持设备PhonePC/2in1TabletTVWearable

```
void(* Rcp_SessionListener::onCanceled) (void)
```

**描述**

此函数在[Rcp_Session](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview#ga4f3a7d39c18fe6fdf01c52759213ddcd)取消时调用此函数。

### onClosed

支持设备PhonePC/2in1TabletTVWearable

```
void(* Rcp_SessionListener::onClosed) (void)
```

**描述**

此函数在[Rcp_Session](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview#ga4f3a7d39c18fe6fdf01c52759213ddcd)关闭时调用此函数。