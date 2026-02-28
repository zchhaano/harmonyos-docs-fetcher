# OhosImageSourceOps

```
struct OhosImageSourceOps {...}
```

## 概述

支持设备PhonePC/2in1TabletTVWearable

定义图像源选项信息。此选项给[OH_ImageSource_CreateFromUri](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-source-mdk-h#oh_imagesource_createfromuri)、[OH_ImageSource_CreateFromFd](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-source-mdk-h#oh_imagesource_createfromfd)、[OH_ImageSource_CreateFromData](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-source-mdk-h#oh_imagesource_createfromdata)和[OH_ImageSource_CreateIncremental](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-source-mdk-h#oh_imagesource_createincremental)接口使用。

**起始版本：** 10

**相关模块：** [Image](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image)

**所在头文件：** [image_source_mdk.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-source-mdk-h)

## 汇总

支持设备PhonePC/2in1TabletTVWearable 

### 成员变量

 支持设备PhonePC/2in1TabletTVWearable展开

| 名称 | 描述 |
| --- | --- |
| int32_t density | 图像源像素密度。 |
| int32_t pixelFormat | 图像源像素格式，通常用于描述YUV缓冲区。 |
| struct OhosImageSize size | 图像源像素宽高的大小。 |