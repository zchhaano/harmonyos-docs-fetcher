## 概述

支持设备PhoneTablet

此结构体描述创建超帧上下文实例[FG_Context_VK](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_graphics_accelerate#ga4022ab63c2296d63dcf2c2df178508b7)所需的属性信息。

**起始版本：** 5.0.0(12)

**相关模块：** [GraphicsAccelerate](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_graphics_accelerate)

## 汇总

支持设备PhoneTablet 

### 成员变量

 支持设备PhoneTablet展开

| 名称 | 描述 |
| --- | --- |
| VkInstance vkInstance | Vulkan实例，需在 FG_Context_VK 的整个生命周期内有效。 |
| VkPhysicalDevice vkPhysicalDevice | Vulkan物理设备句柄, 需在 FG_Context_VK 的整个生命周期内有效。 |
| VkDevice vkDevice | Vulkan逻辑设备句柄，需在 FG_Context_VK 的整个生命周期内有效。 |
| uint8_t framesInFlight | 设置并行渲染图像数。例如，如果下一帧图像需要等待上一帧图像送显后再进行渲染，则framesInFlight应设置为1；如果上一帧图像送显的同时，下一帧图像已经在进行渲染，则framesInFlight应设置为2。注意：framesInFlight不允许设置成0。 取值范围：[1, 2]。 |
| PFN_vkGetInstanceProcAddr fnVulkanLoaderFunction | 指向Vulkan的vkGetInstanceProcAddr的函数指针，不允许设置为空。 |

## 结构体成员变量说明

支持设备PhoneTablet 

### fnVulkanLoaderFunction

支持设备PhoneTablet

```
PFN_vkGetInstanceProcAddr FG_ContextDescription_VK::fnVulkanLoaderFunction
```

**描述**

指向Vulkan的vkGetInstanceProcAddr的函数指针，不允许设置为空。

### framesInFlight

支持设备PhoneTablet

```
uint8_t FG_ContextDescription_VK::framesInFlight
```

**描述**

设置并行渲染图像数。 例如，如果下一帧图像需要等待上一帧图像送显后再进行渲染，则framesInFlight应设置为1； 如果上一帧图像送显的同时，下一帧图像已经在进行渲染，则framesInFlight应设置为2。注意：framesInFlight不允许设置成0。

### vkDevice

支持设备PhoneTablet

```
VkDevice FG_ContextDescription_VK::vkDevice
```

**描述**

Vulkan逻辑设备句柄，需在[FG_Context_VK](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_graphics_accelerate#ga4022ab63c2296d63dcf2c2df178508b7)的整个生命周期内有效。

### vkInstance

支持设备PhoneTablet

```
VkInstance FG_ContextDescription_VK::vkInstance
```

**描述**

Vulkan实例, 需在[FG_Context_VK](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_graphics_accelerate#ga4022ab63c2296d63dcf2c2df178508b7)的整个生命周期内有效。

### vkPhysicalDevice

支持设备PhoneTablet

```
VkPhysicalDevice FG_ContextDescription_VK::vkPhysicalDevice
```

**描述**

Vulkan物理设备句柄, 需在[FG_Context_VK](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_graphics_accelerate#ga4022ab63c2296d63dcf2c2df178508b7)的整个生命周期内有效。