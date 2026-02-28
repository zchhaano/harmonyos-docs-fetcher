# NetConn_Route

```
typedef struct NetConn_Route {...} NetConn_Route
```

## 概述

支持设备PhonePC/2in1TabletTVWearable

路由配置信息。

**起始版本：** 11

**相关模块：** [NetConnection](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netconnection)

**所在头文件：** [net_connection_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-connection-type-h)

## 汇总

支持设备PhonePC/2in1TabletTVWearable 

### 成员变量

 支持设备PhonePC/2in1TabletTVWearable展开

| 名称 | 描述 |
| --- | --- |
| char iface [NETCONN_MAX_STR_LEN] | 网络接口 |
| NetConn_NetAddr destination | 目标地址 |
| NetConn_NetAddr gateway | 网关地址 |
| int32_t hasGateway | 是否存在网关 |
| int32_t isDefaultRoute | 是否是默认路由 |