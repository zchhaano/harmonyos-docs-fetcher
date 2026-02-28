## 概述

支持设备PhonePC/2in1TabletTVWearable

指定静态DNS规则使用的IP地址组。用于[Rcp_StaticDnsRuleItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___static_dns_rule_item)。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview)

## 汇总

支持设备PhonePC/2in1TabletTVWearable 

### 成员变量

 支持设备PhonePC/2in1TabletTVWearable展开

| 名称 | 描述 |
| --- | --- |
| char ipAddress [ RCP_IP_MAX_LEN ] | IP地址。 |
| struct Rcp_IpAddress * next | 链式存储。指向下一个 Rcp_IpAddress 。 |

## 结构体成员变量说明

支持设备PhonePC/2in1TabletTVWearable 

### ipAddress

支持设备PhonePC/2in1TabletTVWearable

```
char Rcp_IpAddress::ipAddress[ RCP_IP_MAX_LEN ]
```

**描述**

ip地址。

### next

支持设备PhonePC/2in1TabletTVWearable

```
struct Rcp_IpAddress * Rcp_IpAddress::next
```

**描述**

链式存储。指向下一个[Rcp_IpAddress](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___ip_address)。