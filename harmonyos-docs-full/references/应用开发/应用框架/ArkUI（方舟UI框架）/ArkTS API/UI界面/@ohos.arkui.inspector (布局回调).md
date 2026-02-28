# @ohos.arkui.inspector (布局回调)

提供注册组件布局和组件绘制送显完成回调通知的能力。

 说明 

本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

支持设备PhonePC/2in1TabletTVWearable

```
import { inspector } from '@kit.ArkUI';
```

## inspector.createComponentObserver (deprecated)

支持设备PhonePC/2in1TabletTVWearable

createComponentObserver(id: string): ComponentObserver

绑定指定组件，返回对应的监听句柄。

 说明 

- 从API version 10开始支持，从API version 18开始废弃，建议使用[createComponentObserver](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uiinspector#createcomponentobserver)替代。先使用[UIContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext)中的[getUIInspector](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#getuiinspector)方法获取[UIInspector](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uiinspector)实例，再通过此实例调用替代方法createComponentObserver。
- 从API version 10开始，可以通过使用[UIContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext)中的[getUIInspector](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#getuiinspector)方法获取当前UI上下文关联的[UIInspector](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uiinspector)对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

 展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | string | 是 | 指定组件id，该id通过通用属性 id 或者 key 设置。 |

**返回值：**

 展开

| 类型 | 说明 |
| --- | --- |
| ComponentObserver | 组件回调事件监听句柄，用于注册和取消注册监听回调。 |

**示例：**

```
let listener:inspector.ComponentObserver = inspector.createComponentObserver('COMPONENT_ID'); //监听id为COMPONENT_ID的组件回调事件
```

## ComponentObserver

支持设备PhonePC/2in1TabletTVWearable

组件布局和组件绘制送显完成回调的句柄，包含了申请句柄时的首次查询结果。

### on('layout')

支持设备PhonePC/2in1TabletTVWearable

on(type: 'layout', callback: () => void): void

通过句柄向对应的查询条件注册回调，当组件布局完成时会触发该回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

 展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 必须填写字符串'layout'。 layout: 组件布局完成。 |
| callback | () => void | 是 | 监听layout的回调。 |

### off('layout')

支持设备PhonePC/2in1TabletTVWearable

off(type: 'layout', callback?: () => void): void

通过句柄向对应的查询条件取消注册回调，当组件布局完成时不再触发指定的回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

 展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 必须填写字符串'layout'。 layout: 组件布局完成。 |
| callback | () => void | 否 | 需要取消注册的回调，如果参数缺省则取消注册该句柄下所有的回调。callback需要和 on('layout') 方法中的callback为相同对象时才能取消回调成功。 |

### on('draw')

支持设备PhonePC/2in1TabletTVWearable

on(type: 'draw', callback: () => void): void

通过句柄向对应的查询条件注册回调，当组件绘制送显完成时会触发该回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

 展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 必须填写字符串'draw'。 draw: 组件绘制送显完成。 |
| callback | () => void | 是 | 监听draw的回调。 |

### off('draw')

支持设备PhonePC/2in1TabletTVWearable

off(type: 'draw', callback?: () => void): void

通过句柄向对应的查询条件取消注册回调，当组件绘制送显完成时不再触发指定的回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

 展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 必须填写字符串'draw'。 draw: 组件绘制送显完成。 |
| callback | () => void | 否 | 需要取消注册的回调，如果参数缺省则取消注册该句柄下所有的回调。callback需要和 on('draw') 方法中的callback为相同对象时才能取消回调成功。 |

### on('drawChildren') 20+

支持设备PhonePC/2in1TabletTVWearable

on(type: 'drawChildren', callback: Callback<void>): void

通过[ComponentObserver](/consumer/cn/doc/harmonyos-references/js-apis-arkui-inspector#componentobserver)注册drawChildren事件回调方法，当组件的子组件绘制送显完成时会触发该回调方法。如果组件树中存在多个drawChildren事件回调，只会触发在最顶层的drawChildren事件回调。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

 展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 必须填写字符串'drawChildren'。 drawChildren: 子组件绘制送显完成。 |
| callback | Callback<void> | 是 | 监听drawChildren的回调。 |

### off('drawChildren') 20+

支持设备PhonePC/2in1TabletTVWearable

off(type: 'drawChildren', callback?: Callback<void>): void

通过句柄向对应的查询条件取消注册回调，当组件的子组件绘制送显完成时不再触发指定的回调。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

 展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 必须填写字符串'drawChildren'。 drawChildren: 子组件绘制送显完成。 |
| callback | Callback<void> | 否 | 需要取消注册的回调，如果参数缺省则取消注册该句柄下所有的回调。callback需要和 on('drawChildren')20+ 方法中的callback为相同对象时才能取消回调成功。 |

## 示例

支持设备PhonePC/2in1TabletTVWearable

以下示例展示了inspector注册组件布局和组件绘制送显完成回调通知能力的基本用法。

```
import { inspector } from '@kit.ArkUI';

@Entry
@Component
struct ImageExample {
  build() {
    Column() {
      Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Start }) {
        Row({ space: 5 }) {
          Image($r('app.media.startIcon'))
            .width(110)
            .height(110)
            .border({ width: 1 })
            .id('IMAGE_ID')
        }
        .id('ROW_ID')
      }
    }.height(320).width(360).padding({ right: 10, top: 10 })
  }

  listenerForImage: inspector.ComponentObserver = this.getUIContext().getUIInspector().createComponentObserver('IMAGE_ID')
  listenerForRow: inspector.ComponentObserver = this.getUIContext().getUIInspector().createComponentObserver('ROW_ID')

  aboutToAppear() {
    let onLayoutComplete: () => void = (): void => {
      // 根据需要补充实现代码
    }
    let onDrawComplete: () => void = (): void => {
      // 根据需要补充实现代码
    }
    let onDrawChildrenComplete: () => void = (): void => {
      // 根据需要补充实现代码
    }
    // 绑定当前js实例
    let FuncLayout = onLayoutComplete
    let FuncDraw = onDrawComplete
    let FuncDrawChildren = onDrawChildrenComplete
    let OffFuncLayout = onLayoutComplete
    let OffFuncDraw = onDrawComplete
    let OffFuncDrawChildren = onDrawChildrenComplete

    this.listenerForImage.on('layout', FuncLayout)
    this.listenerForImage.on('draw', FuncDraw)
    this.listenerForRow.on('drawChildren', FuncDrawChildren)

    // 通过句柄向对应的查询条件取消注册回调，由开发者自行决定在何时调用
    // this.listenerForImage.off('layout', OffFuncLayout)
    // this.listenerForImage.off('draw', OffFuncDraw)
    // this.listenerForRow.off('drawChildren', OffFuncDrawChildren)
  }
}
```