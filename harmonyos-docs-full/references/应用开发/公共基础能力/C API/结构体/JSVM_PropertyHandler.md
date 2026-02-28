# JSVM_PropertyHandler

```
typedef struct {...} JSVM_PropertyHandler
```

## 概述

支持设备PhonePC/2in1TabletWearable

包含将class作为函数进行调用时所触发的回调函数的函数指针，以及访问实例对象属性时触发的回调函数的函数指针集。

**起始版本：** 18

**相关模块：** [JSVM](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm)

**所在头文件：** [jsvm_types.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-types-h)

## 汇总

支持设备PhonePC/2in1TabletWearable 

### 成员变量

 支持设备PhonePC/2in1TabletWearable展开

| 名称 | 描述 |
| --- | --- |
| JSVM_PropertyHandlerCfg propertyHandlerCfg | 访问实例对象属性触发相应的回调函数。 |
| JSVM_Callback callAsFunctionCallback | 实例对象作为函数调用将触发此回调。 |