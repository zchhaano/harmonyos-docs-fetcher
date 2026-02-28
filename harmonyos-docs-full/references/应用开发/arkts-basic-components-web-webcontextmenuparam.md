# Class (WebContextMenuParam)

实现长按页面元素或鼠标右键弹出来的菜单信息。示例代码参考[onContextMenuShow事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-events#oncontextmenushow9)。

 说明 

- 该组件首批接口从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
- 本Class首批接口从API version 9开始支持。
- 示例效果请以真机运行为准。

## constructor 9+

支持设备PhonePC/2in1TabletTVWearable

constructor()

WebContextMenuParam的构造函数。

**系统能力：** SystemCapability.Web.Webview.Core

## x 9+

支持设备PhonePC/2in1TabletTVWearable

x(): number

弹出菜单的x坐标。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

 展开

| 类型 | 说明 |
| --- | --- |
| number | 显示正常返回非负整数，否则返回-1。 单位：vp。 |

## y 9+

支持设备PhonePC/2in1TabletTVWearable

y(): number

弹出菜单的y坐标。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

 展开

| 类型 | 说明 |
| --- | --- |
| number | 显示正常返回非负整数，否则返回-1。 单位：vp。 |

## getLinkUrl 9+

支持设备PhonePC/2in1TabletTVWearable

getLinkUrl(): string

获取经过安全检查的url链接地址。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

 展开

| 类型 | 说明 |
| --- | --- |
| string | 如果长按位置是链接，返回经过安全检查的url链接。 |

## getUnfilteredLinkUrl 9+

支持设备PhonePC/2in1TabletTVWearable

getUnfilteredLinkUrl(): string

获取原始url链接地址。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

 展开

| 类型 | 说明 |
| --- | --- |
| string | 如果长按位置是链接，返回原始的url链接。 |

## getSourceUrl 9+

支持设备PhonePC/2in1TabletTVWearable

getSourceUrl(): string

获取sourceUrl链接。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

 展开

| 类型 | 说明 |
| --- | --- |
| string | 如果选中的元素有src属性，返回src的url。返回url的最大上限为2M，超出上限时返回空字符串。 |

## existsImageContents 9+

支持设备PhonePC/2in1TabletTVWearable

existsImageContents(): boolean

是否存在图像内容。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

 展开

| 类型 | 说明 |
| --- | --- |
| boolean | 长按位置中有图片返回true，否则返回false。 |

## getMediaType 9+

支持设备PhonePC/2in1TabletTVWearable

getMediaType(): ContextMenuMediaType

获取网页元素媒体类型。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

 展开

| 类型 | 说明 |
| --- | --- |
| ContextMenuMediaType | 网页元素媒体类型。 |

## getSelectionText 9+

支持设备PhonePC/2in1TabletTVWearable

getSelectionText(): string

获取选中文本。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

 展开

| 类型 | 说明 |
| --- | --- |
| string | 菜单上下文选中文本内容，不存在则返回空。 |

## getSourceType 9+

支持设备PhonePC/2in1TabletTVWearable

getSourceType(): ContextMenuSourceType

获取菜单事件来源。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

 展开

| 类型 | 说明 |
| --- | --- |
| ContextMenuSourceType | 菜单事件来源。 |

## getInputFieldType 9+

支持设备PhonePC/2in1TabletTVWearable

getInputFieldType(): ContextMenuInputFieldType

获取网页元素输入框类型。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

 展开

| 类型 | 说明 |
| --- | --- |
| ContextMenuInputFieldType | 输入框类型。 |

## isEditable 9+

支持设备PhonePC/2in1TabletTVWearable

isEditable(): boolean

获取网页元素是否可编辑标识。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

 展开

| 类型 | 说明 |
| --- | --- |
| boolean | 网页元素可编辑返回true，不可编辑返回false。 |

## getEditStateFlags 9+

支持设备PhonePC/2in1TabletTVWearable

getEditStateFlags(): number

获取网页元素可编辑标识。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

 展开

| 类型 | 说明 |
| --- | --- |
| number | 网页元素可编辑标识，参照 ContextMenuEditStateFlags 。 |

## getPreviewWidth 13+

支持设备PhonePC/2in1TabletTVWearable

getPreviewWidth(): number

获取预览图的宽。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

 展开

| 类型 | 说明 |
| --- | --- |
| number | 预览图的宽。 单位：vp。 |

## getPreviewHeight 13+

支持设备PhonePC/2in1TabletTVWearable

getPreviewHeight(): number

获取预览图的高。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

 展开

| 类型 | 说明 |
| --- | --- |
| number | 预览图的高。 单位：vp。 |

## getContextMenuMediaType 22+

支持设备PhonePC/2in1TabletTVWearable

getContextMenuMediaType(): ContextMenuDataMediaType

在上报上下文菜单事件时，获取用户点击的网页元素类型。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

 展开

| 类型 | 说明 |
| --- | --- |
| ContextMenuDataMediaType | 网页元素媒体类型。 |