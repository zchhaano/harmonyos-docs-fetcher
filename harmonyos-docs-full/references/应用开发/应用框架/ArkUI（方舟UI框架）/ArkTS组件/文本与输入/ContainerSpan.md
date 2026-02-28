# ContainerSpan

[Text](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text)组件的子组件，用于统一管理多个[Span](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-span)、[ImageSpan](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-imagespan)的背景色及圆角弧度。

 说明 

该组件从API version 11开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## 子组件

支持设备PhonePC/2in1TabletTVWearable

可以包含[Span](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-span)、[ImageSpan](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-imagespan) 子组件。

## 接口

支持设备PhonePC/2in1TabletTVWearable

ContainerSpan()

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 属性

支持设备PhonePC/2in1TabletTVWearable

仅支持以下属性：

### textBackgroundStyle

支持设备PhonePC/2in1TabletTVWearable

textBackgroundStyle(style: TextBackgroundStyle)

设置文本背景样式。子组件在不设置该属性时，将继承此属性值。

 说明 

从API version 12开始，该接口支持在[attributeModifier](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-attribute-modifier#attributemodifier)中调用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

 展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| style | TextBackgroundStyle | 是 | 文本背景样式。 默认值： { color: Color.Transparent, radius: 0 } |

### attributeModifier 12+

支持设备PhonePC/2in1TabletTVWearable

attributeModifier(modifier: AttributeModifier<ContainerSpanAttribute>)

设置组件的动态属性。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

 展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| modifier | AttributeModifier <ContainerSpanAttribute> | 是 | 动态设置组件的属性。 |

## 事件

支持设备PhonePC/2in1TabletTVWearable

不支持[通用事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-component-general-events)。

## 示例

支持设备PhonePC/2in1TabletTVWearable 

### 示例1（设置背景样式）

从API version 11开始，该示例通过[textBackgroundStyle](/consumer/cn/doc/harmonyos-references/ts-basic-components-containerspan#textbackgroundstyle)属性展示了文本设置背景样式的效果。

```
// xxx.ets
@Component
@Entry
struct Index {
  build() {
    Column() {
      Text() {
        ContainerSpan() {
          // $r('app.media.app_icon')需要替换为开发者所需的图像资源文件。
          ImageSpan($r('app.media.app_icon'))
            .width('40vp')
            .height('40vp')
            .verticalAlign(ImageSpanAlignment.CENTER)
          Span('   Hello World !   ').fontSize('16fp').fontColor(Color.White)
        }
        .textBackgroundStyle({
          color: "#7F007DFF",
          radius: {
            topLeft: 12,
            topRight: 12,
            bottomLeft: 12,
            bottomRight: 12
          }
        })
      }
    }.width('100%').alignItems(HorizontalAlign.Center)
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170639.42046525127444570598695964481743:50001231000000:2800:BE049BDA5CD12AE6696C67F9547F82C1731FEEA68B67DA813E304ACBA0DCB438.png)

### 示例2（通过attributeModifier设置背景样式）

从API version 12开始，该示例通过[attributeModifier](/consumer/cn/doc/harmonyos-references/ts-basic-components-containerspan#attributemodifier12)属性展示了文本设置背景样式的效果。

```
import { ContainerSpanModifier } from '@kit.ArkUI';

class MyContainerSpanModifier extends ContainerSpanModifier {
  applyNormalAttribute(instance: ContainerSpanAttribute): void {
    super.applyNormalAttribute?.(instance);
    this.textBackgroundStyle({ color: "#7F007DFF", radius: "12vp" });
  }
}

@Entry
@Component
struct ContainerSpanModifierExample {
  @State containerSpanModifier: ContainerSpanModifier = new MyContainerSpanModifier();

  build() {
    Column() {
      Text() {
        ContainerSpan() {
          // $r('app.media.startIcon')需要替换为开发者所需的图像资源文件。
          ImageSpan($r('app.media.startIcon'))
            .width('40vp')
            .height('40vp')
            .verticalAlign(ImageSpanAlignment.CENTER)
          Span(' I\'m ContainerSpan attributeModifier ').fontSize('16fp').fontColor(Color.White)
        }.attributeModifier(this.containerSpanModifier as MyContainerSpanModifier)
      }
    }.width('100%').alignItems(HorizontalAlign.Center)
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170639.65865495494994268085429415277744:50001231000000:2800:BF407D295FD275D97109F6AA4E4C11F7A476FDFEB53C36CC3F13DC289C377AD0.png)