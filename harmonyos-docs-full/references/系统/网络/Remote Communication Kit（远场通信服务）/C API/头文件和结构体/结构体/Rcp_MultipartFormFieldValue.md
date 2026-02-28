## 概述

支持设备PhonePC/2in1TabletTVWearable

多部分表单域值，在[Rcp_MultipartForm](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview#ga9f974771548d3ed2054aba0e7506fef9)中使用。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview)

## 汇总

支持设备PhonePC/2in1TabletTVWearable 

### 成员变量

 支持设备PhonePC/2in1TabletTVWearable展开

| 名称 | 描述 |
| --- | --- |
| Rcp_MultipartValueType type | 表示union中使用的数据类型。 |
| union { | union结构。 |
| Rcp_FormFieldValue formValue | 简单表单数据字段值。 |
| Rcp_FormFieldFileValue formFileValue | 简单表单数据字段文件值。 |
| } data | data中使用的数据由type进行区分。 |
| struct Rcp_MultipartFormFieldValue * next | 指向下一个 Rcp_MultipartFormFieldValue 。链式存储。 |

## 结构体成员变量说明

支持设备PhonePC/2in1TabletTVWearable 

### formFileValue

支持设备PhonePC/2in1TabletTVWearable收起自动换行深色代码主题复制

```
Rcp_FormFieldFileValue Rcp_MultipartFormFieldValue::formFileValue
```

**描述**

简单表单数据字段文件值。

### formValue

支持设备PhonePC/2in1TabletTVWearable收起自动换行深色代码主题复制

```
Rcp_FormFieldValue Rcp_MultipartFormFieldValue::formValue
```

**描述**

简单表单数据字段值。

### next

支持设备PhonePC/2in1TabletTVWearable收起自动换行深色代码主题复制

```
struct Rcp_MultipartFormFieldValue * Rcp_MultipartFormFieldValue::next
```

**描述**

指向下一个[Rcp_MultipartFormFieldValue](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___multipart_form_field_value)。链式存储。

### type

支持设备PhonePC/2in1TabletTVWearable收起自动换行深色代码主题复制

```
Rcp_MultipartValueType Rcp_MultipartFormFieldValue:: type
```

**描述**

表示union中使用的数据类型。