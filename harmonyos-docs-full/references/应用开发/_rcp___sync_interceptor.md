## 概述

支持设备PhonePC/2in1TabletTVWearable

同步拦截器。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview)

## 汇总

支持设备PhonePC/2in1TabletTVWearable 

### 成员变量

 支持设备PhonePC/2in1TabletTVWearable展开

| 名称 | 描述 |
| --- | --- |
| Rcp_Response *(* intercept )( Rcp_Request *request, const Rcp_SyncRequestHandler *next, uint32_t *errCode) | 指向同步拦截器函数的指针。用户若需要使用拦截器，需实现该函数。 |

## 结构体成员变量说明

支持设备PhonePC/2in1TabletTVWearable 

### intercept

支持设备PhonePC/2in1TabletTVWearable

```
Rcp_Response *(* Rcp_SyncInterceptor::intercept) ( Rcp_Request *request, const Rcp_SyncRequestHandler *next, uint32_t *errCode)
```

**描述**

指向同步拦截器函数的指针。用户若需要使用拦截器，需实现该函数。

**起始版本：** 5.0.0(12)

**参数:**

 展开

| 名称 | 描述 |
| --- | --- |
| request | 指向 Rcp_Request 的指针。 |
| next | 指向下一个同步处理器的指针 Rcp_SyncRequestHandler 。 |
| errCode | 表示拦截器的返回值。 |

**返回：**

Rcp_Response* 返回的响应。