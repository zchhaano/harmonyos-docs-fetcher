# Class (WebResourceHandler)

通过WebResourceHandler，可以提供自定义的返回头以及返回体给Web组件。

 说明 

- 本模块首批接口从API version 9开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
- 本Class首批接口从API version 12开始支持。
- 示例效果请以真机运行为准。

## 导入模块

 支持设备PhonePC/2in1TabletTVWearable收起自动换行深色代码主题复制

```
import { webview } from '@kit.ArkWeb' ;
```

## didReceiveResponse 12+

 支持设备PhonePC/2in1TabletTVWearable

didReceiveResponse(response: WebSchemeHandlerResponse): void

将构造的响应头传递给被拦截的请求。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| response | WebSchemeHandlerResponse | 是 | 该拦截请求的响应。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-webview)、[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

  展开

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. |
| 17100021 | The resource handler is invalid. |

**示例：**

示例请参考[OnRequestStart](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webschemehandler#onrequeststart12)。

## didReceiveResponseBody 12+

 支持设备PhonePC/2in1TabletTVWearable

didReceiveResponseBody(data: ArrayBuffer): void

将构造的响应体传递给被拦截的请求。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | ArrayBuffer | 是 | 响应体数据。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-webview)、[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

  展开

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. |
| 17100021 | The resource handler is invalid. |

**示例：**

示例请参考[OnRequestStart](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webschemehandler#onrequeststart12)。

## didFinish 12+

 支持设备PhonePC/2in1TabletTVWearable

didFinish(): void

通知Web组件被拦截的请求已经完成，并且没有更多的数据可用，调用前需要优先调用[didReceiveResponse](/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webresourcehandler#didreceiveresponse12)将构造的响应头传递给被拦截的请求。

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-webview)。

  展开

| 错误码ID | 错误信息 |
| --- | --- |
| 17100021 | The resource handler is invalid. |

**示例：**

示例请参考[OnRequestStart](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webschemehandler#onrequeststart12)。

## didFail 12+

 支持设备PhonePC/2in1TabletTVWearable

didFail(code: WebNetErrorList): void

通知ArkWeb内核被拦截请求应该返回失败，调用前需要优先调用[didReceiveResponse](/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webresourcehandler#didreceiveresponse12)将构造的响应头传递给被拦截的请求。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | WebNetErrorList | 是 | 网络错误码。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-webview)、[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

  展开

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types. |
| 17100021 | The resource handler is invalid. |

**示例：**

示例请参考[OnRequestStart](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webschemehandler#onrequeststart12)。

## didFail 20+

 支持设备PhonePC/2in1TabletTVWearable

didFail(code: WebNetErrorList, completeIfNoResponse: boolean): void

通知ArkWeb内核，被拦截请求应返回失败。若completeIfNoResponse为false，调用前需优先调用[didReceiveResponse](/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webresourcehandler#didreceiveresponse12)，将构造的响应头传递给被拦截的请求。若completeIfNoResponse为true，且调用前未调用[didReceiveResponse](/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webresourcehandler#didreceiveresponse12)，则自动生成一个响应头，网络错误码为-104，详情参见[WebNetErrorList](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-neterrorlist#webneterrorlist)。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | WebNetErrorList | 是 | 网络错误码。 |
| completeIfNoResponse | boolean | 是 | 调用当前接口时，若之前未调用过 didReceiveResponse ，是否完成此次网络请求；值为true时，若之前未调用过 didReceiveResponse ，则会自动生成一个response以完成此次网络请求，网络错误码为-104；值为false时，将等待应用调用 didReceiveResponse 并传入response，不会直接完成此次网络请求。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-webview)。

  展开

| 错误码ID | 错误信息 |
| --- | --- |
| 17100101 | The errorCode is either ARKWEB_NET_OK or outside the range of error codes in WebNetErrorList. |
| 17100021 | The resource handler is invalid. |

**示例：**

 收起自动换行深色代码主题复制

```
```