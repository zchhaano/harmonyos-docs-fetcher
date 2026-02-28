# SplitLayout

上下结构布局介绍了常用的页面布局样式。主要分为上下文本和上下图文两种类型。

 说明 

该组件从API version 10开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## 导入模块

支持设备PhonePC/2in1TabletTVWearable

```
import { SplitLayout } from '@kit.ArkUI';
```

## 子组件

支持设备PhonePC/2in1TabletTVWearable

无

## 属性

支持设备PhonePC/2in1TabletTVWearable

不支持[通用属性](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-component-general-attributes)。

## SplitLayout

支持设备PhonePC/2in1TabletTVWearable

SplitLayout({mainImage: Resource, primaryText: string, secondaryText?: string, tertiaryText?: string, container: () => void })

**装饰器类型：**@Component

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

 展开

| 名称 | 类型 | 必填 | 装饰器类型 | 说明 |
| --- | --- | --- | --- | --- |
| mainImage | ResourceStr | 是 | @State | 传入图片。 |
| primaryText | ResourceStr | 是 | @Prop | 标题内容。 |
| secondaryText | ResourceStr | 否 | @Prop | 副标题内容。 |
| tertiaryText | ResourceStr | 否 | @Prop | 辅助文本。 |
| container | () => void | 是 | @BuilderParam | 容器内组件。 |

## 事件

支持设备PhonePC/2in1TabletTVWearable

不支持[通用事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-component-general-events)。

## 示例

支持设备PhonePC/2in1TabletTVWearable

该示例通过SplitLayout实现了页面布局，并具备自适应能力。

```
import { SplitLayout } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State demoImage: Resource = $r("app.media.background");

  build() {
    Column() {
      SplitLayout({
        mainImage: this.demoImage,
        primaryText: '新歌推荐',
        secondaryText: '私人订制新歌精选站，为你推荐专属优质新歌;',
        tertiaryText: '每日更新',
      }) {
        Text('示例：空白区域容器内可添加组件')
          .margin({ top: 36 })
      }
    }
    .justifyContent(FlexAlign.SpaceBetween)
    .height('100%')
    .width('100%')
  }
}
```

小于等于600vp布局：

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170743.02105967421944549526512979226052:50001231000000:2800:CCF9E28C731171DCE017057F40180E694F502583BCBB1F59C892907D4CECB24C.png)

大于600vp且小于等于840vp的布局：

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170743.24349216998455826211409224284560:50001231000000:2800:31B6F8A9E49463F5BD3A3CD1CFCA85D73367E0E2E532AFACBDCD632DAA490B7E.png)

大于840vp布局：

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170743.26792181355654171093084304240245:50001231000000:2800:AF3D0A306EFC78220FF2A35234920D8F6358524B262257090D058C1AA088DA95.png)