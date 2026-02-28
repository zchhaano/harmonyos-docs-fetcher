## 概述

支持设备PhoneTablet

此结构体描述超帧输入输出图像的格式信息，该接口仅适配Vulkan图形API平台。

**起始版本：** 5.0.0(12)

**相关模块：** [GraphicsAccelerate](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_graphics_accelerate)

## 汇总

支持设备PhoneTablet 

### 成员变量

 支持设备PhoneTablet展开

| 名称 | 描述 |
| --- | --- |
| VkFormat inputColorFormat | 真实渲染帧颜色缓冲区图像格式。 |
| VkFormat inputDepthStencilFormat | 深度模板缓冲区图像格式。 |
| VkFormat outputColorFormat | 预测帧缓冲区图像格式。 |

## 结构体成员变量说明

支持设备PhoneTablet 

### inputColorFormat

支持设备PhoneTablet

```
VkFormat FG_ImageFormat_VK::inputColorFormat
```

**描述**

真实渲染帧颜色缓冲区图像格式。

### inputDepthStencilFormat

支持设备PhoneTablet

```
VkFormat FG_ImageFormat_VK::inputDepthStencilFormat
```

**描述**

深度模板缓冲区图像格式。

### outputColorFormat

支持设备PhoneTablet

```
VkFormat FG_ImageFormat_VK::outputColorFormat
```

**描述**

预测帧缓冲区图像格式。