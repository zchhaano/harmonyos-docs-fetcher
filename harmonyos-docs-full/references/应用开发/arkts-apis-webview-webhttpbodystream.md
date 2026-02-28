# Class (WebHttpBodyStream)

POST、PUT请求的数据体，支持BYTES、FILE、BLOB、CHUNKED类型的数据。注意本类中其他接口需要在[initialize](/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webhttpbodystream#initialize12)成功后才能调用。

 说明 

- 本模块首批接口从API version 9开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
- 本Class首批接口从API version 12开始支持。
- 示例效果请以真机运行为准。

## 导入模块

 支持设备PhonePC/2in1TabletTVWearable收起自动换行深色代码主题复制

```
import { webview } from '@kit.ArkWeb' ;
```

## initialize 12+

 支持设备PhonePC/2in1TabletTVWearable

initialize(): Promise<void>

初始化WebHttpBodyStream。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

  展开

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise实例，用于获取WebHttpBodyStream是否初始化成功。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-webview)。

  展开

| 错误码ID | 错误信息 |
| --- | --- |
| 17100022 | Failed to initialize the HTTP body stream. |

**示例：**

 收起自动换行深色代码主题复制

```
```

## read 12+

 支持设备PhonePC/2in1TabletTVWearable

read(size: number): Promise<ArrayBuffer>

读取WebHttpBodyStream中的数据。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| size | number | 是 | 读取WebHttpBodyStream中的字节数。 |

**返回值：**

  展开

| 类型 | 说明 |
| --- | --- |
| Promise<ArrayBuffer> | Promise实例，用于获取WebHttpBodyStream中读取的数据。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

  展开

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

**示例：**

完整示例代码参考[initialize](/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webhttpbodystream#initialize12)。

## getSize 12+

 支持设备PhonePC/2in1TabletTVWearable

getSize(): number

获取WebHttpBodyStream中的数据大小，分块传输时总是返回零。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

  展开

| 类型 | 说明 |
| --- | --- |
| number | 获取WebHttpBodyStream中的数据大小。 |

**示例：**

完整示例代码参考[initialize](/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webhttpbodystream#initialize12)。

## getPosition 12+

 支持设备PhonePC/2in1TabletTVWearable

getPosition(): number

读取WebHttpBodyStream中当前的读取位置。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

  展开

| 类型 | 说明 |
| --- | --- |
| number | WebHttpBodyStream中当前的读取位置。 |

**示例：**

完整示例代码参考[initialize](/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webhttpbodystream#initialize12)。

## isChunked 12+

 支持设备PhonePC/2in1TabletTVWearable

isChunked(): boolean

WebHttpBodyStream是否采用分块传输。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

  展开

| 类型 | 说明 |
| --- | --- |
| boolean | WebHttpBodyStream是否采用分块传输，如果采用分块传输则返回true，否则返回false。 |

**示例：**

完整示例代码参考[initialize](/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webhttpbodystream#initialize12)。

## isEof 12+

 支持设备PhonePC/2in1TabletTVWearable

isEof(): boolean

判断WebHttpBodyStream中的所有数据是否都已被读取。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

  展开

| 类型 | 说明 |
| --- | --- |
| boolean | WebHttpBodyStream中的所有数据是否都已被读取。 如果所有数据都已被读取，则返回true。对于分块传输类型的WebHttpBodyStream，在第一次读取尝试之前返回false。 |

**示例：**

完整示例代码参考[initialize](/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webhttpbodystream#initialize12)。

## isInMemory 12+

 支持设备PhonePC/2in1TabletTVWearable

isInMemory(): boolean

判断WebHttpBodyStream中的上传数据是否在内存中。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

  展开

| 类型 | 说明 |
| --- | --- |
| boolean | WebHttpBodyStream中的上传数据是否在内存中。 如果WebHttpBodyStream中的上传数据完全在内存中，并且所有读取请求都将同步成功，则返回true。对于分块传输类型的数据，预期返回false。 |

**示例：**

完整示例代码参考[initialize](/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webhttpbodystream#initialize12)。