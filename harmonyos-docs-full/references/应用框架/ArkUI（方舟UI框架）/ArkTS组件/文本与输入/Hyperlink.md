# Hyperlink

超链接组件，组件宽高范围内点击实现跳转。

 说明 

- 该组件从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
- 该组件仅支持与系统浏览器配合使用。

## 需要权限

 支持设备PhonePC/2in1TabletTVWearable

跳转的目标应用使用网络时，需要申请权限ohos.permission.INTERNET。具体申请方式请参考[声明权限](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/declare-permissions)。

## 子组件

 支持设备PhonePC/2in1TabletTVWearable

可以包含[Image](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image)子组件。

## 接口

 支持设备PhonePC/2in1TabletTVWearable

Hyperlink(address: string | Resource, content?: string | Resource)

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| address | string \| Resource | 是 | Hyperlink组件跳转的网页。 |
| content | string \| Resource | 否 | Hyperlink组件中超链接显示文本。 说明： 组件内有子组件时，不显示超链接文本。 |

## 属性

 支持设备PhonePC/2in1TabletTVWearable

除支持[通用属性](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-component-general-attributes)外，还支持以下属性：

### color

 支持设备PhonePC/2in1TabletTVWearable

color(value: Color | number | string | Resource)

设置超链接文本的颜色。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Color \| number \| string \| Resource | 是 | 超链接文本的颜色。 phone默认值为'#ff007dff'，wearable设备默认值'#1F71FF'，tv设备默认值为'#266EFB'，均显示为蓝色。 |

## 示例

 支持设备PhonePC/2in1TabletTVWearable

该示例展示了超链接图片和文本跳转的效果。

 收起自动换行深色代码主题复制

```
@Entry @Component struct HyperlinkExample { build ( ) { Column () { Column () { Hyperlink ( 'https://example.com/' ) { // $r('app.media.bg')需要替换为开发者所需的图像资源文件。 Image ($r( 'app.media.bg' )) . width ( 200 ) . height ( 100 ) } } Column () { Hyperlink ( 'https://example.com/' , 'Go to the developer website' ) { } . color ( Color . Blue ) } }. width ( '100%' ). height ( '100%' ). justifyContent ( FlexAlign . Center ) } }
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170711.13579085304915220601415738885806:50001231000000:2800:9262D165797F4EC20CF9084C09C033E0B246AEA255D0F26641670C4569B1F116.png)