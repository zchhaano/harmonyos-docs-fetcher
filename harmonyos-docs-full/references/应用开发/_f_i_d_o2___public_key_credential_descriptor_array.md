## 概述

支持设备PhonePC/2in1Tablet

PublicKey凭证描述符数组。

**起始版本：** 6.0.0(20)

**相关模块：** [FIDO2](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/passkey)

## 汇总

支持设备PhonePC/2in1Tablet 

### 成员变量

 支持设备PhonePC/2in1Tablet展开

| 名称 | 描述 |
| --- | --- |
| uint32_t allowCredentiallNum | 允许凭证数目。 |
| FIDO2_PublicKeyCredentialDescriptor * allowCredentials | 认证凭据的附加参数列表。默认值为[]。 |

## 结构体成员变量说明

支持设备PhonePC/2in1Tablet 

### allowCredentiallNum

支持设备PhonePC/2in1Tablet

```
uint32_t FIDO2_PublicKeyCredentialDescriptorArray::allowCredentiallNum
```

**描述**

允许凭证数目。

### allowCredentials

支持设备PhonePC/2in1Tablet

```
FIDO2_PublicKeyCredentialDescriptor * FIDO2_PublicKeyCredentialDescriptorArray::allowCredentials
```

**描述**

认证凭据的附加参数列表。默认值为[]。