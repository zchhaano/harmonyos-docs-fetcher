## 概述

支持设备PhonePC/2in1TabletTVWearable

定义了与区域相关的功能函数，包括区域的创建，边界设置和销毁等。

**引用文件：** <native_drawing/drawing_region.h>

**库：** libnative_drawing.so

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**相关模块：** [Drawing](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing)

## 汇总

支持设备PhonePC/2in1TabletTVWearable 

### 枚举

 支持设备PhonePC/2in1TabletTVWearable展开

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| OH_Drawing_RegionOpMode | OH_Drawing_RegionOpMode | 区域操作类型枚举。 |

### 函数

 支持设备PhonePC/2in1TabletTVWearable展开

| 名称 | 描述 |
| --- | --- |
| OH_Drawing_Region* OH_Drawing_RegionCreate(void) | 用于创建一个区域对象，实现更精确的图形控制。 |
| OH_Drawing_Region* OH_Drawing_RegionCopy(const OH_Drawing_Region* region) | 用于创建一个区域对象的拷贝。 |
| bool OH_Drawing_RegionContains(OH_Drawing_Region* region, int32_t x, int32_t y) | 判断区域是否包含指定坐标点。 本接口会产生错误码，可以通过 OH_Drawing_ErrorCodeGet 查看错误码的取值。 region为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。 |
| bool OH_Drawing_RegionOp(OH_Drawing_Region* region, const OH_Drawing_Region* other, OH_Drawing_RegionOpMode op) | 将两个区域按照指定的区域操作类型合并。 本接口会产生错误码，可以通过 OH_Drawing_ErrorCodeGet 查看错误码的取值。 region、dst任意一个为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER； op不在枚举范围内时返回OH_DRAWING_ERROR_PARAMETER_OUT_OF_RANGE。 |
| bool OH_Drawing_RegionSetRect(OH_Drawing_Region* region, const OH_Drawing_Rect* rect) | 用于尝试给区域对象设置矩形边界。 本接口会产生错误码，可以通过 OH_Drawing_ErrorCodeGet 查看错误码的取值。 region、rect任意一个为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。 |
| bool OH_Drawing_RegionSetPath(OH_Drawing_Region* region, const OH_Drawing_Path* path, const OH_Drawing_Region* clip) | 给区域对象设置为指定区域内路径表示的范围。 本接口会产生错误码，可以通过 OH_Drawing_ErrorCodeGet 查看错误码的取值。 region、path、clip任意一个为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。 |
| void OH_Drawing_RegionDestroy(OH_Drawing_Region* region) | 用于销毁区域对象并回收该对象占有的内存。 |
| OH_Drawing_ErrorCode OH_Drawing_RegionEmpty(OH_Drawing_Region* region) | 设置当前区域为空。 |

## 枚举类型说明

支持设备PhonePC/2in1TabletTVWearable 

### OH_Drawing_RegionOpMode

支持设备PhonePC/2in1TabletTVWearable

```
enum OH_Drawing_RegionOpMode
```

**描述**

区域操作类型枚举。

**起始版本：** 12

 展开

| 枚举项 | 描述 |
| --- | --- |
| REGION_OP_MODE_DIFFERENCE | 差集操作。 |
| REGION_OP_MODE_INTERSECT | 交集操作。 |
| REGION_OP_MODE_UNION | 并集操作。 |
| REGION_OP_MODE_XOR | 异或操作。 |
| REGION_OP_MODE_REVERSE_DIFFERENCE | 反向差集操作。 |
| REGION_OP_MODE_REPLACE | 替换操作。 |

## 函数说明

支持设备PhonePC/2in1TabletTVWearable 

### OH_Drawing_RegionCreate()

支持设备PhonePC/2in1TabletTVWearable

```
OH_Drawing_Region* OH_Drawing_RegionCreate(void)
```

**描述**

用于创建一个区域对象，实现更精确的图形控制。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**返回：**

 展开

| 类型 | 说明 |
| --- | --- |
| OH_Drawing_Region * | 函数会返回一个指针，指针指向创建的区域对象 OH_Drawing_Region 。 |

### OH_Drawing_RegionCopy()

支持设备PhonePC/2in1TabletTVWearable

```
OH_Drawing_Region* OH_Drawing_RegionCopy(const OH_Drawing_Region* region)
```

**描述**

用于创建一个区域对象的拷贝。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 20

**参数：**

 展开

| 参数项 | 描述 |
| --- | --- |
| const OH_Drawing_Region * region | 指向用于拷贝的区域对象 OH_Drawing_Region 的指针。 |

**返回：**

 展开

| 类型 | 说明 |
| --- | --- |
| OH_Drawing_Region * | 函数会返回一个指针，指针指向创建的新区域对象。 |

### OH_Drawing_RegionContains()

支持设备PhonePC/2in1TabletTVWearable

```
bool OH_Drawing_RegionContains(OH_Drawing_Region* region, int32_t x, int32_t y)
```

**描述**

判断区域是否包含指定坐标点。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-error-code-h#oh_drawing_errorcodeget)查看错误码的取值。

region为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

 展开

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Region * region | 指向区域对象 OH_Drawing_Region 的指针。 |
| int32_t x | 表示指定坐标点的x轴坐标。 |
| int32_t y | 表示指定坐标点的y轴坐标。 |

**返回：**

 展开

| 类型 | 说明 |
| --- | --- |
| bool | 返回区域是否包含指定坐标点。true表示区域包含该坐标点，false表示区域不包含该坐标点。 |

### OH_Drawing_RegionOp()

支持设备PhonePC/2in1TabletTVWearable

```
bool OH_Drawing_RegionOp(OH_Drawing_Region* region, const OH_Drawing_Region* other, OH_Drawing_RegionOpMode op)
```

**描述**

将两个区域按照指定的区域操作类型合并。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-error-code-h#oh_drawing_errorcodeget)查看错误码的取值。

region、dst任意一个为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER；

op不在枚举范围内时返回OH_DRAWING_ERROR_PARAMETER_OUT_OF_RANGE。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

 展开

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Region * region | 指向区域对象 OH_Drawing_Region 的指针，操作完成后的区域结果将会保存在此区域对象中。 |
| const OH_Drawing_Region * other | 指向区域对象 OH_Drawing_Region 的指针。 |
| OH_Drawing_RegionOpMode op | 区域操作枚举类型，支持可选的具体模式可见 OH_Drawing_RegionOpMode 枚举。 |

**返回：**

 展开

| 类型 | 说明 |
| --- | --- |
| bool | 返回操作后的区域是否为空。true表示区域不为空，false表示区域为空。 |

### OH_Drawing_RegionSetRect()

支持设备PhonePC/2in1TabletTVWearable

```
bool OH_Drawing_RegionSetRect(OH_Drawing_Region* region, const OH_Drawing_Rect* rect)
```

**描述**

用于尝试给区域对象设置矩形边界。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-error-code-h#oh_drawing_errorcodeget)查看错误码的取值。

region、rect任意一个为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

 展开

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Region * region | 指向区域对象 OH_Drawing_Region 的指针。 |
| const OH_Drawing_Rect * rect | 指向矩形对象的指针。 |

**返回：**

 展开

| 类型 | 说明 |
| --- | --- |
| bool | 返回区域对象设置矩形边界是否成功的结果。true表示设置矩形边界成功，false表示设置矩形边界失败。 |

### OH_Drawing_RegionSetPath()

支持设备PhonePC/2in1TabletTVWearable

```
bool OH_Drawing_RegionSetPath(OH_Drawing_Region* region, const OH_Drawing_Path* path, const OH_Drawing_Region* clip)
```

**描述**

给区域对象设置为指定区域内路径表示的范围。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-error-code-h#oh_drawing_errorcodeget)查看错误码的取值。

region、path、clip任意一个为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

 展开

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Region * region | 指向区域对象 OH_Drawing_Region 的指针。 |
| const OH_Drawing_Path * path | 指向路径对象 OH_Drawing_Path 的指针。 |
| const OH_Drawing_Region * clip | 指向区域对象 OH_Drawing_Region 的指针。 |

**返回：**

 展开

| 类型 | 说明 |
| --- | --- |
| bool | 返回操作后的区域是否为空。true表示区域不为空，false表示区域为空。 |

### OH_Drawing_RegionDestroy()

支持设备PhonePC/2in1TabletTVWearable

```
void OH_Drawing_RegionDestroy(OH_Drawing_Region* region)
```

**描述**

用于销毁区域对象并回收该对象占有的内存。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

 展开

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Region * region | 指向区域对象 OH_Drawing_Region 的指针。 |

### OH_Drawing_RegionEmpty()

支持设备PhonePC/2in1TabletTVWearable

```
OH_Drawing_ErrorCode OH_Drawing_RegionEmpty(OH_Drawing_Region* region)
```

**描述**

设置当前区域为空。

**起始版本：** 22

**参数：**

 展开

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Region * region | 指向区域对象 OH_Drawing_Region 的指针。 |

**返回：**

 展开

| 类型 | 说明 |
| --- | --- |
| OH_Drawing_ErrorCode | 函数返回执行错误码。 返回OH_DRAWING_SUCCESS，表示执行成功。 返回OH_DRAWING_ERROR_INCORRECT_PARAMETER，表示参数region为空。 |