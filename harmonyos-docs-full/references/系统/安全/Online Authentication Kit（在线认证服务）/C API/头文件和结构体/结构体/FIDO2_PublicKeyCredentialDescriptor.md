## 概述

支持设备PhonePC/2in1Tablet

用于注册或认证凭据的参数。

**起始版本：** 6.0.0(20)

**相关模块：** [FIDO2](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/passkey)

## 汇总

支持设备PhonePC/2in1Tablet 

### 成员变量

 支持设备PhonePC/2in1Tablet展开

| 名称 | 描述 |
| --- | --- |
| FIDO2_PublicKeyCredentialType type | 凭证类型。 |
| Uint8Buff id | 凭据标识符。 |
| FIDO2_AuthenticatorTransportArray transports | 定义身份认证器访问类型（USB、NFC、蓝牙）。 |

## 结构体成员变量说明

支持设备PhonePC/2in1Tablet 

### id

支持设备PhonePC/2in1Tablet

```
Uint8Buff FIDO2_PublicKeyCredentialDescriptor::id
```

**描述**

凭据标识符。

### transports

支持设备PhonePC/2in1Tablet

```
FIDO2_AuthenticatorTransportArray FIDO2_PublicKeyCredentialDescriptor::transports
```

**描述**

定义身份认证器访问类型（USB、NFC、蓝牙）。

### type

支持设备PhonePC/2in1Tablet

```
FIDO2_PublicKeyCredentialType FIDO2_PublicKeyCredentialDescriptor::type
```

**描述**

凭证类型。