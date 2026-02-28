# LoadingProgress

用于显示加载动效的组件。

加载动效在组件不可见时停止，组件的可见状态基于[onVisibleAreaChange](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-component-visible-area-change-event#onvisibleareachange)处理，可见阈值ratios大于0即视为可见状态。

 说明 

该组件从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## 子组件

支持设备PhonePC/2in1TabletTVWearable

无

## 接口

支持设备PhonePC/2in1TabletTVWearable

LoadingProgress()

创建加载进度组件。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 属性

支持设备PhonePC/2in1TabletTVWearable

除支持[通用属性](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-component-general-attributes)外，还支持以下属性：

 说明 

组件应设置合理的宽高，当组件宽高设置过大时加载动效可能不符合预期效果。

### color

支持设备PhonePC/2in1TabletTVWearable

color(value: ResourceColor)

设置加载进度条前景色。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

 展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | ResourceColor | 是 | 加载进度条的前景色。 默认值： API version 10及以下：'#99666666' API version 11及以上：'#ff666666' |

### enableLoading 10+

支持设备PhonePC/2in1TabletTVWearable

enableLoading(value: boolean)

设置LoadingProgress动画是否显示。LoadingProgress动画不显示时，该组件依旧占位。通用属性[Visibility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-appendix-enums#visibility).Hidden隐藏的是包括[border](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-border#border)、[padding](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-size#padding)等整个组件范围，而enableLoading=false只隐藏LoadingProgress本身动画内容，不包括border等。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

 展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | LoadingProgress动画是否显示。 默认值：true，true表示显示LoadingProgress动画，false表示不显示LoadingProgress动画。 |

### contentModifier 12+

支持设备PhonePC/2in1TabletTVWearable

contentModifier(modifier: ContentModifier<LoadingProgressConfiguration>)

定制LoadingProgress内容区的方法。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

 展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| modifier | ContentModifier<LoadingProgressConfiguration> | 是 | 在LoadingProgress组件上，定制内容区的方法。 modifier： 内容修改器，开发者需要自定义class实现ContentModifier接口。 |

## 事件

支持设备PhonePC/2in1TabletTVWearable

支持[通用事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-component-general-events)。

## LoadingProgressConfiguration 12+ 对象说明

支持设备PhonePC/2in1TabletTVWearable

开发者需要自定义class实现ContentModifier接口。继承自[CommonConfiguration](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-content-modifier#commonconfigurationt)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

 展开

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| enableLoading | boolean | 否 | 否 | LoadingProgress动画是否显示。 默认值：true，true表示显示LoadingProgress动画，false表示不显示LoadingProgress动画。 |

## LoadingProgressStyle枚举说明

支持设备PhonePC/2in1TabletTVWearable

表示LoadingProgress的样式类型，不推荐使用。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

 展开

| 名称 | 值 | 说明 |
| --- | --- | --- |
| Default | 1 | 默认加载样式。API version 8及以后不支持设置。 |
| Circular | 2 | 环形加载样式。API version 8及以后不支持设置。 |
| Orbital | 3 | 彗星形加载样式。API version 8及以后默认为彗星形样式。 |

## 示例

支持设备PhonePC/2in1TabletTVWearable 

### 示例1（设置颜色）

该示例通过[color](/consumer/cn/doc/harmonyos-references/ts-basic-components-loadingprogress#color)接口，实现了设置加载动效颜色的功能。

 收起自动换行深色代码主题复制

```
// xxx.ets @Entry @Component struct LoadingProgressExample { build ( ) { Column ({ space : 5 }) { Text ( 'Orbital LoadingProgress ' ). fontSize ( 9 ). fontColor ( 0xCCCCCC ). width ( '90%' ) LoadingProgress () . color ( Color . Blue ) . layoutWeight ( 1 ) }. width ( '100%' ). margin ({ top : 5 }) } }
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170631.89198780013306730788048633174986:50001231000000:2800:F451B2CC3AD4293B50FA0265F0DF88C858B8E84B941FE1A9BE88D779DC8D1897.gif)

### 示例2（设置定制内容区）

该示例通过[contentModifier](/consumer/cn/doc/harmonyos-references/ts-basic-components-loadingprogress#contentmodifier12)接口，实现了定制内容区的功能，并通过[enableLoading](/consumer/cn/doc/harmonyos-references/ts-basic-components-loadingprogress#enableloading10)接口实现了通过按钮切换是否显示LoadingProgress的效果。

 收起自动换行深色代码主题复制

```
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170631.11310706464838467152587375699125:50001231000000:2800:20F3CB6905B8792FF827482B094B3320AA201D6F84F6AC27E2B0AE509AE118DA.gif)