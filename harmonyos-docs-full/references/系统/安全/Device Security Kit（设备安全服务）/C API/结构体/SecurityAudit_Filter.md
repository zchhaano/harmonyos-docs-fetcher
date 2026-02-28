## 概述

支持设备PC/2in1

提供过滤条件。

**起始版本：** 6.0.0(20)

**相关模块：** [SecurityAudit](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/devicesecurity-capi-securityaudit)

**所在头文件：** [security_audit.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/devicesecurity-capi-security-audit-8h)

## 汇总

支持设备PC/2in1 

### 成员变量

 支持设备PC/2in1展开

| 名称 | 描述 |
| --- | --- |
| bool isInclude | TRUE: 符合条件的事件被返回给客户端。 FALSE: 符合条件的事件不被返回给客户端。 |
| SecurityAudit_FilterType type | 过滤器类型。 |
| const char ** value | 事件的过滤器的值。 |
| uint64_t valueCount | 过滤器值的数量。 |

## 结构体成员变量说明

支持设备PC/2in1 

### isInclude

支持设备PC/2in1

```
bool SecurityAudit_Filter::isInclude
```

**描述**

TRUE: 符合条件的事件被返回给客户端。 FALSE: 符合条件的事件不被返回给客户端。

### type

支持设备PC/2in1

```
SecurityAudit_FilterType SecurityAudit_Filter::type
```

**描述**

过滤器类型。

### value

支持设备PC/2in1

```
const char** SecurityAudit_Filter::value
```

**描述**

事件的过滤器的值。

### valueCount

```
uint64_t SecurityAudit_Filter::valueCount
```

**描述**

过滤器值的数量。