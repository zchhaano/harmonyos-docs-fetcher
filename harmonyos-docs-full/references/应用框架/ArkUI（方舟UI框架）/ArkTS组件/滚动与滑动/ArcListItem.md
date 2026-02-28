# ArcListItem

用来展示列表具体子组件，必须配合[ArcList](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-arclist)来使用。

 说明 

- 该组件从API version 18开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
- 该组件的父组件只能是[ArcList](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-arclist)。
- 当ArcListItem配合[LazyForEach](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-rendering-control-lazyforeach)使用时，ArcListItem子组件在ArcListItem创建时创建。配合[if/else](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-rendering-control-ifelse)、[ForEach](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-rendering-control-foreach)使用时，或父组件为[ArcList](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-arclist)时，ArcListItem子组件在ArcListItem布局时创建。

## 导入模块

 支持设备Wearable说明 

- ArcListItemAttribute是用于配置ArcListItem组件属性的关键接口。API version 21及之前版本，导入ArcListItem组件后需要开发者手动导入ArcListItemAttribute，否则会编译报错。从API version 22开始，编译工具链识别到导入ArcListItem组件后，会自动导入ArcListItemAttribute，无需开发者手动导入ArcListItemAttribute。
- 如果开发者手动导入ArcListItemAttribute，DevEco Studio会显示置灰，API version 21及之前版本删除会编译报错，从API version 22开始，删除对功能无影响。

API version 21及之前版本：

 收起自动换行深色代码主题复制

```
import { ArcListItem , ArcListItemAttribute } from '@kit.ArkUI' ;
```

API version 22及之后版本：

 收起自动换行深色代码主题复制

```
import { ArcListItem } from '@kit.ArkUI' ;
```

## 子组件

 支持设备Wearable

可以包含单个子组件。

## 接口

 支持设备Wearable

ArcListItem()

创建弧形列表子组件。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

## 属性

 支持设备Wearable

除支持[通用属性](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-component-general-attributes)外，还支持以下属性：

### autoScale

 支持设备Wearable

autoScale(enable: Optional<boolean>)

用于设置ArcListItem是否支持自动缩放显示。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | Optional <boolean> | 是 | ArcListItem是否支持自动缩放显示，true表示支持自动缩放显示，false表示不支持自动缩放显示。 默认值：true，支持自动缩放显示。 |

### swipeAction

 支持设备Wearable

swipeAction(options: Optional<SwipeActionOptions>)

用于设置ArcListItem的划出组件。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | Optional < SwipeActionOptions > | 是 | ArcListItem的划出组件。 |

## 示例

 支持设备Wearable

该示例展示了子项关闭自动缩放和开启自动缩放后的对比效果。

 收起自动换行深色代码主题复制

```
// xxx.ets import { LengthMetrics , CircleShape } from '@kit.ArkUI' ; // 从API version 22开始，无需手动导入ArcListAttribute和ArcListItemAttribute。具体请参考ArcList、ArcListItem的导入模块说明。 import { ArcList , ArcListItem , ArcListAttribute , ArcListItemAttribute } from '@kit.ArkUI' ; @Entry @Component struct ArcListItemExample { private arr : number [] = [ 0 , 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 ]; private watchSize : string = '466px' ; // 手表默认宽高：466*466 private itemSize : string = '414px' ; // item宽度 @Builder buildList ( ) { Stack () { Column () { } . width ( this . watchSize ) . height ( this . watchSize ) . clipShape ( new CircleShape ({ width : '100%' , height : '100%' })) . backgroundColor ( 0x707070 ) ArcList ({ initialIndex : 3 }) { ForEach ( this . arr , ( item: number ) => { ArcListItem () { Button ( '' + item, { type : ButtonType . Capsule }) . width ( this . itemSize ) . height ( '70px' ) . fontSize ( '40px' ) . backgroundColor ( 0x17A98D ) } . autoScale (item % 3 == 0 || item % 5 == 0 ) }, ( item: number ) => item. toString ()) } . space ( LengthMetrics . px ( 10 )) . borderRadius ( this . watchSize ) } . width ( this . watchSize ) . height ( this . watchSize ) } build ( ) { Column () { this . buildList (); } . width ( '100%' ) . height ( '100%' ) . alignItems ( HorizontalAlign . Center ) . justifyContent ( FlexAlign . Center ) } }
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170553.16464445662709827457915594734521:50001231000000:2800:FA6229979DC66C30D98FC5343F76C88F3FB9B64AB8C7CDBCE6DE6FFB1348B948.png)