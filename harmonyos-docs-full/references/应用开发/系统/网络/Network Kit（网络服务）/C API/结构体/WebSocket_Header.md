# WebSocket_Header

```
struct WebSocket_Header {...}
```

## 概述

支持设备PhonePC/2in1TabletTVWearable

websocket客户端增加header头的链表节点。

**起始版本：** 11

**相关模块：** [netstack](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack)

**所在头文件：** [net_websocket_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-websocket-type-h)

## 汇总

支持设备PhonePC/2in1TabletTVWearable 

### 成员变量

 支持设备PhonePC/2in1TabletTVWearable展开

| 名称 | 描述 |
| --- | --- |
| const char *fieldName | Header头的字段名。 |
| const char *fieldValue | Header头的字段内容。 |
| struct WebSocket_Header *next | header头链表的next指针。 |