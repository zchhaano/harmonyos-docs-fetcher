# ImageProcessing_ColorSpaceInfo

收起自动换行深色代码主题复制

```
typedef struct ImageProcessing_ColorSpaceInfo { ...} ImageProcessing_ColorSpaceInfo
```

## 概述

 支持设备PhonePC/2in1Tablet

色彩空间信息，用于色彩空间转换能力查询。

**参考：**

[OH_ImageProcessing_IsColorSpaceConversionSupported](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-processing-h#oh_imageprocessing_iscolorspaceconversionsupported), [OH_ImageProcessing_IsCompositionSupported](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-processing-h#oh_imageprocessing_iscompositionsupported), [OH_ImageProcessing_IsDecompositionSupported](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-processing-h#oh_imageprocessing_isdecompositionsupported)

**起始版本：** 13

**相关模块：** [ImageProcessing](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-imageprocessing)

**所在头文件：** [image_processing_types.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-processing-types-h)

## 汇总

 支持设备PhonePC/2in1Tablet  

### 成员变量

 支持设备PhonePC/2in1Tablet 展开

| 名称 | 描述 |
| --- | --- |
| int32_t metadataType | 定义元数据类型，参考 OH_Pixelmap_HdrMetadataKey 。 |
| int32_t colorSpace | 定义色彩空间，参考 ColorSpaceName 。 |
| int32_t pixelFormat | 定义像素格式，参考 PIXEL_FORMAT 。 |