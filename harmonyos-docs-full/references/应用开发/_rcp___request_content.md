## 概述

支持设备PhonePC/2in1TabletTVWearable

请求的内容。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview)

## 汇总

支持设备PhonePC/2in1TabletTVWearable 

### 成员变量

 支持设备PhonePC/2in1TabletTVWearable展开

| 名称 | 描述 |
| --- | --- |
| Rcp_ContentType type | 表示union中使用的数据类型。 |
| union { | union结构。data中使用的数据由type进行区分。 |
| Rcp_Buffer contentStr | contentStr：文本。 |
| Rcp_Form * form | form：表单。 |
| Rcp_MultipartForm * multipartForm | multipartForm：多部分表单。 |
| Rcp_GetDataCallback getDataCallback | getDataCallback：使用回调函数获取数据。 |
| } data | data中使用的数据由type进行区分。 |

## 结构体成员变量说明

支持设备PhonePC/2in1TabletTVWearable 

### contentStr

支持设备PhonePC/2in1TabletTVWearable

```
Rcp_Buffer Rcp_RequestContent::contentStr
```

**描述**

字符串内容。

### form

支持设备PhonePC/2in1TabletTVWearable

```
Rcp_Form * Rcp_RequestContent::form
```

**描述**

表单内容。

### getDataCallback

支持设备PhonePC/2in1TabletTVWearable

```
Rcp_GetDataCallback Rcp_RequestContent::getDataCallback
```

**描述**

回调函数。

### multipartForm

支持设备PhonePC/2in1TabletTVWearable

```
Rcp_MultipartForm * Rcp_RequestContent::multipartForm
```

**描述**

多部分表单内容。

### type

支持设备PhonePC/2in1TabletTVWearable

```
Rcp_ContentType Rcp_RequestContent::type
```

**描述**

表示union中使用的数据类型。