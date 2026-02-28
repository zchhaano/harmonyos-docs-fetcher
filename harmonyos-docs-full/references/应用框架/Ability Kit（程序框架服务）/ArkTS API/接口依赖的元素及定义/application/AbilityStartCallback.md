# AbilityStartCallback

定义拉起UIExtensionAbility执行结果的回调。

 说明 

本模块首批接口从API version 11开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

从API version 11开始，本模块接口支持在元服务中使用。

## 导入模块

支持设备PhonePC/2in1TabletTVWearable收起自动换行深色代码主题复制

```
import { common } from '@kit.AbilityKit' ;
```

## AbilityStartCallback

支持设备PhonePC/2in1TabletTVWearable 

### 属性

支持设备PhonePC/2in1TabletTVWearable

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

 展开

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| completionHandler 21+ | CompletionHandlerForAbilityStartCallback | 否 | 是 | 用于返回拉起指定类型的Ability组件的回调结果。 元服务API ：从API version 21开始，该接口支持在元服务中使用。 |

### onError

支持设备PhonePC/2in1TabletTVWearable

onError(code: number, name: string, message: string): void

拉起UIExtensionAbility执行失败的回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

 展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | number | 是 | 拉起UIExtensionAbility执行失败时返回的结果码。 |
| name | string | 是 | 拉起UIExtensionAbility执行失败时返回的名称。 |
| message | string | 是 | 拉起UIExtensionAbility执行失败时返回的错误信息。 |

**示例：**

 收起自动换行深色代码主题复制

```
import { UIAbility , common } from '@kit.AbilityKit' ; import { BusinessError } from '@kit.BasicServicesKit' ; export default class EntryAbility extends UIAbility { onForeground ( ) { let wantParam : Record < string , Object > = { 'time' : '2023-10-23 20:45' , }; let abilityStartCallback : common. AbilityStartCallback = { onError : ( code: number , name: string , message: string ) => { console . info ( `code: ${code} , name: ${name} , message: ${message} ` ); }, onResult : ( abilityResult: common.AbilityResult ) => { console . info ( `resultCode: ${abilityResult.resultCode} , bundleName: ${abilityResult.want?.bundleName} ` ); } }; this . context . startAbilityByType ( 'photoEditor' , wantParam, abilityStartCallback, ( err: BusinessError ) => { if (err) { console . error ( `startAbilityByType fail, err: ${ JSON .stringify(err)} ` ); } else { console . info ( `success` ); } }); } }
```

### onResult 12+

支持设备PhonePC/2in1TabletTVWearable

onResult?(parameter: AbilityResult): void

拉起UIExtensionAbility终止时的回调。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

 展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| parameter | AbilityResult | 是 | 当调用 terminateSelfWithResult 方法终止UIExtensionAbility时返回的结果。 |

**示例：**

 收起自动换行深色代码主题复制

```
import { UIAbility , common } from '@kit.AbilityKit' ; import { BusinessError } from '@kit.BasicServicesKit' ; export default class EntryAbility extends UIAbility { onForeground ( ) { let wantParam : Record < string , Object > = { 'time' : '2023-10-23 20:45' , }; let abilityStartCallback : common. AbilityStartCallback = { onError : ( code: number , name: string , message: string ) => { console . info ( `code:` + code + `name:` + name + `message:` + message); }, onResult : ( abilityResult: common.AbilityResult ) => { console . info ( `resultCode:` + abilityResult. resultCode + `bundleName:` + abilityResult. want ?. bundleName ); } }; this . context . startAbilityByType ( 'photoEditor' , wantParam, abilityStartCallback, ( err: BusinessError ) => { if (err) { console . error ( `startAbilityByType fail, err: ${ JSON .stringify(err)} ` ); } else { console . info ( `success` ); } }); } }
```