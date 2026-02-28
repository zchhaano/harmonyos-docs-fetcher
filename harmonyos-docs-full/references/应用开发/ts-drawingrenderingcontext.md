# DrawingRenderingContext

DrawingRenderingContext对象与Canvas组件绑定后，可在Canvas组件上进行绘制，绘制对象可以是形状、文本、图片等。

 说明 

从API version 12开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## constructor

 支持设备PhonePC/2in1TabletTVWearable

constructor(unit?: LengthMetricsUnit)

构造使用drawing接口进行绘制的Canvas画布对象，支持配置DrawingRenderingContext对象的单位模式。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| unit | LengthMetricsUnit | 否 | 用来配置DrawingRenderingContext对象的单位模式，配置后无法更改，配置方法同 CanvasRenderingContext2D 。 异常值undefined、NaN和Infinity按默认值处理。 默认值：DEFAULT |

## size

 支持设备PhonePC/2in1TabletTVWearable

get size(): Size

获取DrawingRenderingContext的大小。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

  展开

| 类型 | 说明 |
| --- | --- |
| Size | DrawingRenderingContext的尺寸信息。 |

## canvas

 支持设备PhonePC/2in1TabletTVWearable

get canvas(): DrawingCanvas

获取绘制内容的画布对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

  展开

| 类型 | 说明 |
| --- | --- |
| DrawingCanvas | 绘制内容的画布对象。 |

## invalidate

 支持设备PhonePC/2in1TabletTVWearable

invalidate(): void

使组件无效，触发组件的重新渲染。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## DrawingCanvas 12+ 对象说明

 支持设备PhonePC/2in1TabletTVWearable

type DrawingCanvas = Canvas

可用于向XComponent上绘制内容的画布对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

  展开

| 类型 | 说明 |
| --- | --- |
| Canvas | 返回一个Canvas对象。 |

## Size

 支持设备PhonePC/2in1TabletTVWearable

DrawingRenderingContext的尺寸信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

  展开

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| width | number | 否 | 否 | 获取DrawingRenderingContext的宽度，其值为关联的Canvas组件的宽度。 |
| height | number | 否 | 否 | 获取DrawingRenderingContext的高度，其值为关联的Canvas组件的高度。 |

## 示例

 支持设备PhonePC/2in1TabletTVWearable  

### 示例1（绘制图形）

该示例实现了如何使用DrawingRenderingContext中的方法绘制图形。

 收起自动换行深色代码主题复制

```
import { common2D, drawing } from '@kit.ArkGraphics2D' ; // xxx.ets @Entry @Component struct CanvasExample { private context : DrawingRenderingContext = new DrawingRenderingContext (); build ( ) { Flex ({ direction : FlexDirection . Column , alignItems : ItemAlign . Center , justifyContent : FlexAlign . Center }) { Canvas ( this . context ) . width ( '100%' ) . height ( '50%' ) . backgroundColor ( '#D5D5D5' ) . onReady ( () => { let brush = new drawing. Brush (); // 使用RGBA(39, 135, 217, 255)填充圆心为(200, 200)，半径为100的圆 brush. setColor ({ alpha : 255 , red : 39 , green : 135 , blue : 217 }); this . context . canvas . attachBrush (brush); this . context . canvas . drawCircle ( 200 , 200 , 100 ); this . context . canvas . detachBrush (); this . context . invalidate (); }) Button ( "Clear" ) . width ( '120' ) . height ( '50' ) . onClick ( () => { let color : common2D. Color = { alpha : 0 , red : 0 , green : 0 , blue : 0 }; // 使用RGBA(0, 0, 0, 0)填充画布 this . context . canvas . clear (color); this . context . invalidate (); }) } . width ( '100%' ) . height ( '100%' ) } }
```

图1 绘制圆心为(200, 200)，半径为100的圆，填充色为RGBA(39, 135, 217, 255)

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170559.21889166761995024470481391148035:50001231000000:2800:E170AC42C27E05678781AA62495D60955D7A8F6CE1F8D1EC400ED827AD782517.png)

图2 点击Clear按钮清空画布

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170559.91033872612610990294978284428573:50001231000000:2800:11656AF3B5C21838F54A77FFA2E186D5E514A66ACD607A310DD23DDC91965621.png)

### 示例2（绘制文本）

该示例实现了通过[makeFromRawFile](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-graphics-drawing-typeface#makefromrawfile18)（从API version 18开始）加载自定义字体。并使用[drawTextBlob](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-graphics-drawing-canvas#drawtextblob)绘制文本，drawing接口绘制自定义文字时，不需要调用this.uiContext.getFont().[registerFont](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-font#registerfont)或者fontCollection.[loadFontSync](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-graphics-text#loadfontsync)提前注册字体，而是通过drawing.Typeface.[makeFromRawFile](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-graphics-drawing-typeface#makefromrawfile18)（从API version 18开始）传入rawfile目录下的自定义字体文件。

 收起自动换行深色代码主题复制

```
import { drawing } from '@kit.ArkGraphics2D' ; // xxx.ets @Entry @Component struct CanvasExample { private context : DrawingRenderingContext = new DrawingRenderingContext (); build ( ) { Flex ({ direction : FlexDirection . Column , alignItems : ItemAlign . Center , justifyContent : FlexAlign . Center }) { Canvas ( this . context ) . width ( '100%' ) . height ( '50%' ) . backgroundColor ( '#D5D5D5' ) . onReady ( () => { let font = new drawing. Font (); font. setSize ( 50 ); // 加载rawfile目录下的自定义字体文件HarmonyOS_Sans_Bold.ttf const myTypeFace = drawing. Typeface . makeFromRawFile ($rawfile( 'HarmonyOS_Sans_Bold.ttf' )); font. setTypeface (myTypeFace); const textBlob = drawing. TextBlob . makeFromString ( "Hello World" , font, drawing. TextEncoding . TEXT_ENCODING_UTF8 ); this . context . canvas . drawTextBlob (textBlob, 60 , 100 ); this . context . invalidate (); }) } . width ( '100%' ) . height ( '100%' ) } }
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170559.30710037902442746725585580343994:50001231000000:2800:DACADC3D80C0C4804AAC802D7FD47ECF1FE30CA41F0CCFC47295A4785CF8F65E.png)