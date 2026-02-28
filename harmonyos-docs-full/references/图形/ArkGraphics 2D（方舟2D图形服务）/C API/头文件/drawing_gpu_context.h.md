## 概述

支持设备PhonePC/2in1TabletTVWearable

声明与绘图模块中的图形处理器上下文对象相关的函数。

**引用文件：** <native_drawing/drawing_gpu_context.h>

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
| OH_Drawing_GpuContextOptions | OH_Drawing_GpuContextOptions | 定义有关图形处理器上下文的选项。 |

### 函数

 支持设备PhonePC/2in1TabletTVWearable展开

| 名称 | 描述 |
| --- | --- |
| OH_Drawing_GpuContext* OH_Drawing_GpuContextCreateFromGL(OH_Drawing_GpuContextOptions gpuContextOptions) | 用于创建一个使用OpenGL作为后端接口的图形处理器上下文对象。 |
| OH_Drawing_GpuContext* OH_Drawing_GpuContextCreate(void) | 用于创建一个图形处理器上下文对象, 使用的后端类型取决于运行设备。 |
| void OH_Drawing_GpuContextDestroy(OH_Drawing_GpuContext* gpuContext) | 用于销毁图形处理器上下文对象并回收该对象占用的内存。 |

## 函数说明

支持设备PhonePC/2in1TabletTVWearable 

### OH_Drawing_GpuContextCreateFromGL()

支持设备PhonePC/2in1TabletTVWearable

```
OH_Drawing_GpuContext* OH_Drawing_GpuContextCreateFromGL(OH_Drawing_GpuContextOptions gpuContextOptions)
```

**描述**

用于创建一个使用OpenGL作为后端接口的图形处理器上下文对象。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**废弃版本：** 18

**替代接口：** OH_Drawing_GpuContextCreate

**参数：**

 展开

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_GpuContextOptions gpuContextOptions | 图形处理器上下文选项 OH_Drawing_GpuContextOptions 。 |

**返回：**

 展开

| 类型 | 说明 |
| --- | --- |
| OH_Drawing_GpuContext * | 返回一个指针，指针指向创建的图形处理器上下文对象 OH_Drawing_GpuContext 。 |

### OH_Drawing_GpuContextCreate()

支持设备PhonePC/2in1TabletTVWearable

```
OH_Drawing_GpuContext* OH_Drawing_GpuContextCreate(void)
```

**描述**

用于创建一个图形处理器上下文对象, 使用的后端类型取决于运行设备。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 16

**返回：**

 展开

| 类型 | 说明 |
| --- | --- |
| OH_Drawing_GpuContext * | 返回一个指针，指针指向创建的图形处理器上下文对象 OH_Drawing_GpuContext 。 |

### OH_Drawing_GpuContextDestroy()

支持设备PhonePC/2in1TabletTVWearable

```
void OH_Drawing_GpuContextDestroy(OH_Drawing_GpuContext* gpuContext)
```

**描述**

用于销毁图形处理器上下文对象并回收该对象占用的内存。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

 展开

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_GpuContext * gpuContext | 指向图形处理器上下文对象的指针 OH_Drawing_GpuContext 。 |