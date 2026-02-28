# Class (WebSchemeHandlerResponse)

请求的响应，可以为被拦截的请求创建一个Response并填充自定义的内容返回给Web组件。

 说明 

- 本模块首批接口从API version 9开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
- 本Class首批接口从API version 12开始支持。
- 示例效果请以真机运行为准。

## 导入模块

 支持设备PhonePC/2in1TabletTVWearable收起自动换行深色代码主题复制

```
import { webview } from '@kit.ArkWeb' ;
```

## constructor 12+

 支持设备PhonePC/2in1TabletTVWearable

constructor()

Response的构造函数。

**系统能力：** SystemCapability.Web.Webview.Core

**示例：**

 收起自动换行深色代码主题复制

```
// xxx.ets import { webview, WebNetErrorList } from '@kit.ArkWeb' ; import { BusinessError } from '@kit.BasicServicesKit' ; @Entry @Component struct WebComponent { controller : webview. WebviewController = new webview. WebviewController (); schemeHandler : webview. WebSchemeHandler = new webview. WebSchemeHandler (); build ( ) { Column () { Button ( 'response' ). onClick ( () => { let response = new webview. WebSchemeHandlerResponse (); try { response. setUrl ( "http://www.example.com" ) response. setStatus ( 200 ) response. setStatusText ( "OK" ) response. setMimeType ( "text/html" ) response. setEncoding ( "utf-8" ) response. setHeaderByName ( "header1" , "value1" , false ) response. setNetErrorCode ( WebNetErrorList . NET_OK ) console . info ( "[schemeHandler] getUrl:" + response. getUrl ()) console . info ( "[schemeHandler] getStatus:" + response. getStatus ()) console . info ( "[schemeHandler] getStatusText:" + response. getStatusText ()) console . info ( "[schemeHandler] getMimeType:" + response. getMimeType ()) console . info ( "[schemeHandler] getEncoding:" + response. getEncoding ()) console . info ( "[schemeHandler] getHeaderByValue:" + response. getHeaderByName ( "header1" )) console . info ( "[schemeHandler] getNetErrorCode:" + response. getNetErrorCode ()) } catch (error) { console . error ( `ErrorCode: ${(error as BusinessError).code} ,  Message: ${(error as BusinessError).message} ` ); } }) Web ({ src : 'https://www.example.com' , controller : this . controller }) } } }
```

## setUrl 12+

 支持设备PhonePC/2in1TabletTVWearable

setUrl(url: string): void

给当前的Response设置重定向或因HSTS而更改后的URL，设置了url后会触发请求的跳转。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | string | 是 | 即将要跳转的URL。 |

**示例：**

完整示例代码参考[constructor](/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webschemehandlerresponse#constructor12)。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

  展开

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types. |

## setNetErrorCode 12+

 支持设备PhonePC/2in1TabletTVWearable

setNetErrorCode(code: WebNetErrorList): void

给当前的Response设置网络错误码。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | WebNetErrorList | 是 | 网络错误码。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

  展开

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |

**示例：**

完整示例代码参考[constructor](/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webschemehandlerresponse#constructor12)。

## setStatus 12+

 支持设备PhonePC/2in1TabletTVWearable

setStatus(code: number): void

给当前的Response设置HTTP状态码。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | number | 是 | Http状态码。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

  展开

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types. |

**示例：**

完整示例代码参考[constructor](/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webschemehandlerresponse#constructor12)。

## setStatusText 12+

 支持设备PhonePC/2in1TabletTVWearable

setStatusText(text: string): void

给当前的Response设置状态文本。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | string | 是 | 状态文本。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

  展开

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types. |

**示例：**

完整示例代码参考[constructor](/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webschemehandlerresponse#constructor12)。

## setMimeType 12+

 支持设备PhonePC/2in1TabletTVWearable

setMimeType(type: string): void

给当前的Response设置媒体类型。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 媒体类型。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

  展开

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types. |

**示例：**

完整示例代码参考[constructor](/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webschemehandlerresponse#constructor12)。

## setEncoding 12+

 支持设备PhonePC/2in1TabletTVWearable

setEncoding(encoding: string): void

给当前的Response设置字符集。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| encoding | string | 是 | 字符集。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

  展开

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types. |

**示例：**

完整示例代码参考[constructor](/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webschemehandlerresponse#constructor12)。

## setHeaderByName 12+

 支持设备PhonePC/2in1TabletTVWearable

setHeaderByName(name: string, value: string, overwrite: boolean): void

给当前的Response设置头信息。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 头部（header）的名称。 |
| value | string | 是 | 头部（header）的值。 |
| overwrite | boolean | 是 | 如果为true，将覆盖现有的头部，否则不覆盖。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

  展开

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |

**示例：**

完整示例代码参考[constructor](/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webschemehandlerresponse#constructor12)。

## getUrl 12+

 支持设备PhonePC/2in1TabletTVWearable

getUrl(): string

获取重定向或由于HSTS而更改后的URL。

风险提示：如果想获取url来做JavascriptProxy通信接口认证，请使用[getLastJavascriptProxyCallingFrameUrl 12+](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webviewcontroller#getlastjavascriptproxycallingframeurl12)

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

  展开

| 类型 | 说明 |
| --- | --- |
| string | 获取经过重定向或由于HSTS而更改后的URL。 |

**示例：**

完整示例代码参考[constructor](/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webschemehandlerresponse#constructor12)。

## getNetErrorCode 12+

 支持设备PhonePC/2in1TabletTVWearable

getNetErrorCode(): WebNetErrorList

获取Response的网络错误码。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

  展开

| 类型 | 说明 |
| --- | --- |
| WebNetErrorList | 获取Response的网络错误码。 |

**示例：**

完整示例代码参考[constructor](/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webschemehandlerresponse#constructor12)。

## getStatus 12+

 支持设备PhonePC/2in1TabletTVWearable

getStatus(): number

获取Response的Http状态码。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

  展开

| 类型 | 说明 |
| --- | --- |
| number | 获取Response的Http状态码。 |

**示例：**

完整示例代码参考[constructor](/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webschemehandlerresponse#constructor12)。

## getStatusText 12+

 支持设备PhonePC/2in1TabletTVWearable

getStatusText(): string

获取Response的状态文本。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

  展开

| 类型 | 说明 |
| --- | --- |
| string | 状态文本。 |

**示例：**

完整示例代码参考[constructor](/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webschemehandlerresponse#constructor12)。

## getMimeType 12+

 支持设备PhonePC/2in1TabletTVWearable

getMimeType(): string

获取Response的媒体类型。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

  展开

| 类型 | 说明 |
| --- | --- |
| string | 媒体类型。 |

**示例：**

完整示例代码参考[constructor](/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webschemehandlerresponse#constructor12)。

## getEncoding 12+

 支持设备PhonePC/2in1TabletTVWearable

getEncoding(): string

获取Response的字符集。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

  展开

| 类型 | 说明 |
| --- | --- |
| string | 字符集。 |

**示例：**

完整示例代码参考[constructor](/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webschemehandlerresponse#constructor12)。

## getHeaderByName 12+

 支持设备PhonePC/2in1TabletTVWearable

getHeaderByName(name: string): string

按名称获取Response头部字段值。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 头部（header）的名称。 |

**返回值：**

  展开

| 类型 | 说明 |
| --- | --- |
| string | 头部（header）的值。 |

**示例：**

完整示例代码参考[constructor](/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webschemehandlerresponse#constructor12)。