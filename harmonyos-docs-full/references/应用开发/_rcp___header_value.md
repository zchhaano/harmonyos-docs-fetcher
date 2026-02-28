## 概述

支持设备PhonePC/2in1TabletTVWearable

请求或响应的标头映射的值类型。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview)

## 汇总

支持设备PhonePC/2in1TabletTVWearable 

### 成员变量

 支持设备PhonePC/2in1TabletTVWearable展开

| 名称 | 描述 |
| --- | --- |
| char * value | 标头键值对的值。 |
| struct Rcp_HeaderValue * next | 链式存储。指向下一个 Rcp_HeaderValue 。 |

## 结构体成员变量说明

支持设备PhonePC/2in1TabletTVWearable 

### next

支持设备PhonePC/2in1TabletTVWearable

```
struct Rcp_HeaderValue * Rcp_HeaderValue::next
```

**描述**

链式存储。指向下一个[Rcp_HeaderValue](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___header_value)。

### value

支持设备PhonePC/2in1TabletTVWearable

```
char* Rcp_HeaderValue::value
```

**描述**

值。