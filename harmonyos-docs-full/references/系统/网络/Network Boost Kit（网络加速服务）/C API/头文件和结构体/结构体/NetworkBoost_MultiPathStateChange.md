## 概述

支持设备PhonePC/2in1Tablet

多网状态信息，用于注册多网状态变化事件回调后，系统多网状态发生变化的事件通知。

**起始版本：** 6.0.2(22)

**相关模块：** [NetworkBoost](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-boost-c-overview)

## 汇总

支持设备PhonePC/2in1Tablet 

### 成员变量

 支持设备PhonePC/2in1Tablet展开

| 名称 | 描述 |
| --- | --- |
| NetworkBoost_MultiPathState multiPathState | 多网状态。 |
| NetworkBoost_MultiPathChangeCause changeCause | 多网状态变化原因。 |
| NetworkBoost_NetHandle netHandle | 多网链路的netHandle。 |
| NetworkBoost_PathState pathState | 多网链路状态。 |
| NetworkBoost_PathType pathType | 多网链路类型。 |

## 结构体成员变量说明

支持设备PhonePC/2in1Tablet 

## multiPathState

支持设备PhonePC/2in1Tablet

```
NetworkBoost_MultiPathState NetworkBoost_MultiPathStateChange::multiPathState
```

**描述**

多网状态，可以通过该信息获取当前多网所处状态，包含空闲态、建立中、已建立和释放中四种状态。

## changeCause

支持设备PhonePC/2in1Tablet

```
NetworkBoost_MultiPathChangeCause NetworkBoost_MultiPathStateChange::changeCause
```

**描述**

多网状态变化原因，在多网状态发生变化时，通过该信息可以获取发生多网状态发生变化的原因。

## netHandle

支持设备PhonePC/2in1Tablet

```
NetworkBoost_NetHandle NetworkBoost_MultiPathStateChange::netHandle
```

**描述**

多网链路的netHandle。

## pathState

支持设备PhonePC/2in1Tablet

```
NetworkBoost_PathState NetworkBoost_MultiPathStateChange::pathState
```

**描述**

多网链路状态。

## pathType

支持设备PhonePC/2in1Tablet

```
NetworkBoost_PathType NetworkBoost_MultiPathStateChange::pathType
```

**描述**

多网链路类型。