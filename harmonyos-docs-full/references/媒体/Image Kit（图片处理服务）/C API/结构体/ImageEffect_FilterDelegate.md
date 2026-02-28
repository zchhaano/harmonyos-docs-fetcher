# ImageEffect_FilterDelegate

```
typedef struct ImageEffect_FilterDelegate {...} ImageEffect_FilterDelegate
```

## 概述

支持设备PhonePC/2in1TabletTV

自定义滤镜回调函数结构体。

**起始版本：** 12

**相关模块：** [ImageEffect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-imageeffect)

**所在头文件：** [image_effect_filter.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-effect-filter-h)

## 汇总

支持设备PhonePC/2in1TabletTV 

### 成员变量

 支持设备PhonePC/2in1TabletTV展开

| 名称 | 描述 |
| --- | --- |
| OH_EffectFilterDelegate_SetValue setValue | 参数设置函数指针。 |
| OH_EffectFilterDelegate_Render render | 滤镜渲染函数指针。 |
| OH_EffectFilterDelegate_Save save | 序列化效果器函数指针。 |
| OH_EffectFilterDelegate_Restore restore | 反序列化效果器函数指针。 |