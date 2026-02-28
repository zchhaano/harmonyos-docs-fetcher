# TextArea

多行文本输入框组件，当输入的文本内容超过组件宽度时会自动换行显示。

高度未设置时，组件无默认高度，自适应内容高度。宽度未设置时，默认撑满最大宽度。

 说明 

该组件从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## 子组件

 支持设备PhonePC/2in1TabletTVWearable

无

## 接口

 支持设备PhonePC/2in1TabletTVWearable

TextArea(value?: TextAreaOptions)

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | TextAreaOptions | 否 | TextArea组件参数。 |

## TextAreaOptions对象说明

 支持设备PhonePC/2in1TabletTVWearable

TextArea初始化参数。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

  展开

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| placeholder | ResourceStr | 否 | 是 | 设置无输入时的提示文本。输入内容后，提示文本不显示。 仅设置placeholder属性时，手柄依然跟随拖动，手柄松开后光标停留在文字开头位置。 |
| text | ResourceStr | 否 | 是 | 设置输入框当前的文本内容。 建议通过onChange事件将状态变量与文本实时绑定， 避免组件刷新时TextArea中的文本内容异常。 从API version 10开始，该参数支持 $$ 双向绑定变量。 从API version 18开始，该参数支持 !! 双向绑定变量。 |
| controller 8+ | TextAreaController | 否 | 是 | 设置TextArea控制器。 |

## 属性

 支持设备PhonePC/2in1TabletTVWearable

除支持[通用属性](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-component-general-attributes)，还支持以下属性：

 说明 

[通用属性padding](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-size#padding)的默认值为：

{

top: '8vp',

right: '16vp',

bottom: '8vp',

left: '16vp'

}

从API version 11开始，多行输入框可设置.width('auto')使组件宽度自适应文本宽度，自适应时组件宽度受constraintSize属性以及父容器传递的最大最小宽度限制，其余使用方式参考[尺寸设置](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-size)。

### placeholderColor

 支持设备PhonePC/2in1TabletTVWearable

placeholderColor(value: ResourceColor)

设置placeholder文本颜色。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | ResourceColor | 是 | placeholder文本颜色。 默认值：跟随主题。 |

### placeholderFont

 支持设备PhonePC/2in1TabletTVWearable

placeholderFont(value: Font)

设置placeholder文本样式，包括字体大小、字体粗细、字体族、字体风格。

 说明 

可以使用[loadFontSync](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-graphics-text#loadfontsync)注册自定义字体。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Font | 是 | placeholder文本样式。 |

### textAlign

 支持设备PhonePC/2in1TabletTVWearable

textAlign(value: TextAlign)

设置文本在输入框中的水平对齐方式。

支持TextAlign.Start、TextAlign.Center和TextAlign.End。从API version 11开始，新增TextAlign.JUSTIFY选项。

可通过[align](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-location#align)属性控制文本段落在垂直方向上的位置，此组件中不可通过align属性控制文本段落在水平方向上的位置。

- Alignment.TopStart、Alignment.Top、Alignment.TopEnd：内容顶部对齐。
- Alignment.Start、Alignment.Center、Alignment.End：内容垂直居中。
- Alignment.BottomStart、Alignment.Bottom、Alignment.BottomEnd：内容底部对齐。

当textAlign属性设置为TextAlign.JUSTIFY时，最后一行文本不参与两端对齐，为水平对齐首部效果。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | TextAlign | 是 | 文本在输入框中的水平对齐方式。 默认值：TextAlign.Start |

  说明 

textAlign只能调整文本整体的布局，不影响字符的显示顺序。若需要调整字符的显示顺序，请参考[镜像状态字符对齐](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-internationalization#镜像状态字符对齐)。

### caretColor

 支持设备PhonePC/2in1TabletTVWearable

caretColor(value: ResourceColor)

设置输入框光标颜色。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | ResourceColor | 是 | 输入框光标颜色。 默认值：'#007DFF' |

  说明 

从API version 12开始，此接口支持设置文本手柄颜色，光标和文本手柄颜色保持一致。

### fontColor

 支持设备PhonePC/2in1TabletTVWearable

fontColor(value: ResourceColor)

设置字体颜色。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | ResourceColor | 是 | 字体颜色。 |

### fontSize

 支持设备PhonePC/2in1TabletTVWearable

fontSize(value: Length)

设置字体大小。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Length | 是 | 字体大小。fontSize为number类型时，使用fp单位。字体默认大小16fp，Wearable设备上默认值为：18fp。不支持设置百分比字符串。 |

### fontStyle

 支持设备PhonePC/2in1TabletTVWearable

fontStyle(value: FontStyle)

设置字体样式。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | FontStyle | 是 | 字体样式。 默认值：FontStyle.Normal |

### fontWeight

 支持设备PhonePC/2in1TabletTVWearable

fontWeight(value: number | FontWeight | ResourceStr)

设置文本的字体粗细，设置过大可能会在不同字体下有截断。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number \| FontWeight \| ResourceStr | 是 | 文本的字体粗细，number类型取值[100, 900]，取值间隔为100，默认为400，取值越大，字体越粗。string类型仅支持number类型取值的字符串形式，例如"400"，以及"bold"、"bolder"、"lighter"、"regular"、"medium"，分别对应FontWeight中相应的枚举值。 默认值：FontWeight.Normal 从API version 20开始，支持Resource类型。 |

### fontFamily

 支持设备PhonePC/2in1TabletTVWearable

fontFamily(value: ResourceStr)

设置字体列表。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | ResourceStr | 是 | 字体列表。默认字体'HarmonyOS Sans'。 使用多个字体时，请用逗号','分隔，字体的优先级按顺序生效。例如：'Arial,HarmonyOS Sans'。 |

  说明 

推荐使用[loadFontSync](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-graphics-text#loadfontsync)注册自定义字体。

### inputFilter 8+

 支持设备PhonePC/2in1TabletTVWearable

inputFilter(value: ResourceStr, error?: (value: string) => void)

通过正则表达式设置输入过滤器。匹配表达式的输入允许显示，不匹配的输入将被过滤。

单字符输入场景仅支持单字符匹配，多字符输入场景支持字符串匹配，例如粘贴。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | ResourceStr | 是 | 正则表达式。 |
| error | (value: string) => void | 否 | 正则匹配失败时，返回被过滤的内容。 |

### copyOption 9+

 支持设备PhonePC/2in1TabletTVWearable

copyOption(value: CopyOptions)

设置输入的文本是否可复制。设置CopyOptions.None时，只支持粘贴和全选。

设置CopyOptions.None时，不支持拖拽操作。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | CopyOptions | 是 | 输入的文本是否可复制。 默认值：CopyOptions.LocalDevice，支持设备内复制。 |

### maxLength 10+

 支持设备PhonePC/2in1TabletTVWearable

maxLength(value: number)

设置文本的最大输入字符数。默认不设置最大输入字符数限制。到达文本最大字符限制，将无法继续输入字符，同时边框变为红色。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 文本的最大输入字符数。 当value<0时，按照默认值处理，不设限制。 默认值：uint32_max，即2的32次方-1。 |

### showCounter 10+

 支持设备PhonePC/2in1TabletTVWearable

showCounter(value: boolean, options?: InputCounterOptions)

设置当通过InputCounterOptions输入的字符数超过阈值时显示计数器。未调用showCounter接口时，默认不显示计数器。

参数value为true时，才能设置options，文本框开启计数器功能，需要配合maxLength（设置最大字符限制）一起使用。字符计数器显示的效果是当前输入字符数/最大可输入字符数。

当输入字符数大于最大字符数乘百分比值时，显示字符计数器。如果用户设置计数器时不设置InputCounterOptions，那么当前输入字符数达到最大字符数时，边框和计数器下标将变为红色。用户同时设置参数value为true和InputCounterOptions，当thresholdPercentage数值在有效区间内，且输入字符数超过最大字符数时，边框和计数器下标将变为红色，框体抖动。highlightBorder设置为false，则不显示红色边框，计数器默认显示红色边框。内联模式下字符计数器不显示。

[示例2（设置计数器）](/consumer/cn/doc/harmonyos-references/ts-basic-components-textarea#示例2设置计数器)展示了设置showCounter的效果。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 是否显示计数器。 true表示显示计数器，false表示不显示。 |
| options 11+ | InputCounterOptions | 否 | 计数器的配置项。 |

### style 10+

 支持设备PhonePC/2in1TabletTVWearable

style(value: TextContentStyle)

设置文本框多态样式，内联输入风格只支持TextAreaType.NORMAL类型。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | TextContentStyle | 是 | 文本框多态样式。 默认值：TextContentStyle.DEFAULT |

### enableKeyboardOnFocus 10+

 支持设备PhonePC/2in1TabletTVWearable

enableKeyboardOnFocus(value: boolean)

设置TextArea通过点击以外的方式获焦时，是否主动拉起软键盘。

从API version 10开始，获焦默认绑定输入法。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 通过点击以外的方式获焦时，是否主动拉起软键盘。 true表示主动拉起，false表示不主动拉起。 默认值：true |

### selectionMenuHidden 10+

 支持设备PhonePC/2in1TabletTVWearable

selectionMenuHidden(value: boolean)

设置是否不弹出系统文本选择菜单。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 是否不弹出系统文本选择菜单。 设置为true时，单击输入框光标、长按输入框、双击输入框、三击输入框或者右键输入框，不弹出系统文本选择菜单。 设置为false时，弹出系统文本选择菜单。 默认值：false |

### barState 10+

 支持设备PhonePC/2in1TabletTVWearable

barState(value: BarState)

设置输入框滚动条的显示模式。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | BarState | 是 | 输入框滚动条的显示模式。 默认值：BarState.Auto |

### maxLines 10+

 支持设备PhonePC/2in1TabletTVWearable

maxLines(value: number)

配置textOverflow一起使用时，maxLines为可显示行数，超出截断；未配置textOverflow时，内联模式获焦状态下内容超出maxLines时，文本可滚动显示，内联模式非获焦状态下不生效maxLines，非内联模式按行截断。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 内联输入风格编辑态时文本可显示的最大行数。 默认值：3，非内联模式下，默认值为UINT32_MAX。 取值范围：(0, UINT32_MAX] |

### maxLines 20+

 支持设备PhonePC/2in1TabletTVWearable

maxLines(lines: number, options: MaxLinesOptions)

配置[textOverflow](/consumer/cn/doc/harmonyos-references/ts-basic-components-textarea#textoverflow12)一起使用时，maxLines为可显示行数，超出可配置为截断或滚动。未配置textOverflow时，内联模式获焦状态下内容超出maxLines时，文本可滚动显示。内联模式非获焦状态下，maxLines不生效。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| lines | number | 是 | 内联输入风格编辑态时文本可显示的最大行数。 默认值：3，非内联模式下，默认值为+∞，不限制最大行数。 取值范围：(0, +∞) |
| options | MaxLinesOptions | 是 | 文本超长时显示效果。 默认值：MaxLinesMode.CLIP |

### minLines 20+

 支持设备PhonePC/2in1TabletTVWearable

minLines(lines: Optional<number>)

设置最小行数。组件的高度将根据lines自动调整，确保显示高度不低于lines对应的高度。如果设置了[constraintSize](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-size#constraintsize)，那么组件最后显示高度会在[constraintSize](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-size#constraintsize)约束内。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| lines | Optional <number> | 是 | 最小行数。 默认值：1 取值范围：取值范围：[1, INT32_MAX] 如果lines的值小于1，取默认值。 |

### customKeyboard 10+

 支持设备PhonePC/2in1TabletTVWearable

customKeyboard(value: CustomBuilder | ComponentContent | undefined, options?: KeyboardOptions)

设置自定义键盘。

当设置自定义键盘时，输入框激活后不会打开系统输入法，而是加载指定的自定义组件。

自定义键盘的高度可以通过自定义组件根节点的height属性设置，宽度则使用系统默认值。

自定义键盘采用覆盖原始界面的方式呈现，当没有开启避让模式或者输入框不需要避让的场景，不会对应用原始界面产生压缩或者上提。

自定义键盘无法获取焦点，但是会拦截手势事件。

默认在输入控件失去焦点时，关闭自定义键盘，开发者也可以通过[TextAreaController](/consumer/cn/doc/harmonyos-references/ts-basic-components-textarea#textareacontroller8).[stopEditing](/consumer/cn/doc/harmonyos-references/ts-basic-components-textarea#stopediting10)方法控制键盘关闭。

当设置自定义键盘时，可以通过绑定[onKeyPrelme](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-events-key#onkeypreime12)事件规避物理键盘的输入。

 说明 

该接口不支持在[attributeModifier](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-attribute-modifier#attributemodifier)中调用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | CustomBuilder \| ComponentContent 22+ \| undefined 22+ | 是 | 自定义键盘。设定值为undefined时，关闭自定义键盘。 |
| options 12+ | KeyboardOptions | 否 | 设置自定义键盘是否支持避让功能。 |

### type 11+

 支持设备PhonePC/2in1TabletTVWearable

type(value: TextAreaType)

设置输入框类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | TextAreaType | 是 | 输入框类型。 默认值：TextAreaType.NORMAL |

### enterKeyType 11+

 支持设备PhonePC/2in1TabletTVWearable

enterKeyType(value: EnterKeyType)

设置输入法回车键类型。

 说明 

从API version 12开始，该接口支持在[attributeModifier](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-attribute-modifier#attributemodifier)中调用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | EnterKeyType | 是 | 输入法回车键类型。 默认值：EnterKeyType.NEW_LINE |

### enableAutoFill 12+

 支持设备PhonePC/2in1TabletTVWearable

enableAutoFill(value: boolean)

设置是否启用自动填充。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 是否启用自动填充。 true表示启用，false表示不启用。 默认值：true |

### enableSelectedDataDetector 22+

 支持设备PhonePC/2in1TabletTVWearable

enableSelectedDataDetector(enable: boolean | undefined)

设置是否对选中文本进行实体识别。该接口依赖设备底层应具有文本识别能力，否则设置不会生效。

当enableSelectedDataDetector设置为true时，默认识别所有类型的实体。

需要[CopyOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-appendix-enums#copyoptions9)为CopyOptions.LocalDevice或CopyOptions.CROSS_DEVICE时，本功能生效。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | boolean \| undefined | 是 | 开启选中词文本识别。 true：开启识别，false：关闭识别。默认值为：true。 |

### contentType 12+

 支持设备PhonePC/2in1TabletTVWearable

contentType(contentType: ContentType)

设置自动填充类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| contentType | ContentType | 是 | 自动填充类型。 |

### lineHeight 12+

 支持设备PhonePC/2in1TabletTVWearable

lineHeight(value: number | string | Resource)

设置文本的文本行高，设置值不大于0时，不限制文本行高，自适应字体大小，number类型时单位为fp。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number \| string \| Resource | 是 | 文本的文本行高。 |

  说明 

特殊字符字体高度远超出同行的其他字符高度时，文本框出现截断、遮挡、内容相对位置发生变化等不符合预期的显示异常，需要开发者调整组件高度、行高等属性，修改对应的页面布局。

### decoration 12+

 支持设备PhonePC/2in1TabletTVWearable

decoration(value: TextDecorationOptions)

设置文本装饰线类型样式及其颜色。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | TextDecorationOptions | 是 | 文本装饰线对象。 默认值：{ type: TextDecorationType.None, color: Color.Black, style: TextDecorationStyle.SOLID } |

  说明 

当文字的下边缘轮廓与装饰线位置相交时，会触发下划线避让规则，下划线将在这些字符处避让文字。常见“gjyqp”等英文字符。

当文本装饰线的颜色设置为Color.Transparent时，装饰线颜色设置为跟随每行第一个字的字体颜色。当文本装饰线的颜色设置为透明色16进制对应值“#00FFFFFF”时，装饰线颜色设置为透明色。

### letterSpacing 12+

 支持设备PhonePC/2in1TabletTVWearable

letterSpacing(value: number | string | Resource)

设置文本字符间距。设置该值为百分比时，按默认值显示。当设置该值为0时，使用默认值。string类型支持number类型取值的字符串形式，可以附带单位，例如"10"、"10fp"。

当取值为负值时，文字会发生压缩，负值过小时会将组件内容区大小压缩为0，导致无内容显示。

对每个字符生效，包括行尾字符。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number \| string \| Resource | 是 | 文本字符间距。 单位： fp |

### fontFeature 12+

 支持设备PhonePC/2in1TabletTVWearable

fontFeature(value: string)

设置文字特性效果，比如数字等宽的特性。

格式为：normal | <feature-tag-value>

<feature-tag-value>的格式为：<string> [ <integer> | on | off ]

<feature-tag-value>的个数可以有多个，中间用','隔开。

例如，使用等宽数字的输入格式为："ss01" on。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string | 是 | 文字特性效果。 |

Font Feature当前支持的属性见[fontFeature属性列表](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text#fontfeature12)。

设置Font Feature属性，Font Feature是OpenType字体的高级排版能力，如支持连字、数字等宽等特性，一般用在自定义字体中，其能力需要字体本身支持。

更多Font Feature能力介绍可参考https://www.w3.org/TR/css-fonts-3/#font-feature-settings-prop和https://sparanoid.com/lab/opentype-features/。

### wordBreak 12+

 支持设备PhonePC/2in1TabletTVWearable

wordBreak(value: WordBreak)

设置文本断行规则。该属性对placeholder文本无效。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | WordBreak | 是 | 文本断行规则。 默认值：WordBreak.BREAK_WORD |

  说明 

组件不支持clip属性设置，设置该属性任意枚举值对组件文本截断无影响。

### selectedBackgroundColor 12+

 支持设备PhonePC/2in1TabletTVWearable

selectedBackgroundColor(value: ResourceColor)

设置文本选中底板颜色。如果未设置不透明度，默认为20%不透明度。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | ResourceColor | 是 | 文本选中底板颜色。 |

### caretStyle 12+

 支持设备PhonePC/2in1TabletTVWearable

caretStyle(value: CaretStyle)

设置光标风格。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | CaretStyle | 是 | 光标的风格。 |

  说明 

当同时设置caretColor属性和caretStyle属性中的color参数时，遵循后设置生效原则。

从API version 12开始，此接口支持设置文本手柄颜色，光标和文本手柄颜色保持一致。

### textIndent 12+

 支持设备PhonePC/2in1TabletTVWearable

textIndent(value: Dimension)

设置首行文本缩进。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Dimension | 是 | 首行文本缩进。 默认值：0 |

### textOverflow 12+

 支持设备PhonePC/2in1TabletTVWearable

textOverflow(value: TextOverflow)

设置文本超长时的显示方式。

内联模式，主动配置textOverflow才会生效按[maxLines](/consumer/cn/doc/harmonyos-references/ts-basic-components-textarea#maxlines10)截断效果，不配置时，默认不截断。

文本截断是按字截断。例如，英文以单词为最小单位进行截断，若需要以字母为单位进行截断，[wordBreak](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-appendix-enums#wordbreak11)属性可设置为WordBreak.BREAK_ALL。

当textOverflow设置为TextOverflow.None、TextOverflow.Clip、TextOverflow.Ellipsis时，需配合[maxLines](/consumer/cn/doc/harmonyos-references/ts-basic-components-textarea#maxlines10)使用，单独设置不生效。设置TextOverflow.None与TextOverflow.Clip效果一样。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | TextOverflow | 是 | 文本超长时的显示方式。 默认值：TextOverflow.Clip |

  说明 

TextArea组件不支持设置TextOverflow.MARQUEE模式,当设置为TextOverflow.MARQUEE模式时 显示为TextOverflow.Clip

### minFontSize 12+

 支持设备PhonePC/2in1TabletTVWearable

minFontSize(value: number | string | Resource)

设置文本最小显示字号。string类型支持number类型取值的字符串形式，可以附带单位，例如"10"、"10fp"。

需配合[maxFontSize](/consumer/cn/doc/harmonyos-references/ts-basic-components-textarea#maxfontsize12)以及[maxLines](/consumer/cn/doc/harmonyos-references/ts-basic-components-textarea#maxlines10)或布局大小限制使用，单独设置不生效。

自适应字号生效时，fontSize设置不生效。

minFontSize小于或等于0时，自适应字号不生效，此时按照[fontSize](/consumer/cn/doc/harmonyos-references/ts-basic-components-textarea#fontsize)属性的值生效，未设置时按照其默认值生效。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number \| string \| Resource | 是 | 文本最小显示字号。 单位： fp |

### maxFontSize 12+

 支持设备PhonePC/2in1TabletTVWearable

maxFontSize(value: number | string | Resource)

设置文本最大显示字号。string类型支持number类型取值的字符串形式，可以附带单位，例如"10"、"10fp"。

需配合[minFontSize](/consumer/cn/doc/harmonyos-references/ts-basic-components-textarea#minfontsize12)以及[maxLines](/consumer/cn/doc/harmonyos-references/ts-basic-components-textarea#maxlines10)或布局大小限制使用，单独设置不生效。

自适应字号生效时，fontSize设置不生效。

maxFontSize小于等于0或者maxFontSize小于minFontSize时，自适应字号不生效，此时按照[fontSize](/consumer/cn/doc/harmonyos-references/ts-basic-components-textarea#fontsize)属性的值生效，未设置时按照其默认值生效。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number \| string \| Resource | 是 | 文本最大显示字号。 单位： fp |

### heightAdaptivePolicy 12+

 支持设备PhonePC/2in1TabletTVWearable

heightAdaptivePolicy(value: TextHeightAdaptivePolicy)

设置文本自适应高度的方式。

当设置为TextHeightAdaptivePolicy.MAX_LINES_FIRST时，优先使用[maxLines](/consumer/cn/doc/harmonyos-references/ts-basic-components-textarea#maxlines10)属性来调整文本高度。如果使用maxLines属性的布局大小超过了布局约束，则尝试在[minFontSize](/consumer/cn/doc/harmonyos-references/ts-basic-components-textarea#minfontsize12)和[maxFontSize](/consumer/cn/doc/harmonyos-references/ts-basic-components-textarea#maxfontsize12)的范围内缩小字体以显示更多文本。

组件设置为内联输入风格，编辑态与非编辑态存在字体大小不一致情况。

当设置为TextHeightAdaptivePolicy.MIN_FONT_SIZE_FIRST时，优先使用minFontSize属性来调整文本高度。如果使用minFontSize属性可以将文本布局在一行中，则尝试在minFontSize和maxFontSize的范围内增大字体并使用最大可能的字体大小。

当设置为TextHeightAdaptivePolicy.LAYOUT_CONSTRAINT_FIRST时，优先使用布局约束来调整文本高度。如果布局大小超过布局约束，则尝试在minFontSize和maxFontSize的范围内缩小字体以满足布局约束。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | TextHeightAdaptivePolicy | 是 | 文本自适应高度的方式。 默认值：TextHeightAdaptivePolicy.MAX_LINES_FIRST |

### lineSpacing 12+

 支持设备PhonePC/2in1TabletTVWearable

lineSpacing(value: LengthMetrics)

设置文本的行间距，设置值不大于0时，取默认值0。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | LengthMetrics | 是 | 文本的行间距。默认值：0 |

### lineSpacing 20+

 支持设备PhonePC/2in1TabletTVWearable

lineSpacing(value: LengthMetrics, options?: LineSpacingOptions)

设置文本的行间距。当不配置LineSpacingOptions时，首行上方和尾行下方默认会有行间距。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | LengthMetrics | 是 | 文本的行间距。设置值不大于0时，取默认值0。 |
| options | LineSpacingOptions | 否 | 设置行间距配置项。 默认值：{ onlyBetweenLines: false } |

### lineBreakStrategy 12+

 支持设备PhonePC/2in1TabletTVWearable

lineBreakStrategy(strategy: LineBreakStrategy)

设置折行规则。该属性在[wordBreak](/consumer/cn/doc/harmonyos-references/ts-basic-components-textarea#wordbreak12)不等于WordBreak.BREAK_ALL的时候生效，不支持连词符。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| strategy | LineBreakStrategy | 是 | 文本的折行规则。 默认值：LineBreakStrategy.GREEDY |

### editMenuOptions 12+

 支持设备PhonePC/2in1TabletTVWearable

editMenuOptions(editMenu: EditMenuOptions)

设置自定义菜单扩展项，允许用户设置扩展项的文本内容、图标、回调方法。

调用[disableMenuItems](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-textmenucontroller#disablemenuitems20)或[disableSystemServiceMenuItems](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-textmenucontroller#disablesystemservicemenuitems20)接口屏蔽文本选择菜单内的系统服务菜单项时，editMenuOptions接口内回调方法[onCreateMenu](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-text-common#oncreatemenu12)的入参列表中不包含被屏蔽的菜单选项。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| editMenu | EditMenuOptions | 是 | 扩展菜单选项。 |

### enablePreviewText 12+

 支持设备PhonePC/2in1TabletTVWearable

enablePreviewText(enable: boolean)

设置是否开启输入预上屏。

预上屏内容定义为文字暂存态，目前不支持文字拦截功能。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | boolean | 是 | 是否开启输入预上屏。 true表示开启，false表示不开启。 默认值：true |

  说明 

“预上屏”描述的是一种文字暂存状态。需要在输入法中开启预上屏功能，在输入文本过程中，未确认输入候选词时，文本框中显示标记文本。例如，通过拼音输入中文时，未确定候选词之前，在输入框中显示拼音字母，该状态称为文字预上屏。

### enableHapticFeedback 13+

 支持设备PhonePC/2in1TabletTVWearable

enableHapticFeedback(isEnabled: boolean)

设置是否开启触控反馈。

开启触控反馈时，需要在工程的module.json5中配置requestPermissions字段以开启振动权限，配置如下：

```
"requestPermissions": [
 {
    "name": "ohos.permission.VIBRATE",
 }
]
```

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isEnabled | boolean | 是 | 是否开启触控反馈。 true表示开启，false表示不开启。 默认值：true |

### autoCapitalizationMode 20+

 支持设备PhonePC/2in1TabletTVWearable

autoCapitalizationMode(mode: AutoCapitalizationMode)

设置自动大小写模式的文本模式，只提供接口能力，具体实现以输入法应用为主。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | AutoCapitalizationMode | 是 | 自动大小写模式，默认状态无效。 |

### keyboardAppearance 15+

 支持设备PhonePC/2in1TabletTVWearable

keyboardAppearance(appearance: Optional<KeyboardAppearance>)

设置输入框拉起的键盘样式。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| appearance | Optional < KeyboardAppearance > | 是 | 键盘样式。 默认值：KeyboardAppearance.NONE_IMMERSIVE |

### strokeWidth 20+

 支持设备PhonePC/2in1TabletTVWearable

strokeWidth(width: Optional<LengthMetrics>)

设置文本描边的宽度。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| width | Optional < LengthMetrics > | 是 | 文本描边的宽度。当LengthMetrics的单位为px时， 若设置值小于0，显示实心字；若大于0，显示空心字。 默认值为0，不做描边处理。 |

### strokeColor 20+

 支持设备PhonePC/2in1TabletTVWearable

strokeColor(color: Optional<ResourceColor>)

设置文本描边的颜色。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| color | Optional < ResourceColor > | 是 | 描边颜色。默认值为字体颜色，设置异常值时取默认值。 |

### stopBackPress 15+

 支持设备PhonePC/2in1TabletTVWearable

stopBackPress(isStopped: Optional<boolean>)

设置是否阻止返回键传递。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isStopped | Optional <boolean> | 是 | 是否阻止返回键。 true表示阻止，false表示不阻止。 默认值：true。异常值取默认值。 |

### halfLeading 18+

 支持设备PhonePC/2in1TabletTVWearable

halfLeading(halfLeading: Optional<boolean>)

设置文本在行内垂直居中，将行间距平分至行的顶部与底部。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| halfLeading | Optional <boolean> | 是 | 设置文本是否垂直居中。 true表示将行间距平分至行的顶部与底部，false则不平分。 默认值：false |

### minFontScale 18+

 支持设备PhonePC/2in1TabletTVWearable

minFontScale(scale: Optional<number | Resource>)

设置文本最小的字体缩放倍数。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scale | Optional <number \| Resource > | 是 | 文本最小的字体缩放倍数，支持undefined类型。 取值范围：[0, 1] 说明： 设置的值小于0时，按值为0处理。设置的值大于1，按值为1处理。异常值默认不生效。 使用前需在工程中配置configuration.json文件和app.json5文件，具体详见 示例17设置最小字体范围与最大字体范围 。 |

### maxFontScale 18+

 支持设备PhonePC/2in1TabletTVWearable

maxFontScale(scale: Optional<number | Resource>)

设置文本最大的字体缩放倍数。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scale | Optional <number \| Resource > | 是 | 文本最大的字体缩放倍数，支持undefined类型。 取值范围：[1, +∞) 说明： 设置的值小于1时，按值为1处理。异常值默认不生效。 使用前需在工程中配置configuration.json文件和app.json5文件，具体详见 示例17设置最小字体范围与最大字体范围 。 |

### ellipsisMode 18+

 支持设备PhonePC/2in1TabletTVWearable

ellipsisMode(mode: Optional<EllipsisMode>)

设置省略位置。ellipsisMode属性需要配合[textOverflow](/consumer/cn/doc/harmonyos-references/ts-basic-components-textarea#textoverflow12)设置为TextOverflow.Ellipsis以及[maxLines](/consumer/cn/doc/harmonyos-references/ts-basic-components-textarea#maxlines10)使用，单独设置ellipsisMode属性不生效。

EllipsisMode.START和EllipsisMode.CENTER仅在[maxLines](/consumer/cn/doc/harmonyos-references/ts-basic-components-textarea#maxlines10)设置为1生效。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | Optional < EllipsisMode > | 是 | 省略位置。 默认值：EllipsisMode.END |

### enableAutoSpacing 20+

 支持设备PhonePC/2in1TabletTVWearable

enableAutoSpacing(enabled: Optional<boolean>)

设置是否开启中文与西文的自动间距。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | Optional <boolean> | 是 | 是否开启中文与西文的自动间距。 true为开启自动间距，false为不开启。 默认值：false |

### scrollBarColor 22+

 支持设备PhonePC/2in1TabletTVWearable

scrollBarColor(thumbColor: ColorMetrics | undefined)

设置滚动条的颜色。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| thumbColor | ColorMetrics \| undefined | 是 | 滚动条的颜色。 默认值：'#66182431'，显示为灰色。 |

## 事件

 支持设备PhonePC/2in1TabletTVWearable

除支持[通用事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-component-general-events)外，还支持以下事件：

### onChange

 支持设备PhonePC/2in1TabletTVWearable

onChange(callback: EditableTextOnChangeCallback)

输入内容发生变化时，触发该回调。

在本回调中，若执行了光标操作，需要开发者在预上屏场景下依据previewText参数调整光标逻辑，以适应预上屏场景。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | EditableTextOnChangeCallback | 是 | 当前输入文本内容变化时的回调。 |

### onEditChange 10+

 支持设备PhonePC/2in1TabletTVWearable

onEditChange(callback: (isEditing: boolean) => void)

输入状态变化时，触发该回调。有光标时为编辑态，无光标时为非编辑态。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isEditing | boolean | 是 | 是否处于编辑态。 true：编辑态；false：非编辑态。 |

### onCopy 8+

 支持设备PhonePC/2in1TabletTVWearable

onCopy(callback: (value: string) => void)

进行复制操作时，触发该回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string | 是 | 复制的文本内容。 |

### onCut 8+

 支持设备PhonePC/2in1TabletTVWearable

onCut(callback: (value: string) => void)

进行剪切操作时，触发该回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string | 是 | 剪切的文本内容。 |

### onPaste

 支持设备PhonePC/2in1TabletTVWearable

onPaste(callback: (value: string, event: PasteEvent) => void)

进行粘贴操作时，触发该回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string | 是 | 粘贴的文本内容。 |
| event 11+ | PasteEvent | 是 | 用户自定义的粘贴事件。 |

### onTextSelectionChange 10+

 支持设备PhonePC/2in1TabletTVWearable

onTextSelectionChange(callback: (selectionStart: number, selectionEnd: number) => void)

文本选择的位置或编辑状态下光标位置发生变化时，触发该回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| selectionStart | number | 是 | 所选文本的起始位置，文字的起始位置为0。 |
| selectionEnd | number | 是 | 所选文本的结束位置。 |

### onContentScroll 10+

 支持设备PhonePC/2in1TabletTVWearable

onContentScroll(callback: (totalOffsetX: number, totalOffsetY: number) => void)

文本内容滚动时，触发该回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| totalOffsetX | number | 是 | 文本在内容区的横坐标偏移。 单位： px |
| totalOffsetY | number | 是 | 文本在内容区的纵坐标偏移。 单位： px |

### onSubmit 11+

 支持设备PhonePC/2in1TabletTVWearable

onSubmit(callback: (enterKey: EnterKeyType) => void)

按下软键盘输入法回车键时，触发该回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enterKey | EnterKeyType | 是 | 输入法回车键类型，类型为EnterKeyType.NEW_LINE时不触发onSubmit。 |

### onSubmit 14+

 支持设备PhonePC/2in1TabletTVWearable

onSubmit(callback: TextAreaSubmitCallback)

按下软键盘输入法回车键触发该回调事件，提交事件时提供保持TextArea编辑状态的方法。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | TextAreaSubmitCallback | 是 | 按下软键盘输入法回车键时的回调事件。 |

### onWillInsert 12+

 支持设备PhonePC/2in1TabletTVWearable

onWillInsert(callback: Callback<InsertValue, boolean>)

在将要输入时，触发该回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback< InsertValue , boolean> | 是 | 在将要输入时调用的回调。 在返回true时，表示正常插入，返回false时，表示不插入。 在预上屏和候选词操作时，该回调不触发。 仅支持系统输入法输入的场景。 |

### onDidInsert 12+

 支持设备PhonePC/2in1TabletTVWearable

onDidInsert(callback: Callback<InsertValue>)

在输入完成时，触发该回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback< InsertValue > | 是 | 在输入完成时调用的回调。 仅支持系统输入法输入的场景。 |

### onWillDelete 12+

 支持设备PhonePC/2in1TabletTVWearable

onWillDelete(callback: Callback<DeleteValue, boolean>)

在将要删除时，触发该回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback< DeleteValue , boolean> | 是 | 在将要删除时调用的回调。 在返回true时，表示正常删除，返回false时，表示不删除。 在预上屏删除操作时，该回调不触发。 仅支持系统输入法输入的场景。 |

### onDidDelete 12+

 支持设备PhonePC/2in1TabletTVWearable

onDidDelete(callback: Callback<DeleteValue>)

在删除完成时，触发该回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback< DeleteValue > | 是 | 在删除完成时调用的回调。 仅支持系统输入法输入的场景。 |

  说明 

点击清除按钮不触发onDidDelete回调。

### onWillChange 15+

 支持设备PhonePC/2in1TabletTVWearable

onWillChange(callback: Callback<EditableTextChangeValue, boolean>)

在文本内容将要发生变化时，触发该回调。

onWillChange的回调时序晚于onWillInsert、onWillDelete，早于onDidInsert、onDidDelete。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback< EditableTextChangeValue , boolean> | 是 | 在文本内容将要发生变化时的回调。 返回true时，表示正常修改。返回false时，表示拦截此次触发。 |

### onWillAttachIME 22+

 支持设备PhonePC/2in1TabletTVWearable

onWillAttachIME(callback: Callback<IMEClient> | undefined)

在输入框将要绑定输入法前触发该回调。

从API version 22开始，调用[IMEClient](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-text-common#imeclient20对象说明)的[setExtraConfig](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-text-common#setextraconfig22)方法可以设置输入法扩展信息。在绑定输入法成功后，输入法会收到扩展信息，输入法可以依据此信息实现自定义功能。

IMEClient仅在onWillAttachIME执行期间有效，不可进行异步调用。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback< IMEClient > \| undefined | 是 | 在输入框将要绑定输入法前触发该回调。 |

## TextAreaController 8+

 支持设备PhonePC/2in1TabletTVWearable

TextArea组件的控制器继承自[TextContentControllerBase](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-text-style#textcontentcontrollerbase)，涉及的接口有[getTextContentRect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-text-style#gettextcontentrect)、[getTextContentLineCount](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-text-style#gettextcontentlinecount)、[getCaretOffset](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-text-style#getcaretoffset11)、[addText](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-text-style#addtext15)、[deleteText](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-text-style#deletetext15)、[getSelection](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-text-style#getselection15)、[clearPreviewText](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-text-style#clearpreviewtext17)、[setStyledPlaceholder](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-text-style#setstyledplaceholder22)。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### 导入对象

```
controller: TextAreaController = new TextAreaController()
```

### constructor 8+

 支持设备PhonePC/2in1TabletTVWearable

constructor()

TextAreaController的构造函数。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### caretPosition 8+

 支持设备PhonePC/2in1TabletTVWearable

caretPosition(value: number): void

设置输入光标的位置。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 从字符串开始到光标所在位置的字符长度。 当value<0时，按照0处理。当value>字符串长度时，按照字符串长度处理。 |

### setTextSelection 10+

 支持设备PhonePC/2in1TabletTVWearable

setTextSelection(selectionStart: number, selectionEnd: number, options?: SelectionOptions): void

组件在获焦状态下，调用该接口设置文本选择区域并高亮显示，且只有在selectionStart小于selectionEnd时，文字才会被选取、高亮显示。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| selectionStart | number | 是 | 文本选择区域起始位置，文本框中文字的起始位置为0。 当selectionStart小于0时，按0处理；当selectionStart大于文字最大长度时，按照文字最大长度处理。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| selectionEnd | number | 是 | 文本选择区域结束位置。 当selectionEnd小于0时，按0处理；当selectionEnd大于文字最大长度时，按照文字最大长度处理。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| options 12+ | SelectionOptions | 否 | 选中文字时的配置。 默认值：MenuPolicy.DEFAULT 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |

  说明 

如果selectionMenuHidden被赋值为true或设备为2in1时，即使options被赋值为MenuPolicy.SHOW，调用setTextSelection也不弹出菜单。

如果选中的文本含有emoji表情时，表情的起始位置包含在设置的文本选中区域内就会被选中。

### stopEditing 10+

 支持设备PhonePC/2in1TabletTVWearable

stopEditing(): void

退出编辑态。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## TextAreaType 11+ 枚举说明

 支持设备PhonePC/2in1TabletTVWearable

多行文本输入框类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

  展开

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NORMAL | 0 | 基本输入模式，无特殊限制。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| NUMBER | 2 | 纯数字输入模式。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| PHONE_NUMBER | 3 | 电话号码输入模式。 支持输入数字、空格、+ 、-、*、#、(、)，长度不限。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| EMAIL | 5 | 邮箱地址输入模式。 支持数字，字母，下划线、小数点、!、#、$、%、&、'、*、+、-、/、=、?、^、`、{、\|、}、~，以及@字符（只能存在一个@字符）。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| NUMBER_DECIMAL 12+ | 12 | 带小数点的数字输入模式。 支持数字，小数点（只能存在一个小数点）。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| URL 12+ | 13 | 带URL的输入模式，无特殊限制。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| ONE_TIME_CODE 20+ | 14 | 验证码输入模式，无特殊限制。 元服务API： 从API version 20开始，该接口支持在元服务中使用。 |

## TextAreaSubmitCallback 14+

 支持设备PhonePC/2in1TabletTVWearable

type TextAreaSubmitCallback = (enterKeyType: EnterKeyType, event?: SubmitEvent) => void

软键盘按下回车键时的回调事件。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enterKeyType | EnterKeyType | 是 | 软键盘输入法回车键类型。 类型为EnterKeyType.NEW_LINE时不触发onSubmit。 |
| event | SubmitEvent | 否 | 提交事件。 |

## 示例

 支持设备PhonePC/2in1TabletTVWearable  

### 示例1（设置与获取光标位置）

从API version 8开始，该示例通过[controller](/consumer/cn/doc/harmonyos-references/ts-basic-components-textarea#textareacontroller8)实现了光标位置的设置与获取。

```
// xxx.ets
@Entry
@Component
struct TextAreaExample {
  @State text: string = '';
  @State positionInfo: CaretOffset = { index: 0, x: 0, y: 0 };
  controller: TextAreaController = new TextAreaController();

  build() {
    Column() {
      TextArea({
        text: this.text,
        placeholder: 'The text area can hold an unlimited amount of text. input your word...',
        controller: this.controller
      })
        .placeholderFont({ size: 16, weight: 400 })
        .width(336)
        .height(56)
        .margin(20)
        .fontSize(16)
        .fontColor('#182431')
        .backgroundColor('#FFFFFF')
        .onChange((value: string) => {
          this.text = value;
        })
      Text(this.text)
      Button('Set caretPosition 1')
        .backgroundColor('#007DFF')
        .margin(15)
        .onClick(() => {
          // 设置光标位置到第一个字符后
          this.controller.caretPosition(1);
        })
      Button('Get CaretOffset')
        .backgroundColor('#007DFF')
        .margin(15)
        .onClick(() => {
          this.positionInfo = this.controller.getCaretOffset();
        })
    }.width('100%').height('100%').backgroundColor('#F1F3F5')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170454.19894097115893546843929509194178:50001231000000:2800:53387C3F8B16BF3ACDA66D8435D42E3D9B04240F994C46717B10F15F0DA53062.gif)

### 示例2（设置计数器）

从API version 10开始，该示例通过[maxLength](/consumer/cn/doc/harmonyos-references/ts-basic-components-textarea#maxlength10)、[showCounter](/consumer/cn/doc/harmonyos-references/ts-basic-components-textarea#showcounter10)属性实现了计数器的功能。

```
// xxx.ets
@Entry
@Component
struct TextAreaExample {
  @State text: string = '';
  controller: TextAreaController = new TextAreaController();

  build() {
    Column() {
      TextArea({
        text: this.text,
        placeholder: 'The text area can hold an unlimited amount of text. input your word...',
        controller: this.controller
      })
        .placeholderFont({ size: 16, weight: 400 })
        .width(336)
        .height(56)
        .margin(20)
        .fontSize(16)
        .fontColor('#182431')
        .backgroundColor('#FFFFFF')
        .maxLength(4)
        .showCounter(true, { thresholdPercentage: 50, highlightBorder: true })
          // 计数器显示效果为用户当前输入字符数/最大字符限制数。最大字符限制数通过maxLength()接口设置。
          // 如果用户当前输入字符数达到最大字符限制乘50%（thresholdPercentage）。字符计数器显示。
          // 用户设置highlightBorder为false时，配置取消红色边框。不设置此参数时，默认为true。
        .onChange((value: string) => {
          this.text = value;
        })
    }.width('100%').height('100%').backgroundColor('#F1F3F5')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170454.58531689419207518388972752240990:50001231000000:2800:996DB86DA2192F6234363916DA009B22B2014F1D3C7735DB375DBFB5663A2F30.gif)

### 示例3（设置自定义键盘）

该示例通过[customKeyboard](/consumer/cn/doc/harmonyos-references/ts-basic-components-textarea#customkeyboard10)（从API version 10开始）属性分别将value中的入参类型设置为[CustomBuilder](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#custombuilder8)和[ComponentContent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-componentcontent#componentcontent-1)，实现了自定义键盘的功能。

从API version 22开始[customKeyboard](/consumer/cn/doc/harmonyos-references/ts-basic-components-textarea#customkeyboard10)属性新增了入参类型[ComponentContent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-componentcontent#componentcontent-1)。

```
// xxx.ets
import { ComponentContent } from '@kit.ArkUI';
class BuilderParams {
  inputValue: string;
  controller: TextAreaController;

  constructor(inputValue: string, controller: TextAreaController) {
    this.inputValue = inputValue;
    this.controller = controller;
  }
}
@Builder
function CustomKeyboardBuilder(builderParams: BuilderParams) {
  Column() {
    Row() {
      Button('x').onClick(() => {
        // 关闭自定义键盘
        builderParams.controller.stopEditing();
      }).margin(10)
    }

    Grid() {
      ForEach([1, 2, 3, 4, 5, 6, 7, 8, 9, '*', 0, '#'], (item: number | string) => {
        GridItem() {
          Button(item + "")
            .width(110).onClick(() => {
            builderParams.inputValue += item;
          })
        }
      })
    }.maxCount(3).columnsGap(10).rowsGap(10).padding(5)
  }.backgroundColor(Color.Gray)
}
@Entry
@Component
struct TextAreaExample {
  controller: TextAreaController = new TextAreaController();
  @State inputValue: string = "";
  @State componentContent ?: ComponentContent<BuilderParams> = undefined;
  @State builderParam: BuilderParams = new BuilderParams(this.inputValue, this.controller);
  @State supportAvoidance: boolean = true;

  aboutToAppear(): void {
    // 创建ComponentContent
    this.componentContent = new ComponentContent(this.getUIContext(), wrapBuilder(CustomKeyboardBuilder), this.builderParam);
  }
  build(){
    Column() {
      Text('Builder').margin(10).border({ width: 1 })
      TextArea({ controller: this.builderParam.controller, text: this.builderParam.inputValue })
        .customKeyboard(this.componentContent, { supportAvoidance: this.supportAvoidance })
        .margin(10).border({ width: 1 }).height('48vp')

      Text('ComponentContent').margin(10).border({ width: 1 })
      TextArea({ controller: this.builderParam.controller, text: this.builderParam.inputValue })
        .customKeyboard(CustomKeyboardBuilder(this.builderParam), { supportAvoidance: this.supportAvoidance })
        .margin(10).border({ width: 1 }).height('48vp')
    }
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170454.26376724528554644403124627692304:50001231000000:2800:EE8841D55C435A017EBBA79F21F7B4607FCFA34E7253D1FFDA05901D34F8C06A.gif)

### 示例4（设置输入法回车键类型）

从API version 11开始，该示例通过[enterKeyType](/consumer/cn/doc/harmonyos-references/ts-basic-components-textarea#enterkeytype11)属性实现了动态切换输入法回车键的效果。

```
// xxx.ets
@Entry
@Component
struct TextAreaExample {
  @State text: string = '';
  @State enterTypes: Array<EnterKeyType> =
    [EnterKeyType.Go, EnterKeyType.Search, EnterKeyType.Send, EnterKeyType.Done, EnterKeyType.Next,
      EnterKeyType.PREVIOUS, EnterKeyType.NEW_LINE];
  @State index: number = 0;

  build() {
    Column({ space: 20 }) {
      TextArea({ placeholder: '请输入用户名', text: this.text })
        .width(380)
        .enterKeyType(this.enterTypes[this.index])
        .onChange((value: string) => {
          this.text = value;
        })
        .onSubmit((enterKey: EnterKeyType) => {
          console.info("trigger area onSubmit" + enterKey);
        })
      Button('改变EnterKeyType').onClick(() => {
        this.index = (this.index + 1) % this.enterTypes.length;
      })

    }.width('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170454.58687736338493264481085206852439:50001231000000:2800:A38C82791604018C464BD047451C5068B330586685DEA1B4ADFB6880A30DC20B.gif)

### 示例5（设置文本断行规则）

从API version 12开始，该示例通过[wordBreak](/consumer/cn/doc/harmonyos-references/ts-basic-components-textarea#wordbreak12)属性实现了TextArea不同断行规则下的效果。

```
// xxx.ets
@Entry
@Component
struct TextAreaExample {
  build() {
    Column() {
      Text("属性WordBreakType为NORMAL的样式：").fontSize(16).fontColor(0xFF0000)
      TextArea({
        text: 'This is set wordBreak to WordBreak text Taumatawhakatangihangakoauauotamateaturipukakapikimaungahoronukupokaiwhenuakitanatahu.'
      })
        .fontSize(16)
        .border({ width: 1 })
        .wordBreak(WordBreak.NORMAL)
      Text("英文文本，属性WordBreakType为BREAK_ALL的样式：").fontSize(16).fontColor(0xFF0000)
      TextArea({
        text: 'This is set wordBreak to WordBreak text Taumatawhakatangihangakoauauotamateaturipukakapikimaungahoronukupokaiwhenuakitanatahu.'
      })
        .fontSize(16)
        .border({ width: 1 })
        .wordBreak(WordBreak.BREAK_ALL)
      Text("中文文本，属性WordBreakType为BREAK_ALL的样式：").fontSize(16).fontColor(0xFF0000)
      TextArea({
        text: '多行文本输入框组件，当输入的文本内容超过组件宽度时会自动换行显示。\n高度未设置时，组件无默认高度，自适应内容高度。宽度未设置时，默认撑满最大宽度。'
      })
        .fontSize(16)
        .border({ width: 1 })
        .wordBreak(WordBreak.BREAK_ALL)
      Text("属性WordBreakType为BREAK_WORD的样式：").fontSize(16).fontColor(0xFF0000)
      TextArea({
        text: 'This is set wordBreak to WordBreak text Taumatawhakatangihangakoauauotamateaturipukakapikimaungahoronukupokaiwhenuakitanatahu.'
      })
        .fontSize(16)
        .border({ width: 1 })
        .wordBreak(WordBreak.BREAK_WORD)
    }
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170454.67981449092264056672528473097815:50001231000000:2800:14BD9A5BE53AE658984C8E0DBBAAEA12B40697D268D60B6135063BF929F92E9C.jpeg)

### 示例6（设置文本样式）

从API version 12开始，该示例通过[lineHeight](/consumer/cn/doc/harmonyos-references/ts-basic-components-textarea#lineheight12)、[letterSpacing](/consumer/cn/doc/harmonyos-references/ts-basic-components-textarea#letterspacing12)、[decoration](/consumer/cn/doc/harmonyos-references/ts-basic-components-textarea#decoration12)属性展示了不同样式的文本效果。

```
// xxx.ets
@Entry
@Component
struct TextAreaExample {
  build() {
    Row() {
      Column() {
        Text('lineHeight').fontSize(9).fontColor(0xCCCCCC)
        TextArea({ text: 'lineHeight unset' })
          .border({ width: 1 }).padding(10).margin(5)
        TextArea({ text: 'lineHeight 15' })
          .border({ width: 1 }).padding(10).margin(5).lineHeight(15)
        TextArea({ text: 'lineHeight 30' })
          .border({ width: 1 }).padding(10).margin(5).lineHeight(30)

        Text('letterSpacing').fontSize(9).fontColor(0xCCCCCC)
        TextArea({ text: 'letterSpacing 0' })
          .border({ width: 1 }).padding(5).margin(5).letterSpacing(0)
        TextArea({ text: 'letterSpacing 3' })
          .border({ width: 1 }).padding(5).margin(5).letterSpacing(3)
        TextArea({ text: 'letterSpacing -1' })
          .border({ width: 1 }).padding(5).margin(5).letterSpacing(-1)

        Text('decoration').fontSize(9).fontColor(0xCCCCCC)
        TextArea({ text: 'LineThrough, Red\nsecond line' })
          .border({ width: 1 }).padding(5).margin(5)
          .decoration({ type: TextDecorationType.LineThrough, color: Color.Red })
        TextArea({ text: 'Overline, Red, DOTTED\nsecond line' })
          .border({ width: 1 }).padding(5).margin(5)
          .decoration({ type: TextDecorationType.Overline, color: Color.Red, style: TextDecorationStyle.DOTTED })
        TextArea({ text: 'Underline, Red, WAVY\nsecond line' })
          .border({ width: 1 }).padding(5).margin(5)
          .decoration({ type: TextDecorationType.Underline, color: Color.Red, style: TextDecorationStyle.WAVY })
      }.height('90%')
    }
    .width('90%')
    .margin(10)
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170454.39428563387748247703315423494044:50001231000000:2800:589A48B72A03DB412EA3F078FDF759305721558F4EE112D20CA87A9C527637A1.png)

### 示例7（设置文字特性效果）

从API version 12开始，该示例通过[fontFeature](/consumer/cn/doc/harmonyos-references/ts-basic-components-textarea#fontfeature12)属性实现了文本在不同文字特性下的展示效果。

```
// xxx.ets
@Entry
@Component
struct TextAreaExample {
  @State text1: string = 'This is ss01 on : 0123456789';
  @State text2: string = 'This is ss01 off: 0123456789';

  build() {
    Column() {
      TextArea({ text: this.text1 })
        .fontSize(20)
        .margin({ top: 200 })
        .fontFeature("\"ss01\" on")
      TextArea({ text: this.text2 })
        .margin({ top: 10 })
        .fontSize(20)
        .fontFeature("\"ss01\" off")
    }
    .width("90%")
    .margin("5%")
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170454.57717673033650951804528183038642:50001231000000:2800:12ED2144F72552C7E048CB1AA41894EC9F4A9C9C819D4EC10B04E2E4ECF53C2D.png)

### 示例8（自定义键盘避让）

该示例通过[customKeyboard](/consumer/cn/doc/harmonyos-references/ts-basic-components-textarea#customkeyboard10)（从API version 10开始）属性配置[KeyboardOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-richeditor#keyboardoptions12)（从API version 12开始）接口实现了自定义键盘避让的效果。

```
// xxx.ets
@Entry
@Component
struct TextAreaExample {
  controller: TextAreaController = new TextAreaController();
  @State inputValue: string = "";
  @State height1: string | number = '80%';
  @State height2: number = 100;
  @State supportAvoidance: boolean = true;

  // 自定义键盘组件
  @Builder
  CustomKeyboardBuilder() {
    Column() {
      Row() {
        Button('x').onClick(() => {
          // 关闭自定义键盘
          this.controller.stopEditing();
        }).margin(10)
      }

      Grid() {
        ForEach([1, 2, 3, 4, 5, 6, 7, 8, 9, '*', 0, '#'], (item: number | string) => {
          GridItem() {
            Button(item + "")
              .width(110).onClick(() => {
              this.inputValue += item;
            })
          }
        })
      }.maxCount(3).columnsGap(10).rowsGap(10).padding(5)
    }.backgroundColor(Color.Gray)
  }

  build() {
    Column() {
      Row() {
        Button("20%")
          .fontSize(24)
          .onClick(() => {
            this.height1 = "20%";
          })
        Button("80%")
          .fontSize(24)
          .margin({ left: 20 })
          .onClick(() => {
            this.height1 = "80%";
          })
      }
      .justifyContent(FlexAlign.Center)
      .alignItems(VerticalAlign.Bottom)
      .height(this.height1)
      .width("100%")
      .padding({ bottom: 50 })

      TextArea({ controller: this.controller, text: this.inputValue })// 绑定自定义键盘
        .height(100)
        .customKeyboard(this.CustomKeyboardBuilder(), { supportAvoidance: this.supportAvoidance })
        .margin(10)
        .border({ width: 1 })
    }
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170454.54709883466485028984062821034066:50001231000000:2800:5A46D343734784C11EF0B7B45DB517B8A31C8B3B5BE4646C1AE8FB733C9EF39E.gif)

### 示例9（设置文本自适应）

从API version 12开始，该示例通过[minFontSize](/consumer/cn/doc/harmonyos-references/ts-basic-components-textarea#minfontsize12)、[maxFontSize](/consumer/cn/doc/harmonyos-references/ts-basic-components-textarea#maxfontsize12)、[heightAdaptivePolicy](/consumer/cn/doc/harmonyos-references/ts-basic-components-textarea#heightadaptivepolicy12)属性展示了文本自适应字号的效果。

```
// xxx.ets
@Entry
@Component
struct TextAreaExample {
  build() {
    Row() {
      Column() {
        Text('heightAdaptivePolicy').fontSize(9).fontColor(0xCCCCCC)
        TextArea({text: 'This is the text with the height adaptive policy set'})
          .width('80%').height(90).borderWidth(1).margin(1)
          .minFontSize(4)
          .maxFontSize(40)
          .maxLines(3)
          .heightAdaptivePolicy(TextHeightAdaptivePolicy.MAX_LINES_FIRST)
        TextArea({text: 'This is the text with the height adaptive policy set'})
          .width('80%').height(90).borderWidth(1).margin(1)
          .minFontSize(4)
          .maxFontSize(40)
          .maxLines(3)
          .heightAdaptivePolicy(TextHeightAdaptivePolicy.MIN_FONT_SIZE_FIRST)
        TextArea({text: 'This is the text with the height adaptive policy set'})
          .width('80%').height(90).borderWidth(1).margin(1)
          .minFontSize(4)
          .maxFontSize(40)
          .maxLines(3)
          .heightAdaptivePolicy(TextHeightAdaptivePolicy.LAYOUT_CONSTRAINT_FIRST)
      }.height('90%')
    }
    .width('90%')
    .margin(10)
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170454.02470849704062210094873499912620:50001231000000:2800:6D06A7F7DBE2485D230505C540F1B87E4AB8762B0EEFD9983E8028AFB33AF770.png)

### 示例10（设置文本行间距）

从API version 12开始，该示例通过[lineSpacing](/consumer/cn/doc/harmonyos-references/ts-basic-components-textarea#linespacing12)属性展示了文本在不同行间距下的展示效果，同时，配置[LineSpacingOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-text-common#linespacingoptions20对象说明)中的onlyBetweenLines（从API version 20开始）属性，可以设置文本的行间距，是否仅在行与行之间生效。

```
// xxx.ets
import { LengthMetrics } from '@kit.ArkUI';

@Entry
@Component
struct TextAreaExample {
  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Start, justifyContent: FlexAlign.SpaceBetween }) {
      Text('TextArea lineSpacing.').fontSize(9).fontColor(0xCCCCCC)
      TextArea({ text: 'This is the TextArea with no lineSpacing set.' })
        .fontSize(12)
      TextArea({ text: 'This is the TextArea with lineSpacing set to 20_px.' })
        .fontSize(12)
        .lineSpacing(LengthMetrics.px(20))
      TextArea({ text: 'This is the TextArea with lineSpacing set to 20_vp.' })
        .fontSize(12)
        .lineSpacing(LengthMetrics.vp(20))
      TextArea({ text: 'This is the TextArea with lineSpacing set to 20_fp.' })
        .fontSize(12)
        .lineSpacing(LengthMetrics.fp(20))
      TextArea({ text: 'This is the TextArea with lineSpacing set to 20_lpx.' })
        .fontSize(12)
        .lineSpacing(LengthMetrics.lpx(20))
      TextArea({ text: 'This is the TextArea with lineSpacing set to 100%.' })
        .fontSize(12)
        .lineSpacing(LengthMetrics.percent(1))
      TextArea({ text: 'The line spacing of this TextArea is set to 20_px, and the spacing is effective only between the lines.' })
        .fontSize(12)
        .lineSpacing(LengthMetrics.px(20), { onlyBetweenLines: true })
    }.height(600).width(350).padding({ left: 35, right: 35, top: 35 })
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170454.41569238243756712514859027172201:50001231000000:2800:B8697E67356A42414C11462EC2AD14921FCC570A31A52CFC2E7E77C13C0D2678.png)

### 示例11（设置自动填充）

从API version 12开始，该示例通过[contentType](/consumer/cn/doc/harmonyos-references/ts-basic-components-textarea#contenttype12)、[enableAutoFill](/consumer/cn/doc/harmonyos-references/ts-basic-components-textarea#enableautofill12)属性实现了文本自动填充的功能。

```
// xxx.ets
@Entry
@Component
struct TextAreaExample {
  @State text: string = '';

  build() {
    Column() {
      // 邮箱地址自动填充类型
      TextArea({ placeholder: 'input your email...' })
        .width('95%')
        .height(40)
        .margin(20)
        .contentType(ContentType.EMAIL_ADDRESS)
        .enableAutoFill(true)
        .maxLength(20)
      // 街道地址自动填充类型
      TextArea({ placeholder: 'input your street address...' })
        .width('95%')
        .height(40)
        .margin(20)
        .contentType(ContentType.FULL_STREET_ADDRESS)
        .enableAutoFill(true)
        .maxLength(20)
    }.width('100%').height('100%').backgroundColor('#F1F3F5')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170454.82184630555315224356014947860163:50001231000000:2800:FA75F0EC77E6BB1C544514A634E91DCD1B4E54516DF087959F5D309414591A8B.png)

### 示例12（设置折行规则）

从API version 12开始，该示例通过[lineBreakStrategy](/consumer/cn/doc/harmonyos-references/ts-basic-components-textarea#linebreakstrategy12)属性实现了TextArea不同折行规则下的效果。

```
// xxx.ets
@Entry
@Component
struct TextAreaExample {
  @State message1: string =
    "They can be classified as built-in components–those directly provided by the ArkUI framework and custom components – those defined by developers" +
      "The built-in components include buttons radio buttonsprogress indicators and text You can set the rendering effect of these components in method chaining mode," +
      "page components are divided into independent UI units to implement independent creation development and reuse of different units on pages making pages more engineering-oriented.";
  @State lineBreakStrategyIndex: number = 0;
  @State lineBreakStrategy: LineBreakStrategy[] =
    [LineBreakStrategy.GREEDY, LineBreakStrategy.HIGH_QUALITY, LineBreakStrategy.BALANCED];
  @State lineBreakStrategyStr: string[] = ['GREEDY', 'HIGH_QUALITY', 'BALANCED'];

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Start }) {
      Text('lineBreakStrategy').fontSize(9).fontColor(0xCCCCCC)
      TextArea({ text: this.message1 })
        .fontSize(12)
        .border({ width: 1 })
        .padding(10)
        .width('100%')
        .lineBreakStrategy(this.lineBreakStrategy[this.lineBreakStrategyIndex])
      Row() {
        Button('当前lineBreakStrategy模式：' + this.lineBreakStrategyStr[this.lineBreakStrategyIndex]).onClick(() => {
          this.lineBreakStrategyIndex++;
          if (this.lineBreakStrategyIndex > (this.lineBreakStrategyStr.length - 1)) {
            this.lineBreakStrategyIndex = 0;
          }
        })
      }.padding({ top: 10 })
    }.height(700).width(370).padding({ left: 35, right: 35, top: 35 })
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170454.61647195951505122577954982849597:50001231000000:2800:3AF1D2CBAF938D1DCCC2FC75F0A30AAD1A23E42B88F8DDB7244967AF8B061CA8.gif)

### 示例13（支持插入和删除回调）

从API version 12开始，该示例通过[onWillInsert](/consumer/cn/doc/harmonyos-references/ts-basic-components-textarea#onwillinsert12)、[onDidInsert](/consumer/cn/doc/harmonyos-references/ts-basic-components-textarea#ondidinsert12)、[onWillDelete](/consumer/cn/doc/harmonyos-references/ts-basic-components-textarea#onwilldelete12)、[onDidDelete](/consumer/cn/doc/harmonyos-references/ts-basic-components-textarea#ondiddelete12)接口实现了插入和删除的功能。

```
// xxx.ets
@Entry
@Component
struct TextAreaExample {
  @State insertValue: string = "";
  @State deleteValue: string = "";
  @State insertOffset: number = 0;
  @State deleteOffset: number = 0;
  @State deleteDirection: number = 0;

  build() {
    Row() {
      Column() {
        TextArea({ text: "TextArea支持插入回调文本" })
          .width(300)
          .height(60)
          .onWillInsert((info: InsertValue) => {
            this.insertValue = info.insertValue;
            return true;
          })
          .onDidInsert((info: InsertValue) => {
            this.insertOffset = info.insertOffset;
          })

        Text("insertValue:" + this.insertValue + "  insertOffset:" + this.insertOffset).height(30)

        TextArea({ text: "TextArea支持删除回调文本b" })
          .width(300)
          .height(60)
          .onWillDelete((info: DeleteValue) => {
            this.deleteValue = info.deleteValue;
            this.deleteDirection = info.direction;
            return true;
          })
          .onDidDelete((info: DeleteValue) => {
            this.deleteOffset = info.deleteOffset;
            this.deleteDirection = info.direction;
          })

        Text("deleteValue:" + this.deleteValue + "  deleteOffset:" + this.deleteOffset).height(30)
        Text("deleteDirection:" + (this.deleteDirection == 0 ? "BACKWARD" : "FORWARD")).height(30)

      }.width('100%')
    }
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170454.35983157854824430632173779795259:50001231000000:2800:FEFD71520A080B8846C4E552CFD9BFA609E08D6A882097FC65BF98F7C15D79A2.png)

### 示例14（文本扩展自定义菜单）

从API version 12开始，该示例通过[editMenuOptions](/consumer/cn/doc/harmonyos-references/ts-basic-components-textarea#editmenuoptions12)接口实现了文本设置自定义菜单扩展项的文本内容、图标以及回调的功能，同时，可以在[onPrepareMenu](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-text-common#属性-1)（从API version 20开始）回调中，进行菜单数据的设置。

```
// xxx.ets
@Entry
@Component
struct TextAreaExample {
  @State text: string = 'TextArea editMenuOptions';
  @State endIndex: number = 0;
  onCreateMenu = (menuItems: Array<TextMenuItem>) => {
    // $r('app.media.startIcon')需要替换为开发者所需的图像资源文件。
    let item1: TextMenuItem = {
      content: 'create1',
      icon: $r('app.media.startIcon'),
      id: TextMenuItemId.of('create1'),
    };
    let item2: TextMenuItem = {
      content: 'create2',
      id: TextMenuItemId.of('create2'),
      icon: $r('app.media.startIcon'),
    };
    menuItems.push(item1);
    menuItems.unshift(item2);
    return menuItems;
  }
  onMenuItemClick = (menuItem: TextMenuItem, textRange: TextRange) => {
    if (menuItem.id.equals(TextMenuItemId.of("create2"))) {
      console.info("拦截 id: create2 start:" + textRange.start + "; end:" + textRange.end);
      return true;
    }
    if (menuItem.id.equals(TextMenuItemId.of("prepare1"))) {
      console.info("拦截 id: prepare1 start:" + textRange.start + "; end:" + textRange.end);
      return true;
    }
    if (menuItem.id.equals(TextMenuItemId.COPY)) {
      console.info("拦截 COPY start:" + textRange.start + "; end:" + textRange.end);
      return true;
    }
    if (menuItem.id.equals(TextMenuItemId.SELECT_ALL)) {
      console.info("不拦截 SELECT_ALL start:" + textRange.start + "; end:" + textRange.end);
      return false;
    }
    return false;
  }
  onPrepareMenu = (menuItems: Array<TextMenuItem>) => {
    // $r('app.media.startIcon')需要替换为开发者所需的图像资源文件。
    let item1: TextMenuItem = {
      content: 'prepare1_' + this.endIndex,
      icon: $r('app.media.startIcon'),
      id: TextMenuItemId.of('prepare1'),
    };
    menuItems.unshift(item1);
    return menuItems;
  }
  @State editMenuOptions: EditMenuOptions = {
    onCreateMenu: this.onCreateMenu,
    onMenuItemClick: this.onMenuItemClick,
    onPrepareMenu: this.onPrepareMenu
  };

  build() {
    Column() {
      TextArea({ text: this.text })
        .width('95%')
        .height(56)
        .editMenuOptions(this.editMenuOptions)
        .margin({ top: 100 })
        .onTextSelectionChange((selectionStart: number, selectionEnd: number) => {
          this.endIndex = selectionEnd;
        })
    }
    .width("90%")
    .margin("5%")
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170454.63324702451467781599531549329564:50001231000000:2800:DA22489929F70B6AFBF3073FAB3EDD5AFF2E2F581B3E47F2BAE32B18860FF569.png)

### 示例15（文本设置省略模式）

该示例通过[textOverflow](/consumer/cn/doc/harmonyos-references/ts-basic-components-textarea#textoverflow12)（从API version 12开始）、[ellipsisMode](/consumer/cn/doc/harmonyos-references/ts-basic-components-textarea#ellipsismode18)（从API version 18开始）、[maxLines](/consumer/cn/doc/harmonyos-references/ts-basic-components-textarea#maxlines10)（从API version 10开始）属性展示了文本超长省略以及调整省略位置的效果。

```
// xxx.ets
@Entry
@Component
struct EllipsisModeExample {
  @State textIndex: number = 0;
  @State text: string = "As the sun begins to set, casting a warm golden hue across the sky," +
    "the world seems to slow down and breathe a sigh of relief. The sky is painted with hues of orange, " +
    " pink, and lavender, creating a breath taking tapestry that stretches as far as the eye can see." +
    "The air is filled with the sweet scent of blooming flowers, mingling with the earthy aroma of freshly turned soil.";
  @State ellipsisModeIndex: number = 0;
  @State ellipsisMode: (EllipsisMode | undefined | null)[] =
    [EllipsisMode.START, EllipsisMode.END, EllipsisMode.CENTER, undefined, null];
  @State ellipsisModeStr: string[] = ['START ', 'END', 'CENTER', 'undefined', 'null'];
  @State textOverflowIndex: number = 0;
  @State textOverflow: TextOverflow[] = [TextOverflow.Ellipsis, TextOverflow.Clip];
  @State textOverflowStr: string[] = ['Ellipsis', 'Clip'];
  @State maxLinesIndex: number = 0;
  @State maxLines: number[] = [1, 2, 3];
  @State maxLinesStr: string[] = ['1', '2', '3'];
  @State styleAreaIndex: number = 0;
  @State styleArea: TextContentStyle[] = [TextContentStyle.INLINE, TextContentStyle.DEFAULT];
  @State styleAreaStr: string[] = ['INLINE', 'DEFAULT'];

  build() {
    Column({ space: 20 }) {
      TextArea({ text: this.text })
        .textOverflow(this.textOverflow[this.textOverflowIndex])
        .ellipsisMode(this.ellipsisMode[this.ellipsisModeIndex])
        .maxLines(this.maxLines[this.maxLinesIndex])
        .style(this.styleArea[this.styleAreaIndex])
        .fontSize(30)
        .margin(30)

      Button('更改ellipsisMode模式：' + this.ellipsisModeStr[this.ellipsisModeIndex]).onClick(() => {
        this.ellipsisModeIndex++;
        if (this.ellipsisModeIndex > (this.ellipsisModeStr.length - 1)) {
          this.ellipsisModeIndex = 0;
        }
      }).fontSize(20)
      Button('更改textOverflow模式：' + this.textOverflowStr[this.textOverflowIndex]).onClick(() => {
        this.textOverflowIndex++;
        if (this.textOverflowIndex > (this.textOverflowStr.length - 1)) {
          this.textOverflowIndex = 0;
        }
      }).fontSize(20)
      Button('更改maxLines大小：' + this.maxLinesStr[this.maxLinesIndex]).onClick(() => {
        this.maxLinesIndex++;
        if (this.maxLinesIndex > (this.maxLinesStr.length - 1)) {
          this.maxLinesIndex = 0;
        }
      }).fontSize(20)
      Button('更改Style大小：' + this.styleAreaStr[this.styleAreaIndex]).onClick(() => {
        this.styleAreaIndex++;
        if (this.styleAreaIndex > (this.styleAreaStr.length - 1)) {
          this.styleAreaIndex = 0;
        }
      }).fontSize(20)
    }.height(600).width('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170454.81253620698912324202346370789204:50001231000000:2800:9FDF8C2F547B6B05B36C0396DE7674BFBB37CF6BE641DEEE3EA425EF8EE1B16D.png)

### 示例16（自定义复制、剪切、粘贴）

该示例通过[onCopy](/consumer/cn/doc/harmonyos-references/ts-basic-components-textarea#oncopy8)、[onCut](/consumer/cn/doc/harmonyos-references/ts-basic-components-textarea#oncut8)、[onPaste](/consumer/cn/doc/harmonyos-references/ts-basic-components-textarea#onpaste)展示如何监听文本选择菜单的复制、剪切、粘贴按钮，以及如何屏蔽系统粘贴功能并实现自定义的粘贴能力，同时，可以通过[maxFontScale](/consumer/cn/doc/harmonyos-references/ts-basic-components-textarea#maxfontscale18)、[minFontScale](/consumer/cn/doc/harmonyos-references/ts-basic-components-textarea#minfontscale18)属性设置文本最大和最小的字体缩放倍数。

```
// xxx.ets
@Entry
@Component
struct TextAreaExample {
  @State text: string = '';
  controller: TextAreaController = new TextAreaController();

  build() {
    Column() {
      TextArea({
        text: this.text,
        placeholder: 'placeholder',
        controller: this.controller
      })
        .placeholderColor(Color.Red)
        .textAlign(TextAlign.Center)
        .caretColor(Color.Green)
        .caretStyle({ width: '2vp' })
        .fontStyle(FontStyle.Italic)
        .fontWeight(FontWeight.Bold)
        .fontFamily('HarmonyOS Sans')
        .inputFilter('[a-zA-Z]+', (value) => { // 只允许字母输入
          console.error(`unsupported char ${value}`);
        })
        .copyOption(CopyOptions.LocalDevice)
        .enableKeyboardOnFocus(false)
        .selectionMenuHidden(false)
        .barState(BarState.On)
        .type(TextAreaType.NORMAL)
        .selectedBackgroundColor(Color.Orange)
        .textIndent(2)
        .halfLeading(true)
        .minFontScale(1)
        .maxFontScale(2)
        .enablePreviewText(true)
        .enableHapticFeedback(true)
        .stopBackPress(false)// 返回键交给其他组件处理
        .width(336)
        .height(56)
        .margin(20)
        .fontSize(16)
        .onEditChange((isEditing: boolean) => {
          console.info(`isEditing ${isEditing}`);
        })
        .onCopy((value) => {
          console.info(`copy ${value}`);
        })
        .onCut((value) => {
          console.info(`cut ${value}`);
        })
        .onPaste((value, event) => {
          // 阻止系统粘贴功能，开发者可自行实现
          if (event.preventDefault) {
            event.preventDefault();
          }
          console.info(`paste:${value}`);
          this.text = value;
        })
        .onTextSelectionChange((start: number, end: number) => {
          console.info(`onTextSelectionChange start ${start}, end ${end}`);
        })
        .onContentScroll((totalOffsetX: number, totalOffsetY: number) => {
          console.info(`onContentScroll offsetX ${totalOffsetX}, offsetY ${totalOffsetY}`);
        })
    }.width('100%').height('100%').backgroundColor('#F1F3F5')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170455.00742446680005954094691318042071:50001231000000:2800:5756B776A300D4104D856F7DCBA8598F8F2E8207A1F52677E7D3FDEEC40331AC.png)

### 示例17（设置最小字体范围与最大字体范围）

从API version 18开始，该示例通过[minFontScale](/consumer/cn/doc/harmonyos-references/ts-basic-components-textarea#minfontscale18)、[maxFontScale](/consumer/cn/doc/harmonyos-references/ts-basic-components-textarea#maxfontscale18)设置字体显示最小与最大范围。

```
// 开启应用缩放跟随系统
// AppScope/resources/base，新建文件夹profile。
// AppScope/resources/base/profile，新建文件configuration.json。
// AppScope/resources/base/profile/configuration.json，增加如下代码。
{
  "configuration": {
    "fontSizeScale": "followSystem",
    "fontSizeMaxScale": "3.2"
  }
}
```

```
// AppScope/app.json5，修改如下代码。
{
  "app": {
    "bundleName": "com.example.myapplication",
    "vendor": "example",
    "versionCode": 1000000,
    "versionName": "1.0.0",
    "icon": "$media:app_icon",
    "label": "$string:app_name",
    "configuration": "$profile:configuration"
  }
}
```

```
// xxx.ets
@Entry
@Component
struct TextAreaExample {
  @State minFontScale: number = 0.85;
  @State maxFontScale: number = 2;

  build() {
    Column() {
      Column({ space: 30 }) {
        Text("通过minFontScale、maxFontScale调整文本显示的最大和最小字体缩放倍数。")
        TextArea({
          placeholder: 'The text area can hold an unlimited amount of text. input your word...',
          text: '通过minFontScale、maxFontScale调整文本显示的最大和最小字体缩放倍数。'
        })
          .minFontScale(this.minFontScale)// 设置最小字体缩放倍数，参数为undefined则跟随系统默认倍数缩放
          .maxFontScale(this.maxFontScale) // 设置最大字体缩放倍数，参数为undefined则跟随系统默认倍数缩放
      }.width('100%')
    }
  }
}
```

### 示例18（设置选中指定区域的文本内容）

从API version 10开始，该示例通过[setTextSelection](/consumer/cn/doc/harmonyos-references/ts-basic-components-textarea#settextselection10)方法展示如何设置选中指定区域的文本内容以及菜单的显隐策略。

```
// xxx.ets

@Entry
@Component
struct TextAreaExample {
  controller: TextAreaController = new TextAreaController();
  @State startIndex: number = 0;
  @State endIndex: number = 0;

  build() {
    Column({ space: 3 }) {
      Text('Selection start:' + this.startIndex + ' end:' + this.endIndex)
      TextArea({ text: 'Hello World', controller: this.controller })
        .width('95%')
        .height(80)
        .margin(10)
        .defaultFocus(true)
        .enableKeyboardOnFocus(true)
        .onTextSelectionChange((selectionStart: number, selectionEnd: number) => {
          this.startIndex = selectionStart;
          this.endIndex = selectionEnd;
        })

      Button('setTextSelection [0,3], set menuPolicy is MenuPolicy.SHOW')
        .onClick(() => {
          this.controller.setTextSelection(0, 3, { menuPolicy: MenuPolicy.SHOW });
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170455.93859813595756930737154800678069:50001231000000:2800:1BFC0D38A97567136EAF493E0EDE596228492D995B0FA8A82334D1DA3825D676.png)

### 示例19（设置文本描边）

从API version 20开始，该示例通过[strokeWidth](/consumer/cn/doc/harmonyos-references/ts-basic-components-textarea#strokewidth20)和[strokeColor](/consumer/cn/doc/harmonyos-references/ts-basic-components-textarea#strokecolor20)属性设置文本的描边宽度及颜色。

```
// xxx.ets
import { LengthMetrics } from '@kit.ArkUI';

@Entry
@Component
struct TextAreaExample {
  build() {
    Row() {
      Column() {
        Text('stroke feature').fontSize(9).fontColor(0xCCCCCC)

        TextArea({ text: 'Text without stroke' })
          .width('100%')
          .height(60)
          .borderWidth(1)
          .fontSize(40)
        TextArea({ text: 'Text with stroke' })
          .width('100%')
          .height(60)
          .borderWidth(1)
          .fontSize(40)
          .strokeWidth(LengthMetrics.px(-3.0))
          .strokeColor(Color.Red)
        TextArea({ text: 'Text with stroke' })
          .width('100%')
          .height(60)
          .borderWidth(1)
          .fontSize(40)
          .strokeWidth(LengthMetrics.px(3.0))
          .strokeColor(Color.Red)
      }.height('90%')
    }
    .width('90%')
    .margin(10)
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170455.08161129855057429260400898819502:50001231000000:2800:09BAE2C0EC48DC1F571C207096EC91F73F3CC022055B7A4E53ED000892244DDA.png)

### 示例20（设置中西文自动间距）

从API version 20开始，该示例通过[enableAutoSpacing](/consumer/cn/doc/harmonyos-references/ts-basic-components-textarea#enableautospacing20)属性设置中西文自动间距。

```
// xxx.ets
@Entry
@Component
struct TextAreaExample {
  build() {
    Row() {
      Column() {
        Text('开启中西文自动间距').margin(5)
        TextArea({text: '中西文Auto Spacing自动间距'})
          .enableAutoSpacing(true)
        Text('关闭中西文自动间距').margin(5)
        TextArea({text: '中西文Auto Spacing自动间距'})
          .enableAutoSpacing(false)
      }.height('100%')
    }
    .width('60%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170455.78570142903532716363627173898483:50001231000000:2800:2F5B5D1DDABBB0E622B02DF5C40CDB20725F2C770F8BC06F465E3CF9EFE9960B.png)

### 示例21（设置最大行数）

从API version 20开始，该示例通过[maxLines](/consumer/cn/doc/harmonyos-references/ts-basic-components-textarea#maxlines20)属性设置显示最大行数，超出最大行数后可滚动。

```
// xxx.ets
@Entry
@Component
struct TextAreaExample {
  build() {
    Row() {
      Column() {
        TextArea({ text: '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20' })
          .fontSize(50)
          .width('50%')
          .borderWidth(1)
          .margin(100)
          .textOverflow(TextOverflow.Clip)
          .maxLines(3, { overflowMode: MaxLinesMode.SCROLL })
      }.height('90%')
    }
    .width('90%')
    .margin(10)
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170455.61483980425385416878083198457125:50001231000000:2800:D8D36D368A20363E7FB5E8ABFAAE512D15B5F6E3181BC6A22AC10B3189433909.gif)

### 示例22（设置最小行数）

从API version 20开始，该示例通过[minLines](/consumer/cn/doc/harmonyos-references/ts-basic-components-textarea#minlines20)属性设置显示的最小行数。

```
// xxx.ets
@Entry
@Component
struct Index {
  @State message: string = 'Hello World';

  build() {
    Row() {
      Column() {
        TextArea({ text: this.message })
          .width('95%')
          .fontSize(20)
          .margin(10)
          .minLines(3)
      }
    }
    .width('90%')
    .margin(10)
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170455.64559598066171993827262505293836:50001231000000:2800:03C3F7F112973BC20D6568613C6343A760CD69F5EE542594D1F5DAB2C092F5EA.png)

### 示例23（设置字符计数颜色以及超出字符颜色）

从API version 22开始，该示例通过[showCounter](/consumer/cn/doc/harmonyos-references/ts-basic-components-textarea#showcounter10)属性的counterTextColor和counterTextOverflowColor设置字符计数颜色以及超出字符颜色。

```
import { ColorMetrics } from '@kit.ArkUI';

// xxx.ets
@Entry
@Component
struct TextAreaExample {
  @State text: string = '';
  controller: TextAreaController = new TextAreaController();

  build() {
    Column() {
      TextArea({
        text: this.text,
        placeholder: 'The text area can hold an unlimited amount of text. input your word...',
        controller: this.controller
      })
        .placeholderFont({ size: 16, weight: 400 })
        .width(336)
        .height(56)
        .margin(20)
        .fontSize(16)
        .fontColor('#182431')
        .backgroundColor('#FFFFFF')
        .maxLength(4)
        .showCounter(true, {
          thresholdPercentage: 50,
          highlightBorder: true,
          counterTextColor: ColorMetrics.resourceColor(Color.Red),
          counterTextOverflowColor: ColorMetrics.resourceColor(Color.Orange)
        })
    }.width('100%').height('100%').backgroundColor('#F1F3F5')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170455.82802176078347606257413739505586:50001231000000:2800:E3765D9AD45E7EB1800FF75F06F422D0F6B2BA968EA3957A720DF7DF28041A1C.gif)

### 示例24（设置滚动条颜色）

从API version 22开始，该示例通过[scrollBarColor](/consumer/cn/doc/harmonyos-references/ts-basic-components-textarea#scrollbarcolor22)属性设置滚动条颜色。

```
// xxx.ets
import { ColorMetrics } from '@kit.ArkUI';
@Entry
@Component
struct Index {
  controller: TextAreaController = new TextAreaController();
  build() {
      Column() {
        TextArea({
          text: "Hello World TextArea",
          placeholder: 'Type to text area...',
          controller: this.controller
        })
          .width(336)
          .height(56)
          .margin({bottom:5})
          .fontSize(16)
          .fontColor('#182431')
          .backgroundColor('#FFFFFF')
          .barState(BarState.On)
          .scrollBarColor(undefined)
        TextArea({
          text: "Hello World TextArea",
          placeholder: 'Type to text area...',
          controller: this.controller
        })
          .width(336)
          .height(56)
          .margin({bottom:5})
          .fontSize(16)
          .fontColor('#182431')
          .backgroundColor('#FFFFFF')
          .barState(BarState.On)
          .scrollBarColor(ColorMetrics.resourceColor(Color.Orange))
        TextArea({
          text: "Hello World TextArea",
          placeholder: 'Type to text area...',
          controller: this.controller
        })
          .width(336)
          .height(56)
          .margin({bottom:5})
          .fontSize(16)
          .fontColor('#182431')
          .backgroundColor('#FFFFFF')
          .barState(BarState.On)
          .scrollBarColor(ColorMetrics.rgba(255, 100, 255))
      }
      .backgroundColor(Color.Blue).width('100%').height('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170455.73458382393639952080985508261998:50001231000000:2800:4CAF8E0735E13CACA48BE36216D2139F4A431BBA81CEC51888F4FA7C0DE340D5.jpg)

### 示例25（设置placeholder富文本样式）

从API version 22开始，该示例通过[setStyledPlaceholder](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-text-style#setstyledplaceholder22)接口设置placeholder富文本样式。

```
// xxx.ets
import { LengthMetrics } from '@kit.ArkUI';

@Entry
@Component
struct TextAreaExample {
  styledString: MutableStyledString =
    new MutableStyledString("段落标题\n正文第一段\n正文第二段indent 40 vp\n正文第三段textAlign居中对齐",
      [
        {
          start: 0,
          length: 4,
          styledKey: StyledStringKey.FONT,
          styledValue: new TextStyle({ fontSize: LengthMetrics.vp(24), fontWeight: FontWeight.Bolder })
        },
        {
          start: 5,
          length: 5,
          styledKey: StyledStringKey.FONT,
          styledValue: new TextStyle({ fontColor: Color.Gray })
        },
        {
          start: 11,
          length: 1,
          styledKey: StyledStringKey.PARAGRAPH_STYLE,
          styledValue: new ParagraphStyle({
            textIndent: LengthMetrics.vp(40),
            maxLines: 1,
            overflow: TextOverflow.Ellipsis
          })
        },
        {
          start: 29,
          length: 1,
          styledKey: StyledStringKey.PARAGRAPH_STYLE,
          styledValue: new ParagraphStyle({
            textAlign: TextAlign.Center
          })
        }
      ]);
  controller: TextAreaController = new TextAreaController();

  aboutToAppear() {
    this.controller.setStyledPlaceholder(this.styledString)
  }

  build() {
    Scroll() {
      Column() {
        Text("TextArea placeholder富文本")
          .fontSize(8)
        TextArea({ controller: this.controller })
          .width(200)
          .fontSize(24)
          .margin(10)
      }
      .width('100%')
    }
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170455.26493199908000734342033004175558:50001231000000:2800:830563B0C390E2C3618104AEF04829E9B8564143AA66349CF4F40DF237A26BBE.jpg)

### 示例26（设置输入法扩展信息）

从API version 22开始，该示例通过[IMEClient](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-text-common#imeclient20对象说明)的setExtraConfig设置输入法扩展信息。

```
// xxx.ets
@Entry
@Component
struct TextAreaExample {
  build() {
    Column() {
      TextArea({ text: '拉起输入法前执行onWillAttachIME回调' })
        .onWillAttachIME((client: IMEClient) => {
          client.setExtraConfig({
            customSettings: {
              name: "TextArea", // 自定义属性
              id: client.nodeId // 自定义属性
            }
          })
        })
    }.height('100%')
  }
}
```