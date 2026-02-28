# 跨设备互通（RichEditor控件）

富文本控件已经集成跨设备互通能力，通过使用富文本控件[RichEditor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-richeditor)的右键菜单即可使用跨设备互通能力。跨设备互通提供跨设备的相机、扫描、通过图库访问图片的能力，平板或2in1设备可以调用手机的相机、扫描、图库等功能。

## 场景介绍

您通过此能力实现跨设备交互，可以使用其他设备的相机、扫描和图库功能。

## 约束与限制

需同时满足以下条件，才能使用该功能：

- **设备限制**

  - 本端设备：HarmonyOS版本为HarmonyOS NEXT及以上的平板或2in1设备。
  - 远端设备：HarmonyOS版本为HarmonyOS NEXT及以上、具有相机能力的手机或平板设备。
- **使用限制**

  - 双端设备需要登录同一华为账号。
  - 跨设备互通API支持根据特定调用策略调用设备。调用策略：2in1设备可以调用平板和手机，平板可以调用手机，同类型设备不可调用。
  - 双端设备需要打开WLAN和蓝牙开关。

条件允许时，建议双端设备接入同一个局域网，可提升唤醒相机的速度。

## 开发步骤

- 添加[RichEditor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-richeditor)富文本组件，即可在富文本组件中右键中选择其他设备进行导入，通过onWillChange属性对回传的照片进行处理。收起自动换行深色代码主题复制

```
@ Entry @ Component struct Index { controller : RichEditorController = new RichEditorController () options : RichEditorOptions = { controller : this . controller } build () { Column () { Column () { RichEditor ( this . options ) . onWillChange (( value : RichEditorChangeValue ) => { if ( value ?. replacedImageSpans [ 0 ]?. imageStyle ?. objectFit != 0 ) { return true ; } for ( let item of value . replacedImageSpans ) { this . controller . addImageSpan ( item . valuePixelMap , { imageStyle : { size : [ "500px" , "500px" ], layoutStyle : { borderRadius : '10px' , } } }) } return false ; }) . borderWidth ( 1 ) . borderColor ( Color . Green ) . width ( "100%" ) . height ( "100%" ) } . borderWidth ( 1 ) . borderColor ( Color . Red ) . width ( "100%" ) . height ( "70%" ) } } }
```

使用流程如下：

1.在富文本区域右键。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170029.36288646941852125055553881053365:50001231000000:2800:45F13AF3B9105CBD0095A3B92A6C2F32FF567227AF69B1ACEAB0FC7F0E09A1C7.png)

2.选择想要使用的能力。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170029.19781670499550374822439321216409:50001231000000:2800:3CA3ECAA3E29A0B42BA4B9BE768565B4220F4A34D47EE0A0D71AB19E9F73E8E8.png)

3.等待对端设备拍照回传。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170029.24900406108699563983799377680734:50001231000000:2800:E2459C7A77EE23AD9D55A62326D845A5244F79BB2D31C58B746117ACCE4B2ED3.png)

4.图片回传后

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170030.57812854244794881596779741188070:50001231000000:2800:867AC0BFC80681CE292A816F5246913574EB4296E0A23A4F1D0EF473521A20F7.png)

## 关闭富文本跨设备互通能力

如果需要关闭富文本右键菜单跨设备互通能力，可通过editMenuOptions属性自定义菜单内容去除跨设备互通菜单项即可规避，示例如下：

 收起自动换行深色代码主题复制

```
@Entry @Component struct Index { controller: RichEditorController = new RichEditorController() options: RichEditorOptions = { controller: this.controller } build () { Column () { Column () { RichEditor (this.options) .editMenuOptions ({ onCreateMenu: (menuItems: Array<TextMenuItem>) => { if (menuItems.length === 0) { return menuItems; } let newMenuItems : TextMenuItem[] = []; menuItems. forEach ((item, index) => { if (!item.id. equals (TextMenuItemId.COLLABORATION_SERVICE)) { newMenuItems. push (item); } }) return newMenuItems; }, onMenuItemClick : ( menuItem : TextMenuItem, textRange : TextRange) => { return false ; } }) .borderWidth ( 1 ) .borderColor (Color.Green) .width ( "100%" ) .height ( "100%" ) } .borderWidth ( 1 ) .borderColor (Color.Red) .width ( "100%" ) .height ( "70%" ) } } }
```