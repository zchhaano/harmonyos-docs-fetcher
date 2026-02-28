## 概述

支持设备PhonePC/2in1Tablet

网络质量回调信息。

**起始版本：** 5.1.0(18)

**相关模块：** [NetworkBoost](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-boost-c-overview)

## 汇总

支持设备PhonePC/2in1Tablet 

### 成员变量

 支持设备PhonePC/2in1Tablet展开

| 名称 | 描述 |
| --- | --- |
| NetworkBoost_PathType pathType | 相应的数据路径上的网络质量信息。 |
| uint64_t linkUpBandwidth | 上行带宽信息，单位为bps。 |
| uint64_t linkDownBandwidth | 下行带宽信息，单位为bps。 |
| uint64_t linkUpRate | 上行速率，单位为bps。 |
| uint64_t linkDownRate | 下行速率，单位为bps。 |
| uint32_t rttMs | RTT时延，单位为ms，取值范围是任意正数。 |
| uint32_t linkUpBufferDelayMs | 上行发送空口缓冲时延，单位为ms，取值范围是任意正数。 |
| uint32_t linkUpBufferCongestionPercent | 上行发送空口缓冲时延占总缓冲时间的比例，取值范围[0, 100]。 |

## 结构体成员变量说明

支持设备PhonePC/2in1Tablet 

### linkDownBandwidth

支持设备PhonePC/2in1Tablet

```
uint64_t NetworkBoost_NetworkQos::linkDownBandwidth
```

**描述**

下行带宽信息，单位为bps。

### linkDownRate

支持设备PhonePC/2in1Tablet

```
uint64_t NetworkBoost_NetworkQos::linkDownRate
```

**描述**

下行速率，单位为bps。

### linkUpBandwidth

支持设备PhonePC/2in1Tablet

```
uint64_t NetworkBoost_NetworkQos::linkUpBandwidth
```

**描述**

上行带宽信息，单位为bps。

### linkUpBufferCongestionPercent

支持设备PhonePC/2in1Tablet

```
uint32_t NetworkBoost_NetworkQos::linkUpBufferCongestionPercent
```

**描述**

上行发送空口缓冲时延占总缓冲时间的比例，取值范围[0, 100]。

### linkUpBufferDelayMs

支持设备PhonePC/2in1Tablet

```
uint32_t NetworkBoost_NetworkQos::linkUpBufferDelayMs
```

**描述**

上行发送空口缓冲时延（单位ms），取值范围是任意正数。

### linkUpRate

支持设备PhonePC/2in1Tablet

```
uint64_t NetworkBoost_NetworkQos::linkUpRate
```

**描述**

上行速率，单位为bps。

### pathType

支持设备PhonePC/2in1Tablet

```
NetworkBoost_PathType NetworkBoost_NetworkQos::pathType
```

**描述**

相应的数据路径上的网络质量信息。

### rttMs

支持设备PhonePC/2in1Tablet

```
uint32_t NetworkBoost_NetworkQos::rttMs
```

**描述**

RTT时延（单位ms），取值范围是任意正数。