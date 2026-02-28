# 前景色设置

设置组件的前景色。与背景色相对应，前景色会影响绘制组件内容的颜色。主要影响文字的颜色、形状绘制组件的填充色。

 说明 

 从API version 10开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## foregroundColor

支持设备PhonePC/2in1TabletTVWearable

foregroundColor(value: ResourceColor | ColoringStrategy): T

设置组件的前景色。当组件未设置前景色，默认继承父组件。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

 展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | ResourceColor \| ColoringStrategy | 是 | 设置组件的前景颜色或者根据智能取色策略设置前景颜色。不支持 属性动画 。 |

**返回值：**

 展开

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## foregroundColor 18+

支持设备PhonePC/2in1TabletTVWearable

foregroundColor(color: Optional<ResourceColor | ColoringStrategy>): T

设置组件的前景色。当组件未设置前景色，默认继承父组件。与[foregroundColor](/consumer/cn/doc/harmonyos-references/ts-universal-attributes-foreground-color#foregroundcolor)相比，color参数新增了对undefined类型的支持。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

 展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| color | Optional < ResourceColor \| ColoringStrategy > | 是 | 设置组件的前景颜色或者根据智能取色策略设置前景颜色。不支持属性动画。 当color的值为undefined时，维持之前取值或组件默认取值，具体行为不同组件可能会有差异，建议开发者使用确定颜色或 ColoringStrategy 。 |

**返回值：**

 展开

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## 示例

支持设备PhonePC/2in1TabletTVWearable 

### 示例1（使用前景色设置）

该示例主要演示通过foregroundColor设置前景色。

```
// xxx.ets
@Entry
@Component
struct ForegroundColorExample {
  build() {
    Column({ space: 100 }) {
      // 绘制一个直径为150的圆，默认填充色为黑色
      Circle({ width: 150, height: 200 }).margin(20)
      // 绘制一个直径为150的圆，设置前景色为橙色
      Circle({ width: 150, height: 200 }).foregroundColor(Color.Orange)
    }.width('100%').backgroundColor(Color.Gray)
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170902.30501786260519022870019764390623:50001231000000:2800:621DB8D4B9693887F208370CC24F505E8B9036DE42C1D54E6B2D02A5DBA77B71.png)

### 示例2（设置前景色为组件背景色反色）

该示例通过[ColoringStrategy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-appendix-enums#coloringstrategy10).INVERT将前景色设置为背景色反色。

```
// xxx.ets
@Entry
@Component
struct ColoringStrategyExample {
  build() {
    Column({ space: 100 }) {
      // 绘制一个直径为150的圆,默认填充色为黑色
      Circle({ width: 150, height: 200 })
      // 绘制一个直径为150的圆，设置前景色为组件背景色的反色
      Circle({ width: 150, height: 200 })
        .backgroundColor(Color.Black)
        .foregroundColor(ColoringStrategy.INVERT)
    }.width('100%')
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170902.62329804054057981441660520436931:50001231000000:2800:2476118B8A5C8E835F4B92DFC4A26F6922A9EACEBE8FDCC9F12515C0AD93EA07.png)

### 示例3（前景色未继承父组件）

该示例主要演示组件同时设置前景色和背景色与只设置背景色的效果对比。

```
// xxx.ets
@Entry
@Component
struct ForegroundColorInherit {
  build() {
    Column() {
      Button('设置前景色为橘色').fontSize(20).foregroundColor(Color.Orange).backgroundColor(Color.Gray)
      Divider()
      Button('未设置前景色继承自父组件').fontSize(20).backgroundColor(Color.Gray)
    }.foregroundColor(Color.Pink)
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170902.94424919833612342639573447756443:50001231000000:2800:C903443467EE58BA24F041DD7002B41856AED4239B4A6874A32DA186BD85A71D.png)