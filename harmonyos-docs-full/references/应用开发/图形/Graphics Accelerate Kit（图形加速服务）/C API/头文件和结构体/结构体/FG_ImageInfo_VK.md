## 概述

支持设备PhoneTablet

此结构体描述超帧输入输出图像信息。

**起始版本：** 5.0.0(12)

**相关模块：** [GraphicsAccelerate](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_graphics_accelerate)

## 汇总

支持设备PhoneTablet 

### 成员变量

 支持设备PhoneTablet展开

| 名称 | 描述 |
| --- | --- |
| FG_Image_VK * image | 超帧输入输出图像结构体 FG_Image_VK 对象的指针，该图像实例需要通过 HMS_FG_CreateImage_VK 进行创建，通过 HMS_FG_DestroyImage_VK 进行销毁。 |
| FG_ImageSync_VK initialSync | HMS_FG_Dispatch_VK 执行前，该图像的同步状态。 |
| FG_ImageSync_VK finalSync | HMS_FG_Dispatch_VK 执行后，该图像的同步状态。 |

## 结构体成员变量说明

支持设备PhoneTablet 

### finalSync

支持设备PhoneTablet

```
FG_ImageSync_VK FG_ImageInfo_VK::finalSync
```

**描述**

[HMS_FG_Dispatch_VK](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_graphics_accelerate#ga21f86a194e72e99dd54fd39080385a37)执行后，该图像的同步状态。

### image

支持设备PhoneTablet

```
FG_Image_VK * FG_ImageInfo_VK::image
```

**描述**

超帧输入输出图像结构体[FG_Image_VK](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_graphics_accelerate#gabd6ee9704e997ffc2792ad3c89847019)对象的指针，该图像实例需要通过[HMS_FG_CreateImage_VK](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_graphics_accelerate#ga7733f097ea5f4ae4d2aa53d11d7e60ff)进行创建，通过[HMS_FG_DestroyImage_VK](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_graphics_accelerate#gac850c7cd41a1aebaf9bcf943ebff372a)进行销毁。

### initialSync

支持设备PhoneTablet

```
FG_ImageSync_VK FG_ImageInfo_VK::initialSync
```

**描述**

[HMS_FG_Dispatch_VK](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_graphics_accelerate#ga21f86a194e72e99dd54fd39080385a37)执行前，该图像的同步状态。