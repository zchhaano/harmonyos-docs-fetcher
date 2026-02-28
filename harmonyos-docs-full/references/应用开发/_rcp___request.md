## 概述

支持设备PhonePC/2in1TabletTVWearable

网络请求。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview)

## 汇总

支持设备PhonePC/2in1TabletTVWearable 

### 成员变量

 支持设备PhonePC/2in1TabletTVWearable展开

| 名称 | 描述 |
| --- | --- |
| char id [ RCP_MAX_REQUEST_ID_LEN ] | 每个请求的唯一ID。由系统生成。 |
| char * url | 请求URL。 |
| const char * method | 请求方法。默认值为GET。 |
| Rcp_Headers * headers | 请求标头。 |
| Rcp_RequestContent * content | 请求体。 |
| Rcp_Configuration * configuration | 请求配置。请参见 Rcp_Configuration 。 |
| Rcp_TransferRange * transferRange | HTTP传输范围。该设置将转换为HTTP Range标头。 |
| Rcp_RequestCookies * cookies | 请求Cookie。该设置将转换为HTTP Cookie标头。 |
| void * requestPrivate | 可扩展字段。 |

## 结构体成员变量说明

支持设备PhonePC/2in1TabletTVWearable 

### configuration

支持设备PhonePC/2in1TabletTVWearable

```
Rcp_Configuration * Rcp_Request::configuration
```

**描述**

请求配置。请参见[Rcp_Configuration](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___configuration)。

### content

支持设备PhonePC/2in1TabletTVWearable

```
Rcp_RequestContent * Rcp_Request::content
```

**描述**

请求体。

### cookies

支持设备PhonePC/2in1TabletTVWearable

```
Rcp_RequestCookies * Rcp_Request::cookies
```

**描述**

请求Cookie。该设置将转换为HTTP Cookie标头。

### headers

支持设备PhonePC/2in1TabletTVWearable

```
Rcp_Headers * Rcp_Request::headers
```

**描述**

请求标头。

### id

支持设备PhonePC/2in1TabletTVWearable

```
char Rcp_Request::id[ RCP_MAX_REQUEST_ID_LEN ]
```

**描述**

每个请求的唯一ID。由系统生成。

### method

支持设备PhonePC/2in1TabletTVWearable

```
const char* Rcp_Request::method
```

**描述**

请求方法。默认值为GET。

### requestPrivate

支持设备PhonePC/2in1TabletTVWearable

```
void* Rcp_Request::requestPrivate
```

**描述**

可扩展字段。

### transferRange

支持设备PhonePC/2in1TabletTVWearable

```
Rcp_TransferRange * Rcp_Request::transferRange
```

**描述**

HTTP传输范围。该设置将转换为HTTP Range标头。

### url

支持设备PhonePC/2in1TabletTVWearable

```
char* Rcp_Request::url
```

**描述**

请求URL。