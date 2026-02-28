# Http_Request

```
typedef struct Http_Request {...} Http_Request
```

## 概述

支持设备PhonePC/2in1TabletTVWearable

HTTP请求结构体。

**起始版本：** 20

**相关模块：** [netstack](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack)

**所在头文件：** [net_http_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-http-type-h)

## 汇总

支持设备PhonePC/2in1TabletTVWearable 

### 成员变量

 支持设备PhonePC/2in1TabletTVWearable展开

| 名称 | 描述 |
| --- | --- |
| uint32_t requestId | HTTP请求的Id。 |
| char *url | HTTP请求的URL。 |
| Http_RequestOptions *options | HTTP请求配置，指向Http_RequestOptions的指针，参考 Http_RequestOptions 。 |