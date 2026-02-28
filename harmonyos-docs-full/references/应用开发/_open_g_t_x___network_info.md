## 概述

支持设备PhoneTablet

此结构体描述当前设备网络信息，游戏应用获取到网络信息后传递此参数。

**起始版本：** 5.0.0(12)

**相关模块：** [GraphicsAccelerate](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_graphics_accelerate)

## 汇总

支持设备PhoneTablet 

### 成员变量

 支持设备PhoneTablet展开

| 名称 | 描述 |
| --- | --- |
| OpenGTX_NetworkLatency networkLatency | 游戏中的网络延迟。 如果没有上下行时延，则设置为total（总时延）的值。将游戏总时延以0ms、50ms、100ms、150ms、200ms分为5个档位，当档位发生变化时，游戏应用通知OpenGTX。 |
| char* networkServerIP | 游戏服务器的IP地址，字符长度范围[1,256]。 |

## 结构体成员变量说明

支持设备PhoneTablet 

### networkLatency

支持设备PhoneTablet收起自动换行深色代码主题复制

```
OpenGTX_NetworkLatency OpenGTX_NetworkInfo::networkLatency
```

**描述**

游戏中的网络延迟。 如果没有上下行时延，则设置为total（总时延）的值。将游戏总时延以0ms、50ms、100ms、150ms、200ms分为5个档位，当档位发生变化时，游戏应用通知OpenGTX。

### networkServerIP

支持设备PhoneTablet收起自动换行深色代码主题复制

```
char * OpenGTX_NetworkInfo::networkServerIP
```

**描述**

游戏服务器的IP地址，字符长度范围[1,256]。