# Http_HeaderEntry

```
typedef struct Http_HeaderEntry {...} Http_HeaderEntry
```

## 概述

支持设备PhonePC/2in1TabletTVWearable

请求或者响应的标头的所有键值对。

**起始版本：** 20

**相关模块：** [netstack](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack)

**所在头文件：** [net_http_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-http-type-h)

## 汇总

支持设备PhonePC/2in1TabletTVWearable 

### 成员变量

 支持设备PhonePC/2in1TabletTVWearable展开

| 名称 | 描述 |
| --- | --- |
| char *key | 请求或者响应的标头中的键。 |
| Http_HeaderValue *value | 请求或者响应的标头中的键对应的值，参考 Http_HeaderValue 。 |
| struct Http_HeaderEntry *next | 链式存储。指向下一个Http_HeaderEntry。 |