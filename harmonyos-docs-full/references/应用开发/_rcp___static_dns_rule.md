## 概述

支持设备PhonePC/2in1TabletTVWearable

静态DNS规则。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview)

## 汇总

支持设备PhonePC/2in1TabletTVWearable 

### 成员变量

 支持设备PhonePC/2in1TabletTVWearable展开

| 名称 | 描述 |
| --- | --- |
| Rcp_StaticDnsRuleItem staticDnsRule | 单个静态DNS规则。 |
| struct Rcp_StaticDnsRule * next | 链式存储。指向下一个 Rcp_StaticDnsRule 的指针。 |

## 结构体成员变量说明

支持设备PhonePC/2in1TabletTVWearable 

### next

支持设备PhonePC/2in1TabletTVWearable

```
struct Rcp_StaticDnsRule * Rcp_StaticDnsRule::next
```

**描述**

链式存储。指向下一个[Rcp_StaticDnsRule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___static_dns_rule)的指针。

### staticDnsRule

支持设备PhonePC/2in1TabletTVWearable

```
Rcp_StaticDnsRuleItem Rcp_StaticDnsRule::staticDnsRule
```

**描述**

单个静态DNS规则。