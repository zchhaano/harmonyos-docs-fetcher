## 概述

支持设备PhonePC/2in1TabletTVWearable

简单表单数据字段值，参见[Rcp_Form](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview#ga40787f67faf4ea7111e4cda03f3f16be)和[Rcp_MultipartFormFieldValue](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___multipart_form_field_value)。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview)

## 汇总

支持设备PhonePC/2in1TabletTVWearable 

### 成员变量

 支持设备PhonePC/2in1TabletTVWearable展开

| 名称 | 描述 |
| --- | --- |
| Rcp_FormValueType type | 表示union中使用的数据类型。 |
| union { | union结构。 |
| uint8_t varBool | bool类型。 |
| int32_t varInt32 | int32类型。 |
| int64_t varInt64 | int64类型。 |
| double varDouble | double类型。 |
| Rcp_Buffer varStr | string类型。 |
| } data | data中使用的数据由type进行区分。 |
| struct Rcp_FormFieldValue * next | 指向下一个 Rcp_FormFieldValue 。链式存储。 |

## 结构体成员变量说明

支持设备PhonePC/2in1TabletTVWearable 

### next

支持设备PhonePC/2in1TabletTVWearable

```
struct Rcp_FormFieldValue * Rcp_FormFieldValue::next
```

**描述**

指向下一个[Rcp_FormFieldValue](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___form_field_value)。链式存储。

### type

支持设备PhonePC/2in1TabletTVWearable

```
Rcp_FormValueType Rcp_FormFieldValue::type
```

**描述**

表示union中使用的数据类型。

### varBool

支持设备PhonePC/2in1TabletTVWearable

```
uint8_t Rcp_FormFieldValue::varBool
```

**描述**

bool。

### varDouble

支持设备PhonePC/2in1TabletTVWearable

```
double Rcp_FormFieldValue::varDouble
```

**描述**

double。

### varInt32

支持设备PhonePC/2in1TabletTVWearable

```
int32_t Rcp_FormFieldValue::varInt32
```

**描述**

int32。

### varInt64

支持设备PhonePC/2in1TabletTVWearable

```
int64_t Rcp_FormFieldValue::varInt64
```

**描述**

int64。

### varStr

支持设备PhonePC/2in1TabletTVWearable

```
Rcp_Buffer Rcp_FormFieldValue::varStr
```

**描述**

string。