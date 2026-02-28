## 概述

支持设备PhonePC/2in1TabletTVWearable

[Rcp_FormFieldFileValue](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___form_field_file_value)中使用的简单表单数据字段值。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview)

## 汇总

支持设备PhonePC/2in1TabletTVWearable 

### 成员变量

 支持设备PhonePC/2in1TabletTVWearable展开

| 名称 | 描述 |
| --- | --- |
| Rcp_ContentOrPathOrCallbackType type | 表示union中使用的数据类型。 |
| union { | union结构。data中使用的数据由type进行区分。 |
| Rcp_Buffer content | content: 文本数据。 |
| char path [ RCP_MAX_PATH_LEN ] | path: 文件路径。 |
| Rcp_GetDataCallback callback | callback: 获取数据的回调函数。 |
| } data | data中使用的数据由type进行区分。 |

## 结构体成员变量说明

支持设备PhonePC/2in1TabletTVWearable 

### callback

支持设备PhonePC/2in1TabletTVWearable

```
Rcp_GetDataCallback Rcp_ContentOrPathOrCallback::callback
```

**描述**

获取数据的回调。

### content

支持设备PhonePC/2in1TabletTVWearable

```
Rcp_Buffer Rcp_ContentOrPathOrCallback::content
```

**描述**

文本数据。

### path

支持设备PhonePC/2in1TabletTVWearable

```
char Rcp_ContentOrPathOrCallback::path[ RCP_MAX_PATH_LEN ]
```

**描述**

文件路径。

### type

支持设备PhonePC/2in1TabletTVWearable

```
Rcp_ContentOrPathOrCallbackType Rcp_ContentOrPathOrCallback::type
```

**描述**

union中使用的数据类型。