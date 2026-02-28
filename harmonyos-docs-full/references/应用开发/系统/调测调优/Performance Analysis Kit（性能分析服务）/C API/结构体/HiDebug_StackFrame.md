# HiDebug_StackFrame

收起自动换行深色代码主题复制

```
typedef struct HiDebug_StackFrame { ...} HiDebug_StackFrame
```

## 概述

支持设备PhonePC/2in1TabletTVWearable

栈帧内容的定义。

**起始版本：** 20

**相关模块：** [HiDebug](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidebug)

**所在头文件：** [hidebug_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidebug-type-h)

## 汇总

支持设备PhonePC/2in1TabletTVWearable 

### 成员变量

 支持设备PhonePC/2in1TabletTVWearable展开

| 名称 | 描述 |
| --- | --- |
| HiDebug_StackFrameType type | 当前栈的类型。 |
| struct HiDebug_JsStackFrame js | 由 HiDebug_JsStackFrame 定义的js栈帧内容。 |
| struct HiDebug_NativeStackFrame native | 由 HiDebug_NativeStackFrame 定义的native栈帧内容。 |