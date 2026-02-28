# @ohos.prompt (弹窗)

创建并显示文本提示框、对话框和操作菜单。

 说明 

从API version 9 开始，该接口不再维护，推荐使用新接口[@ohos.promptAction (弹窗)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-promptaction)。

本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

支持设备PhonePC/2in1TabletTVWearable

```
import prompt from '@ohos.prompt'
```

## prompt.showToast

支持设备PhonePC/2in1TabletTVWearable

showToast(options: ShowToastOptions): void

创建并显示文本提示框。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

 展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | ShowToastOptions | 是 | 文本弹窗选项。 |

**示例：**

```
import prompt from '@ohos.prompt'
prompt.showToast({
  message: 'Message Info',
    duration: 2000
});
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170424.56370048140268636795091040585442:50001231000000:2800:079BFF01D774E7537ABF3C2F98188BE4B9C2DE7C78853DF0094C9DBC388D0EA4.gif)

## ShowToastOptions

支持设备PhonePC/2in1TabletTVWearable

文本提示框的选项。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full。

 展开

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| message | string | 是 | 显示的文本信息。 |
| duration | number | 否 | 默认值1500ms，取值区间：1500ms-10000ms。若小于1500ms则取默认值，若大于10000ms则取上限值10000ms。 |
| bottom | string\| number | 否 | 设置弹窗边框距离屏幕底部的位置，无上限值，默认单位vp。 |

## prompt.showDialog

支持设备PhonePC/2in1TabletTVWearable

showDialog(options: ShowDialogOptions): Promise<ShowDialogSuccessResponse>

创建并显示对话框，对话框响应后同步返回结果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

 展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | ShowDialogOptions | 是 | 对话框选项。 |

**返回值：**

 展开

| 类型 | 说明 |
| --- | --- |
| Promise< ShowDialogSuccessResponse > | 对话框响应结果。 |

**示例：**

```
import prompt from '@ohos.prompt'
prompt.showDialog({
  title: 'Title Info',
  message: 'Message Info',
  buttons: [
    {
      text: 'button1',
      color: '#000000'
    },
    {
      text: 'button2',
      color: '#000000'
    }
  ],
})
  .then(data => {
    console.info('showDialog success, click button: ' + data.index);
  })
  .catch((err:Error) => {
    console.info('showDialog error: ' + err);
  })
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170424.68752460368083022977425923941928:50001231000000:2800:CEB79C1810AC48E8B2F182306561919FDBC99CAF9356C046CF65329194862A34.gif)

## prompt.showDialog

支持设备PhonePC/2in1TabletTVWearable

showDialog(options: ShowDialogOptions, callback: AsyncCallback<ShowDialogSuccessResponse>):void

创建并显示对话框，对话框响应结果异步返回。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

 展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | ShowDialogOptions | 是 | 页面显示对话框信息描述。 |
| callback | AsyncCallback< ShowDialogSuccessResponse > | 是 | 对话框响应结果回调。 |

**示例：**

```
import prompt from '@ohos.prompt'
prompt.showDialog({
  title: 'showDialog Title Info',
  message: 'Message Info',
  buttons: [
    {
      text: 'button1',
      color: '#000000'
    },
    {
      text: 'button2',
      color: '#000000'
    }
  ]
}, (err, data) => {
  if (err) {
    console.info('showDialog err: ' + err);
    return;
  }
  console.info('showDialog success callback, click button: ' + data.index);
});
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170424.52629148812427376327380144368404:50001231000000:2800:ADEE86C857420D5D2B28B059A4A474AE44D4C0DF835E4FC2A1CE572E0819F931.gif)

## ShowDialogOptions

支持设备PhonePC/2in1TabletTVWearable

对话框的选项。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

 展开

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| title | string | 否 | 标题文本。 |
| message | string | 否 | 内容文本。 |
| buttons | [ Button , Button ?, Button ?] | 否 | 对话框中按钮的数组，结构为：{text:'button', color: '#666666'}，支持1-3个按钮。其中第一个为positiveButton，第二个为negativeButton，第三个为neutralButton。 |

## ShowDialogSuccessResponse

支持设备PhonePC/2in1TabletTVWearable

对话框的响应结果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

 展开

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 选中按钮在buttons数组中的索引。 |

## prompt.showActionMenu

支持设备PhonePC/2in1TabletTVWearable

showActionMenu(options: ActionMenuOptions, callback: AsyncCallback<ActionMenuSuccessResponse>):void

创建并显示操作菜单，菜单响应结果异步返回。

**系统能力：** 以下各项对应的系统能力均为SystemCapability.ArkUI.ArkUI.Full。

**参数：**

 展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | ActionMenuOptions | 是 | 操作菜单选项。 |
| callback | AsyncCallback< ActionMenuSuccessResponse > | 是 | 菜单响应结果回调。 |

**示例：**

```
import prompt from '@ohos.prompt'
prompt.showActionMenu({
  title: 'Title Info',
  buttons: [
    {
      text: 'item1',
      color: '#666666'
    },
    {
      text: 'item2',
      color: '#000000'
    },
  ]
}, (err, data) => {
  if (err) {
    console.info('showActionMenu err: ' + err);
    return;
  }
  console.info('showActionMenu success callback, click button: ' + data.index);
})
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170424.63455113653995601607048443880159:50001231000000:2800:431D58605B9A25F978B3E5A1B9143A4C530EF943F0AEB5E00F23D4D5C61D7296.gif)

## prompt.showActionMenu

支持设备PhonePC/2in1TabletTVWearable

showActionMenu(options: ActionMenuOptions): Promise<ActionMenuSuccessResponse>

创建并显示操作菜单，菜单响应后同步返回结果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

 展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | ActionMenuOptions | 是 | 操作菜单选项。 |

**返回值：**

 展开

| 类型 | 说明 |
| --- | --- |
| Promise< ActionMenuSuccessResponse > | 菜单响应结果。 |

**示例：**

```
import prompt from '@ohos.prompt'
prompt.showActionMenu({
  title: 'showActionMenu Title Info',
  buttons: [
    {
      text: 'item1',
      color: '#666666'
    },
    {
      text: 'item2',
      color: '#000000'
    },
  ]
})
  .then(data => {
    console.info('showActionMenu success, click button: ' + data.index);
  })
  .catch((err:Error) => {
    console.info('showActionMenu error: ' + err);
  })
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170424.73081294376927404751349017360023:50001231000000:2800:FAD49E63330470B9D6ECBF7E22C0517A14E01EB55BB404101B7C6EAEA61946E6.gif)

## ActionMenuOptions

支持设备PhonePC/2in1TabletTVWearable

操作菜单的选项。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full。

 展开

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| title | string | 否 | 标题文本。 |
| buttons | [ Button , Button ?, Button ?, Button ?, Button ?, Button ?] | 是 | 菜单中菜单项按钮的数组，结构为：{text:'button', color: '#666666'}，支持1-6个按钮。大于6个按钮时弹窗不显示。 |

## ActionMenuSuccessResponse

支持设备PhonePC/2in1TabletTVWearable

操作菜单的响应结果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

 展开

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 选中按钮在buttons数组中的索引，从0开始。 |

## Button

支持设备PhonePC/2in1TabletTVWearable

菜单中的菜单项按钮。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

 展开

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | string | 是 | 按钮文本内容。 |
| color | string | 是 | 按钮文本颜色。 |