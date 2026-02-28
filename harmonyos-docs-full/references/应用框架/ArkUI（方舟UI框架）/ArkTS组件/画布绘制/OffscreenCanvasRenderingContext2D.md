# OffscreenCanvasRenderingContext2D

使用OffscreenCanvasRenderingContext2D在Canvas上进行离屏绘制，绘制对象可以是形状、文本、图片等。离屏绘制是指将需要绘制的内容先绘制在缓存区，然后将其转换成图片，一次性绘制到Canvas上。离屏绘制使用CPU进行绘制，绘制速度较慢，对绘制速度有要求的场景应避免使用离屏绘制。

 说明 

从 API version 8 开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

OffscreenCanvasRenderingContext2D无法在ServiceExtensionAbility中使用，ServiceExtensionAbility中建议使用[Drawing模块](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-graphics-drawing)进行离屏绘制。

## 构造函数

 支持设备PhonePC/2in1TabletTVWearable  

### constructor

 支持设备PhonePC/2in1TabletTVWearable

constructor(width: number, height: number, settings?: RenderingContextSettings)

构造离屏Canvas画布对象，支持配置画布宽高和OffscreenCanvasRenderingContext2D对象的参数。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| width | number | 是 | 离屏画布的宽度，默认单位：vp 异常值NaN和Infinity按无效值处理。 |
| height | number | 是 | 离屏画布的高度，默认单位：vp 异常值NaN和Infinity按无效值处理。 |
| settings | RenderingContextSettings | 否 | 用来配置OffscreenCanvasRenderingContext2D对象的参数，见RenderingContextSettings接口描述。 异常值undefined按 RenderingContextSettings 的默认值处理。 默认值：null |

### constructor 12+

 支持设备PhonePC/2in1TabletTVWearable

constructor(width: number, height: number, settings?: RenderingContextSettings, unit?: LengthMetricsUnit)

构造离屏Canvas画布对象，支持配置画布宽高、OffscreenCanvasRenderingContext2D对象的参数和单位模式。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| width | number | 是 | 离屏画布的宽度，默认单位：vp 异常值NaN和Infinity按无效值处理。 |
| height | number | 是 | 离屏画布的高度，默认单位：vp 异常值NaN和Infinity按无效值处理。 |
| settings | RenderingContextSettings | 否 | 用来配置OffscreenCanvasRenderingContext2D对象的参数，见RenderingContextSettings接口描述。 异常值undefined按 RenderingContextSettings 的默认值处理。 默认值：null |
| unit | LengthMetricsUnit | 否 | 用来配置OffscreenCanvasRenderingContext2D对象的单位模式，配置后无法动态更改，配置方法同 CanvasRenderingContext2D 。 异常值undefined、NaN和Infinity按默认值处理。 默认值：DEFAULT |

## 属性

 支持设备PhonePC/2in1TabletTVWearable说明 

fillStyle、shadowColor与 strokeStyle 中string类型格式为 'rgb(255, 255, 255)'，'rgba(255, 255, 255, 1.0)'，'#FFFFFF'。

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
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          let offContext = this.offCanvas.getContext("2d", this.settings)
          // 使用string设置fillStyle属性
          offContext.fillStyle = '#0000ff'
          offContext.fillRect(20, 20, 150, 100)
          let image = this.offCanvas.transferToImageBitmap()
          this.context.transferFromImageBitmap(image)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

```
// xxx.ets
@Entry
@Component
struct FillStyleExample {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          let offContext = this.offCanvas.getContext("2d", this.settings)
          // 使用number设置fillStyle属性
          offContext.fillStyle = 0x0000FF
          offContext.fillRect(20, 20, 150, 100)
          let image = this.offCanvas.transferToImageBitmap()
          this.context.transferFromImageBitmap(image)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170655.95680010157137657972299274328819:50001231000000:2800:88074C2B47F5AAC0CCA8314FCFE7088B61D575D2CA9357D64405C2D48E550FDE.png)

### lineWidth

 支持设备PhonePC/2in1TabletTVWearable

设置绘制线条的宽度，此属性为只写属性，可通过赋值语句设置其值，但无法通过读取操作获取其当前值，若尝试读取将返回undefined。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

  展开

| 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- |
| number | 否 | 否 | 默认值：1（px） 默认单位：vp lineWidth取值不支持0和负数，0、负数和NaN按默认值处理，Infinity会导致和lineWidth属性相关的接口无法绘制。 |

```
// xxx.ets
@Entry
@Component
struct LineWidthExample {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          let offContext = this.offCanvas.getContext("2d", this.settings)
          // 设置lineWidth属性
          offContext.lineWidth = 5
          offContext.strokeRect(25, 25, 85, 105)
          let image = this.offCanvas.transferToImageBitmap()
          this.context.transferFromImageBitmap(image)
      })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170655.46711923851215090033360098064149:50001231000000:2800:80B4308B163EF34DCD649710455BADCBBDCCB054F5D8109719029D90850CF202.png)

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
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          let offContext = this.offCanvas.getContext("2d", this.settings)
          offContext.lineWidth = 10
          // 使用string设置strokeStyle属性
          offContext.strokeStyle = '#0000ff'
          offContext.strokeRect(25, 25, 155, 105)
          let image = this.offCanvas.transferToImageBitmap()
          this.context.transferFromImageBitmap(image)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

```
// xxx.ets
@Entry
@Component
struct StrokeStyleExample {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          let offContext = this.offCanvas.getContext("2d", this.settings)
          offContext.lineWidth = 10
          // 使用number设置strokeStyle属性
          offContext.strokeStyle = 0x0000ff
          offContext.strokeRect(25, 25, 155, 105)
          let image = this.offCanvas.transferToImageBitmap()
          this.context.transferFromImageBitmap(image)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170655.05207776907572722589865382852003:50001231000000:2800:860BDAC96764BACF30BCD9A1CAB626F45873276ECABD952931A8A2C183AA345A.png)

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
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          let offContext = this.offCanvas.getContext("2d", this.settings)
          offContext.lineWidth = 8
          offContext.beginPath()
          // 设置lineCap属性
          offContext.lineCap = 'round'
          offContext.moveTo(30, 50)
          offContext.lineTo(220, 50)
          offContext.stroke()
          let image = this.offCanvas.transferToImageBitmap()
          this.context.transferFromImageBitmap(image)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170655.71174530844165827182783993378185:50001231000000:2800:701F6697C510066F2DD68D3720458A311E30804ADFC9C8D54E98E615E8DE5BC5.png)

### lineJoin

 支持设备PhonePC/2in1TabletTVWearable

指定线段间相交的交点样式，此属性为只写属性，可通过赋值语句设置其值，但无法通过读取操作获取其当前值，若尝试读取将返回undefined。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

  展开

| 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- |
| CanvasLineJoin | 否 | 否 | 默认值：'miter' |

```
// xxx.ets
@Entry
@Component
struct LineJoinExample {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          let offContext = this.offCanvas.getContext("2d", this.settings)
          offContext.beginPath()
          offContext.lineWidth = 8
          // 设置lineJoin属性
          offContext.lineJoin = 'miter'
          offContext.moveTo(30, 30)
          offContext.lineTo(120, 60)
          offContext.lineTo(30, 110)
          offContext.stroke()
          let image = this.offCanvas.transferToImageBitmap()
          this.context.transferFromImageBitmap(image)
      })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170655.54284983131744565205486771130648:50001231000000:2800:E57AD30681169BA85704CAE41EDB8D1A888928811F2C819E8589D543F4190BCB.png)

### miterLimit

 支持设备PhonePC/2in1TabletTVWearable

设置斜接面限制值，该值指定了线条相交处内角和外角的距离，仅当设置了lineJoin为miter才生效，此属性为只写属性，可通过赋值语句设置其值，但无法通过读取操作获取其当前值，若尝试读取将返回undefined。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

  展开

| 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- |
| number | 否 | 否 | 默认值：10px 单位：px。 miterLimit取值不支持0和负数，0、负数和NaN按默认值处理，Infinity会导致和miterLimit属性相关的接口无法绘制。 |

```
// xxx.ets
@Entry
@Component
struct MiterLimit {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          let offContext = this.offCanvas.getContext("2d", this.settings)
          offContext.lineWidth = 8
          offContext.lineJoin = 'miter'
          // 设置miterLimit属性
          offContext.miterLimit = 3
          offContext.moveTo(30, 30)
          offContext.lineTo(60, 35)
          offContext.lineTo(30, 37)
          offContext.stroke()
          let image = this.offCanvas.transferToImageBitmap()
          this.context.transferFromImageBitmap(image)
      })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170655.35741656725004944431074814874421:50001231000000:2800:DFBF73CA314F4521AE7A8FD09143F6627343D3229925532CB753835B9B8E15CC.png)

### font

 支持设备PhonePC/2in1TabletTVWearable

设置文本绘制中的字体样式，此属性为只写属性，可通过赋值语句设置其值，但无法通过读取操作获取其当前值，若尝试读取将返回undefined。

语法：ctx.font = 'font-style font-weight font-size font-family'

- font-style(可选)，用于指定字体样式，支持如下几种样式：'normal','italic'。

- font-weight(可选)，用于指定字体的粗细，支持如下几种类型：'normal', 'bold', 'bolder', 'lighter', 100, 200, 300, 400, 500, 600, 700, 800, 900。

- font-size(可选)，指定字号和行高，单位支持px、vp。使用时需要添加单位。

- font-family(可选)，指定字体系列，支持如下几种类型：'sans-serif', 'serif', 'monospace'。

从API version 20开始，支持通过该接口设置注册过的自定义字体（只能在主线程使用，不支持在worker线程中使用；DevEco Studio的预览器不支持显示自定义字体）。自定义字体注册有以下两种方式。一种是通过ArkUI的异步接口this.uiContext.getFont().[registerFont](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-font#registerfont)注册，调用后立即绘制可能会导致自定义字体不生效。另一种是直接调用字体引擎的fontCollection.[loadFontSync](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-graphics-text#loadfontsync)接口来注册自定义字体到字体引擎。在直接调用字体引擎接口注册自定义字体时，fontCollection的实例需要是text.FontCollection.getGlobalInstance()，因为组件默认会从该实例加载字体。如果使用其他实例，可能会导致自定义字体不生效。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

  展开

| 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- |
| string | 否 | 否 | 默认值：'normal normal 14px sans-serif' |

```
import { text } from '@kit.ArkGraphics2D';

@Entry
@Component
struct FontDemo {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('rgb(213,213,213)')
        .onReady(() => {
          let offContext = this.offCanvas.getContext("2d", this.settings);
          // 常规字体样式，常规粗细，字体大小为30px，字体系列为sans-serif
          offContext.font = 'normal normal 30px sans-serif'
          offContext.fillText("Hello px", 20, 60)
          // 斜体样式，加粗，字体大小为30vp，字体系列为monospace
          offContext.font = 'italic bold 30vp monospace'
          offContext.fillText("Hello vp", 20, 100)
          // 加载rawfile目录下的自定义字体文件HarmonyOS_Sans_Thin_Italic.ttf
          let fontCollection = text.FontCollection.getGlobalInstance();
          fontCollection.loadFontSync('HarmonyOS_Sans_Thin_Italic', $rawfile("HarmonyOS_Sans_Thin_Italic.ttf"))
          // 加粗，字体大小为30vp，字体系列为HarmonyOS_Sans_Thin_Italic
          offContext.font = "bold 30vp HarmonyOS_Sans_Thin_Italic"
          offContext.fillText("Hello customFont", 20, 140)
          let image = this.offCanvas.transferToImageBitmap();
          this.context.transferFromImageBitmap(image)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170655.75388176734139687266000473319607:50001231000000:2800:07E9BCC62FC4A15AF893A110CD1E1ECDBC3882010F2021FF06DE3E11ED77D2E1.jpeg)

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
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('rgb(213,213,213)')
        .onReady(() => {
          let offContext = this.offCanvas.getContext("2d", this.settings)
          offContext.strokeStyle = 'rgb(39,135,217)'
          offContext.moveTo(140, 10)
          offContext.lineTo(140, 160)
          offContext.stroke()

          offContext.font = '50px sans-serif'

          // 设置textAlign属性为start
          offContext.textAlign = 'start'
          offContext.fillText('textAlign=start', 140, 60)
          // 设置textAlign属性为end
          offContext.textAlign = 'end'
          offContext.fillText('textAlign=end', 140, 80)
          // 设置textAlign属性为left
          offContext.textAlign = 'left'
          offContext.fillText('textAlign=left', 140, 100)
          // 设置textAlign属性为center
          offContext.textAlign = 'center'
          offContext.fillText('textAlign=center', 140, 120)
          // 设置textAlign属性为right
          offContext.textAlign = 'right'
          offContext.fillText('textAlign=right', 140, 140)
          let image = this.offCanvas.transferToImageBitmap()
          this.context.transferFromImageBitmap(image)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170655.16703299612468926933091836807154:50001231000000:2800:B044535E716E70F76BD2CD829A348B2CA81BFA926C6BB9863773A11902604410.png)

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
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('rgb(213,213,213)')
        .onReady(() => {
          let offContext = this.offCanvas.getContext("2d", this.settings)
          offContext.strokeStyle = '#0000ff'
          offContext.moveTo(0, 120)
          offContext.lineTo(400, 120)
          offContext.stroke()

          offContext.font = '20px sans-serif'

          // 设置textBaseline属性为top
          offContext.textBaseline = 'top'
          offContext.fillText('Top', 10, 120)
          // 设置textBaseline属性为bottom
          offContext.textBaseline = 'bottom'
          offContext.fillText('Bottom', 55, 120)
          // 设置textBaseline属性为middle
          offContext.textBaseline = 'middle'
          offContext.fillText('Middle', 125, 120)
          // 设置textBaseline属性为alphabetic
          offContext.textBaseline = 'alphabetic'
          offContext.fillText('Alphabetic', 195, 120)
          // 设置textBaseline属性为hanging
          offContext.textBaseline = 'hanging'
          offContext.fillText('Hanging', 295, 120)
          let image = this.offCanvas.transferToImageBitmap()
          this.context.transferFromImageBitmap(image)
      })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170655.41622045903141992654258298980435:50001231000000:2800:FF6BA76E3E7ADFFD0D7E5F5E6372656F0972E89920AC2A6CE2B65E1B33D2D26A.jpg)

### globalAlpha

 支持设备PhonePC/2in1TabletTVWearable

设置透明度，此属性为只写属性，可通过赋值语句设置其值，但无法通过读取操作获取其当前值，若尝试读取将返回undefined。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

  展开

| 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- |
| number | 否 | 否 | 范围为[0.0, 1.0]，0.0为完全透明，1.0为完全不透明。若给定值小于0.0，则取值0.0；若给定值大于1.0，则取值1.0。 API version 18之前，设置NaN或Infinity时，在该方法后执行的绘制方法无法绘制。API version 18及以后，设置NaN或Infinity时当前接口不生效，其他传入有效参数的绘制方法正常绘制。 默认值：1.0 |

```
// xxx.ets
@Entry
@Component
struct GlobalAlpha {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          let offContext = this.offCanvas.getContext("2d", this.settings)
          offContext.fillStyle = 'rgb(0,0,255)'
          offContext.fillRect(0, 0, 50, 50)
          // 设置globalAlpha属性
          offContext.globalAlpha = 0.4
          offContext.fillStyle = 'rgb(0,0,255)'
          offContext.fillRect(50, 50, 50, 50)
          let image = this.offCanvas.transferToImageBitmap()
          this.context.transferFromImageBitmap(image)
      })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170655.67190660450487254900633026180896:50001231000000:2800:C15B33AB66A734E1FF5382D082486B8AF1BFD37B59BCED4759B9DCD2709DB7BA.png)

### lineDashOffset

 支持设备PhonePC/2in1TabletTVWearable

设置画布的虚线偏移量，精度为float，仅当设置setLineDash时属性才生效，此属性为只写属性，可通过赋值语句设置其值，但无法通过读取操作获取其当前值，若尝试读取将返回undefined。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

  展开

| 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- |
| number | 否 | 否 | 默认值：0.0 单位：vp 异常值NaN和Infinity按默认值处理。 |

```
// xxx.ets
@Entry
@Component
struct LineDashOffset {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          let offContext = this.offCanvas.getContext("2d", this.settings)
          offContext.arc(100, 75, 50, 0, 6.28)
          offContext.setLineDash([10,20])
          // 设置lineDashOffset属性
          offContext.lineDashOffset = 10.0
          offContext.stroke()
          let image = this.offCanvas.transferToImageBitmap()
          this.context.transferFromImageBitmap(image)
      })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170655.78482721644845046574977901464239:50001231000000:2800:4F69718E5C5D0DA019BC07DE80E8437547162F17CB958070BB949F61665E902A.png)

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
            let offContext = new OffscreenCanvasRenderingContext2D(ctx1.width, ctx1.height, this.settings);
            offContext.fillStyle = 'rgb(39,135,217)';
            offContext.fillRect(25, 25, 75, 75); // 原有图形
            offContext.globalCompositeOperation = 'source-over'; // 默认值，可省略
            offContext.fillStyle = 'rgb(23,169,141)';
            offContext.fillRect(75, 75, 75, 75); // 新图形覆盖
            let image = offContext.transferToImageBitmap();
            this.context1.transferFromImageBitmap(image);
          })
        // 2. destination-out：新图形擦除原有图形（橡皮擦核心逻辑）
        Canvas(this.context2)
          .width('45%')
          .borderWidth(1)
          .margin(5)
          .onReady(() => {
            let ctx2 = this.context2;
            let offContext = new OffscreenCanvasRenderingContext2D(ctx2.width, ctx2.height, this.settings);
            // 先绘制背景
            offContext.fillStyle = 'rgb(39,135,217)';
            offContext.fillRect(0, 0, ctx2.width, ctx2.height);
            // 设置合成模式为擦除
            offContext.globalCompositeOperation = 'destination-out';
            // 绘制圆形作为橡皮擦
            offContext.beginPath();
            offContext.arc(ctx2.width / 2, ctx2.height / 2, 60, 0, Math.PI * 2);
            offContext.fill(); // 擦除圆形区域的背景
            let image = offContext.transferToImageBitmap();
            this.context2.transferFromImageBitmap(image);
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
            let offContext = new OffscreenCanvasRenderingContext2D(ctx3.width, ctx3.height, this.settings);
            // 先绘制原有图形（圆形蒙版）
            offContext.beginPath();
            offContext.arc(ctx3.width / 2, ctx3.height / 2, 80, 0, Math.PI * 2);
            offContext.fillStyle = '#fff';
            offContext.fill();
            // 设置合成模式
            offContext.globalCompositeOperation = 'source-in';
            // 绘制新图形（渐变矩形）
            const gradient = offContext.createLinearGradient(0, 0, ctx3.width, ctx3.height);
            gradient.addColorStop(0, 'rgb(23,169,141)');
            gradient.addColorStop(1, 'rgb(39,135,217)');
            offContext.fillStyle = gradient;
            offContext.fillRect(0, 0, 200, 200); // 仅圆形区域显示渐变
            let image = offContext.transferToImageBitmap();
            this.context3.transferFromImageBitmap(image);
          })
        // 4. lighter：新图形与原有图形叠加（亮度相加，滤色效果）
        Canvas(this.context4)
          .width('45%')
          .borderWidth(1)
          .margin(5)
          .onReady(() => {
            let ctx4 = this.context4;
            let offContext = new OffscreenCanvasRenderingContext2D(ctx4.width, ctx4.height, this.settings);
            // 原有图形（半透明红色圆）
            offContext.beginPath();
            offContext.arc(70, 100, 50, 0, Math.PI * 2);
            offContext.fillStyle = 'rgba(234, 67, 53, 0.7)';
            offContext.fill();
            // 设置合成模式
            offContext.globalCompositeOperation = 'lighter';
            // 新图形（半透明蓝色圆）
            offContext.beginPath();
            offContext.arc(110, 100, 50, 0, Math.PI * 2);
            offContext.fillStyle = 'rgba(66, 133, 244, 0.7)';
            offContext.fill(); // 重叠区域变成紫色（亮度叠加）
            let image = offContext.transferToImageBitmap();
            this.context4.transferFromImageBitmap(image);
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
            let offContext = new OffscreenCanvasRenderingContext2D(ctx5.width, ctx5.height, this.settings);
            // 原有图形（绿色矩形）
            offContext.fillStyle = 'rgb(23,169,141)';
            offContext.fillRect(0, 0, ctx5.width, ctx5.height);
            // 设置合成模式
            offContext.globalCompositeOperation = 'destination-atop';
            // 新图形（小圆形）
            offContext.beginPath();
            offContext.arc(ctx5.width / 2, ctx5.height / 2, 60, 0, Math.PI * 2);
            offContext.fillStyle = '#000';
            offContext.fill(); // 仅矩形与圆形重叠的部分保留
            let image = offContext.transferToImageBitmap();
            this.context5.transferFromImageBitmap(image);
          })
        // 6. 文字蒙版（“source-in”的高级用法）
        Canvas(this.context6)
          .width('45%')
          .borderWidth(1)
          .margin(5)
          .onReady(() => {
            let ctx6 = this.context6;
            let offContext = new OffscreenCanvasRenderingContext2D(ctx6.width, ctx6.height, this.settings);
            // 先绘制文字（作为蒙版）
            offContext.font = 'bold 40vp';
            offContext.textAlign = 'center';
            offContext.textBaseline = 'middle';
            offContext.fillText('CANVAS', ctx6.width / 2, ctx6.height / 2);
            // 设置合成模式
            offContext.globalCompositeOperation = 'source-in';
            // 绘制渐变背景（仅文字区域显示）
            let textGradient = offContext.createLinearGradient(50, 0, 300, 100);
            textGradient.addColorStop(0.0, 'rgb(39,135,217)');
            textGradient.addColorStop(0.5, 'rgb(255,238,240)');
            textGradient.addColorStop(1.0, 'rgb(23,169,141)');
            offContext.fillStyle = textGradient;
            offContext.fillRect(0, 0, 200, 200); // 渐变仅填充文字区域
            let image = offContext.transferToImageBitmap();
            this.context6.transferFromImageBitmap(image);
          })
      }
      .height('30%')
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170655.67717311365314731208749357159444:50001231000000:2800:815CAB86E2BB730D3F420372385C869EA45269E331D36FDF3A15E30531A9A495.png)

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
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('rgb(213,213,213)')
        .onReady(() =>{
          let offContext = this.offCanvas.getContext("2d", this.settings)
          // 设置shadowBlur属性
          offContext.shadowBlur = 30
          offContext.shadowColor = 'rgb(0,0,0)'
          offContext.fillStyle = 'rgb(39,135,217)'
          offContext.fillRect(20, 20, 100, 80)
          let image = this.offCanvas.transferToImageBitmap()
          this.context.transferFromImageBitmap(image)
      })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170655.46474958560104675032616603768012:50001231000000:2800:AC9339C533C059E074846E7A69B96B3F10BD4ECA19FBA99368881C1BD7B1B5FD.jpg)

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
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('rgb(213,213,213)')
        .onReady(() => {
          let offContext = this.offCanvas.getContext("2d", this.settings)
          offContext.shadowBlur = 30
          // 设置shadowColor属性
          offContext.shadowColor = 'rgb(255,192,0)'
          offContext.fillStyle = 'rgb(39,135,217)'
          offContext.fillRect(30, 30, 100, 100)
          let image = this.offCanvas.transferToImageBitmap()
          this.context.transferFromImageBitmap(image)
      })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170655.12897235467851482466259857873098:50001231000000:2800:4FA720B6B0923ADAE845D6F7FAD60702DC5538E1CE0B4CDA0BBA06B1A63DD185.jpg)

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
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          let offContext = this.offCanvas.getContext("2d", this.settings)
          offContext.shadowBlur = 10
          // 设置shadowOffsetX属性
          offContext.shadowOffsetX = 20
          offContext.shadowColor = 'rgb(0,0,0)'
          offContext.fillStyle = 'rgb(255,0,0)'
          offContext.fillRect(20, 20, 100, 80)
          let image = this.offCanvas.transferToImageBitmap()
          this.context.transferFromImageBitmap(image)
      })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170655.95453071911884831483085220323740:50001231000000:2800:C17626D221AC1E27EEA775A3021AF8A1052E6AA7123C6AC7BB00B084394C4616.png)

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
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          let offContext = this.offCanvas.getContext("2d", this.settings)
          offContext.shadowBlur = 10
          // 设置shadowOffsetY属性
          offContext.shadowOffsetY = 20
          offContext.shadowColor = 'rgb(0,0,0)'
          offContext.fillStyle = 'rgb(255,0,0)'
          offContext.fillRect(30, 30, 100, 100)
          let image = this.offCanvas.transferToImageBitmap()
          this.context.transferFromImageBitmap(image)
      })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170655.09824687450043940849508093444172:50001231000000:2800:956E2B01CBF84C4AF525C25FD05FC43A687C22F21D9C7F5455413384A384F872.png)

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
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  // "common/images/icon.jpg"需要替换为开发者所需的图像资源文件
  private img:ImageBitmap = new ImageBitmap("common/images/icon.jpg");
  private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          let offContext = this.offCanvas.getContext("2d", this.settings)
          // 设置imageSmoothingEnabled属性
          offContext.imageSmoothingEnabled = false
          offContext.drawImage(this.img,0,0,400,200)
          let image = this.offCanvas.transferToImageBitmap()
          this.context.transferFromImageBitmap(image)
      })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170655.47633610644624764698337486400624:50001231000000:2800:C8ACAD055BC2055BF4748B10D846DF894A17D129BD0934257AA7181EF99E7C73.png)

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
  struct ImageSmoothingQualityDemoOff {
    private settings: RenderingContextSettings = new RenderingContextSettings(true);
    private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.
settings);
    private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);
    // "common/images/example.jpg"需要替换为开发者所需的图像资源文件
    private img:ImageBitmap = new ImageBitmap("common/images/example.jpg");

    build() {
      Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center,
justifyContent: FlexAlign.Center }) {
        Canvas(this.context)
          .width('100%')
          .height('100%')
          .backgroundColor('#ffff00')
          .onReady(() =>{
            let offContext = this.offCanvas.getContext("2d", this.settings)
            let offctx = offContext
            offctx.imageSmoothingEnabled = true
            // 设置imageSmoothingQuality属性
            offctx.imageSmoothingQuality = 'high'
            offctx.drawImage(this.img, 0, 0, 400, 200)

            let image = this.offCanvas.transferToImageBitmap()
            this.context.transferFromImageBitmap(image)
          })
      }
      .width('100%')
      .height('100%')
    }
  }
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170656.98546957373413933367937747084211:50001231000000:2800:11B67BA4432BCA4647684032149F9742BDA82F484D00657A46677235D70CE668.jpeg)

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
  struct DirectionDemoOff {
    private settings: RenderingContextSettings = new RenderingContextSettings(true);
    private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.
settings);
    private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

    build() {
      Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center,
justifyContent: FlexAlign.Center }) {
        Canvas(this.context)
          .width('100%')
          .height('100%')
          .backgroundColor('#ffff00')
          .onReady(() =>{
            let offContext = this.offCanvas.getContext("2d", this.settings)
            let offctx = offContext
            offctx.font = '48px serif';
            offctx.textAlign = 'start'
            offctx.fillText("Hi ltr!", 200, 50);

            // 设置direction属性
            offctx.direction = "rtl";
            offctx.fillText("Hi rtl!", 200, 100);

            let image = offctx.transferToImageBitmap()
            this.context.transferFromImageBitmap(image)
          })
      }
      .width('100%')
      .height('100%')
    }
  }
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170656.14581813673857536641631021235653:50001231000000:2800:15BC27F6A627AA418B69188721D6E978BFEA89ED4C8135AA9867F261D0A49435.jpeg)

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
  struct FilterDemoOff {
    private settings: RenderingContextSettings = new RenderingContextSettings(true);
    private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
    private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);
    // "common/images/example.jpg"需要替换为开发者所需的图像资源文件
    private img: ImageBitmap = new ImageBitmap("common/images/example.jpg");

    build() {
      Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
        Canvas(this.context)
          .width('100%')
          .height('100%')
          .onReady(() => {
            let offContext = this.offCanvas.getContext("2d", this.settings)
            let img = this.img

            offContext.drawImage(img, 0, 0, 100, 100);

            offContext.filter = 'grayscale(50%)';
            offContext.drawImage(img, 100, 0, 100, 100);

            offContext.filter = 'sepia(60%)';
            offContext.drawImage(img, 200, 0, 100, 100);

            offContext.filter = 'saturate(30%)';
            offContext.drawImage(img, 0, 100, 100, 100);

            offContext.filter = 'hue-rotate(90deg)';
            offContext.drawImage(img, 100, 100, 100, 100);

            offContext.filter = 'invert(100%)';
            offContext.drawImage(img, 200, 100, 100, 100);

            offContext.filter = 'opacity(25%)';
            offContext.drawImage(img, 0, 200, 100, 100);

            offContext.filter = 'brightness(0.4)';
            offContext.drawImage(img, 100, 200, 100, 100);

            offContext.filter = 'contrast(200%)';
            offContext.drawImage(img, 200, 200, 100, 100);

            offContext.filter = 'blur(5px)';
            offContext.drawImage(img, 0, 300, 100, 100);

            // Applying multiple filters
            offContext.filter = 'opacity(50%) contrast(200%) grayscale(50%)';
            offContext.drawImage(img, 100, 300, 100, 100);

            let image = this.offCanvas.transferToImageBitmap()
            this.context.transferFromImageBitmap(image)
          })
      }
      .width('100%')
      .height('100%')
    }
  }
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170656.45442406092827560541411526617450:50001231000000:2800:85DC980F9C068E47B00AF47CDFD14D6864C77B0133B9BE615BC7311F1A93AFF4.jpeg)

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
  import { LengthMetrics, LengthUnit } from '@kit.ArkUI';

  @Entry
  @Component
  struct letterSpacingDemo {
    private settings: RenderingContextSettings = new RenderingContextSettings(true);
    private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
    private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

    build() {
      Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
        Canvas(this.context)
          .width('100%')
          .height('100%')
          .backgroundColor('rgb(213,213,213)')
          .onReady(() => {
            let offContext = this.offCanvas.getContext("2d", this.settings)
            offContext.font = '30vp'
            // 使用string设置direction属性
            offContext.letterSpacing = '10vp'
            offContext.fillText('hello world', 30, 50)
            // 使用LengthMetrics对象设置direction属性
            offContext.letterSpacing = new LengthMetrics(10, LengthUnit.VP)
            offContext.fillText('hello world', 30, 100)
            let image = this.offCanvas.transferToImageBitmap()
            this.context.transferFromImageBitmap(image)
          })
      }
      .width('100%')
      .height('100%')
    }
  }
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170656.20527016099298141567091970624764:50001231000000:2800:BABBB238D1C0F84132CC46F32B6BEB1B948CBF290D8F5CF4BD2228BC0B28A7FD.jpeg)

## 方法

 支持设备PhonePC/2in1TabletTVWearable  

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
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('rgb(213,213,213)')
        .onReady(() =>{
          let offContext = this.offCanvas.getContext("2d", this.settings)
          offContext.fillRect(30,30,100,100)
          let image = this.offCanvas.transferToImageBitmap()
          this.context.transferFromImageBitmap(image)
       })
      }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170656.43858448176141994903582572611433:50001231000000:2800:58B747B8E6B107407EC71B2FF3B35CA90659D9F5DE14BA10E6E1B9977751DFEA.jpg)

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
| width | number | 是 | 指定矩形的宽度。 异常值undefined、null、NaN或Infinity按无效值处理，不进行绘制。 默认单位：vp |
| height | number | 是 | 指定矩形的高度。 异常值undefined、null、NaN或Infinity按无效值处理，不进行绘制。 默认单位：vp |

**示例：**

```
// xxx.ets
@Entry
@Component
struct StrokeRect {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          let offContext = this.offCanvas.getContext("2d", this.settings)
          offContext.strokeRect(30, 30, 200, 150)
          let image = this.offCanvas.transferToImageBitmap()
          this.context.transferFromImageBitmap(image)
      })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170656.25051854490417401459764733281965:50001231000000:2800:A36DD607E449441B6F9FDDD40C7BB92B70337987AAA84902D7122A29AE2AA08E.png)

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
| width | number | 是 | 指定矩形的宽度。 异常值undefined、null、NaN或Infinity按无效值处理，不进行绘制。 默认单位：vp |
| height | number | 是 | 指定矩形的高度。 异常值undefined、null、NaN或Infinity按无效值处理，不进行绘制。 默认单位：vp |

**示例：**

```
// xxx.ets
@Entry
@Component
struct ClearRect {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          let offContext = this.offCanvas.getContext("2d", this.settings)
          offContext.fillStyle = 'rgb(0,0,255)'
          offContext.fillRect(20,20,200,200)
          offContext.clearRect(30,30,150,100)
          let image = this.offCanvas.transferToImageBitmap()
          this.context.transferFromImageBitmap(image)
      })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170656.41609789464279917318824837530611:50001231000000:2800:A74F50FEE81C03E9BAF39CE4800C234EC8A36BF88FA9EB251A852CC261600F42.png)

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
| maxWidth | number | 否 | 指定文本允许的最大宽度。 异常值null按无效值处理，不进行绘制，undefined、NaN或Infinity按默认值处理。 默认单位：vp 默认值：不限制宽度。 |

**示例：**

```
// xxx.ets
@Entry
@Component
struct FillText {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          let offContext = this.offCanvas.getContext("2d", this.settings)
          offContext.font = '30px sans-serif'
          offContext.fillText("Hello World!", 20, 100)
          let image = this.offCanvas.transferToImageBitmap()
          this.context.transferFromImageBitmap(image)
      })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170656.17196189487226000350819637318115:50001231000000:2800:CD29A54ADAF705A12875F9FE35F04D3705537EEF8C26EA393305F9E8873D3760.png)

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
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          let offContext = this.offCanvas.getContext("2d", this.settings)
          offContext.font = '55px sans-serif'
          offContext.strokeText("Hello World!", 20, 60)
          let image = this.offCanvas.transferToImageBitmap()
          this.context.transferFromImageBitmap(image)
      })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170656.16217000091587295611108692961118:50001231000000:2800:AF717069D8941C60BEC9F76418CEDFA8612C69CF19E7FA9281FFFB9C03360643.png)

### measureText

 支持设备PhonePC/2in1TabletTVWearable

measureText(text: string): TextMetrics

该方法返回一个文本测算的对象，通过该对象可以获取指定文本的宽度值。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | string | 是 | 需要进行测量的文本。 |

**返回值：**

  展开

| 类型 | 说明 |
| --- | --- |
| TextMetrics | 文本的尺寸信息。 传入异常值undefined或null时按"undefined"或"null"计算。 |

**示例：**

```
// xxx.ets
@Entry
@Component
struct MeasureText {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('rgb(213,213,213)')
        .onReady(() => {
          let offContext = this.offCanvas.getContext("2d", this.settings)
          offContext.font = '50px sans-serif'
          offContext.fillText("Hello World!", 20, 100)
          offContext.fillText("width:" + offContext.measureText("Hello World!").width, 20, 200)
          let image = this.offCanvas.transferToImageBitmap()
          this.context.transferFromImageBitmap(image)
      })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170656.27650596779101802091268864993642:50001231000000:2800:7C22CD45A679F95D2D038907DDFF89F59024CF17709E4ABAE2CF2E595BF5B26A.jpg)

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
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() => {
          let offContext = this.offCanvas.getContext("2d", this.settings)
          offContext.moveTo(125, 25)
          offContext.lineTo(125, 105)
          offContext.lineTo(175, 105)
          offContext.lineTo(175, 25)
          offContext.strokeStyle = 'rgb(255,0,0)'
          offContext.stroke()
          let image = this.offCanvas.transferToImageBitmap()
          this.context.transferFromImageBitmap(image)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170656.28873139474864560016408731087392:50001231000000:2800:F1DE224692AC073416842BFA7D13EA7DF10487A9E141AFD034933F7D37F61B03.png)

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
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);
  private path2Da: Path2D = new Path2D();

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() => {
          let offContext = this.offCanvas.getContext("2d", this.settings)
          this.path2Da.moveTo(25, 25)
          this.path2Da.lineTo(25, 105)
          this.path2Da.lineTo(75, 105)
          this.path2Da.lineTo(75, 25)
          offContext.strokeStyle = 'rgb(0,0,255)'
          offContext.stroke(this.path2Da)
          let image = this.offCanvas.transferToImageBitmap()
          this.context.transferFromImageBitmap(image)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170656.60147011227763901706274731025896:50001231000000:2800:93D8F03DCE858EBD5C303A1D7B95DA0475E8792C61EEA13268048EFB5B590013.png)

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
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('rgb(213,213,213)')
        .onReady(() => {
          let offContext = this.offCanvas.getContext("2d", this.settings)
          offContext.beginPath()
          offContext.lineWidth = 6
          offContext.strokeStyle = '#0000ff'
          offContext.moveTo(15, 80)
          offContext.lineTo(280, 160)
          offContext.stroke()
          let image = this.offCanvas.transferToImageBitmap()
          this.context.transferFromImageBitmap(image)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170656.74590172450980872286074304346109:50001231000000:2800:874DE4E6675051AE466EB27ED5B81CB333860B9B53C8F8E25A37EA2BA9CC2B0D.jpg)

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
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          let offContext = this.offCanvas.getContext("2d", this.settings)
          offContext.beginPath()
          offContext.moveTo(10, 10)
          offContext.lineTo(280, 160)
          offContext.stroke()
          let image = this.offCanvas.transferToImageBitmap()
          this.context.transferFromImageBitmap(image)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170656.39265205229935703156528773706606:50001231000000:2800:FC094584E5EE29FC6CE5BC1853B4A67F96E17EE2525378B9801C2D63883E994C.png)

### lineTo

 支持设备PhonePC/2in1TabletTVWearable

lineTo(x: number, y: number): void

从当前点到指定点进行路径连接。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| x | number | 是 | 指定位置的x坐标。 API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。 默认单位：vp |
| y | number | 是 | 指定位置的y坐标。 API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。 默认单位：vp |

**示例：**

```
// xxx.ets
@Entry
@Component
struct LineTo {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          let offContext = this.offCanvas.getContext("2d", this.settings)
          offContext.beginPath()
          offContext.moveTo(10, 10)
          offContext.lineTo(280, 160)
          offContext.stroke()
          let image = this.offCanvas.transferToImageBitmap()
          this.context.transferFromImageBitmap(image)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170656.08655903613033653172660510128510:50001231000000:2800:0AF7CA21821442497E1C571022BBDEB033FC1A4C56470BE8762772AD25CFC13A.png)

### closePath

 支持设备PhonePC/2in1TabletTVWearable

closePath(): void

结束当前路径形成一个封闭路径。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```
// xxx.ets
@Entry
@Component
struct ClosePath {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
            let offContext = this.offCanvas.getContext("2d", this.settings)
            offContext.beginPath()
            offContext.moveTo(30, 30)
            offContext.lineTo(110, 30)
            offContext.lineTo(70, 90)
            offContext.closePath()
            offContext.stroke()
            let image = this.offCanvas.transferToImageBitmap()
            this.context.transferFromImageBitmap(image)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170656.11104506794618825131406804173730:50001231000000:2800:6A25361B8F5DF83B73A895B93A477B409534503447CBC33BDBC970069E03BD47.png)

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
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  // "common/images/example.jpg"需要替换为开发者所需的图像资源文件
  private img:ImageBitmap = new ImageBitmap("common/images/example.jpg");
  private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('rgb(213,213,213)')
        .onReady(() => {
          let offContext = this.offCanvas.getContext("2d", this.settings)
          let pattern = offContext.createPattern(this.img, 'repeat')
          offContext.fillStyle = pattern as CanvasPattern
          offContext.fillRect(0, 0, 200, 200)
          let image = this.offCanvas.transferToImageBitmap()
          this.context.transferFromImageBitmap(image)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170656.27761313804977071405786201626968:50001231000000:2800:CA4BB84C4649D35194D4BA87D1092A65745B97BD9E41EDE88E2F5F7F38D58901.jpg)

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
  private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);
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
          let offContext = this.offCanvas.getContext("2d", this.settings)
          // 三次贝塞尔曲线
          offContext.beginPath();
          offContext.moveTo(this.start.x, this.start.y);
          offContext.bezierCurveTo(this.cp1.x, this.cp1.y, this.cp2.x, this.cp2.y, this.end.x, this.end.y);
          offContext.stroke();

          // 起点和终点
          offContext.fillStyle = 'rgb(39,135,217)';
          offContext.beginPath();
          offContext.arc(this.start.x, this.start.y, 5, 0, 2 * Math.PI); // 起点
          offContext.arc(this.end.x, this.end.y, 5, 0, 2 * Math.PI); // 终点
          offContext.fill();

          // 控制点
          offContext.fillStyle = 'rgb(23,169,141)';
          offContext.beginPath();
          offContext.arc(this.cp1.x, this.cp1.y, 5, 0, 2 * Math.PI); // 控制点一
          offContext.arc(this.cp2.x, this.cp2.y, 5, 0, 2 * Math.PI); // 控制点二
          offContext.fill();
          let image = this.offCanvas.transferToImageBitmap();
          this.context.transferFromImageBitmap(image);
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170657.03476523780125697520184398833637:50001231000000:2800:BE25463021DBF43CDEE9117F1E0BC5D9EA8A2BEF073AF80753091FC002321191.png)

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
  private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);
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
          let offContext = this.offCanvas.getContext("2d", this.settings);
          // 二次贝塞尔曲线
          offContext.beginPath();
          offContext.moveTo(this.start.x, this.start.y);
          offContext.quadraticCurveTo(this.cp.x, this.cp.y, this.end.x, this.end.y);
          offContext.stroke();

          // 起始点和结束点
          offContext.fillStyle = 'rgb(39,135,217)';
          offContext.beginPath();
          offContext.arc(this.start.x, this.start.y, 5, 0, 2 * Math.PI); // 起始点
          offContext.arc(this.end.x, this.end.y, 5, 0, 2 * Math.PI); // 结束点
          offContext.fill();

          // 控制点
          offContext.fillStyle = 'rgb(23,169,141)';
          offContext.beginPath();
          offContext.arc(this.cp.x, this.cp.y, 5, 0, 2 * Math.PI);
          offContext.fill();

          let image = this.offCanvas.transferToImageBitmap();
          this.context.transferFromImageBitmap(image);
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170657.92786594660987039782456175140122:50001231000000:2800:2EEE6797D25BC23DFBFC96D9D37FBF5BAD17B3FE38009DCAA964FFF582B7D123.png)

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
| startAngle | number | 是 | 弧线的起始弧度。 API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。 默认单位：弧度 |
| endAngle | number | 是 | 弧线的终止弧度。 API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。 默认单位：弧度 |
| counterclockwise | boolean | 否 | 是否逆时针绘制圆弧。 true：逆时针绘制圆弧；false：顺时针绘制圆弧。 默认值：false，设置null或undefined按默认值处理。 |

**示例：**

```
// xxx.ets
@Entry
@Component
struct Arc {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          let offContext = this.offCanvas.getContext("2d", this.settings)
          offContext.beginPath()
          offContext.arc(100, 75, 50, 0, 6.28)
          offContext.stroke()
          let image = this.offCanvas.transferToImageBitmap()
          this.context.transferFromImageBitmap(image)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170657.93992070387673904803597887181565:50001231000000:2800:801F09AF964B6B8F293DF6D6363C84F6A4462794C733F7A6523CCB20FCBD698A.jpeg)

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
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          let offContext = this.offCanvas.getContext("2d", this.settings)

          // 切线
          offContext.beginPath()
          offContext.strokeStyle = '#808080'
          offContext.lineWidth = 1.5;
          offContext.moveTo(360, 20);
          offContext.lineTo(360, 170);
          offContext.lineTo(110, 170);
          offContext.stroke();

          // 圆弧
          offContext.beginPath()
          offContext.strokeStyle = '#000000'
          offContext.lineWidth = 3;
          offContext.moveTo(360, 20)
          offContext.arcTo(360, 170, 110, 170, 150)
          offContext.stroke()

          // 起始点
          offContext.beginPath();
          offContext.fillStyle = '#00ff00';
          offContext.arc(360, 20, 4, 0, 2 * Math.PI);
          offContext.fill();

          // 控制点
          offContext.beginPath();
          offContext.fillStyle = '#ff0000';
          offContext.arc(360, 170, 4, 0, 2 * Math.PI);
          offContext.arc(110, 170, 4, 0, 2 * Math.PI);
          offContext.fill();

          let image = this.offCanvas.transferToImageBitmap()
          this.context.transferFromImageBitmap(image)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170657.19964335089228733331452757202456:50001231000000:2800:55A3BD4C284922433BE0B2DF8B9A4F1EB1069F89538C98CCF6B3F737A05EF962.png)

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
| rotation | number | 是 | 椭圆的旋转角度。 API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。 单位为弧度。 |
| startAngle | number | 是 | 椭圆绘制的起始点角度。 API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。 单位为弧度。 |
| endAngle | number | 是 | 椭圆绘制的结束点角度。 API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。 单位为弧度。 |
| counterclockwise | boolean | 否 | 是否以逆时针方向绘制椭圆。 true：逆时针方向绘制椭圆。 false：顺时针方向绘制椭圆。 默认值：false，设置null或undefined按默认值处理。 |

**示例：**

```
// xxx.ets
@Entry
@Component
struct CanvasExample {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);
  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          let offContext = this.offCanvas.getContext("2d", this.settings)
          offContext.beginPath()
          offContext.ellipse(200, 200, 50, 100, Math.PI * 0.25, Math.PI * 0.5, Math.PI * 2, false)
          offContext.stroke()
          offContext.beginPath()
          offContext.ellipse(200, 300, 50, 100, Math.PI * 0.25, Math.PI * 0.5, Math.PI * 2, true)
          offContext.stroke()
          let image = this.offCanvas.transferToImageBitmap()
          this.context.transferFromImageBitmap(image)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170657.39062781497135116873884833162762:50001231000000:2800:4586CE79B18A5B35937B228BC8A95791DA1A7D1CD2534EC199F960C0B55B7160.jpeg)

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
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          let offContext = this.offCanvas.getContext("2d", this.settings)
          offContext.rect(20, 20, 100, 100) // Create a 100*100 rectangle at (20, 20)
          offContext.stroke()
          let image = this.offCanvas.transferToImageBitmap()
          this.context.transferFromImageBitmap(image)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170657.47192877246031717909153405471801:50001231000000:2800:599025D7A73800C928F9430FBC16B5BE1A503D9E5111D1EF72D8D377D9BBE126.jpeg)

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
| radii | number \| Array<number> | 否 | 指定用于矩形角的圆弧半径的数字或列表。 参数类型为number时，所有矩形角的圆弧半径按该数字执行。 参数类型为Array<number>时，数目为1-4个按下面执行： 1. [所有矩形角的圆弧半径] 2. [左上及右下矩形角的圆弧半径, 右上及左下矩形角的圆弧半径] 3. [左上矩形角的圆弧半径, 右上及左下矩形角的圆弧半径, 右下矩形角的圆弧半径] 4. [左上矩形角的圆弧半径, 右上矩形角的圆弧半径, 右下矩形角的圆弧半径, 左下矩形角的圆弧半径] radii存在负数或列表的数目不在[1,4]内时抛出异常，错误码：103701。 默认值：0，null和undefined按默认值处理。 圆弧半径超过矩形宽高时会等比例缩放到宽高的长度。 默认单位：vp |

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
  private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#D5D5D5')
        .onReady(() => {
          let offContext = this.offCanvas.getContext("2d", this.settings)
          try {
            offContext.fillStyle = '#707070'
            offContext.beginPath()
            // 创建一个(10vp, 10vp)为起点，宽高为100vp，四个矩形角圆弧半径为10vp的圆角矩形
            offContext.roundRect(10, 10, 100, 100, 10)
            // 创建一个(120vp, 10vp)为起点，宽高为100vp，四个矩形角圆弧半径为10vp的圆角矩形
            offContext.roundRect(120, 10, 100, 100, [10])
            offContext.fill()
            offContext.beginPath()
            // 创建一个(10vp, 120vp)为起点，宽高为100vp，左上矩形角圆弧半径及右下矩形角圆弧半径为10vp，右上矩形角圆弧半径及左下矩形角圆弧半径为20vp的圆角矩形
            offContext.roundRect(10, 120, 100, 100, [10, 20])
            // 创建一个(120vp, 120vp)为起点，宽高为100vp，左上矩形角圆弧半径为10vp，右上矩形角圆弧半径及左下矩形角圆弧半径为20vp，右下矩形角圆弧半径为30vp的圆角矩形
            offContext.roundRect(120, 120, 100, 100, [10, 20, 30])
            // 创建一个(10vp, 230vp)为起点，宽高为100vp，左上矩形角圆弧半径为10vp，右上矩形角圆弧半径为20vp，右下矩形角圆弧半径为30vp，左下矩形角圆弧半径为40vp的圆角矩形
            offContext.roundRect(10, 230, 100, 100, [10, 20, 30, 40])
            // 创建一个(220vp, 330vp)为起点，宽高为-100vp，左上矩形角圆弧半径为10vp，右上矩形角圆弧半径为20vp，右下矩形角圆弧半径为30vp，左下矩形角圆弧半径为40vp的圆角矩形
            offContext.roundRect(220, 330, -100, -100, [10, 20, 30, 40])
            offContext.stroke()
          } catch (error) {
            let e: BusinessError = error as BusinessError;
            console.error(`Failed to create roundRect. Code: ${e.code}, message: ${e.message}`);
          }
          // 在离屏画布最近渲染的图像上创建一个ImageBitmap对象
          let image = this.offCanvas.transferToImageBitmap()
          // 将创建的ImageBitmap对象显示在Canvas画布上
          this.context.transferFromImageBitmap(image)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170657.25813792408213850218525528229838:50001231000000:2800:B9CE201E2E62E717E07EC795EBDEC90C66D578CA47F4674F138708C11F59EE6A.jpeg)

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

```
// xxx.ets
@Entry
@Component
struct Fill {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          let offContext = this.offCanvas.getContext("2d", this.settings)
          offContext.fillStyle = '#000000'
          offContext.rect(20, 20, 100, 100) // Create a 100*100 rectangle at (20, 20)
          offContext.fill()
          let image = this.offCanvas.transferToImageBitmap()
          this.context.transferFromImageBitmap(image)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170657.51695298585314212343000134100222:50001231000000:2800:7500C00F381709537075570DC3618EA1245C3D2AAA22FDF5909DEEDD01B1C511.png)

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
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          let offContext = this.offCanvas.getContext("2d", this.settings)
          let region = new Path2D()
          region.moveTo(30, 90)
          region.lineTo(110, 20)
          region.lineTo(240, 130)
          region.lineTo(60, 130)
          region.lineTo(190, 20)
          region.lineTo(270, 90)
          region.closePath()
          // Fill path
          offContext.fillStyle = '#00ff00'
          offContext.fill(region, "evenodd")
          let image = this.offCanvas.transferToImageBitmap()
          this.context.transferFromImageBitmap(image)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170657.30043780194363320091255398759659:50001231000000:2800:9C9BD32C6001CA5E812890CD9CAFA3CC02237638505FB72892D6C6EE6AB084D8.jpg)

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

**示例：**

```
// xxx.ets
@Entry
@Component
struct Clip {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          let offContext = this.offCanvas.getContext("2d", this.settings)
          offContext.rect(0, 0, 100, 200)
          offContext.stroke()
          offContext.clip()
          offContext.fillStyle = "rgb(255,0,0)"
          offContext.fillRect(0, 0, 200, 200)
          let image = this.offCanvas.transferToImageBitmap()
          this.context.transferFromImageBitmap(image)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170657.44564215938955488843344030192993:50001231000000:2800:83C03CE00EF13C43D7D88AD04E097C0A7BC016B60BE24D752A810CACB0F639E2.png)

### clip

 支持设备PhonePC/2in1TabletTVWearable

clip(path: Path2D, fillRule?: CanvasFillRule): void

设置指定路径为剪切路径。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数:**

  展开

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| path | Path2D | 是 | Path2D剪切路径。 异常值undefined或null按无效值处理。 |
| fillRule | CanvasFillRule | 否 | 指定要剪切对象的规则。 可选参数为："nonzero"，"evenodd"。 异常值undefined或null按默认值处理。 默认值："nonzero" |

**示例：**

```
// xxx.ets
@Entry
@Component
struct Clip {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          let offContext = this.offCanvas.getContext("2d", this.settings)
          let region = new Path2D()
          region.moveTo(30, 90)
          region.lineTo(110, 20)
          region.lineTo(240, 130)
          region.lineTo(60, 130)
          region.lineTo(190, 20)
          region.lineTo(270, 90)
          region.closePath()
          offContext.clip(region,"evenodd")
          offContext.fillStyle = "rgb(0,255,0)"
          offContext.fillRect(0, 0, 600, 600)
          let image = this.offCanvas.transferToImageBitmap()
          this.context.transferFromImageBitmap(image)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170657.29862018117620351318348294415847:50001231000000:2800:857724CDF07D5BCEF4D4D0A39360E0CEB8BB6DA71A7400BE5A9E0BEFC20682AB.jpg)

### reset 12+

 支持设备PhonePC/2in1TabletTVWearable

reset(): void

将OffscreenCanvasRenderingContext2D重置为其默认状态，清除后台缓冲区、绘制状态栈、绘制路径和样式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```
// xxx.ets
@Entry
@Component
struct Reset {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          let offContext = this.offCanvas.getContext("2d", this.settings)
          offContext.fillStyle = '#0000ff'
          offContext.fillRect(20, 20, 150, 100)
          offContext.reset()
          offContext.fillRect(20, 150, 150, 100)
          let image = this.offCanvas.transferToImageBitmap()
          this.context.transferFromImageBitmap(image)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170657.68320542916321577093411391047467:50001231000000:2800:4915928BF256E6AAA8392437214814C8855916F4E64A6AB24F77ED21DF4E1A4A.png)

### saveLayer 12+

 支持设备PhonePC/2in1TabletTVWearable

saveLayer(): void

创建一个图层。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```
// xxx.ets
@Entry
@Component
struct saveLayer {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() => {
          let offContext = this.offCanvas.getContext("2d", this.settings)
          offContext.fillStyle = "#0000ff"
          offContext.fillRect(50,100,300,100)
          offContext.fillStyle = "#00ffff"
          offContext.fillRect(50,150,300,100)
          offContext.globalCompositeOperation = 'destination-over'
          offContext.saveLayer()
          offContext.globalCompositeOperation = 'source-over'
          offContext.fillStyle = "#ff0000"
          offContext.fillRect(100,50,100,300)
          offContext.fillStyle = "#00ff00"
          offContext.fillRect(150,50,100,300)
          offContext.restoreLayer()
          let image = this.offCanvas.transferToImageBitmap()
          this.context.transferFromImageBitmap(image)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170657.60217985622073388490804571010453:50001231000000:2800:A0875BD3CEA283DE30FCEECE052E4D695AD081DD55F9F33EE7E74977BEBB9990.png)

### restoreLayer 12+

 支持设备PhonePC/2in1TabletTVWearable

restoreLayer(): void

恢复图像变换和裁剪状态至saveLayer前的状态，并将图层绘制在canvas上。restoreLayer示例同saveLayer。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

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
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() => {
          let offContext = this.offCanvas.getContext("2d", this.settings)
          offContext.setTransform(1,0.5, -0.5, 1, 10, 10)
          offContext.fillStyle = 'rgb(0,0,255)'
          offContext.fillRect(0, 0, 100, 100)
          offContext.resetTransform()
          offContext.fillStyle = 'rgb(255,0,0)'
          offContext.fillRect(0, 0, 100, 100)
          let image = this.offCanvas.transferToImageBitmap()
          this.context.transferFromImageBitmap(image)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170657.29717763844396626732688325762941:50001231000000:2800:EF452C6D7758A87A9E95ADB0BB6B78359285FCBF0397370E3E6D6DF3EAD0F7EB.png)

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
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          let offContext = this.offCanvas.getContext("2d", this.settings)
          offContext.rotate(45 * Math.PI / 180)
          offContext.fillRect(70, 20, 50, 50)
          let image = this.offCanvas.transferToImageBitmap()
          this.context.transferFromImageBitmap(image)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170657.15526541684058096729497245576255:50001231000000:2800:A7AB1F260DA858DC6D742142EA97CCCC607858C140861AD54178756A6D8DC679.png)

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
| x | number | 是 | 设置水平方向的缩放值。 API version 18之前，设置NaN或Infinity时，在该方法后执行的绘制方法无法绘制；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的绘制方法正常绘制。 |
| y | number | 是 | 设置垂直方向的缩放值。 API version 18之前，设置NaN或Infinity时，在该方法后执行的绘制方法无法绘制；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的绘制方法正常绘制。 |

**示例：**

```
// xxx.ets
@Entry
@Component
struct Scale {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          let offContext = this.offCanvas.getContext("2d", this.settings)
          offContext.lineWidth = 3
          offContext.strokeRect(30, 30, 50, 50)
          offContext.scale(2, 2) // Scale to 200%
          offContext.strokeRect(30, 30, 50, 50)
          let image = this.offCanvas.transferToImageBitmap()
          this.context.transferFromImageBitmap(image)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170657.26315645198459372107716619444147:50001231000000:2800:8130BD4038F259FBF2F25C990F5DE1264DE46E7CE478C633D56F8DC5B487FC66.png)

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
struct Transform {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('rgb(213,213,213)')
        .onReady(() => {
          let offContext = this.offCanvas.getContext("2d", this.settings)
          offContext.fillStyle = 'rgb(112,112,112)'
          offContext.fillRect(0, 0, 100, 100)
          offContext.transform(1, 0.5, -0.5, 1, 10, 10)
          offContext.fillStyle = 'rgb(0,74,175)'
          offContext.fillRect(0, 0, 100, 100)
          offContext.transform(1, 0.5, -0.5, 1, 10, 10)
          offContext.fillStyle = 'rgb(39,135,217)'
          offContext.fillRect(0, 0, 100, 100)
          let image = this.offCanvas.transferToImageBitmap()
          this.context.transferFromImageBitmap(image)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170658.95847715259776047963814590667616:50001231000000:2800:B193371A8D6E15EE9EA3AFD3FE8198A6C841C0460326A56E4636C7847376ED4E.jpg)

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
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          let offContext = this.offCanvas.getContext("2d", this.settings)
          offContext.fillStyle = 'rgb(255,0,0)'
          offContext.fillRect(0, 0, 100, 100)
          offContext.setTransform(1,0.5, -0.5, 1, 10, 10)
          offContext.fillStyle = 'rgb(0,0,255)'
          offContext.fillRect(0, 0, 100, 100)
          let image = this.offCanvas.transferToImageBitmap()
          this.context.transferFromImageBitmap(image)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170658.76925061612154558480728567119190:50001231000000:2800:9ACF280C3329AD52DA4DC17BDBD4078EF9A97C0A27C2AC3DDA0AA8E080AAF802.png)

### setTransform

 支持设备PhonePC/2in1TabletTVWearable

setTransform(transform?: Matrix2D): void

以Matrix2D对象为模板重置现有的变换矩阵并创建新的变换矩阵。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 描述 |
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
   private offcontext1: OffscreenCanvasRenderingContext2D = new OffscreenCanvasRenderingContext2D(600, 200, this.settings);
   private context2: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
   private offcontext2: OffscreenCanvasRenderingContext2D = new OffscreenCanvasRenderingContext2D(600, 200, this.settings);

   build() {
     Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
       Text('context1');
       Canvas(this.context1)
         .width('230vp')
         .height('160vp')
         .backgroundColor('#ffff00')
         .onReady(() =>{
           this.offcontext1.fillRect(100, 20, 50, 50);
           this.offcontext1.setTransform(1, 0.5, -0.5, 1, 10, 10);
           this.offcontext1.fillRect(100, 20, 50, 50);
           let image = this.offcontext1.transferToImageBitmap();
           this.context1.transferFromImageBitmap(image);
         })
       Text('context2');
       Canvas(this.context2)
         .width('230vp')
         .height('160vp')
         .backgroundColor('#0ffff0')
         .onReady(() =>{
           this.offcontext2.fillRect(100, 20, 50, 50);
           let storedTransform = this.offcontext1.getTransform();
           this.offcontext2.setTransform(storedTransform);
           this.offcontext2.fillRect(100, 20, 50, 50);
           let image = this.offcontext2.transferToImageBitmap();
           this.context2.transferFromImageBitmap(image);
         })
     }
     .width('100%')
     .height('100%')
   }
 }
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170658.73498815711666925698890731230655:50001231000000:2800:906DE1F62A7083CF1C618196B25A798E912EB499D03B72660807B25578032AC2.jpeg)

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
  private offcontext1: OffscreenCanvasRenderingContext2D = new OffscreenCanvasRenderingContext2D(600, 100, this.settings);
  private context2: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private offcontext2: OffscreenCanvasRenderingContext2D = new OffscreenCanvasRenderingContext2D(600, 100, this.settings);

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Text('context1');
      Canvas(this.context1)
        .width('230vp')
        .height('120vp')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          this.offcontext1.fillRect(50, 50, 50, 50);
          this.offcontext1.setTransform(1.2, Math.PI/8, Math.PI/6, 0.5, 30, -25);
          this.offcontext1.fillRect(50, 50, 50, 50);
          let image = this.offcontext1.transferToImageBitmap();
          this.context1.transferFromImageBitmap(image);
        })
      Text('context2');
      Canvas(this.context2)
        .width('230vp')
        .height('120vp')
        .backgroundColor('#0ffff0')
        .onReady(() =>{
          this.offcontext2.fillRect(50, 50, 50, 50);
          let storedTransform = this.offcontext1.getTransform();
          console.info("Matrix [scaleX = " + storedTransform.scaleX + ", scaleY = " + storedTransform.scaleY +
          ", rotateX = " + storedTransform.rotateX + ", rotateY = " + storedTransform.rotateY +
          ", translateX = " + storedTransform.translateX + ", translateY = " + storedTransform.translateY + "]")
          this.offcontext2.setTransform(storedTransform);
          this.offcontext2.fillRect(50,50,50,50);
          let image = this.offcontext2.transferToImageBitmap();
          this.context2.transferFromImageBitmap(image);
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170658.74667818210510906775586641528473:50001231000000:2800:517FD2E306D409BE01F0A4135195341C4C22891A431800CC895C32250F1DFF9C.png)

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
| y | number | 是 | 设置垂直平移量。 API version 18之前，设置NaN或Infinity时，在该方法后执行的绘制方法无法绘制；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的绘制方法正常绘制。 默认单位：vp |

**示例：**

```
// xxx.ets
@Entry
@Component
struct Translate {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          let offContext = this.offCanvas.getContext("2d", this.settings)
          offContext.fillRect(10, 10, 50, 50)
          offContext.translate(70, 70)
          offContext.fillRect(10, 10, 50, 50)
          let image = this.offCanvas.transferToImageBitmap()
          this.context.transferFromImageBitmap(image)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170658.73414198841053655466597738116156:50001231000000:2800:CF8D9423DD5469674C454925C62E3C3B3704CF5A897B28318B33C23AD685F3E5.png)

### drawImage

 支持设备PhonePC/2in1TabletTVWearable

drawImage(image: ImageBitmap | PixelMap, dx: number, dy: number): void

进行图像绘制。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用，卡片中不支持PixelMap对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| image | ImageBitmap \| PixelMap | 是 | 图片资源，请参考ImageBitmap或PixelMap。 异常值undefined或null按无效值处理，不进行绘制。 |
| dx | number | 是 | 绘制区域左上角在x轴的位置。 异常值undefined或null按0处理，NaN和Infinity按无效值处理，不进行绘制。 默认单位：vp |
| dy | number | 是 | 绘制区域左上角在y轴的位置。 异常值undefined或null按0处理，NaN和Infinity按无效值处理，不进行绘制。 默认单位：vp |

**示例：**

```
// xxx.ets
@Entry
@Component
struct DrawImage {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  // "common/images/example.jpg"需要替换为开发者所需的图像资源文件
  private img: ImageBitmap = new ImageBitmap("common/images/example.jpg");
  private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#D5D5D5')
        .onReady(() => {
          let offContext = this.offCanvas.getContext("2d", this.settings)
          offContext.drawImage(this.img, 0, 0)
          let image = this.offCanvas.transferToImageBitmap()
          this.context.transferFromImageBitmap(image)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170658.10793877056106510004289320378402:50001231000000:2800:70C1D59B010259DA301EB68C02D9858993FF6098EA8BE5BE05E7AD3E8ACE96BF.png)

### drawImage

 支持设备PhonePC/2in1TabletTVWearable

drawImage(image: ImageBitmap | PixelMap, dx: number, dy: number, dw: number, dh: number): void

将图像拉伸或压缩绘制。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用，卡片中不支持PixelMap对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| image | ImageBitmap \| PixelMap | 是 | 图片资源，请参考ImageBitmap或PixelMap。 异常值undefined或null按无效值处理，不进行绘制。 |
| dx | number | 是 | 绘制区域左上角在x轴的位置。 异常值undefined或null按0处理，NaN和Infinity按无效值处理，不进行绘制。 默认单位：vp |
| dy | number | 是 | 绘制区域左上角在y轴的位置。 异常值undefined或null按0处理，NaN和Infinity按无效值处理，不进行绘制。 默认单位：vp |
| dw | number | 是 | 绘制区域的宽度。 负数、异常值undefined或null按0处理，NaN和Infinity按无效值处理，不进行绘制。 默认单位：vp |
| dh | number | 是 | 绘制区域的高度。 负数、异常值undefined或null按0处理，NaN和Infinity按无效值处理，不进行绘制。 默认单位：vp |

**示例：**

```
// xxx.ets
@Entry
@Component
struct DrawImage {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  // "common/images/example.jpg"需要替换为开发者所需的图像资源文件
  private img: ImageBitmap = new ImageBitmap("common/images/example.jpg");
  private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#D5D5D5')
        .onReady(() => {
          let offContext = this.offCanvas.getContext("2d", this.settings)
          offContext.drawImage(this.img, 0, 0, 300, 300)
          let image = this.offCanvas.transferToImageBitmap()
          this.context.transferFromImageBitmap(image)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170658.99290050608274382576417996726795:50001231000000:2800:C774E6E538ED0F18E59169D7F5A21E41AF740C431A9EBBAA82BE309BFAA58FE8.png)

### drawImage

 支持设备PhonePC/2in1TabletTVWearable

drawImage(image: ImageBitmap | PixelMap, sx: number, sy: number, sw: number, sh: number, dx: number, dy: number, dw: number, dh: number): void

将图像裁剪后拉伸或压缩绘制。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用，卡片中不支持PixelMap对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| image | ImageBitmap \| PixelMap | 是 | 图片资源，请参考ImageBitmap或PixelMap。 异常值undefined或null按无效值处理，不进行绘制。 |
| sx | number | 是 | 裁切源图像时距离源图像左上角的x坐标值。 异常值undefined或null按0处理，NaN和Infinity按无效值处理，不进行绘制。 image类型为ImageBitmap时，默认单位：vp image类型为PixelMap时，API version 18前，默认单位：px；API version 18及以后，默认单位：vp |
| sy | number | 是 | 裁切源图像时距离源图像左上角的y坐标值。 异常值undefined或null按0处理，NaN和Infinity按无效值处理，不进行绘制。 image类型为ImageBitmap时，默认单位：vp image类型为PixelMap时，API version 18前，默认单位：px；API version 18及以后，默认单位：vp |
| sw | number | 是 | 裁切源图像时需要裁切的宽度。 负数、异常值undefined或null按0处理，NaN和Infinity按无效值处理，不进行绘制。 image类型为ImageBitmap时，默认单位：vp image类型为PixelMap时，API version 18前，默认单位：px；API version 18及以后，默认单位：vp |
| sh | number | 是 | 裁切源图像时需要裁切的高度。 负数、异常值undefined或null按0处理，NaN和Infinity按无效值处理，不进行绘制。 image类型为ImageBitmap时，默认单位：vp image类型为PixelMap时，API version 18前，默认单位：px；API version 18及以后，默认单位：vp |
| dx | number | 是 | 绘制区域左上角在x轴的位置。 异常值undefined或null按0处理，NaN和Infinity按无效值处理，不进行绘制。 默认单位：vp |
| dy | number | 是 | 绘制区域左上角在y轴的位置。 异常值undefined或null按0处理，NaN和Infinity按无效值处理，不进行绘制。 默认单位：vp |
| dw | number | 是 | 绘制区域的宽度。 负数、异常值undefined或null按0处理，NaN和Infinity按无效值处理，不进行绘制。 默认单位：vp |
| dh | number | 是 | 绘制区域的高度。 负数、异常值undefined或null按0处理，NaN和Infinity按无效值处理，不进行绘制。 默认单位：vp |

**示例：**

```
// xxx.ets
@Entry
@Component
struct DrawImage {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  // "common/images/example.jpg"需要替换为开发者所需的图像资源文件
  private img: ImageBitmap = new ImageBitmap("common/images/example.jpg");
  private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#D5D5D5')
        .onReady(() => {
          let offContext = this.offCanvas.getContext("2d", this.settings)
          offContext.drawImage(this.img, 0, 0, 500, 500, 0, 0, 400, 300)
          let image = this.offCanvas.transferToImageBitmap()
          this.context.transferFromImageBitmap(image)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170658.05326842423472479949525678218645:50001231000000:2800:D9C5876BCFB60E304A446A5505319F48B1E25D3BE712073D9CF861015EEE81A7.png)

### createImageData

 支持设备PhonePC/2in1TabletTVWearable

createImageData(sw: number, sh: number): ImageData

根据当前ImageData对象重新创建一个宽、高相同的ImageData对象，请参考[ImageData](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-components-canvas-imagedata)，该接口存在内存拷贝行为，高耗时，应避免频繁使用。createImageData示例同putImageData。

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

createImageData(imageData: ImageData): ImageData

根据已创建的ImageData对象创建新的ImageData对象（不会复制图像数据），请参考[ImageData](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-components-canvas-imagedata)，该接口存在内存拷贝行为，高耗时，应避免频繁使用。createImageData示例同putImageData。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| imageData | ImageData | 是 | 被复制的ImageData对象。 异常值undefined和null按width和height为0的ImageData处理。 |

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

| 参数 | 类型 | 必填 | 说明 |
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
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  // "common/images/example.jpg"需要替换为开发者所需的图像资源文件
  private img: ImageBitmap = new ImageBitmap("common/images/example.jpg");
  private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() => {
          let offContext = this.offCanvas.getContext("2d", this.settings)
          offContext.drawImage(this.img, 100, 100, 130, 130)
          let pixelmap = offContext.getPixelMap(150, 150, 130, 130)
          offContext.setPixelMap(pixelmap)
          let image = this.offCanvas.transferToImageBitmap()
          this.context.transferFromImageBitmap(image)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170658.34387784391201175041122543751550:50001231000000:2800:3FC32B02C73DC1799D2699AA94EF58C01A330BC3AB1FD52B4EB4681ECAD5F536.png)

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
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);
  // "/common/images/1234.png"需要替换为开发者所需的图像资源文件
  private img:ImageBitmap = new ImageBitmap("/common/images/1234.png");

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          let offContext = this.offCanvas.getContext("2d", this.settings)
          offContext.drawImage(this.img,0,0,130,130)
          let imageData = offContext.getImageData(50,50,130,130)
          offContext.putImageData(imageData,150,150)
          let image = this.offCanvas.transferToImageBitmap()
          this.context.transferFromImageBitmap(image)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170658.64927599137708029079493558803928:50001231000000:2800:31F44A04288E75912BDD5F4EE87CBCDF451F858AB96EE4A99ABF540395D8650B.png)

### putImageData

 支持设备PhonePC/2in1TabletTVWearable

putImageData(imageData: ImageData, dx: number | string, dy: number | string): void

使用[ImageData](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-components-canvas-imagedata)数据填充新的矩形区域。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 描述 |
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
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('rgb(213,213,213)')
        .onReady(() => {
          let offContext = this.offCanvas.getContext("2d", this.settings)
          let imageDataNum = offContext.createImageData(100, 100)
          let imageData = offContext.createImageData(imageDataNum)
          for (let i = 0; i < imageData.data.length; i += 4) {
            imageData.data[i + 0] = 112
            imageData.data[i + 1] = 112
            imageData.data[i + 2] = 112
            imageData.data[i + 3] = 255
          }
          offContext.putImageData(imageData, 10, 10)
          let image = this.offCanvas.transferToImageBitmap()
          this.context.transferFromImageBitmap(image)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170658.59035196695105285717973352174885:50001231000000:2800:BC0C4677CBF9C30BEF109172EFD63ABEB017D1868F0CCD4FC252EF27E78AE96D.png)

### putImageData

 支持设备PhonePC/2in1TabletTVWearable

putImageData(imageData: ImageData, dx: number | string, dy: number | string, dirtyX: number | string, dirtyY: number | string, dirtyWidth?: number | string, dirtyHeight: number | string): void

使用[ImageData](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-components-canvas-imagedata)数据裁剪后填充至新的矩形区域。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 描述 |
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
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('rgb(213,213,213)')
        .onReady(() => {
          let offContext = this.offCanvas.getContext("2d", this.settings)
          let imageDataNum = offContext.createImageData(100, 100)
          let imageData = offContext.createImageData(imageDataNum)
          for (let i = 0; i < imageData.data.length; i += 4) {
            imageData.data[i + 0] = 112
            imageData.data[i + 1] = 112
            imageData.data[i + 2] = 112
            imageData.data[i + 3] = 255
          }
          offContext.putImageData(imageData, 10, 10, 0, 0, 100, 50)
          let image = this.offCanvas.transferToImageBitmap()
          this.context.transferFromImageBitmap(image)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170658.30605684016150174637841255102135:50001231000000:2800:E9D0922632B4A0A42181720D57B4372988436EEFA0C8A9D3064E59E74CD6F481.png)

### setLineDash

setLineDash(segments: number[]): void

设置画布的虚线样式。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

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
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#D5D5D5')
        .onReady(() => {
          let offContext = this.offCanvas.getContext("2d", this.settings)
          offContext.arc(100, 75, 50, 0, 6.28)
          offContext.setLineDash([10, 20])
          offContext.stroke()
          let image = this.offCanvas.transferToImageBitmap()
          this.context.transferFromImageBitmap(image)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170658.72765020028596304163118301830088:50001231000000:2800:5AC3F4B31D748574B08B3AA248E6CB335555498A9BB24CC4A6B391ABD6579C96.png)

### getLineDash

getLineDash(): number[]

获得当前画布的虚线样式。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**返回值：**

  展开

| 类型 | 说明 |
| --- | --- |
| number[] | 返回数组，该数组用来描述线段如何交替和间距长度。 异常值undefined或null按无效值处理。 默认单位：vp |

**示例：**

```
// xxx.ets
@Entry
@Component
struct OffscreenCanvasGetLineDash {
  @State message: string = 'Hello World';
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

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
            let offContext = this.offCanvas.getContext("2d", this.settings)
            offContext.arc(100, 75, 50, 0, 6.28)
            offContext.setLineDash([10, 20])
            offContext.stroke()
            let res = offContext.getLineDash()
            this.message = JSON.stringify(res)
            let image = this.offCanvas.transferToImageBitmap()
            this.context.transferFromImageBitmap(image)
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170658.13522738320458461086769470414296:50001231000000:2800:D43B1481AD47946C26D52F93BC26C21A3802A37A9ADBA15F90E703C71FD4ADB9.png)

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
struct ToDataURL {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private offCanvas: OffscreenCanvas = new OffscreenCanvas(100, 100);
  @State dataURL: string = "";

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width(100)
        .height(100)
        .onReady(() => {
          let offContext = this.offCanvas.getContext("2d", this.settings)
          offContext.fillRect(0,0,100,100)
          this.dataURL = offContext.toDataURL()
        })
      Text(this.dataURL)
    }
    .width('100%')
    .height('100%')
    .backgroundColor('#ffff00')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170658.75404504123465948767056545647171:50001231000000:2800:7D10A4C5D180F0179A18453F03CA460175784454AF160372702874C6CA01CD9C.png)

### transferToImageBitmap

 支持设备PhonePC/2in1TabletTVWearable

transferToImageBitmap(): ImageBitmap

在离屏画布最近渲染的图像上创建一个ImageBitmap对象。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

  展开

| 类型 | 说明 |
| --- | --- |
| ImageBitmap | 存储离屏画布上渲染的像素数据。 |

**示例：**

```
// xxx.ets
@Entry
@Component
struct PutImageData {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('rgb(213,213,213)')
        .onReady(() => {
          let offContext = this.offCanvas.getContext("2d", this.settings)
          let imageData = offContext.createImageData(100, 100)
          for (let i = 0; i < imageData.data.length; i += 4) {
            imageData.data[i + 0] = 112
            imageData.data[i + 1] = 112
            imageData.data[i + 2] = 112
            imageData.data[i + 3] = 255
          }
          offContext.putImageData(imageData, 10, 10)
          let image = this.offCanvas.transferToImageBitmap()
          this.context.transferFromImageBitmap(image)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170658.86975179236602433106928027358560:50001231000000:2800:BF676BC0D71AA354BA8C0ABBA0CF8CF30616E87C6DF2BF975C7D863364FB8338.png)

### restore

 支持设备PhonePC/2in1TabletTVWearable

restore(): void

对保存的绘图上下文进行恢复。

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
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          let offContext = this.offCanvas.getContext("2d", this.settings)
          offContext.save() // save the default state
          offContext.fillStyle = "#00ff00"
          offContext.fillRect(20, 20, 100, 100)
          offContext.restore() // restore to the default state
          offContext.fillRect(150, 75, 100, 100)
          let image = this.offCanvas.transferToImageBitmap()
          this.context.transferFromImageBitmap(image)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170659.44286897785083496028714572394480:50001231000000:2800:482C1A1F8DD079DBC194F17D8872A295EAA6332A1CB464C58F21559067E7C88C.png)

### save

 支持设备PhonePC/2in1TabletTVWearable

save(): void

对当前的绘图上下文进行保存。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```
// xxx.ets
@Entry
@Component
struct CanvasExample {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() =>{
          let offContext = this.offCanvas.getContext("2d", this.settings)
          offContext.save() // save the default state
          offContext.fillStyle = "#00ff00"
          offContext.fillRect(20, 20, 100, 100)
          offContext.restore() // restore to the default state
          offContext.fillRect(150, 75, 100, 100)
          let image = this.offCanvas.transferToImageBitmap()
          this.context.transferFromImageBitmap(image)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170659.31873547328432128685689272035283:50001231000000:2800:47E0DA0C700AE6AD5BEB4D636F74176F0C80817A5D1E8850EFFBA39645B154E7.png)

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
| CanvasGradient | 新的CanvasGradient对象，用于在offscreenCanvas上创建渐变效果。 |

**示例：**

```
// xxx.ets
@Entry
@Component
struct CreateLinearGradient {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('rgb(213,213,213)')
        .onReady(() =>{
          let offContext = this.offCanvas.getContext("2d", this.settings)
          let grad = offContext.createLinearGradient(50,0, 300,100)
          grad.addColorStop(0.0, 'rgb(39,135,217)')
          grad.addColorStop(0.5, 'rgb(255,238,240)')
          grad.addColorStop(1.0, 'rgb(23,169,141)')
          offContext.fillStyle = grad
          offContext.fillRect(0, 0, 400, 400)
          let image = this.offCanvas.transferToImageBitmap()
          this.context.transferFromImageBitmap(image)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170659.02289871379400279978365800099628:50001231000000:2800:D539AF9111DCC50583677C1586ABCCC99DA491544647626303880D4C0DA4CD91.png)

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
| CanvasGradient | 新的CanvasGradient对象，用于在offscreenCanvas上创建渐变效果。 |

**示例：**

```
// xxx.ets
@Entry
@Component
struct CreateRadialGradient {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('rgb(213,213,213)')
        .onReady(() =>{
          let offContext = this.offCanvas.getContext("2d", this.settings)
          let grad = offContext.createRadialGradient(200,200,50, 200,200,200)
          grad.addColorStop(0.0, 'rgb(39,135,217)')
          grad.addColorStop(0.5, 'rgb(255,238,240)')
          grad.addColorStop(1.0, 'rgb(112,112,112)')
          offContext.fillStyle = grad
          offContext.fillRect(0, 0, 440, 440)
          let image = this.offCanvas.transferToImageBitmap()
          this.context.transferFromImageBitmap(image)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170659.54273585872063484615814191289382:50001231000000:2800:187B612688CEC20FE62FFEF40355486726902A122F5959F7A4C85BB67E404F8D.png)

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
| CanvasGradient | 新的CanvasGradient对象，用于在offscreenCanvas上创建渐变效果。 |

**示例：**

```
// xxx.ets
@Entry
@Component
struct OffscreenCanvasConicGradientPage {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffffff')
        .onReady(() =>{
          let offContext = this.offCanvas.getContext("2d", this.settings)
          let grad = offContext.createConicGradient(0, 50, 80)
          grad.addColorStop(0.0, '#ff0000')
          grad.addColorStop(0.5, '#ffffff')
          grad.addColorStop(1.0, '#00ff00')
          offContext.fillStyle = grad
          offContext.fillRect(0, 30, 100, 100)
          let image = this.offCanvas.transferToImageBitmap()
          this.context.transferFromImageBitmap(image)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170659.42888499400514594430387905958686:50001231000000:2800:A5FC2E881B4E97B73834E0FC6ED2226C9979BC0AC78FAA37A249B54768F17F16.png)