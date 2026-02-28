# 路径动画 (motionPath)

设置组件进行位移动画时的运动路径。

 说明 

从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## motionPath

 支持设备PhonePC/2in1TabletTVWearable

motionPath(value: MotionPathOptions): T

设置组件的路径动画。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | MotionPathOptions | 是 | 设置组件的运动路径。 |

**返回值：**

  展开

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## MotionPathOptions

 支持设备PhonePC/2in1TabletTVWearable

设置组件的运动路径。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

  展开

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| path | string | 否 | 否 | 位移动画的运动路径，使用 svg路径字符串 。path中支持使用start和end进行起点和终点的替代，如：'Mstart.x start.y L50 50 Lend.x end.y Z'，更多说明请参考 绘制路径 。 设置为空字符串时相当于不设置路径动画。 |
| from | number | 否 | 是 | 运动路径的起点。 默认值：0.0 取值范围：[0.0, 1.0] 设置小于0.0或大于1.0的值时，按默认值0.0处理。 |
| to | number | 否 | 是 | 运动路径的终点。 默认值：1.0 取值范围：[0.0, 1.0] 设置小于0.0或大于1.0的值时，按默认值1.0处理，且满足to值 >= 异常值处理后的from值。 |
| rotatable | boolean | 否 | 是 | 是否跟随路径进行旋转。true代表跟随路径进行旋转，false代表不跟随路径进行旋转。 默认值：false |

## 示例

 支持设备PhonePC/2in1TabletTVWearable

该示例主要演示如何设置组件进行位移动画时的运动路径。

```
// xxx.ets
@Entry
@Component
struct MotionPathExample {
  @State toggle: boolean = true;

  build() {
    Column() {
      Button('click me').margin(50)
        .motionPath({
          path: 'Mstart.x start.y L300 200 L300 500 Lend.x end.y',
          from: 0.0,
          to: 1.0,
          rotatable: true
        }) // 执行动画：从起点移动到(300,200)，再到(300,500)，再到终点
        .onClick(() => {
          this.getUIContext()?.animateTo({ duration: 4000, curve: Curve.Linear }, () => {
            this.toggle = !this.toggle; // 通过this.toggle变化组件的位置
          });
        })
    }.width('100%').height('100%').alignItems(this.toggle ? HorizontalAlign.Start : HorizontalAlign.Center)
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170641.67838983296030399036976521644081:50001231000000:2800:113613DAE41ABF83565F26A471A56F106FD568E6D9E2D2320A09D5DFBA74A0EF.gif)