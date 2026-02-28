## 概述

支持设备PhonePC/2in1TabletTV

XEngine 高性能着色器接口。使用此头文件中的接口前需要通过[HMS_XEG_EnumerateDeviceExtensionProperties](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xengine#hms_xeg_enumeratedeviceextensionproperties)接口查询[XEG_HPS_RADIX_SORT_EXTENSION_NAME](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xengine#xeg_hps_radix_sort_extension_name)扩展可用。

**引用文件**：<xengine/xeg_vulkan_hps.h>

**库：** libxengine.so

**系统能力：** SystemCapability.Graphic.XEngine

**起始版本：** 6.0.0(20)

**相关模块：** [XEngine](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xengine)

## 汇总

支持设备PhonePC/2in1TabletTV 

### 结构体

 支持设备PhonePC/2in1TabletTV展开

| 名称 | 描述 |
| --- | --- |
| struct XEG_HPSCreateInfo | 此结构体描述创建 XEG_HPS 对象的信息。 |
| struct XEG_HPSRadixSort | 此结构体描述HPS基数排序扩展结构信息。 |
| struct XEG_HPSRadixSortDescription | 此结构体描述使用 XEG_HPS_RADIX_SORT_EXTENSION_NAME 扩展进行排序时所需的信息。 |

### 类型定义

 支持设备PhonePC/2in1TabletTV展开

| 名称 | 描述 |
| --- | --- |
| VK_DEFINE_HANDLE( XEG_HPS ) | XEG_HPS 的句柄。 |
| typedef struct XEG_HPSCreateInfo XEG_HPSCreateInfo | 此结构体描述创建 XEG_HPS 对象的信息。 |
| typedef struct XEG_HPSRadixSort XEG_HPSRadixSort | 此结构体描述HPS基数排序扩展结构信息。 |
| typedef struct XEG_HPSRadixSortDescription XEG_HPSRadixSortDescription | 此结构体描述使用 XEG_HPS_RADIX_SORT_EXTENSION_NAME 扩展进行排序时所需的信息。 |
| typedef VkResult(VKAPI_PTR * PFN_HMS_XEG_CreateHPS ) (VkDevice device, const XEG_HPSCreateInfo *pCreateInfo, XEG_HPS *pHps) | 创建 XEG_HPS 对象的函数指针定义。 |
| typedef void(VKAPI_PTR * PFN_HMS_XEG_DestroyHPS ) ( XEG_HPS hps) | 销毁 XEG_HPS 对象的函数指针定义。 |
| typedef VkResult(VKAPI_PTR * PFN_HMS_XEG_CmdRadixSortHPS ) (VkCommandBuffer commandBuffer, XEG_HPS hps, const XEG_HPSRadixSortDescription *pDescription) | 录制HPS排序命令的函数指针定义，使用此接口前需要通过 HMS_XEG_EnumerateDeviceExtensionProperties 接口查询是否支持 XEG_HPS_RADIX_SORT_EXTENSION_NAME 扩展。 |

### 函数

 支持设备PhonePC/2in1TabletTV展开

| 名称 | 描述 |
| --- | --- |
| VKAPI_ATTR VkResult VKAPI_CALL HMS_XEG_CreateHPS (VkDevice device, const XEG_HPSCreateInfo *pCreateInfo, XEG_HPS *pHps) | 创建 XEG_HPS 对象。 |
| VKAPI_ATTR void VKAPI_CALL HMS_XEG_DestroyHPS ( XEG_HPS hps) | 销毁 XEG_HPS 对象。 |
| VKAPI_ATTR VkResult VKAPI_CALL HMS_XEG_CmdRadixSortHPS (VkCommandBuffer commandBuffer, XEG_HPS hps, const XEG_HPSRadixSortDescription *pDescription) | 录制HPS排序命令，使用此接口前需要通过 HMS_XEG_EnumerateDeviceExtensionProperties 接口查询是否支持 XEG_HPS_RADIX_SORT_EXTENSION_NAME 扩展。 |