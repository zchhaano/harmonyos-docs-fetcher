# 创建瀑布流（WaterFlow）

[瀑布流](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-waterflow)常用于展示图片信息，尤其在购物和资讯类应用中。

ArkUI提供了WaterFlow容器组件，用于构建瀑布流布局。WaterFlow组件支持条件渲染、循环渲染和懒加载等方式生成子组件。

 说明 

本文仅展示关键代码片段，可运行的完整代码请参考[WaterFlow示例代码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-waterflow#示例)。

## 布局与约束

瀑布流支持横向和纵向布局。在纵向布局中，可以通过[columnsTemplate](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-waterflow#columnstemplate)设置列数；在横向布局中，可以通过[rowsTemplate](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-waterflow#rowstemplate)设置行数。

在瀑布流的纵向布局中，第一行的子节点按从左到右顺序排列，从第二行开始，每个子节点将放置在当前总高度最小的列。如果多个列的总高度相同，则按照从左到右的顺序填充。如下图：

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165851.67327467251428206400570578033926:50001231000000:2800:B007C20189A97834D6B9ECACBA324654234B7ABE52DCA4550826DDFF900C0CD5.png)

在瀑布流的横向布局中，每个子节点都会放置在当前总宽度最小的行。若多行总宽度相同，则按照从上到下的顺序进行填充。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165851.96675391816543233888685571007181:50001231000000:2800:304466C66F94F4C8D69496F3A0DC949269439A1D8C578CAD83006FECD3AC3F34.png)

## 无限滚动

### 到达末尾时新增数据

瀑布流常用于无限滚动的信息流。可以在瀑布流组件到达末尾位置时触发的[onReachEnd](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-waterflow#onreachend)事件回调中对[LazyForEach](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-rendering-control-lazyforeach)增加新数据，并将footer做成正在加载新数据的样式（使用[LoadingProgress](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-loadingprogress)组件）。

 收起自动换行深色代码主题复制

```
@Builder itemFoot ( ) { Row () { LoadingProgress () . color ( Color . Blue ). height ( 50 ). aspectRatio ( 1 ). width ( '20%' ) // 请将$r('app.string.waterFlow_text1')替换为实际资源文件，在本示例中该资源文件的value值为"正在加载 " Text ($r( 'app.string.waterFlow_text1' )) . fontSize ( 20 ) . width ( '30%' ) . height ( 50 ) . align ( Alignment . Center ) . margin ({ top : 2 }) }. width ( '100%' ). justifyContent ( FlexAlign . Center ) } build ( ) { NavDestination () { Column ({ space : 12 }) { // ... WaterFlow ({ footer : this . itemFoot (), layoutMode : WaterFlowLayoutMode . SLIDING_WINDOW }) { LazyForEach ( this . dataSource , ( item: number ) => { FlowItem () { ReusableFlowItem ({ item : item }) } . width ( '100%' ) . aspectRatio ( this . itemHeightArray [item % 100 ] / this . itemWidthArray [item% 100 ]) . backgroundColor ( this . colors [item % 5 ]) }, ( item: string ) => item) } . columnsTemplate ( '1fr ' . repeat ( this . columns )) . backgroundColor ( 0xFAEEE0 ) . width ( '100%' ) . height ( '100%' ) . layoutWeight ( 1 ) // 触底加载数据 . onReachEnd ( () => { setTimeout ( () => { this . dataSource . addNewItems ( 100 ); }, 1000 ) }) } // ... } . backgroundColor ( '#f1f2f3' ) // 请将$r('app.string.WaterFlowInfiniteScrolling_title')替换为实际资源文件，在本示例中该资源文件的value值为"无限滚动（到达末尾时新增数据）" . title ($r( 'app.string.WaterFlowInfiniteScrolling_title' )) }
```

[WaterFlowInfiniteScrolling.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/waterFlow/WaterFlowInfiniteScrolling.ets#L96-L147) 

在此处应通过在数据末尾添加元素的方式来新增数据，不可直接修改dataArray后通过LazyForEach的[onDataReloaded](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-rendering-control-lazyforeach#ondatareloaded)方法通知瀑布流重新加载数据。

由于在瀑布流布局中，各子节点的高度不一致，下面的节点位置依赖于上面的节点，所以重新加载所有数据会触发整个瀑布流重新计算布局，可能会导致卡顿。在数据末尾增加数据后，应使用[onDataAdd](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-rendering-control-lazyforeach#ondataadd8)通知，以使瀑布流能够识别新增数据并继续加载，同时避免对已有数据进行重复处理。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165851.27603798802469676815658195041313:50001231000000:2800:5CB83CDD7B5ED0F3A2EB530CD7B354B5B1C64538C51892130F07F4D7B8BBDE69.gif)

### 提前新增数据

虽然在onReachEnd()触发时加载数据可以实现无限加载，但在滑动到底部会出现明显的停顿。

为了实现更加流畅的无限滑动，需要调整增加新数据的时机。比如可以在LazyForEach还剩余若干个数据未遍历的情况下提前加载新数据。以下代码通过在WaterFlow的[onScrollIndex](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-waterflow#onscrollindex11)中判断当前显示的最后一个子节点相对数据集终点的距离，并在合适时机提前加载新数据，实现了无停顿的无限滚动。

 收起自动换行深色代码主题复制

```
build ( ) { NavDestination () { Column ({ space : 12 }) { // ... WaterFlow ({ layoutMode : WaterFlowLayoutMode . SLIDING_WINDOW }) { LazyForEach ( this . dataSource , ( item: number ) => { FlowItem () { ReusableFlowItem ({ item : item }) } . width ( '100%' ) . aspectRatio ( this . itemHeightArray [item % 100 ] / this . itemWidthArray [item% 100 ]) . backgroundColor ( this . colors [item % 5 ]) }, ( item: string ) => item) } . columnsTemplate ( '1fr ' . repeat ( this . columns )) . backgroundColor ( 0xFAEEE0 ) . width ( '100%' ) . height ( '100%' ) . layoutWeight ( 1 ) // 即将触底时提前增加数据 . onScrollIndex ( ( first: number , last: number ) => { if (last + 20 >= this . dataSource . totalCount ()) { setTimeout ( () => { this . dataSource . addNewItems ( 100 ); }, 1000 ); } }) } // ... } . backgroundColor ( '#f1f2f3' ) // 请将$r('app.string.WaterFlowInfiniteScrollingEarly_title')替换为实际资源文件，在本示例中该资源文件的value值为"无限滚动（提前新增数据）" . title ($r( 'app.string.WaterFlowInfiniteScrollingEarly_title' )) }
```

[WaterFlowInfiniteScrollingEarly.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/waterFlow/WaterFlowInfiniteScrollingEarly.ets#L110-L149) 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165851.69608649738007060062766405772216:50001231000000:2800:A0BF4F6EA514DC8D48580F76305DC3586CEC3E2F014FA552F2EFAA6F807878E3.gif)

## 动态切换列数

通过动态调整瀑布流的列数，应用能够实现在列表模式与瀑布流模式间的切换，或适应屏幕宽度的变化。 若要动态设置列数，建议采用瀑布流的移动窗口布局模式，这可以实现更快速的列数转换。

 收起自动换行深色代码主题复制

```
@Reusable @Component struct ReusableListItem { @State item : number = 0 ; aboutToReuse ( params: Record< string , number > ) { this . item = params. item ; } build ( ) { Row () { Image ( 'res/waterFlow(' + this . item % 5 + ').JPG' ) . objectFit ( ImageFit . Fill ) . height ( 100 ) . aspectRatio ( 1 ) Text ( 'N' + this . item ). fontSize ( 12 ). height ( '16' ). layoutWeight ( 1 ). textAlign ( TextAlign . Center ) } } } @Entry @Component export struct WaterFlowDynamicSwitchover { // 通过状态变量设置列数，可以按需修改触发布局更新 @State columns : number = 2 ; // ... build ( ) { NavDestination () { Column ({ space : 12 }) { // ... Column ({ space : 2 }) { // 请将$r('app.string.waterFlow_text2')替换为实际资源文件，在本示例中该资源文件的value值为"切换列数 " Button ($r( 'app.string.waterFlow_text2' )). fontSize ( 20 ). onClick ( () => { if ( this . columns === 2 ) { this . columns = 1 ; } else { this . columns = 2 ; } }) WaterFlow ({ layoutMode : WaterFlowLayoutMode . SLIDING_WINDOW }) { LazyForEach ( this . dataSource , ( item: number ) => { FlowItem () { if ( this . columns === 1 ) { ReusableListItem ({ item : item }) } else { ReusableFlowItem ({ item : item }) } } . width ( '100%' ) . aspectRatio ( this . columns === 2 ? this . itemHeightArray [item % 100 ] / this . itemWidthArray [item % 100 ] : 0 ) . backgroundColor ( this . colors [item % 5 ]) }, ( item: string ) => item) } . columnsTemplate ( '1fr ' . repeat ( this . columns )) . backgroundColor ( 0xFAEEE0 ) . width ( '100%' ) . height ( '100%' ) . layoutWeight ( 1 ) // 即将触底时提前增加数据 . onScrollIndex ( ( first: number , last: number ) => { if (last + 20 >= this . dataSource . totalCount ()) { setTimeout ( () => { this . dataSource . addNewItems ( 100 ); }, 1000 ); } }) // ... } } // ... } . backgroundColor ( '#f1f2f3' ) // 请将$r('app.string.WaterFlowDynamicSwitchover_title')替换为实际资源文件，在本示例中该资源文件的value值为"动态切换列数" . title ($r( 'app.string.WaterFlowDynamicSwitchover_title' )) } }
```

[WaterFlowDynamicSwitchover.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/waterFlow/WaterFlowDynamicSwitchover.ets#L40-L188) 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165851.85276951278167896304370474251792:50001231000000:2800:8B98DD06F9E1652CF6DADB432D78F05AED3F9873D587B9446838A62458F4C16F.gif)

## 分组混合布局

许多应用界面在瀑布流上方包含其他内容，这类场景可通过在Scroll或List内部嵌套WaterFlow来实现。类似下图：

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165852.91357617417011575736884713858525:50001231000000:2800:D5C1F1422D6C511FDB1935ED374474E338193E34261FF0D9ACC17050DCD4DBE7.png)

如果能够将不同部分的子节点整合到一个数据源中，那么通过设置[WaterFlowSections](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-waterflow#waterflowsections12)，可以在一个 WaterFlow 容器内实现混合布局。与嵌套滚动相比，这种方法可以简化滚动事件处理等应用逻辑。

每个瀑布流分组可以分别设置自己的列数、行间距、列间距、margin和子节点总数，如下代码可以实现上述效果：

 收起自动换行深色代码主题复制

```
```

[WaterFlowGroupingMixing.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/waterFlow/WaterFlowGroupingMixing.ets#L40-L148) 说明 

使用分组混合布局时不支持单独设置footer，可以使用最后一个分组作为尾部组件。

增加或删除数据后需要同步修改对应分组的itemCount。

## 示例代码

- [实现WaterFlow瀑布流布局功能](https://gitcode.com/HarmonyOS_Samples/water-flow)
- [主页瀑布流实现](https://gitcode.com/HarmonyOS-Cases/cases/blob/master/CommonAppDevelopment/feature/functionalscenes/README.md)