## 概述

支持设备PhonePC/2in1TabletTVWearable

代理配置中用于过滤不使用代理的urls。

如果[Rcp_Request.url](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___request#a39a1cc0a1ad666d8d9ad40eec4b52de7)匹配[Rcp_Exclusions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___exclusions)规则，则[Rcp_Request](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___request)不会使用代理。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview)

## 汇总

支持设备PhonePC/2in1TabletTVWearable 

### 成员变量

 支持设备PhonePC/2in1TabletTVWearable展开

| 名称 | 描述 |
| --- | --- |
| Rcp_ExclusionsValueType type | 表示union中使用的数据类型。 |
| union { | union结构。 |
| Rcp_Urls * urls | Urls。链式存储url。 |
| Rcp_ExclusionFunction exclusionFunction | 回调函数。通过回调函数过滤url。 |
| } data | data中使用的数据由type进行区分。 |

## 结构体成员变量说明

支持设备PhonePC/2in1TabletTVWearable 

### exclusionFunction

支持设备PhonePC/2in1TabletTVWearable

```
Rcp_ExclusionFunction Rcp_Exclusions::exclusionFunction
```

**描述**

通过回调过滤。

### type

支持设备PhonePC/2in1TabletTVWearable

```
Rcp_ExclusionsValueType Rcp_Exclusions::type
```

**描述**

表示union中使用的数据类型。

### urls

支持设备PhonePC/2in1TabletTVWearable

```
Rcp_Urls * Rcp_Exclusions::urls
```

**描述**

Urls。