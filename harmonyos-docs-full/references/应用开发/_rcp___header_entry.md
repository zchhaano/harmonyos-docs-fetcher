## 概述

支持设备PhonePC/2in1TabletTVWearable

请求或响应的标头的所有键值对。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview)

## 汇总

支持设备PhonePC/2in1TabletTVWearable 

### 成员变量

 支持设备PhonePC/2in1TabletTVWearable展开

| 名称 | 描述 |
| --- | --- |
| char * key | 键。如果用户希望使用自定义的content-type覆盖系统原有的content-type，键必须使用小写的“content-type”。 |
| Rcp_HeaderValue * value | 值。 |
| struct Rcp_HeaderEntry * next | 链式存储。指向下一个键值对 Rcp_HeaderEntry 。 |

## 结构体成员变量说明

支持设备PhonePC/2in1TabletTVWearable 

### key

支持设备PhonePC/2in1TabletTVWearable

```
char* Rcp_HeaderEntry::key
```

**描述**

键。如果用户希望使用自定义的content-type覆盖系统原有的content-type，键必须使用小写的“content-type”。

### next

支持设备PhonePC/2in1TabletTVWearable

```
struct Rcp_HeaderEntry * Rcp_HeaderEntry::next
```

**描述**

链式存储。指向下一个键值对[Rcp_HeaderEntry](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___header_entry)。

### value

支持设备PhonePC/2in1TabletTVWearable

```
Rcp_HeaderValue * Rcp_HeaderEntry::value
```

**描述**

标头键值对的值。