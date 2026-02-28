## 概述

支持设备PhonePC/2in1TabletTVWearable

发送到远程服务器的客户端证书，远程服务器将使用它来验证客户端的标识。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview)

## 汇总

支持设备PhonePC/2in1TabletTVWearable 

### 成员变量

 支持设备PhonePC/2in1TabletTVWearable展开

| 名称 | 描述 |
| --- | --- |
| char * content | 客户端证书内容。它应采用“PEM”、“DER”或“P12”格式。 |
| char * filePath | 客户端证书的路径。文件的格式应为“PEM”、“DER”或“P12”格式。 |
| char * key | 客户端证书私钥的文件名。 |
| char * keyPassword | 客户端证书私钥的密码。 |
| Rcp_CertType type | 客户端证书类型。 |

## 结构体成员变量说明

支持设备PhonePC/2in1TabletTVWearable 

### content

支持设备PhonePC/2in1TabletTVWearable

```
char* Rcp_ClientCertificate::content
```

**描述**

客户端证书内容。它应采用“PEM”、“DER”或“P12”格式。

### filePath

支持设备PhonePC/2in1TabletTVWearable

```
char* Rcp_ClientCertificate::filePath
```

**描述**

客户端证书的路径。文件的格式应为“PEM”、“DER”或“P12”格式。

### key

支持设备PhonePC/2in1TabletTVWearable

```
char* Rcp_ClientCertificate::key
```

**描述**

客户端证书私钥的文件名。

### keyPassword

支持设备PhonePC/2in1TabletTVWearable

```
char* Rcp_ClientCertificate::keyPassword
```

**描述**

客户端证书私钥的密码。

### type

支持设备PhonePC/2in1TabletTVWearable

```
Rcp_CertType Rcp_ClientCertificate::type
```

**描述**

客户端证书类型。