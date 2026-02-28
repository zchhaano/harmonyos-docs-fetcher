# 创建弧形轮播 (ArcSwiper)（圆形屏幕推荐使用）

ArcSwiper是弧形轮播组件，在圆形屏幕场景下使用，提供弧形轮播显示能力。具体用法请参考[ArcSwiper](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-arcswiper)。

在使用ArcSwiper组件之前，需要在代码中先导入ArcSwiper模块。

 收起自动换行深色代码主题复制

```
import { ArcSwiper , ArcSwiperAttribute , ArcDotIndicator , ArcDirection , ArcSwiperController } from '@kit.ArkUI' ;
```

[ArcSwiperStyles.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/arcSwiper/ArcSwiperStyles.ets#L16-L24)  

## 设置导航点样式

ArcSwiper提供了默认的弧形导航点样式，导航点默认显示在ArcSwiper下方居中位置，开发者也可以通过[indicator](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-arcswiper#indicator)属性自定义弧形导航点的样式。

通过indicator属性，开发者可以设置弧形导航点的方向，同时也可以设置导航点和被选中导航点的颜色。

- 导航点使用默认样式

 收起自动换行深色代码主题复制

```
ArcSwiper () { Text ( '0' ) . width ( 233 ) . height ( 233 ) . backgroundColor ( Color . Gray ) . textAlign ( TextAlign . Center ) . fontSize ( 30 ) Text ( '1' ) . width ( 233 ) . height ( 233 ) . backgroundColor ( Color . Green ) . textAlign ( TextAlign . Center ) . fontSize ( 30 ) Text ( '2' ) . width ( 233 ) . height ( 233 ) . backgroundColor ( Color . Pink ) . textAlign ( TextAlign . Center ) . fontSize ( 30 ) }
```

[ArcSwiperStyles.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/arcSwiper/ArcSwiperStyles.ets#L36-L59) 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165846.13185171826594012515281650871468:50001231000000:2800:C02FC92666AEA3239E8546BEEA933D6037C6425BB14F6BABF69A3537DE9EAC7D.png)
- 自定义导航点样式

导航点位于ArcSwiper组件6点钟方向，导航点颜色设为红色，被选中导航点颜色为蓝色。

 收起自动换行深色代码主题复制

```
ArcSwiper () { // ··· } . indicator ( new ArcDotIndicator () . arcDirection ( ArcDirection . SIX_CLOCK_DIRECTION ) // 设置导航点位于6点钟方向 . itemColor ( Color . Red ) // 设置导航点颜色为红色 . selectedItemColor ( Color . Blue ) // 设置选中导航点颜色为蓝色 )
```

[ArcSwiperStyles.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/arcSwiper/ArcSwiperStyles.ets#L63-L94) 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165846.68254181491620458518040613637161:50001231000000:2800:454B54A074D0AB05E7FE9515E4EDC0787580D2878FE43885702086B69DE38467.png)

## 控制页面切换方式

ArcSwiper支持滑动手指、点击导航点、旋转表冠和控制控制器四种方式切换页面。以下示例展示通过控制控制器和旋转表冠翻页的方法。

- 控制控制器翻页。

 收起自动换行深色代码主题复制

```
// 导入ArcButton和ArcSwiper模块 import { ArcButton , ArcButtonOptions , ArcButtonStatus , ArcButtonStyleMode , ArcButtonPosition , ArcSwiper , ArcSwiperAttribute , // ArcSwiper的属性依赖ArcSwiperAttribute对象导入，不建议删除该对象的引入。 ArcSwiperController , // ··· } from '@kit.ArkUI' ; // ··· @Entry @Component export struct ArcSwiperToggle { private wearableSwiperController : ArcSwiperController = new ArcSwiperController (); build ( ) { // ··· Column ({ space : 12 }) { // ··· Stack () { ArcSwiper ( this . wearableSwiperController ) { // ··· } . vertical ( true ) . indicator ( false ) // ··· Column () { ArcButton ({ options : new ArcButtonOptions ({ label : 'previous' , position : ArcButtonPosition . TOP_EDGE , styleMode : ArcButtonStyleMode . EMPHASIZED_LIGHT , onClick : () => { this . wearableSwiperController . showPrevious (); // 通过controller切换到前一页 } }) }) Blank () ArcButton ({ options : new ArcButtonOptions ({ label : 'next' , position : ArcButtonPosition . BOTTOM_EDGE , styleMode : ArcButtonStyleMode . EMPHASIZED_LIGHT , onClick : () => { this . wearableSwiperController . showNext (); // 通过controller切换到后一页 } }) }) }. width ( '100%' ). height ( '100%' ) } // ··· } // ··· } }
```

[ArcSwiperToggle.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/arcSwiper/ArcSwiperToggle.ets#L16-L143) 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165846.72806827378596687716399478296861:50001231000000:2800:7A61CDC28F80CAE6469EC7E8CD6D39F3F5A7B70D0FFB4A20FF0ABDD4E4F9E6F0.gif)
- 旋转表冠翻页。

ArcSwiper在获得焦点时能够响应旋转表冠的操作，用户可以通过旋转表冠来滑动ArcSwiper，从而浏览数据。

 收起自动换行深色代码主题复制

```
ArcSwiper ( // ··· ) { // ··· } // ··· . focusable ( true ) . focusOnTouch ( true ) . defaultFocus ( true )
```

[ArcSwiperToggle.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/arcSwiper/ArcSwiperToggle.ets#L50-L96) 

还可以通过设置[digitalCrownSensitivity](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-arcswiper#digitalcrownsensitivity)属性来调整表冠对事件响应的灵敏度，以适应不同规模的数据处理。在处理大量数据时，可以提高响应事件的灵敏度；而在处理少量数据时，则可以降低灵敏度设置。

 收起自动换行深色代码主题复制

```
ArcSwiper ( // ··· ) { // ··· } // ··· . digitalCrownSensitivity ( CrownSensitivity . MEDIUM )
```

[ArcSwiperToggle.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/arcSwiper/ArcSwiperToggle.ets#L49-L100)

## 设置轮播方向

ArcSwiper支持水平和垂直方向上进行轮播，主要通过[vertical](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-arcswiper#vertical)属性控制。

当vertical为true时，表示在垂直方向上进行轮播；为false时，表示在水平方向上进行轮播。vertical默认值为false。

- 设置水平方向上轮播。

 收起自动换行深色代码主题复制

```
ArcSwiper () { // ··· } . indicator ( true ) . vertical ( false )
```

[ArcSwiperHorizontal.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/arcSwiper/ArcSwiperHorizontal.ets#L31-L58) 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165846.10102088409208983636511004643469:50001231000000:2800:2F398204452911141E8DFA50D67E218BEA6C48028A3D482E86973173447489AA.png)
- 设置垂直方向轮播，导航点设为3点钟方向。

 收起自动换行深色代码主题复制

```
ArcSwiper () { // ··· } . indicator ( new ArcDotIndicator () . arcDirection ( ArcDirection . THREE_CLOCK_DIRECTION )) . vertical ( true )
```

[ArcSwiperVertical.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/arcSwiper/ArcSwiperVertical.ets#L34-L62) 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165846.50749740370764361730293067399055:50001231000000:2800:D9A6C99AF5437665D37DF7D1FC5127A0E3B9D1AEBCD5CB7FD32FB3F91C00B43F.png)

## 自定义切换动画

ArcSwiper支持通过[customContentTransition](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-arcswiper#customcontenttransition)设置自定义切换动画，可以在回调中对视窗内所有页面逐帧设置透明度、缩放比例、位移、渲染层级等属性，从而实现自定义切换动画效果。

 收起自动换行深色代码主题复制

```
```

[ArcSwiperAction.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/arcSwiper/ArcSwiperAction.ets#L16-L93) 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165846.78990720592950186055516959129034:50001231000000:2800:CC7CC5D8299C498B1B187DE0940E5A48F4BC713AEE49A9E845A24BC8E4A770A8.gif)

## 实现侧滑返回

ArcSwiper的滑动事件会与侧滑返回冲突，可以通过[onGestureRecognizerJudgeBegin](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-gesture-blocking-enhancement#ongesturerecognizerjudgebegin)去判断ArcSwiper是否滑动到开头去拦截ArcSwiper的滑动手势，实现再次左滑返回上一页的功能。

 收起自动换行深色代码主题复制

```
import { ArcSwiper , ArcSwiperAttribute , // ArcSwiper的属性依赖ArcSwiperAttribute对象导入，不建议删除该对象的引入。 ArcDotIndicator , ArcDirection , ArcSwiperController } from '@kit.ArkUI' ; // ··· @Entry @Component export struct ArcSwiperSideSlip { @State backgroundColors : Color [] = [ Color . Green , Color . Blue , Color . Yellow , Color . Pink , Color . Gray , Color . Orange ]; innerSelectedIndex : number = 0 ; build ( ) { // ··· Column ({ space : 12 }) { // ··· ArcSwiper () { ForEach ( this . backgroundColors , ( backgroundColor: Color, index: number ) => { Text (index. toString ()) . width ( 233 ) . height ( 233 ) . fontSize ( 50 ) . textAlign ( TextAlign . Center ) . backgroundColor (backgroundColor) }) } . onAnimationStart ( ( index: number , targetIndex: number ) => { this . innerSelectedIndex = targetIndex; }) . onGestureRecognizerJudgeBegin (( event : BaseGestureEvent , current : GestureRecognizer , others : Array < GestureRecognizer >): GestureJudgeResult => { // 在识别器即将要成功时，根据当前组件状态，设置识别器使能状态 if (current) { let target = current. getEventTargetInfo (); if (target && current. isBuiltIn () && current. getType () == GestureControl . GestureType . PAN_GESTURE ) { let swiperTarget = target as ScrollableTargetInfo ; if (swiperTarget instanceof ScrollableTargetInfo && (swiperTarget. isBegin () || this . innerSelectedIndex === 0 )) { // 此处判断swiperTarget.isBegin()或innerSelectedIndex === 0，表明ArcSwiper滑动到开头 let panEvent = event as PanGestureEvent ; if (panEvent && panEvent. offsetX > 0 && (swiperTarget. isBegin () || this . innerSelectedIndex === 0 )) { return GestureJudgeResult . REJECT ; } } } } return GestureJudgeResult . CONTINUE ; }) // ··· } . width ( '100%' ) // ··· } }
```

[ArcSwiperSideSlip.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/arcSwiper/ArcSwiperSideSlip.ets#L16-L86) 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165846.39375017219354544084700999298014:50001231000000:2800:ECBA55EDB59E975F4183D9128F7694C8A949E499221CD9B412418F8F2826F953.gif)