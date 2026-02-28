## 概述

支持设备PhonePC/2in1TabletTVWearable

DNS规则配置。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview)

## 汇总

支持设备PhonePC/2in1TabletTVWearable 

### 成员变量

 支持设备PhonePC/2in1TabletTVWearable展开

| 名称 | 描述 |
| --- | --- |
| Rcp_DnsRuleType type | 表示union中使用的数据类型。 |
| union { | union结构。data中使用的数据由type进行区分。 |
| Rcp_DnsServers * dnsServers | dnsServers：DNS服务器。 |
| Rcp_StaticDnsRule * staticDnsRule | staticDnsRule：静态DNS规则。 |
| Rcp_DynamicDnsRuleFunction dynamicDnsRule | dynamicDnsRule：动态DNS规则。 |
| } data | data中使用的数据由type进行区分。 |

## 结构体成员变量说明

支持设备PhonePC/2in1TabletTVWearable 

### dnsServers

支持设备PhonePC/2in1TabletTVWearable收起自动换行深色代码主题复制

```
Rcp_DnsServers * Rcp_DnsRule::dnsServers
```

**描述**

DNS服务器。

### dynamicDnsRule

支持设备PhonePC/2in1TabletTVWearable收起自动换行深色代码主题复制

```
Rcp_DynamicDnsRuleFunction Rcp_DnsRule::dynamicDnsRule
```

**描述**

动态DNS规则。

### staticDnsRule

支持设备PhonePC/2in1TabletTVWearable收起自动换行深色代码主题复制

```
Rcp_StaticDnsRule * Rcp_DnsRule::staticDnsRule
```

**描述**

静态DNS规则。

### type

支持设备PhonePC/2in1TabletTVWearable收起自动换行深色代码主题复制

```
Rcp_DnsRuleType Rcp_DnsRule:: type
```

**描述**

表示union中使用的数据类型。