# ArkWeb_ProxyMethodWithResult

```
typedef struct {...} ArkWeb_ProxyMethodWithResult
```

## 概述

支持设备PhonePC/2in1TabletTVWearable

注入的Proxy方法通用结构体。

**起始版本：** 18

**相关模块：** [Web](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-web)

**所在头文件：** [arkweb_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkweb-type-h)

## 汇总

支持设备PhonePC/2in1TabletTVWearable 

### 成员变量

 支持设备PhonePC/2in1TabletTVWearable展开

| 名称 | 描述 |
| --- | --- |
| const char* methodName | 注入的方法名。 |
| ArkWeb_OnJavaScriptProxyCallbackWithResult callback | Proxy方法执行的回调。 |
| void* userData | 需要在回调中携带的自定义数据。 |