# Canvas

提供画布组件，用于自定义绘制图形。

 说明 

 该组件从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## 子组件

支持设备PhonePC/2in1TabletTVWearable

不支持。

## 接口

支持设备PhonePC/2in1TabletTVWearable 

### Canvas

支持设备PhonePC/2in1TabletTVWearable

Canvas(context?: CanvasRenderingContext2D | DrawingRenderingContext)

创建Canvas组件时，最大面积不超过10000px*10000px，超过最大面积则无法正常创建。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

 展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | CanvasRenderingContext2D \| DrawingRenderingContext 12+ | 否 | CanvasRenderingContext2D: 不支持多个Canvas共用一个CanvasRenderingContext2D对象，具体描述见 CanvasRenderingContext2D 对象。DrawingRenderingContext: 不支持多个Canvas共用一个DrawingRenderingContext对象，具体描述见 DrawingRenderingContext 对象。 异常值null按无效值处理。 |

### Canvas 12+

支持设备PhonePC/2in1TabletTVWearable

Canvas(context: CanvasRenderingContext2D | DrawingRenderingContext, imageAIOptions: ImageAIOptions)

创建Canvas组件，支持设置CanvasRenderingContext2D对象或DrawingRenderingContext对象，支持设置AI分析选项。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

 展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | CanvasRenderingContext2D \| DrawingRenderingContext 12+ | 是 | CanvasRenderingContext2D: 不支持多个Canvas共用一个CanvasRenderingContext2D对象，具体描述见 CanvasRenderingContext2D 对象。DrawingRenderingContext: 不支持多个Canvas共用一个DrawingRenderingContext对象，具体描述见 DrawingRenderingContext 对象。 异常值null按无效值处理。 |
| imageAIOptions | ImageAIOptions | 是 | 给组件设置一个AI分析选项，通过此项可配置分析类型或绑定一个分析控制器。 异常值null和undefined按 ImageAIOptions 的默认值处理，默认取值为{ type: [ImageAnalyzerType.SUBJECT, ImageAnalyzerType.TEXT], aiController: new ImageAnalyzerController() }，即开启主体识别和文字识别功能。 |

## 属性

支持设备PhonePC/2in1TabletTVWearable

除支持[通用属性](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-component-general-attributes)外，还支持以下属性：

### enableAnalyzer 12+

支持设备PhonePC/2in1TabletTVWearable

设置组件支持AI分析，当前支持主体识别、文字识别和对象查找等功能，支持[attributeModifier](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-attribute-modifier#attributemodifier)动态设置属性方法。

需要搭配[CanvasRenderingContext2D](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-canvasrenderingcontext2d)中的[StartImageAnalyzer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-canvasrenderingcontext2d#startimageanalyzer12)和[StopImageAnalyzer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-canvasrenderingcontext2d#stopimageanalyzer12)一起使用。

不能和[overlay](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-overlay#overlay)属性同时使用，两者同时设置时overlay中CustomBuilder属性将失效。该特性依赖设备能力。

 说明 

从API version 20开始，该接口支持在[attributeModifier](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-attribute-modifier#attributemodifier)中调用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

 展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | boolean | 是 | 组件支持AI分析，需要组件内容支持主体识别、文字识别或对象查找。 设置为true时，组件可进行AI分析，设置为false时，组件不可进行AI分析。 异常值null和undefined按默认值处理。 默认值：false |

## 事件

支持设备PhonePC/2in1TabletTVWearable

除支持[通用事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-component-general-events)外，还支持如下事件：

### onReady

支持设备PhonePC/2in1TabletTVWearable

onReady(event: VoidCallback)

Canvas组件初始化完成或者发生大小变化时的事件回调，支持[attributeModifier](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-attribute-modifier#attributemodifier)动态设置属性方法。

当该事件被触发时画布被清空，该事件之后Canvas组件宽高确定且可获取，可使用Canvas相关API进行绘制。当Canvas组件仅发生位置变化时，只触发[onAreaChange](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-component-area-change-event#onareachange)事件，不触发onReady事件。[onAreaChange](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-component-area-change-event#onareachange)事件在onReady事件后触发。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

 展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | VoidCallback | 是 | Canvas组件初始化完成或者发生大小变化时的事件回调事件。 |

## 示例

支持设备PhonePC/2in1TabletTVWearable 

### 示例1（使用CanvasRenderingContext2D中的方法）

该示例实现了如何在Canvas组件使用[CanvasRenderingContext2D](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-canvasrenderingcontext2d)中的方法进行绘制。

```
// xxx.ets
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
        .backgroundColor('#ffff00')
        .onReady(() => {
          this.context.fillRect(0, 30, 100, 100)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

 ![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170435.61001557808350211876367262439400:50001231000000:2800:B5B31A53D7FDEBBBE6FE4377A53CA952702F781CAC3AF05A02A98D45BF1A04AA.png)

### 示例2（使用DrawingRenderingContext中的方法）

该示例实现了如何在Canvas组件使用[DrawingRenderingContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-drawingrenderingcontext)中的方法进行绘制。

```
// xxx.ets
@Entry
@Component
struct CanvasExample {
  private context: DrawingRenderingContext = new DrawingRenderingContext();

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('rgb(213,213,213)')
        .onReady(() => {
          this.context.canvas.drawCircle(200, 200, 100)
          this.context.invalidate()
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

 ![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170435.33549140146018719489533061582873:50001231000000:2800:6859A72B4FF1FBA14BB1EE447676DA7B9001F1100674C0EFFB53015EE98E0111.png)

### 示例3（使用attributeModifier动态设置Canvas组件的属性及方法）

该示例展示了如何使用[attributeModifier](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-attribute-modifier#attributemodifier)动态设置Canvas组件的[enableAnalyzer](/consumer/cn/doc/harmonyos-references/ts-components-canvas-canvas#enableanalyzer12)属性和[onReady](/consumer/cn/doc/harmonyos-references/ts-components-canvas-canvas#onready)方法。

```
// xxx.ets
import { BusinessError } from '@kit.BasicServicesKit';

class MyCanvasModifier implements AttributeModifier<CanvasAttribute> {
  context: CanvasRenderingContext2D = new CanvasRenderingContext2D()

  applyNormalAttribute(instance: CanvasAttribute): void {
    // 从（0，0）绘制一张宽高为200vp的图片
    instance.onReady(() => {
      // "resources/base/media/img.png"需要替换为开发者所需的图像资源文件
      let image = new ImageBitmap("resources/base/media/img.png")
      this.context.drawImage(image, 0, 0, 200, 200)
    })
    // 设置开启组件AI分析功能，点击start后，长按触发AI识别功能
    instance.enableAnalyzer(true)
  }
}

@Entry
@Component
struct attributeDemo {
  @State modifier: MyCanvasModifier = new MyCanvasModifier()
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)
  private config: ImageAnalyzerConfig = {
    types: [ImageAnalyzerType.SUBJECT, ImageAnalyzerType.TEXT]
  }
  private aiController: ImageAnalyzerController = new ImageAnalyzerController()
  private options: ImageAIOptions = {
    types: [ImageAnalyzerType.SUBJECT, ImageAnalyzerType.TEXT],
    aiController: this.aiController
  }

  build() {
    Row() {
      Column() {
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
          .borderWidth(1)
          .height(200)
          .width(200)
          .attributeModifier(this.modifier)
          .onAppear(() => {
            this.modifier.context = this.context
          })
      }
    }
  }
}
```

 ![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170435.28478962810882801175137368415356:50001231000000:2800:857DAB7909B7396DDA11A3637761E22A0C28F6D1FB6EB0BA3B7A40EDDA99B74D.png)