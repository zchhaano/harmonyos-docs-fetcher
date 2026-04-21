# Camera_MetadataObject

 

```
typedef struct Camera_MetadataObject {...} Camera_MetadataObject

```

 

#### 概述

元数据对象基础。

 

**起始版本：** 11

 

**相关模块：** [OH_Camera](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera)

 

**所在头文件：** [camera.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-camera-h)

  

#### 汇总

 

#### [h2]成员变量

 

| 名称 | 描述 |
| --- | --- |
| Camera_MetadataObjectType type | 元数据对象类型。 |
| int64_t timestamp | 元数据对象时间戳，单位为纳秒（ns）。 |
| Camera_Rect * boundingBox | 检测到的元数据对象的轴对齐边界框。 |