## 概述

支持设备PhonePC/2in1TabletTVWearable

用于验证远程服务器标识的证书颁发机构（CA）。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview)

## 汇总

支持设备PhonePC/2in1TabletTVWearable 

### 成员变量

 支持设备PhonePC/2in1TabletTVWearable展开

| 名称 | 描述 |
| --- | --- |
| char * content | 用于验证对等的证书颁发机构证书捆绑包。应采用PEM格式。 |
| char * filePath | 用于验证对等方的证书颁发机构证书文件的路径。文件应为PEM格式。 |
| char * folderPath | 包含用于验证对等项的多个CA证书的目录的路径。 此目录中的文件应为PEM格式。 文件必须以主题名称的哈希和扩展名“.0”命名。 |

## 结构体成员变量说明

支持设备PhonePC/2in1TabletTVWearable 

### content

支持设备PhonePC/2in1TabletTVWearable收起自动换行深色代码主题复制

```
char * Rcp_CertificateAuthority::content
```

**描述**

用于验证对等的证书颁发机构证书捆绑包。它应采用PEM格式。

### filePath

支持设备PhonePC/2in1TabletTVWearable收起自动换行深色代码主题复制

```
char * Rcp_CertificateAuthority::filePath
```

**描述**

用于验证对等方的证书颁发机构证书文件的路径。文件应为PEM格式。

### folderPath

支持设备PhonePC/2in1TabletTVWearable收起自动换行深色代码主题复制

```
char * Rcp_CertificateAuthority::folderPath
```

**描述**

包含用于验证对等项的多个CA证书的目录的路径。 此目录中的文件应为PEM格式。

文件必须以主题名称的哈希和扩展名“.0”命名。