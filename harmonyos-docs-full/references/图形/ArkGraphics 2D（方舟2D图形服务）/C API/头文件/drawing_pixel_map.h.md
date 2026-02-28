## 概述

支持设备PhonePC/2in1TabletTVWearable

声明与绘图模块中的像素图对象相关的函数。

**引用文件：** <native_drawing/drawing_pixel_map.h>

**库：** libnative_drawing.so

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**相关模块：** [Drawing](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing)

## 汇总

支持设备PhonePC/2in1TabletTVWearable 

### 结构体

 支持设备PhonePC/2in1TabletTVWearable展开

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| NativePixelMap_ | NativePixelMap_ | 声明由图像框架定义的像素图对象。 |
| OH_PixelmapNative | OH_PixelmapNative | 声明由图像框架定义的像素图对象。 |

### 函数

 支持设备PhonePC/2in1TabletTVWearable展开

| 名称 | 描述 |
| --- | --- |
| OH_Drawing_PixelMap* OH_Drawing_PixelMapGetFromNativePixelMap(NativePixelMap_* nativePixelMap) | 从图像框架定义的像素图对象中获取本模块定义的像素图对象。 |
| OH_Drawing_PixelMap* OH_Drawing_PixelMapGetFromOhPixelMapNative(OH_PixelmapNative* pixelmapNative) | 从图像框架定义的像素图对象中获取本模块定义的像素图对象。 |
| void OH_Drawing_PixelMapDissolve(OH_Drawing_PixelMap* pixelMap) | 解除本模块定义的像素图对象和图像框架定义的像素图对象之间的关系，该关系通过调用 OH_Drawing_PixelMapGetFromNativePixelMap 或 OH_Drawing_PixelMapGetFromOhPixelMapNative 建立。若在建立关系后未调用本接口解除关系，将导致像素图对象的内存无法正确释放，进而引发内存泄漏问题。 |

## 函数说明

支持设备PhonePC/2in1TabletTVWearable 

### OH_Drawing_PixelMapGetFromNativePixelMap()

支持设备PhonePC/2in1TabletTVWearable

```
OH_Drawing_PixelMap* OH_Drawing_PixelMapGetFromNativePixelMap(NativePixelMap_* nativePixelMap)
```

**描述**

从图像框架定义的像素图对象中获取本模块定义的像素图对象。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

 展开

| 参数项 | 描述 |
| --- | --- |
| NativePixelMap_ * nativePixelMap | 指向图像框架定义的像素图对象 NativePixelMap_ 的指针。 |

**返回：**

 展开

| 类型 | 说明 |
| --- | --- |
| OH_Drawing_PixelMap * | 函数会返回一个指向本模块定义的像素图对象 OH_Drawing_PixelMap 的指针。如果对象返回NULL，表示创建失败；可能的原因是NativePixelMap_为NULL。 |

### OH_Drawing_PixelMapGetFromOhPixelMapNative()

支持设备PhonePC/2in1TabletTVWearable

```
OH_Drawing_PixelMap* OH_Drawing_PixelMapGetFromOhPixelMapNative(OH_PixelmapNative* pixelmapNative)
```

**描述**

从图像框架定义的像素图对象中获取本模块定义的像素图对象。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

 展开

| 参数项 | 描述 |
| --- | --- |
| OH_PixelmapNative * pixelmapNative | 指向图像框架定义的像素图对象 OH_PixelmapNative 的指针。 |

**返回：**

 展开

| 类型 | 说明 |
| --- | --- |
| OH_Drawing_PixelMap * | 函数会返回一个指向本模块定义的像素图对象 OH_Drawing_PixelMap 的指针。如果对象返回NULL，表示创建失败；可能的原因是OH_PixelmapNative为NULL。 |

### OH_Drawing_PixelMapDissolve()

支持设备PhonePC/2in1TabletTVWearable

```
void OH_Drawing_PixelMapDissolve(OH_Drawing_PixelMap* pixelMap)
```

**描述**

解除本模块定义的像素图对象和图像框架定义的像素图对象之间的关系，该关系通过调用[OH_Drawing_PixelMapGetFromNativePixelMap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-pixel-map-h#oh_drawing_pixelmapgetfromnativepixelmap)或[OH_Drawing_PixelMapGetFromOhPixelMapNative](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-pixel-map-h#oh_drawing_pixelmapgetfromohpixelmapnative)建立。若在建立关系后未调用本接口解除关系，将导致像素图对象的内存无法正确释放，进而引发内存泄漏问题。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

 展开

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_PixelMap * pixelMap | 指向像素图对象 OH_Drawing_PixelMap 的指针。 |