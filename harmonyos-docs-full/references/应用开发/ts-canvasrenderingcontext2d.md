# CanvasRenderingContext2D

CanvasRenderingContext2D对象与Canvas组件绑定后，可在Canvas组件上绘制，绘制对象可以是形状、文本、图片等。

 说明 

- 从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
- 建议使用时将CanvasRenderingContext2D对象与Canvas组件封装到同一个自定义组件中，保证两者一一对应且生命周期保持一致。
- 本文绘制接口在调用时会存入被关联的Canvas组件的指令队列中。仅当当前帧进入渲染阶段且关联的Canvas组件处于可见状态时，这些指令才会从队列中被提取并执行。因此，在Canvas组件不可见的情况下，应尽量避免频繁调用绘制接口，以防止指令在队列中堆积，从而避免内存占用过大的问题，具体示例请参考[控制在画布组件不可见时不进行绘制](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-drawing-customization-on-canvas#控制在画布组件不可见时不进行绘制)。
- Canvas组件的宽或高超过8000px时使用CPU渲染，会导致性能明显下降。

## 构造函数

 支持设备PhonePC/2in1TabletTVWearable  

### constructor

 支持设备PhonePC/2in1TabletTVWearable

constructor(settings?: RenderingContextSettings)

构造Canvas画布对象，支持配置CanvasRenderingContext2D对象的参数。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| settings | RenderingContextSettings | 否 | 用来配置CanvasRenderingContext2D对象的参数，见 RenderingContextSettings 。 异常值undefined和null按 RenderingContextSettings 的默认值处理。 |

### constructor 12+

 支持设备PhonePC/2in1TabletTVWearable

constructor(settings?: RenderingContextSettings, unit?: LengthMetricsUnit)

构造Canvas画布对象，支持配置CanvasRenderingContext2D对象的参数和单位模式。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| settings | RenderingContextSettings | 否 | 用来配置CanvasRenderingContext2D对象的参数，见 RenderingContextSettings 。 异常值undefined和null按 RenderingContextSettings 的默认值处理。 |
| unit | LengthMetricsUnit | 否 | 用来配置CanvasRenderingContext2D对象的单位模式，配置后无法更改。 异常值undefined、NaN和Infinity按默认值处理。 默认值：DEFAULT |

**示例：**

以下示例展示了配置CanvasRenderingContext2D对象的单位模式，默认单位模式为LengthMetricsUnit.DEFAULT，对应默认单位vp，配置后无法动态更改。详细说明见[LengthMetricsUnit](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-graphics#lengthmetricsunit12)。

```
// xxx.ets
import { LengthMetricsUnit } from '@kit.ArkUI'

@Entry
@Component
struct LengthMetricsUnitDemo {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private contextPX: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings, LengthMetricsUnit.PX);
  private contextVP: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.contextPX)
        .width('100%')
        .height(150)
        .backgroundColor('#ffff00')
        .onReady(() => {
          this.contextPX.fillRect(10,10,100,100)
          this.contextPX.clearRect(10,10,50,50)
        })

      Canvas(this.contextVP)
        .width('100%')
        .height(150)
        .backgroundColor('#ffff00')
        .onReady(() => {
          this.contextVP.fillRect(10,10,100,100)
          this.contextVP.clearRect(10,10,50,50)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170541.47296989585047629561392859846739:50001231000000:2800:9B462E692BF6AE76B21B2BC82C7F2AF94D192F6580457786ABB32DDB7CB41806.png)

## 属性

 支持设备PhonePC/2in1TabletTVWearable说明 

fillStyle、shadowColor与 strokeStyle 中string类型格式为rgb(255, 255, 255)、rgba(255, 255, 255, 1.0)或者#FFFFFF。

### fillStyle

 支持设备PhonePC/2in1TabletTVWearable

指定绘制的填充色，此属性为只写属性，可通过赋值语句设置其值，但无法通过读取操作获取其当前值，若尝试读取将返回undefined。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

  展开

| 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- |
| string \|number 10+ \| CanvasGradient \| CanvasPattern | 否 | 否 | - 类型为string时，表示设置填充区域的颜色，颜色格式参考 ResourceColor 中string类型说明。 - 类型为number时，表示设置填充区域的颜色，不支持设置全透明色，颜色格式参考 ResourceColor 中number类型说明。 - 类型为CanvasGradient时，表示渐变对象，使用 createLinearGradient 方法创建。 - 类型为CanvasPattern时，使用 createPattern 方法创建。 默认值：'#000000'（黑色） 异常值设置无效。 |

```
// xxx.ets
@Entry
@Component
struct FillStyleExample {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          this.context.fillStyle = '#0000ff'
          this.context.fillRect(20, 20, 150, 100)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170541.15552548795775499215830168990008:50001231000000:2800:476DC77C2B3A82CDFFBEB395DD4A45CB063A399112F183344FCF28773C9D01BC.png)

### lineWidth

 支持设备PhonePC/2in1TabletTVWearable

设置绘制线条的宽度，此属性为只写属性，可通过赋值语句设置其值，但无法通过读取操作获取其当前值，若尝试读取将返回undefined。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

  展开

| 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- |
| number | 否 | 否 | 默认值：1（px） 默认单位：vp lineWidth取值不支持0和负数，0、负数和NaN按默认值处理，Infinity会导致lineWidth属性异常。 |

```
// xxx.ets
@Entry
@Component
struct LineWidthExample {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
        this.context.lineWidth = 5
        this.context.strokeRect(25, 25, 85, 105)
      })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170541.28201731589005505105709800214988:50001231000000:2800:F63C6320FE25F6084B848021E72456712CAEBC277614D81F5382C7CB1BE797B3.png)

### strokeStyle

 支持设备PhonePC/2in1TabletTVWearable

设置线条的颜色，此属性为只写属性，可通过赋值语句设置其值，但无法通过读取操作获取其当前值，若尝试读取将返回undefined。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

  展开

| 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- |
| string \|number 10+ \| CanvasGradient \| CanvasPattern | 否 | 否 | - 类型为string时，表示设置线条使用的颜色，颜色格式参考 ResourceColor 中string类型说明。 - 类型为number时，表示设置线条使用的颜色，不支持设置全透明色，颜色格式参考 ResourceColor 中number类型说明。 - 类型为CanvasGradient时，表示渐变对象，使用 createLinearGradient 方法创建。 - 类型为CanvasPattern时，使用 createPattern 方法创建。 默认值：'#000000'（黑色） 异常值设置无效。 |

```
// xxx.ets
@Entry
@Component
struct StrokeStyleExample {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          this.context.lineWidth = 10
          this.context.strokeStyle = '#0000ff'
          this.context.strokeRect(25, 25, 155, 105)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170541.57700973529397193493738080567172:50001231000000:2800:754BE5AD6DACFF9E121EDCE1197C0015710AB80B26CB6003CC57C1B84F66D97F.png)

### lineCap

 支持设备PhonePC/2in1TabletTVWearable

指定线端点的样式，此属性为只写属性，可通过赋值语句设置其值，但无法通过读取操作获取其当前值，若尝试读取将返回undefined。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

  展开

| 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- |
| CanvasLineCap | 否 | 否 | 默认值：'butt' |

```
// xxx.ets
@Entry
@Component
struct LineCapExample {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('rgb(213,213,213)')
        .onReady(() => {
          this.context.lineWidth = 8
          this.context.beginPath()
          this.context.lineCap = 'round'
          this.context.moveTo(30, 50)
          this.context.lineTo(220, 50)
          this.context.stroke()
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170541.92216020042031850694959603790126:50001231000000:2800:8794C69394820E6ADB1E1BB7FFC0E8ABE74C2B632DDBF8C0C7BA7D06BA9D32CA.png)

### lineJoin

 支持设备PhonePC/2in1TabletTVWearable

指定线段间相交的交点样式，此属性为只写属性，可通过赋值语句设置其值，但无法通过读取操作获取其当前值，若尝试读取将返回undefined。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

  展开

| 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- |
| CanvasLineJoin | 否 | 否 | 可选值为： - 'round'：在线段相连处绘制一个扇形，扇形的圆角半径是线段的宽度。 - 'bevel'：在线段相连处使用三角形为底填充， 每个部分矩形拐角独立。 - 'miter'：在相连部分的外边缘处进行延伸，使其相交于一点，形成一个菱形区域，该属性可以通过设置miterLimit属性展现效果。 默认值：'miter' |

```
// xxx.ets
@Entry
@Component
struct LineJoinExample {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
        this.context.beginPath()
        this.context.lineWidth = 8
        this.context.lineJoin = 'miter'
        this.context.moveTo(30, 30)
        this.context.lineTo(120, 60)
        this.context.lineTo(30, 110)
        this.context.stroke()
      })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170541.99869094303286117568876642858715:50001231000000:2800:A1F227B609C6B0ECF57D54A67E673D86C67BA087C906EEFF6209D987FD1516B2.png)

### miterLimit

 支持设备PhonePC/2in1TabletTVWearable

设置斜接面限制值，该值指定了线条相交处内角和外角的距离，仅当设置了lineJoin为miter才生效，此属性为只写属性，可通过赋值语句设置其值，但无法通过读取操作获取其当前值，若尝试读取将返回undefined。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

  展开

| 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- |
| number | 否 | 否 | 默认值：10px 单位：px miterLimit取值不支持0和负数，0、负数和NaN按默认值处理，Infinity会导致miterLimit属性异常。 |

```
// xxx.ets
@Entry
@Component
struct MiterLimit {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          this.context.lineWidth = 8
          this.context.lineJoin = 'miter'
          this.context.miterLimit = 3
          this.context.moveTo(30, 30)
          this.context.lineTo(60, 35)
          this.context.lineTo(30, 37)
          this.context.stroke()
      })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170541.99845924319404438968724625675041:50001231000000:2800:ADD94EA1A44FECEB627ECBA9F03EAD9FCCF36E316BEEDC6BCC68B775D0EBF779.png)

### font

 支持设备PhonePC/2in1TabletTVWearable

设置文本绘制中的字体样式，此属性为只写属性，可通过赋值语句设置其值，但无法通过读取操作获取其当前值，若尝试读取将返回undefined。

语法：ctx.font = 'font-style font-weight font-size font-family'

- font-style(可选)，用于指定字体样式，支持如下几种样式：'normal','italic'。

- font-weight(可选)，用于指定字体的粗细，支持如下几种类型：'normal', 'bold', 'bolder', 'lighter', 100, 200, 300, 400, 500, 600, 700, 800, 900。

- font-size(可选)，指定字号和行高，单位支持px、vp。使用时需要添加单位。

- font-family(可选)，指定字体系列，支持如下几种类型：'sans-serif', 'serif', 'monospace'。

从API version 20开始，支持通过该接口设置注册过的自定义字体（DevEco Studio的预览器不支持显示自定义字体）。自定义字体注册有以下两种方式。一种是通过ArkUI的异步接口this.uiContext.getFont().[registerFont](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-font#registerfont)注册，调用后立即绘制可能会导致自定义字体不生效。另一种是直接调用字体引擎的fontCollection.[loadFontSync](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-graphics-text#loadfontsync)接口来注册自定义字体到字体引擎。在直接调用字体引擎接口注册自定义字体时，fontCollection的实例需要是text.FontCollection.getGlobalInstance()，因为组件默认会从该实例加载字体。如果使用其他实例，可能会导致自定义字体不生效。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

  展开

| 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- |
| string | 否 | 否 | 默认值：'normal normal 14px sans-serif' 卡片能力： 从API version 9开始，该接口支持在ArkTS卡片中使用。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |

```
// xxx.ets
import { text } from '@kit.ArkGraphics2D';

@Entry
@Component
struct FontDemo {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('rgb(213,213,213)')
        .onReady(() => {
          // 常规字体样式，常规粗细，字体大小为30px，字体系列为sans-serif
          this.context.font = 'normal normal 30px sans-serif'
          this.context.fillText("Hello px", 20, 60)
          // 斜体样式，加粗，字体大小为30vp，字体系列为monospace
          this.context.font = 'italic bold 30vp monospace'
          this.context.fillText("Hello vp", 20, 100)
          // 加载rawfile目录下的自定义字体文件HarmonyOS_Sans_Thin_Italic.ttf
          let fontCollection = text.FontCollection.getGlobalInstance();
          fontCollection.loadFontSync('HarmonyOS_Sans_Thin_Italic', $rawfile("HarmonyOS_Sans_Thin_Italic.ttf"))
          // 加粗，字体大小为30vp，字体系列为HarmonyOS_Sans_Thin_Italic
          this.context.font = "bold 30vp HarmonyOS_Sans_Thin_Italic"
          this.context.fillText("Hello customFont", 20, 140)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170542.79056134168042439024498429238504:50001231000000:2800:A4CBAE846E0641CA470DEE082C34BC024977F128C410F0153E099098067CF809.jpeg)

### textAlign

 支持设备PhonePC/2in1TabletTVWearable

设置文本绘制中的文本对齐方式，此属性为只写属性，可通过赋值语句设置其值，但无法通过读取操作获取其当前值，若尝试读取将返回undefined。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

  展开

| 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- |
| CanvasTextAlign | 否 | 否 | ltr布局模式下'start'和'left'一致，rtl布局模式下'start'和'right'一致。 默认值：'left' |

```
// xxx.ets
@Entry
@Component
struct CanvasExample {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('rgb(213,213,213)')
        .onReady(() => {
          this.context.strokeStyle = 'rgb(39,135,217)'
          this.context.moveTo(140, 10)
          this.context.lineTo(140, 160)
          this.context.stroke()
          this.context.font = '50px sans-serif'
          this.context.textAlign = 'start'
          this.context.fillText('textAlign=start', 140, 60)
          this.context.textAlign = 'end'
          this.context.fillText('textAlign=end', 140, 80)
          this.context.textAlign = 'left'
          this.context.fillText('textAlign=left', 140, 100)
          this.context.textAlign = 'center'
          this.context.fillText('textAlign=center', 140, 120)
          this.context.textAlign = 'right'
          this.context.fillText('textAlign=right', 140, 140)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170542.61290932348025992999016912799022:50001231000000:2800:A74AD8F40F0F354BA1F04261E68A7CFC91D262B0EA8D996058E5B3550BA01049.png)

### textBaseline

 支持设备PhonePC/2in1TabletTVWearable

设置文本绘制中的水平对齐方式，此属性为只写属性，可通过赋值语句设置其值，但无法通过读取操作获取其当前值，若尝试读取将返回undefined。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

  展开

| 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- |
| CanvasTextBaseline | 否 | 否 | 默认值：'alphabetic' |

```
// xxx.ets
@Entry
@Component
struct TextBaseline {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('rgb(213,213,213)')
        .onReady(() => {
          this.context.strokeStyle = 'rgb(0,0,255)'
          this.context.moveTo(0, 120)
          this.context.lineTo(400, 120)
          this.context.stroke()
          this.context.font = '20px sans-serif'
          this.context.textBaseline = 'top'
          this.context.fillText('Top', 10, 120)
          this.context.textBaseline = 'bottom'
          this.context.fillText('Bottom', 55, 120)
          this.context.textBaseline = 'middle'
          this.context.fillText('Middle', 125, 120)
          this.context.textBaseline = 'alphabetic'
          this.context.fillText('Alphabetic', 195, 120)
          this.context.textBaseline = 'hanging'
          this.context.fillText('Hanging', 295, 120)
      })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170542.39322253652735717365456810702364:50001231000000:2800:5E0B374F7877AAA1FB20E0EFB8A112B49238A2FC10CC222D7D631D9641A79155.jpg)

### globalAlpha

 支持设备PhonePC/2in1TabletTVWearable

设置透明度，此属性为只写属性，可通过赋值语句设置其值，但无法通过读取操作获取其当前值，若尝试读取将返回undefined。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

  展开

| 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- |
| number | 否 | 否 | 范围为[0.0, 1.0]，0.0为完全透明，1.0为完全不透明。若给定值小于0.0，则取值0.0；若给定值大于1.0，则取值1.0. API version 18之前，设置NaN或Infinity时，在该方法后执行的绘制方法无法绘制。API version 18及以后，设置NaN或Infinity时当前接口不生效，其他传入有效参数的绘制方法正常绘制。 默认值：1.0 |

```
// xxx.ets
@Entry
@Component
struct GlobalAlpha {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          this.context.fillStyle = 'rgb(0,0,255)'
          this.context.fillRect(0, 0, 50, 50)
          this.context.globalAlpha = 0.4
          this.context.fillStyle = 'rgb(0,0,255)'
          this.context.fillRect(50, 50, 50, 50)
      })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170542.57928052549253334297283223014684:50001231000000:2800:B3E94B13FB03F1DA11C5FA662489C571EC70369801A1B418E542921C07F5BDA1.png)

### lineDashOffset

 支持设备PhonePC/2in1TabletTVWearable

设置画布的虚线偏移量，精度为float，仅当设置setLineDash时属性才生效，此属性为只写属性，可通过赋值语句设置其值，但无法通过读取操作获取其当前值，若尝试读取将返回undefined。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

  展开

| 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- |
| number | 否 | 否 | API version 18之前，设置NaN或Infinity时，设置了虚线样式的线条绘制出来是实线。API version 18及以后，设置NaN或Infinity时当前接口不生效，设置了虚线样式的线条绘制出来是虚线。 默认值：0.0 默认单位：vp 异常值NaN和Infinity按默认值处理。 |

```
// xxx.ets
import { AnimatorResult } from '@kit.ArkUI';

@Entry
@Component
struct LineDashOffset {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private animator: AnimatorResult | undefined = undefined;

  drawAntLine() { // 实现蚂蚁线动画
    this.animator = this.getUIContext().createAnimator({
      duration: 2000,
      easing: 'linear',
      delay: 0,
      fill: 'none',
      direction: 'normal',
      iterations: -1,
      begin: 0, // 动画插值起点
      end: 1 // 动画插值终点
    });
    this.animator.onFrame = (value: number) => {
      this.context.reset();
      this.context.lineWidth = 2;
      this.context.setLineDash([10, 5]);
      this.context.lineDashOffset = 105 * value;
      this.context.strokeRect(10, 10, 100, 100);
    };
    this.animator.play();
  }

  aboutToDisappear() {
    this.animator?.finish();
    this.animator = undefined;
  }

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('rgb(213,213,213)')
        .onReady(() => {
          this.drawAntLine();
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170542.21178663306212525263620264550365:50001231000000:2800:5D8C485BAB5EC6ACC33FA741B5A0B82D24F86897EBF06DDFAAE3472FB5807314.gif)

### globalCompositeOperation

 支持设备PhonePC/2in1TabletTVWearable

设置合成操作的方式，此属性为只写属性，可通过赋值语句设置其值，但无法通过读取操作获取其当前值，若尝试读取将返回undefined。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

  展开

| 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- |
| string | 否 | 否 | 类型字段可选值有'source-over'，'source-atop'，'source-in'，'source-out'，'destination-over'，'destination-atop'，'destination-in'，'destination-out'，'lighter'，'copy'，'xor'。 默认值：'source-over' |

   展开

| 名称 | 描述 |
| --- | --- |
| source-over | 在现有绘制内容上显示新绘制内容，属于默认值。 |
| source-atop | 在现有绘制内容顶部显示新绘制内容。 |
| source-in | 在现有绘制内容中显示新绘制内容。 |
| source-out | 在现有绘制内容之外显示新绘制内容。 |
| destination-over | 在新绘制内容上方显示现有绘制内容。 |
| destination-atop | 在新绘制内容顶部显示现有绘制内容。 |
| destination-in | 在新绘制内容中显示现有绘制内容。 |
| destination-out | 在新绘制内容外显示现有绘制内容。 |
| lighter | 显示新绘制内容和现有绘制内容。 |
| copy | 显示新绘制内容而忽略现有绘制内容。 |
| xor | 使用异或操作对新绘制内容与现有绘制内容进行融合。 |

```
// xxx.ets
@Entry
@Component
struct GlobalCompositeOperation {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context1: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private context2: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private context3: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private context4: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private context5: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private context6: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);

  build() {
    Column() {
      Row() {
        // 1. source-over：新图形覆盖在原有图形上方（默认行为）
        Canvas(this.context1)
          .width('45%')
          .borderWidth(1)
          .margin(5)
          .onReady(() => {
            let ctx1 = this.context1;
            ctx1.fillStyle = 'rgb(39,135,217)';
            ctx1.fillRect(25, 25, 75, 75); // 原有图形
            ctx1.globalCompositeOperation = 'source-over'; // 默认值，可省略
            ctx1.fillStyle = 'rgb(23,169,141)';
            ctx1.fillRect(75, 75, 75, 75); // 新图形覆盖
          })
        // 2. destination-out：新图形擦除原有图形（橡皮擦核心逻辑）
        Canvas(this.context2)
          .width('45%')
          .borderWidth(1)
          .margin(5)
          .onReady(() => {
            let ctx2 = this.context2;
            // 先绘制背景
            ctx2.fillStyle = 'rgb(39,135,217)';
            ctx2.fillRect(0, 0, ctx2.width, ctx2.height);
            // 设置合成模式为擦除
            ctx2.globalCompositeOperation = 'destination-out';
            // 绘制圆形作为橡皮擦
            ctx2.beginPath();
            ctx2.arc(ctx2.width / 2, ctx2.height / 2, 60, 0, Math.PI * 2);
            ctx2.fill(); // 擦除圆形区域的背景
          })
      }
      .height('30%')

      Row() {
        // 3. source-in：仅保留新图形与原有图形重叠的部分（裁剪或蒙版）
        Canvas(this.context3)
          .width('45%')
          .borderWidth(1)
          .margin(5)
          .onReady(() => {
            let ctx3 = this.context3;
            // 先绘制原有图形（圆形蒙版）
            ctx3.beginPath();
            ctx3.arc(ctx3.width / 2, ctx3.height / 2, 80, 0, Math.PI * 2);
            ctx3.fillStyle = '#fff';
            ctx3.fill();
            // 设置合成模式
            ctx3.globalCompositeOperation = 'source-in';
            // 绘制新图形（渐变矩形）
            const gradient = ctx3.createLinearGradient(0, 0, ctx3.width, ctx3.height);
            gradient.addColorStop(0, 'rgb(23,169,141)');
            gradient.addColorStop(1, 'rgb(39,135,217)');
            ctx3.fillStyle = gradient;
            ctx3.fillRect(0, 0, 200, 200); // 仅圆形区域显示渐变
          })
        // 4. lighter：新图形与原有图形叠加（亮度相加，滤色效果）
        Canvas(this.context4)
          .width('45%')
          .borderWidth(1)
          .margin(5)
          .onReady(() => {
            let ctx4 = this.context4;
            // 原有图形（半透明红色圆）
            ctx4.beginPath();
            ctx4.arc(70, 100, 50, 0, Math.PI * 2);
            ctx4.fillStyle = 'rgba(234, 67, 53, 0.7)';
            ctx4.fill();
            // 设置合成模式
            ctx4.globalCompositeOperation = 'lighter';
            // 新图形（半透明蓝色圆）
            ctx4.beginPath();
            ctx4.arc(110, 100, 50, 0, Math.PI * 2);
            ctx4.fillStyle = 'rgba(66, 133, 244, 0.7)';
            ctx4.fill(); // 重叠区域变成紫色（亮度叠加）
          })
      }
      .height('30%')

      Row() {
        // 5. destination-atop：保留原有图形与新图形重叠的部分，移除其他区域
        Canvas(this.context5)
          .width('45%')
          .borderWidth(1)
          .margin(5)
          .onReady(() => {
            let ctx5 = this.context5;
            // 原有图形（绿色矩形）
            ctx5.fillStyle = 'rgb(23,169,141)';
            ctx5.fillRect(0, 0, ctx5.width, ctx5.height);
            // 设置合成模式
            ctx5.globalCompositeOperation = 'destination-atop';
            // 新图形（小圆形）
            ctx5.beginPath();
            ctx5.arc(ctx5.width / 2, ctx5.height / 2, 60, 0, Math.PI * 2);
            ctx5.fillStyle = '#000';
            ctx5.fill(); // 仅矩形与圆形重叠的部分保留
          })
        // 6. 文字蒙版（“source-in”的高级用法）
        Canvas(this.context6)
          .width('45%')
          .borderWidth(1)
          .margin(5)
          .onReady(() => {
            let ctx6 = this.context6
            // 先绘制文字（作为蒙版）
            ctx6.font = 'bold 40vp';
            ctx6.textAlign = 'center';
            ctx6.textBaseline = 'middle';
            ctx6.fillText('CANVAS', ctx6.width / 2, ctx6.height / 2);
            // 设置合成模式
            ctx6.globalCompositeOperation = 'source-in';
            // 绘制渐变背景（仅文字区域显示）
            let textGradient = ctx6.createLinearGradient(50, 0, 300, 100);
            textGradient.addColorStop(0.0, 'rgb(39,135,217)');
            textGradient.addColorStop(0.5, 'rgb(255,238,240)');
            textGradient.addColorStop(1.0, 'rgb(23,169,141)');
            ctx6.fillStyle = textGradient;
            ctx6.fillRect(0, 0, 200, 200); // 渐变仅填充文字区域
          })
      }
      .height('30%')
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170542.68700389017057358707704436335070:50001231000000:2800:40536AD38D6A3C987A5FC24476B10FA0F0055D4C4FB3C95D0B86F01F7977050E.png)

### shadowBlur

 支持设备PhonePC/2in1TabletTVWearable

设置绘制阴影时的模糊级别，此属性为只写属性，可通过赋值语句设置其值，但无法通过读取操作获取其当前值，若尝试读取将返回undefined。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

  展开

| 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- |
| number | 否 | 否 | 值越大越模糊，精度为float，取值范围≥0。 默认值：0.0 单位：px shadowBlur取值不支持负数，负数、NaN和Infinity按默认值处理。 |

```
// xxx.ets
@Entry
@Component
struct ShadowBlur {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          this.context.shadowBlur = 30
          this.context.shadowColor = 'rgb(0,0,0)'
          this.context.fillStyle = 'rgb(255,0,0)'
          this.context.fillRect(20, 20, 100, 80)
      })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170542.31421749037120615893714019831875:50001231000000:2800:918D553132C0AB609B57E610584EDDDAFD0F547A97E5AD1DC32C6F63C3917FE1.png)

### shadowColor

 支持设备PhonePC/2in1TabletTVWearable

设置绘制阴影时的阴影颜色，此属性为只写属性，可通过赋值语句设置其值，但无法通过读取操作获取其当前值，若尝试读取将返回undefined。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

  展开

| 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- |
| string | 否 | 否 | 颜色格式参考 ResourceColor 中string类型说明。 默认值：透明黑色 |

```
// xxx.ets
@Entry
@Component
struct ShadowColor {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          this.context.shadowBlur = 30
          this.context.shadowColor = 'rgb(0,0,255)'
          this.context.fillStyle = 'rgb(255,0,0)'
          this.context.fillRect(30, 30, 100, 100)
      })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170542.91797932612540792246877642084099:50001231000000:2800:1747373C60420D6073456F588ED8112ABA7A86C11E49A1D317CCC2EF335D88BD.png)

### shadowOffsetX

 支持设备PhonePC/2in1TabletTVWearable

设置绘制阴影时和原有对象的水平偏移值，此属性为只写属性，可通过赋值语句设置其值，但无法通过读取操作获取其当前值，若尝试读取将返回undefined。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

  展开

| 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- |
| number | 否 | 否 | 默认值：0.0 默认单位：vp 异常值NaN和Infinity按默认值处理。 |

```
// xxx.ets
@Entry
@Component
struct ShadowOffsetX {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          this.context.shadowBlur = 10
          this.context.shadowOffsetX = 20
          this.context.shadowColor = 'rgb(0,0,0)'
          this.context.fillStyle = 'rgb(255,0,0)'
          this.context.fillRect(20, 20, 100, 80)
      })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170542.26520736351167011787405523771141:50001231000000:2800:5D0C216909D1F699BA218EA5D0B560005C18767D864A7EE0C942B6F9FFEED470.png)

### shadowOffsetY

 支持设备PhonePC/2in1TabletTVWearable

设置绘制阴影时和原有对象的垂直偏移值，此属性为只写属性，可通过赋值语句设置其值，但无法通过读取操作获取其当前值，若尝试读取将返回undefined。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

  展开

| 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- |
| number | 否 | 否 | 默认值：0.0 默认单位：vp 异常值NaN和Infinity按默认值处理。 |

```
// xxx.ets
@Entry
@Component
struct ShadowOffsetY {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)
  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          this.context.shadowBlur = 10
          this.context.shadowOffsetY = 20
          this.context.shadowColor = 'rgb(0,0,0)'
          this.context.fillStyle = 'rgb(255,0,0)'
          this.context.fillRect(30, 30, 100, 100)
      })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170542.18102703290899936546185452016117:50001231000000:2800:B2986638BCF027BDBAFD4595F5687B21FF5E119B20C1C9B7041E5703D37B7AFD.png)

### imageSmoothingEnabled

 支持设备PhonePC/2in1TabletTVWearable

用于设置绘制图片时是否进行图像平滑度调整，true为启用，false为不启用，此属性为只写属性，可通过赋值语句设置其值，但无法通过读取操作获取其当前值，若尝试读取将返回undefined。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

  展开

| 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- |
| boolean | 否 | 否 | 默认值：true |

```
// xxx.ets
@Entry
@Component
struct ImageSmoothingEnabled {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)
  // "common/images/icon.jpg"需要替换为开发者所需的图像资源文件
  private img:ImageBitmap = new ImageBitmap("common/images/icon.jpg")

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          this.context.imageSmoothingEnabled = false
          this.context.drawImage( this.img,0,0,400,200)
      })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170542.71847640082309910679114088177836:50001231000000:2800:2A9C645A0039DCA4DB4B17C943608624123325E7A824CF6633CE93E9B0381A71.png)

### height

 支持设备PhonePC/2in1TabletTVWearable

组件高度。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

  展开

| 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- |
| number | 是 | 否 | 默认单位：vp |

```
// xxx.ets
@Entry
@Component
struct HeightExample {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width(300)
        .height(300)
        .backgroundColor('#ffff00')
        .onReady(() => {
          let h = this.context.height
          this.context.fillRect(0, 0, 300, h/2)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170542.70966867591904223102667245365278:50001231000000:2800:494A13BB119094FA2FC3B3F1E63F59E90C1AA071EE7C394E8F54847A52937E88.png)

### width

 支持设备PhonePC/2in1TabletTVWearable

组件宽度。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

  展开

| 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- |
| number | 是 | 否 | 默认单位：vp |

```
// xxx.ets
@Entry
@Component
struct WidthExample {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width(300)
        .height(300)
        .backgroundColor('#ffff00')
        .onReady(() => {
          let w = this.context.width
          this.context.fillRect(0, 0, w/2, 300)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170542.30688950131468268058319625096731:50001231000000:2800:A788F7D44D72465E153D81ECA5AE54629363CA7B90A7A72D62BE11687D567E8D.png)

### canvas 13+

 支持设备PhonePC/2in1TabletTVWearable

获取和CanvasRenderingContext2D关联的Canvas组件的FrameNode实例。可用于监听关联的Canvas组件的可见状态。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

  展开

| 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- |
| FrameNode | 是 | 否 | 默认值：null |

```
import { FrameNode } from '@kit.ArkUI'
// xxx.ets
@Entry
@Component
struct CanvasExample {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)
  private text: string = ''

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() => {
          let node: FrameNode = this.context.canvas
          node?.commonEvent.setOnVisibleAreaApproximateChange(
            { ratios: [0, 1], expectedUpdateInterval: 10},
            (isVisible: boolean, currentRatio: number) => {
              if (!isVisible && currentRatio <= 0.0) {
                this.text = 'Canvas is completely invisible.'
              }
              if (isVisible && currentRatio >= 1.0) {
                this.text = 'Canvas is fully visible.'
              }
              this.context.reset()
              this.context.font = '30vp sans-serif'
              this.context.fillText(this.text, 50, 50)
            }
          )
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170542.53161306391258221738271888763019:50001231000000:2800:D1AF6462D0C951E1E6A7B85F1380EC90BE9C36111F06503C7B9A22483312E1D6.png)

### imageSmoothingQuality

 支持设备PhonePC/2in1TabletTVWearable

imageSmoothingEnabled为true时，用于设置图像平滑度，此属性为只写属性，可通过赋值语句设置其值，但无法通过读取操作获取其当前值，若尝试读取将返回undefined。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

  展开

| 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- |
| ImageSmoothingQuality | 否 | 否 | 默认值："low" |

```
// xxx.ets
  @Entry
  @Component
  struct ImageSmoothingQualityDemo {
    private settings: RenderingContextSettings = new RenderingContextSettings(true);
    private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
    // "common/images/example.jpg"需要替换为开发者所需的图像资源文件
    private img:ImageBitmap = new ImageBitmap("common/images/example.jpg");

    build() {
      Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
        Canvas(this.context)
          .width('100%')
          .height('100%')
          .backgroundColor('#ffff00')
          .onReady(() =>{
            let ctx = this.context
            ctx.imageSmoothingEnabled = true
            ctx.imageSmoothingQuality = 'high'
            ctx.drawImage(this.img, 0, 0, 400, 200)
          })
      }
      .width('100%')
      .height('100%')
    }
  }
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170542.51686170516878154284955577277431:50001231000000:2800:6E35705D371F9A168AD40BBCF39A7C2D4C5CC3BFF631C4AD6E08C788ED6BBD05.jpeg)

### direction

 支持设备PhonePC/2in1TabletTVWearable

用于设置绘制文字时使用的文字方向，此属性为只写属性，可通过赋值语句设置其值，但无法通过读取操作获取其当前值，若尝试读取将返回undefined。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

  展开

| 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- |
| CanvasDirection | 否 | 否 | 默认值："inherit" |

```
// xxx.ets
  @Entry
  @Component
  struct DirectionDemo {
    private settings: RenderingContextSettings = new RenderingContextSettings(true);
    private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);

    build() {
      Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
        Canvas(this.context)
          .width('100%')
          .height('100%')
          .backgroundColor('#ffff00')
          .onReady(() =>{
            let ctx = this.context
            ctx.font = '48px serif';
            ctx.textAlign = 'start'
            ctx.fillText("Hi ltr!", 200, 50);

            ctx.direction = "rtl";
            ctx.fillText("Hi rtl!", 200, 100);
          })
      }
      .width('100%')
      .height('100%')
    }
  }
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170542.28569856477845830720660838417416:50001231000000:2800:6243E12403ED4DF5CCA4F92AC3F4DDE72D636C99528CA021E2731EAE7C0302AD.jpeg)

### filter

 支持设备PhonePC/2in1TabletTVWearable

用于设置图像的滤镜，可以组合任意数量的滤镜，此属性为只写属性，可通过赋值语句设置其值，但无法通过读取操作获取其当前值，若尝试读取将返回undefined。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

  展开

| 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- |

```
// xxx.ets
  @Entry
  @Component
  struct FilterDemo {
    private settings: RenderingContextSettings = new RenderingContextSettings(true);
    private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
    // "common/images/example.jpg"需要替换为开发者所需的图像资源文件
    private img: ImageBitmap = new ImageBitmap("common/images/example.jpg");

    build() {
      Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
        Canvas(this.context)
          .width('100%')
          .height('100%')
          .onReady(() => {
            let ctx = this.context
            let img = this.img

            ctx.drawImage(img, 0, 0, 100, 100);

            ctx.filter = 'grayscale(50%)';
            ctx.drawImage(img, 100, 0, 100, 100);

            ctx.filter = 'sepia(60%)';
            ctx.drawImage(img, 200, 0, 100, 100);

            ctx.filter = 'saturate(30%)';
            ctx.drawImage(img, 0, 100, 100, 100);

            ctx.filter = 'hue-rotate(90deg)';
            ctx.drawImage(img, 100, 100, 100, 100);

            ctx.filter = 'invert(100%)';
            ctx.drawImage(img, 200, 100, 100, 100);

            ctx.filter = 'opacity(25%)';
            ctx.drawImage(img, 0, 200, 100, 100);

            ctx.filter = 'brightness(0.4)';
            ctx.drawImage(img, 100, 200, 100, 100);

            ctx.filter = 'contrast(200%)';
            ctx.drawImage(img, 200, 200, 100, 100);

            ctx.filter = 'blur(5px)';
            ctx.drawImage(img, 0, 300, 100, 100);

            // Applying multiple filters
            ctx.filter = 'opacity(50%) contrast(200%) grayscale(50%)';
            ctx.drawImage(img, 100, 300, 100, 100);
          })
      }
      .width('100%')
      .height('100%')
    }
  }
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170542.76198592742152638734796779059978:50001231000000:2800:46115439344308A1FDCCBE885B9450923723ED0F461E668504853FF00A5D6761.jpeg)

### letterSpacing 18+

 支持设备PhonePC/2in1TabletTVWearable

用于指定绘制文本时字母之间的间距，此属性为只写属性，可通过赋值语句设置其值，但无法通过读取操作获取其当前值，若尝试读取将返回undefined。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

  展开

| 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- |
| string \| LengthMetrics | 否 | 否 | 当使用LengthMetrics时： 字间距按照指定的单位设置； 不支持FP、PERCENT和LPX（按无效值处理）； 支持负数和小数，设为小数时字间距不四舍五入。 当使用string时： 不支持设置百分比（按无效值处理）； 支持负数和小数，设为小数时字间距不四舍五入； 若letterSpacing的赋值未指定单位（例如：letterSpacing='10'），且未指定LengthMetricsUnit时，默认单位设置为vp； 指定LengthMetricsUnit为px时，默认单位设置为px； 当letterSpacing的赋值指定单位时（例如：letterSpacing='10vp'），字间距按照指定的单位设置。 默认值：0（输入无效值时，字间距设为默认值） 注：推荐使用LengthMetrics，性能更好。 |

```
// xxx.ets
  import { LengthMetrics, LengthUnit } from '@kit.ArkUI'

  @Entry
  @Component
  struct letterSpacingDemo {
    private settings: RenderingContextSettings = new RenderingContextSettings(true)
    private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

    build() {
      Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
        Canvas(this.context)
          .width('100%')
          .height('100%')
          .backgroundColor('rgb(213,213,213)')
          .onReady(() => {
            this.context.font = '30vp'
            this.context.letterSpacing = '10vp'
            this.context.fillText('hello world', 30, 50)
            this.context.letterSpacing = new LengthMetrics(10, LengthUnit.VP)
            this.context.fillText('hello world', 30, 100)
          })
      }
      .width('100%')
      .height('100%')
    }
  }
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170542.69981799293585422158075784341338:50001231000000:2800:C571F04FBD7E7A3F6333B875D166A700CF0177ACAB75344C02229486BA9D2FF4.jpeg)

## 方法

 支持设备PhonePC/2in1TabletTVWearable

以下方法在隐藏页面中调用会产生缓存，应避免在隐藏页面中频繁刷新Canvas。

### fillRect

 支持设备PhonePC/2in1TabletTVWearable

fillRect(x: number, y: number, w: number, h: number): void

填充一个矩形。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 指定矩形左上角点的x坐标。 异常值undefined、null、NaN或Infinity按无效值处理，不进行绘制。 默认单位：vp |
| y | number | 是 | 指定矩形左上角点的y坐标。 异常值undefined、null、NaN或Infinity按无效值处理，不进行绘制。 默认单位：vp |
| w | number | 是 | 指定矩形的宽度。 异常值undefined、null、NaN或Infinity按无效值处理，不进行绘制。 默认单位：vp |
| h | number | 是 | 指定矩形的高度。 异常值undefined、null、NaN或Infinity按无效值处理，不进行绘制。 默认单位：vp |

**示例：**

```
// xxx.ets
@Entry
@Component
struct FillRect {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('rgb(213,213,213)')
        .onReady(() => {
          this.context.fillRect(30, 30, 100, 100)
       })
      }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170543.00146400501664819070724023260837:50001231000000:2800:356C61D3692705BA900E39F72FA86475F50E13DF2BD6095249229EE0E1422DD4.jpg)

### strokeRect

 支持设备PhonePC/2in1TabletTVWearable

strokeRect(x: number, y: number, w: number, h: number): void

绘制具有边框的矩形，矩形内部不填充。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 指定矩形的左上角x坐标。 异常值undefined、null、NaN或Infinity按无效值处理，不进行绘制。 默认单位：vp |
| y | number | 是 | 指定矩形的左上角y坐标。 异常值undefined、null、NaN或Infinity按无效值处理，不进行绘制。 默认单位：vp |
| w | number | 是 | 指定矩形的宽度。 异常值undefined、null、NaN或Infinity按无效值处理，不进行绘制。 默认单位：vp |
| h | number | 是 | 指定矩形的高度。 异常值undefined、null、NaN或Infinity按无效值处理，不进行绘制。 默认单位：vp |

**示例：**

```
// xxx.ets
@Entry
@Component
struct StrokeRect {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          this.context.strokeRect(30, 30, 200, 150)
      })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170543.07851783449613126410010743382307:50001231000000:2800:FEB72FB1565C1EF1DB704E0F7D0A6C6C51B0C93CB2DD06D3AD5B4A23F2B6A735.png)

### clearRect

 支持设备PhonePC/2in1TabletTVWearable

clearRect(x: number, y: number, w: number, h: number): void

删除指定区域内的绘制内容。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 指定矩形上的左上角x坐标。 异常值undefined、null、NaN或Infinity按无效值处理，不进行绘制。 默认单位：vp |
| y | number | 是 | 指定矩形上的左上角y坐标。 异常值undefined、null、NaN或Infinity按无效值处理，不进行绘制。 默认单位：vp |
| w | number | 是 | 指定矩形的宽度。 异常值undefined、null、NaN或Infinity按无效值处理，不进行绘制。 默认单位：vp |
| h | number | 是 | 指定矩形的高度。 异常值undefined、null、NaN或Infinity按无效值处理，不进行绘制。 默认单位：vp |

**示例：**

```
// xxx.ets
@Entry
@Component
struct ClearRect {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          this.context.fillStyle = 'rgb(0,0,255)'
          this.context.fillRect(20,20,200,200)
          this.context.clearRect(30,30,150,100)
      })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170543.42555671313364207201125045332815:50001231000000:2800:5E5609CF1D80D1DE2D04CD25BBB53E6E576890567753E10D6C6D9848AE9D1259.png)

### fillText

 支持设备PhonePC/2in1TabletTVWearable

fillText(text: string, x: number, y: number, maxWidth?: number): void

绘制填充类文本。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | string | 是 | 需要绘制的文本内容。 异常值undefined或null按无效值处理，不进行绘制。 |
| x | number | 是 | 文本绘制起点的x轴坐标。 异常值undefined、null、NaN或Infinity按无效值处理，不进行绘制。 默认单位：vp |
| y | number | 是 | 文本绘制起点的y轴坐标。 异常值undefined、null、NaN或Infinity按无效值处理，不进行绘制。 默认单位：vp |
| maxWidth | number | 否 | 指定文本允许的最大宽度。 异常值null按无效值处理，不进行绘制，undefined、NaN或Infinity按默认值处理。 默认值：不限制宽度。 默认单位：vp |

**示例：**

```
// xxx.ets
@Entry
@Component
struct FillText {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          this.context.font = '30px sans-serif'
          this.context.fillText("Hello World!", 20, 100)
      })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170543.80181099795723615650487772971187:50001231000000:2800:EE667146FF3DBBA351173942DFFCFE36AB71FAC365A78473666683535FC8AA05.png)

### strokeText

 支持设备PhonePC/2in1TabletTVWearable

strokeText(text: string, x: number, y: number, maxWidth?: number): void

绘制描边类文本。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | string | 是 | 需要绘制的文本内容。 异常值undefined或null按无效值处理，不进行绘制。 |
| x | number | 是 | 文本绘制起点的x轴坐标。 异常值undefined、null、NaN或Infinity按无效值处理，不进行绘制。 默认单位：vp |
| y | number | 是 | 文本绘制起点的y轴坐标。 异常值undefined、null、NaN或Infinity按无效值处理，不进行绘制。 默认单位：vp |
| maxWidth | number | 否 | 需要绘制的文本的最大宽度。 异常值null按无效值处理，不进行绘制，undefined、NaN或Infinity按默认值处理。 默认单位：vp 默认值：不限制宽度。 |

**示例：**

```
// xxx.ets
@Entry
@Component
struct StrokeText {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('rgb(213,213,213)')
        .onReady(() => {
          this.context.font = '50vp sans-serif'
          this.context.strokeText("Hello World!", 20, 60)
      })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170543.68190221879038386470673591293770:50001231000000:2800:F3F66A2799383B90E23EFF49405BA674FE74F38C2E557FD44029C88B8AC91332.jpg)

### measureText

 支持设备PhonePC/2in1TabletTVWearable

measureText(text: string): TextMetrics

该方法返回一个文本测算的对象，通过该对象可以获取指定文本的宽度值。不同设备上获取的宽度值可能不同。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | string | 是 | 需要进行测量的文本。 传入异常值undefined或null时按"undefined"或"null"计算。 |

**返回值：**

  展开

| 类型 | 说明 |
| --- | --- |
| TextMetrics | 文本的尺寸信息。 |

**示例：**

```
// xxx.ets
@Entry
@Component
struct MeasureText {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('rgb(213,213,213)')
        .onReady(() => {
          this.context.font = '50px sans-serif'
          this.context.fillText("Hello World!", 20, 100)
          this.context.fillText("width:" + this.context.measureText("Hello World!").width, 20, 200)
      })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170543.33150681722192584553978322670306:50001231000000:2800:37C7BBB5E5CE36E8FCF50B3B8B6690C58880AC5815BA8B7D8AC225803726013D.jpg)

### stroke

 支持设备PhonePC/2in1TabletTVWearable

stroke(): void

根据当前的路径，进行边框绘制操作。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```
// xxx.ets
@Entry
@Component
struct Stroke {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() => {
          this.context.moveTo(125, 25)
          this.context.lineTo(125, 105)
          this.context.lineTo(175, 105)
          this.context.lineTo(175, 25)
          this.context.strokeStyle = 'rgb(255,0,0)'
          this.context.stroke()
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170543.25478469775389650817145188526887:50001231000000:2800:B27C0E99C1B44D266D6A629A2E0F94BC4B77C3E2DCAE248C1E9ECD7271CF3369.png)

### stroke

 支持设备PhonePC/2in1TabletTVWearable

stroke(path: Path2D): void

根据指定的路径，进行边框绘制操作。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | Path2D | 是 | 需要绘制的Path2D。 异常值undefined或null按无效值处理，不进行绘制。 |

**示例：**

```
// xxx.ets
@Entry
@Component
struct Stroke {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)
  private path2Da: Path2D = new Path2D()

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() => {
          this.path2Da.moveTo(25, 25)
          this.path2Da.lineTo(25, 105)
          this.path2Da.lineTo(75, 105)
          this.path2Da.lineTo(75, 25)
          this.context.strokeStyle = 'rgb(0,0,255)'
          this.context.stroke(this.path2Da)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170543.57659443211559932921431827310585:50001231000000:2800:3780935782C1CFBC16964CD7BBAABD6D34A125817D67FACEBC7DBB26D2D07873.png)

### beginPath

 支持设备PhonePC/2in1TabletTVWearable

beginPath(): void

创建一个新的绘制路径。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```
// xxx.ets
@Entry
@Component
struct BeginPath {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('rgb(213,213,213)')
        .onReady(() => {
          this.context.lineWidth = 6
          this.context.strokeStyle = 'rgb(39,135,217)'
          this.context.moveTo(15, 80)
          this.context.lineTo(280, 160)
          this.context.stroke()
          this.context.beginPath()
          this.context.lineTo(300, 240)
          this.context.lineTo(15, 240)
          this.context.stroke()
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170543.17712740789631483931549616138258:50001231000000:2800:352619469A0DEE4A4C68165F7EFE245AC7113D9769A88140C71FA159D3222B5E.png)

### moveTo

 支持设备PhonePC/2in1TabletTVWearable

moveTo(x: number, y: number): void

路径从当前点移动到指定点。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 指定位置的x坐标。 API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。 默认单位：vp |
| y | number | 是 | 指定位置的y坐标。 API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。 默认单位：vp |

  说明 

API version 18之前，若未执行moveTo接口或moveTo接口传入无效参数，路径以(0,0)为起点。

API version 18及以后，若未执行moveTo接口或moveTo接口传入无效参数，路径以初次调用的lineTo、arcTo、bezierCurveTo或quadraticCurveTo接口中的起始点为起点。

**示例：**

```
// xxx.ets
@Entry
@Component
struct MoveTo {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          this.context.beginPath()
          this.context.moveTo(10, 10)
          this.context.lineTo(280, 160)
          this.context.stroke()
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170543.84525098961839490438854057964956:50001231000000:2800:73C5CC443078CFBE914848875CA0A18830BC9B3DDA207451C0DDFADB1E18F1FE.png)

### lineTo

 支持设备PhonePC/2in1TabletTVWearable

lineTo(x: number, y: number): void

从当前点到指定点进行路径连接。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 指定位置的x坐标。 API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。 默认单位：vp |
| y | number | 是 | 指定位置的y坐标。 API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。 默认单位：vp |

**示例：**

```
// xxx.ets
@Entry
@Component
struct LineTo {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          this.context.beginPath()
          this.context.moveTo(10, 10)
          this.context.lineTo(280, 160)
          this.context.stroke()
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170543.52166133538175281529391193473613:50001231000000:2800:35F9E00CD49A3CAC1E5F03E2B724C4C9099C6578F669DA328E4D52A195A907EE.png)

### closePath

 支持设备PhonePC/2in1TabletTVWearable

closePath(): void

结束当前路径，形成一个封闭路径。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```
// xxx.ets
@Entry
@Component
struct ClosePath {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
            this.context.beginPath()
            this.context.moveTo(30, 30)
            this.context.lineTo(110, 30)
            this.context.lineTo(70, 90)
            this.context.closePath()
            this.context.stroke()
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170543.55206405548579694010477010716480:50001231000000:2800:695A0B8197DB3203AD148253A67B0A02B3ABAF5B9CE356E18CF5D0CF4CACA5AA.png)

### createPattern

 支持设备PhonePC/2in1TabletTVWearable

createPattern(image: ImageBitmap, repetition: string | null): CanvasPattern | null

通过指定图像和重复方式创建图片填充的模板。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| image | ImageBitmap | 是 | 图源对象，具体参考ImageBitmap对象。 异常值undefined或null按无效值处理。 |
| repetition | string \| null | 是 | 设置图像重复的方式： 'repeat'：沿x轴和y轴重复绘制图像； 'repeat-x'：沿x轴重复绘制图像； 'repeat-y'：沿y轴重复绘制图像； 'no-repeat'：不重复绘制图像； 'clamp'：在原始边界外绘制时，超出部分使用边缘的颜色绘制； 'mirror'：沿x轴和y轴重复翻转绘制图像。 异常值undefined或null按无效值处理。 |

**返回值：**

  展开

| 类型 | 说明 |
| --- | --- |
| CanvasPattern \| null | 通过指定图像和重复方式创建图片填充的模板对象。 |

**示例：**

```
// xxx.ets
@Entry
@Component
struct CreatePattern {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)
  // "common/images/icon.jpg"需要替换为开发者所需的图像资源文件
  private img:ImageBitmap = new ImageBitmap("common/images/icon.jpg")

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          let pattern = this.context.createPattern(this.img, 'repeat')
          if (pattern) {
            this.context.fillStyle = pattern
          }
          this.context.fillRect(0, 0, 200, 200)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170543.37780681597683995455637516205152:50001231000000:2800:517B3C5968B48428EDF354854FBEEF3016BB723A7B645FCD0FDA1549B34FDA48.png)

### bezierCurveTo

 支持设备PhonePC/2in1TabletTVWearable

bezierCurveTo(cp1x: number, cp1y: number, cp2x: number, cp2y: number, x: number, y: number): void

创建三次贝塞尔曲线的路径。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| cp1x | number | 是 | 第一个贝塞尔参数的x坐标值。 API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。 默认单位：vp |
| cp1y | number | 是 | 第一个贝塞尔参数的y坐标值。 API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。 默认单位：vp |
| cp2x | number | 是 | 第二个贝塞尔参数的x坐标值。 API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。 默认单位：vp |
| cp2y | number | 是 | 第二个贝塞尔参数的y坐标值。 API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。 默认单位：vp |
| x | number | 是 | 路径结束时的x坐标值。 API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。 默认单位：vp |
| y | number | 是 | 路径结束时的y坐标值。 API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。 默认单位：vp |

**示例：**

```
// xxx.ets
import { Point } from '@kit.TestKit';

@Entry
@Component
struct BezierCurveTo {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private start: Point = { x: 50, y: 50 };
  private end: Point = { x: 250, y: 100 };
  private cp1: Point = { x: 200, y: 30 };
  private cp2: Point = { x: 130, y: 80 };

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('rgb(213,213,213)')
        .onReady(() => {
          let ctx = this.context;
          // 三次贝塞尔曲线
          ctx.beginPath();
          ctx.moveTo(this.start.x, this.start.y);
          ctx.bezierCurveTo(this.cp1.x, this.cp1.y, this.cp2.x, this.cp2.y, this.end.x, this.end.y);
          ctx.stroke();

          // 起点和终点
          ctx.fillStyle = 'rgb(39,135,217)';
          ctx.beginPath();
          ctx.arc(this.start.x, this.start.y, 5, 0, 2 * Math.PI); // 起点
          ctx.arc(this.end.x, this.end.y, 5, 0, 2 * Math.PI); // 终点
          ctx.fill();

          // 控制点
          ctx.fillStyle = 'rgb(23,169,141)';
          ctx.beginPath();
          ctx.arc(this.cp1.x, this.cp1.y, 5, 0, 2 * Math.PI); // 控制点一
          ctx.arc(this.cp2.x, this.cp2.y, 5, 0, 2 * Math.PI); // 控制点二
          ctx.fill();
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170543.14462054657909740070938330274250:50001231000000:2800:B6090E675C44039FDD9863EE1E4A566D9C871557D21B6BF04946F8EA1F3C34DD.png)

### quadraticCurveTo

 支持设备PhonePC/2in1TabletTVWearable

quadraticCurveTo(cpx: number, cpy: number, x: number, y: number): void

创建二次贝塞尔曲线的路径。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| cpx | number | 是 | 贝塞尔参数的x坐标值。 API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。 默认单位：vp |
| cpy | number | 是 | 贝塞尔参数的y坐标值。 API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。 默认单位：vp |
| x | number | 是 | 路径结束时的x坐标值。 API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。 默认单位：vp |
| y | number | 是 | 路径结束时的y坐标值。 API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。 默认单位：vp |

**示例：**

```
// xxx.ets
import { Point } from '@kit.TestKit';

@Entry
@Component
struct QuadraticCurveTo {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private start: Point = { x: 50, y: 20 };
  private end: Point = { x: 50, y: 100 };
  private cp: Point = { x: 230, y: 30 };

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('rgb(213,213,213)')
        .onReady(() => {
          let ctx = this.context;
          // 二次贝塞尔曲线
          ctx.beginPath();
          ctx.moveTo(this.start.x, this.start.y);
          ctx.quadraticCurveTo(this.cp.x, this.cp.y, this.end.x, this.end.y);
          ctx.stroke();

          // 起始点和结束点
          ctx.fillStyle = 'rgb(39,135,217)';
          ctx.beginPath();
          ctx.arc(this.start.x, this.start.y, 5, 0, 2 * Math.PI); // 起始点
          ctx.arc(this.end.x, this.end.y, 5, 0, 2 * Math.PI); // 结束点
          ctx.fill();

          // 控制点
          ctx.fillStyle = 'rgb(23,169,141)';
          ctx.beginPath();
          ctx.arc(this.cp.x, this.cp.y, 5, 0, 2 * Math.PI);
          ctx.fill();
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170543.16318717741801981022576777282072:50001231000000:2800:B54193AC5118D6DEEAAA7C52C8F89E0F6EE7448CB45E273ED5F164B6647FE03C.png)

### arc

 支持设备PhonePC/2in1TabletTVWearable

arc(x: number, y: number, radius: number, startAngle: number, endAngle: number, counterclockwise?: boolean): void

绘制弧线路径。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 弧线圆心的x坐标值。 API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。 默认单位：vp |
| y | number | 是 | 弧线圆心的y坐标值。 API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。 默认单位：vp |
| radius | number | 是 | 弧线的圆半径。 API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。 默认单位：vp |
| startAngle | number | 是 | 弧线的起始弧度。 API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。 单位：弧度 |
| endAngle | number | 是 | 弧线的终止弧度。 API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。 单位：弧度 |
| counterclockwise | boolean | 否 | 是否逆时针绘制圆弧。 true：逆时针方向绘制圆弧。 false：顺时针方向绘制圆弧。 默认值：false，设置null或undefined按默认值处理。 |

**示例：**

```
// xxx.ets
@Entry
@Component
struct Arc {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          this.context.beginPath()
          this.context.arc(100, 75, 50, 0, 6.28)
          this.context.stroke()
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170543.40026635429037273438984461821671:50001231000000:2800:B9408B9DFD9F2E4E167EF23C55605970939577424ABBEFB49BD9B572FE0EAF33.jpeg)

### arcTo

 支持设备PhonePC/2in1TabletTVWearable

arcTo(x1: number, y1: number, x2: number, y2: number, radius: number): void

依据给定的控制点和圆弧半径创建圆弧路径。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x1 | number | 是 | 第一个控制点的x坐标值。 API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。 默认单位：vp |
| y1 | number | 是 | 第一个控制点的y坐标值。 API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。 默认单位：vp |
| x2 | number | 是 | 第二个控制点的x坐标值。 API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。 默认单位：vp |
| y2 | number | 是 | 第二个控制点的y坐标值。 API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。 默认单位：vp |
| radius | number | 是 | 圆弧的圆半径值。 API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。 默认单位：vp |

**示例：**

```
// xxx.ets
@Entry
@Component
struct ArcTo {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          // 切线
          this.context.beginPath()
          this.context.strokeStyle = '#808080'
          this.context.lineWidth = 1.5;
          this.context.moveTo(360, 20);
          this.context.lineTo(360, 170);
          this.context.lineTo(110, 170);
          this.context.stroke();

          // 圆弧
          this.context.beginPath()
          this.context.strokeStyle = '#000000'
          this.context.lineWidth = 3;
          this.context.moveTo(360, 20)
          this.context.arcTo(360, 170, 110, 170, 150)
          this.context.stroke()

          // 起始点
          this.context.beginPath();
          this.context.fillStyle = '#00ff00';
          this.context.arc(360, 20, 4, 0, 2 * Math.PI);
          this.context.fill();

          // 控制点
          this.context.beginPath();
          this.context.fillStyle = '#ff0000';
          this.context.arc(360, 170, 4, 0, 2 * Math.PI);
          this.context.arc(110, 170, 4, 0, 2 * Math.PI);
          this.context.fill();
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170543.89940262825467746167599787776737:50001231000000:2800:9F854CBAA6868D24463A378AF3D0E25D4A6AF5FF53FE1A4A58993D45385D9E76.png)

此示例中，arcTo()创建的圆弧为黑色，圆弧的两条切线为灰色。控制点为红色，起始点为绿色。

可以想象两条切线：一条切线从起始点到第一个控制点，另一条切线从第一个控制点到第二个控制点。arcTo()在这两条切线间创建一个圆弧，并使圆弧与这两条切线都相切。

### ellipse

 支持设备PhonePC/2in1TabletTVWearable

ellipse(x: number, y: number, radiusX: number, radiusY: number, rotation: number, startAngle: number, endAngle: number, counterclockwise?: boolean): void

在规定的矩形区域绘制一个椭圆。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 椭圆圆心的x轴坐标。 API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。 默认单位：vp |
| y | number | 是 | 椭圆圆心的y轴坐标。 API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。 默认单位：vp |
| radiusX | number | 是 | 椭圆x轴的半径长度。 API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。 默认单位：vp |
| radiusY | number | 是 | 椭圆y轴的半径长度。 API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。 默认单位：vp |
| rotation | number | 是 | 椭圆的旋转角度。 API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。 单位：弧度 |
| startAngle | number | 是 | 椭圆绘制的起始点角度。 API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。 单位：弧度 |
| endAngle | number | 是 | 椭圆绘制的结束点角度。 API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。 单位：弧度 |
| counterclockwise | boolean | 否 | 是否以逆时针方向绘制椭圆。 true：逆时针方向绘制椭圆。 false：顺时针方向绘制椭圆。 默认值：false，设置null或undefined按默认值处理。 |

**示例：**

```
// xxx.ets
@Entry
@Component
struct CanvasExample {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          this.context.beginPath()
          this.context.ellipse(200, 200, 50, 100, Math.PI * 0.25, Math.PI * 0.5, Math.PI * 2, false)
          this.context.stroke()
          this.context.beginPath()
          this.context.ellipse(200, 300, 50, 100, Math.PI * 0.25, Math.PI * 0.5, Math.PI * 2, true)
          this.context.stroke()
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170544.79626214185685690157033919626132:50001231000000:2800:3FD48B2F19EDCF571B5C9ED124641162FE892EF7E9F3CBDE772E9112C7CE7433.jpeg)

### rect

 支持设备PhonePC/2in1TabletTVWearable

rect(x: number, y: number, w: number, h: number): void

创建矩形路径。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 指定矩形的左上角x坐标值。 API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。 默认单位：vp |
| y | number | 是 | 指定矩形的左上角y坐标值。 API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。 默认单位：vp |
| w | number | 是 | 指定矩形的宽度。 API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。 默认单位：vp |
| h | number | 是 | 指定矩形的高度。 API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。 默认单位：vp |

**示例：**

```
// xxx.ets
@Entry
@Component
struct CanvasExample {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          this.context.rect(20, 20, 100, 100) // Create a 100*100 rectangle at (20, 20)
          this.context.stroke()
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170544.83920395542063514957840158778630:50001231000000:2800:7AAB9CABCBD3E78B914613C1521C355DA2248E06B7B383E872B516FF08E0741C.jpeg)

### roundRect 20+

 支持设备PhonePC/2in1TabletTVWearable

roundRect(x: number, y: number, w: number, h: number, radii?: number | Array<number>): void

创建圆角矩形路径，此方法不会直接渲染内容，如需将圆角矩形绘制到画布上，可以使用fill或stroke方法。

**卡片能力：** 从API version 20开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 指定矩形的左上角x坐标值。 null按0处理，undefined按无效值处理，不进行绘制。 如需绘制完整矩形，取值范围：[0, Canvas宽度)。 默认单位：vp |
| y | number | 是 | 指定矩形的左上角y坐标值。 null按0处理，undefined按无效值处理，不进行绘制。 如需绘制完整矩形，取值范围：[0, Canvas高度)。 默认单位：vp |
| w | number | 是 | 指定矩形的宽度，设置负值为向左绘制。 null按0处理，undefined按无效值处理，不进行绘制。 如需绘制完整矩形，取值范围：[-x, Canvas宽度 - x]。 默认单位：vp |
| h | number | 是 | 指定矩形的高度，设置负值为向上绘制。 null按0处理，undefined按无效值处理，不进行绘制。 如需绘制完整矩形，取值范围：[-y, Canvas高度 - y]。 默认单位：vp |
| radii | number \| Array<number> | 否 | 指定用于矩形角的圆弧半径的数字或列表。 参数类型为number时，所有矩形角的圆弧半径按该数字执行。 参数类型为Array<number>时，数目为1-4个按下面执行： [所有矩形角的圆弧半径] [左上及右下矩形角的圆弧半径, 右上及左下矩形角的圆弧半径] [左上矩形角的圆弧半径, 右上及左下矩形角的圆弧半径, 右下矩形角的圆弧半径] [左上矩形角的圆弧半径, 右上矩形角的圆弧半径, 右下矩形角的圆弧半径, 左下矩形角的圆弧半径] radii存在负数或列表的数目不在[1,4]内时抛出异常，错误码：103701。 默认值：0，null和undefined按默认值处理。 圆弧半径超过矩形宽高时会等比例缩放到宽高的长度。 默认单位：vp |

**错误码：**

以下错误码的详细介绍请参见[Canvas组件错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-canvas)。

  展开

| 错误码ID | 错误信息 | 可能原因 |
| --- | --- | --- |
| 103701 | Parameter error. | 1. The param radii is a list that has zero or more than four elements; 2. The param radii contains negative value. |

**示例：**

该示例展示了绘制六个圆角矩形：

1. 创建一个(10vp, 10vp)为起点，宽高为100vp，四个矩形角圆弧半径为10vp的圆角矩形并填充；
2. 创建一个(120vp, 10vp)为起点，宽高为100vp，四个矩形角圆弧半径为10vp的圆角矩形并填充；
3. 创建一个(10vp, 120vp)为起点，宽高为100vp，左上矩形角圆弧半径及右下矩形角圆弧半径为10vp，右上矩形角圆弧半径及左下矩形角圆弧半径为20vp的圆角矩形并描边；
4. 创建一个(120vp, 120vp)为起点，宽高为100vp，左上矩形角圆弧半径为10vp，右上矩形角圆弧半径及左下矩形角圆弧半径为20vp，右下矩形角圆弧半径为30vp的圆角矩形并描边；
5. 创建一个(10vp, 230vp)为起点，宽高为100vp，左上矩形角圆弧半径为10vp，右上矩形角圆弧半径为20vp，右下矩形角圆弧半径为30vp，左下矩形角圆弧半径为40vp的圆角矩形并描边；
6. 创建一个(220vp, 330vp)为起点，宽高为-100vp，左上矩形角圆弧半径为10vp，右上矩形角圆弧半径为20vp，右下矩形角圆弧半径为30vp，左下矩形角圆弧半径为40vp的圆角矩形并描边。

```
// xxx.ets
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct CanvasExample {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#D5D5D5')
        .onReady(() => {
          try {
            this.context.fillStyle = '#707070'
            this.context.beginPath()
            // 创建一个(10vp, 10vp)为起点，宽高为100vp，四个矩形角圆弧半径为10vp的圆角矩形
            this.context.roundRect(10, 10, 100, 100, 10)
            // 创建一个(120vp, 10vp)为起点，宽高为100vp，四个矩形角圆弧半径为10vp的圆角矩形
            this.context.roundRect(120, 10, 100, 100, [10])
            this.context.fill()
            this.context.beginPath()
            // 创建一个(10vp, 120vp)为起点，宽高为100vp，左上矩形角圆弧半径及右下矩形角圆弧半径为10vp，右上矩形角圆弧半径及左下矩形角圆弧半径为20vp的圆角矩形
            this.context.roundRect(10, 120, 100, 100, [10, 20])
            // 创建一个(120vp, 120vp)为起点，宽高为100vp，左上矩形角圆弧半径为10vp，右上矩形角圆弧半径及左下矩形角圆弧半径为20vp，右下矩形角圆弧半径为30vp的圆角矩形
            this.context.roundRect(120, 120, 100, 100, [10, 20, 30])
            // 创建一个(10vp, 230vp)为起点，宽高为100vp，左上矩形角圆弧半径为10vp，右上矩形角圆弧半径为20vp，右下矩形角圆弧半径为30vp，左下矩形角圆弧半径为40vp的圆角矩形
            this.context.roundRect(10, 230, 100, 100, [10, 20, 30, 40])
            // 创建一个(220vp, 330vp)为起点，宽高为-100vp，左上矩形角圆弧半径为10vp，右上矩形角圆弧半径为20vp，右下矩形角圆弧半径为30vp，左下矩形角圆弧半径为40vp的圆角矩形
            this.context.roundRect(220, 330, -100, -100, [10, 20, 30, 40])
            this.context.stroke()
          } catch (error) {
            let e: BusinessError = error as BusinessError;
            console.error(`Failed to create roundRect. Code: ${e.code}, message: ${e.message}`);
          }
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170544.10087404165520175408279264205608:50001231000000:2800:E720ACCBC030F01EA3491C9E36AB6F676E90B7937D579C16A35722959E5838DB.jpeg)

### fill

 支持设备PhonePC/2in1TabletTVWearable

fill(fillRule?: CanvasFillRule): void

对当前路径进行填充。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数:**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fillRule | CanvasFillRule | 否 | 指定要填充对象的规则。 可选参数为："nonzero"，"evenodd"。 异常值undefined或null按默认值处理。 默认值："nonzero" |

**示例:**

```
// xxx.ets
@Entry
@Component
struct Fill {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          this.context.rect(20, 20, 100, 100) // Create a 100*100 rectangle at (20, 20)
          this.context.fill()
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170544.67408272484081923980415357840239:50001231000000:2800:79D30335FACBEB35C23932ABFB10A6235EF8A97885250F65BC9E10D206D8B5C5.png)

### fill

 支持设备PhonePC/2in1TabletTVWearable

fill(path: Path2D, fillRule?: CanvasFillRule): void

对指定路径进行填充。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数:**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | Path2D | 是 | Path2D填充路径。 异常值undefined或null按无效值处理。 |
| fillRule | CanvasFillRule | 否 | 指定要填充对象的规则。 可选参数为："nonzero"，"evenodd"。 异常值undefined或null按默认值处理。 默认值："nonzero" |

**示例:**

```
// xxx.ets
@Entry
@Component
struct Fill {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          let region = new Path2D()
          region.moveTo(30, 90)
          region.lineTo(110, 20)
          region.lineTo(240, 130)
          region.lineTo(60, 130)
          region.lineTo(190, 20)
          region.lineTo(270, 90)
          region.closePath()
          // Fill path
          this.context.fillStyle = '#00ff00'
          this.context.fill(region, "evenodd")
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170544.11246984007560253943997079656028:50001231000000:2800:25C55AF044540EAFFF61119428D354F5F54FF5BED5BA13F448315954CA2503B0.jpg)

### clip

 支持设备PhonePC/2in1TabletTVWearable

clip(fillRule?: CanvasFillRule): void

设置当前路径为剪切路径。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数:**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fillRule | CanvasFillRule | 否 | 指定要剪切对象的规则。 可选参数为："nonzero"，"evenodd"。 异常值undefined或null按默认值处理。 默认值："nonzero" |

**示例:**

```
// xxx.ets
@Entry
@Component
struct Clip {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          this.context.rect(0, 0, 100, 200)
          this.context.stroke()
          this.context.clip()
          this.context.fillStyle = "rgb(255,0,0)"
          this.context.fillRect(0, 0, 200, 200)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170544.89087839173563043449549842357905:50001231000000:2800:74FEFB497A4E6FF2014FAA1C669B8674C60E804188ADDF0027EB8A13CBD52BC2.png)

### clip

 支持设备PhonePC/2in1TabletTVWearable

clip(path: Path2D, fillRule?: CanvasFillRule): void

设置指定路径为剪切路径。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数:**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | Path2D | 是 | Path2D剪切路径。 异常值undefined或null按无效值处理。 |
| fillRule | CanvasFillRule | 否 | 指定要剪切对象的规则。 可选参数为："nonzero"，"evenodd"。 异常值undefined或null按默认值处理。 默认值："nonzero" |

**示例:**

```
// xxx.ets
@Entry
@Component
struct Clip {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)
  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          let region = new Path2D()
          region.moveTo(30, 90)
          region.lineTo(110, 20)
          region.lineTo(240, 130)
          region.lineTo(60, 130)
          region.lineTo(190, 20)
          region.lineTo(270, 90)
          region.closePath()
          this.context.clip(region,"evenodd")
          this.context.fillStyle = "rgb(0,255,0)"
          this.context.fillRect(0, 0, this.context.width, this.context.height)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170544.69629322654756522304117498217744:50001231000000:2800:C4BF2E61DC617018D56F7D696479730DBBAA1B7EF05778AC7D1F29A584C8A8CB.jpg)

### reset 12+

 支持设备PhonePC/2in1TabletTVWearable

reset(): void

将CanvasRenderingContext2D重置为其默认状态，清除后台缓冲区、绘制状态栈、绘制路径和样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```
// xxx.ets
@Entry
@Component
struct Reset {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          this.context.fillStyle = '#0000ff'
          this.context.fillRect(20, 20, 150, 100)
          this.context.reset()
          this.context.fillRect(20, 150, 150, 100)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170544.01461597545543896346801977843551:50001231000000:2800:68AAE9FA82488688DC0CC1A9C4CAACFB0D82BF13921F7C440ADE11835BD26EBD.png)

### saveLayer 12+

 支持设备PhonePC/2in1TabletTVWearable

saveLayer(): void

创建一个图层。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```
// xxx.ets
@Entry
@Component
struct saveLayer {
private settings: RenderingContextSettings = new RenderingContextSettings(true)
private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

build() {
  Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
    Canvas(this.context)
      .width('100%')
      .height('100%')
      .backgroundColor('#ffff00')
      .onReady(() =>{
        this.context.fillStyle = "#0000ff"
        this.context.fillRect(50,100,300,100)
        this.context.fillStyle = "#00ffff"
        this.context.fillRect(50,150,300,100)
        this.context.globalCompositeOperation = 'destination-over'
        this.context.saveLayer()
        this.context.globalCompositeOperation = 'source-over'
        this.context.fillStyle = "#ff0000"
        this.context.fillRect(100,50,100,300)
        this.context.fillStyle = "#00ff00"
        this.context.fillRect(150,50,100,300)
        this.context.restoreLayer()
      })
  }
  .width('100%')
  .height('100%')
}
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170544.01392721119364725945562013066709:50001231000000:2800:1A48DBF3F90B7F43AE6F20C69199BEBD2090E1328D2F909C794C2B78A967811C.png)

### restoreLayer 12+

 支持设备PhonePC/2in1TabletTVWearable

restoreLayer(): void

恢复图像变换和裁剪状态至saveLayer前的状态，并将图层绘制在canvas上。restoreLayer示例代码同saveLayer。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### resetTransform

 支持设备PhonePC/2in1TabletTVWearable

resetTransform(): void

使用单位矩阵重新设置当前矩阵。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```
// xxx.ets
@Entry
@Component
struct ResetTransform {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          this.context.setTransform(1,0.5, -0.5, 1, 10, 10)
          this.context.fillStyle = 'rgb(0,0,255)'
          this.context.fillRect(0, 0, 100, 100)
          this.context.resetTransform()
          this.context.fillStyle = 'rgb(255,0,0)'
          this.context.fillRect(0, 0, 100, 100)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170544.72603499334994475617895547864175:50001231000000:2800:795CBFD71F6B5274E377948ECDA4AD5AF29C998089C744611427E0D8D8426D3D.png)

### rotate

 支持设备PhonePC/2in1TabletTVWearable

rotate(angle: number): void

针对当前坐标轴进行顺时针旋转。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| angle | number | 是 | 设置顺时针旋转的弧度值，可以通过 degree * Math.PI / 180 将角度转换为弧度值。 API version 18之前，设置NaN或Infinity时，在该方法后执行的绘制方法无法绘制；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的绘制方法正常绘制。 单位：弧度 |

**示例：**

```
// xxx.ets
@Entry
@Component
struct Rotate {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          this.context.rotate(45 * Math.PI / 180)
          this.context.fillRect(70, 20, 50, 50)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170544.37937519211446110872441074968366:50001231000000:2800:10443AB4CAFD7402DEE7793B239F618FF0EB1A0A1BC044DEB68AE6A26870EEA1.png)

### scale

 支持设备PhonePC/2in1TabletTVWearable

scale(x: number, y: number): void

设置canvas画布的缩放变换属性，后续的绘制操作将按照缩放比例进行缩放。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 设置水平方向的缩放值。 API version 18之前，设置NaN或Infinity时，在该方法后执行的绘制方法无法绘制；不支持设置0和负数，设置0、负数、null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、0、负数、null或undefined时当前接口不生效，其他传入有效参数的绘制方法正常绘制。 |
| y | number | 是 | 设置垂直方向的缩放值，不支持设置负数。 API version 18之前，设置NaN或Infinity时，在该方法后执行的绘制方法无法绘制；不支持设置0和负数，设置0、负数、null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、0、负数、null或undefined时当前接口不生效，其他传入有效参数的绘制方法正常绘制。 |

**示例：**

```
// xxx.ets
@Entry
@Component
struct Scale {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          this.context.lineWidth = 3
          this.context.strokeRect(30, 30, 50, 50)
          this.context.scale(2, 2) // Scale to 200%
          this.context.strokeRect(30, 30, 50, 50)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170544.89910791216446524734008253793315:50001231000000:2800:882556D84C18B3E2DB27C9B55486027A4E5789508EDC03840F1C640AF720B808.png)

### transform

 支持设备PhonePC/2in1TabletTVWearable

transform(a: number, b: number, c: number, d: number, e: number, f: number): void

transform方法对应一个变换矩阵，想对一个图形进行变化的时候，只要设置此变换矩阵相应的参数，对图形的各个定点的坐标分别乘以这个矩阵，就能得到新的定点的坐标。矩阵变换效果可叠加。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

 说明 

图形中各个点变换后的坐标可通过下方坐标计算公式计算。

变换后的坐标计算方式（x和y为变换前坐标，x'和y'为变换后坐标）：

- x' = a * x + c * y + e
- y' = b * x + d * y + f

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| a | number | 是 | 变换矩阵中第一行第一列的单元格。scaleX：指定水平缩放值，支持设置负数。 API version 18之前，设置NaN或Infinity时，在该方法后执行的绘制方法无法绘制；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的绘制方法正常绘制。 |
| b | number | 是 | 变换矩阵第二行第一列的单元格。skewY：指定垂直倾斜值，支持设置负数。 API version 18之前，设置NaN或Infinity时，在该方法后执行的绘制方法无法绘制；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的绘制方法正常绘制。 |
| c | number | 是 | 变换矩阵第一行第二列的单元格。skewX：指定水平倾斜值，支持设置负数。 API version 18之前，设置NaN或Infinity时，在该方法后执行的绘制方法无法绘制；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的绘制方法正常绘制。 |
| d | number | 是 | 变换矩阵第二行第二列的单元格。scaleY：指定垂直缩放值，支持设置负数。 API version 18之前，设置NaN或Infinity时，在该方法后执行的绘制方法无法绘制；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的绘制方法正常绘制。 |
| e | number | 是 | 变换矩阵第一行第三列的单元格。translateX：指定水平移动值，支持设置负数。 API version 18之前，设置NaN或Infinity时，在该方法后执行的绘制方法无法绘制；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的绘制方法正常绘制。 默认单位：vp |
| f | number | 是 | 变换矩阵第二行第三列的单元格。translateY：指定垂直移动值，支持设置负数。 API version 18之前，设置NaN或Infinity时，在该方法后执行的绘制方法无法绘制；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的绘制方法正常绘制。 默认单位：vp |

**示例：**

```
// xxx.ets
@Entry
@Component
struct Transform {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('rgb(213,213,213)')
        .onReady(() => {
          this.context.fillStyle = 'rgb(112,112,112)'
          this.context.fillRect(0, 0, 100, 100)
          this.context.transform(1, 0.5, -0.5, 1, 10, 10)
          this.context.fillStyle = 'rgb(0,74,175)'
          this.context.fillRect(0, 0, 100, 100)
          this.context.transform(1, 0.5, -0.5, 1, 10, 10)
          this.context.fillStyle = 'rgb(39,135,217)'
          this.context.fillRect(0, 0, 100, 100)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170544.81462318548258959924400957960331:50001231000000:2800:187CDFF303D7A46EECCF88EF5D9A5273529CE4401E6D5922DBEDF0390E3126C9.jpg)

### setTransform

 支持设备PhonePC/2in1TabletTVWearable

setTransform(a: number, b: number, c: number, d: number, e: number, f: number): void

setTransform方法使用的参数和transform()方法相同，但setTransform()方法会重置现有的变换矩阵并创建新的变换矩阵。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

 说明 

图形中各个点变换后的坐标可通过下方坐标计算公式计算。

变换后的坐标计算方式（x和y为变换前坐标，x'和y'为变换后坐标）：

- x' = a * x + c * y + e
- y' = b * x + d * y + f

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| a | number | 是 | scaleX：指定水平缩放值，支持设置负数。 API version 18之前，设置NaN或Infinity时，在该方法后执行的绘制方法无法绘制；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的绘制方法正常绘制。 |
| b | number | 是 | skewY：指定垂直倾斜值，支持设置负数。 API version 18之前，设置NaN或Infinity时，在该方法后执行的绘制方法无法绘制；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的绘制方法正常绘制。 |
| c | number | 是 | skewX：指定水平倾斜值，支持设置负数。 API version 18之前，设置NaN或Infinity时，在该方法后执行的绘制方法无法绘制；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的绘制方法正常绘制。 |
| d | number | 是 | scaleY：指定垂直缩放值，支持设置负数。 API version 18之前，设置NaN或Infinity时，在该方法后执行的绘制方法无法绘制；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的绘制方法正常绘制。 |
| e | number | 是 | translateX：指定水平移动值，支持设置负数。 API version 18之前，设置NaN或Infinity时，在该方法后执行的绘制方法无法绘制；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的绘制方法正常绘制。 默认单位：vp |
| f | number | 是 | translateY：指定垂直移动值，支持设置负数。 API version 18之前，设置NaN或Infinity时，在该方法后执行的绘制方法无法绘制；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的绘制方法正常绘制。 默认单位：vp |

**示例：**

```
// xxx.ets
@Entry
@Component
struct SetTransform {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('rgb(213,213,213)')
        .onReady(() => {
          this.context.fillStyle = 'rgb(112,112,112)'
          this.context.fillRect(0, 0, 100, 100)
          this.context.transform(1, 0.5, -0.5, 1, 10, 10)
          this.context.fillStyle = 'rgb(23,169,141)'
          this.context.fillRect(0, 0, 100, 100)
          this.context.setTransform(1, 0.5, -0.5, 1, 10, 10)
          this.context.fillStyle = 'rgb(39,135,217)'
          this.context.fillRect(0, 0, 100, 100)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170544.27214926927562238278369637517450:50001231000000:2800:D98BA9AB88BACFC5827DD61FB6F844AE0E04CE60323B3DFA1A1697E47A23F0F9.png)

### setTransform

 支持设备PhonePC/2in1TabletTVWearable

setTransform(transform?: Matrix2D): void

以Matrix2D对象为模板重置现有的变换矩阵并创建新的变换矩阵。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| transform | Matrix2D | 否 | 变换矩阵。 异常值undefined或null按无效值处理。 默认值：null |

**示例：**

```
// xxx.ets
@Entry
@Component
struct TransFormDemo {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context1: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private context2: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Text('context1');
      Canvas(this.context1)
        .width('230vp')
        .height('160vp')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          this.context1.fillRect(100, 20, 50, 50);
          this.context1.setTransform(1, 0.5, -0.5, 1, 10, 10);
          this.context1.fillRect(100, 20, 50, 50);
        })
      Text('context2');
      Canvas(this.context2)
        .width('230vp')
        .height('160vp')
        .backgroundColor('#0ffff0')
        .onReady(() =>{
          this.context2.fillRect(100, 20, 50, 50);
          let storedTransform = this.context1.getTransform();
          this.context2.setTransform(storedTransform);
          this.context2.fillRect(100, 20, 50, 50);
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170545.90621428565923221406234501463440:50001231000000:2800:5CA2F5B7FFE21B758F0F6CC322C5078E55BE6FCA4240C90E83AF2ED896BEEDB3.jpeg)

### getTransform

 支持设备PhonePC/2in1TabletTVWearable

getTransform(): Matrix2D

获取当前被应用到上下文的转换矩阵。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

  展开

| 类型 | 说明 |
| --- | --- |
| Matrix2D | 当前被应用到上下文的转换矩阵。 |

**示例：**

```
// xxx.ets
@Entry
@Component
struct TransFormDemo {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context1: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private context2: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Text('context1');
      Canvas(this.context1)
        .width('230vp')
        .height('120vp')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          this.context1.fillRect(50, 50, 50, 50);
          this.context1.setTransform(1.2, Math.PI/8, Math.PI/6, 0.5, 30, -25);
          this.context1.fillRect(50, 50, 50, 50);
        })
      Text('context2');
      Canvas(this.context2)
        .width('230vp')
        .height('120vp')
        .backgroundColor('#0ffff0')
        .onReady(() =>{
          this.context2.fillRect(50, 50, 50, 50);
          let storedTransform = this.context1.getTransform();
          console.info("Matrix [scaleX = " + storedTransform.scaleX + ", scaleY = " + storedTransform.scaleY +
          ", rotateX = " + storedTransform.rotateX + ", rotateY = " + storedTransform.rotateY +
          ", translateX = " + storedTransform.translateX + ", translateY = " + storedTransform.translateY + "]")
          this.context2.setTransform(storedTransform);
          this.context2.fillRect(50,50,50,50);
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170545.94970372825018168910271060613488:50001231000000:2800:0D44B6B6CC925436046DF9FCED63AF3D106710BF0EC620B311233E829160B666.png)

### translate

 支持设备PhonePC/2in1TabletTVWearable

translate(x: number, y: number): void

移动当前坐标系的原点。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 设置水平平移量。 API version 18之前，设置NaN或Infinity时，在该方法后执行的绘制方法无法绘制；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的绘制方法正常绘制。 默认单位：vp |
| y | number | 是 | 设置竖直平移量。 API version 18之前，设置NaN或Infinity时，在该方法后执行的绘制方法无法绘制；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的绘制方法正常绘制。 默认单位：vp |

**示例：**

```
// xxx.ets
@Entry
@Component
struct Translate {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          this.context.fillRect(10, 10, 50, 50)
          this.context.translate(70, 70)
          this.context.fillRect(10, 10, 50, 50)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170545.50071647330496572720009118827663:50001231000000:2800:3ABE3759A682E8022C6612046A9B09B5F115B262ACE2EF299EA1AD06EB33F0CA.png)

### drawImage

 支持设备PhonePC/2in1TabletTVWearable

drawImage(image: ImageBitmap | PixelMap, dx: number, dy: number): void

进行图像绘制。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用，卡片中不支持PixelMap对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| image | ImageBitmap \| PixelMap | 是 | 图片资源，请参考ImageBitmap或PixelMap。 异常值undefined或null按无效值处理，不进行绘制。 |
| dx | number | 是 | 绘制区域左上角在x轴的位置。 异常值undefined或null按0处理，NaN和Infinity按无效值处理，不进行绘制。 默认单位：vp |
| dy | number | 是 | 绘制区域左上角在y轴的位置。 异常值undefined或null按0处理，NaN和Infinity按无效值处理，不进行绘制。 默认单位：vp |

**示例：**

```
// xxx.ets
@Entry
@Component
struct ImageExample {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  // "common/images/example.jpg"需要替换为开发者所需的图像资源文件
  private img: ImageBitmap = new ImageBitmap("common/images/example.jpg");

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#D5D5D5')
        .onReady(() => {
          this.context.drawImage(this.img, 0, 0)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170545.36483311483844752604963039981766:50001231000000:2800:B8720410A54D3F16BDA2FF197106C5A045892E6D8EA60EB485C8B4D6E339C9A2.png)

### drawImage

 支持设备PhonePC/2in1TabletTVWearable

drawImage(image: ImageBitmap | PixelMap, dx: number, dy: number, dw: number, dh: number): void

将图像拉伸或压缩绘制。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用，卡片中不支持PixelMap对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| image | ImageBitmap \| PixelMap | 是 | 图片资源，请参考ImageBitmap或PixelMap。 异常值undefined或null按无效值处理，不进行绘制。 |
| dx | number | 是 | 绘制区域左上角在x轴的位置。 异常值undefined或null按0处理，NaN和Infinity按无效值处理，不进行绘制。 默认单位：vp |
| dy | number | 是 | 绘制区域左上角在y轴的位置。 异常值undefined或null按0处理，NaN和Infinity按无效值处理，不进行绘制。 默认单位：vp |
| dw | number | 是 | 绘制区域的宽度。当绘制区域的宽度和裁剪图像的宽度不一致时，将图像宽度拉伸或压缩为绘制区域的宽度。 负数、异常值undefined或null按0处理，NaN和Infinity按无效值处理，不进行绘制。 默认单位：vp |
| dh | number | 是 | 绘制区域的高度。当绘制区域的高度和裁剪图像的高度不一致时，将图像高度拉伸或压缩为绘制区域的高度。 负数、异常值undefined或null按0处理，NaN和Infinity按无效值处理，不进行绘制。 默认单位：vp |

**示例：**

```
// xxx.ets
@Entry
@Component
struct ImageExample {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  // "common/images/example.jpg"需要替换为开发者所需的图像资源文件
  private img: ImageBitmap = new ImageBitmap("common/images/example.jpg");

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#D5D5D5')
        .onReady(() => {
          this.context.drawImage(this.img, 0, 0, 300, 300)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170545.25551206082670976277291886806541:50001231000000:2800:C94E35DA28B45E090CFCD9BDE60FE8E3A295941A14CAB598F31E25040B9D2851.png)

### drawImage

 支持设备PhonePC/2in1TabletTVWearable

drawImage(image: ImageBitmap | PixelMap, sx: number, sy: number, sw: number, sh: number, dx: number, dy: number, dw: number, dh: number): void

将图像裁剪后拉伸或压缩绘制。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用，卡片中不支持PixelMap对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| image | ImageBitmap \| PixelMap | 是 | 图片资源，请参考ImageBitmap或PixelMap。 异常值undefined或null按无效值处理，不进行绘制。 |
| sx | number | 是 | 裁切源图像时距离源图像左上角的x坐标值。 异常值undefined或null按0处理，NaN和Infinity按无效值处理，不进行绘制。 image类型为ImageBitmap时，默认单位：vp image类型为PixelMap时，API version 18前，默认单位：px；API version 18及以后，默认单位：vp |
| sy | number | 是 | 裁切源图像时距离源图像左上角的y坐标值。 异常值undefined或null按0处理，NaN和Infinity按无效值处理，不进行绘制。 image类型为ImageBitmap时，默认单位：vp image类型为PixelMap时，API version 18前，默认单位：px；API version 18及以后，默认单位：vp |
| sw | number | 是 | 裁切源图像时需要裁切的宽度。 负数、异常值undefined或null按0处理，NaN和Infinity按无效值处理，不进行绘制。 image类型为ImageBitmap时，默认单位：vp image类型为PixelMap时，API version 18前，默认单位：px；API version 18及以后，默认单位：vp |
| sh | number | 是 | 裁切源图像时需要裁切的高度。 负数、异常值undefined或null按0处理，NaN和Infinity按无效值处理，不进行绘制。 image类型为ImageBitmap时，默认单位：vp image类型为PixelMap时，API version 18前，默认单位：px；API version 18及以后，默认单位：vp |
| dx | number | 是 | 绘制区域左上角在x轴的位置。 异常值undefined或null按0处理，NaN和Infinity按无效值处理，不进行绘制。 默认单位：vp |
| dy | number | 是 | 绘制区域左上角在y轴的位置。 异常值undefined或null按0处理，NaN和Infinity按无效值处理，不进行绘制。 默认单位：vp |
| dw | number | 是 | 绘制区域的宽度。 负数、异常值undefined或null按0处理，NaN和Infinity按无效值处理，不进行绘制。当绘制区域的宽度和裁剪图像的宽度不一致时，将图像宽度拉伸或压缩为绘制区域的宽度。 默认单位：vp |
| dh | number | 是 | 绘制区域的高度。 负数、异常值undefined或null按0处理，NaN和Infinity按无效值处理，不进行绘制。当绘制区域的高度和裁剪图像的高度不一致时，将图像高度拉伸或压缩为绘制区域的高度。 默认单位：vp |

**示例：**

```
// xxx.ets
@Entry
@Component
struct ImageExample {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  // "common/images/example.jpg"需要替换为开发者所需的图像资源文件
  private img: ImageBitmap = new ImageBitmap("common/images/example.jpg");

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#D5D5D5')
        .onReady(() => {
          this.context.drawImage(this.img, 0, 0, 500, 500, 0, 0, 400, 300)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170545.23948805948256210512048216109731:50001231000000:2800:D48B677F54707F17243F7ED1974F88CD9D84247BE772F737FC180F91BC3025CC.png)

### createImageData

 支持设备PhonePC/2in1TabletTVWearable

createImageData(sw: number, sh: number): ImageData

创建新的、空白的、指定大小的ImageData 对象，请参考[ImageData](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-components-canvas-imagedata)，该接口存在内存拷贝行为，高耗时，应避免频繁使用。createImageData示例同[putImageData](/consumer/cn/doc/harmonyos-references/ts-canvasrenderingcontext2d#putimagedata)。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sw | number | 是 | ImageData的宽度。 异常值undefined、null、NaN和Infinity按0处理。 默认单位：vp |
| sh | number | 是 | ImageData的高度。 异常值undefined、null、NaN和Infinity按0处理。 默认单位：vp |

**返回值：**

  展开

| 类型 | 说明 |
| --- | --- |
| ImageData | 新的ImageData对象。 |

### createImageData

 支持设备PhonePC/2in1TabletTVWearable

createImageData(imageData: ImageData): ImageData

根据一个现有的ImageData对象重新创建一个宽、高相同的ImageData对象（不会复制图像数据），请参考[ImageData](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-components-canvas-imagedata)，该接口存在内存拷贝行为，高耗时，应避免频繁使用。createImageData示例同[putImageData](/consumer/cn/doc/harmonyos-references/ts-canvasrenderingcontext2d#putimagedata)。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| imageData | ImageData | 是 | 现有的ImageData对象。 异常值undefined和null按width和height为0的ImageData处理。 |

**返回值：**

  展开

| 类型 | 说明 |
| --- | --- |
| ImageData | 新的ImageData对象。 |

### getPixelMap

 支持设备PhonePC/2in1TabletTVWearable

getPixelMap(sx: number, sy: number, sw: number, sh: number): PixelMap

以当前canvas指定区域内的像素创建[PixelMap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-pixelmap)对象，该接口存在内存拷贝行为，高耗时，应避免频繁使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sx | number | 是 | 需要输出的区域的左上角x坐标。 异常值undefined、null、NaN和Infinity按0处理。 默认单位：vp |
| sy | number | 是 | 需要输出的区域的左上角y坐标。 异常值undefined、null、NaN和Infinity按0处理。 默认单位：vp |
| sw | number | 是 | 需要输出的区域的宽度。 异常值undefined、null、NaN和Infinity按0处理。 默认单位：vp |
| sh | number | 是 | 需要输出的区域的高度。 异常值undefined、null、NaN和Infinity按0处理。 默认单位：vp |

**返回值：**

  展开

| 类型 | 说明 |
| --- | --- |
| PixelMap | 新的PixelMap对象。 |

**示例：**

 说明 

DevEco Studio的预览器不支持显示使用setPixelMap绘制的内容。

```
// xxx.ets
@Entry
@Component
struct GetPixelMap {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)
  // "common/images/example.jpg"需要替换为开发者所需的图像资源文件
  private img: ImageBitmap = new ImageBitmap("common/images/example.jpg")

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() => {
          this.context.drawImage(this.img, 100, 100, 130, 130)
          let pixelmap = this.context.getPixelMap(150, 150, 130, 130)
          this.context.setPixelMap(pixelmap)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170545.28674700557669833217133534272474:50001231000000:2800:E57E75A4949CFFE680E7596817CE3850B165C28FC6DA314B9735C1A4431BB410.png)

### setPixelMap

 支持设备PhonePC/2in1TabletTVWearable

setPixelMap(value?: PixelMap): void

将当前传入[PixelMap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-pixelmap)对象绘制在画布上。setPixelMap示例同getPixelMap。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | PixelMap | 否 | 包含像素值的PixelMap对象。 异常值undefined和null按无效值处理，不进行绘制。 默认值：null |

### getImageData

 支持设备PhonePC/2in1TabletTVWearable

getImageData(sx: number, sy: number, sw: number, sh: number): ImageData

以当前canvas指定区域内的像素创建[ImageData](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-components-canvas-imagedata)对象，该接口存在内存拷贝行为，高耗时，应避免频繁使用。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sx | number | 是 | 需要输出的区域的左上角x坐标。 异常值undefined、null、NaN和Infinity按0处理。 默认单位：vp |
| sy | number | 是 | 需要输出的区域的左上角y坐标。 异常值undefined、null、NaN和Infinity按0处理。 默认单位：vp |
| sw | number | 是 | 需要输出的区域的宽度。 异常值undefined、null、NaN和Infinity按0处理。 默认单位：vp |
| sh | number | 是 | 需要输出的区域的高度。 异常值undefined、null、NaN和Infinity按0处理。 默认单位：vp |

**返回值：**

  展开

| 类型 | 说明 |
| --- | --- |
| ImageData | 新的ImageData对象。 |

**示例：**

```
// xxx.ets
@Entry
@Component
struct GetImageData {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)
  // "/common/images/1234.png"需要替换为开发者所需的图像资源文件
  private img:ImageBitmap = new ImageBitmap("/common/images/1234.png")

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          this.context.drawImage(this.img,0,0,130,130)
          let imageData = this.context.getImageData(50,50,130,130)
          this.context.putImageData(imageData,150,150)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170545.14790752331373007134227749515035:50001231000000:2800:4C59BF2ECC180A18EF3BD3B3E294C81531A069F74DA8981E3BB78BA946CD94DC.png)

### putImageData

 支持设备PhonePC/2in1TabletTVWearable

putImageData(imageData: ImageData, dx: number | string, dy: number | string): void

使用[ImageData](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-components-canvas-imagedata)数据填充新的矩形区域。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| imageData | ImageData | 是 | 包含像素值的ImageData对象。 异常值undefined或null按无效值处理，不进行绘制。 |
| dx | number \| string 10+ | 是 | 填充区域在x轴方向的偏移量。 异常值undefined、null、NaN和Infinity按0处理。 默认单位：vp |
| dy | number \| string 10+ | 是 | 填充区域在y轴方向的偏移量。 异常值undefined、null、NaN和Infinity按0处理。 默认单位：vp |

**示例：**

```
// xxx.ets
@Entry
@Component
struct PutImageData {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('rgb(213,213,213)')
        .onReady(() => {
          let imageDataNum = this.context.createImageData(100, 100)
          let imageData = this.context.createImageData(imageDataNum)
          for (let i = 0; i < imageData.data.length; i += 4) {
            imageData.data[i + 0] = 112
            imageData.data[i + 1] = 112
            imageData.data[i + 2] = 112
            imageData.data[i + 3] = 255
          }
          this.context.putImageData(imageData, 10, 10)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170545.74878157289631110853090611840752:50001231000000:2800:D83998085A174EA83432B1D92121E7FA8148842CCB7ED73DCB72F932EB75AD64.png)

### putImageData

 支持设备PhonePC/2in1TabletTVWearable

putImageData(imageData: ImageData, dx: number | string, dy: number | string, dirtyX: number | string, dirtyY: number | string, dirtyWidth: number | string, dirtyHeight: number | string): void

使用[ImageData](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-components-canvas-imagedata)数据裁剪后填充至新的矩形区域。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| imageData | ImageData | 是 | 包含像素值的ImageData对象。 异常值undefined或null按无效值处理，不进行绘制。 |
| dx | number \| string 10+ | 是 | 填充区域在x轴方向的偏移量。 异常值undefined、null、NaN和Infinity按0处理。 默认单位：vp |
| dy | number \| string 10+ | 是 | 填充区域在y轴方向的偏移量。 异常值undefined、null、NaN和Infinity按0处理。 默认单位：vp |
| dirtyX | number \| string 10+ | 是 | 源图像数据矩形裁切范围左上角距离源图像左上角的x轴偏移量。 异常值undefined、null、NaN和Infinity按0处理。 默认单位：vp |
| dirtyY | number \| string 10+ | 是 | 源图像数据矩形裁切范围左上角距离源图像左上角的y轴偏移量。 异常值undefined、null、NaN和Infinity按0处理。 默认单位：vp |
| dirtyWidth | number \| string 10+ | 是 | 源图像数据矩形裁切范围的宽度。 异常值undefined、null、NaN和Infinity按0处理。 默认单位：vp |
| dirtyHeight | number \| string 10+ | 是 | 源图像数据矩形裁切范围的高度。 异常值undefined、null、NaN和Infinity按0处理。 默认单位：vp |

**示例：**

```
// xxx.ets
@Entry
@Component
struct PutImageData {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('rgb(213,213,213)')
        .onReady(() => {
          let imageDataNum = this.context.createImageData(100, 100)
          let imageData = this.context.createImageData(imageDataNum)
          for (let i = 0; i < imageData.data.length; i += 4) {
            imageData.data[i + 0] = 112
            imageData.data[i + 1] = 112
            imageData.data[i + 2] = 112
            imageData.data[i + 3] = 255
          }
          this.context.putImageData(imageData, 10, 10, 0, 0, 100, 50)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170545.54119118897328483704408648939933:50001231000000:2800:B2085E66BEF6A431961A82E2467E24A5EB51922BA74F39D85C0B95CAEC5597CB.png)

### setLineDash

 支持设备PhonePC/2in1TabletTVWearable

setLineDash(segments: number[]): void

设置画布的虚线样式。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| segments | number[] | 是 | 描述线段如何交替和线段间距长度的数组。 异常值undefined或null按无效值处理。 默认单位：vp |

**示例：**

```
// xxx.ets
@Entry
@Component
struct SetLineDash {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#D5D5D5')
        .onReady(() =>{
          this.context.arc(100, 75, 50, 0, 6.28)
          this.context.setLineDash([10,20])
          this.context.stroke()
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170545.71985814636954900473476400453993:50001231000000:2800:9F73C47F071654EA6C10989E6F8A3999C1F963FA7CEAE5ADA08657D0192AA1A4.png)

### getLineDash

 支持设备PhonePC/2in1TabletTVWearable

getLineDash(): number[]

获得当前画布的虚线样式。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

  展开

| 类型 | 说明 |
| --- | --- |
| number[] | 返回数组，该数组用来描述线段如何交替和间距长度。 默认单位：vp |

**示例：**

```
// xxx.ets
@Entry
@Component
struct CanvasGetLineDash {
  @State message: string = 'Hello World'
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Row() {
      Column() {
        Text(this.message)
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
        Canvas(this.context)
          .width('100%')
          .height('100%')
          .backgroundColor('#D5D5D5')
          .onReady(() => {
            this.context.arc(100, 75, 50, 0, 6.28)
            this.context.setLineDash([10, 20])
            this.context.stroke()
            let res = this.context.getLineDash()
            this.message = JSON.stringify(res)
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170545.71888898159890539907069676172952:50001231000000:2800:A95F25CE4B130B67A3E8A31D194631C93FA7CD7DAE582D7761AFDA1FF925DC18.png)

### transferFromImageBitmap

 支持设备PhonePC/2in1TabletTVWearable

transferFromImageBitmap(bitmap: ImageBitmap): void

显示给定的ImageBitmap对象。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| bitmap | ImageBitmap | 是 | 待显示的ImageBitmap对象。 |

**示例：**

```
// xxx.ets
@Entry
@Component
struct TransferFromImageBitmap {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)
  private offContext: OffscreenCanvasRenderingContext2D = new OffscreenCanvasRenderingContext2D(600, 600, this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('rgb(213,213,213)')
        .onReady(() =>{
          let imageData = this.offContext.createImageData(100, 100)
          for (let i = 0; i < imageData.data.length; i += 4) {
            imageData.data[i + 0] = 255
            imageData.data[i + 1] = 0
            imageData.data[i + 2] = 60
            imageData.data[i + 3] = 80
          }
          this.offContext.putImageData(imageData, 10, 10)
          let image = this.offContext.transferToImageBitmap()
          this.context.transferFromImageBitmap(image)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170545.80197147136126768440458444681602:50001231000000:2800:8713B139CA53C5ADDBD695A45B3AB35BEE2A17D59202275B1D84F6569EDF92F6.jpg)

### toDataURL

 支持设备PhonePC/2in1TabletTVWearable

toDataURL(type?: string, quality?: any): string

生成一个包含图片展示的URL，该接口存在内存拷贝行为，高耗时，应避免频繁使用。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 否 | 用于指定图像格式。 可选参数为："image/png"，"image/jpeg"，"image/webp"。 异常值undefined或null按默认值处理。 默认值：image/png |
| quality | any | 否 | 在指定图片格式为image/jpeg或image/webp的情况下，可以从0到1的区间内选择图片的质量。如果超出取值范围，将会使用默认值0.92。 异常值undefined、null、NaN和Infinity按默认值处理。 默认值：0.92 |

**返回值：**

  展开

| 类型 | 说明 |
| --- | --- |
| string | 图像的URL地址。 |

**示例：**

```
// xxx.ets
@Entry
@Component
struct CanvasExample {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)
  @State toDataURL: string = ""

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width(100)
        .height(100)
        .onReady(() =>{
          this.context.fillStyle = "#00ff00"
          this.context.fillRect(0,0,100,100)
          this.toDataURL = this.context.toDataURL("image/png", 0.92)
        })
      Text(this.toDataURL)
    }
    .width('100%')
    .height('100%')
    .backgroundColor('#ffff00')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170545.63416369378758751138230790589670:50001231000000:2800:132EE8F8E0C39E765A729D9B251C9FA2AD53E8E47D17850309D3155047495A20.png)

### restore

 支持设备PhonePC/2in1TabletTVWearable

restore(): void

恢复保存的绘图上下文。

 说明 

当restore()次数未超出save()次数时，从栈中弹出存储的绘制状态并恢复CanvasRenderingContext2D对象的属性、剪切路径和变换矩阵的值。

当restore()次数超出save()次数时，此方法不做任何改变。

当没有保存状态时，此方法不做任何改变。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```
// xxx.ets
@Entry
@Component
struct CanvasExample {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          this.context.save() // save the default state
          this.context.fillStyle = "#00ff00"
          this.context.fillRect(20, 20, 100, 100)
          this.context.restore() // restore to the default state
          this.context.fillRect(150, 75, 100, 100)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170545.62498098370400294554893769003680:50001231000000:2800:44DEF495E62CE81C77352464523E651246743373EA1A47BE603BB2E7FB4C00FB.png)

### save

 支持设备PhonePC/2in1TabletTVWearable

save(): void

将当前状态放入栈中，保存canvas的全部状态，通常在需要保存绘制状态时调用。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```
// xxx.ets
@Entry
@Component
struct CanvasExample {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          this.context.save() // save the default state
          this.context.fillStyle = "#00ff00"
          this.context.fillRect(20, 20, 100, 100)
          this.context.restore() // restore to the default state
          this.context.fillRect(150, 75, 100, 100)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170546.00699722085392730693644753523022:50001231000000:2800:F26515CE4AAA1AA4F106A57A8346E340EC2F83A70155EA62F444562E425DBFDC.png)

### createLinearGradient

 支持设备PhonePC/2in1TabletTVWearable

createLinearGradient(x0: number, y0: number, x1: number, y1: number): CanvasGradient

创建一个线性渐变色。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x0 | number | 是 | 起点的x轴坐标。 异常值undefined和null会导致此接口返回undefined，NaN和Infinity按无效值处理。 默认单位：vp |
| y0 | number | 是 | 起点的y轴坐标。 异常值undefined和null会导致此接口返回undefined，NaN和Infinity按无效值处理。 默认单位：vp |
| x1 | number | 是 | 终点的x轴坐标。 异常值undefined和null会导致此接口返回undefined，NaN和Infinity按无效值处理。 默认单位：vp |
| y1 | number | 是 | 终点的y轴坐标。 异常值undefined和null会导致此接口返回undefined，NaN和Infinity按无效值处理。 默认单位：vp |

**返回值：**

  展开

| 类型 | 说明 |
| --- | --- |
| CanvasGradient | 新的CanvasGradient对象，用于在canvas上创建渐变效果。 |

**示例：**

```
// xxx.ets
@Entry
@Component
struct CreateLinearGradient {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('rgb(213,213,213)')
        .onReady(() =>{
          let grad = this.context.createLinearGradient(50,0, 300,100)
          grad.addColorStop(0.0, 'rgb(39,135,217)')
          grad.addColorStop(0.5, 'rgb(255,238,240)')
          grad.addColorStop(1.0, 'rgb(23,169,141)')
          this.context.fillStyle = grad
          this.context.fillRect(0, 0, 400, 400)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170546.17213385753270908600070112662697:50001231000000:2800:E5DC13247892CB99BBD5378A2DFC95FBF9C79E7DEF877181E6FA44B3411B80B3.png)

### createRadialGradient

 支持设备PhonePC/2in1TabletTVWearable

createRadialGradient(x0: number, y0: number, r0: number, x1: number, y1: number, r1: number): CanvasGradient

创建一个径向渐变色。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x0 | number | 是 | 起始圆的x轴坐标。 异常值undefined和null会导致此接口返回undefined，NaN和Infinity按无效值处理。 默认单位：vp |
| y0 | number | 是 | 起始圆的y轴坐标。 异常值undefined和null会导致此接口返回undefined，NaN和Infinity按无效值处理。 默认单位：vp |
| r0 | number | 是 | 起始圆的半径。必须是非负且有限的。 异常值undefined和null会导致此接口返回undefined，NaN和Infinity按无效值处理。 默认单位：vp |
| x1 | number | 是 | 终点圆的x轴坐标。 异常值undefined和null会导致此接口返回undefined，NaN和Infinity按无效值处理。 默认单位：vp |
| y1 | number | 是 | 终点圆的y轴坐标。 异常值undefined和null会导致此接口返回undefined，NaN和Infinity按无效值处理。 默认单位：vp |
| r1 | number | 是 | 终点圆的半径。必须为非负且有限的。 异常值undefined和null会导致此接口返回undefined，NaN和Infinity按无效值处理。 默认单位：vp |

**返回值：**

  展开

| 类型 | 说明 |
| --- | --- |
| CanvasGradient | 新的CanvasGradient对象，用于在canvas上创建渐变效果。 |

**示例：**

```
// xxx.ets
@Entry
@Component
struct CreateRadialGradient {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('rgb(213,213,213)')
        .onReady(() => {
          let grad = this.context.createRadialGradient(200, 200, 50, 200, 200, 200)
          grad.addColorStop(0.0, 'rgb(39,135,217)')
          grad.addColorStop(0.5, 'rgb(255,238,240)')
          grad.addColorStop(1.0, 'rgb(112,112,112)')
          this.context.fillStyle = grad
          this.context.fillRect(0, 0, 440, 440)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170546.12932584148888137468973486300256:50001231000000:2800:FDC4F868FF8FDEDC19D913D979525A75529439889B485457FB513B2ABBC7BB87.png)

### createConicGradient 10+

 支持设备PhonePC/2in1TabletTVWearable

createConicGradient(startAngle: number, x: number, y: number): CanvasGradient

创建一个圆锥渐变色。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| startAngle | number | 是 | 开始渐变的角度。角度测量从中心右侧水平开始，顺时针移动。 异常值undefined和null按0处理，NaN和Infinity按无效值处理。 单位：弧度 |
| x | number | 是 | 圆锥渐变的中心x轴坐标。 异常值undefined和null按0处理，NaN和Infinity按无效值处理。 默认单位：vp |
| y | number | 是 | 圆锥渐变的中心y轴坐标。 异常值undefined和null按0处理，NaN和Infinity按无效值处理。 默认单位：vp |

**返回值：**

  展开

| 类型 | 说明 |
| --- | --- |
| CanvasGradient | 新的CanvasGradient对象，用于在canvas上创建渐变效果。 |

**示例：**

```
// xxx.ets
@Entry
@Component
struct CanvasExample {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffffff')
        .onReady(() => {
          let grad = this.context.createConicGradient(0, 50, 80)
          grad.addColorStop(0.0, 'rgb(39,135,217)')
          grad.addColorStop(0.5, 'rgb(213,213,213)')
          grad.addColorStop(1.0, 'rgb(23,160,141)')
          this.context.fillStyle = grad
          this.context.fillRect(0, 30, 100, 100)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170546.35384002022418584820749497488727:50001231000000:2800:0B799D6B9A13276626AF24D177229C6D1BD399994FB05A3145807C3829284612.png)

### on('onAttach') 13+

 支持设备PhonePC/2in1TabletTVWearable

on(type: 'onAttach', callback: () => void): void

订阅CanvasRenderingContext2D与Canvas组件发生绑定的场景。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 订阅CanvasRenderingContext2D与Canvas组件发生绑定的回调。 异常值undefined或null按无效值处理。 |
| callback | () => void | 是 | 订阅CanvasRenderingContext2D与Canvas组件发生绑定后触发的回调。 异常值undefined或null按无效值处理。 |

  说明 

CanvasRenderingContext2D对象在同一时间只能与一个Canvas组件绑定。

当CanvasRenderingContext2D对象和Canvas组件发生绑定时，会触发'onAttach'回调，表示可以获取到[canvas](/consumer/cn/doc/harmonyos-references/ts-canvasrenderingcontext2d#canvas13)。

避免在'onAttach'中执行绘制方法，应保证Canvas组件已经'[onReady](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-components-canvas-canvas#事件)'再进行绘制。

触发'onAttach'回调的一般场景：

1、Canvas组件创建时绑定CanvasRenderingContext2D对象;

2、CanvasRenderingContext2D对象新绑定一个Canvas组件时。

### on('onDetach') 13+

 支持设备PhonePC/2in1TabletTVWearable

on(type: 'onDetach', callback: () => void): void

订阅CanvasRenderingContext2D与Canvas组件解除绑定的场景。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 订阅CanvasRenderingContext2D与Canvas组件解除绑定的回调。 异常值undefined或null按无效值处理。 |
| callback | () => void | 是 | 订阅CanvasRenderingContext2D与Canvas组件解除绑定后触发的回调。 异常值undefined或null按无效值处理。 |

  说明 

当CanvasRenderingContext2D对象和Canvas组件解除绑定时，会触发'onDetach'回调，表示应停止绘制行为。

触发'onDetach'回调的一般场景：

1、Canvas组件销毁时解除绑定CanvasRenderingContext2D对象;

2、CanvasRenderingContext2D对象新绑定一个Canvas组件，会先解除已有的绑定。

### off('onAttach') 13+

 支持设备PhonePC/2in1TabletTVWearable

off(type: 'onAttach', callback?: () => void): void

取消订阅CanvasRenderingContext2D与Canvas组件发生绑定的场景。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消订阅CanvasRenderingContext2D与Canvas组件发生绑定的回调。 异常值undefined或null按无效值处理。 |
| callback | () => void | 否 | 为空表示取消所有订阅CanvasRenderingContext2D与Canvas组件发生绑定后触发的回调。 非空则取消订阅发生绑定对应的回调。 异常值undefined或null按无效值处理。 |

### off('onDetach') 13+

 支持设备PhonePC/2in1TabletTVWearable

off(type: 'onDetach', callback?: () => void): void

取消订阅CanvasRenderingContext2D与Canvas组件解除绑定的场景。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消订阅CanvasRenderingContext2D与Canvas组件解除绑定的回调。 异常值undefined或null按无效值处理。 |
| callback | () => void | 否 | 为空代表取消所有订阅CanvasRenderingContext2D与Canvas组件解除绑定后触发的回调。 非空代表取消订阅解除绑定对应的回调。 异常值undefined或null按无效值处理。 |

**示例：**

```
import { BusinessError } from '@kit.BasicServicesKit';
import { FrameNode } from '@kit.ArkUI'

// xxx.ets
@Entry
@Component
struct AttachDetachExample {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)
  private scroller: Scroller = new Scroller()
  private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
  private node: FrameNode | null = null
  attachCallback = () => {
    console.info('CanvasRenderingContext2D attached to the canvas frame node.')
    this.node = this.context.canvas
  }
  detachCallback = () => {
    console.info('CanvasRenderingContext2D detach from the canvas frame node.')
    this.node = null
  }

  aboutToAppear(): void {
    try {
      this.context.on('onAttach', this.attachCallback)
      this.context.on('onDetach', this.detachCallback)
    } catch (error) {
      let e: BusinessError = error as BusinessError;
      console.error(`Error code: ${e.code}, message: ${e.message}`);
    }
  }

  aboutToDisappear(): void {
    try {
      this.context.off('onAttach')
      this.context.off('onDetach')
    } catch (error) {
      let e: BusinessError = error as BusinessError;
      console.error(`Error code: ${e.code}, message: ${e.message}`);
    }
  }

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Scroll(this.scroller) {
        Flex({ direction: FlexDirection.Column }) {
          ForEach(this.arr, (item: number) => {
            Row() {
              if (item == 3) {
                Canvas(this.context)
                  .width('100%')
                  .height(150)
                  .backgroundColor('rgb(213,213,213)')
                  .onReady(() => {
                    this.context.font = '30vp sans-serif'
                    this.node?.commonEvent.setOnVisibleAreaApproximateChange(
                      { ratios: [0, 1], expectedUpdateInterval: 10 },
                      (isVisible: boolean, currentRatio: number) => {
                        if (!isVisible && currentRatio <= 0.0) {
                          console.info('Canvas is completely invisible.')
                        }
                        if (isVisible && currentRatio >= 1.0) {
                          console.info('Canvas is fully visible.')
                        }
                      }
                    )
                  })
              } else {
                Text(item.toString())
                  .width('100%')
                  .height(150)
                  .backgroundColor('rgb(39,135,217)')
                  .borderRadius(15)
                  .fontSize(16)
                  .textAlign(TextAlign.Center)
                  .margin({ top: 5 })
              }
            }
          }, (item: number) => item.toString())
        }
      }
      .width('90%')
      .scrollBar(BarState.Off)
      .scrollable(ScrollDirection.Vertical)
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170546.48432444139509797803604465943778:50001231000000:2800:961BF57CC6BEB0E9996D3715CB3ED7F6C2A03DF5FBEE7BDDA0405919EF65864F.gif)

### startImageAnalyzer 12+

 支持设备PhonePC/2in1TabletTVWearable

startImageAnalyzer(config: ImageAnalyzerConfig): Promise<void>

配置并启动AI分析功能，使用Promise异步回调。使用前需先设置[enableAnalyzer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-components-canvas-canvas#enableanalyzer12)为true，启用图像AI分析能力。

该方法调用时，将截取调用时刻的画面帧进行分析，使用时需注意启动分析的时机，避免出现画面和分析内容不一致的情况。

未执行完重复调用该方法会触发错误回调。示例代码同stopImageAnalyzer。

 说明 

分析类型不支持动态修改。

当检测到画面有变化时，分析结果将自动销毁，可重新调用本接口启动分析。

该特性依赖设备能力，不支持该能力的情况下，将返回错误码。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| config | ImageAnalyzerConfig | 是 | 执行AI分析所需要的入参，用于配置AI分析功能。 异常值undefined或null按无效值处理。 |

**返回值：**

  展开

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[AI分析类库错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-image-analyzer)。

  展开

| 错误码ID | 错误信息 |
| --- | --- |
| 110001 | Image analysis feature is unsupported. |
| 110002 | Image analysis is currently being executed. |
| 110003 | Image analysis is stopped. |

### stopImageAnalyzer 12+

 支持设备PhonePC/2in1TabletTVWearable

stopImageAnalyzer(): void

停止AI分析功能，AI分析展示的内容将被销毁。

 说明 

在startImageAnalyzer方法未返回结果时调用本方法，会触发其错误回调。

该特性依赖设备能力。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```
// xxx.ets
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct ImageAnalyzerExample {
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)
  private config: ImageAnalyzerConfig = {
    types: [ImageAnalyzerType.SUBJECT, ImageAnalyzerType.TEXT]
  }
  // 'common/images/example.png'需要替换为开发者所需的图像资源文件
  private img = new ImageBitmap('common/images/example.png')
  private aiController: ImageAnalyzerController = new ImageAnalyzerController()
  private options: ImageAIOptions = {
    types: [ImageAnalyzerType.SUBJECT, ImageAnalyzerType.TEXT],
    aiController: this.aiController
  }

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Button('start')
        .width(100)
        .height(50)
        .margin(5)
        .onClick(() => {
          this.context.startImageAnalyzer(this.config)
            .then(() => {
              console.info("analysis complete")
            })
            .catch((error: BusinessError) => {
              console.info("error code: " + error.code)
            })
        })
      Button('stop')
        .width(100)
        .height(50)
        .margin(5)
        .onClick(() => {
          this.context.stopImageAnalyzer()
        })
      Button('getTypes')
        .width(100)
        .height(50)
        .margin(5)
        .onClick(() => {
          this.aiController.getImageAnalyzerSupportTypes()
        })
      Canvas(this.context, this.options)
        .width(200)
        .height(200)
        .enableAnalyzer(true)
        .onReady(() => {
          this.context.drawImage(this.img, 0, 0, 200, 200)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170546.39147346911824207972169367200995:50001231000000:2800:1C392C3E8C2F1F96775E97DF95635EF8B6C491BC8E5A6F461F5578B1D2966E48.png)

## CanvasDirection类型说明

 支持设备PhonePC/2in1TabletTVWearable

type CanvasDirection = "inherit" | "ltr" | "rtl"

定义当前文本方向的类型。取值类型为下表类型中的并集。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

  展开

| 类型 | 说明 |
| --- | --- |
| inherit | 继承canvas组件通用属性已设定的文本方向，若canvas组件未设置direction属性，则跟随系统文字方向。 |
| ltr | 从左往右。 |
| rtl | 从右往左。 |

## CanvasFillRule类型说明

 支持设备PhonePC/2in1TabletTVWearable

type CanvasFillRule = "evenodd" | "nonzero"

定义用于确定点是在路径内还是路径外的填充样式算法的类型。取值类型为下表类型中的并集。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

  展开

| 类型 | 说明 |
| --- | --- |
| evenodd | 奇偶规则。 此规则通过从画布上的某点向任意方向发射一条射线，并统计图形路径与射线的交点数量来判断该点是否在图形内部。如果交点数量是奇数，则该点在图形内部，否则在图形外部。 |
| nonzero | 非零规则。 此规则通过从画布上的某点向任意方向发射一条射线，并检查图形路径与射线的交点来判断该点是否在图形内部。初始计数为0，为路径的每一段线段指定一个方向值，每当路径从左向右穿过射线时加1，从右向左穿过时减1。如果最终的结果是0，则该点在图形外部，否则在图形内部。 |

**示例**

```
// xxx.ets
@Entry
@Component
struct Index {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('rgb(213, 213, 213)')
        .onReady(() => {
          let offContext = this.offCanvas.getContext("2d", this.settings)
          offContext.font = '60px sans-serif'
          offContext.fillStyle = 'rgb(39, 135, 217)';
          // 非零环绕规则 (nonzero)
          offContext.beginPath();
          offContext.arc(100, 100, 60, 0, Math.PI * 2);
          offContext.arc(100, 100, 20, 0, Math.PI * 2);
          offContext.fill('nonzero'); // 使用非零环绕规则
          offContext.fillText('nonzero', 65, 200)
          // 奇偶环绕规则 (evenodd)
          offContext.beginPath();
          offContext.arc(250, 100, 60, 0, Math.PI * 2);
          offContext.arc(250, 100, 20, 0, Math.PI * 2);
          offContext.fill('evenodd'); // 使用奇偶环绕规则
          offContext.fillText('evenodd', 215, 200)
          let image = this.offCanvas.transferToImageBitmap()
          this.context.transferFromImageBitmap(image)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170546.25573677514463655244327380024934:50001231000000:2800:9617B106187FBF2D17FCDC9453609C7C8A1C218CFD209AA9833C0522A347D627.png)

## CanvasLineCap类型说明

 支持设备PhonePC/2in1TabletTVWearable

type CanvasLineCap = "butt" | "round" | "square"

定义绘制每条线段端点的类型。取值类型为下表类型中的并集。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

  展开

| 类型 | 说明 |
| --- | --- |
| butt | 线条两端为平行线，不额外扩展。 |
| round | 在线条两端延伸半个圆，直径等于线宽。 |
| square | 在线条两端延伸一个矩形，宽度等于线宽的一半，高度等于线宽。 |

## CanvasLineJoin类型说明

 支持设备PhonePC/2in1TabletTVWearable

type CanvasLineJoin = "bevel" | "miter" | "round"

定义长度不为0的两个连接部分（线段、圆弧和曲线）的类型。取值类型为下表类型中的并集。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

  展开

| 类型 | 说明 |
| --- | --- |
| bevel | 在线段相连处使用三角形为底填充， 每个部分矩形拐角独立。 |
| miter | 在相连部分的外边缘处进行延伸，使其相交于一点，形成一个菱形区域，该属性可以通过设置miterLimit属性展现效果。 |
| round | 在线段相连处绘制一个扇形，扇形的圆角半径是线段的宽度。 |

## CanvasTextAlign类型说明

 支持设备PhonePC/2in1TabletTVWearable

type CanvasTextAlign = "center" | "end" | "left" | "right" | "start"

定义文本对齐方式的类型。取值类型为下表类型中的并集。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

  展开

| 类型 | 说明 |
| --- | --- |
| center | 文本居中对齐。 |
| start | 文本对齐界线开始的地方。 |
| end | 文本对齐界线结束的地方。 |
| left | 文本左对齐。 |
| right | 文本右对齐。 |

## CanvasTextBaseline类型说明

 支持设备PhonePC/2in1TabletTVWearable

type CanvasTextBaseline = "alphabetic" | "bottom" | "hanging" | "ideographic" | "middle" | "top"

定义文本基线类型。取值类型为下表类型中的并集。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

  展开

| 类型 | 说明 |
| --- | --- |
| alphabetic | 文本基线是标准的字母基线。 |
| bottom | 文本基线在文本块的底部。 与ideographic基线的区别在于ideographic基线不需要考虑下行字母。 |
| hanging | 文本基线是悬挂基线。 |
| ideographic | 文字基线是表意字基线；如果字符本身超出了alphabetic基线，那么ideographic基线位置在字符本身的底部。 |
| middle | 文本基线在文本块的中间。 |
| top | 文本基线在文本块的顶部。 |

## ImageSmoothingQuality类型说明

 支持设备PhonePC/2in1TabletTVWearable

type ImageSmoothingQuality = "high" | "low" | "medium"

定义图片平滑度类型。取值类型为下表类型中的并集。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

  展开

| 类型 | 说明 |
| --- | --- |
| low | 低画质 |
| medium | 中画质 |
| high | 高画质 |

## TextMetrics

 支持设备PhonePC/2in1TabletTVWearable

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

  展开

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| width | number | 是 | 否 | 只读属性，文本方块的宽度。 |
| height | number | 是 | 否 | 只读属性，文本方块的高度。 |
| actualBoundingBoxAscent | number | 是 | 否 | 只读属性，从 CanvasRenderingContext2D.textBaseline 属性标明的水平线到渲染文本的矩形边界顶部的距离。 |
| actualBoundingBoxDescent | number | 是 | 否 | 只读属性，从 CanvasRenderingContext2D.textBaseline 属性标明的水平线到渲染文本的矩形边界底部的距离。 |
| actualBoundingBoxLeft | number | 是 | 否 | 只读属性，平行于基线，从 CanvasRenderingContext2D.textAlign 属性确定的对齐点到文本矩形边界左侧的距离。 |
| actualBoundingBoxRight | number | 是 | 否 | 只读属性，平行于基线，从 CanvasRenderingContext2D.textAlign 属性确定的对齐点到文本矩形边界右侧的距离。 |
| alphabeticBaseline | number | 是 | 否 | 只读属性，从 CanvasRenderingContext2D.textBaseline 属性标明的水平线到线框的 alphabetic 基线的距离。 |
| emHeightAscent | number | 是 | 否 | 只读属性，从 CanvasRenderingContext2D.textBaseline 属性标明的水平线到线框中 em 方块顶部的距离。 |
| emHeightDescent | number | 是 | 否 | 只读属性，从 CanvasRenderingContext2D.textBaseline 属性标明的水平线到线框中 em 方块底部的距离。 |
| fontBoundingBoxAscent | number | 是 | 否 | 只读属性，从 CanvasRenderingContext2D.textBaseline 属性标明的水平线到渲染文本的所有字体的矩形最高边界顶部的距离。 |
| fontBoundingBoxDescent | number | 是 | 否 | 只读属性，从 CanvasRenderingContext2D.textBaseline 属性标明的水平线到渲染文本的所有字体的矩形边界最底部的距离。 |
| hangingBaseline | number | 是 | 否 | 只读属性，从 CanvasRenderingContext2D.textBaseline 属性标明的水平线到线框的 hanging 基线的距离。 |
| ideographicBaseline | number | 是 | 否 | 只读属性，从 CanvasRenderingContext2D.textBaseline 属性标明的水平线到线框的 ideographic 基线的距离。 |

## RenderingContextSettings

 支持设备PhonePC/2in1TabletTVWearable

用来配置CanvasRenderingContext2D对象的参数，包括是否开启抗锯齿。

 说明 

RenderingContextSettings的抗锯齿效果对文本绘制无影响。

### constructor

 支持设备PhonePC/2in1TabletTVWearable

constructor(antialias?: boolean)

构造CanvasRenderingContext2D对象，支持配置开启抗锯齿。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| antialias | boolean | 否 | 表明canvas是否开启抗锯齿。 异常值undefined按默认值处理。 false：表示不开启抗锯齿功能，true：表示开启抗锯齿。 默认值：false |

### 属性

 支持设备PhonePC/2in1TabletTVWearable

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

  展开

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| antialias | boolean | 否 | 是 | 表明canvas是否开启抗锯齿。 异常值undefined按默认值处理。 false：表示不开启抗锯齿功能，true：表示开启抗锯齿。 默认值：false |