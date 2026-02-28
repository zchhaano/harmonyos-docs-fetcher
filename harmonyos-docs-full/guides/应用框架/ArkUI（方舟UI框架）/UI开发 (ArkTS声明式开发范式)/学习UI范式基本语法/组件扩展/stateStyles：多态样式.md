# stateStyles：多态样式

@Styles仅应用于静态页面的样式复用，stateStyles可以依据组件的内部状态的不同，快速设置不同样式。这就是我们本章要介绍的内容stateStyles（又称为：多态样式）。

 说明 

多态样式仅支持通用属性。如果多态样式不生效，则该属性可能为组件的私有属性，例如：[fontColor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-button#fontcolor)、[TextInput](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput)组件的[backgroundColor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-background)等。此时，可以通过[attributeModifier](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-attribute-modifier#attributemodifier)动态设置组件属性来解决此问题。

## 概述

stateStyles是属性方法，可以根据UI内部状态来设置样式，类似于css伪类，但语法不同。ArkUI提供以下六种状态：

- focused：获焦态。
- normal：正常态。
- pressed：按压态。
- disabled：不可用态。
- clicked：点击态。
- selected10+：选中态。

 说明 

获焦态目前仅支持通过外接键盘的Tab键或方向键触发，不支持在嵌套滚动组件场景下通过按键触发。

## 使用场景

### 基础场景

下面的示例展示了stateStyles最基本的使用场景。Button1处于第一个组件，Button2处于第二个组件。按压时显示为pressed态指定的黑色。使用Tab键走焦，Button1获焦并显示为focused态指定的粉色。当Button2获焦的时候，Button2显示为focused态指定的粉色，Button1失焦显示normal态指定的蓝色。

 收起自动换行深色代码主题复制

```
@Entry @Component struct StateStylesSample { build ( ) { Column () { Button ( 'Button1' ) . stateStyles ({ focused : { . backgroundColor ( '#ffffeef0' ) }, pressed : { . backgroundColor ( '#ff707070' ) }, normal : { . backgroundColor ( '#ff2787d9' ) } }) . margin ( 20 ) Button ( 'Button2' ) . stateStyles ({ focused : { . backgroundColor ( '#ffffeef0' ) }, pressed : { . backgroundColor ( '#ff707070' ) }, normal : { . backgroundColor ( '#ff2787d9' ) } }) }. margin ( '30%' ) } }
```

[StateStylesSample.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/StateStyle/entry/src/main/ets/pages/StateStyle/StateStylesSample.ets#L16-L50) 

**图1** 获焦态和按压态

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165957.15633968893946325201896544771627:50001231000000:2800:C24F16CAAC0A1DF18935B6B6C5184725C72595BA2E8739B53005E1C3774132F7.gif)

### @Styles和stateStyles联合使用

以下示例通过@Styles指定stateStyles的不同状态。

 收起自动换行深色代码主题复制

```
@Entry @Component struct MyComponent { @Styles normalStyle ( ) { . backgroundColor ( Color . Gray ) } @Styles pressedStyle ( ) { . backgroundColor ( Color . Red ) } build ( ) { Column () { Text ( 'Text1' ) . fontSize ( 50 ) . fontColor ( Color . White ) . stateStyles ({ normal : this . normalStyle , pressed : this . pressedStyle , }) } } }
```

[MyComponent.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/StateStyle/entry/src/main/ets/pages/NormalStyle/MyComponent.ets#L16-L39) 

**图2** 正常态和按压态

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165957.33505881228929917369254905536860:50001231000000:2800:BD0DB53605C61DA538CD18F8085BC529D817EE99D35668E805B81930A25DBC0D.gif)

### 在stateStyles里使用常规变量和状态变量

stateStyles可以通过this绑定组件内的常规变量和状态变量。

 收起自动换行深色代码主题复制

```
@Entry @Component struct CompWithInlineStateStyles { @State focusedColor : Color = 0xD5D5D5 ; normalColor : Color = 0x004AAF ; build ( ) { Column () { Button ( 'clickMe' ) . height ( 100 ) . width ( 100 ) . stateStyles ({ normal : { . backgroundColor ( this . normalColor ) }, focused : { . backgroundColor ( this . focusedColor ) } }) . onClick ( () => { this . focusedColor = 0x707070 ; }) . margin ( '30%' ) } } }
```

[CompWithInlineStateStyles.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/StateStyle/entry/src/main/ets/pages/FocusStyle/CompWithInlineStateStyles.ets#L15-L42) 

Button默认normal态显示蓝色，第一次按下Tab键让Button获焦显示为focus态的浅灰色，点击事件触发后，再次按下Tab键让Button获焦，focus态变为深灰色。

**图3** 点击改变获焦态样式

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165957.70628786749549095556190351642912:50001231000000:2800:F9C9DE60FDF2E810F342D5C453A0606AFD2FDBC1D7A785EC544F59A457AA0834.gif)