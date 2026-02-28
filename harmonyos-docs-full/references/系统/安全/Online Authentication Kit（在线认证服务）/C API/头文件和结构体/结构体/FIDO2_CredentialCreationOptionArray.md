## 概述

支持设备PhonePC/2in1Tablet

认证凭据的附加参数数组。

**起始版本：** 6.0.0(20)

**相关模块：** [FIDO2](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/passkey)

## 汇总

支持设备PhonePC/2in1Tablet 

### 成员变量

 支持设备PhonePC/2in1Tablet展开

| 名称 | 描述 |
| --- | --- |
| uint32_t pubKeyCredParamNum | PubKeyCredParam参数数目。 |
| FIDO2_PublicKeyCredentialParameters * pubKeyCredParams | 认证凭据的附加参数。 |

## 结构体成员变量说明

支持设备PhonePC/2in1Tablet 

### pubKeyCredParamNum

支持设备PhonePC/2in1Tablet

```
uint32_t FIDO2_CredentialCreationOptionArray::pubKeyCredParamNum
```

**描述**

PubKeyCredParam参数数目。

### pubKeyCredParams

支持设备PhonePC/2in1Tablet

```
FIDO2_PublicKeyCredentialParameters * FIDO2_CredentialCreationOptionArray::pubKeyCredParams
```

**描述**

认证凭据的附加参数。