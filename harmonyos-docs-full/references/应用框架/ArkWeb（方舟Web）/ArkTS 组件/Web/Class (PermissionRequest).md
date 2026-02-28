# Class (PermissionRequest)

Web组件返回授权或拒绝权限功能的对象。示例代码参考[onPermissionRequest事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-events#onpermissionrequest9)。

 说明 

- 该组件首批接口从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
- 本Class首批接口从API version 9开始支持。
- 示例效果请以真机运行为准。

## constructor 9+

支持设备PhonePC/2in1TabletTVWearable

constructor()

PermissionRequest的构造函数。

**系统能力：** SystemCapability.Web.Webview.Core

## deny 9+

支持设备PhonePC/2in1TabletTVWearable

deny(): void

拒绝网页所请求的权限。

**系统能力：** SystemCapability.Web.Webview.Core

## getOrigin 9+

支持设备PhonePC/2in1TabletTVWearable

getOrigin(): string

获取网页来源。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

 展开

| 类型 | 说明 |
| --- | --- |
| string | 当前请求权限网页的来源。 |

## getAccessibleResource 9+

支持设备PhonePC/2in1TabletTVWearable

getAccessibleResource(): Array<string>

获取网页所请求的权限资源列表，资源列表类型参考[ProtectedResourceType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-e#protectedresourcetype9)。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

 展开

| 类型 | 说明 |
| --- | --- |
| Array<string> | 网页所请求的权限资源列表。 |

## grant 9+

支持设备PhonePC/2in1TabletTVWearable

grant(resources: Array<string>): void

对网页访问的给定权限进行授权。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

 展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resources | Array<string> | 是 | 授予网页请求的权限的资源列表。 |