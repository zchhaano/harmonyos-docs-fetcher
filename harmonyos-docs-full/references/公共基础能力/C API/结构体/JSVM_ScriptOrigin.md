# JSVM_ScriptOrigin

```
typedef struct {...} JSVM_ScriptOrigin
```

## 概述

支持设备PhonePC/2in1TabletWearable

某段JavaScript代码的原始信息，如sourceMap路径、源文件名、源文件中的起始行/列号等。

**起始版本：** 12

**相关模块：** [JSVM](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm)

**所在头文件：** [jsvm_types.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-types-h)

## 汇总

支持设备PhonePC/2in1TabletWearable 

### 成员变量

 支持设备PhonePC/2in1TabletWearable展开

| 名称 | 描述 |
| --- | --- |
| const char* sourceMapUrl | Sourcemap 路径。 |
| const char* resourceName | 源文件名。 |
| size_t resourceLineOffset | 这段代码在源文件中的起始行号。 |
| size_t resourceColumnOffset | 这段代码在源文件中的起始列号。 |