# 切换按钮 (Toggle)

Toggle组件提供状态按钮样式、勾选框样式和开关样式，一般用于两种状态之间的切换。具体用法请参考[Toggle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-toggle)。

## 创建切换按钮

Toggle通过调用[ToggleOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-toggle#toggleoptions18对象说明)来创建，具体调用形式如下：

 收起自动换行深色代码主题复制

```
Toggle ( options : { type : ToggleType , isOn?: boolean })
```

其中，ToggleType为开关类型，包括Button、Checkbox和Switch，isOn为切换按钮的状态。

API version 11开始，Checkbox默认样式由圆角方形变为圆形。

接口调用有以下两种形式：

- 创建不包含子组件的Toggle。

当ToggleType为Checkbox或者Switch时，用于创建不包含子组件的Toggle：

 收起自动换行深色代码主题复制

```
Toggle ({ type : ToggleType . Checkbox , isOn : false }). id ( 'toggle1' ) // 请开发者替换为实际的id Toggle ({ type : ToggleType . Checkbox , isOn : true }). id ( 'toggle2' ) // 请开发者替换为实际的id
```

[CreateToggle.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/ChooseComponent/entry/src/main/ets/pages/toggle/CreateToggle.ets#L30-L33) 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165852.03036572481476435295207891570418:50001231000000:2800:EFB1FDEECDE22A54B848ACA5112AFAC75BED0FA53B271EB267A2C6345919046A.png)

 收起自动换行深色代码主题复制

```
Toggle ({ type : ToggleType . Switch , isOn : false }). id ( 'toggle3' ) // 请开发者替换为实际的id Toggle ({ type : ToggleType . Switch , isOn : true }). id ( 'toggle4' ) // 请开发者替换为实际的id
```

[CreateToggle.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/ChooseComponent/entry/src/main/ets/pages/toggle/CreateToggle.ets#L39-L42) 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165853.09594810193624295906541534767799:50001231000000:2800:7E972EAF1A9AF837B382A3C83790EBEC88C269D4358612B72BA43EAE48F2480D.png)
- 创建包含子组件的Toggle。

当ToggleType为Button时，只能包含一个子组件，如果子组件有文本设置，则相应的文本内容会显示在按钮上。

 收起自动换行深色代码主题复制

```
Toggle ({ type : ToggleType . Button , isOn : false }) { Text ( 'status button' ) . fontColor ( '#182431' ) . fontSize ( 12 ) }. width ( 100 ). id ( 'toggle5' ) // 请开发者替换为实际的id Toggle ({ type : ToggleType . Button , isOn : true }) { Text ( 'status button' ) . fontColor ( '#182431' ) . fontSize ( 12 ) }. width ( 100 ). id ( 'toggle6' ) // 请开发者替换为实际的id
```

[CreateToggle.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/ChooseComponent/entry/src/main/ets/pages/toggle/CreateToggle.ets#L61-L73) 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165853.88394930927581017436569451486538:50001231000000:2800:81E8EE813752B5063A7A837A1E45A1963794427E7916350589DC88E3D2927373.png)

## 自定义样式

- 通过selectedColor属性设置Toggle打开选中后的背景颜色。

 收起自动换行深色代码主题复制

```
Toggle ({ type : ToggleType . Button , isOn : true }) { Text ( 'status button' ) . fontColor ( '#182431' ) . fontSize ( 12 ) }. width ( 100 ) . selectedColor ( Color . Pink ) // ··· Toggle ({ type : ToggleType . Checkbox , isOn : true }) . selectedColor ( Color . Pink ) // ··· Toggle ({ type : ToggleType . Switch , isOn : true }) . selectedColor ( Color . Pink ) // ···
```

[ToggleCustomStyle.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/ChooseComponent/entry/src/main/ets/pages/toggle/ToggleCustomStyle.ets#L31-L52) 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165853.30988393565902454729464095137354:50001231000000:2800:A4A75FAF4E24B218767A958197AE73AB2CF531DB29227F522605B2B9A8D5EEE7.png)
- 通过switchPointColor属性设置Switch类型的圆形滑块颜色，仅对type为ToggleType.Switch生效。

 收起自动换行深色代码主题复制

```
Toggle ({ type : ToggleType . Switch , isOn : false }) . switchPointColor ( Color . Pink ) // ··· Toggle ({ type : ToggleType . Switch , isOn : true }) . switchPointColor ( Color . Pink ) // ···
```

[ToggleCustomStyle.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/ChooseComponent/entry/src/main/ets/pages/toggle/ToggleCustomStyle.ets#L60-L71) 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165853.28543557180565651695867746876729:50001231000000:2800:622263CCD2C5EF73178C94D30088004CF2B88A5AF19B76E91C0FD2EF4587CF95.png)

## 添加事件

除支持[通用事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-component-general-events)外，Toggle还用于选中和取消选中后触发某些操作，可以绑定onChange事件来响应操作后的自定义行为。

 收起自动换行深色代码主题复制

```
Toggle ({ type : ToggleType . Switch , isOn : false }) . onChange ( ( isOn: boolean ) => { if (isOn) { // 需要执行的操作 // ··· } })
```

[CreateToggle.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/ChooseComponent/entry/src/main/ets/pages/toggle/CreateToggle.ets#L44-L54)   

## 场景示例

Toggle用于切换蓝牙开关状态。

 收起自动换行深色代码主题复制

```
// xxx.ets import { promptAction } from '@kit.ArkUI' ; @Entry @Component export struct ToggleSample { @State message : string = 'off' ; pathStack : NavPathStack = new NavPathStack (); build ( ) { // ··· Column ({ space : 8 }) { Column ({ space : 8 }) { Text ( 'Bluetooth Mode: ' + this . message ) . id ( 'message' ) Row () { Text ( 'Bluetooth' ) Blank () Toggle ({ type : ToggleType . Switch }) . id ( 'toggle' ) // 请开发者替换为实际的id . onChange ( ( isOn: boolean ) => { if (isOn) { this . message = 'on' ; promptAction. openToast ({ 'message' : 'Bluetooth is on.' }); } else { this . message = 'off' ; promptAction. openToast ({ 'message' : 'Bluetooth is off.' }); } }) }. width ( '100%' ) } . alignItems ( HorizontalAlign . Start ) . backgroundColor ( '#fff' ) . borderRadius ( 12 ) . padding ( 12 ) . width ( '100%' ) } . width ( '100%' ) . height ( '100%' ) . padding ({ left : 12 , right : 12 }) // ··· . backgroundColor ( '#f1f2f3' ) // 请将$r('app.string.ToggleCaseExample_title')替换为实际资源文件，在本示例中该资源文件的value值为"toggle蓝牙示例" . title ($r( 'app.string.ToggleCaseExample_title' )) } }
```

[ToggleCaseExample.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/ChooseComponent/entry/src/main/ets/pages/toggle/ToggleCaseExample.ets#L16-L69) 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165853.90935183603712078316420059633060:50001231000000:2800:AFFE1C5E3973467942D791ED3A5E815DF7CEF858752C5B583C3DCA675429E569.gif)