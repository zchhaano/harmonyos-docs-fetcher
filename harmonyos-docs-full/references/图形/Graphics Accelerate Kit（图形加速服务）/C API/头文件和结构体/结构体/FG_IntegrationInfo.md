## 概述

支持设备PhoneTablet

此结构体描述超帧集成的信息。包括显示模式，是否需要额外缓存深度和颜色纹理，以及是否需要翻转颜色纹理。仅在[FG_PredictionMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_graphics_accelerate#gaea2169cd5ae4bf9e8a17dc58f33e8766)为FG_PREDICTION_MODE_INTERPOLATION时生效。

**起始版本**：5.1.0(18)

**相关模块：** [GraphicsAccelerate](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_graphics_accelerate)

## 汇总

支持设备PhoneTablet 

### 成员变量

 支持设备PhoneTablet展开

| 名称 | 描述 |
| --- | --- |
| FG_PresentMode presentMode | 预测帧展示模式。取值为FG_PRESENT_BY_SYSTEM时，仅在 FG_PredictionMode 为FG_PREDICTION_MODE_INTERPOLATION时生效。 |
| bool textureCachedByGame | 深度纹理和颜色纹理是否被游戏单独缓存来用于超帧。缓存情况下算法将直接使用不再额外缓存。取值为True时，仅在 FG_PredictionMode 为FG_PREDICTION_MODE_INTERPOLATION时生效。 取值范围：[true, false]。 |
| bool needFlipInputColor | 输入的颜色纹理是否需要翻转。需要翻转情况下，算法映射Y轴坐标读取颜色纹理。取值为True时，仅在 FG_PredictionMode 为FG_PREDICTION_MODE_INTERPOLATION时生效。 取值范围：[true, false]。 |
| bool needFlipOutputColor | 预测帧是否需要翻转。需要翻转情况下，算法映射Y轴坐标进行翻转输出。取值为True时，仅在 FG_PredictionMode 为FG_PREDICTION_MODE_INTERPOLATION时生效。 取值范围：[true, false]。 |

## 结构体成员变量说明

支持设备PhoneTablet 

### presentMode

支持设备PhoneTablet

```
FG_PresentMode FG_IntegrationInfo::presentMode
```

**描述**

展示模式。

### textureCachedByGame

支持设备PhoneTablet

```
bool FG_IntegrationInfo::textureCachedByGame
```

**描述**

深度纹理和颜色纹理是否被游戏单独缓存来用于超帧。缓存情况下算法将直接使用不再额外缓存。取值为True时，仅在[FG_PredictionMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_graphics_accelerate#gaea2169cd5ae4bf9e8a17dc58f33e8766)为FG_PREDICTION_MODE_INTERPOLATION生效。

### needFlipInputColor

支持设备PhoneTablet

```
bool FG_IntegrationInfo::needFlipInputColor
```

**描述**

输入的颜色纹理是否需要翻转。需要翻转情况下，算法映射Y轴坐标读取颜色纹理。取值为True时，仅在[FG_PredictionMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_graphics_accelerate#gaea2169cd5ae4bf9e8a17dc58f33e8766)为FG_PREDICTION_MODE_INTERPOLATION生效。

### needFlipOutputColor

支持设备PhoneTablet

```
bool FG_IntegrationInfo::needFlipOutputColor
```

**描述**

预测帧是否需要翻转。需要翻转情况下，算法映射Y轴坐标进行翻转输出。取值为True时，仅在[FG_PredictionMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_graphics_accelerate#gaea2169cd5ae4bf9e8a17dc58f33e8766)为FG_PREDICTION_MODE_INTERPOLATION生效。