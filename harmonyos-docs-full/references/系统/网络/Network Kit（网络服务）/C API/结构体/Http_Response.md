# Http_Response

```
typedef struct Http_Response {...} Http_Response
```

## 概述

支持设备PhonePC/2in1TabletTVWearable

定义HTTP响应的结构体。

**起始版本：** 20

**相关模块：** [netstack](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack)

**所在头文件：** [net_http_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-http-type-h)

## 汇总

支持设备PhonePC/2in1TabletTVWearable 

### 成员变量

 支持设备PhonePC/2in1TabletTVWearable展开

| 名称 | 描述 |
| --- | --- |
| Http_Buffer body | HTTP请求响应的数据，参考 Http_Buffer 。 |
| Http_ResponseCode responseCode | HTTP请求响应码，参考 Http_ResponseCode 。 |
| Http_Headers *headers | HTTP响应的头，指向Http_Headers的指针，参考 Http_Headers 。 |
| char *cookies | HTTP响应Cookies。 |
| Http_PerformanceTiming *performanceTiming | HTTP响应时间信息，指向Http_PerformanceTiming的指针，参考 Http_PerformanceTiming 。 |

### 成员函数

 支持设备PhonePC/2in1TabletTVWearable展开

| 名称 | 描述 |
| --- | --- |
| void (*destroyResponse)(struct Http_Response **response) | 销毁HTTP响应的回调函数 |

## 成员函数说明

支持设备PhonePC/2in1TabletTVWearable 

### destroyResponse()

支持设备PhonePC/2in1TabletTVWearable

```
void (*destroyResponse)(struct Http_Response **response)
```

**描述**

销毁HTTP响应的回调函数

**起始版本：** 20

**参数：**

 展开

| 参数项 | 描述 |
| --- | --- |
| struct Http_Response **response | 要销毁的HTTP响应，指向Http_Response的指针，参考 Http_Response 。 |