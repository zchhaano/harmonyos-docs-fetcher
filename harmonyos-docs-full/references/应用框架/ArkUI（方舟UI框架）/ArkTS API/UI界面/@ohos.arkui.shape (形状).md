# @ohos.arkui.shape (形状)

在[clipShape](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-sharp-clipping#clipshape12)和[maskShape](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-sharp-clipping#maskshape12)接口中可以传入对应的形状。

 说明 

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

支持设备PhonePC/2in1TabletTVWearable收起自动换行深色代码主题复制

```
import { CircleShape , EllipseShape , PathShape , RectShape } from "@kit.ArkUI" ;
```

## CircleShape

支持设备PhonePC/2in1TabletTVWearable

用于 clipShape 和 maskShape 接口的圆形形状。

继承自[BaseShape](/consumer/cn/doc/harmonyos-references/js-apis-arkui-shape#baseshape)。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### constructor

支持设备PhonePC/2in1TabletTVWearable

constructor(options?: ShapeSize)

创建CircleShape对象。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

 展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | ShapeSize | 否 | 形状的大小。 |

## EllipseShape

支持设备PhonePC/2in1TabletTVWearable

用于 clipShape 和 maskShape 接口的椭圆形状。

继承自[BaseShape](/consumer/cn/doc/harmonyos-references/js-apis-arkui-shape#baseshape)。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### constructor

支持设备PhonePC/2in1TabletTVWearable

constructor(options?: ShapeSize)

创建EllipseShape对象。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

 展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | ShapeSize | 否 | 形状的大小。 |

## PathShape

支持设备PhonePC/2in1TabletTVWearable

用于 clipShape 和 maskShape 接口的路径。

继承自[CommonShapeMethod](/consumer/cn/doc/harmonyos-references/js-apis-arkui-shape#commonshapemethod)。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### constructor

支持设备PhonePC/2in1TabletTVWearable

constructor(options?: PathShapeOptions)

创建PathShape对象。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

 展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | PathShapeOptions | 否 | 路径参数。 |

### commands

支持设备PhonePC/2in1TabletTVWearable

commands(commands: string): PathShape

设置路径的绘制指令。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

 展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| commands | string | 是 | 路径的绘制指令。 |

**返回值：**

 展开

| 类型 | 说明 |
| --- | --- |
| PathShape | 返回PathShape对象。 |

## RectShape

支持设备PhonePC/2in1TabletTVWearable

用于 clipShape 和 maskShape 接口的矩形形状。

继承自[BaseShape](/consumer/cn/doc/harmonyos-references/js-apis-arkui-shape#baseshape)。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### constructor

支持设备PhonePC/2in1TabletTVWearable

constructor(options?: RectShapeOptions | RoundRectShapeOptions)

创建RectShape对象。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

 展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | RectShapeOptions \| RoundRectShapeOptions | 否 | 矩形形状参数。 |

### radiusWidth

支持设备PhonePC/2in1TabletTVWearable

radiusWidth(rWidth: number | string): RectShape

设置矩形形状圆角半径的宽度。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

 展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| rWidth | number  \|  string | 是 | 矩形形状圆角半径的宽度。 类型为number时取值范围是[0, +∞)，string时是 Length 。 单位：vp 取值为异常值时按照0vp处理。 |

**返回值：**

 展开

| 类型 | 说明 |
| --- | --- |
| RectShape | 返回RectShape对象。 |

### radiusHeight

支持设备PhonePC/2in1TabletTVWearable

radiusHeight(rHeight: number | string): RectShape

设置矩形形状圆角半径的高度。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

 展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| rHeight | number  \|  string | 是 | 矩形形状圆角半径的高度。 类型为number时取值范围是[0, +∞)，string时是 Length 。 单位：vp 取值为异常值时按照0vp处理。 |

**返回值：**

 展开

| 类型 | 说明 |
| --- | --- |
| RectShape | 返回RectShape对象。 |

### radius

支持设备PhonePC/2in1TabletTVWearable

radius(radius: number | string | Array<number  |  string>): RectShape

设置矩形形状的圆角半径。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

 展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| radius | number  \|  string  \|  Array<number  \|  string> | 是 | 矩形形状的圆角半径。仅接受数组的前四个元素，分别为矩形左上，右上，左下，右下的圆角半径。 类型为number时取值范围是[0, +∞)，string时是 Length 。 单位：vp 取值为异常值时按照0vp处理。 |

**返回值：**

 展开

| 类型 | 说明 |
| --- | --- |
| RectShape | 返回RectShape对象。 |

## ShapeSize

支持设备PhonePC/2in1TabletTVWearable

形状的尺寸参数。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

 展开

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| width | number  \|  string | 否 | 是 | 形状的宽度。 类型为number时取值范围是[0, +∞)，string时是 Length 。 单位：vp 取值为异常值时按照0vp处理。 |
| height | number  \|  string | 否 | 是 | 形状的高度。 类型为number时取值范围是[0, +∞)，string时是 Length 。 单位：vp 取值为异常值时按照0vp处理。 |

## PathShapeOptions

支持设备PhonePC/2in1TabletTVWearable

PathShape 的构造函数参数。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

 展开

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| commands | string | 否 | 是 | 绘制路径的指令。更多说明请参考commands支持的 绘制命令 。 |

## RectShapeOptions

支持设备PhonePC/2in1TabletTVWearable

RectShape 的构造函数参数。

继承自[ShapeSize](/consumer/cn/doc/harmonyos-references/js-apis-arkui-shape#shapesize)。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

 展开

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| radius | number  \|  string  \|  Array<number  \|  string> | 否 | 是 | 矩形形状的圆角半径。 类型为number时取值范围是[0, +∞)，string时是 Length 。 单位：vp 取值为异常值时按照0vp处理。 |

## RoundRectShapeOptions

支持设备PhonePC/2in1TabletTVWearable

RectShape 带有半径的构造函数参数。

继承自[ShapeSize](/consumer/cn/doc/harmonyos-references/js-apis-arkui-shape#shapesize)。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

 展开

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| radiusWidth | number  \|  string | 否 | 是 | 矩形形状圆角半径的宽度。 类型为number时取值范围是[0, +∞)，string时是 Length 。 单位：vp 取值为异常值时按照0vp处理。 |
| radiusHeight | number  \|  string | 否 | 是 | 矩形形状圆角半径的高度。 类型为number时取值范围是[0, +∞)，string时是 Length 。 单位：vp 取值为异常值时按照0vp处理。 |

## BaseShape

支持设备PhonePC/2in1TabletTVWearable

继承自[CommonShapeMethod](/consumer/cn/doc/harmonyos-references/js-apis-arkui-shape#commonshapemethod)。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### width

支持设备PhonePC/2in1TabletTVWearable

width(width: Length): T

设置形状的宽度。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

 展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| width | Length | 是 | 形状的宽度。 单位：vp 取值为异常值时按照0vp处理。 |

**返回值：**

 展开

| 类型 | 说明 |
| --- | --- |
| T | 返回当前对象。 |

### height

支持设备PhonePC/2in1TabletTVWearable

height(height: Length): T

设置形状的高度。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

 展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| height | Length | 是 | 形状的高度。 单位：vp 取值为异常值时按照0vp处理。 |

**返回值：**

 展开

| 类型 | 说明 |
| --- | --- |
| T | 返回当前对象。 |

### size

支持设备PhonePC/2in1TabletTVWearable

size(size: SizeOptions): T

设置形状的大小。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

 展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| size | SizeOptions | 是 | 形状的大小。 |

**返回值：**

 展开

| 类型 | 说明 |
| --- | --- |
| T | 返回当前对象。 |

## CommonShapeMethod

支持设备PhonePC/2in1TabletTVWearable

常见的形状方法。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### offset

支持设备PhonePC/2in1TabletTVWearable

offset(offset: Position): T

设置相对于组件布局位置的坐标偏移。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

 展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| offset | Position | 是 | 相对于组件布局位置的坐标偏移。 |

**返回值：**

 展开

| 类型 | 说明 |
| --- | --- |
| T | 返回当前对象。 |

### fill

支持设备PhonePC/2in1TabletTVWearable

fill(color: ResourceColor): T

设置形状的填充区域的透明度，黑色表示完全透明，白色表示完全不透明。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

 展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| color | ResourceColor | 是 | 形状的填充区域的透明度，黑色表示完全透明，白色表示完全不透明。 |

**返回值：**

 展开

| 类型 | 说明 |
| --- | --- |
| T | 返回当前对象。 |

### position

支持设备PhonePC/2in1TabletTVWearable

position(position: Position): T

设置形状的位置。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

 展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| position | Position | 是 | 设置形状的位置。 |

**返回值：**

 展开

| 类型 | 说明 |
| --- | --- |
| T | 返回当前对象。 |

## 示例

支持设备PhonePC/2in1TabletTVWearable

该示例主要演示通过[clipShape](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-sharp-clipping#clipshape12)和[maskShape](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-sharp-clipping#maskshape12)将图片裁剪和遮罩成不同形状。

 收起自动换行深色代码主题复制

```
import { CircleShape , EllipseShape , PathShape , RectShape } from '@kit.ArkUI' ; @Entry @Component struct ShapeExample { build ( ) { Column ({ space : 15 }) { Text ( 'CircleShape, position' ). fontSize ( 20 ). width ( '75%' ). fontColor ( '#DCDCDC' ) // $r('app.media.startIcon')需替换为开发者所需的资源文件 Image ($r( 'app.media.startIcon' )) . clipShape ( new CircleShape ({ width : '280px' , height : '280px' }). position ({ x : '20px' , y : '20px' })) . width ( '500px' ). height ( '280px' ) Text ( 'EllipseShape, offset' ). fontSize ( 20 ). width ( '75%' ). fontColor ( '#DCDCDC' ) // $r('app.media.startIcon')需替换为开发者所需的资源文件 Image ($r( 'app.media.startIcon' )) . clipShape ( new EllipseShape ({ width : '350px' , height : '280px' }). offset ({ x : '10px' , y : '10px' })) . width ( '500px' ). height ( '280px' ) Text ( 'PathShape, fill' ). fontSize ( 20 ). width ( '75%' ). fontColor ( '#DCDCDC' ) // $r('app.media.startIcon')需替换为开发者所需的资源文件 Image ($r( 'app.media.startIcon' )) . maskShape ( new PathShape (). commands ( 'M100 0 L200 240 L0 240 Z' ). fill ( Color . Red )) . width ( '500px' ). height ( '280px' ) Text ( 'RectShape, width, height, fill' ). fontSize ( 20 ). width ( '75%' ). fontColor ( '#DCDCDC' ) // $r('app.media.startIcon')需替换为开发者所需的资源文件 Image ($r( 'app.media.startIcon' )) . maskShape ( new RectShape (). width ( '350px' ). height ( '280px' ). fill ( Color . Red )) . width ( '500px' ). height ( '280px' ) } . width ( '100%' ) . margin ({ top : 15 }) } }
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170652.92391641988177087288895079237791:50001231000000:2800:B1DC9F174922792389FF461D8B818ECBB36A98F514F7DA93A2AF9355E3FEFE36.png)