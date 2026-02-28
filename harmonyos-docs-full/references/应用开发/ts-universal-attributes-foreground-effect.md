# 前景属性设置

设置组件的前景属性。

 说明 

 从API version 12开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## foregroundEffect

支持设备PhonePC/2in1TabletTVWearable

foregroundEffect(options: ForegroundEffectOptions): T

设置组件的前景属性。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

 展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | ForegroundEffectOptions | 是 | 设置组件前景属性包括：模糊半径。 |

**返回值：**

 展开

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## ForegroundEffectOptions 12+

支持设备PhonePC/2in1TabletTVWearable

前景效果参数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

 展开

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| radius | number | 否 | 否 | 模糊半径，取值范围：[0, +∞)。 仅在组件范围内生效，与其他接口连用时超出组件范围的效果无法生效。 |

## 示例

支持设备PhonePC/2in1TabletTVWearable

该示例主要演示通过foregroundEffect接口设置前景属性。

 收起自动换行深色代码主题复制

```
// xxx.ets @Entry @Component struct Index { build ( ) { Row () { // $r("app.media.icon")需要替换为开发者所需的图像资源文件。 Image ($r( 'app.media.icon' )) . width ( 100 ) . height ( 100 ) . foregroundEffect ({ radius : 20 }) } . width ( '100%' ) . height ( '100%' ) . justifyContent ( FlexAlign . Center ) } }
```

效果图如下：

radius表示模糊半径，数值越大，效果越模糊。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170906.74301827878729789486287412607720:50001231000000:2800:3F6E175A3AFBDE5CDF6FA32C7A4A82F40EBC7D44758A3284279D237B4AC497AB.jpg)