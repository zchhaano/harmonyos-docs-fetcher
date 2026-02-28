## 概述

支持设备PhonePC/2in1Tablet

描述支持的认证器数组。

**起始版本：** 6.0.0(20)

**相关模块：** [FIDO2](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/passkey)

## 汇总

支持设备PhonePC/2in1Tablet 

### 成员变量

 支持设备PhonePC/2in1Tablet展开

| 名称 | 描述 |
| --- | --- |
| uint32_t number | 认证器数目。 |
| FIDO2_AuthenticatorMetadata * authenticators | 认证器支持的扩展。 |

## 结构体成员变量说明

支持设备PhonePC/2in1Tablet 

### authenticators

支持设备PhonePC/2in1Tablet

```
FIDO2_AuthenticatorMetadata * FIDO2_AuthenticatorMetadataArray::authenticators
```

**描述**

认证器支持的扩展。

### number

支持设备PhonePC/2in1Tablet

```
uint32_t FIDO2_AuthenticatorMetadataArray::number
```

**描述**

认证器数目。