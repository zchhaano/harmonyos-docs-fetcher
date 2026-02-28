# ArkWeb_JavaScriptBridgeData

收起自动换行深色代码主题复制

```
typedef struct { ...} ArkWeb_JavaScriptBridgeData
```

## 概述

支持设备PhonePC/2in1TabletTVWearable

定义JavaScript Bridge数据的基础结构。

**起始版本：** 12

**相关模块：** [Web](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-web)

**所在头文件：** [arkweb_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkweb-type-h)

## 汇总

支持设备PhonePC/2in1TabletTVWearable 

### 成员变量

 支持设备PhonePC/2in1TabletTVWearable展开

| 名称 | 描述 |
| --- | --- |
| const uint8_t* buffer | 指向传输数据的指针。仅支持前端传入String和ArrayBuffer类型，其余类型会被json序列化后，以String类型传递。 |
| size_t size | 传输数据的长度。 |