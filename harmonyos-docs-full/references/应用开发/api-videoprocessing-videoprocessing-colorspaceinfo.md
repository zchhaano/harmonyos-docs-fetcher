# VideoProcessing_ColorSpaceInfo

收起自动换行深色代码主题复制

```
typedef struct VideoProcessing_ColorSpaceInfo { ...} VideoProcessing_ColorSpaceInfo
```

## 概述

 支持设备PhonePC/2in1Tablet

视频颜色空间信息数据结构。

**参考：** [OH_VideoProcessing_IsColorSpaceConversionSupported](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-video-processing-h#oh_videoprocessing_iscolorspaceconversionsupported)

**起始版本：** 12

**相关模块：** [VideoProcessing](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-videoprocessing)

**所在头文件：** [video_processing_types.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-video-processing-types-h)

## 汇总

 支持设备PhonePC/2in1Tablet  

### 成员变量

 支持设备PhonePC/2in1Tablet 展开

| 名称 | 描述 |
| --- | --- |
| int32_t metadataType | 视频元数据类型，参考 OH_NativeBuffer_MetadataType 。 |
| int32_t colorSpace | 视频颜色空间类型，参考 OH_NativeBuffer_ColorSpace 。 |
| int32_t pixelFormat | 视频像素格式，参考 OH_NativeBuffer_Format 。 |