# Class (WebContextMenuResult)

实现长按页面元素或鼠标右键弹出来的菜单所执行的响应事件。示例代码参考[onContextMenuShow事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-events#oncontextmenushow9)。

 说明 

- 该组件首批接口从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
- 本Class首批接口从API version 9开始支持。
- 示例效果请以真机运行为准。

## constructor 9+

支持设备PhonePC/2in1TabletTVWearable

constructor()

WebContextMenuResult的构造函数。

**系统能力：** SystemCapability.Web.Webview.Core

## closeContextMenu 9+

支持设备PhonePC/2in1TabletTVWearable

closeContextMenu(): void

不执行WebContextMenuResult其他接口操作时，需要调用此接口关闭菜单。

**系统能力：** SystemCapability.Web.Webview.Core

## copyImage 9+

支持设备PhonePC/2in1TabletTVWearable

copyImage(): void

WebContextMenuParam有图片内容则复制图片。

**系统能力：** SystemCapability.Web.Webview.Core

## copy 9+

支持设备PhonePC/2in1TabletTVWearable

copy(): void

执行与此上下文菜单相关的拷贝文本操作。

**系统能力：** SystemCapability.Web.Webview.Core

## paste 9+

支持设备PhonePC/2in1TabletTVWearable

paste(): void

执行与此上下文菜单相关的粘贴操作。

 说明 

需要配置权限：ohos.permission.READ_PASTEBOARD。

**系统能力：** SystemCapability.Web.Webview.Core

## cut 9+

支持设备PhonePC/2in1TabletTVWearable

cut(): void

执行与此上下文菜单相关的剪切操作。

**系统能力：** SystemCapability.Web.Webview.Core

## selectAll 9+

支持设备PhonePC/2in1TabletTVWearable

selectAll(): void

执行与此上下文菜单相关的全选操作。

**系统能力：** SystemCapability.Web.Webview.Core

## undo 20+

支持设备PhonePC/2in1TabletTVWearable

undo(): void

执行与此上下文菜单相关的撤销操作。

**系统能力：** SystemCapability.Web.Webview.Core

## redo 20+

支持设备PhonePC/2in1TabletTVWearable

redo(): void

执行与此上下文菜单相关的重做操作，即取消用户上一次的撤销操作。

**系统能力：** SystemCapability.Web.Webview.Core

## pasteAndMatchStyle 20+

支持设备PhonePC/2in1TabletTVWearable

pasteAndMatchStyle(): void

执行一个和上下文菜单相关的粘贴操作，粘贴的内容会匹配目标格式，以纯文本形式呈现。

 说明 

需要配置权限：ohos.permission.READ_PASTEBOARD。

**系统能力：** SystemCapability.Web.Webview.Core