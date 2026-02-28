# @Env：环境变量

说明 

本模块首批接口从API version 22开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

开发者指南见：[@Env开发者指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-env-system-property)。

## @Env

 支持设备PhonePC/2in1TabletTVWearable

Env: EnvDecorator

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

  展开

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| Env | EnvDecorator | 环境变量装饰器。 |

**示例：**

```
import { uiObserver } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @Env(SystemProperties.BREAK_POINT) breakpoint: uiObserver.WindowSizeLayoutBreakpointInfo;

  build() {}
}
```

## EnvDecorator

 支持设备PhonePC/2in1TabletTVWearable

type EnvDecorator = (value: SystemProperties) => PropertyDecorator

定义@Env装饰器类型。

**模型约束**：此接口仅可在Stage模型下使用。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | SystemProperties | 是 | 环境变量属性名。 |

**返回值：**

  展开

| 类型 | 说明 |
| --- | --- |
| PropertyDecorator | 属性装饰器。 |

**错误码：**

详细介绍请参见[@Env错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-env)。

  展开

| 错误码ID | 错误信息 |
| --- | --- |
| 140000 | Invalid key for @Env |

## SystemProperties

 支持设备PhonePC/2in1TabletTVWearable

定义环境变量枚举值。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

  展开

| 名称 | 值 | 说明 |
| --- | --- | --- |
| BREAK_POINT | 'system.arkui.breakpoint' | @Env 变量参数，通过@Env(SystemProperties.BREAK_POINT)可获取 WindowSizeLayoutBreakpointInfo 实例。 当该装饰器声明在 @Component 或 @ComponentV2 中时，用于获取当前自定义组件所在窗口的尺寸布局断点信息。 |