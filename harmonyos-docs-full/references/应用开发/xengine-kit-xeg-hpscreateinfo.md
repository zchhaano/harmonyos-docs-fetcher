## 概述

支持设备PhonePC/2in1TabletTV

此结构体描述创建[XEG_HPS](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xengine#xeg_hps)对象的信息。

**起始版本：** 6.0.0(20)

**相关模块：**[XEngine](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xengine)

**所在头文件：**[xeg_vulkan_hps.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-vulkan-hps-8h)

## 汇总

支持设备PhonePC/2in1TabletTV 

### 成员变量

 支持设备PhonePC/2in1TabletTV展开

| 名称 | 描述 |
| --- | --- |
| XEG_StructureType sType | 识别此结构的 XEG_StructureType 值，必须是XEG_STRUCTURE_TYPE_HPS_CREATE_INFO。 |
| const void * pNext | 指向扩展结构的指针，不允许为空。表示启用的XEngine HPS扩展，如当使用 XEG_HPS_RADIX_SORT_EXTENSION_NAME 扩展时，必须指定为 XEG_HPSRadixSort 。 |

## 结构体成员变量说明

支持设备PhonePC/2in1TabletTV 

### pNext

支持设备PhonePC/2in1TabletTV

```
const void* XEG_HPSCreateInfo::pNext
```

**描述**

指向扩展结构的指针，不允许为空。表示启用的XEngine HPS扩展，如当使用[XEG_HPS_RADIX_SORT_EXTENSION_NAME](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xengine#xeg_hps_radix_sort_extension_name)扩展时，必须指定为[XEG_HPSRadixSort](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-hpsradixsort)。

### sType

支持设备PhonePC/2in1TabletTV

```
XEG_StructureType XEG_HPSCreateInfo::sType
```

**描述**

识别此结构的[XEG_StructureType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xengine#xeg_structuretype)值，必须是XEG_STRUCTURE_TYPE_HPS_CREATE_INFO。