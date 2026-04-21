# FIDO2_AuthenticatorTransportArray

  

#### 概述

认证器传输方式数组。

 

**起始版本：** 6.0.0(20)

 

**相关模块：** [FIDO2](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/passkey)

  

#### 汇总

 

#### [h2]成员变量

 

| 名称 | 描述 |
| --- | --- |
| uint32_t transportNum | 传输方式数量。 |
| FIDO2_AuthenticatorTransport * transports | 定义身份认证器访问类型（USB、NFC、蓝牙）。 |

   

#### 结构体成员变量说明

 

#### [h2]transportNum

```
uint32_t FIDO2_AuthenticatorTransportArray::transportNum

```

 

**描述**

 

传输方式数量。

  

#### [h2]transports

```
FIDO2_AuthenticatorTransport* FIDO2_AuthenticatorTransportArray::transports

```

 

**描述**

 

定义身份认证器访问类型（USB、NFC、蓝牙）。