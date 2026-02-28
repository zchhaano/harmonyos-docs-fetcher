# 单选框 (Radio)

Radio是单选框组件，通常用于提供相应的用户交互选择项，同一组的Radio中只有一个可以被选中。具体用法请参考[Radio](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-radio)。

## 创建单选框

Radio通过调用[RadioOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-radio#radiooptions对象说明)来创建，以RadioOptions中的value和group为例：

 收起自动换行深色代码主题复制

```
Radio ( options : { value : string , group : string })
```

其中，value是单选框的名称，group是单选框的所属群组名称。checked属性可以设置单选框的状态，状态分别为false和true，设置为true时表示单选框被选中。

Radio支持设置选中状态和非选中状态的样式。

 收起自动换行深色代码主题复制

```
Radio ({ value : 'Radio1' , group : 'radioGroup' }) . checked ( false ) Radio ({ value : 'Radio2' , group : 'radioGroup' }) . checked ( true )
```

[RadioButton.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/ChooseComponent/entry/src/main/ets/pages/radio/RadioButton.ets#L34-L39) 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165846.70321673011454204316252963576800:50001231000000:2800:F78589DB4FC57F243EACB26891F405EB63202019B249469F360F33E380919CCB.png)

## 添加事件

除支持[通用事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-component-general-events)外，Radio还用于选中后触发某些操作，可以绑定onChange事件来响应选中操作后的自定义行为。

 收起自动换行深色代码主题复制

```
Radio ({ value : 'Radio1' , group : 'radioGroup' }) . onChange ( ( isChecked: boolean ) => { if (isChecked) { //需要执行的操作 // ··· } }) Radio ({ value : 'Radio2' , group : 'radioGroup' }) . onChange ( ( isChecked: boolean ) => { if (isChecked) { //需要执行的操作 // ··· } })
```

[RadioButton.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/ChooseComponent/entry/src/main/ets/pages/radio/RadioButton.ets#L47-L66)   

## 场景示例

通过点击Radio切换声音模式。

 收起自动换行深色代码主题复制

```
// xxx.ets import { promptAction } from '@kit.ArkUI' ; @Entry @Component export struct RadioExample { @State rst : promptAction. ShowToastOptions = { 'message' : 'Ringing mode.' }; @State vst : promptAction. ShowToastOptions = { 'message' : 'Vibration mode.' }; @State sst : promptAction. ShowToastOptions = { 'message' : 'Silent mode.' }; build ( ) { // ··· Row () { Column () { Radio ({ value : 'Ringing' , group : 'radioGroup' }). checked ( true ) . height ( 50 ) . width ( 50 ) . onChange ( ( isChecked: boolean ) => { if (isChecked) { // 切换为响铃模式 this . getUIContext (). getPromptAction (). openToast ( this . rst ); } }) Text ( 'Ringing' ) } Column () { Radio ({ value : 'Vibration' , group : 'radioGroup' }) . height ( 50 ) . width ( 50 ) . onChange ( ( isChecked: boolean ) => { if (isChecked) { // 切换为振动模式 this . getUIContext (). getPromptAction (). openToast ( this . vst ); } }) Text ( 'Vibration' ) } Column () { Radio ({ value : 'Silent' , group : 'radioGroup' }) . height ( 50 ) . width ( 50 ) . onChange ( ( isChecked: boolean ) => { if (isChecked) { // 切换为静音模式 this . getUIContext (). getPromptAction (). openToast ( this . sst ); } }) Text ( 'Silent' ) } }. height ( '100%' ). width ( '100%' ). justifyContent ( FlexAlign . Center ) // ··· } }
```

[RadioSample.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20251117/ArkUISample/ChooseComponent/entry/src/main/ets/pages/radio/RadioSample.ets#L16-L76) 

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165846.93551344471975701920329433556102:50001231000000:2800:22FD1146D3DFA8F353E5EB4266F622E30E872C62EA78DD1DAC87378CC91C7651.gif)