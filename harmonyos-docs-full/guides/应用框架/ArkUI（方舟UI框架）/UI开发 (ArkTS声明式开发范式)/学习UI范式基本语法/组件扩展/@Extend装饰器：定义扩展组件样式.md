# @Extend装饰器：定义扩展组件样式

在前文的示例中，可以使用[@Styles](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-style)用于样式的重用，在@Styles的基础上，我们提供了@Extend，用于扩展组件样式。

 说明 

从API version 9开始支持。

从API version 9开始，该装饰器支持在ArkTS卡片中使用。

从API version 11开始，该装饰器支持在元服务中使用。

## 装饰器使用说明

### 语法

 收起自动换行深色代码主题复制

```
@Extend ( UIComponentName ) function functionName { ... }
```

### 使用规则

- 和@Styles不同，@Extend支持封装指定组件的私有属性、私有事件和自身定义的全局方法。

 收起自动换行深色代码主题复制

```
// @Extend(Text)可以支持Text的私有属性fontColor @Extend ( Text ) function fancy ( ) { . fontColor ( Color . Red ) } // superFancyText可以调用预定义的fancy @Extend ( Text ) function superFancyText ( size: number ) { . fontSize (size) . fancy () }
```

[GlobalFunctionExtension.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/extend/GlobalFunctionExtension.ets#L29-L42)
- 使用@Extend封装指定组件的私有属性、私有事件和自身定义的全局方法时，不支持和@Styles混用。

 收起自动换行深色代码主题复制

```
@Styles function fancy ( ) { . backgroundColor ( Color . Red ) } // superFancyText不可以调用预定义的fancy @Extend ( Text ) function superFancyText ( size: number ) { . fontSize (size) . fancy () }
```
- 和@Styles不同，@Extend装饰的方法支持参数，开发者可以在调用时传递参数，调用遵循TS方法传值调用。

 收起自动换行深色代码主题复制

```
// xxx.ets @Extend ( Text ) function fancy ( fontSize: number ) { . fontColor ( Color . Red ) . fontSize (fontSize) } @Entry @Component struct FancyUse { build ( ) { Row ({ space : 10 }) { Text ( 'Fancy' ) . fancy ( 16 ) Text ( 'Fancy' ) . fancy ( 24 ) } } }
```

[ExtendParameterUsage.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/extend/ExtendParameterUsage.ets#L28-L48)
- @Extend装饰的方法的参数可以为function，作为Event事件的句柄。

 收起自动换行深色代码主题复制

```
@Extend ( Text ) function makeMeClick ( onClick: () => void ) { . backgroundColor ( Color . Blue ) . onClick (onClick) } @Entry @Component struct FancyUse { @State label : string = 'Hello World' ; onClickHandler ( ) { this . label = 'Hello ArkUI' ; } build ( ) { Row ({ space : 10 }) { Text ( ` ${ this .label} ` ) . makeMeClick ( () => { this . onClickHandler (); }) } } }
```

[ExtendFunctionHandle.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/extend/ExtendFunctionHandle.ets#L29-L54)
- @Extend的参数可以为[状态变量](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-state-management-overview)，当状态变量改变时，UI可以正常的被刷新渲染。

 收起自动换行深色代码主题复制

```
@Extend ( Text ) function fancy ( fontSize: number ) { . fontColor ( Color . Blue ) . fontSize (fontSize) } @Entry @Component struct FancyUse { @State fontSizeValue : number = 20 ; build ( ) { Column ({ space : 10 }) { Text ( 'Fancy' ) . fancy ( this . fontSizeValue ) . onClick ( () => { this . fontSizeValue = 30 ; }) } . width ( '100%' ) } }
```

[ExtendUIStateVariable.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/extend/ExtendUIStateVariable.ets#L29-L51)

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165956.23050537540520200961237859798407:50001231000000:2800:EE9908A700E90012283C040032392C2F7699ECA2782826D910F0B382F3FA4914.gif)

## 限制条件

- 和@Styles不同，@Extend仅支持在全局定义，不支持在组件内部定义。

 说明 

仅限在当前文件内使用，不支持导出。

如果要实现export功能，推荐使用[AttributeModifier](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-user-defined-extension-attributemodifier)。

【反例】

 收起自动换行深色代码主题复制

```
@Entry @Component struct FancyUse { // 错误写法，@Extend仅支持在全局定义，不支持在组件内部定义 @Extend ( Text ) function fancy ( fontSize : number ) { . fontSize (fontSize) } build ( ) { Row ({ space : 10 }) { Text ( 'Fancy' ) . fancy ( 16 ) } } }
```

【正例】

 收起自动换行深色代码主题复制

```
// 正确写法 @Extend ( Text ) function fancy ( fontSize: number ) { . fontSize (fontSize) } @Entry @Component struct FancyUse { build ( ) { Row ({ space : 10 }) { Text ( 'Fancy' ) . fancy ( 16 ) } } }
```

[ExtendPositiveExample.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/extend/ExtendPositiveExample.ets#L29-L46)   

## 使用场景

以下示例声明了3个Text组件，每个Text组件均设置了[fontStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-appendix-enums#fontstyle)、[fontWeight](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-appendix-enums#fontweight) 和[backgroundColor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-background#backgroundcolor)样式。

 收起自动换行深色代码主题复制

```
@Entry @Component struct FancyUse { @State label : string = 'Hello World' ; build ( ) { Row ({ space : 10 }) { Text ( ` ${ this .label} ` ) . fontStyle ( FontStyle . Italic ) . fontWeight ( 500 ) . backgroundColor ( Color . Yellow ) Text ( ` ${ this .label} ` ) . fontStyle ( FontStyle . Italic ) . fontWeight ( 600 ) . backgroundColor ( Color . Pink ) Text ( ` ${ this .label} ` ) . fontStyle ( FontStyle . Italic ) . fontWeight ( 700 ) . backgroundColor ( Color . Orange ) }. margin ( '20%' ) } }
```

[ExtendUsageScenario.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/extend/ExtendUsageScenario.ets#L29-L52) 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165956.08381923344858493151642756781021:50001231000000:2800:24D1A55BF21846C87FB9A46B3C0FBA95D319D70B0D683C6271ED202ABFB9C935.png)

使用@Extend将样式组合复用，示例如下。

 收起自动换行深色代码主题复制

```
@Extend ( Text ) function fancyText ( weightValue: number , color: Color ) { . fontStyle ( FontStyle . Italic ) . fontWeight (weightValue) . backgroundColor (color) }
```

[ExtendUsageScenariotwo.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/extend/ExtendUsageScenariotwo.ets#L29-L36) 

通过@Extend组合样式后，使得代码更加简洁，增强可读性。

 收起自动换行深色代码主题复制

```
@Entry @Component struct FancyUse { @State label : string = 'Hello World' ; build ( ) { Row ({ space : 10 }) { Text ( ` ${ this .label} ` ) . fancyText ( 100 , Color . Blue ) Text ( ` ${ this .label} ` ) . fancyText ( 200 , Color . Pink ) Text ( ` ${ this .label} ` ) . fancyText ( 300 , Color . Orange ) }. margin ( '20%' ) } }
```

[ExtendUsageScenariotwo.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/extend/ExtendUsageScenariotwo.ets#L37-L54)