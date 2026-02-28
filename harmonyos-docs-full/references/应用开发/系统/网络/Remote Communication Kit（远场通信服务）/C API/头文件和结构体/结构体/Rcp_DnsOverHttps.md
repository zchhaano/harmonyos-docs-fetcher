## 概述

支持设备PhonePC/2in1TabletTVWearable

HTTPS上的DNS配置如果设置，则首选由DOH dns服务器解析的地址。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview)

## 汇总

支持设备PhonePC/2in1TabletTVWearable 

### 成员变量

 支持设备PhonePC/2in1TabletTVWearable展开

| 名称 | 描述 |
| --- | --- |
| const char * url | DOH服务器的URL。 |
| bool skipCertificatesValidation | 判断是否跳过证书验证。默认值为false。 |

## 结构体成员变量说明

支持设备PhonePC/2in1TabletTVWearable 

### skipCertificatesValidation

支持设备PhonePC/2in1TabletTVWearable

```
bool Rcp_DnsOverHttps::skipCertificatesValidation
```

**描述**

判断是否跳过证书验证。默认值为false。

### url

支持设备PhonePC/2in1TabletTVWearable

```
const char* Rcp_DnsOverHttps::url
```

**描述**

DOH服务器的URL。