## 概述

支持设备PhonePC/2in1TabletTVWearable

DNS解析配置。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview)

## 汇总

支持设备PhonePC/2in1TabletTVWearable 

### 成员变量

 支持设备PhonePC/2in1TabletTVWearable展开

| 名称 | 描述 |
| --- | --- |
| Rcp_DnsRule * dnsRules | DNS规则配置。 |
| Rcp_DnsOverHttps dnsOverHttps | DOH配置。 |

## 结构体成员变量说明

支持设备PhonePC/2in1TabletTVWearable 

### dnsOverHttps

支持设备PhonePC/2in1TabletTVWearable

```
Rcp_DnsOverHttps Rcp_DnsConfiguration::dnsOverHttps
```

**描述**

DOH配置。

### dnsRules

支持设备PhonePC/2in1TabletTVWearable

```
Rcp_DnsRule * Rcp_DnsConfiguration::dnsRules
```

**描述**

DNS规则配置。

[Rcp_DnsServers](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___dns_servers): 表示优先使用指定的dns服务器解析主机名。

[Rcp_StaticDnsRule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___static_dns_rule): 表示如果主机名匹配，则优先使用指定的地址。

[Rcp_DynamicDnsRuleFunction](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview#gad0ace0c83dd20972b34ff1538700eab3): 表示优先使用函数中返回的地址。