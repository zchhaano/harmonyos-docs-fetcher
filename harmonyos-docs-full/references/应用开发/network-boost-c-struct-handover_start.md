## 概述

支持设备PhonePC/2in1Tablet

连接迁移开始信息。

**起始版本：** 5.1.0(18)

**相关模块：** [NetworkBoost](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-boost-c-overview)

## 汇总

支持设备PhonePC/2in1Tablet 

### 成员变量

 支持设备PhonePC/2in1Tablet展开

| 名称 | 描述 |
| --- | --- |
| uint32_t expires | 连接迁移全流程的超时时间，单位为s，取值为任意正整数或者0。 |
| NetworkBoost_DataSpeedAction dataSpeedAction | 老链路的发包建议。 |

## 结构体成员变量说明

支持设备PhonePC/2in1Tablet 

### dataSpeedAction

支持设备PhonePC/2in1Tablet

```
NetworkBoost_DataSpeedAction NetworkBoost_HandoverStart::dataSpeedAction
```

**描述**

老链路的发包建议。

### expires

支持设备PhonePC/2in1Tablet

```
uint32_t NetworkBoost_HandoverStart::expires
```

**描述**

连接迁移全流程的超时时间，单位为s，取值为任意正整数或者0。