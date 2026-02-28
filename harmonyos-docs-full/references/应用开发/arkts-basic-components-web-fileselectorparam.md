# Class (FileSelectorParam)

Web组件获取文件对象。示例代码参考[onShowFileSelector事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-events#onshowfileselector9)。

 说明 

- 该组件首批接口从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
- 本Class首批接口从API version 9开始支持。
- 示例效果请以真机运行为准。

## constructor 9+

支持设备PhonePC/2in1TabletTVWearable

constructor()

FileSelectorParam的构造函数。

**系统能力：** SystemCapability.Web.Webview.Core

## getTitle 9+

支持设备PhonePC/2in1TabletTVWearable

getTitle(): string

获取文件选择器标题。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

 展开

| 类型 | 说明 |
| --- | --- |
| string | 返回文件选择器标题。 |

## getMode 9+

支持设备PhonePC/2in1TabletTVWearable

getMode(): FileSelectorMode

获取文件选择器的模式。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

 展开

| 类型 | 说明 |
| --- | --- |
| FileSelectorMode | 返回文件选择器的模式。 |

## getAcceptType 9+

支持设备PhonePC/2in1TabletTVWearable

getAcceptType(): Array<string>

获取文件过滤类型。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

 展开

| 类型 | 说明 |
| --- | --- |
| Array<string> | 返回文件过滤类型。 |

## isCapture 9+

支持设备PhonePC/2in1TabletTVWearable

isCapture(): boolean

获取是否调用多媒体能力。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

 展开

| 类型 | 说明 |
| --- | --- |
| boolean | 返回是否调用多媒体能力。 true表示返回调用多媒体能力，false表示返回未调用多媒体能力。 |

## getMimeTypes 18+

支持设备PhonePC/2in1TabletTVWearable

getMimeTypes(): Array<string>

获取文件MIME类型。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

 展开

| 类型 | 说明 |
| --- | --- |
| Array<string> | 返回文件MIME类型。 |