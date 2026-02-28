# AnimateTo使用迁移

在状态管理从V1迁移至V2的过程中，[animateTo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#animateto)执行动画前如需修改状态变量，可参考本文档的适配方案。

## 执行动画前重新定义初始态场景

**V1实现代码如下：**

 收起自动换行深色代码主题复制

```
@Entry @Component struct Index { @State w : number = 50 ; // 宽度 @State h : number = 50 ; // 高度 @State message : string = 'Hello' ; build ( ) { Column () { Button ( 'change size' ) . margin ( 20 ) . onClick ( () => { // 在执行动画前，存在额外的修改 this . w = 100 ; this . h = 100 ; this . message = 'Hello World' ; this . getUIContext (). animateTo ({ duration : 1000 }, () => { this . w = 200 ; this . h = 200 ; this . message = 'Hello ArkUI' ; }) }) Column () { Text ( ` ${ this .message} ` ) } . backgroundColor ( '#ff17a98d' ) . width ( this . w ) . height ( this . h ) } } }
```

预期动画效果：绿色矩形从长宽100变为200，字符串从Hello World变为Hello ArkUI。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170015.29775753023635561496949704540318:50001231000000:2800:BACEF79F85BCC4AF2455FA551F89F1A4834A7A9754266FD67AD8C5F43A059C05.gif)

**V1迁移V2**

 收起自动换行深色代码主题复制

```
@Entry @ComponentV2 struct Index { @Local w : number = 50 ; // 宽度 @Local h : number = 50 ; // 高度 @Local message : string = 'Hello' ; build ( ) { Column () { Button ( 'change size' ) . margin ( 20 ) . onClick ( () => { // 在执行动画前，存在额外的修改 this . w = 100 ; this . h = 100 ; this . message = 'Hello World' ; this . getUIContext (). animateTo ({ duration : 1000 }, () => { this . w = 200 ; this . h = 200 ; this . message = 'Hello ArkUI' ; }) }) Column () { Text ( ` ${ this .message} ` ) } . backgroundColor ( '#ff17a98d' ) . width ( this . w ) . height ( this . h ) } } }
```

[LocalQuestionV2animateTo.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/local/LocalQuestionV2animateTo.ets#L29-L63) 

由于当前animateTo与V2的刷新机制不兼容，执行动画前的额外修改未生效，实际显示的动画效果如下图所示：绿色矩形从长宽50变为200，字符串从Hello变为Hello ArkUI。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170015.85150039052498533009122977636237:50001231000000:2800:9E4D7F6C4878DD26DB0183E0130537951422E27EF0BFE41DA08F09FC71054C35.gif)

## 迁移方案

### API version 22之前的迁移方案

从API version 22之前，可以使用一个duration为0的[animateToImmediately](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-explicit-animatetoimmediately#animatetoimmediately)将额外的修改先刷新，再执行原来的动画达成预期的效果。

完整代码如下：

 收起自动换行深色代码主题复制

```
@Entry @ComponentV2 struct Index { @Local w : number = 50 ; // 宽度 @Local h : number = 50 ; // 高度 @Local message : string = 'Hello' ; build ( ) { Column () { Button ( 'change size' ) . margin ( 20 ) . onClick ( () => { // 在执行动画前，存在额外的修改 this . w = 100 ; this . h = 100 ; this . message = 'Hello World' ; animateToImmediately ({ duration : 0 }, () => { }) this . getUIContext (). animateTo ({ duration : 1000 }, () => { this . w = 200 ; this . h = 200 ; this . message = 'Hello ArkUI' ; }) }) Column () { Text ( ` ${ this .message} ` ) } . backgroundColor ( '#ff17a98d' ) . width ( this . w ) . height ( this . h ) } } }
```

### API version 22及以后的迁移方案

从API version 22开始，可以使用[applySync接口](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-applysync-flushupdates-flushuiupdates)实现预期的显示效果。

原理为使用applySync接口同步刷新闭包函数内的状态变量变化，再执行原来的动画达成预期的效果。

 收起自动换行深色代码主题复制

```
import { UIUtils } from '@kit.ArkUI' ; @Entry @ComponentV2 struct Index { @Local w : number = 50 ; // 宽度 @Local h : number = 50 ; // 高度 @Local message : string = 'Hello' ; build ( ) { Column () { Button ( 'change size' ) . margin ( 20 ) . onClick ( () => { // 在执行动画前，存在额外的修改 UIUtils . applySync ( () => { this . w = 100 ; this . h = 100 ; this . message = 'Hello World' ; }) this . getUIContext (). animateTo ({ duration : 1000 }, () => { this . w = 200 ; this . h = 200 ; this . message = 'Hello ArkUI' ; }) }) Column () { Text ( ` ${ this .message} ` ) } . backgroundColor ( '#ff17a98d' ) . width ( this . w ) . height ( this . h ) } } }
```

[LocalQuestionExpectedEffect.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/local/LocalQuestionExpectedEffect.ets#L15-L53)