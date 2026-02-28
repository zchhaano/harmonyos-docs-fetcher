## 概述

支持设备PhonePC/2in1TabletTVWearable

该接口用在[Rcp_DnsServers](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___dns_servers)中，表示一个DNS服务器的地址和端口。

**起始版本：** 5.0.0(12)

**相关模块：**[RemoteCommunication](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview)

## 汇总

支持设备PhonePC/2in1TabletTVWearable 

### 成员变量

 支持设备PhonePC/2in1TabletTVWearable展开

| 名称 | 描述 |
| --- | --- |
| char ip [ RCP_IP_MAX_LEN ] | IPv4或IPv6地址。 |
| uint16_t port | 表示端口。取值范围：[0, 65535]。 |

## 结构体成员变量说明

支持设备PhonePC/2in1TabletTVWearable 

### ip

支持设备PhonePC/2in1TabletTVWearable

```
char Rcp_IpAndPort::ip[ RCP_IP_MAX_LEN ]
```

**描述**

IPv4或IPv6地址。

### port

支持设备PhonePC/2in1TabletTVWearable

```
uint16_t Rcp_IpAndPort::port
```

**描述**

表示端口。取值范围：[0, 65535]。