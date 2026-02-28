# Web组件对接软键盘

开发者能够通过Web组件对接软键盘，来处理系统软键盘的显示与交互问题，同时实现软键盘的自定义功能。主要有以下场景：

- 拉起系统软键盘输入文字：点击网页输入框时，屏幕下方将弹出系统默认的软键盘。开发者可以通过软键盘输入文字，输入的内容会显示在输入框中。
- 自定义系统软键盘的回车键类型：设置不同的回车键类型，例如：确认、下一个和提交。
- 软键盘避让：在移动设备上，由于输入法通常显示在屏幕下方区域，应用可设置不同的Web页面软键盘避让模式，来避让软键盘。例如：平移、调整大小和不避让。
- 自定义软键盘输入：在移动设备上，可以使用自绘制输入法在Web页面输入，以此替代系统软键盘。

## Web页面输入框输入与软键盘交互的W3C标准支持

为支持Web页面与系统软键盘、自定义软键盘等的良好交互，ArkWeb遵循并实现了W3C规范中的以下输入控制属性：

- type属性

type属性定义了input元素的类型，影响输入的验证、显示方式和键盘类型。常见的type值包括：

  展开

| type值 | 描述 |
| --- | --- |
| text | 默认值。普通文本输入 |
| number | 数字输入 |
| email | 电子邮件地址输入 |
| password | 密码输入 |
| tel | 电话号码输入 |
| url | URL输入 |
| date | 日期选择器 |
| time | 时间选择器 |
| checkbox | 复选框 |
| radio | 单选按钮 |
| file | 文件上传 |
| submit | 提交按钮 |
| reset | 重置按钮 |
| button | 普通按钮 |
- inputmode属性

inputmode属性用于配置输入法类型，默认值：text。

  展开

| inputmode | 描述 |
| --- | --- |
| decimal | 只显示数字键盘，通常还有一个逗号键。 |
| email | 文本键盘，键通常用于电子邮件地址，如[@]。 |
| none | 不应出现键盘。 |
| numeric | 只显示数字键盘。 |
| search | 文本键盘，[enter]键通常显示为[go]。 |
| tel | 只显示数字键盘，通常还有[+]、[*]和[#]键。 |
| text | 默认文本键盘。 |
| url | 文本键盘，键通常用于网址，如[.]和[/]，以及特殊的[.com]键，或者其他通常用于本地设置的域名结束符。 |
- enterkeyhint属性

enterkeyhint属性用于指定移动设备虚拟键盘上回车键的显示方式。

  展开

| enterkeyhint值 | 描述 |
| --- | --- |
| enter | 显示默认的回车键 |
| done | 表示输入完成 |
| go | 表示跳转或执行 |
| next | 进入下一个输入字段 |
| previous | 返回上一个输入字段 |
| search | 执行搜索 |
| send | 发送信息 |

 说明 

点击网页输入框时，屏幕下方将弹出系统默认的软键盘，用户可以进行文字输入。

type属性影响键盘显示、输入验证和元素外观。

inputmode优化移动设备键盘输入体验，不影响基本行为或验证。

## 软键盘自动弹出

为提升用户体验，可以在页面完成加载后，输入框自动获焦并弹出软键盘。通过调用[showTextInput()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inputmethod#showtextinput10)设置软键盘自动弹出功能。

 收起自动换行深色代码主题复制

```
<!-- index.html --> <!DOCTYPE html > < html > < head > < title > 测试网页 </ title > </ head > < body > < h1 > DEMO </ h1 > < input type = "text" id = "input_a" > </ body > </ html >
```

 收起自动换行深色代码主题复制

```
//Index.ets import { webview } from '@kit.ArkWeb' ; import { inputMethod } from '@kit.IMEKit' ; @Entry @Component struct WebComponent { controller : webview. WebviewController = new webview. WebviewController (); build ( ) { Column () { Web ({ src : $rawfile( "index.html" ), controller : this . controller }) . onPageEnd ( () => { this . controller . runJavaScript ( `document.getElementById('input_a').focus()` ). then ( () => { setTimeout ( () => { inputMethod. getController (). showTextInput (); }, 10 ); }); }); } } }
```

## 设置软键盘避让模式

在移动设备上，支持设置Web页面的软键盘避让模式。

1. 在应用代码中设置UIContext的软键盘避让模式[setKeyboardAvoidMode()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-expand-safe-area#setkeyboardavoidmode11)。ArkWeb组件支持Resize和Offset两种模式。

- Resize模式下，应用窗口高度可缩小避开软键盘，ArkWeb组件跟随ArkUI重新布局。
- Offset模式下（以及默认模式），应用窗口高度不变，ArkWeb组件根据自身的避让模式进行避让。

（1）设置UIContext的软键盘避让模式。

 收起自动换行深色代码主题复制

```
import { KeyboardAvoidMode } from '@kit.ArkUI' ; import { hilog } from '@kit.PerformanceAnalysisKit' ; // ··· onWindowStageCreate ( windowStage: window .WindowStage ) { hilog. info ( 0x0000 , 'testTag' , '%{public}s' , 'Ability onWindowStageCreate' ); windowStage. loadContent ( 'pages/Index' , ( err, data ) => { let keyboardAvoidMode = windowStage. getMainWindowSync (). getUIContext (). getKeyboardAvoidMode (); // 设置虚拟键盘抬起时压缩页面大小为减去键盘的高度 windowStage. getMainWindowSync (). getUIContext (). setKeyboardAvoidMode ( KeyboardAvoidMode . RESIZE ); if (err. code ) { hilog. error ( 0x0000 , 'testTag' , 'Failed to load the content. Cause: %{public}s' , JSON . stringify (err) ?? '' ); return ; } hilog. info ( 0x0000 , 'testTag' , 'Succeeded in loading the content. Data: %{public}s' , JSON . stringify (data) ?? '' ); }); }
```

[Entry2Ability.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkWeb/ManageWebPageInteracts/entry2/src/main/ets/entry2ability/Entry2Ability.ets#L18-L48) 

（2）在Web组件中调起软键盘。

 收起自动换行深色代码主题复制

```
<!-- index.html --> <!DOCTYPE html > < html > < head > < title > 测试网页 </ title > </ head > < body > < h1 > DEMO </ h1 > < input type = "text" id = "input_a" > </ body > </ html >
```

 收起自动换行深色代码主题复制

```
//Index.ets import { webview } from '@kit.ArkWeb' ; @Entry @Component struct KeyboardAvoidExample { controller : webview. WebviewController = new webview. WebviewController (); build ( ) { Column () { Row (). height ( "50%" ). width ( "100%" ). backgroundColor ( Color . Gray ) Web ({ src : $rawfile( "index.html" ), controller : this . controller }) Text ( "I can see the bottom of the page" ). width ( "100%" ). textAlign ( TextAlign . Center ). backgroundColor ( Color . Pink ). layoutWeight ( 1 ) }. width ( '100%' ). height ( "100%" ) } }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkWeb/ManageWebPageInteracts/entry2/src/main/ets/pages/Index.ets#L16-L32) 

ArkWeb组件将跟随ArkUI重新布局，效果如图1和图2所示。

**图1** Web组件网页默认软键盘避让模式

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165739.09180046425380403720915396302275:50001231000000:2800:68D98D5A9158A88FD8E6FE2BFFEDD2C497A6730641B2A4DCEBC53AA1363C5AED.png)

**图2** Web组件网页跟随Arkui软键盘避让模式

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165739.44972564819363908343326253863173:50001231000000:2800:44AFC49F1BDADF71F9B9278A6A38F0462701DAAA5C64797F0EE8B311418C8200.png)

2.在UIContext的键盘避让模式为Offset模式时，应用可通过[WebKeyboardAvoidMode()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-e#webkeyboardavoidmode12)设置ArkWeb组件的键盘避让模式。Web组件的[WebKeyboardAvoidMode()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-e#webkeyboardavoidmode12)接口优先级高于W3C侧virtualKeyboard.overlayContent。

- RESIZE_VISUAL：仅调整可视视口的大小，而不调整布局视口的大小。
- RESIZE_CONTENT：调整视觉视口和布局视口的大小。
- OVERLAYS_CONTENT：不调整任何视口的大小，获焦input元素没有滚动到可视区域的行为。

 说明 

可视视口指用户正在看到的网站的区域，该区域的宽度等于移动设备的浏览器窗口的宽度。

布局视口指网页本身的宽度。

在应用代码中设置ArkWeb的软键盘避让模式。

 收起自动换行深色代码主题复制

```
// Index.ets import { webview } from '@kit.ArkWeb' ; @Entry @Component struct KeyboardAvoidExample { controller : webview. WebviewController = new webview. WebviewController (); build ( ) { Column () { Row (). height ( '50%' ). width ( '100%' ). backgroundColor ( Color . Gray ) Web ({ src : $rawfile( 'index.html' ), controller : this . controller }) . keyboardAvoidMode ( WebKeyboardAvoidMode . OVERLAYS_CONTENT ) //此时ArkWeb组件不会调整任何视口的大小。 Text ( 'I can see the bottom of the page' ) . width ( '100%' ) . textAlign ( TextAlign . Center ) . backgroundColor ( Color . Pink ) . layoutWeight ( 1 ) }. width ( '100%' ). height ( '100%' ) } }
```

[SetSKBMode_one.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkWeb/ManageWebPageInteracts/entry/src/main/ets/pages/SetSKBMode_one.ets#L16-L37) 

ArkWeb组件根据避让模式进行避让，效果见图3。

**图3** Web组件网页自身软键盘避让模式

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165739.88475638802247210884118611366204:50001231000000:2800:2F380CC69CB84BBBA43885D8FC09D28B5852DB7A2131AF55A0FEF658B1FFE56E.png)

3.在软键盘弹出时，为使Web组件不发生避让行为，可通过调用[expandSafeArea()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-expand-safe-area#expandsafearea)设置Web组件扩展安全区域。更多详细示例可参考[网页中安全区域计算和避让适配](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/web-safe-area-insets)。

 收起自动换行深色代码主题复制

```
// xxx.ets import { webview } from '@kit.ArkWeb' ; @Entry @Component struct WebComponent { controller : webview. WebviewController = new webview. WebviewController (); build ( ) { Column () { Web ({ src : 'www.example.com' , controller : this . controller }) . width ( '100%' ). height ( '100%' ) . expandSafeArea ([ SafeAreaType . KEYBOARD , SafeAreaType . SYSTEM ]) } } }
```

与其他Web组件行为的交互场景：

  展开

| 交叉场景 | 规格 |
| --- | --- |
| 同层渲染 | 同层Web：软键盘避让方式与普通场景相同。 同层系统组件：由ArkUI负责软键盘避让模式。 |
| 离屏创建组件 | 默认使用与非离屏创建一致的软键盘避让模式，在添加至组件树前设置其他避让模式即可生效。 |
| customDialog | customDialog自身避让。 |
| 折叠屏 | 软键盘避让行为与普通场景行为一致。屏幕软键盘将根据屏幕开合状态进行调整。 |
| 软键盘托管 | 软键盘避让行为与普通场景行为一致。 |
| Web嵌套滚动 | 在嵌套滚动场景下，建议不要使用Web软键盘避让，包括RESIZE_VISUAL和RESIZE_CONTENT。 |

## 拦截系统软键盘与自定义软键盘输入

应用可以通过监听[onInterceptKeyboardAttach](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-events#oninterceptkeyboardattach12)回调，在软键盘拉起前，控制软键盘的显示，包括系统默认软键盘、带有特定Enter键的软键盘，或完全自定义软键盘。借助这一功能，开发者能够实现对软键盘的灵活管理。

- 使用系统默认软键盘
- 使用带有定制Enter键的系统软键盘
- 使用完全由应用程序自定义的软键盘

 收起自动换行深色代码主题复制

```
```

 收起自动换行深色代码主题复制

```
<!-- index.html --> <!DOCTYPE html > < html > < head > < meta charset = "utf-8" > < meta name = "viewport" content = "width=device-width,minimum-scale=1.0,maximum-scale=1.0" > </ head > < body > < p style = "font-size:12px" > input标签，原有默认行为： </ p > < input type = "text" style = "width: 300px; height: 20px" > < br > < hr style = "height:2px;border-width:0;color:gray;background-color:gray" > < p style = "font-size:12px" > input标签，系统键盘自定义enterKeyType属性 enter key UNSPECIFIED： </ p > < input type = "text" keyboard-return = "UNSPECIFIED" style = "width: 300px; height: 20px" > < br > < hr style = "height:2px;border-width:0;color:gray;background-color:gray" > < p style = "font-size:12px" > input标签，系统键盘自定义enterKeyType属性 enter key GO： </ p > < input type = "text" keyboard-return = "GO" style = "width: 300px; height: 20px" > < br > < hr style = "height:2px;border-width:0;color:gray;background-color:gray" > < p style = "font-size:12px" > input标签，系统键盘自定义enterKeyType属性 enter key SEARCH： </ p > < input type = "text" keyboard-return = "SEARCH" style = "width: 300px; height: 20px" > < br > < hr style = "height:2px;border-width:0;color:gray;background-color:gray" > < p style = "font-size:12px" > input标签，系统键盘自定义enterKeyType属性 enter key SEND： </ p > < input type = "text" keyboard-return = "SEND" style = "width: 300px; height: 20px" > < br > < hr style = "height:2px;border-width:0;color:gray;background-color:gray" > < p style = "font-size:12px" > input标签，系统键盘自定义enterKeyType属性 enter key NEXT： </ p > < input type = "text" keyboard-return = "NEXT" style = "width: 300px; height: 20px" > < br > < hr style = "height:2px;border-width:0;color:gray;background-color:gray" > < p style = "font-size:12px" > input标签，系统键盘自定义enterKeyType属性 enter key DONE： </ p > < input type = "text" keyboard-return = "DONE" style = "width: 300px; height: 20px" > < br > < hr style = "height:2px;border-width:0;color:gray;background-color:gray" > < p style = "font-size:12px" > input标签，系统键盘自定义enterKeyType属性 enter key PREVIOUS： </ p > < input type = "text" keyboard-return = "PREVIOUS" style = "width: 300px; height: 20px" > < br > < hr style = "height:2px;border-width:0;color:gray;background-color:gray" > < p style = "font-size:12px" > input标签，应用自定义键盘： </ p > < input type = "text" data-keyboard = "customKeyboard" style = "width: 300px; height: 20px" > < br > </ body > </ html >
```

ArkWeb自定义键盘的示例效果如图4、图5和图6所示。

**图4** ArkWeb自定义键盘数字键盘

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165739.26231296409258323258282868658836:50001231000000:2800:96EF6FBB42B0F5A2E163E9EEC117B03B36B7DBE114EFCC8B83634EAB21B0622B.png)

**图5** ArkWeb自定义键盘字母键盘

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165739.83732008797572155678017093194875:50001231000000:2800:17DE731A294257B07FF6C797ABC7861C78931091D4EAE20C235EB3DFE5991BFF.png)

**图6** ArkWeb自定义键盘符号键盘

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165739.02140615134011035617362490992256:50001231000000:2800:D26FABBD6155CC0AAD63000C734C57778563AA954B6161AA96639DC20D43A2CA.png)