## 概述

支持设备PhonePC/2in1TabletTVWearable

描述请求的所有Cookie键值对。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview)

## 汇总

支持设备PhonePC/2in1TabletTVWearable 

### 成员变量

 支持设备PhonePC/2in1TabletTVWearable展开

| 名称 | 描述 |
| --- | --- |
| char * key | 请求Cookie键值对的键。 |
| char * value | 请求Cookie键值对的值。 |
| struct Rcp_RequestCookieEntry * next | 链式存储。指向下一个 Rcp_RequestCookieEntry 的指针。 |

## 结构体成员变量说明

支持设备PhonePC/2in1TabletTVWearable 

### key

支持设备PhonePC/2in1TabletTVWearable

```
char* Rcp_RequestCookieEntry::key
```

**描述**

请求Cookie键值对的键。

### next

支持设备PhonePC/2in1TabletTVWearable

```
struct Rcp_RequestCookieEntry * Rcp_RequestCookieEntry::next
```

**描述**

链式存储。指向下一个[Rcp_RequestCookieEntry](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___request_cookie_entry)的指针。

### value

支持设备PhonePC/2in1TabletTVWearable

```
char* Rcp_RequestCookieEntry::value
```

**描述**

请求Cookie键值对的值。