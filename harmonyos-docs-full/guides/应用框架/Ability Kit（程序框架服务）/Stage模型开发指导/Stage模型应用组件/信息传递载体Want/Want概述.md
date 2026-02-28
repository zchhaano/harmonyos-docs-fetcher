## Want的定义与用途

[Want](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-want)是一种对象，用于在应用组件之间传递信息。

其中，一种常见的使用场景是作为[startAbility()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext#startability)方法的参数。例如，当UIAbilityA需要启动UIAbilityB并向UIAbilityB传递一些数据时，可以使用Want作为一个载体，将数据传递给UIAbilityB。

**图1** Want用法示意

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165902.57308826838065306638699505465143:50001231000000:2800:31DCF2552F494C440D11203509907AE0AE84E00F436B7577AC2FD32C143CE2B2.png)

## Want的类型

- **显式Want**：在启动目标应用组件时，调用方传入的[want](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-want)参数中指定了abilityName和bundleName，称为显式Want。

显式Want通常用于应用内组件启动，通过在Want对象内指定本应用Bundle名称信息（bundleName）和abilityName来启动应用内目标组件。当有明确处理请求的对象时，显式Want是一种简单有效的启动目标应用组件的方式。

 说明 

从API 12开始，已不再推荐三方应用使用指定Ability方式（即显式Want）拉起其他应用，推荐通过指定[应用链接](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-startup-overview#应用链接)的方式来实现。

  收起自动换行深色代码主题复制

```
import { common, Want } from '@kit.AbilityKit' ; // ··· let wantInfo : Want = { deviceId : '' , // deviceId为空表示本设备 bundleName : 'com.samples.wantoverview' , abilityName : 'ExplicitAbility' , };
```

[ExplicitPage.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/Ability/WantOverview/entry/src/main/ets/pages/ExplicitPage.ets#L15-L30)
- **隐式Want**：在启动目标应用组件时，调用方传入的[want](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-want)参数中未指定abilityName，称为隐式Want。

当需要处理的对象不明确时，可以使用隐式Want，在当前应用中使用其他应用提供的某个能力，而不关心提供该能力的具体应用。隐式Want使用[skills标签](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/module-configuration-file#skills标签)来定义需要使用的能力，并由系统匹配声明支持该请求的所有应用来处理请求。例如，需要打开一个链接的请求，系统将匹配所有声明支持该请求的应用，然后让用户选择使用哪个应用打开链接。

 收起自动换行深色代码主题复制

```
import { common, Want } from '@kit.AbilityKit' ; // ··· let wantInfo : Want = { // uncomment line below if wish to implicitly query only in the specific bundle. // bundleName: 'com.example.myapplication', action : 'ohos.want.action.search' , // entities can be omitted entities : [ 'entity.system.browsable' ], uri : 'https://www.test.com:8080/query/student' , type : 'text/plain' , };
```

[ImplicitPage.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/Ability/WantOverview/entry/src/main/ets/pages/ImplicitPage.ets#L15-L34) 说明 

  - 根据系统中待匹配应用组件的匹配情况不同，使用隐式Want启动应用组件时会出现以下三种情况。

    - 未匹配到满足条件的应用组件：启动失败。
    - 匹配到一个满足条件的应用组件：直接启动该应用组件。
    - 匹配到多个满足条件的应用组件（[UIAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-uiability)）：弹出选择框让用户选择。
  - 对于启动ServiceExtensionAbility的场景。

    - 调用方传入的[want](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-want)参数中带有abilityName，则不允许通过隐式Want启动ServiceExtensionAbility。
    - 调用方传入的want参数中带有bundleName，则允许使用startServiceExtensionAbility()方法隐式Want启动ServiceExtensionAbility，默认返回优先级最高的ServiceExtensionAbility，如果优先级相同，返回第一个。