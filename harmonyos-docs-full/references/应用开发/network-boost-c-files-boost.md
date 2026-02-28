## 概述

支持设备PhonePC/2in1Tablet

声明用于网络加速的API。提供基本的函数、结构体和const定义。

**库：** libnetwork_boost.so

**系统能力：** SystemCapability.Communication.NetworkBoost.Core

**起始版本：** 6.0.2(22)

**相关模块：** [NetworkBoost](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-boost-c-overview)

## 汇总

支持设备PhonePC/2in1Tablet 

## 结构体

 支持设备PhonePC/2in1Tablet展开

| 名称 | 描述 |
| --- | --- |
| struct NetworkBoost_SceneDesc | 业务场景描述信息。 |

## 枚举

 支持设备PhonePC/2in1Tablet展开

| 名称 | 描述 |
| --- | --- |
| struct NetworkBoost_SceneEvent { SCENE_EVENT_ENTER = 0, SCENE_EVENT_UPDATE = 1, SCENE_EVENT_LEAVE = 2 } | 业务事件枚举。 |

## 函数

 支持设备PhonePC/2in1Tablet展开

| 名称 | 描述 |
| --- | --- |
| int32_t HMS_NetworkBoost_SetSceneDesc ( NetworkBoost_SceneDesc sceneDesc) | 设置业务场景。 |