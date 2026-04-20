# FIDO2_AuthenticatorMetadata

  

#### 概述

认证器元数据。

 

**起始版本：** 6.0.0(20)

 

**相关模块：** [FIDO2](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/passkey)

  

#### 汇总

 

#### [h2]成员变量

 

| 名称 | 描述 |
| --- | --- |
| Uint8Buff aaguid | 认证器的aaguid。 |
| FIDO2_Uvm uvm | 支持的认证器类型。 |
| bool isAvailable | 认证器是否可用。 |

   

#### 结构体成员变量说明

 

#### [h2]aaguid

```
Uint8Buff FIDO2_AuthenticatorMetadata::aaguid

```

 

**描述**

 

认证器的aaguid。

  

#### [h2]isAvailable

```
bool FIDO2_AuthenticatorMetadata::isAvailable

```

 

**描述**

 

认证器是否可用。如果返回true，则表示认证器可用；返回false，表示认证器不可用。

  

#### [h2]uvm

```
FIDO2_Uvm FIDO2_AuthenticatorMetadata::uvm

```

 

**描述**

 

支持的认证器类型。