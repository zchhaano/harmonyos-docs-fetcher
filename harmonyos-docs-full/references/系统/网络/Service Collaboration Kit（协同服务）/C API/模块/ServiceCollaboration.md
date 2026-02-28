## 概述

支持设备PhonePC/2in1TabletTV

提供ServiceCollaboration跨设备互通的相关NDK接口。

**系统能力：** SystemCapability.Collaboration.Service

**起始版本：** 5.0.0(12)

## 汇总

支持设备PhonePC/2in1TabletTV 

### 文件

 支持设备PhonePC/2in1TabletTV展开

| 名称 | 描述 |
| --- | --- |
| service_collaboration_api.h | 跨设备互通的接口以及相关类型的定义。 |

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
| ServiceCollaboration_CollaborationDeviceInfoSets * HMS_ServiceCollaboration_GetCollaborationDeviceInfos ( uint32_t fileterNum, ServiceCollaborationFilterType serviceFileterTypes[]) | 获取支持相关能力的设备列表。 |
| uint32_t HMS_ServiceCollaboration_StartCollaboration ( const ServiceCollaboration_SelectInfo * selectService, ServiceCollaborationCallback * callback) | 拉起跨设备互通能力。 |
| int32_t HMS_ServiceCollaboration_StopCollaboration (uint32_t collaborationId) | 取消跨设备互通能力。 |

## 宏定义说明

支持设备PhonePC/2in1TabletTV 

### COLLABORATIONDEVICEINFO_DEVICENETWORKID_MAXLENGTH

支持设备PhonePC/2in1TabletTV收起自动换行深色代码主题复制

```
# define COLLABORATIONDEVICEINFO_DEVICENETWORKID_MAXLENGTH   65
```

**描述**

设备network Id最大长度。

**起始版本：** 5.0.0(12)

### COLLABORATIONDEVICEINFO_DEVICENAME_MAXLENGTH

支持设备PhonePC/2in1TabletTV收起自动换行深色代码主题复制

```
# define COLLABORATIONDEVICEINFO_DEVICENAME_MAXLENGTH   128
```

**描述**

设备名最大长度。

**起始版本：** 5.0.0(12)

## 类型定义说明

支持设备PhonePC/2in1TabletTV 

### ServiceCollaboration_CollaborationDeviceInfo

支持设备PhonePC/2in1TabletTV收起自动换行深色代码主题复制

```
typedef struct ServiceCollaboration_CollaborationDeviceInfo ServiceCollaboration_CollaborationDeviceInfo
```

**描述**

设备信息对象。

**起始版本：**5.0.0(12)

### ServiceCollaboration_CollaborationDeviceInfoSets

支持设备PhonePC/2in1TabletTV收起自动换行深色代码主题复制

```
typedef struct ServiceCollaboration_CollaborationDeviceInfoSets ServiceCollaboration_CollaborationDeviceInfoSets
```

**描述**

设备信息对象集合。

**起始版本：**5.0.0(12)

### ServiceCollaboration_SelectInfo

支持设备PhonePC/2in1TabletTV收起自动换行深色代码主题复制

```
typedef struct ServiceCollaboration_SelectInfo ServiceCollaboration_SelectInfo
```

**描述**

被选择的设备信息。

**起始版本：**5.0.0(12)

### ServiceCollaborationCallback

支持设备PhonePC/2in1TabletTV收起自动换行深色代码主题复制

```
typedef struct ServiceCollaborationCallback ServiceCollaborationCallback
```

**描述**

回调跨设备互通状态信息。

**起始版本：**5.0.0(12)

### ServiceCollaborationFilterType

支持设备PhonePC/2in1TabletTV收起自动换行深色代码主题复制

```
typedef enum ServiceCollaborationFilterType ServiceCollaborationFilterType
```

**描述**

跨设备互通能力类型的枚举。

**起始版本：** 5.0.0(12)

### ServiceCollaborationDataType

支持设备PhonePC/2in1TabletTV收起自动换行深色代码主题复制

```
typedef enum ServiceCollaborationDataType ServiceCollaborationDataType
```

**描述**

回传数据类型。

**起始版本：** 5.0.0(12)

### ServiceCollaborationEventCode

支持设备PhonePC/2in1TabletTV收起自动换行深色代码主题复制

```
typedef enum ServiceCollaborationEventCode ServiceCollaborationEventCode
```

**描述**

错误码枚举。

**起始版本：** 5.0.0(12)

## 枚举定义说明

支持设备PhonePC/2in1TabletTV 

### ServiceCollaborationFilterType

支持设备PhonePC/2in1TabletTV收起自动换行深色代码主题复制

```
enum ServiceCollaborationFilterType
```

**描述**

跨设备互通能力类型枚举。

**起始版本：**5.0.0(12)

 展开

| 枚举值 | 描述 |
| --- | --- |
| TAKE_PHOTO = 1 | 拍照。 |
| SCAN_DOCUMENT = 2 | 扫描。 |
| IMAGE_PICKER = 3 | 从图库中选择。 |

### ServiceCollaborationDataType

支持设备PhonePC/2in1TabletTV收起自动换行深色代码主题复制

```
enum ServiceCollaborationDataType
```

**描述**

回传数据类型。

**起始版本：**5.0.0(12)

 展开

| 枚举值 | 描述 |
| --- | --- |
| IMAGE = 1 | 图片。 |

### ServiceCollaborationEventCode

支持设备PhonePC/2in1TabletTV收起自动换行深色代码主题复制

```
enum ServiceCollaborationEventCode
```

**描述**

错误码枚举。

**起始版本：**5.0.0(12)

 展开

| 枚举值 | 描述 |
| --- | --- |
| LAST_DATA_BACK = 1001202000 | 已收到最后一个数据包。 |
| PEER_CANCEL = 1001202001 | 对端取消。 |
| NETWORK_ERROR = 1001202002 | 网络异常。 |
| PEER_WIFI_NOT_OPEN = 1001202004 | 对端WLAN未开启。 |
| LOCAL_WIFI_NOT_OPEN = 1001202005 | 本端WLAN未开启。 |
| DATA_BACK_START = 1001202006 | 开始回传数据。 |
| MIDDLE_DATA_BACK = 1001202007 | 收到中间数据。 |
| TIMEOUT_AUTO_CANCEL = 1001202008 | 接收数据超时取消。 |
| DATA_READ_FAILED = 1001202009 | 数据读取失败。 |
| LINK_SHUTDOWN = 1001202011 | 链路断开。 |
| REMOTE_HOTSPOT_CONFLICT = 1001202013 | 由于对端开启热点产生了链路冲突。 起始版本： 5.1.0(18) |
| REMOTE_DISTRIBUTED_SERVICES_CONFLICT = 1001202014 | 由于对端设备正在与其他设备进行互联而产生了链路冲突。 起始版本： 5.1.0(18) |

## 函数说明

支持设备PhonePC/2in1TabletTV 

### HMS_ServiceCollaboration_GetCollaborationDeviceInfos

支持设备PhonePC/2in1TabletTV收起自动换行深色代码主题复制

```
ServiceCollaboration_CollaborationDeviceInfoSets * HMS_ServiceCollaboration_GetCollaborationDeviceInfos ( uint32_t fileterNum, ServiceCollaborationFilterType serviceFileterTypes[]) ;
```

**描述**

获取支持相关能力的设备列表。

**起始版本：** 5.0.0(12)

**参数:**

 展开

| 名称 | 描述 |
| --- | --- |
| uint32_t fileterNum | 服务能力类型总数。 |
| ServiceCollaborationFilterType serviceFileterTypes[] | 具体需要的服务能力类型的数组。 |

**返回：**

返回[ServiceCollaboration_CollaborationDeviceInfoSets](/consumer/cn/doc/harmonyos-references/servicecollaboration-capi-module#section121718545319)，设备信息对象集合。

### HMS_ServiceCollaboration_StartCollaboration

支持设备PhonePC/2in1TabletTV收起自动换行深色代码主题复制

```
uint32_t HMS_ServiceCollaboration_StartCollaboration ( const ServiceCollaboration_SelectInfo * selectService, ServiceCollaborationCallback * callback) ;
```

**描述**

拉起跨设备互通能力。

**起始版本：** 5.0.0(12)

**参数:**

 展开

| 名称 | 描述 |
| --- | --- |
| const ServiceCollaboration_SelectInfo * selectService | 选择需要拉起的服务能力类型。 |
| ServiceCollaborationCallback * callback | 回调。 |

**返回：**

返回uint32_t的collaborationId，本次跨设备互通唯一标识。

### HMS_ServiceCollaboration_StopCollaboration

支持设备PhonePC/2in1TabletTV收起自动换行深色代码主题复制

```
int32_t HMS_ServiceCollaboration_StopCollaboration ( uint32_t collaborationId) ;
```

**描述**

取消跨设备互通能力。

**起始版本：** 5.0.0(12)

**参数:**

 展开

| 名称 | 描述 |
| --- | --- |
| uint32_t collaborationId | 跨设备互通唯一标识。 |

**返回：**

返回stop结果，0为成功。