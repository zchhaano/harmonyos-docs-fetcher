## 概述

支持设备PhonePC/2in1Tablet

认证器声明响应。

**起始版本：** 6.0.0(20)

**相关模块：** [FIDO2](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/passkey)

## 汇总

支持设备PhonePC/2in1Tablet 

### 成员变量

 支持设备PhonePC/2in1Tablet展开

| 名称 | 描述 |
| --- | --- |
| Uint8Buff attestationObject | 声明对象。 |
| Uint8Buff clientDataJson | 获取客户端数据，表示WebAuthn依赖方和客户端的上下文绑定，包含类型、挑战值及源等数据。 |
| Uint8Buff publicKey | publicKey凭证请求的选项，字节流。 |
| Uint8Buff authenticatorData | 认证器数据，字节流。 |
| FIDO2_Algorithm publicKeyAlgorithm | 密码算法。 |
| FIDO2_AuthenticatorTransportArray transports | 定义身份认证器访问类型（USB、NFC、蓝牙）。 |

## 结构体成员变量说明

支持设备PhonePC/2in1Tablet 

### attestationObject

支持设备PhonePC/2in1Tablet

```
Uint8Buff FIDO2_AuthenticatorAttestationResponse::attestationObject
```

**描述**

声明对象。

### authenticatorData

支持设备PhonePC/2in1Tablet

```
Uint8Buff FIDO2_AuthenticatorAttestationResponse::authenticatorData
```

**描述**

认证器数据，字节流。

### clientDataJson

支持设备PhonePC/2in1Tablet

```
Uint8Buff FIDO2_AuthenticatorAttestationResponse::clientDataJson
```

**描述**

获取客户端数据，表示WebAuthn依赖方和客户端的上下文绑定，包含类型、挑战值及源等数据。

### publicKey

支持设备PhonePC/2in1Tablet

```
Uint8Buff FIDO2_AuthenticatorAttestationResponse::publicKey
```

**描述**

publicKey凭证请求的选项，字节流。

### publicKeyAlgorithm

支持设备PhonePC/2in1Tablet

```
FIDO2_Algorithm FIDO2_AuthenticatorAttestationResponse::publicKeyAlgorithm
```

**描述**

密码算法。

### transports

支持设备PhonePC/2in1Tablet

```
FIDO2_AuthenticatorTransportArray FIDO2_AuthenticatorAttestationResponse::transports
```

**描述**

定义身份认证器访问类型（USB、NFC、蓝牙）。