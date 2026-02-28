## 概述

支持设备PhoneTablet

此结构体描述超帧输入输出图像的分辨率。

**起始版本：** 5.0.0(12)

**相关模块：** [GraphicsAccelerate](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_graphics_accelerate)

## 汇总

支持设备PhoneTablet 

### 成员变量

 支持设备PhoneTablet展开

| 名称 | 描述 |
| --- | --- |
| FG_Dimension2D inputColorResolution | 真实渲染帧颜色缓冲区分辨率。 |
| FG_Dimension2D inputDepthStencilResolution | 真实渲染帧深度模板缓冲区分辨率。当设置成0时, 系统中会默认使用 inputColorResolution 作为真实帧深度模板缓冲区分辨率。 |
| FG_Dimension2D outputColorResolution | 预测帧缓冲区分辨率。当设置成0时, 系统中会默认使用 inputColorResolution 作为预测帧缓冲区分辨率。 |

## 结构体成员变量说明

支持设备PhoneTablet 

### inputColorResolution

支持设备PhoneTablet

```
FG_Dimension2D FG_ResolutionInfo::inputColorResolution
```

**描述**

真实渲染帧颜色缓冲区分辨率。

### inputDepthStencilResolution

支持设备PhoneTablet

```
FG_Dimension2D FG_ResolutionInfo::inputDepthStencilResolution
```

**描述**

真实渲染帧深度模板缓冲区分辨率。当设置成0时, 系统中会默认使用[inputColorResolution](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_g___resolution_info#af99a47a1f71f8c13d8f5dff8ac02d137)作为真实帧深度模板缓冲区分辨率。

### outputColorResolution

支持设备PhoneTablet

```
FG_Dimension2D FG_ResolutionInfo::outputColorResolution
```

**描述**

预测帧缓冲区分辨率。当设置成0时, 系统中会默认使用[inputColorResolution](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_g___resolution_info#af99a47a1f71f8c13d8f5dff8ac02d137)作为预测帧缓冲区分辨率。