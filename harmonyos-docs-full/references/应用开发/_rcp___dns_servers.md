## 概述

支持设备PhonePC/2in1TabletTVWearable

DNS服务器。[Rcp_DnsConfiguration.dnsRules](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___dns_configuration#ab09aacb68c682d9beea100cae481eaa4)中的类型之一。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview)

## 汇总

支持设备PhonePC/2in1TabletTVWearable 

### 成员变量

 支持设备PhonePC/2in1TabletTVWearable展开

| 名称 | 描述 |
| --- | --- |
| Rcp_IpAndPort ipAndPort | IP和端口。 |
| struct Rcp_DnsServers * next | 链式存储。指向下一个 Rcp_DnsServers 的指针。 |

## 结构体成员变量说明

支持设备PhonePC/2in1TabletTVWearable 

### ipAndPort

支持设备PhonePC/2in1TabletTVWearable

```
Rcp_IpAndPort Rcp_DnsServers::ipAndPort
```

**描述**

IP和端口。

### next

支持设备PhonePC/2in1TabletTVWearable

```
struct Rcp_DnsServers * Rcp_DnsServers::next
```

**描述**

链式存储。指向下一个[Rcp_DnsServers](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___dns_servers)的指针。