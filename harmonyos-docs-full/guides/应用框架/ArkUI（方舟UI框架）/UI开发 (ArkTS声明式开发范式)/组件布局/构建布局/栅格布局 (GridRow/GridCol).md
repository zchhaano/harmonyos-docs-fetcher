## 概述

栅格布局是一种通用的辅助定位工具，对移动设备的界面设计有较好的借鉴作用。主要优势包括：

1. 提供可循的规律：栅格布局可以为布局提供规律性的结构，解决多尺寸多设备的动态布局问题。通过将页面划分为等宽的列数和行数，可以方便地对页面元素进行定位和排版。
2. 统一的定位标注：栅格布局可以为系统提供一种统一的定位标注，保证不同设备上各个模块的布局一致性。这可以减少设计和开发的复杂度，提高工作效率。
3. 灵活的间距调整方法：栅格布局可以提供一种灵活的间距调整方法，满足特殊场景布局调整的需求。通过调整列与列之间和行与行之间的间距，可以控制整个页面的排版效果。
4. 自动换行和自适应：栅格布局可以完成一对多布局的自动换行和自适应。当页面元素的数量超出了一行或一列的容量时，他们会自动换到下一行或下一列，并且在不同的设备上自适应排版，使得页面布局更加灵活和适应性强。

[GridRow](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-gridrow)为栅格容器组件，需与栅格子组件[GridCol](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-gridcol)在栅格布局场景中联合使用。

## 栅格容器GridRow

### 栅格容器断点

栅格容器以设备的水平宽度（[像素单位](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-pixel-units)，单位vp）作为断点依据，定义设备的宽度类型，形成了一套断点规则。开发者可根据需求在不同的断点区间实现不同的页面布局效果。

栅格容器默认断点将设备宽度分为xs、sm、md、lg四类，尺寸范围如下：

  展开

| 断点名称 | 取值范围（vp） | 设备描述 |
| --- | --- | --- |
| xs | [0, 320） | 最小宽度类型设备。 |
| sm | [320, 600) | 小宽度类型设备。 |
| md | [600, 840) | 中等宽度类型设备。 |
| lg | [840, +∞) | 大宽度类型设备。 |

在GridRow栅格组件中，允许开发者使用[BreakPoints](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-gridrow#breakpoints)自定义修改断点的取值范围，最多支持6个断点，除了默认的4个断点外，还可以启用xl和xxl断点，支持6种不同尺寸（xs，sm，md，lg，xl，xxl）设备的布局设置。

  展开

| 断点名称 | 设备描述 |
| --- | --- |
| xs | 最小宽度类型设备。 |
| sm | 小宽度类型设备。 |
| md | 中等宽度类型设备。 |
| lg | 大宽度类型设备。 |
| xl | 特大宽度类型设备。 |
| xxl | 超大宽度类型设备。 |

- 开发者可根据实际使用场景，通过一个单调递增数组设置断点位置。由于栅格容器默认支持4个断点，在不设置断点位置时，系统为默认断点配置的单调递增数组为["320vp", "600vp", "840vp"]。开发者使用[BreakPoints](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-gridrow#breakpoints)最多可支持6个断点，因此此单调递增数组最大长度为5。

假设传入的数组是[n0, n1, n2, n3, n4]，则各个断点取值如下：

  展开

| 断点 | 取值范围 |
| --- | --- |
| xs | [0, n0) |
| sm | [n0, n1) |
| md | [n1, n2) |
| lg | [n2, n3) |
| xl | [n3, n4) |
| xxl | [n4, INF) |

  收起自动换行深色代码主题复制

```
breakpoints : { value : [ '100vp' , '200vp' ]} // 表示xs、sm、md共3个断点被使用，小于100vp为xs，100vp-200vp为sm，大于200vp为md。 breakpoints : { value : [ '320vp' , '600vp' ]} // 表示xs、sm、md共3个断点被使用，小于320vp为xs，320vp-600vp为sm，大于600vp为md。 breakpoints : { value : [ '320vp' , '600vp' , '840vp' , '1440vp' ]} // 表示xs、sm、md、lg、xl共5个断点被使用，小于320vp为xs，320vp-600vp为sm，  600vp-840vp为md，840vp-1440vp为lg，大于1440vp为xl。
```
- 栅格容器通过监听窗口或容器的尺寸变化进行断点，通过reference设置断点切换参考物。考虑到应用可能以非全屏窗口的形式显示，以应用窗口宽度为参照物更为通用。

例如，通过断点设置将应用宽度分成6个区间，通过columns配置各断点下栅格容器的栅格列数。

 收起自动换行深色代码主题复制

```
@Entry @Component struct WindowRefGridLayout { @State currentBp : string = "unknown" @State bgColors : ResourceColor [] = [ 'rgb(213,213,213)' , 'rgb(150,150,150)' , 'rgb(0,74,175)' , 'rgb(39,135,217)' , 'rgb(61,157,180)' , 'rgb(23,169,141)' , 'rgb(255,192,0)' , 'rgb(170,10,33)' ]; build ( ) { Column ({ space : 6 }) { Text ( this . currentBp ) GridRow ({ columns : { xs : 2 , // 窗口宽度落入xs断点上，栅格容器分为2列。 sm : 4 , // 窗口宽度落入sm断点上，栅格容器分为4列。 md : 8 , // 窗口宽度落入md断点上，栅格容器分为8列。 lg : 12 , // 窗口宽度落入lg断点上，栅格容器分为12列。 xl : 12 , // 窗口宽度落入xl断点上，栅格容器分为12列。 xxl : 12 // 窗口宽度落入xxl断点上，栅格容器分为12列。 }, breakpoints : { value : [ '320vp' , '600vp' , '840vp' , '1440vp' , '1600vp' ], // 表示在保留默认断点['320vp', '600vp', '840vp']的同时自定义增加'1440vp', '1600vp'的断点，实际开发中需要根据实际使用场景，合理设置断点值实现一次开发多端适配。 reference : BreakpointsReference . WindowSize } }) { ForEach ( this . bgColors , ( color: ResourceColor, index?: number | undefined ) => { GridCol ({ span : 1 }) { // 所有子组件占一列。 Row () { Text ( ` ${index} ` ) }. width ( '100%' ). height ( '50vp' ) }. backgroundColor (color) }) } . height ( 200 ) . border ({ color : 'rgb(39,135,217)' , width : 2 }) . onBreakpointChange ( ( breakPoint ) => { this . currentBp = breakPoint }) } } }
```

[GridLayoutReference.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/gridlayout/GridLayoutReference.ets#L15-L48) 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165946.03810954550065708483317751430220:50001231000000:2800:99F6A6F0EB17F8AC2D798C3C064E69E91FE5EE39056067C8FE100BD27D6494E4.gif)

### 布局的总列数

GridRow中通过columns设置栅格布局的总列数。

- API version 20之前，columns默认值为12，即在未设置columns时，任何断点下，栅格布局均被分成12列。
- API version 20及以后，columns默认值为{ xs: 2, sm: 4, md: 8, lg: 12, xl: 12, xxl: 12 }。

 收起自动换行深色代码主题复制

```
// xxx.ets @Entry @Component struct GridColumnsWithDefaults { @State bgColors : ResourceColor [] = [ 'rgb(213,213,213)' , 'rgb(150,150,150)' , 'rgb(0,74,175)' , 'rgb(39,135,217)' , 'rgb(61,157,180)' , 'rgb(23,169,141)' , 'rgb(255,192,0)' , 'rgb(170,10,33)' , 'rgb(213,213,213)' , 'rgb(150,150,150)' , 'rgb(0,74,175)' , 'rgb(39,135,217)' ]; build ( ) { GridRow () { ForEach ( this . bgColors , ( item: ResourceColor, index?: number | undefined ) => { GridCol ({ span : 1 }) { Row () { Text ( ` ${index} ` ) }. width ( '100%' ). height ( '50' ) }. backgroundColor (item) }) } } }
```

[GridLayoutColumns.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/gridlayout/GridLayoutColumns.ets#L15-L36) 

API version 20之前布局显示：

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165946.42834673747876041736398646977813:50001231000000:2800:3B034CA585AA105D7AF8F9CB4DE15192D809D43E0F895D51AA2DCDAC8B4055D4.png)

API version 20及以后布局显示（以sm设备为例，默认栅格列数为4）：

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165946.55440451309143883020687503881322:50001231000000:2800:0A682AC4A84C2A51C4EA042426F697E915CC440F59FBAE06499151EBFF59644B.png)

columns支持number和[GridRowColumnOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-gridrow#gridrowcolumnoption)两种类型, 可按两种方式设置栅格布局的总列数。

- 当columns类型为number时，栅格布局在任何尺寸设备下都被分为同一列数。下面分别设置栅格布局列数为4和8，子元素占一列，效果如下：

 收起自动换行深色代码主题复制

```
// xxx.ets @Entry @Component struct FixedFourColumnGrid { @State bgColors : ResourceColor [] = [ 'rgb(213,213,213)' , 'rgb(150,150,150)' , 'rgb(0,74,175)' , 'rgb(39,135,217)' , 'rgb(61,157,180)' , 'rgb(23,169,141)' , 'rgb(255,192,0)' , 'rgb(170,10,33)' ]; build ( ) { Column ({ space : 6 }) { Text ( 'columns：4' ). alignSelf ( ItemAlign . Start ) Row () { GridRow ({ columns : 4 }) { ForEach ( this . bgColors , ( item: ResourceColor, index?: number | undefined ) => { GridCol ({ span : 1 }) { Row () { Text ( ` ${index} ` ) }. width ( '100%' ). height ( '50' ) }. backgroundColor (item) }) } . width ( '100%' ). height ( '100%' ) } . height ( 160 ) . border ({ color : 'rgb(39,135,217)' , width : 2 }) . width ( '90%' ) } } }
```

[GridLayoutColumnsToFour.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/gridlayout/GridLayoutColumnsToFour.ets#L15-L42) 收起自动换行深色代码主题复制

```
// xxx.ets @Entry @Component struct FixedEightColumnGrid { @State bgColors : ResourceColor [] = [ 'rgb(213,213,213)' , 'rgb(150,150,150)' , 'rgb(0,74,175)' , 'rgb(39,135,217)' , 'rgb(61,157,180)' , 'rgb(23,169,141)' , 'rgb(255,192,0)' , 'rgb(170,10,33)' ]; build ( ) { Column ({ space : 6 }) { Text ( 'columns：8' ). alignSelf ( ItemAlign . Start ) Row () { GridRow ({ columns : 8 }) { ForEach ( this . bgColors , ( item: ResourceColor, index?: number | undefined ) => { GridCol ({ span : 1 }) { Row () { Text ( ` ${index} ` ) }. width ( '100%' ). height ( '50' ) }. backgroundColor (item) }) } . width ( '100%' ). height ( '100%' ) } . height ( 160 ) . border ({ color : 'rgb(39,135,217)' , width : 2 }) . width ( '90%' ) } } }
```

[GridLayoutColumnsToEight.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/gridlayout/GridLayoutColumnsToEight.ets#L15-L42) 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165946.68564660962742026226382493492717:50001231000000:2800:CF031757286149909DBD95FC30C50FE048831E3483449A85228742A6B5A44399.png)
- 当columns类型为[GridRowColumnOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-gridrow#gridrowcolumnoption)时，支持下面6种不同尺寸（xs，sm，md，lg，xl，xxl）设备的栅格列数设置，不同尺寸的设备支持配置不同的栅格列数。

 收起自动换行深色代码主题复制

```
@Entry @Component struct GridRowColumnOptionLayout { @State bgColors : ResourceColor [] = [ 'rgb(213,213,213)' , 'rgb(150,150,150)' , 'rgb(0,74,175)' , 'rgb(39,135,217)' , 'rgb(61,157,180)' , 'rgb(23,169,141)' , 'rgb(255,192,0)' , 'rgb(170,10,33)' ]; build ( ) { GridRow ({ columns : { sm : 4 , md : 8 }, breakpoints : { value : [ '320vp' , '600vp' , '840vp' , '1440vp' , '1600vp' ] // 表示在保留默认断点['320vp', '600vp', '840vp']的同时自定义增加'1440vp', '1600vp'的断点，实际开发中需要根据实际使用场景，合理设置断点值实现一次开发多端适配。 } }) { ForEach ( this . bgColors , ( item: ResourceColor, index?: number | undefined ) => { GridCol ({ span : 1 }) { Row () { Text ( ` ${index} ` ) }. width ( '100%' ). height ( '50' ) }. backgroundColor (item) }) } . height ( 200 ) . border ({ color : 'rgb(39,135,217)' , width : 2 }) } }
```

[GridLayoutColumnOption.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/gridlayout/GridLayoutColumnOption.ets#L15-L42) 

API version 20之前布局显示（xs设备未配置栅格列数，取默认列数12）：

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165946.68470008271708647414949536893917:50001231000000:2800:BC5F81FC2FFA242D00062B054C06D6FAAA7B15748692437E19C1F532B5B3F9E8.gif)

API version 20及以后布局显示（xs设备继承sm设备栅格列数）：

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165946.42918730727016022985152161820322:50001231000000:2800:2373B3A068BCBAAF029C4D2300E5E5F61E362E6AF176C30144072E4F22E4E7CD.gif)

仅部分设置sm、md的栅格列数，未配置的xs、lg、xl、xxl设备根据[栅格列数补全](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-gridrow#gridrowcolumnoption)取默认值。

### 排列方向

栅格布局中，可以通过设置GridRow的direction属性来指定栅格子组件在栅格容器中的排列方向。该属性可以设置为[GridRowDirection](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-gridrow#gridrowdirection枚举说明).Row（从左往右排列）或[GridRowDirection](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-gridrow#gridrowdirection枚举说明).RowReverse（从右往左排列），以满足不同的布局需求。通过合理的direction属性设置，可以使得页面布局更加灵活和符合设计要求。

- 子组件默认从左往右排列。

 收起自动换行深色代码主题复制

```
GridRow ({ direction : GridRowDirection . Row }) { /* ... */ }
```

[GridLayoutDirectionRow.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/gridlayout/GridLayoutDirectionRow.ets#L21-L23) 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165946.94381015304068771775499231612762:50001231000000:2800:EEEC516BAC5FAADB7A55C970BDE5B185D6B2A3963595B2EE74E212563A75108E.png)
- 子组件从右往左排列。

 收起自动换行深色代码主题复制

```
GridRow ({ direction : GridRowDirection . RowReverse }) { /* ... */ }
```

[GridLayoutDirectionRowReverse.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/gridlayout/GridLayoutDirectionRowReverse.ets#L21-L23) 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165946.06993432173481469149585300964935:50001231000000:2800:0573C257A189005D0C715FF3D6573CAC37DCF55E89402218A3BD70E1D20289EB.png)

### 子组件间距

GridRow中通过gutter属性设置子元素在水平和垂直方向的间距。

- 当gutter类型为number时，同时设置栅格子组件间水平和垂直方向边距且相等。下例中，设置子组件水平与垂直方向距离相邻元素的间距为10。

 收起自动换行深色代码主题复制

```
GridRow ({ gutter : 10 }) { /* ... */ }
```

[GridLayoutGutterToNumber.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/gridlayout/GridLayoutGutterToNumber.ets#L21-L23) 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165946.58472281163416879916477211409678:50001231000000:2800:DC110C19F5FBA72AF83F92F94602F058C7A3E7D80861641399A7911ACD792A3F.png)
- 当gutter类型为[GutterOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-gridrow#gutteroption)时，单独设置栅格子组件水平垂直边距，x属性为水平方向间距，y为垂直方向间距。

 收起自动换行深色代码主题复制

```
GridRow ({ gutter : { x : 20 , y : 50 } }) { /* ... */ }
```

[GridLayoutGutterOption.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/gridlayout/GridLayoutGutterOption.ets#L21-L23) 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165947.47918482566488823787738088737594:50001231000000:2800:C78A59E94E237072A0AD304E6CA2DE5AA9A21AE0C62CF048E0FF7B97B71324CD.png)

## 子组件GridCol

GridCol组件作为GridRow组件的子组件，通过给GridCol传参或者设置属性两种方式，设置span（占用列数），offset（偏移列数），order（元素序号）的值。

- 设置span。

 收起自动换行深色代码主题复制

```
let gSpan : Record < string , number > = { 'xs' : 1 , 'sm' : 2 , 'md' : 3 , 'lg' : 4 }
```

[GridColSpan.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/gridlayout/GridColSpan.ets#L15-L17) 收起自动换行深色代码主题复制

```
GridCol ({ span : 2 }){} GridCol ({ span : { xs : 1 , sm : 2 , md : 3 , lg : 4 } }){} GridCol (){}. span ( 2 ) GridCol (){}. span (gSpan)
```

[GridColSpan.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/gridlayout/GridColSpan.ets#L24-L29)
- 设置offset。

 收起自动换行深色代码主题复制

```
let gOffset : Record < string , number > = { 'xs' : 1 , 'sm' : 2 , 'md' : 3 , 'lg' : 4 }
```

[GridColOffset.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/gridlayout/GridColOffset.ets#L15-L17) 收起自动换行深色代码主题复制

```
GridCol ({ offset : 2 , span : 1 }){} GridCol ({ offset : { xs : 2 , sm : 2 , md : 2 , lg : 2 }, span : 1 }){} GridCol ({ span : 1 }){}. offset (gOffset)
```

[GridColOffset.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/gridlayout/GridColOffset.ets#L24-L28)
- 设置order。

 收起自动换行深色代码主题复制

```
let gOrder : Record < string , number > = { 'xs' : 1 , 'sm' : 2 , 'md' : 3 , 'lg' : 4 }
```

[GridColOrder.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/gridlayout/GridColOrder.ets#L15-L17) 收起自动换行深色代码主题复制

```
GridCol ({ order : 2 , span : 1 }){} GridCol ({ order : { xs : 1 , sm : 2 , md : 3 , lg : 4 }, span : 1 }){} GridCol ({ span : 1 }){}. order ( 2 ) GridCol ({ span : 1 }){}. order (gOrder)
```

[GridColOrder.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/gridlayout/GridColOrder.ets#L24-L29)

### span

子组件占栅格布局的列数，决定了子组件的宽度。默认值为1。

span支持number和[GridColColumnOption](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-gridcol#gridcolcolumnoption)两种类型, 可按两种方式设置栅格子组件占栅格容器的列数。

- 当span类型为number时，子组件在所有尺寸设备下占用的列数相同。

 收起自动换行深色代码主题复制

```
// xxx.ets @Entry @Component struct SpanNumberExample { @State bgColors : ResourceColor [] = [ 'rgb(213,213,213)' , 'rgb(150,150,150)' , 'rgb(0,74,175)' , 'rgb(39,135,217)' , 'rgb(61,157,180)' , 'rgb(23,169,141)' , 'rgb(255,192,0)' , 'rgb(170,10,33)' ]; build ( ) { GridRow ({ columns : 8 }) { ForEach ( this . bgColors , ( color: ResourceColor, index?: number | undefined ) => { GridCol ({ span : 2 }) { Row () { Text ( ` ${index} ` ) }. width ( '100%' ). height ( '50vp' ) } . backgroundColor (color) }) } . border ({ color : 'rgb(39,135,217)' , width : 2 }) . height ( '150vp' ) } }
```

[GridColSpanToNumber.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/gridlayout/GridColSpanToNumber.ets#L15-L37) 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165947.87926916674272356952587027088215:50001231000000:2800:E5C9C5EE02DF2946D3DEC3F109D237DE7E439ACA9E2746F552662DEE369F2309.png)
- 当span类型为GridColColumnOption时，支持6种不同尺寸（xs，sm，md，lg，xl，xxl）设备中子组件所占列数设置，不同尺寸的设备下子组件支持配置不同列数。若仅部分设置sm、md的列数，未配置的xs、lg、xl、xxl设备根据[列数补全](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-gridcol#gridcolcolumnoption)取默认值。

 收起自动换行深色代码主题复制

```
@Entry @Component struct SpanColumnOptionExample { @State currentBp : string = "unknown" @State bgColors : ResourceColor [] = [ 'rgb(213,213,213)' , 'rgb(150,150,150)' , 'rgb(0,74,175)' , 'rgb(39,135,217)' , 'rgb(61,157,180)' , 'rgb(23,169,141)' , 'rgb(255,192,0)' , 'rgb(170,10,33)' ]; build ( ) { Column ({ space : 6 }) { GridRow ({ columns : 8 }) { ForEach ( this . bgColors , ( color: ResourceColor, index?: number | undefined ) => { GridCol ({ span : { xs : 1 , sm : 2 , md : 3 , lg : 4 } }) { Row () { Text ( ` ${index} ` ) }. width ( '100%' ). height ( '50vp' ) } . backgroundColor (color) }) } . border ({ color : 'rgb(39,135,217)' , width : 2 }) . height ( '150vp' ) . onBreakpointChange ( ( breakPoint ) => { this . currentBp = breakPoint }) Text ( this . currentBp ) } } }
```

[GridColSpanToOption.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/gridlayout/GridColSpanToOption.ets#L15-L36) 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165947.16727121097701707018525145115909:50001231000000:2800:D7608B897F6C01BE719BB725A3FBFCACBF48E4C9F21FA9DCD9853E3201063817.gif)

### offset

栅格子组件相对于前一个子组件的偏移列数，默认为0。

- 当offset类型为number时，子组件偏移相同列数。

 收起自动换行深色代码主题复制

```
@Entry @Component struct OffsetNumberExample { @State bgColors : ResourceColor [] = [ 'rgb(213,213,213)' , 'rgb(150,150,150)' , 'rgb(0,74,175)' , 'rgb(39,135,217)' , 'rgb(61,157,180)' , 'rgb(23,169,141)' , 'rgb(255,192,0)' , 'rgb(170,10,33)' ]; build ( ) { Column () { GridRow ({ columns : 12 }) { ForEach ( this . bgColors , ( color: ResourceColor, index?: number | undefined ) => { GridCol ({ offset : 2 , span : 1 }) { Row () { Text ( '' + index) }. width ( '100%' ). height ( '50vp' ) } . backgroundColor (color) }) } Blank (). width ( '100%' ). height ( 150 ) }. border ({ color : 'rgb(39,135,217)' , width : 2 }) } }
```

[GridColOffsetToNumber.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/gridlayout/GridColOffsetToNumber.ets#L15-L36) 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165947.27502444927453865550550182933391:50001231000000:2800:AE3BC210DF6BEE3353C0D5419B1074CDAE6B584F7DD1956C27557B218CFC057D.png)

在lg及以上尺寸的设备上，栅格分成12列，每一个子组件占1列，偏移2列，每个子组件及间距共占3列，1行放4个子组件。
- 当offset类型为GridColColumnOption时，支持6种不同尺寸（xs，sm，md，lg，xl，xxl）设备中子组件所占列数设置，各个尺寸下数值可不同。

 收起自动换行深色代码主题复制

```
@Entry @Component struct OffsetColumnOptionExample { @State currentBp : string = "unknown" @State bgColors : ResourceColor [] = [ 'rgb(213,213,213)' , 'rgb(150,150,150)' , 'rgb(0,74,175)' , 'rgb(39,135,217)' , 'rgb(61,157,180)' , 'rgb(23,169,141)' , 'rgb(255,192,0)' , 'rgb(170,10,33)' ]; build ( ) { Column ({ space : 6 }) { GridRow ({ columns : 12 }) { ForEach ( this . bgColors , ( color: ResourceColor, index?: number | undefined ) => { GridCol ({ offset : { xs : 1 , sm : 2 , md : 3 , lg : 4 }, span : 1 }) { Row () { Text ( '' + index) }. width ( '100%' ). height ( '50vp' ) } . backgroundColor (color) }) } . height ( 200 ) . border ({ color : 'rgb(39,135,217)' , width : 2 }) . onBreakpointChange ( ( breakPoint ) => { this . currentBp = breakPoint }) Text ( this . currentBp ) } } }
```

[GridColOffsetToOption.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/gridlayout/GridColOffsetToOption.ets#L15-L38) 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165947.55449071864963337157055389739813:50001231000000:2800:F38E12A43A5F702A0B961C072822F7770DCCD4B40C836165626E8EC3F2D2AB65.gif)

### order

栅格子组件的序号，决定子组件排列次序。当子组件不设置order或者设置相同的order, 子组件按照代码顺序展示。当子组件设置不同的order时，order较小的组件在前，较大的在后。

当子组件部分设置order，部分不设置order时，未设置order的子组件依次排序靠前，设置了order的子组件按照数值从小到大排列。

- 当order类型为number时，子组件在任何尺寸下排序次序一致。

 收起自动换行深色代码主题复制

```
GridRow ({ columns : 12 }) { GridCol ({ order : 4 , span : 1 }) { Row () { Text ( '1' ) }. width ( '100%' ). height ( '50vp' ) }. backgroundColor ( 'rgb(213,213,213)' ) GridCol ({ order : 3 , span : 1 }) { Row () { Text ( '2' ) }. width ( '100%' ). height ( '50vp' ) }. backgroundColor ( 'rgb(150,150,150)' ) GridCol ({ order : 2 , span : 1 }) { Row () { Text ( '3' ) }. width ( '100%' ). height ( '50vp' ) }. backgroundColor ( 'rgb(0,74,175)' ) GridCol ({ order : 1 , span : 1 }) { Row () { Text ( '4' ) }. width ( '100%' ). height ( '50vp' ) }. backgroundColor ( 'rgb(39,135,217)' ) }
```

[GridColOrderToNumber.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/gridlayout/GridColOrderToNumber.ets#L20-L46) 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165947.40530055673289021094111342770644:50001231000000:2800:F904D0922BFA7FCD3D42C2D5E9DAFBE09ED37A29D575BB3C031C0F8316CC3FD2.png)
- 当order类型为GridColColumnOption时，支持6种不同尺寸（xs，sm，md，lg，xl，xxl）设备中子组件排序次序设置。在xs设备中，子组件排列顺序为1234；sm为2341，md为3412，lg为2431。

 收起自动换行深色代码主题复制

```
@Entry @Component struct OrderColumnOptionExample { @State currentBp : string = 'unknown' build ( ) { Column ({ space : 5 }) { GridRow ({ columns : 12 }) { GridCol ({ order : { xs : 1 , sm : 5 , md : 3 , lg : 7 }, span : 1 }) { Row () { Text ( '1' ) }. width ( '100%' ). height ( '50vp' ) }. backgroundColor ( 'rgb(213,213,213)' ) GridCol ({ order : { xs : 2 , sm : 2 , md : 6 , lg : 1 }, span : 1 }) { Row () { Text ( '2' ) }. width ( '100%' ). height ( '50vp' ) }. backgroundColor ( 'rgb(150,150,150)' ) GridCol ({ order : { xs : 3 , sm : 3 , md : 1 , lg : 6 }, span : 1 }) { Row () { Text ( '3' ) }. width ( '100%' ). height ( '50vp' ) }. backgroundColor ( 'rgb(0,74,175)' ) GridCol ({ order : { xs : 4 , sm : 4 , md : 2 , lg : 5 }, span : 1 }) { Row () { Text ( '4' ) }. width ( '100%' ). height ( '50vp' ) }. backgroundColor ( 'rgb(39,135,217)' ) }. border ({ width : 1 , color : 'rgb(39,135,217)' }). height ( '200vp' ). onBreakpointChange ( ( breakpoint ) => { this . currentBp = breakpoint }) Text ( this . currentBp ) } } }
```

[GridColOrderToOption.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/gridlayout/GridColOrderToOption.ets#L15-L57) 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165947.57320936078605984887153006512732:50001231000000:2800:5D71524C7F9473D692782C1F055E434CDD50803EBF25BDDB69AEC27C16ED5985.gif)

## 栅格组件的嵌套使用

栅格组件也可以嵌套使用，完成一些复杂的布局。

以下示例中，栅格把整个空间分为12份。第一层GridRow嵌套GridCol，分为中间大区域以及“footer”区域。第二层GridRow嵌套GridCol，分为“left”和“right”区域。子组件空间按照上一层父组件的空间划分，粉色的区域是屏幕空间的12列，绿色和蓝色的区域是父组件GridCol的12列，依次进行空间的划分。

 收起自动换行深色代码主题复制

```
@Entry @Component struct GridRowExample { build ( ) { GridRow ({ columns : 12 }) { GridCol ({ span : 12 }) { GridRow ({ columns : 12 }) { GridCol ({ span : 2 }) { Row () { Text ( 'left' ). fontSize ( 24 ) } . justifyContent ( FlexAlign . Center ) . height ( '90%' ) }. backgroundColor ( '#ff41dbaa' ) GridCol ({ span : 10 }) { Row () { Text ( 'right' ). fontSize ( 24 ) } . justifyContent ( FlexAlign . Center ) . height ( '90%' ) }. backgroundColor ( '#ff4168db' ) } . backgroundColor ( '#19000000' ) } GridCol ({ span : 12 }) { Row () { Text ( 'footer' ). width ( '100%' ). textAlign ( TextAlign . Center ) }. width ( '100%' ). height ( '10%' ). backgroundColor ( Color . Pink ) } }. width ( '100%' ). height ( 300 ) } }
```

[GridRowExample.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/gridlayout/GridRowExample.ets#L15-L50) 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165947.10193449893224080269216059565751:50001231000000:2800:3C85465A18E72BAD31BBC58B5B147DB8ACA51F0A0FDEFEDB0A610D62EAA7E0DD.png)

综上所述，栅格组件提供了丰富的自定义能力，功能非常灵活和强大。只需要明确栅格在不同断点下的Columns、Margin、Gutter及span等参数，即可确定最终布局，无需关心具体的设备类型及设备状态（如横竖屏）等。