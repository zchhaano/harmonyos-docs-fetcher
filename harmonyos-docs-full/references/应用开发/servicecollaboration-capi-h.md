## 概述

支持设备PhonePC/2in1TabletTV

函数export定义的接口。

**库：**libservice_collaboration_ndk.z.so

**系统能力：** SystemCapability.Collaboration.Service

**起始版本：** 5.0.0(12)

**相关模块：**[ServiceCollaboration](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/servicecollaboration-capi-module)

## 汇总

支持设备PhonePC/2in1TabletTV 

### 结构体

 支持设备PhonePC/2in1TabletTV展开

| 名称 | 描述 |
| --- | --- |
| struct ServiceCollaboration_CollaborationDeviceInfo | 跨设备互通获取的设备信息对象，包含设备的基本信息和能力类型。 |
| struct ServiceCollaboration_CollaborationDeviceInfoSets | 通过 HMS_ServiceCollaboration_GetCollaborationDeviceInfos 获取的对端设备信息对象集合。 |
| struct ServiceCollaboration_SelectInfo | 使用 HMS_ServiceCollaboration_StartCollaboration 触发跨设备互通时，被选择的设备信息。 |
| struct ServiceCollaborationCallback | 传给 HMS_ServiceCollaboration_StartCollaboration 的回调方法。 |

### 宏定义

 支持设备PhonePC/2in1TabletTV展开

| 名称 | 描述 |
| --- | --- |
| COLLABORATIONDEVICEINFO_DEVICENETWORKID_MAXLENGTH 65 | 设备network Id最大长度。 |
| COLLABORATIONDEVICEINFO_DEVICENAME_MAXLENGTH 128 | 设备名最大长度。 |

### 类型定义

 支持设备PhonePC/2in1TabletTV展开

| 名称 | 描述 |
| --- | --- |
| typedef enum ServiceCollaborationFilterType ServiceCollaborationFilterType | 跨设备互通能力类型枚举。 |
| typedef enum ServiceCollaborationDataType ServiceCollaborationDataType | 回传数据类型。 |
| typedef enum ServiceCollaborationEventCode ServiceCollaborationEventCode | 错误码枚举。 |
| typedef struct ServiceCollaboration_CollaborationDeviceInfo ServiceCollaboration_CollaborationDeviceInfo | 设备信息对象。 |
| typedef struct ServiceCollaboration_CollaborationDeviceInfoSets ServiceCollaboration_CollaborationDeviceInfoSets | 设备信息对象集合。 |
| typedef struct ServiceCollaboration_SelectInfo ServiceCollaboration_SelectInfo | 被选择的设备信息。 |
| typedef struct ServiceCollaborationCallback ServiceCollaborationCallback | 回调跨设备互通状态信息。 |

### 枚举

 支持设备PhonePC/2in1TabletTV展开

| 名称 | 描述 |
| --- | --- |
| ServiceCollaborationFilterType { TAKE_PHOTO = 1, SCAN_DOCUMENT = 2, IMAGE_PICKER = 3 } | 跨设备互通能力类型的枚举。 |
| ServiceCollaborationDataType { IMAGE = 1 } | 回传数据类型。 |
| ServiceCollaborationEventCode { LAST_DATA_BACK = 1001202000, PEER_CANCEL = 1001202001, NETWORK_ERROR = 1001202002, PEER_WIFI_NOT_OPEN = 1001202004, LOCAL_WIFI_NOT_OPEN = 1001202005, DATA_BACK_START = 1001202006, MIDDLE_DATA_BACK = 1001202007, TIMEOUT_AUTO_CANCEL = 1001202008, DATA_READ_FAILED = 1001202009, LINK_SHUTDOWN = 1001202011, REMOTE_HOTSPOT_CONFLICT = 1001202013, REMOTE_DISTRIBUTED_SERVICES_CONFLICT = 1001202014 } | 错误码枚举。 |

### 函数

 支持设备PhonePC/2in1TabletTV展开

| 名称 | 描述 |
| --- | --- |
| ServiceCollaboration_CollaborationDeviceInfoSets * HMS_ServiceCollaboration_GetCollaborationDeviceInfos ( uint32_t fileterNum, ServiceCollaborationFilterType serviceFileterTypes[]); | 获取支持相关能力的设备列表。 |
| uint32_t HMS_ServiceCollaboration_StartCollaboration ( const ServiceCollaboration_SelectInfo * selectService, ServiceCollaborationCallback * callback) | 拉起跨设备互通能力。 |
| int32_t HMS_ServiceCollaboration_StopCollaboration (uint32_t collaborationId); | 取消跨设备互通能力。 |