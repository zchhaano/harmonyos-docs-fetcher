## 概述

支持设备PhonePC/2in1TabletTVWearable

会话配置。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview)

## 汇总

支持设备PhonePC/2in1TabletTVWearable 

### 成员变量

 支持设备PhonePC/2in1TabletTVWearable展开

| 名称 | 描述 |
| --- | --- |
| Rcp_SessionType type | 会话类型。 |
| Rcp_InterceptorArray interceptors | 用户自定义的异步拦截器数组。 |
| Rcp_SyncInterceptorArray syncInterceptors | 用户定义的同步拦截器数组。 |
| const char * baseUrl | 基本URL。 |
| Rcp_Headers * headers | 请求标头。 |
| Rcp_RequestCookies * cookies | 请求的Cookie。 |
| Rcp_SessionListener sessionListener | 回调函数，供session监听close()或cancel()事件。 |
| Rcp_Configuration * requestConfiguration | 默认请求配置。这些选项可以通过 Request.configuration 来覆盖。 |
| Rcp_ConnectionConfiguration connectionConfiguration | 连接配置。 |

## 结构体成员变量说明

支持设备PhonePC/2in1TabletTVWearable 

### baseUrl

支持设备PhonePC/2in1TabletTVWearable

```
const char* Rcp_SessionConfiguration::baseUrl
```

**描述**

基本URL。

举例， 如果请求的url为 '?name=value', 基本url是 'https://example.com'，那么最后当请求被送往服务端时的最终url为 'https://example.com?name=value'。

### connectionConfiguration

支持设备PhonePC/2in1TabletTVWearable

```
Rcp_ConnectionConfiguration Rcp_SessionConfiguration::connectionConfiguration
```

**描述**

连接配置。

它用于指定此会话中允许的最大同时连接总数以及允许连接到单个主机的最大同时连接数。

### cookies

支持设备PhonePC/2in1TabletTVWearable

```
Rcp_RequestCookies * Rcp_SessionConfiguration::cookies
```

**描述**

请求的Cookie。

如果调用了[HMS_Rcp_Fetch](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview#ga7ea546b69b9ea60ea4716ee64e8b04cb)或者[HMS_Rcp_FetchSync](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview#ga48a83535a4658e9872ded4b0dd8c812f)，在参数中的[Rcp_Request](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___request)中没有[Rcp_RequestCookies](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview#ga44f2b679fefd37e78c43dbcba59d6d50)，则[Rcp_SessionConfiguration.cookies](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___session_configuration#a16b3f819c4b51898edb1da8cf6341752)将是[Rcp_Request.cookies](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___request#a4233d0d064ac2209accfb25a701047c9)，如果两者都存在，则将它们合并。

### headers

支持设备PhonePC/2in1TabletTVWearable

```
Rcp_Headers * Rcp_SessionConfiguration::headers
```

**描述**

请求标头。

如果调用了[HMS_Rcp_Fetch](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview#ga7ea546b69b9ea60ea4716ee64e8b04cb)或[HMS_Rcp_FetchSync](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview#ga48a83535a4658e9872ded4b0dd8c812f)，并且[Rcp_Request](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___request)中没有[Rcp_Headers](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview#gac4f343ec02dec34268e93ce746e6c982)，[Rcp_SessionConfiguration.headers](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___session_configuration#a83eabab4e8f469be1d4fe9afa5a885e8)将是[Rcp_Request.headers](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___request#a4ebc6011dc454a18c04eca049f8e95cd)，如果两者都存在，则将它们合并。

### interceptors

支持设备PhonePC/2in1TabletTVWearable

```
Rcp_InterceptorArray Rcp_SessionConfiguration::interceptors
```

**描述**

用户自定义的异步拦截器数组。

异步拦截器将被制成拦截器链。

输入: [A, B, C, D]， 处理逻辑将为 A->B->C->D->defaultHandler。

### requestConfiguration

支持设备PhonePC/2in1TabletTVWearable

```
Rcp_Configuration * Rcp_SessionConfiguration::requestConfiguration
```

**描述**

默认请求配置。这些选项可以通过**Request.configuration**来覆盖。

### sessionListener

支持设备PhonePC/2in1TabletTVWearable

```
Rcp_SessionListener Rcp_SessionConfiguration::sessionListener
```

**描述**

回调函数，供session监听close()或cancel()事件。

### syncInterceptors

支持设备PhonePC/2in1TabletTVWearable

```
Rcp_SyncInterceptorArray Rcp_SessionConfiguration::syncInterceptors
```

**描述**

用户定义的同步拦截器数组。

同步拦截器会被做成拦截器链。

输入: [A, B, C, D], 处理逻辑将为 A->B->C->D->defaultHandler。

### type

支持设备PhonePC/2in1TabletTVWearable

```
Rcp_SessionType Rcp_SessionConfiguration::type
```

**描述**

会话类型。