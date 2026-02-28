# 创建轮播 (Swiper)

[Swiper](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-swiper)组件提供滑动轮播显示的能力。Swiper本身是一个容器组件，当设置了多个子组件后，可以对这些子组件进行轮播显示。通常，在一些应用首页显示推荐的内容时，需要用到轮播显示的能力。

针对复杂页面场景，可以使用 Swiper 组件的预加载机制，利用主线程的空闲时间来提前构建和布局绘制组件，优化滑动体验。

## 布局与约束

Swiper作为一个容器组件，如果设置了自身尺寸属性，则在轮播显示过程中均以该尺寸生效。如果自身尺寸属性未被设置，则分两种情况：如果设置了[prevMargin](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-swiper#prevmargin10)或者[nextMargin](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-swiper#nextmargin10)属性，则Swiper自身尺寸会跟随其父组件；如果未设置prevMargin或者nextMargin属性，则会自动根据子组件的大小设置自身的尺寸。

## 循环播放

通过[loop](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-swiper#loop)属性控制是否循环播放，该属性默认值为true。

当loop为true时，在显示第一页或最后一页时，可以继续往前切换到前一页或者往后切换到后一页。如果loop为false，则在第一页或最后一页时，无法继续向前或者向后切换页面。

- loop为true

 收起自动换行深色代码主题复制

```
Swiper () { Text ( '0' ) . width ( '90%' ) . height ( '100%' ) . backgroundColor ( Color . Gray ) . textAlign ( TextAlign . Center ) . fontSize ( 30 ) Text ( '1' ) . width ( '90%' ) . height ( '100%' ) . backgroundColor ( Color . Green ) . textAlign ( TextAlign . Center ) . fontSize ( 30 ) Text ( '2' ) . width ( '90%' ) . height ( '100%' ) . backgroundColor ( Color . Pink ) . textAlign ( TextAlign . Center ) . fontSize ( 30 ) } // ··· . loop ( true )
```

[SwiperLoop.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/swiper/SwiperLoop.ets#L25-L52) 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165837.39982531944669779498957447454477:50001231000000:2800:A33E5A79884BA5E834B9145457FA0332413B3A563932D71072A4BF5266812E59.gif)

- loop为false

 收起自动换行深色代码主题复制

```
Swiper () { // ··· } // ··· . loop ( false )
```

[SwiperLoop.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/swiper/SwiperLoop.ets#L56-L85) 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165837.76891399779710454022872436048769:50001231000000:2800:FB670F626064FBACD2DBFB9DF74ED7B7A98C47B90883C0E7911C0829A92922A6.gif)

## 自动轮播

Swiper通过设置[autoPlay](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-swiper#autoplay)属性，控制是否自动轮播子组件。该属性默认值为false。

autoPlay为true时，会自动切换播放子组件，子组件与子组件之间的播放间隔通过interval属性设置。interval属性默认值为3000，单位毫秒。

 收起自动换行深色代码主题复制

```
Swiper () { // ··· } // ··· . loop ( true ) . autoPlay ( true ) . interval ( 1000 )
```

[SwiperAutoPlay.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/swiper/SwiperAutoPlay.ets#L25-L56) 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165837.64967009816162178740207296738309:50001231000000:2800:1064FB6AF4EC5C32EF2AAC62582AD1F30A54837E56D92A2E900677EEBCB6358D.gif)

## 导航点样式

Swiper提供了默认的导航点样式和导航点箭头样式，导航点默认显示在Swiper下方居中位置，开发者也可以通过[indicator](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-swiper#indicator)属性自定义导航点的位置和样式，导航点箭头默认不显示。

通过indicator属性，开发者可以设置导航点相对于Swiper组件上下左右四个方位的位置，同时也可以设置每个导航点的尺寸、颜色、蒙层和被选中导航点的颜色。

- 导航点使用默认样式

 收起自动换行深色代码主题复制

```
Swiper () { Text ( '0' ) . width ( '90%' ) . height ( '100%' ) . backgroundColor ( Color . Gray ) . textAlign ( TextAlign . Center ) . fontSize ( 30 ) Text ( '1' ) . width ( '90%' ) . height ( '100%' ) . backgroundColor ( Color . Green ) . textAlign ( TextAlign . Center ) . fontSize ( 30 ) Text ( '2' ) . width ( '90%' ) . height ( '100%' ) . backgroundColor ( Color . Pink ) . textAlign ( TextAlign . Center ) . fontSize ( 30 ) }
```

[SwiperIndicatorStyle.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/swiper/SwiperIndicatorStyle.ets#L26-L49) 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165837.28698503883412390651237770898327:50001231000000:2800:DCD7AC535766D558DF2B5DBA415732CF8F707F00390D33A4476EA12A22451161.png)

- 自定义导航点样式

选中的导航点，直径设为30vp，且颜色为蓝色；未选中的导航点，直径设为15vp，颜色设为红色。

 收起自动换行深色代码主题复制

```
Swiper () { // ··· } // ··· . indicator ( Indicator . dot () . left ( 0 ) . itemWidth ( 15 ) . itemHeight ( 15 ) . selectedItemWidth ( 30 ) . selectedItemHeight ( 15 ) . color ( Color . Red ) . selectedColor ( Color . Blue ) )
```

[SwiperIndicatorStyle.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/swiper/SwiperIndicatorStyle.ets#L54-L92) 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165838.32854130684732581248728641792251:50001231000000:2800:EEB117683D3BF433C30F48E58D4C9C9C20D7215FAB06403E7BB0E0DB8F383C81.png)

Swiper通过设置[displayArrow](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-swiper#displayarrow10)属性，可以控制导航点箭头的大小、位置、颜色，底板的大小及颜色，以及鼠标悬停时是否显示箭头。

- 箭头使用默认样式

 收起自动换行深色代码主题复制

```
Swiper () { // ··· } // ··· . displayArrow ( true , false )
```

[SwiperIndicatorStyle.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/swiper/SwiperIndicatorStyle.ets#L96-L125) 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165838.17295852750746383528685722422400:50001231000000:2800:12D787758772D52D173FB672D1DFD21FB7BBFFEC61C92FEF8D01E6E9BAFCD297.gif)

- 自定义箭头样式

箭头显示在组件两侧，大小为18vp，导航点箭头颜色设为蓝色。

 收起自动换行深色代码主题复制

```
Swiper () { // ··· } // ··· . displayArrow ({ showBackground : true , isSidebarMiddle : true , backgroundSize : 24 , backgroundColor : Color . White , arrowSize : 18 , arrowColor : Color . Blue }, false )
```

[SwiperIndicatorStyle.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/swiper/SwiperIndicatorStyle.ets#L129-L165) 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165838.95726219071342575559716584370135:50001231000000:2800:701BF7E2F55A58C9618890D111DBFF03AE2A0D7E419A8EFBB320B38A5D52CA32.gif)

## 页面切换方式

Swiper支持手指滑动、点击导航点和通过控制器三种方式切换页面，以下示例展示通过控制器切换页面的方法。

 收起自动换行深色代码主题复制

```
@Entry @Component export struct SwiperPageSwitchMethod { private swiperBackgroundColors : Color [] = [ Color . Blue , Color . Brown , Color . Gray , Color . Green , Color . Orange , Color . Pink , Color . Red , Color . Yellow ]; private swiperAnimationMode : ( SwiperAnimationMode | boolean | undefined )[] = [ undefined , true , false , SwiperAnimationMode . NO_ANIMATION , SwiperAnimationMode . DEFAULT_ANIMATION , SwiperAnimationMode . FAST_ANIMATION ]; private swiperController : SwiperController = new SwiperController (); private animationModeIndex : number = 0 ; private animationMode : ( SwiperAnimationMode | boolean | undefined ) = undefined ; @State animationModeStr : string = 'undefined' ; @State targetIndex : number = 0 ; aboutToAppear (): void { this . toSwiperAnimationModeStr (); } build ( ) { // ··· Column ({ space : 5 }) { Swiper ( this . swiperController ) { ForEach ( this . swiperBackgroundColors , ( backgroundColor: Color, index: number ) => { Text (index. toString ()) . width ( 250 ) . height ( 250 ) . backgroundColor (backgroundColor) . textAlign ( TextAlign . Center ) . fontSize ( 30 ) }) } // ··· . indicator ( true ) Row ({ space : 12 }) { Button ( 'showNext' ) . onClick ( () => { this . swiperController . showNext (); // 通过controller切换到后一页 }) Button ( 'showPrevious' ) . onClick ( () => { this . swiperController . showPrevious (); // 通过controller切换到前一页 }) }. margin ( 5 ) Row ({ space : 12 }) { Text ( 'Index:' ) Button ( this . targetIndex . toString ()) . onClick ( () => { this . targetIndex = ( this . targetIndex + 1 ) % this . swiperBackgroundColors . length ; }) }. margin ( 5 ) Row ({ space : 12 }) { Text ( 'AnimationMode:' ) Button ( this . animationModeStr ) . onClick ( () => { this . animationModeIndex = ( this . animationModeIndex + 1 ) % this . swiperAnimationMode . length ; this . toSwiperAnimationModeStr (); }) }. margin ( 5 ) Row ({ space : 12 }) { Button ( 'changeIndex(' + this . targetIndex + ', ' + this . animationModeStr + ')' ) . onClick ( () => { this . swiperController . changeIndex ( this . targetIndex , this . animationMode ); // 通过controller切换到指定页 }) }. margin ( 5 ) } // ··· } private toSwiperAnimationModeStr ( ) { this . animationMode = this . swiperAnimationMode [ this . animationModeIndex ]; if (( this . animationMode === true ) || ( this . animationMode === false )) { this . animationModeStr = '' + this . animationMode ; } else if (( this . animationMode === SwiperAnimationMode . NO_ANIMATION ) || ( this . animationMode === SwiperAnimationMode . DEFAULT_ANIMATION ) || ( this . animationMode === SwiperAnimationMode . FAST_ANIMATION )) { this . animationModeStr = SwiperAnimationMode [ this . animationMode ]; } else { this . animationModeStr = 'undefined' ; } } }
```

[SwiperPageSwitchMethod.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/swiper/SwiperPageSwitchMethod.ets#L18-L117) 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165838.93610462346730083732182232756516:50001231000000:2800:AD6C7660308731EA083E7CC3F23DF366277C3AEF05E0CEB988B0D4A4E6D87B7F.gif)

## 轮播方向

Swiper支持水平和垂直方向上进行轮播，主要通过[vertical](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-swiper#vertical)属性控制。

当vertical为true时，表示在垂直方向上进行轮播；为false时，表示在水平方向上进行轮播。vertical默认值为false。

- 设置水平方向上轮播。

 收起自动换行深色代码主题复制

```
Swiper ( // ··· ) { // ··· } // ··· . indicator ( true ) . vertical ( false )
```

[SwiperDirection.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/swiper/SwiperDirection.ets#L29-L63) 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165838.62693862649086801250782308452968:50001231000000:2800:DC3B45112B92725C91F046986DD399C752D51F76487CBCED96A71FB2DA29A1A3.png)

- 设置垂直方向轮播。

 收起自动换行深色代码主题复制

```
Swiper ( // ··· ) { // ··· } // ··· . indicator ( true ) . vertical ( true )
```

[SwiperDirection.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/swiper/SwiperDirection.ets#L80-L114) 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165838.01375274138593734225479673587449:50001231000000:2800:74978FB5341CB0044B021B664A4D4787FC2DF91BDA24E9E33C92C8D3855F3771.png)

## 每页显示多个子页面

Swiper支持在一个页面内同时显示多个子组件，通过[displayCount](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-swiper#displaycount8)属性设置。

 收起自动换行深色代码主题复制

```
Swiper () { Text ( '0' ) . width ( 250 ) . height ( 250 ) . backgroundColor ( Color . Gray ) . textAlign ( TextAlign . Center ) . fontSize ( 30 ) Text ( '1' ) . width ( 250 ) . height ( 250 ) . backgroundColor ( Color . Green ) . textAlign ( TextAlign . Center ) . fontSize ( 30 ) Text ( '2' ) . width ( 250 ) . height ( 250 ) . backgroundColor ( Color . Pink ) . textAlign ( TextAlign . Center ) . fontSize ( 30 ) Text ( '3' ) . width ( 250 ) . height ( 250 ) . backgroundColor ( Color . Yellow ) . textAlign ( TextAlign . Center ) . fontSize ( 30 ) } // ··· . indicator ( true ) . displayCount ( 2 ) }
```

[SwiperMultiPage.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/swiper/SwiperMultiPage.ets#L25-L58) 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165838.50929122083652703706889730070765:50001231000000:2800:F19A92104D289A392D1C80B34192CE40723FF5980CFC2351AAF97C6B53380CEC.png)

## 自定义切换动画

Swiper支持通过[customContentTransition](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-swiper#customcontenttransition12)设置自定义切换动画，可以在回调中对视窗内所有页面逐帧设置透明度、缩放比例、位移、渲染层级等属性实现自定义切换动画。

 收起自动换行深色代码主题复制

```
```

[SwiperCustomAnimation.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/swiper/SwiperCustomAnimation.ets#L18-L107) 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165838.72837854648826923433724570116026:50001231000000:2800:15FE5915ACC44896E7C4EBDA74A9EA818AACBD673B39CAF965359232DD697473.gif)

## Swiper与Tabs联动

Swiper选中的元素改变时，会通过[onSelected](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-swiper#onselected18)回调事件，将元素的索引值index返回。通过调用[tabsController.changeIndex(index)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-tabs#changeindex)方法来实现Tabs页签的切换。

 收起自动换行深色代码主题复制

```
// xxx.ets class MyDataSource implements IDataSource { private list : number [] = []; constructor ( list: number [] ) { this . list = list; } totalCount (): number { return this . list . length ; } getData ( index : number ): number { return this . list [index]; } registerDataChangeListener ( listener : DataChangeListener ): void { } unregisterDataChangeListener ( ) { } } @Entry @Component export struct SwiperAndTabsLinkage { @State fontColor : string = '#182431' ; @State selectedFontColor : string = '#007DFF' ; @State currentIndex : number = 0 ; private list : number [] = []; private tabsController : TabsController = new TabsController (); private swiperController : SwiperController = new SwiperController (); private swiperData : MyDataSource = new MyDataSource ([]); private context = this . getUIContext (). getHostContext () as common. UIAbilityContext ; aboutToAppear (): void { for ( let i = 0 ; i <= 9 ; i++) { this . list . push (i); } this . swiperData = new MyDataSource ( this . list ); } @Builder tabBuilder ( index: number , name: string ) { Column () { Text (name) . fontColor ( this . currentIndex === index ? this . selectedFontColor : this . fontColor ) . fontSize ( 16 ) . fontWeight ( this . currentIndex === index ? 500 : 400 ) . lineHeight ( 22 ) . margin ({ top : 17 , bottom : 7 }) Divider () . strokeWidth ( 2 ) . color ( '#007DFF' ) . opacity ( this . currentIndex === index ? 1 : 0 ) }. width ( '20%' ) } build ( ) { // ... Column () { Tabs ({ barPosition : BarPosition . Start , controller : this . tabsController }) { ForEach ( this . list , ( index: number ) => { // 请在resources\base\element\string.json文件中配置name为'swiper_text1' ，value为非空字符串的资源 TabContent (). tabBar ( this . tabBuilder (index, this . context . resourceManager . getStringByNameSync ( 'swiper_text1' ) + this . list [index])) }) } . onTabBarClick ( ( index: number ) => { this . currentIndex = index; this . swiperController . changeIndex (index, true ); }) . barMode ( BarMode . Scrollable ) . backgroundColor ( '#F1F3F5' ) . height ( 56 ) . width ( '100%' ) Swiper ( this . swiperController ) { LazyForEach ( this . swiperData , ( item: string ) => { Text (item. toString ()) . onAppear ( ()=> { console . info ( 'onAppear ' + item. toString ()); }) . onDisAppear ( ()=> { console . info ( 'onDisAppear ' + item. toString ()); }) . width ( '100%' ) . height ( '40%' ) . backgroundColor ( 0xAFEEEE ) . textAlign ( TextAlign . Center ) . fontSize ( 30 ) }, ( item: string ) => item) } . loop ( false ) . onSelected ( ( index: number ) => { console . info ( 'onSelected:' + index); this . currentIndex = index; this . tabsController . changeIndex (index); }) } // ... } }
```

[SwiperAndTabsLinkage.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/swiper/SwiperAndTabsLinkage.ets#L18-L131) 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165838.79845804032263260881069299545614:50001231000000:2800:34289BFDC57E3B04D0FB07A97E3938156F1034CD5CC60EE8578C9F22960A9246.gif)

## 设置圆点导航点间距

针对圆点导航点，可以通过DotIndicator的[space](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-swiper#space19)属性来设置圆点导航点的间距。

 收起自动换行深色代码主题复制

```
Swiper ( // ··· ) { // ··· } . indicator ( new DotIndicator () . space ( this . space ) // ··· )
```

[SwiperIgnoreComponentSize.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/swiper/SwiperIgnoreComponentSize.ets#L76-L115)   

## 导航点忽略组件大小

当导航点的[bottom](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-swiper#bottom)设为0之后，导航点的底部与Swiper的底部还会有一定间距。如果希望消除该间距，可通过调用bottom(bottom, ignoreSize)属性来进行设置。将ignoreSize设置为true，即可忽略导航点组件大小，达到消除该间距的目的。

- 圆点导航点忽略组件大小。

 收起自动换行深色代码主题复制

```
Swiper ( // ··· ) { // ··· } . indicator ( new DotIndicator () // ··· . bottom ( LengthMetrics . vp ( 0 ), this . ignoreSize ) // true // ··· )
```

[SwiperIgnoreComponentSize.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/swiper/SwiperIgnoreComponentSize.ets#L77-L114) 

- 数字导航点忽略组件大小。

 收起自动换行深色代码主题复制

```
Swiper ( // ··· ) { // ··· } . indicator ( new DigitIndicator () . bottom ( LengthMetrics . vp ( 0 ), true ) )
```

[SwiperDigitIndicatorIgnoreComponentSize.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/swiper/SwiperDigitIndicatorIgnoreComponentSize.ets#L62-L83) 

圆点导航点设置间距及忽略组件大小完整示例代码如下：

 收起自动换行深色代码主题复制

```
```

[SwiperIgnoreComponentSize.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/swiper/SwiperIgnoreComponentSize.ets#L16-L150) 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165838.91885408798384211258835401748519:50001231000000:2800:FD8A83646C2D53647C88185FF75BCAD49B491457B4585BE7DB1E54074D70856F.gif)

## 保持可见内容位置不变

Swiper通过设置[maintainVisibleContentPosition](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-swiper#maintainvisiblecontentposition20)属性，可在使用LazyForEach懒加载数据时（如通过onDataAdd新增数据），保持当前可见内容位置不变，避免因数据增删导致的视图跳动。该属性默认值为false。

maintainVisibleContentPosition为true时，显示区域上方或前方插入或删除数据时可见内容位置不变。

关于数据[LazyForEach：数据懒加载](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-rendering-control-lazyforeach)的具体使用，可参考数据懒加载章节中的示例。

 收起自动换行深色代码主题复制

```
// xxx.ets class MyDataSource implements IDataSource { private listeners : DataChangeListener [] = []; private dataArray : string [] = [ '0' , '1' , '2' , '3' , '4' , '5' , '6' ]; public totalCount (): number { return this . dataArray . length ; } public getData ( index : number ): string | undefined { return this . dataArray [index]; } public addData ( index : number , data : string ): void { this . dataArray . splice (index, 0 , data); this . listeners . forEach ( listener => { listener. onDataAdd (index); }) } public deleteData ( index : number ): void { this . dataArray . splice (index, 1 ); this . listeners . forEach ( listener => { listener. onDataDelete (index); }) } registerDataChangeListener ( listener : DataChangeListener ): void { if ( this . listeners . indexOf (listener) < 0 ) { hilog. info ( DOMAIN , 'testTag' , 'add listener' ); this . listeners . push (listener); } } unregisterDataChangeListener ( listener : DataChangeListener ): void { const pos = this . listeners . indexOf (listener); if (pos >= 0 ) { hilog. info ( DOMAIN , 'testTag' , 'remove listener' ); this . listeners . splice (pos, 1 ); } } } @Entry @Component export struct SwiperVisibleContentPosition { private data : MyDataSource = new MyDataSource (); @State index : number = 3 ; build ( ) { // ... Column ({ space : 12 }) { // ... Swiper () { LazyForEach ( this . data , ( item: string ) => { Text (item. toString ()) . width ( '90%' ) . height ( 160 ) . backgroundColor ( 0xAFEEEE ) . textAlign ( TextAlign . Center ) . fontSize ( 30 ) }) } . onChange ( ( index ) => { this . index = index; }) . index ( 3 ) . maintainVisibleContentPosition ( true ) // ... Column ({ space : 12 }) { Text ( 'index:' + this . index ). fontSize ( 20 ) Row () { // 在LazyForEach索引为0的位置添加数据 Button ( 'header data add' ). height ( 30 ). onClick ( () => { this . data . addData ( 0 , 'header Data' ); }) // 删除LazyForEach索引为0的位置数据 Button ( 'header data delete' ). height ( 30 ). onClick ( () => { this . data . deleteData ( 0 ); }) } }. margin ( 5 ) // ... }. width ( '100%' ) . margin ({ top : 5 }) // ... } }
```

[SwiperVisibleContentPosition.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/swiper/SwiperVisibleContentPosition.ets#L21-L134) 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165838.04281184867584125620500504261131:50001231000000:2800:820886E3655ABDF13894319FA73890DD2D304F78AF56DC1AA3D57D3787063B31.gif)

## 示例代码

- [短视频切换](https://gitcode.com/HarmonyOS_Samples/short-video)