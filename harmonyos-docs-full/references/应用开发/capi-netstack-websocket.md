# WebSocket

```
struct WebSocket {...}
```

## 概述

支持设备PhonePC/2in1TabletTVWearable

webSocket客户端结构体。

**起始版本：** 11

**相关模块：** [netstack](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack)

**所在头文件：** [net_websocket_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-websocket-type-h)

## 汇总

支持设备PhonePC/2in1TabletTVWearable 

### 成员变量

 支持设备PhonePC/2in1TabletTVWearable展开

| 名称 | 描述 |
| --- | --- |
| WebSocket_OnOpenCallback onOpen | 客户端接收连接消息的回调指针。 |
| WebSocket_OnMessageCallback onMessage | 客户端接收消息的回调指针。 |
| WebSocket_OnErrorCallback onError | 客户端接收错误消息的回调指针。 |
| WebSocket_OnCloseCallback onClose | 客户端接收关闭消息的回调指针。 |
| WebSocket_RequestOptions requestOptions | 客户端建立连接请求内容。 |