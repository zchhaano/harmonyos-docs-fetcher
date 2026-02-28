## 概述

支持设备PhonePC/2in1TabletTVWearable

描述单个静态DNS规则。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview)

## 汇总

支持设备PhonePC/2in1TabletTVWearable 

### 成员变量

 支持设备PhonePC/2in1TabletTVWearable展开

| 名称 | 描述 |
| --- | --- |
| char host [ RCP_HOST_MAX_LEN ] | 主机名。 |
| uint16_t port | 端口号。范围： [0, 65535]。 |
| Rcp_IpAddress * ipAddresses | 表示 Rcp_StaticDnsRuleItem.host 对应的IP地址。 |

## 结构体成员变量说明

支持设备PhonePC/2in1TabletTVWearable 

### host

支持设备PhonePC/2in1TabletTVWearable

```
char Rcp_StaticDnsRuleItem::host[ RCP_HOST_MAX_LEN ]
```

**描述**

主机名。

### ipAddresses

支持设备PhonePC/2in1TabletTVWearable

```
Rcp_IpAddress * Rcp_StaticDnsRuleItem::ipAddresses
```

**描述**

表示[Rcp_StaticDnsRuleItem.host](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___static_dns_rule_item#a1d3b3f7dce4d6bc4cca968d9c039d4f0)对应的IP地址。

### port

支持设备PhonePC/2in1TabletTVWearable

```
uint16_t Rcp_StaticDnsRuleItem::port
```

**描述**

端口号。范围： [0, 65535]。