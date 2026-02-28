## 概述

支持设备PhonePC/2in1TabletTVWearable

响应Cookie。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview)

## 汇总

支持设备PhonePC/2in1TabletTVWearable 

### 成员变量

 支持设备PhonePC/2in1TabletTVWearable展开

| 名称 | 描述 |
| --- | --- |
| char * name | 响应Cookie名称。 |
| char * value | 响应Cookie值。 |
| char * domain | 响应Cookie域属性。 |
| char * path | 响应Cookie路径属性。 |
| char * expires | 响应Cookie过期属性。 |
| uint64_t maxAge | 响应Cookie maxAge属性。 |
| bool secure | 响应Cookie安全属性。 |
| bool httpOnly | 响应Cookie httpOnly属性。 |
| char * sameSite | 响应Cookie sameSite属性。 |
| uint64_t rawSize | 此响应Cookie的原始大小。 |
| char * originString | 原始字符串。 |
| Rcp_CookieAttributes * cookieAttributes | 响应Cookie中的所有属性。 |
| struct Rcp_ResponseCookies * next | 链式存储。指向下一个 Rcp_ResponseCookies 的指针。 |

## 结构体成员变量说明

支持设备PhonePC/2in1TabletTVWearable 

### cookieAttributes

支持设备PhonePC/2in1TabletTVWearable

```
Rcp_CookieAttributes * Rcp_ResponseCookies::cookieAttributes
```

**描述**

响应Cookie中的所有属性。

### domain

支持设备PhonePC/2in1TabletTVWearable

```
char* Rcp_ResponseCookies::domain
```

**描述**

响应Cookie域属性。

### expires

支持设备PhonePC/2in1TabletTVWearable

```
char* Rcp_ResponseCookies::expires
```

**描述**

响应Cookie过期属性。

### httpOnly

支持设备PhonePC/2in1TabletTVWearable

```
bool Rcp_ResponseCookies::httpOnly
```

**描述**

响应Cookie httpOnly属性。

### maxAge

支持设备PhonePC/2in1TabletTVWearable

```
uint64_t Rcp_ResponseCookies::maxAge
```

**描述**

响应Cookie maxAge属性。

### name

支持设备PhonePC/2in1TabletTVWearable

```
char* Rcp_ResponseCookies::name
```

**描述**

响应Cookie名称。

### next

支持设备PhonePC/2in1TabletTVWearable

```
struct Rcp_ResponseCookies * Rcp_ResponseCookies::next
```

**描述**

链式存储。指向下一个[Rcp_ResponseCookies](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___response_cookies)的指针。

### originString

支持设备PhonePC/2in1TabletTVWearable

```
char* Rcp_ResponseCookies::originString
```

**描述**

原始字符串。

### path

支持设备PhonePC/2in1TabletTVWearable

```
char* Rcp_ResponseCookies::path
```

**描述**

响应Cookie路径属性。

### rawSize

支持设备PhonePC/2in1TabletTVWearable

```
uint64_t Rcp_ResponseCookies::rawSize
```

**描述**

此响应Cookie的原始大小。

### sameSite

支持设备PhonePC/2in1TabletTVWearable

```
char* Rcp_ResponseCookies::sameSite
```

**描述**

响应Cookie sameSite属性。

### secure

支持设备PhonePC/2in1TabletTVWearable

```
bool Rcp_ResponseCookies::secure
```

**描述**

响应Cookie安全属性。

### value

支持设备PhonePC/2in1TabletTVWearable

```
char* Rcp_ResponseCookies::value
```

**描述**

响应Cookie值。