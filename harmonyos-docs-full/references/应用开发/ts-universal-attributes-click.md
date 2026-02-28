# 点击控制

设置组件是否可以响应点击事件、触摸事件等手指交互事件。

 说明 

 本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## touchable (deprecated)

支持设备PhonePC/2in1TabletTVWearable

touchable(value: boolean): T

设置当前组件是否可以响应点击事件、触摸事件等手指交互事件。

 说明 

从API version 7开始支持，从API version 9开始废弃，建议使用[hitTestBehavior](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-hit-test-behavior#hittestbehavior)替代。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

 展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 设置当前组件是否可以响应点击事件、触摸事件等手指交互事件。 默认值：true，可以响应交互事件。设置为false时，不可以响应交互事件。 |

**返回值：**

 展开

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## 示例

支持设备PhonePC/2in1TabletTVWearable

```
// xxx.ets
@Entry
@Component
struct TouchAbleExample {
  @State text1: string = ''
  @State text2: string = ''

  build() {
    Stack() {
      Rect()
        .fill(Color.Gray).width(150).height(150)
        .onClick(() => {
          console.info(this.text1 = 'Rect Clicked')
        })
        .overlay(this.text1, { align: Alignment.Bottom, offset: { x: 0, y: 20 } })
      Ellipse()
        .fill(Color.Pink).width(150).height(80)
        .touchable(false) // 点击Ellipse区域，不会打印 “Ellipse Clicked”
        .onClick(() => {
          console.info(this.text2 = 'Ellipse Clicked')
        })
        .overlay(this.text2, { align: Alignment.Bottom, offset: { x: 0, y: 20 } })
    }.margin(100)
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170601.49223474942850597167587507186119:50001231000000:2800:21DA29ABDE3842C3534A1C8DF3D345942ECF1F63F9A1F51DD947EFAAECC3262A.gif)