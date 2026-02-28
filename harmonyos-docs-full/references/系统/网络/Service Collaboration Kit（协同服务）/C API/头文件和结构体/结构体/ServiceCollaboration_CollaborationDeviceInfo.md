## 概述

支持设备PhonePC/2in1TabletTV

跨设备互通获取的设备信息对象，包含设备的基本信息和能力类型。

**起始版本：** 5.0.0(12)

**相关模块：** [ServiceCollaboration](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/servicecollaboration-capi-module)

## 汇总

支持设备PhonePC/2in1TabletTV 

### 成员变量

 支持设备PhonePC/2in1TabletTV展开

| 名称 | 描述 |
| --- | --- |
| uint32_t deviceType | 对端设备类型。只有手机或者平板。手机设备类型的值为0x14，平板设备类型的值为0x17。 |
| char deviceNetworkId [ COLLABORATIONDEVICEINFO_DEVICENETWORKID_MAXLENGTH ] | 对端设备network Id。 |
| char deviceName [ COLLABORATIONDEVICEINFO_DEVICENAME_MAXLENGTH ] | 对端设备名。 |
| uint32_t filterNum | 对端设备支持的能力类型列表的大小。 |
| ServiceCollaborationFilterType * serviceFilterTypes | 对端设备支持的能力类型列表。 |

## 结构体成员变量说明

支持设备PhonePC/2in1TabletTV 

### deviceName

支持设备PhonePC/2in1TabletTV

```
char ServiceCollaboration_CollaborationDeviceInfo::deviceName[ COLLABORATIONDEVICEINFO_DEVICENAME_MAXLENGTH ]
```

**描述**

对端设备名。

### deviceNetworkId

支持设备PhonePC/2in1TabletTV

```
char ServiceCollaboration_CollaborationDeviceInfo::deviceNetworkId[ COLLABORATIONDEVICEINFO_DEVICENETWORKID_MAXLENGTH ]
```

**描述**

对端设备network Id。

### deviceType

支持设备PhonePC/2in1TabletTV

```
uint32_t ServiceCollaboration_CollaborationDeviceInfo::deviceType
```

**描述**

对端设备类型。只有手机或者平板。手机设备类型的值为0x14，平板设备类型的值为0x17。

### filterNum

支持设备PhonePC/2in1TabletTV

```
uint32_t ServiceCollaboration_CollaborationDeviceInfo::filterNum
```

**描述**

对端设备支持的能力类型列表的大小。

### serviceFilterTypes

支持设备PhonePC/2in1TabletTV

```
ServiceCollaborationFilterType * ServiceCollaboration_CollaborationDeviceInfo::serviceFilterTypes
```

**描述**

对端设备支持的能力类型列表。