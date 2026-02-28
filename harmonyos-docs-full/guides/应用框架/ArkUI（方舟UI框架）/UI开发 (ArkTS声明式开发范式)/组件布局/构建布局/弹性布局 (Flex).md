## 概述

弹性布局（[Flex](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-flex)）提供更加有效的方式对容器中的子元素进行排列、对齐和分配剩余空间。常用于页面头部导航栏的均匀分布、页面框架的搭建、多行数据的排列等。

容器默认存在主轴与交叉轴，子元素默认沿主轴排列，子元素在主轴方向的尺寸称为主轴尺寸，在交叉轴方向的尺寸称为交叉轴尺寸。

**图1** 主轴为水平方向的Flex容器示意图

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165930.49015354133017660895552942279904:50001231000000:2800:6AF30F5AA928D9E81B91A24F4BE623C546E8E5B7C7A304534B4F65115CDF9094.png)

## 基本概念

- 主轴：Flex组件布局方向的轴线，子元素默认沿着主轴排列。主轴开始的位置称为主轴起始点，结束位置称为主轴结束点。
- 交叉轴：垂直于主轴方向的轴线。交叉轴开始的位置称为交叉轴起始点，结束位置称为交叉轴结束点。

## 布局方向

在弹性布局中，容器的子元素可以按照任意方向排列。通过设置[FlexOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-flex#flexoptions对象说明)的参数direction，可以决定主轴的方向，从而控制子元素的排列方向。

**图2** 弹性布局方向图

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165930.06015184274424033264686555532215:50001231000000:2800:4A455516334664FE0DE0E80F52A4EBC59617D39E4F6D857B3482E9DC23685318.png)

- FlexDirection.Row（默认值）：主轴为水平方向，子元素从起始端沿着水平方向开始排布。

 收起自动换行深色代码主题复制

```
Flex ({ direction : FlexDirection . Row }) { Text ( '1' ). width ( '33%' ). height ( 50 ). backgroundColor ( '#F5DEB3' ) Text ( '2' ). width ( '33%' ). height ( 50 ). backgroundColor ( '#D2B48C' ) Text ( '3' ). width ( '33%' ). height ( 50 ). backgroundColor ( '#F5DEB3' ) } . height ( 70 ) . width ( '90%' ) . padding ( 10 ) . backgroundColor ( '#AFEEEE' )
```

[FlexDirectionRow.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/flexlayout/FlexDirectionRow.ets#L20-L30) 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165930.26839935485591664994643902059766:50001231000000:2800:2333E741D1193DCFD67E6E8DC54BAE03910A7997D2F3E29AEC673B61F069D64D.png)
- FlexDirection.RowReverse：主轴为水平方向，子元素从终点端沿着FlexDirection.Row相反的方向开始排布。

 收起自动换行深色代码主题复制

```
Flex ({ direction : FlexDirection . RowReverse }) { Text ( '1' ). width ( '33%' ). height ( 50 ). backgroundColor ( '#F5DEB3' ) Text ( '2' ). width ( '33%' ). height ( 50 ). backgroundColor ( '#D2B48C' ) Text ( '3' ). width ( '33%' ). height ( 50 ). backgroundColor ( '#F5DEB3' ) } . height ( 70 ) . width ( '90%' ) . padding ( 10 ) . backgroundColor ( '#AFEEEE' )
```

[FlexDirectionRowReverse.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/flexlayout/FlexDirectionRowReverse.ets#L20-L30) 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165930.78999683307430662600926728336205:50001231000000:2800:EDFDC504373C0898FF29CD67AD83C9D0DBADC64C45ACFE33EF1E0359C3BC444A.png)
- FlexDirection.Column：主轴为垂直方向，子元素从起始端沿着垂直方向开始排布。

 收起自动换行深色代码主题复制

```
Flex ({ direction : FlexDirection . Column }) { Text ( '1' ). width ( '100%' ). height ( 50 ). backgroundColor ( '#F5DEB3' ) Text ( '2' ). width ( '100%' ). height ( 50 ). backgroundColor ( '#D2B48C' ) Text ( '3' ). width ( '100%' ). height ( 50 ). backgroundColor ( '#F5DEB3' ) } . height ( 70 ) . width ( '90%' ) . padding ( 10 ) . backgroundColor ( '#AFEEEE' )
```

[FlexDirectionColumn.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/flexlayout/FlexDirectionColumn.ets#L20-L30) 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165930.02760928672422832195718341990491:50001231000000:2800:31E0DF8B4A29C4644EDF83FADF1260A8ABAA36DB74A1E65F1728103EBD109293.png)
- FlexDirection.ColumnReverse：主轴为垂直方向，子元素从终点端沿着FlexDirection.Column相反的方向开始排布。

 收起自动换行深色代码主题复制

```
Flex ({ direction : FlexDirection . ColumnReverse }) { Text ( '1' ). width ( '100%' ). height ( 50 ). backgroundColor ( '#F5DEB3' ) Text ( '2' ). width ( '100%' ). height ( 50 ). backgroundColor ( '#D2B48C' ) Text ( '3' ). width ( '100%' ). height ( 50 ). backgroundColor ( '#F5DEB3' ) } . height ( 70 ) . width ( '90%' ) . padding ( 10 ) . backgroundColor ( '#AFEEEE' )
```

[FlexDirectionColumnReverse.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/flexlayout/FlexDirectionColumnReverse.ets#L20-L30) 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165931.19302697985550240754385911561863:50001231000000:2800:7D5EA5C3EF6C00146EDE4AB6BCF9A66D446040FA05DAD16FDA0CB62FE72DD040.png)

## 布局换行

弹性布局分为单行布局和多行布局。默认情况下，Flex容器中的子元素都排在一条线（又称“轴线”）上。wrap属性控制当子元素主轴尺寸之和大于容器主轴尺寸时，Flex是单行布局还是多行布局。在多行布局时，通过交叉轴方向，确认新行排列方向。

- FlexWrap.NoWrap（默认值）：不换行。如果子元素的宽度总和大于父元素的宽度，则子元素会被压缩宽度。

 收起自动换行深色代码主题复制

```
Flex ({ wrap : FlexWrap . NoWrap }) { Text ( '1' ). width ( '50%' ). height ( 50 ). backgroundColor ( '#F5DEB3' ) Text ( '2' ). width ( '50%' ). height ( 50 ). backgroundColor ( '#D2B48C' ) Text ( '3' ). width ( '50%' ). height ( 50 ). backgroundColor ( '#F5DEB3' ) } . width ( '90%' ) . padding ( 10 ) . backgroundColor ( '#AFEEEE' )
```

[FlexWrapNoWrap.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/flexlayout/FlexWrapNoWrap.ets#L20-L29) 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165931.04285385553939434711699151631258:50001231000000:2800:918B2C24B4878E2F0EC00C78561E7885FC950856CFCB6743E956A719426354BF.png)
- FlexWrap.Wrap：换行，每一行子元素按照主轴方向排列。

 收起自动换行深色代码主题复制

```
Flex ({ wrap : FlexWrap . Wrap }) { Text ( '1' ). width ( '50%' ). height ( 50 ). backgroundColor ( '#F5DEB3' ) Text ( '2' ). width ( '50%' ). height ( 50 ). backgroundColor ( '#D2B48C' ) Text ( '3' ). width ( '50%' ). height ( 50 ). backgroundColor ( '#D2B48C' ) } . width ( '90%' ) . padding ( 10 ) . backgroundColor ( '#AFEEEE' )
```

[FlexWrapWrap.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/flexlayout/FlexWrapWrap.ets#L20-L29) 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165931.84209155350662948811723153935184:50001231000000:2800:AC06EFA91EDA9067A4EB74C7B90DE4315E083E258F59850BE00A1E42B9CBB8EB.png)
- FlexWrap.WrapReverse：换行，每一行子元素按照主轴反方向排列。

 收起自动换行深色代码主题复制

```
Flex ({ wrap : FlexWrap . WrapReverse }) { Text ( '1' ). width ( '50%' ). height ( 50 ). backgroundColor ( '#F5DEB3' ) Text ( '2' ). width ( '50%' ). height ( 50 ). backgroundColor ( '#D2B48C' ) Text ( '3' ). width ( '50%' ). height ( 50 ). backgroundColor ( '#F5DEB3' ) } . width ( '90%' ) . padding ( 10 ) . backgroundColor ( '#AFEEEE' )
```

[FlexWrapWrapReverse.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/flexlayout/FlexWrapWrapReverse.ets#L20-L29) 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165931.79884092235526553096469905204581:50001231000000:2800:20C708E36738BC0388B84D5246794D2E5DD3E0281413E190B4A020B1D0DC6078.png)

## 主轴对齐方式

通过justifyContent参数设置子元素在主轴方向的对齐方式。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165931.27753784765486726093063709776045:50001231000000:2800:21125987F864093E484A1AE7EE42631D696742AA50CE9785AA711CEEB5B24CF8.png)

- FlexAlign.Start（默认值）：子元素在主轴方向起始端对齐， 第一个子元素与父元素边沿对齐，其他元素与前一个元素对齐。

 收起自动换行深色代码主题复制

```
Flex ({ justifyContent : FlexAlign . Start }) { Text ( '1' ). width ( '20%' ). height ( 50 ). backgroundColor ( '#F5DEB3' ) Text ( '2' ). width ( '20%' ). height ( 50 ). backgroundColor ( '#D2B48C' ) Text ( '3' ). width ( '20%' ). height ( 50 ). backgroundColor ( '#F5DEB3' ) } . width ( '90%' ) . padding ({ top : 10 , bottom : 10 }) . backgroundColor ( '#AFEEEE' )
```

[FlexAlignStart.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/flexlayout/FlexAlignStart.ets#L20-L49) 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165931.37019177773513107414176449501185:50001231000000:2800:22D18453926A9FC229EA776E49374E342728B91AB6B92B7A523F3B8A1A9FB1D4.png)
- FlexAlign.Center：子元素在主轴方向居中对齐。

 收起自动换行深色代码主题复制

```
Flex ({ justifyContent : FlexAlign . Center }) { Text ( '1' ). width ( '20%' ). height ( 50 ). backgroundColor ( '#F5DEB3' ) Text ( '2' ). width ( '20%' ). height ( 50 ). backgroundColor ( '#D2B48C' ) Text ( '3' ). width ( '20%' ). height ( 50 ). backgroundColor ( '#F5DEB3' ) } . width ( '90%' ) . padding ({ top : 10 , bottom : 10 }) . backgroundColor ( '#AFEEEE' )
```

[FlexAlignCenter.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/flexlayout/FlexAlignCenter.ets#L20-L29) 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165931.67793915510713673028752647080839:50001231000000:2800:94F646020361CAF237BEE5FF0F35F1560D9D017DC08743E131368FE047749551.png)
- FlexAlign.End：子元素在主轴方向终点端对齐，最后一个子元素与父元素边沿对齐，其他元素与后一个元素对齐。

 收起自动换行深色代码主题复制

```
Flex ({ justifyContent : FlexAlign . End }) { Text ( '1' ). width ( '20%' ). height ( 50 ). backgroundColor ( '#F5DEB3' ) Text ( '2' ). width ( '20%' ). height ( 50 ). backgroundColor ( '#D2B48C' ) Text ( '3' ). width ( '20%' ). height ( 50 ). backgroundColor ( '#F5DEB3' ) } . width ( '90%' ) . padding ({ top : 10 , bottom : 10 }) . backgroundColor ( '#AFEEEE' )
```

[FlexAlignEnd.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/flexlayout/FlexAlignEnd.ets#L20-L29) 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165931.70417830556804227636879951392615:50001231000000:2800:6F9361466064436BE56D111E1B6D2DB82BD121CC166418F4E239FFA2EEA611D1.png)
- FlexAlign.SpaceBetween：Flex主轴方向均匀分配弹性元素，相邻子元素之间距离相同。第一个子元素和最后一个子元素与父元素边沿对齐。

 收起自动换行深色代码主题复制

```
Flex ({ justifyContent : FlexAlign . SpaceBetween }) { Text ( '1' ). width ( '20%' ). height ( 50 ). backgroundColor ( '#F5DEB3' ) Text ( '2' ). width ( '20%' ). height ( 50 ). backgroundColor ( '#D2B48C' ) Text ( '3' ). width ( '20%' ). height ( 50 ). backgroundColor ( '#F5DEB3' ) } . width ( '90%' ) . padding ({ top : 10 , bottom : 10 }) . backgroundColor ( '#AFEEEE' )
```

[FlexAlignSpaceBetween.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/flexlayout/FlexAlignSpaceBetween.ets#L20-L29) 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165931.21816137978206042705494663758255:50001231000000:2800:96704B6AD2B225CBA08B03B035E5A13B64AAD39D62A54B2EE9CA9E5FA3DCF4A0.png)
- FlexAlign.SpaceAround：Flex主轴方向均匀分配弹性元素，相邻子元素之间距离相同。第一个子元素到主轴起始端的距离和最后一个子元素到主轴终点端的距离是相邻元素之间距离的一半。

 收起自动换行深色代码主题复制

```
Flex ({ justifyContent : FlexAlign . SpaceAround }) { Text ( '1' ). width ( '20%' ). height ( 50 ). backgroundColor ( '#F5DEB3' ) Text ( '2' ). width ( '20%' ). height ( 50 ). backgroundColor ( '#D2B48C' ) Text ( '3' ). width ( '20%' ). height ( 50 ). backgroundColor ( '#F5DEB3' ) } . width ( '90%' ) . padding ({ top : 10 , bottom : 10 }) . backgroundColor ( '#AFEEEE' )
```

[FlexAlignSpaceAround.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/flexlayout/FlexAlignSpaceAround.ets#L20-L29) 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165931.22922592857483605666960644678648:50001231000000:2800:C017EA52D52754CBE8181D9F9C03847520F79EC638762ED8572CDACC21185A84.png)
- FlexAlign.SpaceEvenly：Flex主轴方向元素等间距布局，相邻子元素之间的间距、第一个子元素与主轴起始端的间距、最后一个子元素到主轴终点端的间距均相等。

 收起自动换行深色代码主题复制

```
Flex ({ justifyContent : FlexAlign . SpaceEvenly }) { Text ( '1' ). width ( '20%' ). height ( 50 ). backgroundColor ( '#F5DEB3' ) Text ( '2' ). width ( '20%' ). height ( 50 ). backgroundColor ( '#D2B48C' ) Text ( '3' ). width ( '20%' ). height ( 50 ). backgroundColor ( '#F5DEB3' ) } . width ( '90%' ) . padding ({ top : 10 , bottom : 10 }) . backgroundColor ( '#AFEEEE' )
```

[FlexAlignSpaceEvenly.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/flexlayout/FlexAlignSpaceEvenly.ets#L20-L29) 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165931.09789839153493981178659401025132:50001231000000:2800:FAB7E98D0FF2F73FECC343EEC392ABA25362229C0F2A81C153AE1B320DBCA226.png)

## 交叉轴对齐方式

容器和子元素都可以设置交叉轴对齐方式，且子元素设置的对齐方式优先级较高。

### 容器组件设置交叉轴对齐

可以通过设置[FlexOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-flex#flexoptions对象说明)的参数alignItems，设置子元素在交叉轴的对齐方式。

- ItemAlign.Auto：使用Flex容器中默认配置。

 收起自动换行深色代码主题复制

```
Flex ({ alignItems : ItemAlign . Auto }) { Text ( '1' ). width ( '33%' ). height ( 30 ). backgroundColor ( '#F5DEB3' ) Text ( '2' ). width ( '33%' ). height ( 40 ). backgroundColor ( '#D2B48C' ) Text ( '3' ). width ( '33%' ). height ( 50 ). backgroundColor ( '#F5DEB3' ) } . size ({ width : '90%' , height : 80 }) . padding ( 10 ) . backgroundColor ( '#AFEEEE' )
```

[FlexItemAlignAuto.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/flexlayout/FlexItemAlignAuto.ets#L20-L29) 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165931.93502521092488336154533194171038:50001231000000:2800:242AAF21C1399CE1587FFE2A443C5638D93EE8D189DAB4D6921CBBFD3A77597C.png)
- ItemAlign.Start：交叉轴方向首部对齐。

 收起自动换行深色代码主题复制

```
Flex ({ alignItems : ItemAlign . Start }) { Text ( '1' ). width ( '33%' ). height ( 30 ). backgroundColor ( '#F5DEB3' ) Text ( '2' ). width ( '33%' ). height ( 40 ). backgroundColor ( '#D2B48C' ) Text ( '3' ). width ( '33%' ). height ( 50 ). backgroundColor ( '#F5DEB3' ) } . size ({ width : '90%' , height : 80 }) . padding ( 10 ) . backgroundColor ( '#AFEEEE' )
```

[FlexItemAlignStart.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/flexlayout/FlexItemAlignStart.ets#L20-L60) 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165931.86951423133618293287604398208858:50001231000000:2800:436DA64B07A2E8F923E5E4B13B637C697383109A2F8C1CD1066D5CEF21457BF3.png)
- ItemAlign.Center：交叉轴方向居中对齐。

 收起自动换行深色代码主题复制

```
Flex ({ alignItems : ItemAlign . Center }) { Text ( '1' ). width ( '33%' ). height ( 30 ). backgroundColor ( '#F5DEB3' ) Text ( '2' ). width ( '33%' ). height ( 40 ). backgroundColor ( '#D2B48C' ) Text ( '3' ). width ( '33%' ). height ( 50 ). backgroundColor ( '#F5DEB3' ) } . size ({ width : '90%' , height : 80 }) . padding ( 10 ) . backgroundColor ( '#AFEEEE' )
```

[FlexItemAlignCenter.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/flexlayout/FlexItemAlignCenter.ets#L20-L29) 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165931.52164156422372313325708727344719:50001231000000:2800:306303881002E7390C4EE85223BF4C7FD82603CFEDB7B449231E5D344FAA7C0E.png)
- ItemAlign.End：交叉轴方向底部对齐。

 收起自动换行深色代码主题复制

```
Flex ({ alignItems : ItemAlign . End }) { Text ( '1' ). width ( '33%' ). height ( 30 ). backgroundColor ( '#F5DEB3' ) Text ( '2' ). width ( '33%' ). height ( 40 ). backgroundColor ( '#D2B48C' ) Text ( '3' ). width ( '33%' ). height ( 50 ). backgroundColor ( '#F5DEB3' ) } . size ({ width : '90%' , height : 80 }) . padding ( 10 ) . backgroundColor ( '#AFEEEE' )
```

[FlexItemAlignEnd.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/flexlayout/FlexItemAlignEnd.ets#L20-L29) 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165931.31968763577710362294350044033972:50001231000000:2800:4CCA5ADC95ADE0253C97374A2462475E991621E6204D58095FE8871EB6480259.png)
- ItemAlign.Stretch：交叉轴方向拉伸填充，在未设置尺寸时，拉伸到容器尺寸。

 收起自动换行深色代码主题复制

```
Flex ({ alignItems : ItemAlign . Stretch }) { Text ( '1' ). width ( '33%' ). backgroundColor ( '#F5DEB3' ) Text ( '2' ). width ( '33%' ). backgroundColor ( '#D2B48C' ) Text ( '3' ). width ( '33%' ). backgroundColor ( '#F5DEB3' ) } . size ({ width : '90%' , height : 80 }) . padding ( 10 ) . backgroundColor ( '#AFEEEE' )
```

[FlexItemAlignStretch.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/flexlayout/FlexItemAlignStretch.ets#L20-L29) 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165931.80704754246511520937217734815045:50001231000000:2800:4DF29E7F5D04B880A965A89BF59AB4C0C74664D019A6C9D5B707BC5E45992D30.png)
- ItemAlign.Baseline：交叉轴方向文本基线对齐。

 收起自动换行深色代码主题复制

```
Flex ({ alignItems : ItemAlign . Baseline }) { Text ( '1' ). width ( '33%' ). height ( 30 ). backgroundColor ( '#F5DEB3' ) Text ( '2' ). width ( '33%' ). height ( 40 ). backgroundColor ( '#D2B48C' ) Text ( '3' ). width ( '33%' ). height ( 50 ). backgroundColor ( '#F5DEB3' ) } . size ({ width : '90%' , height : 80 }) . padding ( 10 ) . backgroundColor ( '#AFEEEE' )
```

[FlexItemAlignBaseline.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/flexlayout/FlexItemAlignBaseline.ets#L20-L29) 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165931.04225879710076365898056421866693:50001231000000:2800:662E5CED667792A656A740BD8BA74248DA7886126A9E2592B7953BC9508E7C5D.png)

### 子元素设置交叉轴对齐

子元素的[alignSelf](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-flex-layout#alignself)属性也可以设置子元素在父容器交叉轴的对齐方式，且会覆盖Flex布局容器中alignItems配置。如下例所示：

 收起自动换行深色代码主题复制

```
Flex ({ direction : FlexDirection . Row , alignItems : ItemAlign . Center }) { // 容器组件设置子元素居中 Text ( 'alignSelf Start' ). width ( '25%' ). height ( 80 ) . alignSelf ( ItemAlign . Start ) . backgroundColor ( '#F5DEB3' ) Text ( 'alignSelf Baseline' ) . alignSelf ( ItemAlign . Baseline ) . width ( '25%' ) . height ( 80 ) . backgroundColor ( '#D2B48C' ) Text ( 'alignSelf Baseline' ). width ( '25%' ). height ( 100 ) . backgroundColor ( '#F5DEB3' ) . alignSelf ( ItemAlign . Baseline ) Text ( 'no alignSelf' ). width ( '25%' ). height ( 100 ) . backgroundColor ( '#D2B48C' ) Text ( 'no alignSelf' ). width ( '25%' ). height ( 100 ) . backgroundColor ( '#F5DEB3' ) }. width ( '90%' ). height ( 220 ). backgroundColor ( '#AFEEEE' )
```

[FlexAlignSelf.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/flexlayout/FlexAlignSelf.ets#L20-L39) 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165931.03737709718774298015564782991477:50001231000000:2800:63D135B7E7C21B70366AEE303A0E0E2D4BA906517ED2885012AF6E6EEC79ED61.png)

上例中，Flex容器中alignItems设置交叉轴子元素的对齐方式为居中，子元素自身设置了alignSelf属性的情况，覆盖父组件的alignItems值，表现为alignSelf的定义。

### 内容对齐

可以通过[alignContent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-flex#flexoptions对象说明)参数设置子元素各行在交叉轴剩余空间内的对齐方式，只在多行的Flex布局中生效，可选值有：

- FlexAlign.Start：子元素各行与交叉轴起点对齐。

 收起自动换行深色代码主题复制

```
Flex ({ justifyContent : FlexAlign . SpaceBetween , wrap : FlexWrap . Wrap , alignContent : FlexAlign . Start }) { Text ( '1' ). width ( '30%' ). height ( 20 ). backgroundColor ( '#F5DEB3' ) Text ( '2' ). width ( '60%' ). height ( 20 ). backgroundColor ( '#D2B48C' ) Text ( '3' ). width ( '40%' ). height ( 20 ). backgroundColor ( '#D2B48C' ) Text ( '4' ). width ( '30%' ). height ( 20 ). backgroundColor ( '#F5DEB3' ) Text ( '5' ). width ( '20%' ). height ( 20 ). backgroundColor ( '#D2B48C' ) } . width ( '90%' ) . height ( 100 ) . backgroundColor ( '#AFEEEE' )
```

[FlexAlignCenterFlexAlignStart.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/flexlayout/FlexAlignCenterFlexAlignStart.ets#L20-L50) 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165931.70844429363560991352353393335371:50001231000000:2800:CB1F29635F8C48BBB559B107B7088755517B51DA80AC2676945BE78916A633C3.png)
- FlexAlign.Center：子元素各行在交叉轴方向居中对齐。

 收起自动换行深色代码主题复制

```
Flex ({ justifyContent : FlexAlign . SpaceBetween , wrap : FlexWrap . Wrap , alignContent : FlexAlign . Center }) { Text ( '1' ). width ( '30%' ). height ( 20 ). backgroundColor ( '#F5DEB3' ) Text ( '2' ). width ( '60%' ). height ( 20 ). backgroundColor ( '#D2B48C' ) Text ( '3' ). width ( '40%' ). height ( 20 ). backgroundColor ( '#D2B48C' ) Text ( '4' ). width ( '30%' ). height ( 20 ). backgroundColor ( '#F5DEB3' ) Text ( '5' ). width ( '20%' ). height ( 20 ). backgroundColor ( '#D2B48C' ) } . width ( '90%' ) . height ( 100 ) . backgroundColor ( '#AFEEEE' )
```

[FlexAlignCenterFlexAlignCenter.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/flexlayout/FlexAlignCenterFlexAlignCenter.ets#L20-L31) 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165932.67726220091561023512684892201022:50001231000000:2800:7B689F084624C84A327E894BB3EB39F1ABECB76CB45785832BF2BFF748E9EB22.png)
- FlexAlign.End：子元素各行与交叉轴终点对齐。

 收起自动换行深色代码主题复制

```
Flex ({ justifyContent : FlexAlign . SpaceBetween , wrap : FlexWrap . Wrap , alignContent : FlexAlign . SpaceBetween }) { Text ( '1' ). width ( '30%' ). height ( 20 ). backgroundColor ( '#F5DEB3' ) Text ( '2' ). width ( '60%' ). height ( 20 ). backgroundColor ( '#D2B48C' ) Text ( '3' ). width ( '40%' ). height ( 20 ). backgroundColor ( '#D2B48C' ) Text ( '4' ). width ( '30%' ). height ( 20 ). backgroundColor ( '#F5DEB3' ) Text ( '5' ). width ( '20%' ). height ( 20 ). backgroundColor ( '#D2B48C' ) } . width ( '90%' ) . height ( 100 ) . backgroundColor ( '#AFEEEE' )
```

[FlexAlignCenterFlexAlignSpaceBetween.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/flexlayout/FlexAlignCenterFlexAlignSpaceBetween.ets#L20-L31) 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165932.92821799865950209579734057602539:50001231000000:2800:60C0FDCE4580FEDE41488A606D86485264FEF87A18B141BB722282A79B020125.png)
- FlexAlign.SpaceBetween：子元素各行与交叉轴两端对齐，各行间垂直间距平均分布。

 收起自动换行深色代码主题复制

```
Flex ({ justifyContent : FlexAlign . SpaceBetween , wrap : FlexWrap . Wrap , alignContent : FlexAlign . End }) { Text ( '1' ). width ( '30%' ). height ( 20 ). backgroundColor ( '#F5DEB3' ) Text ( '2' ). width ( '60%' ). height ( 20 ). backgroundColor ( '#D2B48C' ) Text ( '3' ). width ( '40%' ). height ( 20 ). backgroundColor ( '#D2B48C' ) Text ( '4' ). width ( '30%' ). height ( 20 ). backgroundColor ( '#F5DEB3' ) Text ( '5' ). width ( '20%' ). height ( 20 ). backgroundColor ( '#D2B48C' ) } . width ( '90%' ) . height ( 100 ) . backgroundColor ( '#AFEEEE' )
```

[FlexAlignCenterFlexAlignEnd.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/flexlayout/FlexAlignCenterFlexAlignEnd.ets#L20-L31) 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165932.22941405490216012869872037188855:50001231000000:2800:D6A7D3DEB2A17BF4D85349376C3B9A507F569F7122692591DF77699B24234779.png)
- FlexAlign.SpaceAround：子元素各行间距相等，是元素首尾行与交叉轴两端距离的两倍。

 收起自动换行深色代码主题复制

```
Flex ({ justifyContent : FlexAlign . SpaceBetween , wrap : FlexWrap . Wrap , alignContent : FlexAlign . SpaceAround }) { Text ( '1' ). width ( '30%' ). height ( 20 ). backgroundColor ( '#F5DEB3' ) Text ( '2' ). width ( '60%' ). height ( 20 ). backgroundColor ( '#D2B48C' ) Text ( '3' ). width ( '40%' ). height ( 20 ). backgroundColor ( '#D2B48C' ) Text ( '4' ). width ( '30%' ). height ( 20 ). backgroundColor ( '#F5DEB3' ) Text ( '5' ). width ( '20%' ). height ( 20 ). backgroundColor ( '#D2B48C' ) } . width ( '90%' ) . height ( 100 ) . backgroundColor ( '#AFEEEE' )
```

[FlexAlignCenterFlexAlignSpaceAround.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/flexlayout/FlexAlignCenterFlexAlignSpaceAround.ets#L20-L31) 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165932.59604941470613989281385487701232:50001231000000:2800:25650F3D62C327D3CA2E1DEF998D306D82AA4C00A148C6B457DCE86884A088E8.png)
- FlexAlign.SpaceEvenly: 子元素各行间距，子元素首尾行与交叉轴两端距离都相等。

 收起自动换行深色代码主题复制

```
Flex ({ justifyContent : FlexAlign . SpaceBetween , wrap : FlexWrap . Wrap , alignContent : FlexAlign . SpaceEvenly }) { Text ( '1' ). width ( '30%' ). height ( 20 ). backgroundColor ( '#F5DEB3' ) Text ( '2' ). width ( '60%' ). height ( 20 ). backgroundColor ( '#D2B48C' ) Text ( '3' ). width ( '40%' ). height ( 20 ). backgroundColor ( '#D2B48C' ) Text ( '4' ). width ( '30%' ). height ( 20 ). backgroundColor ( '#F5DEB3' ) Text ( '5' ). width ( '20%' ). height ( 20 ). backgroundColor ( '#D2B48C' ) } . width ( '90%' ) . height ( 100 ) . backgroundColor ( '#AFEEEE' )
```

[FlexAlignCenterFlexAlignSpaceEvenly.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/flexlayout/FlexAlignCenterFlexAlignSpaceEvenly.ets#L20-L31) 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165932.49037177842440785585641204068259:50001231000000:2800:E69A65230C06EE1F1AFED94267A8F36AF742E5990CECE57DB1E04EBB8C19EEE2.png)

## 自适应拉伸

在弹性布局父组件尺寸过小时，通过子元素的以下属性设置其在父容器的占比，达到自适应布局。

- [flexBasis](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-flex-layout#flexbasis)：设置子元素在父容器主轴方向上的基准尺寸。如果设置了该属性，则子项占用的空间为该属性所设置的值；如果没设置该属性，那子项的空间为width/height的值。

 收起自动换行深色代码主题复制

```
Flex () { Text ( 'flexBasis("auto")' ) . flexBasis ( 'auto' ) // 未设置width以及flexBasis值为auto，内容自身宽度 . height ( 100 ) . backgroundColor ( '#F5DEB3' ) Text ( 'flexBasis("auto")' + ' width("40%")' ) . width ( '40%' ) . flexBasis ( 'auto' ) //设置width以及flexBasis值auto，使用width的值 . height ( 100 ) . backgroundColor ( '#D2B48C' ) Text ( 'flexBasis(100)' ) // 未设置width以及flexBasis值为100，宽度为100vp . flexBasis ( 100 ) . height ( 100 ) . backgroundColor ( '#F5DEB3' ) Text ( 'flexBasis(100)' ) . flexBasis ( 100 ) . width ( 200 ) // flexBasis值为100，覆盖width的设置值，宽度为100vp . height ( 100 ) . backgroundColor ( '#D2B48C' ) }. width ( '90%' ). height ( 120 ). padding ( 10 ). backgroundColor ( '#AFEEEE' )
```

[FlexBasis.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/flexlayout/FlexBasis.ets#L20-L43) 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165932.36675319129107661266024547251018:50001231000000:2800:8A1FF9C28D6CE5617DCC86220A2E299D51D369119A95EA9A6730A18EA1A595C1.png)
- [flexGrow](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-flex-layout#flexgrow)：设置父容器的剩余空间分配给此属性所在组件的比例，用于分配父组件的剩余空间。下述示例运行需要保证设备为横屏状态，否则运行效果可能存在差异。

 收起自动换行深色代码主题复制

```
Flex () { Text ( 'flexGrow(1)' ) . flexGrow ( 1 ) . width ( 100 ) . height ( 100 ) . backgroundColor ( '#F5DEB3' ) Text ( 'flexGrow(4)' ) . flexGrow ( 4 ) . width ( 100 ) . height ( 100 ) . backgroundColor ( '#D2B48C' ) Text ( 'no flexGrow' ) . width ( 100 ) . height ( 100 ) . backgroundColor ( '#F5DEB3' ) }. width ( 360 ). height ( 120 ). padding ( 10 ). backgroundColor ( '#AFEEEE' )
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165932.43821924963738085831218016275927:50001231000000:2800:98E227AFAC988ED3EF94085AAFC72D39B68F5B26ECAE3EC26073624D28BF097E.png)

父容器宽度360vp，三个子元素原始宽度均为100vp，左右padding为20vp，总和320vp，剩余空间40vp根据flexGrow值的占比分配给子元素，未设置flexGrow的子元素不参与分配。

第一个元素以及第二个元素以1:4分配剩下的40vp。第一个元素为100vp+40vp * 1/5=108vp，第二个元素为100vp+40vp * 4/5=132vp。

- [flexShrink](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-flex-layout#flexshrink): 当父容器空间不足时，子元素的压缩比例。

 收起自动换行深色代码主题复制

```
Flex ({ direction : FlexDirection . Row }) { Text ( 'flexShrink(3)' ) . flexShrink ( 3 ) . width ( 200 ) . height ( 100 ) . backgroundColor ( '#F5DEB3' ) Text ( 'no flexShrink' ) . width ( 200 ) . height ( 100 ) . backgroundColor ( '#D2B48C' ) Text ( 'flexShrink(2)' ) . flexShrink ( 2 ) . width ( 200 ) . height ( 100 ) . backgroundColor ( '#F5DEB3' ) }. width ( 400 ). height ( 120 ). padding ( 10 ). backgroundColor ( '#AFEEEE' )
```

[FlexShrink.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/flexlayout/FlexShrink.ets#L20-L39) 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165932.26108393682083082109732304245098:50001231000000:2800:95ACC26C27C30CB0EB8519E1A2F648983F8FD75CCB63BC9EF289EA79B07D2921.png)

父容器宽度400vp，三个子元素原始宽度为200vp，左右padding为20vp，父容器给子元素的布局空间为380vp，超出父容器空间220vp。

将第一个元素和第三个元素以3:2的压缩比例进行压缩，直至不再超出父容器提供的布局空间。第一个元素为200vp - (220vp / 5) * 3=68vp，第三个元素为200vp - (220vp / 5) * 2=112vp。

## 场景示例

使用弹性布局，可以实现子元素沿水平方向排列，两端对齐，子元素间距平分，垂直方向上子元素居中的效果。

 收起自动换行深色代码主题复制

```
@Entry @Component struct FlexExample { build ( ) { Column () { Column ({ space : 5 }) { Flex ({ direction : FlexDirection . Row , wrap : FlexWrap . NoWrap , justifyContent : FlexAlign . SpaceBetween , alignItems : ItemAlign . Center }) { Text ( '1' ). width ( '30%' ). height ( 50 ). backgroundColor ( '#F5DEB3' ) Text ( '2' ). width ( '30%' ). height ( 50 ). backgroundColor ( '#D2B48C' ) Text ( '3' ). width ( '30%' ). height ( 50 ). backgroundColor ( '#F5DEB3' ) } . height ( 70 ) . width ( '90%' ) . backgroundColor ( '#AFEEEE' ) }. width ( '100%' ). margin ({ top : 5 }) }. width ( '100%' ) } }
```

[FlexExample.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/flexlayout/FlexExample.ets#L15-L39) 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165932.06090915597093459183149648730257:50001231000000:2800:986D20BD3539807D697BFCB69183A76BCF68F2C8B26406FE1FDB06754DAD57F0.png)