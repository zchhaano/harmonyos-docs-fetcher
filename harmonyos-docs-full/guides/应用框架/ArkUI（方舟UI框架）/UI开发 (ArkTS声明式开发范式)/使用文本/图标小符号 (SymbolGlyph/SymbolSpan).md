# 图标小符号 (SymbolGlyph/SymbolSpan)

SymbolGlyph是图标小符号组件，便于使用精美的图标，如渲染多色图标和使用动效图标。SymbolSpan作为Text组件的子组件，可在文本中穿插显示图标小符号。具体用法请参考[SymbolGlyph](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolglyph)和[SymbolSpan](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolspan)组件的文档。

## 创建图标

SymbolGlyph通过$r引用Resource资源来创建，目前仅支持系统预置的Symbol资源名。

相关资源可参考[系统图标](https://developer.huawei.com/consumer/cn/doc/design-guides/system-icons-0000001929854962)。

 收起自动换行深色代码主题复制

```
SymbolGlyph ($r( 'sys.symbol.ohos_folder_badge_plus' )) . fontSize ( 96 ) . renderingStrategy ( SymbolRenderingStrategy . SINGLE ) . fontColor ([ Color . Black , Color . Green , Color . White ])
```

[CreatSymbolGlyph.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/TextComponent/entry/src/main/ets/pages/symbol/CreatSymbolGlyph.ets#L25-L30) 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165852.98166945782978352035798610733223:50001231000000:2800:2C12AF1CB9109FAEC75334EAED6967C091CEE3DBD9F4CC9A38DE5D0E306D31AD.png)

## 添加到文本中

[SymbolSpan](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolspan)可作为[Text](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text)的子组件用于显示图标小符号。可以在一个Text组件内添加多个SymbolSpan，从而展示一串连续的图标。

- 创建SymbolSpan。

SymbolSpan组件需嵌入在Text组件中才能显示，单独使用不会呈现任何内容。

 收起自动换行深色代码主题复制

```
Text () { SymbolSpan ($r( 'sys.symbol.ohos_trash' )) . fontWeight ( FontWeight . Normal ) . fontSize ( 96 ) }
```

[SymbolAddToText.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/TextComponent/entry/src/main/ets/pages/symbol/SymbolAddToText.ets#L29-L35) 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165852.77216853155958097669000930464631:50001231000000:2800:76C99A2A7197DA8F98B515545599B6DBAAE4D87D143EB2B6CCEA6262398A524B.png)
- 通过[fontSize](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolspan#fontsize)属性设置SymbolSpan的大小。

 收起自动换行深色代码主题复制

```
Row () { Column () { Text ( '48' ) Text () { SymbolSpan ($r( 'sys.symbol.ohos_folder_badge_plus' )) . fontSize ( 48 ) . renderingStrategy ( SymbolRenderingStrategy . SINGLE ) . fontColor ([ Color . Black , Color . Green , Color . White ]) } } Column () { Text ( '72' ) Text () { SymbolSpan ($r( 'sys.symbol.ohos_folder_badge_plus' )) . fontSize ( 72 ) . renderingStrategy ( SymbolRenderingStrategy . SINGLE ) . fontColor ([ Color . Black , Color . Green , Color . White ]) } } Column () { Text ( '96' ) Text () { SymbolSpan ($r( 'sys.symbol.ohos_folder_badge_plus' )) . fontSize ( 96 ) . renderingStrategy ( SymbolRenderingStrategy . SINGLE ) . fontColor ([ Color . Black , Color . Green , Color . White ]) } } }
```

[SymbolAddToText.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/TextComponent/entry/src/main/ets/pages/symbol/SymbolAddToText.ets#L39-L71) 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165852.72567005276632412225243499507441:50001231000000:2800:A911F492DDF931B3AD69DD510DD9F9E945262160B519346E61D97CD51FB85D3C.png)
- 通过[fontWeight](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolspan#fontweight)属性设置SymbolSpan组件的粗细。

 收起自动换行深色代码主题复制

```
Row () { Column () { Text ( 'Light' ) Text () { SymbolSpan ($r( 'sys.symbol.ohos_trash' )) . fontWeight ( FontWeight . Lighter ) . fontSize ( 96 ) } } Column () { Text ( 'Normal' ) Text () { SymbolSpan ($r( 'sys.symbol.ohos_trash' )) . fontWeight ( FontWeight . Normal ) . fontSize ( 96 ) } } Column () { Text ( 'Bold' ) Text () { SymbolSpan ($r( 'sys.symbol.ohos_trash' )) . fontWeight ( FontWeight . Bold ) . fontSize ( 96 ) } } }
```

[SymbolAddToText.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/TextComponent/entry/src/main/ets/pages/symbol/SymbolAddToText.ets#L75-L104) 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165852.20386931646564515565416772242875:50001231000000:2800:9D1ABF50EE36918434B81958E71B2F2A4820F22FEDE9AB7CE4E3F8C905221893.png)
- 通过[fontColor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolspan#fontcolor)属性设置SymbolSpan的颜色。

 收起自动换行深色代码主题复制

```
Row () { Column () { Text ( 'Black' ) Text () { SymbolSpan ($r( 'sys.symbol.ohos_folder_badge_plus' )) . fontSize ( 96 ) . fontColor ([ Color . Black ]) } } Column () { Text ( 'Green' ) Text () { SymbolSpan ($r( 'sys.symbol.ohos_folder_badge_plus' )) . fontSize ( 96 ) . fontColor ([ Color . Green ]) } } Column () { Text ( 'Pink' ) Text () { SymbolSpan ($r( 'sys.symbol.ohos_folder_badge_plus' )) . fontSize ( 96 ) . fontColor ([ Color . Pink ]) } } }
```

[SymbolAddToText.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/TextComponent/entry/src/main/ets/pages/symbol/SymbolAddToText.ets#L108-L137) 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165852.89889359695681494379055607436895:50001231000000:2800:E235EC5431A9DFFD113BD64E6A2F927B18AF63BC4EA7E65EDE8ACE7FFE630445.png)
- 通过[renderingStrategy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolspan#renderingstrategy)属性设置SymbolSpan的渲染策略。

 收起自动换行深色代码主题复制

```
Row () { Column () { // 请将$r('app.string.single_color')替换为实际资源文件，在本示例中该资源文件的value值为"单色" Text ($r( 'app.string.single_color' )); Text () { SymbolSpan ($r( 'sys.symbol.ohos_folder_badge_plus' )) . fontSize ( 96 ) . renderingStrategy ( SymbolRenderingStrategy . SINGLE ) . fontColor ([ Color . Black , Color . Green , Color . White ]) } } Column () { // 请将$r('app.string.multi_color')替换为实际资源文件，在本示例中该资源文件的value值为"多色" Text ($r( 'app.string.multi_color' )); Text () { SymbolSpan ($r( 'sys.symbol.ohos_folder_badge_plus' )) . fontSize ( 96 ) . renderingStrategy ( SymbolRenderingStrategy . MULTIPLE_COLOR ) . fontColor ([ Color . Black , Color . Green , Color . White ]) } } Column () { // 请将$r('app.string.hierarchical')替换为实际资源文件，在本示例中该资源文件的value值为"分层" Text ($r( 'app.string.hierarchical' )); Text () { SymbolSpan ($r( 'sys.symbol.ohos_folder_badge_plus' )) . fontSize ( 96 ) . renderingStrategy ( SymbolRenderingStrategy . MULTIPLE_OPACITY ) . fontColor ([ Color . Black , Color . Green , Color . White ]) } } }
```

[SymbolAddToText.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/TextComponent/entry/src/main/ets/pages/symbol/SymbolAddToText.ets#L141-L176) 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165852.00022165021891378406589399601441:50001231000000:2800:76E99176733B61BA65FE209C94743EB21A25A6BB1796BBB4BCFCA5D80441A53A.png)
- 通过[effectStrategy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolspan#effectstrategy)属性设置SymbolSpan的动效策略。

 收起自动换行深色代码主题复制

```
Row () { Column () { // 请将$r('app.string.no_action')替换为实际资源文件，在本示例中该资源文件的value值为"无动效" Text ($r( 'app.string.no_action' )); Text () { SymbolSpan ($r( 'sys.symbol.ohos_wifi' )) . fontSize ( 96 ) . effectStrategy ( SymbolEffectStrategy . NONE ) } } Column () { // 请将$r('app.string.overall_scaling_animation_effect')替换为实际资源文件，在本示例中该资源文件的value值为"整体缩放动效" Text ($r( 'app.string.overall_scaling_animation_effect' )); Text () { SymbolSpan ($r( 'sys.symbol.ohos_wifi' )) . fontSize ( 96 ) . effectStrategy ( SymbolEffectStrategy . SCALE ) } } Column () { // 请将$r('app.string.hierarchical_animation')替换为实际资源文件，在本示例中该资源文件的value值为"层级动效" Text ($r( 'app.string.hierarchical_animation' )); Text () { SymbolSpan ($r( 'sys.symbol.ohos_wifi' )) . fontSize ( 96 ) . effectStrategy ( SymbolEffectStrategy . HIERARCHICAL ) } } }
```

[SymbolAddToText.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/TextComponent/entry/src/main/ets/pages/symbol/SymbolAddToText.ets#L181-L213) 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165852.23323238140040033291364635648225:50001231000000:2800:C0F007552E32C9F92413FACC840F3B67BCB5D884D0159859AD45E93B4CFEB9B4.gif)
- SymbolSpan不支持通用事件。

## 自定义图标动效

相较于effectStrategy属性在启动时即触发动效，可以通过以下两种方式来控制动效的播放状态，以及选择更多样化的动效策略。

关于effectStrategy属性与symbolEffect属性的多种动态属性使用及生效原则，详情请参阅[SymbolGlyph.symbolEffect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolglyph#symboleffect12-1)属性的说明。

- 通过设置SymbolEffect属性，可以同时配置SymbolGlyph的动效策略和播放状态。

 收起自动换行深色代码主题复制

```
@State isActive : boolean = true ;
```

[SymbolCustomIconAnimation.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/TextComponent/entry/src/main/ets/pages/symbol/SymbolCustomIconAnimation.ets#L22-L24) 收起自动换行深色代码主题复制

```
Column () { // 请将$r('app.string.variable_color_animation')替换为实际资源文件，在本示例中该资源文件的value值为"可变颜色动效" Text ($r( 'app.string.variable_color_animation' )); SymbolGlyph ($r( 'sys.symbol.ohos_wifi' )) . fontSize ( 96 ) . symbolEffect ( new HierarchicalSymbolEffect ( EffectFillStyle . ITERATIVE ), this . isActive ) // 请将$r('app.string.off')替换为实际资源文件，在本示例中该资源文件的value值为"关闭" // 请将$r('app.string.on')替换为实际资源文件，在本示例中该资源文件的value值为"播放" Button ( this . isActive ? $r( 'app.string.off' ) : $r( 'app.string.on' )). onClick ( () => { this . isActive = ! this . isActive ; }) }
```

[SymbolCustomIconAnimation.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/TextComponent/entry/src/main/ets/pages/symbol/SymbolCustomIconAnimation.ets#L40-L53) 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165852.45779506067138677824034771175357:50001231000000:2800:28B0E2BA49EBC5B19B56E75802DD4B74CDF736FED5D2494E48D1E118384464D9.gif)
- 通过设置SymbolEffect属性，可以同时指定SymbolGlyph的动画效果策略及其播放触发条件。

 收起自动换行深色代码主题复制

```
@State triggerValueReplace : number = 0 ;
```

[SymbolCustomIconAnimation.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/TextComponent/entry/src/main/ets/pages/symbol/SymbolCustomIconAnimation.ets#L25-L29) 收起自动换行深色代码主题复制

```
Column () { // 请将$r('app.string.bounce_animation')替换为实际资源文件，在本示例中该资源文件的value值为"弹跳动效" Text ($r( 'app.string.bounce_animation' )); SymbolGlyph ($r( 'sys.symbol.ellipsis_message_1' )) . fontSize ( 96 ) . fontColor ([ Color . Gray ]) . symbolEffect ( new BounceSymbolEffect ( EffectScope . WHOLE , EffectDirection . UP ), this . triggerValueReplace ) Button ( 'trigger' ). onClick ( () => { this . triggerValueReplace = this . triggerValueReplace + 1 ; }) }
```

[SymbolCustomIconAnimation.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/TextComponent/entry/src/main/ets/pages/symbol/SymbolCustomIconAnimation.ets#L56-L69) 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165852.37315896119659100387948075026206:50001231000000:2800:015DDE92775F7A688C052A1AF77DEEF2121985B22D567BCD1DA6D1057E7F1B6F.gif)
- 从API version 20开始，支持通过设置SymbolEffect属性为[ReplaceSymbolEffect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolglyph#replacesymboleffect12)，设置[ReplaceEffectType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolglyph#replaceeffecttype20枚举说明)为ReplaceEffectType.SLASH_OVERLAY，可以指定SymbolGlyph的禁用动画效果及其播放触发条件。

 收起自动换行深色代码主题复制

```
@State triggerValueReplace : number = 0 ; replaceFlag : boolean = true ; @State renderMode : number = 1 ;
```

[SymbolCustomIconAnimation.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/TextComponent/entry/src/main/ets/pages/symbol/SymbolCustomIconAnimation.ets#L26-L33) 收起自动换行深色代码主题复制

```
Column () { // 请将$r('app.string.disable_animation')替换为实际资源文件，在本示例中该资源文件的value值为"禁用动效" Text ($r( 'app.string.disable_animation' )); SymbolGlyph ( this . replaceFlag ? $r( 'sys.symbol.eye_slash' ) : $r( 'sys.symbol.eye' )) . fontSize ( 96 ) . renderingStrategy ( this . renderMode ) . symbolEffect ( new ReplaceSymbolEffect ( EffectScope . LAYER , ReplaceEffectType . SLASH_OVERLAY ), this . triggerValueReplace ) Button ( 'trigger' ). onClick ( () => { this . replaceFlag = ! this . replaceFlag ; this . triggerValueReplace = this . triggerValueReplace + 1 ; }) }
```

[SymbolCustomIconAnimation.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/TextComponent/entry/src/main/ets/pages/symbol/SymbolCustomIconAnimation.ets#L72-L86) 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165852.09913298983602574419973853566959:50001231000000:2800:7D3A1A834107F76FEEDEDDAD3F29DB522E1FC4844E3218AF7F66B1CC392B703A.gif)
- 从API version 20开始，支持通过设置SymbolEffect属性为[ReplaceSymbolEffect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolglyph#replacesymboleffect12)，设置[ReplaceEffectType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolglyph#replaceeffecttype20枚举说明)为ReplaceEffectType.CROSS_FADE，可以指定SymbolGlyph的快速替换动画效果及其播放触发条件。

 收起自动换行深色代码主题复制

```
@State triggerValueReplace : number = 0 ; replaceFlag : boolean = true ;
```

[SymbolCustomIconAnimation.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/TextComponent/entry/src/main/ets/pages/symbol/SymbolCustomIconAnimation.ets#L27-L31) 收起自动换行深色代码主题复制

```
Column () { // 请将$r('app.string.quick_replacement_animation')替换为实际资源文件，在本示例中该资源文件的value值为"快速替换动效" Text ($r( 'app.string.quick_replacement_animation' )); SymbolGlyph ( this . replaceFlag ? $r( 'sys.symbol.checkmark_circle' ) : $r( 'sys.symbol.repeat_1' )) . fontSize ( 96 ) . symbolEffect ( new ReplaceSymbolEffect ( EffectScope . WHOLE , ReplaceEffectType . CROSS_FADE ), this . triggerValueReplace ) Button ( 'trigger' ). onClick ( () => { this . replaceFlag = ! this . replaceFlag ; this . triggerValueReplace = this . triggerValueReplace + 1 ; }) }
```

[SymbolCustomIconAnimation.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/TextComponent/entry/src/main/ets/pages/symbol/SymbolCustomIconAnimation.ets#L89-L102) 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165852.06213680986728059297898377225626:50001231000000:2800:42A7D86F1F1A7E77F11E8B8451D9DC08B7072C80DDD16069EEA35DEE463BAB25.gif)

## 设置阴影和渐变色

- 从API version 20开始，支持通过[symbolShadow](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolglyph#symbolshadow20)接口实现了symbolGlyph组件显示阴影效果。

 收起自动换行深色代码主题复制

```
@State isActive : boolean = true ; options : ShadowOptions = { radius : 10.0 , color : Color . Blue , offsetX : 10 , offsetY : 10 , };
```

[SymbolShadowAndColor.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/TextComponent/entry/src/main/ets/pages/symbol/SymbolShadowAndColor.ets#L22-L31) 收起自动换行深色代码主题复制

```
Column () { // 请将$r('app.string.shadow_ability')替换为实际资源文件，在本示例中该资源文件的value值为"阴影能力" Text ($r( 'app.string.shadow_ability' )); SymbolGlyph ($r( 'sys.symbol.ohos_wifi' )) . fontSize ( 96 ) . symbolEffect ( new HierarchicalSymbolEffect ( EffectFillStyle . ITERATIVE ), ! this . isActive ) . symbolShadow ( this . options ) // 请将$r('app.string.off')替换为实际资源文件，在本示例中该资源文件的value值为"关闭" // 请将$r('app.string.on')替换为实际资源文件，在本示例中该资源文件的value值为"播放" Button (! this . isActive ? $r( 'app.string.off' ) : $r( 'app.string.on' )). onClick ( () => { this . isActive = ! this . isActive ; }) }
```

[SymbolShadowAndColor.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/TextComponent/entry/src/main/ets/pages/symbol/SymbolShadowAndColor.ets#L47-L61) 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165852.68237592256873863173020428428910:50001231000000:2800:DEC927D9E5D00AED2DEA7BD68B674F4899E428D16B23A6033B0B2D8D81F79555.gif)
- 从API version 20开始，支持通过[shaderStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolglyph#shaderstyle20)接口实现了symbolGlyph组件显示渐变色效果。

 收起自动换行深色代码主题复制

```
radialGradientOptions : RadialGradientOptions = { center : [ '50%' , '50%' ], radius : '20%' , colors : [[ Color . Red , 0.0 ], [ Color . Blue , 0.3 ], [ Color . Green , 0.5 ]], repeating : true , };
```

[SymbolShadowAndColor.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/TextComponent/entry/src/main/ets/pages/symbol/SymbolShadowAndColor.ets#L33-L40) 收起自动换行深色代码主题复制

```
Column () { // 请将$r('app.string.radial_gradient')替换为实际资源文件，在本示例中该资源文件的value值为"径向渐变" Text ($r( 'app.string.radial_gradient' )) . fontSize ( 18 ) . fontColor ( 0xCCCCCC ) . textAlign ( TextAlign . Center ) SymbolGlyph ($r( 'sys.symbol.ohos_folder_badge_plus' )) . fontSize ( 96 ) . shaderStyle ([ new RadialGradientStyle ( this . radialGradientOptions )]) }
```

[SymbolShadowAndColor.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/TextComponent/entry/src/main/ets/pages/symbol/SymbolShadowAndColor.ets#L64-L75) 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165852.23467928111871009765045159029607:50001231000000:2800:657BA0F7E792F61EF7ED4BEEC8C9C80DFD057F59449B45C238665770051158D9.jpg)

## 添加事件

SymbolGlyph组件可以添加通用事件，例如绑定[onClick](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-events-click#onclick)、[onTouch](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-events-touch#ontouch)等事件来响应操作。

 收起自动换行深色代码主题复制

```
@State wifiColor : ResourceColor = Color . Black ;
```

[SymbolAddEvent.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/TextComponent/entry/src/main/ets/pages/symbol/SymbolAddEvent.ets#L21-L23) 收起自动换行深色代码主题复制

```
SymbolGlyph ($r( 'sys.symbol.ohos_wifi' )) . fontSize ( 96 ) . fontColor ([ this . wifiColor ]) . onClick ( () => { this . wifiColor = Color . Gray ; })
```

[SymbolAddEvent.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/TextComponent/entry/src/main/ets/pages/symbol/SymbolAddEvent.ets#L29-L36) 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165852.07043094966944945873720315142343:50001231000000:2800:996A7FC54B4A1D532CC7072DFFAD73F24E6BA796ED6E8DF76B6CF05D05D9D319.gif)

## 场景示例

该示例通过symbolEffect、fontSize、fontColor属性展示了播放列表的效果。

 收起自动换行深色代码主题复制

```
```

[SymbolSceneExample.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/TextComponent/entry/src/main/ets/pages/symbol/SymbolSceneExample.ets#L18-L234) 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165852.60701209576808601916777155536048:50001231000000:2800:651407016E0EBD057A2CEC7397994190C0CCDFB4306D6243D5B268429BE6DE6F.gif)