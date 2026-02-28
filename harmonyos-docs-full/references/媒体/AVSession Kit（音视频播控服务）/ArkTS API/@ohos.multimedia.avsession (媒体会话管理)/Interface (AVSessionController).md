# Interface (AVSessionController)

AVSessionController控制器可查看会话ID，并可完成对会话发送命令及事件，获取会话元数据，播放状态信息等操作。

 说明 

- 本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
- 本Interface首批接口从API version 10开始支持。

## 导入模块

 支持设备PhonePC/2in1TabletTVWearable

```
import { avSession } from '@kit.AVSessionKit';
```

## 属性

 支持设备PhonePC/2in1TabletTVWearable

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

  展开

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| sessionId 10+ | string | 是 | 否 | AVSessionController对象唯一的会话标识。 |

**示例：**

```
import { BusinessError } from '@kit.BasicServicesKit';
import { avSession } from '@kit.AVSessionKit';

@Entry
@Component
struct Index {
  private tag: string = "createNewSession";
  private sessionId: string = "";
  private AVSessionController?: avSession.AVSessionController;
  private currentAVSession?: avSession.AVSession;
  context = this.getUIContext();

  aboutToAppear(): void {

    avSession.createAVSession(this.getUIContext().getHostContext(), this.tag, "audio").then(async (data: avSession.AVSession) => {
      this.currentAVSession = data;
      this.sessionId = this.currentAVSession.sessionId;
      this.AVSessionController = await this.currentAVSession.getController();
      console.info('CreateAVSession :  SUCCESS :sessionId = ${this.sessionId}');
    }).catch((err: BusinessError) => {
      console.error(`CreateController BusinessError: code: ${err.code}, message: ${err.message}`);
    });
  }

  build() {
    Column() {
      Text('AVSession Demo')
        .fontSize(20)
        .margin(10)
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }
}
```

## getAVPlaybackState 10+

 支持设备PhonePC/2in1TabletTVWearable

getAVPlaybackState(callback: AsyncCallback<AVPlaybackState>): void

获取当前的远端播放状态。结果通过callback异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback< AVPlaybackState > | 是 | 回调函数，返回远端播放状态。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

  展开

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |

**示例：**

```
import { BusinessError } from '@kit.BasicServicesKit';

avsessionController.getAVPlaybackState((err: BusinessError, state: avSession.AVPlaybackState) => {
  if (err) {
    console.error(`getAVPlaybackState BusinessError: code: ${err.code}, message: ${err.message}`);
  } else {
    console.info('getAVPlaybackState : SUCCESS');
  }
});
```

## getAVPlaybackState 10+

 支持设备PhonePC/2in1TabletTVWearable

getAVPlaybackState(): Promise<AVPlaybackState>

获取当前的远端播放状态。结果通过Promise异步回调方式返回。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

  展开

| 类型 | 说明 |
| --- | --- |
| Promise< AVPlaybackState > | Promise对象，返回远端播放状态。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

  展开

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |

**示例：**

```
import { BusinessError } from '@kit.BasicServicesKit';

avsessionController.getAVPlaybackState().then((state: avSession.AVPlaybackState) => {
  console.info('getAVPlaybackState : SUCCESS');
}).catch((err: BusinessError) => {
  console.error(`getAVPlaybackState BusinessError: code: ${err.code}, message: ${err.message}`);
});
```

## getAVMetadata 10+

 支持设备PhonePC/2in1TabletTVWearable

getAVMetadata(): Promise<AVMetadata>

获取会话元数据。结果通过Promise异步回调方式返回。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

  展开

| 类型 | 说明 |
| --- | --- |
| Promise< AVMetadata > | Promise对象，返回会话元数据。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

  展开

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |

**示例：**

```
import { BusinessError } from '@kit.BasicServicesKit';

avsessionController.getAVMetadata().then((metadata: avSession.AVMetadata) => {
  console.info(`GetAVMetadata : SUCCESS : assetId : ${metadata.assetId}`);
}).catch((err: BusinessError) => {
  console.error(`GetAVMetadata BusinessError: code: ${err.code}, message: ${err.message}`);
});
```

## getAVMetadata 10+

 支持设备PhonePC/2in1TabletTVWearable

getAVMetadata(callback: AsyncCallback<AVMetadata>): void

获取会话元数据。结果通过callback异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback< AVMetadata > | 是 | 回调函数，返回会话元数据。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

  展开

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |

**示例：**

```
import { BusinessError } from '@kit.BasicServicesKit';

avsessionController.getAVMetadata((err: BusinessError, metadata: avSession.AVMetadata) => {
  if (err) {
    console.error(`GetAVMetadata BusinessError: code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`GetAVMetadata : SUCCESS : assetId : ${metadata.assetId}`);
  }
});
```

## getAVQueueTitle 10+

 支持设备PhonePC/2in1TabletTVWearable

getAVQueueTitle(): Promise<string>

获取当前会话播放列表的名称。结果通过Promise异步回调方式返回。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

  展开

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回播放列表名称。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

  展开

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |

**示例：**

```
import { BusinessError } from '@kit.BasicServicesKit';

avsessionController.getAVQueueTitle().then((title: string) => {
  console.info(`GetAVQueueTitle : SUCCESS : title : ${title}`);
}).catch((err: BusinessError) => {
  console.error(`GetAVQueueTitle BusinessError: code: ${err.code}, message: ${err.message}`);
});
```

## getAVQueueTitle 10+

 支持设备PhonePC/2in1TabletTVWearable

getAVQueueTitle(callback: AsyncCallback<string>): void

获取当前播放列表的名称。结果通过callback异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<string> | 是 | 回调函数，返回播放列表名称。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

  展开

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |

**示例：**

```
import { BusinessError } from '@kit.BasicServicesKit';

avsessionController.getAVQueueTitle((err: BusinessError, title: string) => {
  if (err) {
    console.error(`GetAVQueueTitle BusinessError: code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`GetAVQueueTitle : SUCCESS : title : ${title}`);
  }
});
```

## getAVQueueItems 10+

 支持设备PhonePC/2in1TabletTVWearable

getAVQueueItems(): Promise<Array<AVQueueItem>>

获取当前会话播放列表相关信息。结果通过Promise异步回调方式返回。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

  展开

| 类型 | 说明 |
| --- | --- |
| Promise<Array< AVQueueItem >> | Promise对象，返回播放列表队列。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

  展开

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |

**示例：**

```
import { BusinessError } from '@kit.BasicServicesKit';

avsessionController.getAVQueueItems().then((items: avSession.AVQueueItem[]) => {
  console.info(`GetAVQueueItems : SUCCESS : length : ${items.length}`);
}).catch((err: BusinessError) => {
  console.error(`GetAVQueueItems BusinessError: code: ${err.code}, message: ${err.message}`);
});
```

## getAVQueueItems 10+

 支持设备PhonePC/2in1TabletTVWearable

getAVQueueItems(callback: AsyncCallback<Array<AVQueueItem>>): void

获取当前播放列表相关信息。结果通过callback异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<Array< AVQueueItem >> | 是 | 回调函数，返回播放列表队列。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

  展开

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |

**示例：**

```
import { BusinessError } from '@kit.BasicServicesKit';

avsessionController.getAVQueueItems((err: BusinessError, items: avSession.AVQueueItem[]) => {
  if (err) {
    console.error(`GetAVQueueItems BusinessError: code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`GetAVQueueItems : SUCCESS : length : ${items.length}`);
  }
});
```

## skipToQueueItem 10+

 支持设备PhonePC/2in1TabletTVWearable

skipToQueueItem(itemId: number): Promise<void>

设置指定播放列表单项的ID，发送给session端处理，session端可以选择对这个单项歌曲进行播放。结果通过Promise异步回调方式返回。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| itemId | number | 是 | 播放列表单项的ID值，用以表示选中的播放列表单项。 |

**返回值：**

  展开

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。当播放列表单项ID设置成功，无返回结果，否则返回错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

  展开

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |

**示例：**

```
import { BusinessError } from '@kit.BasicServicesKit';

let queueItemId = 0;
avsessionController.skipToQueueItem(queueItemId).then(() => {
  console.info('SkipToQueueItem successfully');
}).catch((err: BusinessError) => {
  console.error(`SkipToQueueItem BusinessError: code: ${err.code}, message: ${err.message}`);
});
```

## skipToQueueItem 10+

 支持设备PhonePC/2in1TabletTVWearable

skipToQueueItem(itemId: number, callback: AsyncCallback<void>): void

设置指定播放列表单项的ID，发送给session端处理，session端可以选择对这个单项歌曲进行播放。结果通过callback异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| itemId | number | 是 | 播放列表单项的ID值，用以表示选中的播放列表单项。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当播放状态设置成功，err为undefined，否则返回错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

  展开

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |

**示例：**

```
import { BusinessError } from '@kit.BasicServicesKit';

let queueItemId = 0;
avsessionController.skipToQueueItem(queueItemId, (err: BusinessError) => {
  if (err) {
    console.error(`SkipToQueueItem BusinessError: code: ${err.code}, message: ${err.message}`);
  } else {
    console.info('SkipToQueueItem successfully');
  }
});
```

## getOutputDevice 10+

 支持设备PhonePC/2in1TabletTVWearable

getOutputDevice(): Promise<OutputDeviceInfo>

获取播放设备信息。结果通过Promise异步回调方式返回。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

  展开

| 类型 | 说明 |
| --- | --- |
| Promise< OutputDeviceInfo > | Promise对象，返回播放设备信息。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

  展开

| 错误码ID | 错误信息 |
| --- | --- |
| 600101 | Session service exception. |
| 600103 | The session controller does not exist. |

**示例：**

```
import { BusinessError } from '@kit.BasicServicesKit';

avsessionController.getOutputDevice().then((deviceInfo: avSession.OutputDeviceInfo) => {
  console.info('GetOutputDevice : SUCCESS');
}).catch((err: BusinessError) => {
  console.error(`GetOutputDevice BusinessError: code: ${err.code}, message: ${err.message}`);
});
```

## getOutputDevice 10+

 支持设备PhonePC/2in1TabletTVWearable

getOutputDevice(callback: AsyncCallback<OutputDeviceInfo>): void

获取播放设备信息。结果通过callback异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback< OutputDeviceInfo > | 是 | 回调函数，返回播放设备信息。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

  展开

| 错误码ID | 错误信息 |
| --- | --- |
| 600101 | Session service exception. |
| 600103 | The session controller does not exist. |

**示例：**

```
import { BusinessError } from '@kit.BasicServicesKit';

avsessionController.getOutputDevice((err: BusinessError, deviceInfo: avSession.OutputDeviceInfo) => {
  if (err) {
    console.error(`GetOutputDevice BusinessError: code: ${err.code}, message: ${err.message}`);
  } else {
    console.info('GetOutputDevice : SUCCESS');
  }
});
```

## sendAVKeyEvent 10+

 支持设备PhonePC/2in1TabletTVWearable

sendAVKeyEvent(event: KeyEvent): Promise<void>

发送按键事件到控制器对应的会话。结果通过Promise异步回调方式返回。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | KeyEvent | 是 | 按键事件。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

  展开

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| 600101 | Session service exception. |
| 600102 | The session does not exist. |
| 600103 | The session controller does not exist. |
| 600105 | Invalid session command. |
| 600106 | The session is not activated. |

**返回值：**

  展开

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。当事件发送成功，无返回结果，否则返回错误对象。 |

**示例：**

```
import { Key, KeyEvent } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';

let keyItem: Key = {code:0x49, pressedTime:2, deviceId:0};
let event:KeyEvent = {id:1, deviceId:0, actionTime:1, screenId:1, windowId:1, action:2, key:keyItem, unicodeChar:0, keys:[keyItem], ctrlKey:false, altKey:false, shiftKey:false, logoKey:false, fnKey:false, capsLock:false, numLock:false, scrollLock:false};

avsessionController.sendAVKeyEvent(event).then(() => {
  console.info('SendAVKeyEvent Successfully');
}).catch((err: BusinessError) => {
  console.error(`SendAVKeyEvent BusinessError: code: ${err.code}, message: ${err.message}`);
});
```

## sendAVKeyEvent 10+

 支持设备PhonePC/2in1TabletTVWearable

sendAVKeyEvent(event: KeyEvent, callback: AsyncCallback<void>): void

发送按键事件到会话。结果通过callback异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | KeyEvent | 是 | 按键事件。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当事件发送成功，err为undefined，否则返回错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

  展开

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| 600101 | Session service exception. |
| 600102 | The session does not exist. |
| 600103 | The session controller does not exist. |
| 600105 | Invalid session command. |
| 600106 | The session is not activated. |

**示例：**

```
import { Key, KeyEvent } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';

let keyItem: Key = {code:0x49, pressedTime:2, deviceId:0};
let event:KeyEvent = {id:1, deviceId:0, actionTime:1, screenId:1, windowId:1, action:2, key:keyItem, unicodeChar:0, keys:[keyItem], ctrlKey:false, altKey:false, shiftKey:false, logoKey:false, fnKey:false, capsLock:false, numLock:false, scrollLock:false};
avsessionController.sendAVKeyEvent(event, (err: BusinessError) => {
  if (err) {
    console.error(`SendAVKeyEvent BusinessError: code: ${err.code}, message: ${err.message}`);
  } else {
    console.info('SendAVKeyEvent Successfully');
  }
});
```

## getLaunchAbility 10+

 支持设备PhonePC/2in1TabletTVWearable

getLaunchAbility(): Promise<WantAgent>

获取应用在会话中保存的WantAgent对象。结果通过Promise异步回调方式返回。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

  展开

| 类型 | 说明 |
| --- | --- |
| Promise< WantAgent > | Promise对象，返回在 setLaunchAbility 保存的对象，包括应用的相关属性信息，如bundleName，abilityName，deviceId等。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

  展开

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |

**示例：**

```
import { BusinessError } from '@kit.BasicServicesKit';

avsessionController.getLaunchAbility().then((agent: object) => {
  console.info(`GetLaunchAbility : SUCCESS : wantAgent : ${agent}`);
}).catch((err: BusinessError) => {
  console.error(`GetLaunchAbility BusinessError: code: ${err.code}, message: ${err.message}`);
});
```

## getLaunchAbility 10+

 支持设备PhonePC/2in1TabletTVWearable

getLaunchAbility(callback: AsyncCallback<WantAgent>): void

获取应用在会话中保存的WantAgent对象。结果通过callback异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback< WantAgent > | 是 | 回调函数。返回在 setLaunchAbility 保存的对象，包括应用的相关属性信息，如bundleName，abilityName，deviceId等。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

  展开

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |

**示例：**

```
import { BusinessError } from '@kit.BasicServicesKit';

avsessionController.getLaunchAbility((err: BusinessError, agent: object) => {
  if (err) {
    console.error(`GetLaunchAbility BusinessError: code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`GetLaunchAbility : SUCCESS : wantAgent : ${agent}`);
  }
});
```

## getRealPlaybackPositionSync 10+

 支持设备PhonePC/2in1TabletTVWearable

getRealPlaybackPositionSync(): number

获取当前播放位置。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

  展开

| 类型 | 说明 |
| --- | --- |
| number | 时间节点，毫秒数。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

  展开

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |

**示例：**

```
let time: number = avsessionController.getRealPlaybackPositionSync();
```

## isActive 10+

 支持设备PhonePC/2in1TabletTVWearable

isActive(): Promise<boolean>

获取会话是否被激活。结果通过Promise异步回调方式返回。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

  展开

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象，返回会话是否为激活状态，true表示被激活，false表示禁用。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

  展开

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |

**示例：**

```
import { BusinessError } from '@kit.BasicServicesKit';

avsessionController.isActive().then((isActive: boolean) => {
  console.info(`IsActive : SUCCESS : isactive : ${isActive}`);
}).catch((err: BusinessError) => {
  console.error(`IsActive BusinessError: code: ${err.code}, message: ${err.message}`);
});
```

## isActive 10+

 支持设备PhonePC/2in1TabletTVWearable

isActive(callback: AsyncCallback<boolean>): void

判断会话是否被激活。结果通过callback异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<boolean> | 是 | 回调函数。返回会话是否为激活状态，true表示被激活，false表示禁用。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

  展开

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |

**示例：**

```
import { BusinessError } from '@kit.BasicServicesKit';

avsessionController.isActive((err: BusinessError, isActive: boolean) => {
  if (err) {
    console.error(`IsActive BusinessError: code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`IsActive : SUCCESS : isactive : ${isActive}`);
  }
});
```

## destroy 10+

 支持设备PhonePC/2in1TabletTVWearable

destroy(): Promise<void>

销毁当前控制器，销毁后当前控制器不可再用。结果通过Promise异步回调方式返回。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

  展开

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。当控制器销毁成功，无返回结果，否则返回错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

  展开

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |

**示例：**

```
import { BusinessError } from '@kit.BasicServicesKit';

avsessionController.destroy().then(() => {
  console.info('Destroy : SUCCESS ');
}).catch((err: BusinessError) => {
  console.error(`Destroy BusinessError: code: ${err.code}, message: ${err.message}`);
});
```

## destroy 10+

 支持设备PhonePC/2in1TabletTVWearable

destroy(callback: AsyncCallback<void>): void

销毁当前控制器，销毁后当前控制器不可再用。结果通过callback异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当控制器销毁成功，err为undefined，否则返回错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

  展开

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |

**示例：**

```
import { BusinessError } from '@kit.BasicServicesKit';

avsessionController.destroy((err: BusinessError) => {
  if (err) {
    console.error(`Destroy BusinessError: code: ${err.code}, message: ${err.message}`);
  } else {
    console.info('Destroy : SUCCESS ');
  }
});
```

## getValidCommands 10+

 支持设备PhonePC/2in1TabletTVWearable

getValidCommands(): Promise<Array<AVControlCommandType>>

获取会话支持的有效命令。结果通过Promise异步回调方式返回。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

  展开

| 类型 | 说明 |
| --- | --- |
| Promise<Array< AVControlCommandType >> | Promise对象。返回有效命令的集合。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

  展开

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |

**示例：**

```
import { BusinessError } from '@kit.BasicServicesKit';

avsessionController.getValidCommands().then((validCommands: avSession.AVControlCommandType[]) => {
  console.info(`GetValidCommands : SUCCESS : size : ${validCommands.length}`);
}).catch((err: BusinessError) => {
  console.error(`GetValidCommands BusinessError: code: ${err.code}, message: ${err.message}`);
});
```

## getValidCommands 10+

 支持设备PhonePC/2in1TabletTVWearable

getValidCommands(callback: AsyncCallback<Array<AVControlCommandType>>): void

获取会话支持的有效命令。结果通过callback异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<Array< AVControlCommandType >> | 是 | 回调函数，返回有效命令的集合。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

  展开

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |

**示例：**

```
import { BusinessError } from '@kit.BasicServicesKit';

avsessionController.getValidCommands((err: BusinessError, validCommands: avSession.AVControlCommandType[]) => {
  if (err) {
    console.error(`GetValidCommands BusinessError: code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`GetValidCommands : SUCCESS : size : ${validCommands.length}`);
  }
});
```

## sendControlCommand 10+

 支持设备PhonePC/2in1TabletTVWearable

sendControlCommand(command: AVControlCommand): Promise<void>

通过控制器发送命令到其对应的会话。结果通过Promise异步回调方式返回。

 说明 

媒体控制方在使用sendControlCommand命令前，需要确保控制对应的媒体会话注册了对应的监听，注册媒体会话相关监听的方法请参见接口[on'play'](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-avsession-avsession#onplay10)、[on'pause'](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-avsession-avsession#onpause10)等。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| command | AVControlCommand | 是 | 会话的相关命令和命令相关参数。 |

**返回值：**

  展开

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。当命令发送成功，无返回结果，否则返回错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

  展开

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |
| 6600105 | Invalid session command. |
| 6600106 | The session is not activated. |
| 6600107 | Too many commands or events. |

**示例：**

```
import { BusinessError } from '@kit.BasicServicesKit';

let avCommand: avSession.AVControlCommand = {command:'play'};
avsessionController.sendControlCommand(avCommand).then(() => {
  console.info('SendControlCommand successfully');
}).catch((err: BusinessError) => {
  console.error(`SendControlCommand BusinessError: code: ${err.code}, message: ${err.message}`);
});
```

## sendControlCommand 10+

 支持设备PhonePC/2in1TabletTVWearable

sendControlCommand(command: AVControlCommand, callback: AsyncCallback<void>): void

通过会话控制器发送命令到其对应的会话。结果通过callback异步回调方式返回。

 说明 

媒体控制方在使用sendControlCommand命令前，需要确保控制对应的媒体会话注册了对应的监听，注册媒体会话相关监听的方法请参见接口[on'play'](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-avsession-avsession#onplay10)、[on'pause'](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-avsession-avsession#onpause10)等。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| command | AVControlCommand | 是 | 会话的相关命令和命令相关参数。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当命令发送成功，err为undefined，否则返回错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

  展开

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |
| 6600105 | Invalid session command. |
| 6600106 | The session is not activated. |
| 6600107 | Too many commands or events. |

**示例：**

```
import { BusinessError } from '@kit.BasicServicesKit';

let avCommand: avSession.AVControlCommand = {command:'play'};
avsessionController.sendControlCommand(avCommand, (err: BusinessError) => {
  if (err) {
    console.error(`SendControlCommand BusinessError: code: ${err.code}, message: ${err.message}`);
  } else {
    console.info('SendControlCommand successfully');
  }
});
```

## sendCommonCommand 10+

 支持设备PhonePC/2in1TabletTVWearable

sendCommonCommand(command: string, args: {[key: string]: Object}): Promise<void>

通过会话控制器发送自定义控制命令到其对应的会话。结果通过Promise异步回调方式返回。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| command | string | 是 | 需要设置的自定义控制命令的名称。 |
| args | {[key: string]: Object} | 是 | 需要传递的控制命令键值对。 说明： 参数args支持的数据类型有：字符串、数字、布尔值、对象、数组和文件描述符等，详细介绍请参见 @ohos.app.ability.Want(Want) 。 |

**返回值：**

  展开

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

  展开

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |
| 6600105 | Invalid session command. |
| 6600106 | The session is not activated. |
| 6600107 | Too many commands or events. |

**示例：**

```
import { BusinessError } from '@kit.BasicServicesKit';
import { avSession } from '@kit.AVSessionKit';

let tag: string = "createNewSession";
let sessionId: string = "";
let controller:avSession.AVSessionController | undefined = undefined;
avSession.createAVSession(context, tag, "audio").then(async (data:avSession.AVSession)=> {
  currentAVSession = data;
  sessionId = currentAVSession.sessionId;
  controller = await currentAVSession.getController();
  console.info(`CreateAVSession : SUCCESS :sessionId = ${sessionId}`);
}).catch((err: BusinessError) => {
  console.error(`CreateAVSession BusinessError:code: ${err.code}, message: ${err.message}`)
});
let commandName = "my_command";
if (controller !== undefined) {
  (controller as avSession.AVSessionController).sendCommonCommand(commandName, {command : "This is my command"}).then(() => {
    console.info('SendCommonCommand successfully');
  }).catch((err: BusinessError) => {
    console.error(`SendCommonCommand BusinessError: code: ${err.code}, message: ${err.message}`);
  })
}
```

## sendCommonCommand 10+

 支持设备PhonePC/2in1TabletTVWearable

sendCommonCommand(command: string, args: {[key: string]: Object}, callback: AsyncCallback<void>): void

通过会话控制器发送自定义命令到其对应的会话。结果通过callback异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| command | string | 是 | 需要设置的自定义控制命令的名称。 |
| args | {[key: string]: Object} | 是 | 需要传递的控制命令键值对。 说明： 参数args支持的数据类型有：字符串、数字、布尔值、对象、数组和文件描述符等，详细介绍请参见 @ohos.app.ability.Want(Want) 。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当命令发送成功，err为undefined，否则返回错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

  展开

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |
| 6600105 | Invalid session command. |
| 6600106 | The session is not activated. |
| 6600107 | Too many commands or events. |

**示例：**

```
import { BusinessError } from '@kit.BasicServicesKit';
import { avSession } from '@kit.AVSessionKit';

let tag: string = "createNewSession";
let sessionId: string = "";
let controller:avSession.AVSessionController | undefined = undefined;
avSession.createAVSession(context, tag, "audio").then(async (data:avSession.AVSession)=> {
  currentAVSession = data;
  sessionId = currentAVSession.sessionId;
  controller = await currentAVSession.getController();
  console.info(`CreateAVSession : SUCCESS :sessionId = ${sessionId}`);
}).catch((err: BusinessError) => {
  console.error(`CreateAVSession BusinessError:code: ${err.code}, message: ${err.message}`)
});
let commandName = "my_command";
if (controller !== undefined) {
  (controller as avSession.AVSessionController).sendCommonCommand(commandName, {command : "This is my command"}, (err: BusinessError) => {
    if (err) {
      console.error(`SendCommonCommand BusinessError: code: ${err.code}, message: ${err.message}`);
    }
  })
}
```

## sendCustomData 20+

 支持设备PhonePC/2in1TabletTV

sendCustomData(data: Record<string, Object>): Promise<void>

发送私有数据到远端设备。使用Promise异步回调。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | Record<string, Object> | 是 | 应用程序填充的自定义数据。服务端仅解析key为'customData'，且Object为string类型的对象。 |

**返回值：**

  展开

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

  展开

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception.You are advised to:1.Scheduled retry.2.Destroy the current session or session controller and re-create it. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |

**示例：**

```
import { BusinessError } from '@kit.BasicServicesKit';
import { avSession } from '@kit.AVSessionKit';

@Entry
@Component
struct Index {
  private tag: string = "createNewSession";
  private sessionId: string = "";
  private controller: avSession.AVSessionController | undefined = undefined;
  private currentAVSession?: avSession.AVSession;
  context = this.getUIContext();

  aboutToAppear(): void {
    avSession.createAVSession(this.getUIContext().getHostContext(), this.tag, "audio")
      .then(async (data: avSession.AVSession) => {
        this.currentAVSession = data;
        this.sessionId = this.currentAVSession.sessionId;
        this.controller = await this.currentAVSession.getController();
        console.info(`CreateAVSession : SUCCESS :sessionId = ${this.sessionId}`);
      })
      .catch((err: BusinessError) => {
        console.error(`CreateAVSession BusinessError:code: ${err.code}, message: ${err.message}`)
      });

    if (this.controller !== undefined) {
      (this.controller as avSession.AVSessionController).sendCustomData({ customData: "This is my data" })
    }
  }

  build() {
    Column() {
      Text('AVSession Demo')
        .fontSize(20)
        .margin(10)
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }
}
```

## getExtras 10+

 支持设备PhonePC/2in1TabletTVWearable

getExtras(): Promise<{[key: string]: Object}>

获取媒体提供方设置的自定义媒体数据包。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

  展开

| 类型 | 说明 |
| --- | --- |
| Promise<{[key: string]: Object}> | Promise对象，返回媒体提供方设置的自定义媒体数据包，数据包的内容与setExtras设置的内容完全一致。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

  展开

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |
| 6600105 | Invalid session command. |
| 6600107 | Too many commands or events. |

**示例：**

```
import { BusinessError } from '@kit.BasicServicesKit';
import { avSession } from '@kit.AVSessionKit';

@Entry
@Component
struct Index {
  private tag: string = "createNewSession";
  private sessionId: string = "";
  private controller: avSession.AVSessionController | undefined = undefined;
  private currentAVSession?: avSession.AVSession;
  context = this.getUIContext();

  aboutToAppear(): void {

    avSession.createAVSession(this.getUIContext().getHostContext(), this.tag, "audio")
      .then(async (data: avSession.AVSession) => {
        this.currentAVSession = data;
        this.sessionId = this.currentAVSession.sessionId;
        this.controller = await this.currentAVSession.getController();
        console.info(`CreateAVSession : SUCCESS :sessionId = ${this.sessionId}`);
      }).catch((err: BusinessError) => {
      console.error(`CreateAVSession BusinessError:code: ${err.code}, message: ${err.message}`)
    });
    if (this.controller !== undefined) {
      (this.controller as avSession.AVSessionController).getExtras().then((extras) => {
        console.info(`getExtras : SUCCESS : ${extras}`);
      }).catch((err: BusinessError) => {
        console.error(`getExtras BusinessError: code: ${err.code}, message: ${err.message}`);
      });
    }
  }

  build() {
    Column() {
      Text('AVSession Demo')
        .fontSize(20)
        .margin(10)
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }
}
```

## getExtras 10+

 支持设备PhonePC/2in1TabletTVWearable

getExtras(callback: AsyncCallback<{[key: string]: Object}>): void

获取媒体提供方设置的自定义媒体数据包。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<{[key: string]: Object}> | 是 | 回调函数，返回媒体提供方设置的自定义媒体数据包，数据包的内容与setExtras设置的内容完全一致。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

  展开

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |
| 6600105 | Invalid session command. |
| 6600107 | Too many commands or events. |

**示例：**

```
import { BusinessError } from '@kit.BasicServicesKit';
import { avSession } from '@kit.AVSessionKit';

let tag: string = "createNewSession";
let sessionId: string = "";
let controller:avSession.AVSessionController | undefined = undefined;
avSession.createAVSession(context, tag, "audio").then(async (data:avSession.AVSession)=> {
  currentAVSession = data;
  sessionId = currentAVSession.sessionId;
  controller = await currentAVSession.getController();
  console.info(`CreateAVSession : SUCCESS :sessionId = ${sessionId}`);
}).catch((err: BusinessError) => {
  console.error(`CreateAVSession BusinessError:code: ${err.code}, message: ${err.message}`)
});
if (controller !== undefined) {
  (controller as avSession.AVSessionController).getExtras((err, extras) => {
    if (err) {
      console.error(`getExtras BusinessError: code: ${err.code}, message: ${err.message}`);
    } else {
      console.info(`getExtras : SUCCESS : ${extras}`);
    }
  });
}
```

## getExtrasWithEvent 18+

 支持设备PhonePC/2in1TabletTVWearable

getExtrasWithEvent(extraEvent: string): Promise<ExtraInfo>

根据远端分布式事件类型，获取远端分布式媒体提供方设置的自定义媒体数据包。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| extraEvent | string | 是 | 远端分布式事件类型。可获取的事件类型来自于 setExtras 。 对Wearable设备类型，额外提供以下预设的事件类型： 'AUDIO_GET_VOLUME'：获取远端设备音量。 'AUDIO_GET_AVAILABLE_DEVICES'：获取远端所有可连接设备。 'AUDIO_GET_PREFERRED_OUTPUT_DEVICE_FOR_RENDERER_INFO'：获取远端实际发声设备。 |

**返回值：**

  展开

| 类型 | 说明 |
| --- | --- |
| Promise< ExtraInfo > | Promise对象，返回远端分布式媒体提供方设置的自定义媒体数据包。 参数ExtraInfo支持的数据类型有：字符串、数字、布尔值、对象、数组和文件描述符等，详细介绍请参见 @ohos.app.ability.Want (Want) 。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

  展开

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |
| 6600105 | Invalid session command. |

**示例：**

```
import { BusinessError } from '@kit.BasicServicesKit';

let controller: avSession.AVSessionController | ESObject;
const COMMON_COMMAND_STRING_1 = 'AUDIO_GET_VOLUME';
const COMMON_COMMAND_STRING_2 = 'AUDIO_GET_AVAILABLE_DEVICES';
const COMMON_COMMAND_STRING_3 = 'AUDIO_GET_PREFERRED_OUTPUT_DEVICE_FOR_RENDERER_INFO';
if (controller !== undefined) {
  controller.getExtrasWithEvent(COMMON_COMMAND_STRING_1).then(() => {
    console.info(`${[COMMON_COMMAND_STRING_1]}`);
  }).catch((err: BusinessError) => {
    console.error(`getExtrasWithEvent failed with err: ${err.code}, ${err.message}`);
  })

  controller.getExtrasWithEvent(COMMON_COMMAND_STRING_2).then(() => {
    console.info(`${[COMMON_COMMAND_STRING_2]}`);
  }).catch((err: BusinessError) => {
    console.error(`getExtrasWithEvent failed with err: ${err.code}, ${err.message}`);
  })

  controller.getExtrasWithEvent(COMMON_COMMAND_STRING_3).then(() => {
    console.info(`${[COMMON_COMMAND_STRING_3]}`);
  }).catch((err: BusinessError) => {
    console.error(`getExtrasWithEvent failed with err: ${err.code}, ${err.message}`);
  })
}
```

## on('metadataChange') 10+

 支持设备PhonePC/2in1TabletTVWearable

on(type: 'metadataChange', filter: Array<keyof AVMetadata> | 'all', callback: (data: AVMetadata) => void)

设置元数据变化的监听事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持事件'metadataChange'：当元数据需要更新时，触发该事件。 需要更新表示对应属性值被重新设置过，不论新值与旧值是否相同。 |
| filter | Array<keyof AVMetadata>\|'all' | 是 | 'all'表示关注通话状态所有字段变化；Array<keyof AVMetadata>表示关注Array中的字段变化。 |
| callback | (data: AVMetadata ) => void | 是 | 回调函数，参数data是需要更新的元数据。只包含需要更新的元数据属性，不代表当前全量的元数据。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

  展开

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |

**示例：**

```
avsessionController.on('metadataChange', 'all', (metadata: avSession.AVMetadata) => {
  console.info(`on metadataChange assetId : ${metadata.assetId}`);
});

avsessionController.on('metadataChange', ['assetId', 'title', 'description'], (metadata: avSession.AVMetadata) => {
  console.info(`on metadataChange assetId : ${metadata.assetId}`);
});
```

## off('metadataChange') 10+

 支持设备PhonePC/2in1TabletTVWearable

off(type: 'metadataChange', callback?: (data: AVMetadata) => void)

取消元数据变化事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消对应的监听事件，支持事件'metadataChange'。 |
| callback | (data: AVMetadata ) => void | 否 | 回调函数，参数data是需要更新的元数据。只包含需要更新的元数据属性，并不代表当前全量的元数据。 该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

  展开

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |

**示例：**

```
avsessionController.off('metadataChange');
```

## on('playbackStateChange') 10+

 支持设备PhonePC/2in1TabletTVWearable

on(type: 'playbackStateChange', filter: Array<keyof AVPlaybackState> | 'all', callback: (state: AVPlaybackState) => void)

设置播放状态变化的监听事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持事件'playbackStateChange'，当播放状态需要更新时，触发该事件。 需要更新表示对应属性值被重新设置过，不论新值与旧值是否相同。 |
| filter | Array<keyof AVPlaybackState>\|'all' | 是 | 'all'表示关注播放状态所有字段更新。 Array<keyof AVPlaybackstate> 表示关注Array中的字段更新。 |
| callback | (state: AVPlaybackState ) => void | 是 | 回调函数，参数state是需要更新的播放状态。只包含需要更新的播放状态属性，并不代表当前全量的播放状态。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

  展开

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |

**示例：**

```
avsessionController.on('playbackStateChange', 'all', (playbackState: avSession.AVPlaybackState) => {
  console.info(`on playbackStateChange state : ${playbackState.state}`);
});

avsessionController.on('playbackStateChange', ['state', 'speed', 'loopMode'], (playbackState: avSession.AVPlaybackState) => {
  console.info(`on playbackStateChange state : ${playbackState.state}`);
});
```

## off('playbackStateChange') 10+

 支持设备PhonePC/2in1TabletTVWearable

off(type: 'playbackStateChange', callback?: (state: AVPlaybackState) => void)

取消播放状态变化事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消对应的监听事件，支持事件'playbackStateChange'。 |
| callback | (state: AVPlaybackState ) => void | 否 | 回调函数，参数state是需要更新的播放状态。只包含需要更新的播放状态属性，并不代表当前全量的播放状态。 该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

  展开

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |

**示例：**

```
avsessionController.off('playbackStateChange');
```

## on('callMetadataChange') 11+

 支持设备PhonePC/2in1TabletTVWearable

on(type: 'callMetadataChange', filter: Array<keyof CallMetadata> | 'all', callback: Callback<CallMetadata>): void

设置通话元数据变化的监听事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持事件'callMetadataChange'：当通话元数据变化时，触发该事件。 |
| filter | Array<keyof CallMetadata>\|'all' | 是 | 'all'表示关注通话元数据所有字段变化；Array<keyof CallMetadata> 表示关注Array中的字段变化。\| 'all'。 |
| callback | Callback< CallMetadata > | 是 | 回调函数，参数callmetadata是变化后的通话元数据。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

  展开

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |

**示例：**

```
avsessionController.on('callMetadataChange', 'all', (callmetadata: avSession.CallMetadata) => {
  console.info(`on callMetadataChange state : ${callmetadata.name}`);
});

avsessionController.on('callMetadataChange', ['name'], (callmetadata: avSession.CallMetadata) => {
  console.info(`on callMetadataChange state : ${callmetadata.name}`);
});
```

## off('callMetadataChange') 11+

 支持设备PhonePC/2in1TabletTVWearable

off(type: 'callMetadataChange', callback?: Callback<CallMetadata>): void

取消设置通话元数据变化事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消对应的监听事件，支持事件'callMetadataChange'。 |
| callback | Callback< CallMetadata > | 否 | 回调函数，参数calldata是变化后的通话原数据。 该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

  展开

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |

**示例：**

```
avsessionController.off('callMetadataChange');
```

## on('callStateChange') 11+

 支持设备PhonePC/2in1TabletTVWearable

on(type: 'callStateChange', filter: Array<keyof AVCallState> | 'all', callback: Callback<AVCallState>): void

设置通话状态变化的监听事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持事件'callStateChange'：当通话状态变化时，触发该事件。 |
| filter | Array<keyof AVCallState>\|'all' | 是 | 'all' 表示关注通话状态所有字段变化；Array<keyof AVCallState>表示关注Array中的字段变化。\| 'all'。 |
| callback | Callback< AVCallState > | 是 | 回调函数，参数callstate是变化后的通话状态。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

  展开

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified.2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |

**示例：**

```
avsessionController.on('callStateChange', 'all', (callstate: avSession.AVCallState) => {
  console.info(`on callStateChange state : ${callstate.state}`);
});

avsessionController.on('callStateChange', ['state'], (callstate: avSession.AVCallState) => {
  console.info(`on callStateChange state : ${callstate.state}`);
});
```

## off('callStateChange') 11+

 支持设备PhonePC/2in1TabletTVWearable

off(type: 'callStateChange', callback?: Callback<AVCallState>): void

取消设置通话状态变化事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消对应的监听事件，支持事件'callStateChange'。 |
| callback | Callback< AVCallState > | 否 | 回调函数，参数callstate是变化后的通话状态。 该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

  展开

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |

**示例：**

```
avsessionController.off('callMetadataChange');
```

## on('sessionDestroy') 10+

 支持设备PhonePC/2in1TabletTVWearable

on(type: 'sessionDestroy', callback: () => void)

会话销毁的监听事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持事件'sessionDestroy'：当检测到会话销毁时，触发该事件。 |
| callback | () => void | 是 | 回调函数。当监听事件注册成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

  展开

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |

**示例：**

```
avsessionController.on('sessionDestroy', () => {
  console.info('on sessionDestroy : SUCCESS ');
});
```

## off('sessionDestroy') 10+

 支持设备PhonePC/2in1TabletTVWearable

off(type: 'sessionDestroy', callback?: () => void)

取消监听会话的销毁事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消对应的监听事件，支持事件'sessionDestroy'。 |
| callback | () => void | 否 | 回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。 该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

  展开

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |

**示例：**

```
avsessionController.off('sessionDestroy');
```

## on('activeStateChange') 10+

 支持设备PhonePC/2in1TabletTVWearable

on(type: 'activeStateChange', callback: (isActive: boolean) => void)

会话的激活状态的监听事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持事件'activeStateChange'：当检测到会话的激活状态发生改变时，触发该事件。 |
| callback | (isActive: boolean) => void | 是 | 回调函数。参数isActive表示会话是否被激活。true表示被激活，false表示禁用。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

  展开

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |

**示例：**

```
avsessionController.on('activeStateChange', (isActive: boolean) => {
  console.info(`on activeStateChange : SUCCESS : isActive ${isActive}`);
});
```

## off('activeStateChange') 10+

 支持设备PhonePC/2in1TabletTVWearable

off(type: 'activeStateChange', callback?: (isActive: boolean) => void)

取消监听会话激活状态变化事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消对应的监听事件，支持事件'activeStateChange'。 |
| callback | (isActive: boolean) => void | 否 | 回调函数。参数isActive表示会话是否被激活。true表示被激活，false表示禁用。 该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

  展开

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |

**示例：**

```
avsessionController.off('activeStateChange');
```

## on('validCommandChange') 10+

 支持设备PhonePC/2in1TabletTVWearable

on(type: 'validCommandChange', callback: (commands: Array<AVControlCommandType>) => void)

会话支持的有效命令变化监听事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持事件'validCommandChange'：当检测到会话的合法命令发生改变时，触发该事件。 |
| callback | (commands: Array< AVControlCommandType >) => void | 是 | 回调函数。参数commands是有效命令的集合。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

  展开

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |

**示例：**

```
avsessionController.on('validCommandChange', (validCommands: avSession.AVControlCommandType[]) => {
  console.info(`validCommandChange : SUCCESS : size : ${validCommands.length}`);
  console.info(`validCommandChange : SUCCESS : validCommands : ${validCommands.values()}`);
});
```

## off('validCommandChange') 10+

 支持设备PhonePC/2in1TabletTVWearable

off(type: 'validCommandChange', callback?: (commands: Array<AVControlCommandType>) => void)

取消监听会话有效命令变化事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消对应的监听事件，支持事件'validCommandChange'。 |
| callback | (commands: Array< AVControlCommandType >) => void | 否 | 回调函数。参数commands是有效命令的集合。 该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

  展开

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |

**示例：**

```
avsessionController.off('validCommandChange');
```

## on('outputDeviceChange') 10+

 支持设备PhonePC/2in1TabletTVWearable

on(type: 'outputDeviceChange', callback: (state: ConnectionState, device: OutputDeviceInfo) => void): void

设置播放设备变化的监听事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持事件为'outputDeviceChange'：当播放设备变化时，触发该事件）。 |
| callback | (state: ConnectionState , device: OutputDeviceInfo ) => void | 是 | 回调函数，参数device是设备相关信息。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

  展开

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |

**示例：**

```
avsessionController.on('outputDeviceChange', (state: avSession.ConnectionState, device: avSession.OutputDeviceInfo) => {
  console.info(`on outputDeviceChange state: ${state}, device : ${device}`);
});
```

## off('outputDeviceChange') 10+

 支持设备PhonePC/2in1TabletTVWearable

off(type: 'outputDeviceChange', callback?: (state: ConnectionState, device: OutputDeviceInfo) => void): void

取消监听分布式设备变化事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消对应的监听事件，支持事件'outputDeviceChange'。 |
| callback | (state: ConnectionState , device: OutputDeviceInfo ) => void | 否 | 回调函数，参数device是设备相关信息。 该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

  展开

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |

**示例：**

```
avsessionController.off('outputDeviceChange');
```

## on('sessionEvent') 10+

 支持设备PhonePC/2in1TabletTVWearable

on(type: 'sessionEvent', callback: (sessionEvent: string, args: {[key: string]: Object}) => void): void

媒体控制器设置会话自定义事件变化的监听器。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持事件'sessionEvent'：当会话事件变化时，触发该事件。 |
| callback | (sessionEvent: string, args: {[key: string]: Object}) => void | 是 | 回调函数，sessionEvent为变化的会话事件名，args为事件的参数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

  展开

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |

**示例：**

```
import { BusinessError } from '@kit.BasicServicesKit';
import { avSession } from '@kit.AVSessionKit';

let tag: string = "createNewSession";
let sessionId: string = "";
let controller:avSession.AVSessionController | undefined = undefined;
avSession.createAVSession(context, tag, "audio").then(async (data:avSession.AVSession)=> {
  currentAVSession = data;
  sessionId = currentAVSession.sessionId;
  controller = await currentAVSession.getController();
  console.info(`CreateAVSession : SUCCESS :sessionId = ${sessionId}`);
}).catch((err: BusinessError) => {
  console.error(`CreateAVSession BusinessError:code: ${err.code}, message: ${err.message}`)
});
if (controller !== undefined) {
  (controller as avSession.AVSessionController).on('sessionEvent', (sessionEvent, args) => {
    console.info(`OnSessionEvent, sessionEvent is ${sessionEvent}, args: ${JSON.stringify(args)}`);
  });
}
```

## off('sessionEvent') 10+

 支持设备PhonePC/2in1TabletTVWearable

off(type: 'sessionEvent', callback?: (sessionEvent: string, args: {[key: string]: Object}) => void): void

取消会话事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消对应的监听事件，支持事件'sessionEvent'。 |
| callback | (sessionEvent: string, args: {[key: string]: Object}) => void | 否 | 回调函数，参数sessionEvent是变化的事件名，args为事件的参数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

  展开

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |

**示例：**

```
avsessionController.off('sessionEvent');
```

## on('queueItemsChange') 10+

 支持设备PhonePC/2in1TabletTVWearable

on(type: 'queueItemsChange', callback: (items: Array<[AVQueueItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-avsession-i#avqueueitem10)>) => void): void

媒体控制器设置会话自定义播放列表变化的监听器。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持事件'queueItemsChange'：当session修改播放列表时，触发该事件。 |
| callback | (items: Array< AVQueueItem >) => void | 是 | 回调函数，items为变化的播放列表。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

  展开

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |

**示例：**

```
avsessionController.on('queueItemsChange', (items: avSession.AVQueueItem[]) => {
  console.info(`OnQueueItemsChange, items length is ${items.length}`);
});
```

## off('queueItemsChange') 10+

 支持设备PhonePC/2in1TabletTVWearable

off(type: 'queueItemsChange', callback?: (items: Array<[AVQueueItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-avsession-i#avqueueitem10)>) => void): void

取消播放列表变化事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消对应的监听事件，支持事件'queueItemsChange'。 |
| callback | (items: Array< AVQueueItem >) => void | 否 | 回调函数，参数items是变化的播放列表。 该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

  展开

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |

**示例：**

```
avsessionController.off('queueItemsChange');
```

## on('queueTitleChange') 10+

 支持设备PhonePC/2in1TabletTVWearable

on(type: 'queueTitleChange', callback: (title: string) => void): void

媒体控制器设置会话自定义播放列表的名称变化的监听器。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持事件'queueTitleChange'：当session修改播放列表名称时，触发该事件。 |
| callback | (title: string) => void | 是 | 回调函数，title为变化的播放列表名称。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

  展开

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |

**示例：**

```
avsessionController.on('queueTitleChange', (title: string) => {
  console.info(`queueTitleChange, title is ${title}`);
});
```

## off('queueTitleChange') 10+

 支持设备PhonePC/2in1TabletTVWearable

off(type: 'queueTitleChange', callback?: (title: string) => void): void

取消播放列表名称变化事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消对应的监听事件，支持事件'queueTitleChange'。 |
| callback | (title: string) => void | 否 | 回调函数，参数items是变化的播放列表名称。 该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

  展开

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |

**示例：**

```
avsessionController.off('queueTitleChange');
```

## on('extrasChange') 10+

 支持设备PhonePC/2in1TabletTVWearable

on(type: 'extrasChange', callback: (extras: {[key: string]: Object}) => void): void

媒体控制器设置自定义媒体数据包事件变化的监听器。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持事件'extrasChange'：当媒体提供方设置自定义媒体数据包时，触发该事件。 |
| callback | (extras: {[key: string]: Object}) => void | 是 | 回调函数，extras为媒体提供方新设置的自定义媒体数据包，该自定义媒体数据包与dispatchSessionEvent方法设置的数据包完全一致。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

  展开

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |

**示例：**

```
import { BusinessError } from '@kit.BasicServicesKit';
import { avSession } from '@kit.AVSessionKit';

let tag: string = "createNewSession";
let sessionId: string = "";
let controller:avSession.AVSessionController | undefined = undefined;
avSession.createAVSession(context, tag, "audio").then(async (data:avSession.AVSession)=> {
  currentAVSession = data;
  sessionId = currentAVSession.sessionId;
  controller = await currentAVSession.getController();
  console.info(`CreateAVSession : SUCCESS :sessionId = ${sessionId}`);
}).catch((err: BusinessError) => {
  console.error(`CreateAVSession BusinessError:code: ${err.code}, message: ${err.message}`)
});
if (controller !== undefined) {
  (controller as avSession.AVSessionController).on('extrasChange', (extras) => {
    console.info(`Caught extrasChange event,the new extra is: ${JSON.stringify(extras)}`);
  });
}
```

## off('extrasChange') 10+

 支持设备PhonePC/2in1TabletTVWearable

off(type: 'extrasChange', callback?: (extras: {[key: string]: Object}) => void): void

取消自定义媒体数据包变化事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消对应的监听事件，支持事件'extrasChange'。 |
| callback | (extras: {[key: string]: Object}) => void | 否 | 注册监听事件时的回调函数。 该参数为可选参数，若不填写该参数，则认为取消会话所有与此事件相关的监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

  展开

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |

**示例：**

```
avsessionController.off('extrasChange');
```

## on('customDataChange') 20+

 支持设备PhonePC/2in1TabletTV

on(type: 'customDataChange', callback: Callback<Record<string, Object>>): void

注册从远程设备发送的自定义数据的监听器。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持事件'customDataChange'，当媒体提供方发送自定义数据时，触发该事件。 |
| callback | Callback<Record<string, Object>> | 是 | 回调函数，用于接收自定义数据。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

  展开

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |

**示例：**

```
import { BusinessError } from '@kit.BasicServicesKit';
import { avSession } from '@kit.AVSessionKit';

let tag: string = "createNewSession";
let sessionId: string = "";
let controller:avSession.AVSessionController | undefined = undefined;
avSession.createAVSession(context, tag, "audio").then(async (data:avSession.AVSession)=> {
  currentAVSession = data;
  sessionId = currentAVSession.sessionId;
  controller = await currentAVSession.getController();
  console.info(`CreateAVSession : SUCCESS :sessionId = ${sessionId}`);
}).catch((err: BusinessError) => {
  console.error(`CreateAVSession BusinessError:code: ${err.code}, message: ${err.message}`)
});
if (controller !== undefined) {
  (controller as avSession.AVSessionController).on('customDataChange', (callback) => {
    console.info(`Caught customDataChange event,the new callback is: ${JSON.stringify(callback)}`);
  });
}
```

## off('customDataChange') 20+

 支持设备PhonePC/2in1TabletTV

off(type: 'customDataChange', callback?: Callback<Record<string, Object>>): void

取消自定义数据监听。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消对应的监听事件，支持的事件是'customDataChange'。 |
| callback | Callback<Record<string, Object>> | 否 | 注册监听事件时的回调函数。该参数为可选参数，若不填写该参数，则认为取消会话所有与此事件相关的监听。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

  展开

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |

**示例：**

```
avsessionController.off('customDataChange');
```

## getAVPlaybackStateSync 10+

 支持设备PhonePC/2in1TabletTVWearable

getAVPlaybackStateSync(): AVPlaybackState;

使用同步方法获取当前会话的播放状态。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

  展开

| 类型 | 说明 |
| --- | --- |
| AVPlaybackState | 当前会话的播放状态。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

  展开

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |

**示例：**

```
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let playbackState: avSession.AVPlaybackState = avsessionController.getAVPlaybackStateSync();
} catch (err) {
  let error = err as BusinessError;
  console.error(`getAVPlaybackStateSync error, error code: ${error.code}, error message: ${error.message}`);
}
```

## getAVMetadataSync 10+

 支持设备PhonePC/2in1TabletTVWearable

getAVMetadataSync(): AVMetadata

使用同步方法获取会话元数据。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

  展开

| 类型 | 说明 |
| --- | --- |
| AVMetadata | 会话元数据。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

  展开

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |

**示例：**

```
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let metaData: avSession.AVMetadata = avsessionController.getAVMetadataSync();
} catch (err) {
  let error = err as BusinessError;
  console.error(`getAVMetadataSync error, error code: ${error.code}, error message: ${error.message}`);
}
```

## getAVCallState 11+

 支持设备PhonePC/2in1TabletTVWearable

getAVCallState(): Promise<AVCallState>

获取通话状态数据。结果通过Promise异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

  展开

| 类型 | 说明 |
| --- | --- |
| Promise< AVCallState > | Promise对象，返回通话状态。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

  展开

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |

**示例：**

```
import { BusinessError } from '@kit.BasicServicesKit';

avsessionController.getAVCallState().then((callstate: avSession.AVCallState) => {
  console.info(`getAVCallState : SUCCESS : state : ${callstate.state}`);
}).catch((err: BusinessError) => {
  console.error(`getAVCallState BusinessError: code: ${err.code}, message: ${err.message}`);
});
```

## getAVCallState 11+

 支持设备PhonePC/2in1TabletTVWearable

getAVCallState(callback: AsyncCallback<AVCallState>): void

获取通话状态数据。结果通过callback异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback< AVCallState > | 是 | 回调函数，返回通话状态。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

  展开

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |

**示例：**

```
import { BusinessError } from '@kit.BasicServicesKit';

avsessionController.getAVCallState((err: BusinessError, callstate: avSession.AVCallState) => {
  if (err) {
    console.error(`getAVCallState BusinessError: code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`getAVCallState : SUCCESS : state : ${callstate.state}`);
  }
});
```

## getCallMetadata 11+

 支持设备PhonePC/2in1TabletTVWearable

getCallMetadata(): Promise<CallMetadata>

获取通话会话的元数据。结果通过Promise异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

  展开

| 类型 | 说明 |
| --- | --- |
| Promise< CallMetadata > | Promise对象，返回会话元数据。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

  展开

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |

**示例：**

```
import { BusinessError } from '@kit.BasicServicesKit';

avsessionController.getCallMetadata().then((calldata: avSession.CallMetadata) => {
  console.info(`getCallMetadata : SUCCESS : name : ${calldata.name}`);
}).catch((err: BusinessError) => {
  console.error(`getCallMetadata BusinessError: code: ${err.code}, message: ${err.message}`);
});
```

## getCallMetadata 11+

 支持设备PhonePC/2in1TabletTVWearable

getCallMetadata(callback: AsyncCallback<CallMetadata>): void

获取通话会话的元数据。结果通过callback异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback< CallMetadata > | 是 | 回调函数，返回会话元数据。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

  展开

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |

**示例：**

```
import { BusinessError } from '@kit.BasicServicesKit';

avsessionController.getCallMetadata((err: BusinessError, calldata: avSession.CallMetadata) => {
  if (err) {
    console.error(`getCallMetadata BusinessError: code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`getCallMetadata : SUCCESS : name : ${calldata.name}`);
  }
});
```

## getAVQueueTitleSync 10+

 支持设备PhonePC/2in1TabletTVWearable

getAVQueueTitleSync(): string

使用同步方法获取当前会话播放列表的名称。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

  展开

| 类型 | 说明 |
| --- | --- |
| string | 当前会话播放列表名称。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

  展开

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |

**示例：**

```
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let currentQueueTitle: string = avsessionController.getAVQueueTitleSync();
} catch (err) {
  let error = err as BusinessError;
  console.error(`getAVQueueTitleSync error, error code: ${error.code}, error message: ${error.message}`);
}
```

## getAVQueueItemsSync 10+

 支持设备PhonePC/2in1TabletTVWearable

getAVQueueItemsSync(): Array<AVQueueItem>

使用同步方法获取当前会话播放列表相关信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

  展开

| 类型 | 说明 |
| --- | --- |
| Array< AVQueueItem > | 当前会话播放列表队列。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

  展开

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |

**示例：**

```
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let currentQueueItems: Array<avSession.AVQueueItem> = avsessionController.getAVQueueItemsSync();
} catch (err) {
  let error = err as BusinessError;
  console.error(`getAVQueueItemsSync error, error code: ${error.code}, error message: ${error.message}`);
}
```

## getOutputDeviceSync 10+

 支持设备PhonePC/2in1TabletTVWearable

getOutputDeviceSync(): OutputDeviceInfo

使用同步方法获取当前输出设备信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

  展开

| 类型 | 说明 |
| --- | --- |
| OutputDeviceInfo | 当前输出设备信息。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

  展开

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600103 | The session controller does not exist. |

**示例：**

```
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let currentOutputDevice: avSession.OutputDeviceInfo = avsessionController.getOutputDeviceSync();
} catch (err) {
  let error = err as BusinessError;
  console.error(`getOutputDeviceSync error, error code: ${error.code}, error message: ${error.message}`);
}
```

## isActiveSync 10+

 支持设备PhonePC/2in1TabletTVWearable

isActiveSync(): boolean

使用同步方法判断会话是否被激活。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

  展开

| 类型 | 说明 |
| --- | --- |
| boolean | 会话是否为激活状态，true表示被激活，false表示禁用。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

  展开

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |

**示例：**

```
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let isActive: boolean = avsessionController.isActiveSync();
} catch (err) {
  let error = err as BusinessError;
  console.error(`isActiveSync error, error code: ${error.code}, error message: ${error.message}`);
}
```

## getValidCommandsSync 10+

 支持设备PhonePC/2in1TabletTVWearable

getValidCommandsSync(): Array<AVControlCommandType>

使用同步方法获取会话支持的有效命令。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

  展开

| 类型 | 说明 |
| --- | --- |
| Array< AVControlCommandType > | 会话支持的有效命令的集合。 |

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-avsession)。

  展开

| 错误码ID | 错误信息 |
| --- | --- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 6600103 | The session controller does not exist. |

**示例：**

```
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let validCommands: Array<avSession.AVControlCommandType> = avsessionController.getValidCommandsSync();
} catch (err) {
  let error = err as BusinessError;
  console.error(`getValidCommandsSync error, error code: ${error.code}, error message: ${error.message}`);
}
```