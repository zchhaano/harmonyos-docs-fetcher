# Matrix2D

矩阵对象，可以对矩阵进行缩放、旋转和平移等变换。

 说明 

从 API version 8 开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## 构造函数

支持设备PhonePC/2in1TabletTVWearable 

### constructor 10+

支持设备PhonePC/2in1TabletTVWearable

constructor()

构造二维变换矩阵对象，默认值是属性全为0的矩阵。

**卡片能力：** 从API version 10开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### constructor 12+

支持设备PhonePC/2in1TabletTVWearable

constructor(unit: LengthMetricsUnit)

构造二维变换矩阵对象，默认值是属性全为0的矩阵，支持配置Matrix2D对象的单位模式。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

 展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| unit | LengthMetricsUnit | 是 | 用来配置Matrix2D对象的单位模式，配置后无法动态更改，配置方法同 CanvasRenderingContext2D 。 异常值NaN和Infinity按默认值处理。 默认值：DEFAULT |

## 属性

支持设备PhonePC/2in1TabletTVWearable

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

 展开

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| scaleX | number | 否 | 是 | 水平缩放系数，取值范围无限制。 异常值undefined按无效值处理，NaN和Infinity会导致Matrix2D异常。 |
| scaleY | number | 否 | 是 | 垂直缩放系数，取值范围无限制。 异常值undefined按无效值处理，NaN和Infinity会导致Matrix2D异常。 |
| rotateX | number | 否 | 是 | 水平倾斜系数，取值范围无限制。 异常值undefined按无效值处理，NaN和Infinity会导致Matrix2D异常。 |
| rotateY | number | 否 | 是 | 垂直倾斜系数，取值范围无限制。 异常值undefined按无效值处理，NaN和Infinity会导致Matrix2D异常。 |
| translateX | number | 否 | 是 | 水平平移距离，取值范围无限制。 异常值undefined按无效值处理，NaN和Infinity会导致Matrix2D异常。 默认单位：vp |
| translateY | number | 否 | 是 | 垂直平移距离，取值范围无限制。 异常值undefined按无效值处理，NaN和Infinity会导致Matrix2D异常。 默认单位：vp |

  说明 

 可使用[px2vp](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#px2vp12)接口进行单位转换。

**示例：**

 收起自动换行深色代码主题复制

```
// xxx.ets @Entry @Component struct Parameter { private settings : RenderingContextSettings = new RenderingContextSettings ( true ); private context : CanvasRenderingContext2D = new CanvasRenderingContext2D ( this . settings ); private matrix : Matrix2D = new Matrix2D (); build ( ) { Flex ({ direction : FlexDirection . Column , alignItems : ItemAlign . Center , justifyContent : FlexAlign . Center }) { Canvas ( this . context ) . width ( '240vp' ) . height ( '180vp' ) . backgroundColor ( '#ffff00' ) . onReady ( () => { this . context . fillRect ( 100 , 20 , 50 , 50 ) this . matrix . scaleX = 1 this . matrix . scaleY = 1 this . matrix . rotateX = - 0.5 this . matrix . rotateY = 0.5 this . matrix . translateX = 10 this . matrix . translateY = 10 this . context . setTransform ( this . matrix ) this . context . fillRect ( 100 , 20 , 50 , 50 ) }) } . width ( '100%' ) . height ( '100%' ) } }
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170640.87776302881694019524617223231131:50001231000000:2800:97CAFF3B10AB36C5416BE3F3FCDF45A0FF1565D839207613696301CA7B2536F7.png)

## 方法

支持设备PhonePC/2in1TabletTVWearable 

### identity

支持设备PhonePC/2in1TabletTVWearable

identity(): Matrix2D

创建单位矩阵。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

 展开

| 类型 | 说明 |
| --- | --- |
| Matrix2D | 单位矩阵。 |

**示例：**

 收起自动换行深色代码主题复制

```
// xxx.ets @Entry @Component struct Identity { private settings : RenderingContextSettings = new RenderingContextSettings ( true ); private context : CanvasRenderingContext2D = new CanvasRenderingContext2D ( this . settings ); private matrix : Matrix2D = new Matrix2D (); build ( ) { Flex ({ direction : FlexDirection . Column , alignItems : ItemAlign . Center , justifyContent : FlexAlign . Center }) { Canvas ( this . context ) . width ( '240vp' ) . height ( '180vp' ) . backgroundColor ( '#ffff00' ) . onReady ( () => { this . context . fillRect ( 100 , 20 , 50 , 50 ) this . matrix = this . matrix . identity () this . context . setTransform ( this . matrix ) this . context . fillRect ( 100 , 100 , 50 , 50 ) }) } . width ( '100%' ) . height ( '100%' ) } }
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170640.28166612095092420583958151033575:50001231000000:2800:85462BDA01EE540A2A714C80857D7E746EE076E410107FE906CA3EA5CE1378E3.png)

### invert

支持设备PhonePC/2in1TabletTVWearable

invert(): Matrix2D

获取当前矩阵的逆矩阵。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

 展开

| 类型 | 说明 |
| --- | --- |
| Matrix2D | 逆矩阵结果。 |

**示例：**

 收起自动换行深色代码主题复制

```
// xxx.ets @Entry @Component struct Invert { private settings : RenderingContextSettings = new RenderingContextSettings ( true ); private context : CanvasRenderingContext2D = new CanvasRenderingContext2D ( this . settings ); private matrix : Matrix2D = new Matrix2D (); build ( ) { Flex ({ direction : FlexDirection . Column , alignItems : ItemAlign . Center , justifyContent : FlexAlign . Center }) { Canvas ( this . context ) . width ( '240vp' ) . height ( '180vp' ) . backgroundColor ( '#ffff00' ) . onReady ( () => { this . context . fillRect ( 100 , 110 , 50 , 50 ) this . matrix . scaleX = 1 this . matrix . scaleY = 1 this . matrix . rotateX = - 0.5 this . matrix . rotateY = 0.5 this . matrix . translateX = 10 this . matrix . translateY = 10 this . matrix . invert () this . context . setTransform ( this . matrix ) this . context . fillRect ( 100 , 110 , 50 , 50 ) }) } . width ( '100%' ) . height ( '100%' ) } }
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170640.29479436440000896488843970589203:50001231000000:2800:053C268C12ABAE75CF2A1A814FA220AA7CE076952C137781690CF7766597D5D6.png)

### multiply (deprecated)

multiply(other?: Matrix2D): Matrix2D

当前矩阵与目标矩阵相乘。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。该接口为空接口。

该接口从API version 10开始废弃，且无实际绘制效果，故不提供示例。

**参数：**

 展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | Matrix2D | 否 | 目标矩阵。 异常值undefined和null按无效值处理。 默认值：null |

**返回值：**

 展开

| 类型 | 说明 |
| --- | --- |
| Matrix2D | 相乘结果矩阵。 |

### rotate (deprecated)

rotate(rx?: number, ry?: number): Matrix2D

对当前矩阵进行旋转运算。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。该接口为空接口。

该接口从API version 10开始废弃，推荐使用[rotate](/consumer/cn/doc/harmonyos-references/ts-components-canvas-matrix2d#rotate10)。

**参数：**

 展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| rx | number | 否 | 旋转点的水平方向坐标，取值范围无限制。 异常值undefined和null按无效值处理，NaN和Infinity会导致Matrix2D异常。 默认单位：vp |
| ry | number | 否 | 旋转点的垂直方向坐标，取值范围无限制。 异常值undefined和null按无效值处理，NaN和Infinity会导致Matrix2D异常。 默认单位：vp |

**返回值：**

 展开

| 类型 | 说明 |
| --- | --- |
| Matrix2D | 旋转后结果矩阵对象。 |

**示例：**

 收起自动换行深色代码主题复制

```
// xxx.ets @Entry @Component struct Rotate { private settings : RenderingContextSettings = new RenderingContextSettings ( true ); private context : CanvasRenderingContext2D = new CanvasRenderingContext2D ( this . settings ); private matrix : Matrix2D = new Matrix2D (); build ( ) { Flex ({ direction : FlexDirection . Column , alignItems : ItemAlign . Center , justifyContent : FlexAlign . Center }) { Canvas ( this . context ) . width ( '240vp' ) . height ( '180vp' ) . backgroundColor ( '#ffff00' ) . onReady ( () => { this . context . fillRect ( 50 , 110 , 50 , 50 ) this . matrix . scaleX = 1 this . matrix . scaleY = 1 this . matrix . rotateX = - 0.5 this . matrix . rotateY = 0.5 this . matrix . translateX = 10 this . matrix . translateY = 10 this . matrix . rotate ( 5 , 5 ) this . context . setTransform ( this . matrix ) this . context . fillRect ( 50 , 110 , 50 , 50 ) }) } . width ( '100%' ) . height ( '100%' ) } }
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170640.27002348540790603625139925961048:50001231000000:2800:C9E8198A1D78789907B38B1FD7E33DB5EB85D0CDF4DFAA608567AAE5CF5451DE.png)

### rotate 10+

支持设备PhonePC/2in1TabletTVWearable

rotate(degree: number, rx?: number, ry?: number): Matrix2D

以旋转点为中心，对当前矩阵进行右乘旋转运算。

**卡片能力：** 从API version 10开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

 展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| degree | number | 是 | 旋转角度，取值范围无限制。顺时针方向为正角度，可以通过 degree * Math.PI / 180 将角度转换为弧度值。 异常值undefined和null按无效值处理，NaN和Infinity会导致Matrix2D异常。 默认单位：弧度 |
| rx | number | 否 | 旋转点的水平方向坐标，取值范围无限制。 默认单位：vp 异常值undefined和null按无效值处理，NaN和Infinity会导致Matrix2D异常。 默认值：0 |
| ry | number | 否 | 旋转点的垂直方向坐标，取值范围无限制。 默认单位：vp 异常值undefined和null按无效值处理，NaN和Infinity会导致Matrix2D异常。 默认值：0 |

**返回值：**

 展开

| 类型 | 说明 |
| --- | --- |
| Matrix2D | 旋转后结果矩阵对象。 |

**示例：**

 收起自动换行深色代码主题复制

```
// xxx.ets @Entry @Component struct Rotate { private settings : RenderingContextSettings = new RenderingContextSettings ( true ); private context : CanvasRenderingContext2D = new CanvasRenderingContext2D ( this . settings ); private matrix : Matrix2D = new Matrix2D (); build ( ) { Flex ({ direction : FlexDirection . Column , alignItems : ItemAlign . Center , justifyContent : FlexAlign . Center }) { Canvas ( this . context ) . width ( '240vp' ) . height ( '180vp' ) . backgroundColor ( '#ffff00' ) . onReady ( () => { this . context . fillRect ( 60 , 80 , 50 , 50 ) this . matrix . scaleX = 1 this . matrix . scaleY = 1 this . matrix . rotateX = - 0.5 this . matrix . rotateY = 0.5 this . matrix . translateX = 10 this . matrix . translateY = 10 this . matrix . rotate (- 60 * Math . PI / 180 , 5 , 5 ) this . context . setTransform ( this . matrix ) this . context . fillRect ( 60 , 80 , 50 , 50 ) }) } . width ( '100%' ) . height ( '100%' ) } }
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170640.48724176718942940685901381371333:50001231000000:2800:705AC8D9D3E61B95D93EA40A7A235087B4A3EB55A995476D6282DD88F1AC5726.png)

### translate

支持设备PhonePC/2in1TabletTVWearable

translate(tx?: number, ty?: number): Matrix2D

对当前矩阵进行左乘平移运算。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

 展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tx | number | 否 | 水平方向平移距离，取值范围无限制。 异常值undefined和null按无效值处理，NaN和Infinity会导致Matrix2D异常。 默认单位：vp 默认值：0 |
| ty | number | 否 | 垂直方向平移距离，取值范围无限制。 异常值undefined和null按无效值处理，NaN和Infinity会导致Matrix2D异常。 默认单位：vp 默认值：0 |

**返回值：**

 展开

| 类型 | 说明 |
| --- | --- |
| Matrix2D | 平移后结果矩阵对象。 |

**示例：**

 收起自动换行深色代码主题复制

```
// xxx.ets @Entry @Component struct Translate { private settings : RenderingContextSettings = new RenderingContextSettings ( true ); private context : CanvasRenderingContext2D = new CanvasRenderingContext2D ( this . settings ); private matrix : Matrix2D = new Matrix2D (); build ( ) { Flex ({ direction : FlexDirection . Column , alignItems : ItemAlign . Center , justifyContent : FlexAlign . Center }) { Canvas ( this . context ) . width ( '240vp' ) . height ( '180vp' ) . backgroundColor ( '#ffff00' ) . onReady ( () => { this . context . fillRect ( 40 , 20 , 50 , 50 ) this . matrix . scaleX = 1 this . matrix . scaleY = 1 this . matrix . rotateX = 0 this . matrix . rotateY = 0 this . matrix . translateX = 0 this . matrix . translateY = 0 this . matrix . translate ( 100 , 100 ) this . context . setTransform ( this . matrix ) this . context . fillRect ( 40 , 20 , 50 , 50 ) }) } . width ( '100%' ) . height ( '100%' ) } }
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170640.55132503191154112354377372274188:50001231000000:2800:A9D31F67B6C6CB47D00908B30F2F23DE2460ABFE9E1F66AC1F4BD297612D7803.png)

### scale

支持设备PhonePC/2in1TabletTVWearable

scale(sx?: number, sy?: number): Matrix2D

对当前矩阵进行右乘缩放运算。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

 展开

| 参数 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| sx | number | 否 | 水平缩放比例系数，取值范围无限制。 异常值undefined和null按无效值处理，NaN和Infinity会导致Matrix2D异常。 默认值：1.0 |
| sy | number | 否 | 垂直缩放比例系数，取值范围无限制。 异常值undefined和null按无效值处理，NaN和Infinity会导致Matrix2D异常。 默认值：1.0 |

**返回值：**

 展开

| 类型 | 说明 |
| --- | --- |
| Matrix2D | 缩放结果矩阵对象。 |

**示例：**

 收起自动换行深色代码主题复制

```
// xxx.ets @Entry @Component struct Scale { private settings : RenderingContextSettings = new RenderingContextSettings ( true ); private context : CanvasRenderingContext2D = new CanvasRenderingContext2D ( this . settings ); private matrix : Matrix2D = new Matrix2D (); build ( ) { Flex ({ direction : FlexDirection . Column , alignItems : ItemAlign . Center , justifyContent : FlexAlign . Center }) { Canvas ( this . context ) . width ( '240vp' ) . height ( '180vp' ) . backgroundColor ( '#ffff00' ) . onReady ( () => { this . context . fillRect ( 120 , 70 , 50 , 50 ) this . matrix . scaleX = 1 this . matrix . scaleY = 1 this . matrix . rotateX = - 0.5 this . matrix . rotateY = 0.5 this . matrix . translateX = 10 this . matrix . translateY = 10 this . matrix . scale ( 0.5 , 0.5 ) this . context . setTransform ( this . matrix ) this . context . fillRect ( 120 , 70 , 50 , 50 ) }) } . width ( '100%' ) . height ( '100%' ) } }
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170640.47469383108921975536240718649491:50001231000000:2800:3C89F5623AFE0294C6C539899587A3107D276AD12380756FC3FCF48CE82057CF.png)