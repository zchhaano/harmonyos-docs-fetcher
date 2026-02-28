# @ohos.app.ability.abilityDelegatorRegistry (AbilityDelegatorRegistry)

AbilityDelegatorRegistry是自动化测试框架使用指南模块，该模块用于获取[AbilityDelegator](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-abilitydelegator)和[AbilityDelegatorArgs](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-abilitydelegatorargs)对象，其中[AbilityDelegator](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-abilitydelegator)对象提供添加用于监视指定ability的生命周期状态更改的[AbilityMonitor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-abilitymonitor#abilitymonitor-1)对象的能力，[AbilityDelegatorArgs](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-abilitydelegatorargs)对象提供获取当前测试参数的能力。

 说明 

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在[单元测试框架](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/unittest-guidelines)中使用。

## 导入模块

 支持设备PhonePC/2in1TabletTVWearable

```
import { abilityDelegatorRegistry } from '@kit.TestKit';
```

## AbilityLifecycleState

 支持设备PhonePC/2in1TabletTVWearable

Ability生命周期状态，该类型为枚举，可配合[AbilityDelegator](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-abilitydelegator)的[getAbilityState(ability)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-abilitydelegator#getabilitystate9)方法返回不同ability生命周期。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力** ：以下各项对应的系统能力均为SystemCapability.Ability.AbilityRuntime.Core

  展开

| 名称 | 值 | 说明 |
| --- | --- | --- |
| UNINITIALIZED | 0 | 表示Ability处于无效状态。 |
| CREATE | 1 | 表示Ability处于已创建状态。 |
| FOREGROUND | 2 | 表示Ability处于前台状态。 |
| BACKGROUND | 3 | 表示Ability处于后台状态。 |
| DESTROY | 4 | 表示Ability处于已销毁状态。 |

## abilityDelegatorRegistry.getAbilityDelegator

 支持设备PhonePC/2in1TabletTVWearable

getAbilityDelegator(): AbilityDelegator

获取应用程序的[AbilityDelegator](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-abilitydelegator)对象，该对象能够使用调度测试框架的相关功能。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**返回值：**

  展开

| 类型 | 说明 |
| --- | --- |
| AbilityDelegator | AbilityDelegator 对象。可以用来调度测试框架相关功能。 |

**示例：**

```
import { abilityDelegatorRegistry } from '@kit.TestKit';
import { Want } from '@kit.AbilityKit';

let abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
let want: Want = {
  bundleName: 'com.example.myapplication',
  abilityName: 'EntryAbility'
};

abilityDelegator.startAbility(want, (err) => {
  if (err) {
    console.error(`Failed start ability, error: ${JSON.stringify(err)}`);
  } else {
    console.info('Success start ability.');
  }
});
```

## abilityDelegatorRegistry.getArguments

 支持设备PhonePC/2in1TabletTVWearable

getArguments(): AbilityDelegatorArgs

获取单元测试参数[AbilityDelegatorArgs](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-abilitydelegatorargs)对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**返回值：**

  展开

| 类型 | 说明 |
| --- | --- |
| AbilityDelegatorArgs | AbilityDelegatorArgs 对象。可以用来获取测试参数。 |

**示例：**

```
import { abilityDelegatorRegistry } from '@kit.TestKit';

let args = abilityDelegatorRegistry.getArguments();
console.info(`getArguments bundleName: ${args.bundleName}`);
console.info(`getArguments parameters: ${JSON.stringify(args.parameters)}`);
console.info(`getArguments testCaseNames: ${args.testCaseNames}`);
console.info(`getArguments testRunnerClassName: ${args.testRunnerClassName}`);
```

## AbilityDelegator

 支持设备PhonePC/2in1TabletTVWearable

type AbilityDelegator = _AbilityDelegator

AbilityDelegator模块。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

  展开

| 类型 | 说明 |
| --- | --- |
| _AbilityDelegator | AbilityDelegator模块。 |

## AbilityDelegatorArgs

 支持设备PhonePC/2in1TabletTVWearable

type AbilityDelegatorArgs = _AbilityDelegatorArgs

AbilityDelegatorArgs模块。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

  展开

| 类型 | 说明 |
| --- | --- |
| _AbilityDelegatorArgs | AbilityDelegatorArgs模块。 |

## AbilityMonitor

 支持设备PhonePC/2in1TabletTVWearable

type AbilityMonitor = _AbilityMonitor

AbilityMonitor模块。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

  展开

| 类型 | 说明 |
| --- | --- |
| _AbilityMonitor | AbilityMonitor模块。 |

## ShellCmdResult

 支持设备PhonePC/2in1TabletTVWearable

type ShellCmdResult = _ShellCmdResult

ShellCmdResult模块。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

  展开

| 类型 | 说明 |
| --- | --- |
| _ShellCmdResult | ShellCmdResult模块。 |

## AbilityStageMonitor 14+

 支持设备PhonePC/2in1TabletTVWearable

type AbilityStageMonitor = _AbilityStageMonitor

AbilityStageMonitor模块。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

  展开

| 类型 | 说明 |
| --- | --- |
| _AbilityStageMonitor | AbilityStageMonitor模块。 |