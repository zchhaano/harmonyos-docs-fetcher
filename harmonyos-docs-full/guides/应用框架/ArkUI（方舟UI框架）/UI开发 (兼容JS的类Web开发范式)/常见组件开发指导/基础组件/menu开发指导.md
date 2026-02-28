# menu开发指导

提供菜单组件，作为临时性弹出窗口，用于展示用户可执行的操作，具体用法请参考[menu](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-basic-menu)。

## 创建menu组件

在pages/index目录下的hml文件中创建一个menu组件，添加target、type、title属性。

 收起自动换行深色代码主题复制

```
<!-- xxx.hml--> < div class = "container" > < text class = "title-text" id = "textId" > show menu </ text > < menu target = "textId" type = "click" title = "title" > < option value = "Item 1" > Item 1 </ option > < option value = "Item 2" > Item 2 </ option > < option value = "Item 3" > Item 3 </ option > </ menu > </ div >
```

 收起自动换行深色代码主题复制

```
/* xxx.css */ .container { width : 100% ; height : 100% ; flex-direction : column; background-color : #F1F3F5 ; align-items : center; justify-content : center; width : 100% ; } .title-text { font-size : 35px ; }
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165959.03684139372411799998689680412218:50001231000000:2800:392458EC2E6D768FEF65A56C533FF25CB2228B35B51235FBEDADADEEFE9BBBD0.png)

 说明 

- menu仅支持[option](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-basic-option)子组件。
- menu组件不支持focusable、disabled属性。

## 设置样式

为menu组件设置样式，例如字体颜色、大小、字符间距等。

 收起自动换行深色代码主题复制

```
<!-- xxx.hml--> < div class = "container" > < text class = "title-text" id = "textId" > show menu </ text > < menu target = "textId" type = "click" title = "title" > < option value = "Item 1" > Item 1 </ option > < option value = "Item 2" > Item 2 </ option > < option value = "Item 3" > Item 3 </ option > </ menu > </ div >
```

 收起自动换行深色代码主题复制

```
/* xxx.css */ .container { width : 100% ; height : 100% ; flex-direction : column; background-color : #F1F3F5 ; align-items : center; justify-content : center; width : 100% ; } .title-text { font-size : 35px ; background-color : #5a5aee ; color : white; width : 70% ; text-align : center; height : 85px ; border-radius : 12px ; } .menu { text- color : blue; font-size : 35px ; letter-spacing : 2px ; } option{ color : #6a6aef ; font-size : 30px ; }
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165959.87585029300382362535552978675569:50001231000000:2800:88EAC9B8AAFA838A6E400D4EDE556F3CE450CEB6FBA9446571CB2CEAD8D649B7.png)

## 绑定事件

为menu组件绑定oncancel事件（取消操作时触发）。

 收起自动换行深色代码主题复制

```
<!-- xxx.hml--> < div class = "container" > < text class = "title-text" id = "textId" onclick = "textClick" > show menu </ text > < menu title = "title" oncancel = "cancel" id = "menuId" > < option value = "Item 1" > Item 1 </ option > < option value = "Item 2" > Item 2 </ option > < option value = "Item 3" > Item 3 </ option > </ menu > </ div >
```

 收起自动换行深色代码主题复制

```
/* xxx.css */ .container { width : 100% ; height : 100% ; flex-direction : column; background-color : #F1F3F5 ; width : 100% ; } .title-text { font-size : 35px ; background-color : #5a5aee ; color : white; width : 70% ; text-align : center; height : 85px ; border-radius : 12px ; margin-top : 500px ; margin-left : 15% ; } menu { text- color : blue; font-size : 35px ; letter-spacing : 2px ; } option{ color : #6a6aef ; font-size : 30px ; }
```

 收起自动换行深色代码主题复制

```
// xxx.js import promptAction from '@ohos.promptAction' ; export default { cancel ( ) { promptAction. showToast ({ message : "cancel" }) }, textClick ( ) { this .$element( "menuId" ). show ({ x : 175 , y : 590 }); } }
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170000.44385650369899860510269919706439:50001231000000:2800:22BD9496AEC1CBA3793A4114A5EA7FFF01A6BAC98225F40ACFE3EFB08A47B80D.gif)