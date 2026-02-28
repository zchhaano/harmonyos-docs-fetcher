# 动态SymbolGlyphModifier属性设置

SymbolGlyphModifier用于动态设置SymbolGlyph组件的属性和样式，支持使用if/else语句进行设置。[SymbolGlyph](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolglyph)是一个用于展示图标符号的组件。

 说明 

 从API version 12开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## SymbolGlyphModifier

支持设备PhonePC/2in1TabletTVWearable

定义SymbolGlyphModifier。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### constructor

支持设备PhonePC/2in1TabletTVWearable

constructor(src?: Resource)

SymbolGlyphModifier的构造函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

 展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src | Resource | 否 | 资源信息。 |

### applyNormalAttribute

支持设备PhonePC/2in1TabletTVWearable

applyNormalAttribute?(instance: SymbolGlyphAttribute): void

组件普通状态时的样式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

 展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| instance | SymbolGlyphAttribute | 是 | 动态设置SymbolGlyph组件的属性。 |

## 示例

支持设备PhonePC/2in1TabletTVWearable

该示例通过[SymbolGlyphModifier](/consumer/cn/doc/harmonyos-references/universal-attributes-attribute-symbolglyphmodifier#symbolglyphmodifier)和TextInput组件的[cancelButton](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#cancelbutton18)属性展示了自定义右侧symbol类型清除按钮样式的效果。

```
import { SymbolGlyphModifier } from '@kit.ArkUI';

// xxx.ets
@Entry
@Component
struct Index {
  @State text: string = '';
  symbolModifier: SymbolGlyphModifier =
    new SymbolGlyphModifier($r('sys.symbol.trash')).fontColor([Color.Red]).fontSize(16).fontWeight(FontWeight.Regular);

  build() {
    Column() {
      TextInput({ text: this.text, placeholder: 'input your word...' })
        .height(50)
        .cancelButton({
          style: CancelButtonStyle.CONSTANT,
          icon: this.symbolModifier // 从API version 18开始支持symbol类型
        })
    }.margin(10)
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170902.89862590551380392327317941022712:50001231000000:2800:1D70BBF1A6029BB2E52B4D69E9938B89F3C54561957D7DD73B574744D5989D9A.png)