## 概述

支持设备PhonePC/2in1TabletTVWearable

URLs，用于确定主机是否正在使用代理。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview)

## 汇总

支持设备PhonePC/2in1TabletTVWearable 

### 成员变量

 支持设备PhonePC/2in1TabletTVWearable展开

| 名称 | 描述 |
| --- | --- |
| const char * url | 匹配的URL。 |
| struct Rcp_Urls * next | 链式存储。指向下一个 Rcp_Urls 的指针。 |

## 结构体成员变量说明

支持设备PhonePC/2in1TabletTVWearable 

### next

支持设备PhonePC/2in1TabletTVWearable

```
struct Rcp_Urls * Rcp_Urls::next
```

**描述**

链式存储。指向下一个[Rcp_Urls](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___urls)的指针。

### url

支持设备PhonePC/2in1TabletTVWearable

```
const char* Rcp_Urls::url
```

**描述**

匹配的URL。