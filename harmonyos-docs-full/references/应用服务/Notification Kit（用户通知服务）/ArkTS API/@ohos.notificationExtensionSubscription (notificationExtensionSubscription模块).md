# @ohos.notificationExtensionSubscription (notificationExtensionSubscription模块)

本模块提供管理通知扩展的能力，具体包括：打开通知扩展订阅设置界面、订阅和取消订阅通知扩展、获取和设置通知授权状态。

 说明 

本模块首批接口从API version 22开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

 支持设备PhonePC/2in1TabletTVWearable

```
import { notificationExtensionSubscription } from '@kit.NotificationKit';
import { BusinessError } from '@kit.BasicServicesKit';
```

## notificationExtensionSubscription.openSubscriptionSettings

 支持设备PhonePC/2in1TabletTVWearable

openSubscriptionSettings(context: UIAbilityContext): Promise<void>

打开应用的通知扩展订阅授权页面，以半模态弹窗形式显示。用户可在该页面授权"允许获取本机通知"开关与"已获取的本机通知"应用开关。使用Promise异步回调。

**系统能力**：SystemCapability.Notification.Notification

**需要权限**：ohos.permission.SUBSCRIBE_NOTIFICATION

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | UIAbilityContext | 是 | 通知设置页面绑定Ability的上下文。 |

**返回值：**

  展开

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)、[通知错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-notification)。

  展开

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied or current device not supported. |
| 1600001 | Internal error. |
| 1600018 | The notification settings window is already displayed. |
| 1600023 | The application does not implement the NotificationSubscriberExtensionAbility. |

**示例：**

```
import { common } from '@kit.AbilityKit';

try {
  // 请在组件内获取context，确保this.getuIContext().getHostContext()返回结果为UIAbilityContext。
  let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  notificationExtensionSubscription.openSubscriptionSettings(context).then(() => {
    console.info(`openSubscriberSettings success`);
  }).catch((e:Error) => {
    let error = e as BusinessError
    console.error(`failed to call openSubscriptionSettings ${JSON.stringify(error)}`)
  });
} catch (error) {
  console.error(`failed to call openSubscriptionSettings ${JSON.stringify(error)}`)
}
```

## notificationExtensionSubscription.subscribe

 支持设备PhonePC/2in1TabletTVWearable

subscribe(info: NotificationExtensionSubscriptionInfo[]): Promise<void>

订阅通知扩展。使用[蓝牙模块](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/connectivity-kit-intro#蓝牙简介)相关接口获取蓝牙设备的唯一地址后方可订阅。使用Promise异步回调。

**系统能力**：SystemCapability.Notification.Notification

**需要权限**：ohos.permission.SUBSCRIBE_NOTIFICATION

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| info | NotificationExtensionSubscriptionInfo[] | 是 | 订阅的信息列表（数组）。 |

**返回值：**

  展开

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)、[通知错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-notification)。

  展开

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied or current device not supported. |
| 1600001 | Internal error. |
| 1600003 | Failed to connect to the service. |
| 1600023 | The application does not implement the NotificationSubscriberExtensionAbility. |

**示例：**

```
let infos: notificationExtensionSubscription.NotificationExtensionSubscriptionInfo[] = [
  {
    addr: '01:23:45:67:89:AB', // 使用动态获取的蓝牙地址
    type: notificationExtensionSubscription.SubscribeType.BLUETOOTH
  }
];
notificationExtensionSubscription.subscribe(infos).then(() => {
  console.info("subscribe success");
}).catch((err: BusinessError) => {
  console.error(`subscribe fail: ${JSON.stringify(err)}`);
});
```

## notificationExtensionSubscription.unsubscribe

 支持设备PhonePC/2in1TabletTVWearable

unsubscribe(): Promise<void>

取消通知扩展的订阅。使用Promise异步回调。

**系统能力**：SystemCapability.Notification.Notification

**需要权限**：ohos.permission.SUBSCRIBE_NOTIFICATION

**返回值：**

  展开

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[通知错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-notification)。

  展开

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied or current device not supported. |
| 1600001 | Internal error. |
| 1600003 | Failed to connect to the service. |

**示例：**

```
notificationExtensionSubscription.unsubscribe().then(() => {
  console.info("unsubscribe success");
}).catch((err: BusinessError) => {
  console.error(`unsubscribe fail: ${JSON.stringify(err)}`);
});
```

## notificationExtensionSubscription.getSubscribeInfo

 支持设备PhonePC/2in1TabletTVWearable

getSubscribeInfo(): Promise<NotificationExtensionSubscriptionInfo[]>

获取当前应用的通知扩展订阅信息。使用Promise异步回调。

**系统能力**：SystemCapability.Notification.Notification

**需要权限**：ohos.permission.SUBSCRIBE_NOTIFICATION

**返回值：**

  展开

| 类型 | 说明 |
| --- | --- |
| Promise< NotificationExtensionSubscriptionInfo[] > | Promise对象，返回一个 NotificationExtensionSubscriptionInfo[] 对象数组，表示应用的订阅信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[通知错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-notification)。

  展开

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied or current device not supported. |
| 1600001 | Internal error. |
| 1600003 | Failed to connect to the service. |

**示例：**

```
notificationExtensionSubscription.getSubscribeInfo().then((data: notificationExtensionSubscription.NotificationExtensionSubscriptionInfo[]) => {
  console.info(`getSubscribeInfo successfully. Data: ${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
  console.error(`getSubscribeInfo fail: ${JSON.stringify(err)}`);
});
```

## notificationExtensionSubscription.isUserGranted

 支持设备PhonePC/2in1TabletTVWearable

isUserGranted(): Promise<boolean>

查询"允许获取本机通知"的开关状态。使用Promise异步回调。

**系统能力**：SystemCapability.Notification.Notification

**需要权限**：ohos.permission.SUBSCRIBE_NOTIFICATION

**返回值：**

  展开

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示功能已启用；返回false表示功能未启用。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)、[通知错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-notification)。

  展开

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied or current device not supported. |
| 1600001 | Internal error. |
| 1600003 | Failed to connect to the service. |

**示例：**

```
notificationExtensionSubscription.isUserGranted().then((isOpen: boolean) => {
  if (isOpen) {
    console.info('isUserGranted true');
  } else {
    console.info('isUserGranted false');
  }
}).catch((err: BusinessError) => {
  console.error(`isUserGranted fail: ${JSON.stringify(err)}`);
});
```

## notificationExtensionSubscription.getUserGrantedEnabledBundles

 支持设备PhonePC/2in1TabletTVWearable

getUserGrantedEnabledBundles(): Promise<GrantedBundleInfo[]>

获取指定应用中"已获取的本机通知"通知开关开启的应用列表。使用Promise异步回调。

**系统能力**：SystemCapability.Notification.Notification

**需要权限**：ohos.permission.SUBSCRIBE_NOTIFICATION

**返回值：**

  展开

| 类型 | 说明 |
| --- | --- |
| Promise< GrantedBundleInfo[] > | Promise对象，返回获取指定应用中"已获取的本机通知"通知开关开启的应用列表。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[通知错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-notification)。

  展开

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied or current device not supported. |
| 1600001 | Internal error. |
| 1600003 | Failed to connect to the service. |

**示例：**

```
notificationExtensionSubscription.getUserGrantedEnabledBundles().then((data: notificationExtensionSubscription.GrantedBundleInfo[]) => {
  console.info(`getUserGrantedEnabledBundles successfully. Data: ${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
  console.error(`getUserGrantedEnabledBundles fail: ${JSON.stringify(err)}`);
});
```

## NotificationExtensionSubscriptionInfo

 支持设备PhonePC/2in1TabletTVWearable

type NotificationExtensionSubscriptionInfo = _NotificationExtensionSubscriptionInfo

用于描述通知扩展订阅的信息。

**系统能力**： SystemCapability.Notification.Notification

  展开

| 类型 | 说明 |
| --- | --- |
| _NotificationExtensionSubscriptionInfo | 用于描述通知扩展订阅的信息。 |

## NotificationInfo

 支持设备PhonePC/2in1TabletTVWearable

type NotificationInfo = _NotificationInfo

通知订阅扩展能力中[onReceiveMessage](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-notificationsubscriberextensionability#onreceivemessage)回调的通知信息。

**系统能力**：SystemCapability.Notification.Notification

  展开

| 类型 | 说明 |
| --- | --- |
| _NotificationInfo | 通知订阅扩展能力中 onReceiveMessage 回调的通知信息。 |

## SubscribeType

 支持设备PhonePC/2in1TabletTVWearable

表示通知扩展订阅的类型。

**系统能力**：SystemCapability.Notification.Notification

  展开

| 名称 | 值 | 说明 |
| --- | --- | --- |
| BLUETOOTH | 0 | 通过蓝牙订阅通知。 |

## BundleOption

 支持设备PhonePC/2in1TabletTVWearable

type BundleOption = _BundleOption

指定应用的包信息。

**系统能力**： SystemCapability.Notification.Notification

  展开

| 类型 | 说明 |
| --- | --- |
| _BundleOption | 指定应用的包信息。 |

## GrantedBundleInfo

 支持设备PhonePC/2in1TabletTVWearable

type GrantedBundleInfo = _GrantedBundleInfo

授权应用的包信息。

**系统能力**： SystemCapability.Notification.Notification

  展开

| 类型 | 说明 |
| --- | --- |
| _GrantedBundleInfo | 授权应用的包信息。 |