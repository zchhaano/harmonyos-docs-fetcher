# Counter

计数器组件，提供相应的增加或者减少的计数操作。

 说明 

该组件从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## 子组件

支持设备PhonePC/2in1TabletTVWearable

可以包含子组件。

## 接口

支持设备PhonePC/2in1TabletTVWearable

Counter()

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 属性

支持设备PhonePC/2in1TabletTVWearable

除支持[通用属性](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-component-general-attributes)外，还支持以下属性。

### enableInc 10+

支持设备PhonePC/2in1TabletTVWearable

enableInc(value: boolean)

设置增加按钮的禁用或使能。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

 展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 增加按钮禁用或使能。 默认值：true，true表示可以增加按钮，false表示禁止增加按钮。 |

### enableDec 10+

支持设备PhonePC/2in1TabletTVWearable

enableDec(value: boolean)

设置减少按钮的禁用或使能。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

 展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 减少按钮禁用或使能。 默认值：true，true表示可以减少按钮，false表示禁止减少按钮。 |

## 事件

支持设备PhonePC/2in1TabletTVWearable

除支持[通用事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-component-general-events)外，还支持以下事件：

### onInc

支持设备PhonePC/2in1TabletTVWearable

onInc(event: VoidCallback)

监听数值增加事件。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

 展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | VoidCallback | 是 | Counter数值增加的回调函数。 |

### onDec

支持设备PhonePC/2in1TabletTVWearable

onDec(event: VoidCallback)

监听数值减少事件。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

 展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | VoidCallback | 是 | Counter数值减少的回调函数。 |

## 示例

支持设备PhonePC/2in1TabletTVWearable

该示例展示了Counter组件的基本使用方法。点击+、-按钮可以修改value值。

```
// xxx.ets
@Entry
@Component
struct CounterExample {
  @State value1: number = 0;
  @State value2: number = 0;

  build() {
    Column({ space: 50 }) {
      Counter() {
        Text(this.value1.toString())
      }
      .onInc(() => {
        this.value1++;
      })
      .onDec(() => {
        this.value1--;
      })

      Counter() {
        Text(this.value2.toString())
      }
      .onInc(() => {
        this.value2++;
      })
      .onDec(() => {
        this.value2--;
      })
      .enableInc(true)
      .enableDec(false)
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170541.84131336952569497740836844458894:50001231000000:2800:1FB1B4D063EF10FAA9EC3AB07277ABE76792E50196239C3D64F30307D558F3BD.gif)