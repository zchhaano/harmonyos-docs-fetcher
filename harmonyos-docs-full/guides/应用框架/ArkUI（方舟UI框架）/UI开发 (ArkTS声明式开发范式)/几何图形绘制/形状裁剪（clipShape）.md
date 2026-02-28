# 形状裁剪（clipShape）

可利用[clipShape](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-sharp-clipping#clipshape12)接口将组件裁剪为所需的形状。调用该接口后，可以保留该形状覆盖的组件部分，同时移除组件的其余部分。裁剪形状本身是不可见的。

 说明 

不同的形状支持的属性范围不同，路径是一种形状，除此之外还有椭圆、矩形等形状。

路径的形状不支持设置宽度和高度，具体形状支持的属性参考具体[形状](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-shape)的文档。

形状中的[fill](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-shape#fill)属性对clipShape接口不生效。

## 裁剪圆形

通过设置CircleShape，将图片裁剪为圆形。

 收起自动换行深色代码主题复制

```
// xxx.ets import { CircleShape } from '@kit.ArkUI' ; @Entry @Component struct ClipShapeExample { build ( ) { Column ({ space : 15 }) { // 用一个280px直径的圆对图片进行裁剪 // 请将$r('app.media.background')替换为实际资源文件 Image ($r( 'app.media.background' )) . clipShape ( new CircleShape ({ width : '280px' , height : '280px' })) . width ( '500px' ). height ( '280px' ) // 用一个350px直径的圆对图片进行裁剪 // 请将$r('app.media.background')替换为实际资源文件 Image ($r( 'app.media.background' )) . clipShape ( new CircleShape ({ width : '350px' , height : '350px' })) . width ( '500px' ). height ( '370px' ) } . width ( '100%' ) . margin ({ top : 15 }) } }
```

[ClipShapeExample1.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/ClipShape/entry/src/main/ets/View/ClipShapeExample1.ets#L15-L38) 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165839.82718475782765206989543660562174:50001231000000:2800:F0A56B5C6A886053347E5A0C5A7B2CCA25BEFD9102536B864FA54740D4AAE167.png)

## 裁剪椭圆形

通过设置EllipseShape，将图片裁剪为椭圆形。

 收起自动换行深色代码主题复制

```
// xxx.ets import { EllipseShape } from '@kit.ArkUI' ; @Entry @Component struct ClipShapeExample { build ( ) { Column ({ space : 15 }) { // 请将$r('app.media.background')替换为实际资源文件 Image ($r( 'app.media.background' )) . clipShape ( new EllipseShape ({ width : '280px' , height : '200px' })) . width ( '500px' ). height ( '400px' ) // 请将$r('app.media.background')替换为实际资源文件 Image ($r( 'app.media.background' )) . clipShape ( new EllipseShape ({ width : '380px' , height : '280px' })) . width ( '500px' ). height ( '400px' ) } . width ( '100%' ) . margin ({ top : 15 }) } }
```

[ClipShapeExample2.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/ClipShape/entry/src/main/ets/View/ClipShapeExample2.ets#L15-L36) 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165839.40617623143102778969309920365211:50001231000000:2800:1678FB1C637CB4E4F3A8F3E150476D57A17662E4E70B63D85CC3A6B309D5041D.png)

## 裁剪矩形

通过设置RectShape，将图片裁剪为矩形。

 收起自动换行深色代码主题复制

```
// xxx.ets import { RectShape } from '@kit.ArkUI' ; @Entry @Component struct ClipShapeExample { build ( ) { Column ({ space : 15 }) { // 请将$r('app.media.background')替换为实际资源文件 Image ($r( 'app.media.background' )) . clipShape ( new RectShape ({ width : '200px' , height : '200px' })) . width ( '500px' ). height ( '400px' ) // 请将$r('app.media.background')替换为实际资源文件 Image ($r( 'app.media.background' )) . clipShape ( new RectShape ({ width : '380px' , height : '280px' })) . width ( '500px' ). height ( '400px' ) } . width ( '100%' ) . margin ({ top : 15 }) } }
```

[ClipShapeExample3.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/ClipShape/entry/src/main/ets/View/ClipShapeExample3.ets#L15-L36) 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165839.89545305094035661784737934787065:50001231000000:2800:9732F85C98E13789AAFE5197BF8CE38D5698A237822734214D5CFB4A9F13DFD9.png)

## 裁剪不规则形状

通过设置PathShape，将图片裁剪为不规则形状。

 收起自动换行深色代码主题复制

```
// xxx.ets import { PathShape } from '@kit.ArkUI' ; @Entry @Component struct ClipShapeExample { build ( ) { Column ({ space : 15 }) { Row () { // 请将$r('app.media.background')替换为实际资源文件 Image ($r( 'app.media.background' )) . clipShape ( new PathShape ({ commands : 'M0 0 H400 V200 H0 Z' })) . width ( '500px' ). height ( '300px' ) } . clip ( true ) . borderRadius ( 20 ) } . width ( '100%' ) . margin ({ top : 15 }) } }
```

[ClipShapeExample4.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/ClipShape/entry/src/main/ets/View/ClipShapeExample4.ets#L15-L36) 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165839.35472590273051251551330637456073:50001231000000:2800:330F818A093AFC2D686DED73C7353ADB455C757B00EEC42EFD5FE64F6E1D2E2E.png)