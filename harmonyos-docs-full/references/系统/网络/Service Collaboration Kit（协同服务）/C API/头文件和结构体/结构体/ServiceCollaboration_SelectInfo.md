## 概述

支持设备PhonePC/2in1TabletTV

使用[HMS_ServiceCollaboration_StartCollaboration](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/servicecollaboration-capi-module#section4531193410296)触发跨设备互通时，被选择的设备信息。

**起始版本：** 5.0.0(12)

**相关模块：** [ServiceCollaboration](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/servicecollaboration-capi-module)

## 汇总

支持设备PhonePC/2in1TabletTV 

### 成员变量

 支持设备PhonePC/2in1TabletTV展开

| 名称 | 描述 |
| --- | --- |
| ServiceCollaborationFilterType serviceFilterType | 开发者期望的设备能力类型。 |
| char deviceNetworkId [ COLLABORATIONDEVICEINFO_DEVICENETWORKID_MAXLENGTH ] | 被选择的设备network Id。 |
| uint32_t maxSize | 能被选中的最大图片数量。 |

## 结构体成员变量说明

支持设备PhonePC/2in1TabletTV 

### deviceNetworkId

支持设备PhonePC/2in1TabletTV

```
char ServiceCollaboration_SelectInfo::deviceNetworkId[ COLLABORATIONDEVICEINFO_DEVICENETWORKID_MAXLENGTH ]
```

**描述**

被选择的设备network Id。

### maxSize

支持设备PhonePC/2in1TabletTV

```
uint32_t ServiceCollaboration_SelectInfo::maxSize
```

**描述**

能被选中的最大图片数量。

### serviceFilterType

支持设备PhonePC/2in1TabletTV

```
ServiceCollaborationFilterType ServiceCollaboration_SelectInfo::serviceFilterType
```

**描述**

开发者期望的设备能力类型。