## 概述

支持设备PhonePC/2in1TabletTVWearable

表单字段文件值。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview)

## 汇总

支持设备PhonePC/2in1TabletTVWearable 

### 成员变量

 支持设备PhonePC/2in1TabletTVWearable展开

| 名称 | 描述 |
| --- | --- |
| char contentType [ RCP_MAX_CONTENT_TYPE_LEN ] | 多部分表单数据内容类型。 |
| char remoteFileName [ RCP_MAX_FILENAME_LEN ] | 多部分表单数据远程文件名。 |
| Rcp_ContentOrPathOrCallback contentOrPathOrCb | 多部分表单数据内容。 |

## 结构体成员变量说明

支持设备PhonePC/2in1TabletTVWearable 

### contentOrPathOrCb

支持设备PhonePC/2in1TabletTVWearable

```
Rcp_ContentOrPathOrCallback Rcp_FormFieldFileValue::contentOrPathOrCb
```

**描述**

多部分表单数据内容。

### contentType

支持设备PhonePC/2in1TabletTVWearable

```
char Rcp_FormFieldFileValue::contentType[ RCP_MAX_CONTENT_TYPE_LEN ]
```

**描述**

多部分表单数据内容类型。

### remoteFileName

支持设备PhonePC/2in1TabletTVWearable

```
char Rcp_FormFieldFileValue::remoteFileName[ RCP_MAX_FILENAME_LEN ]
```

**描述**

多部分表单数据远程文件名。