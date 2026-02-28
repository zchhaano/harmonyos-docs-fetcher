# input开发指导

input是交互式组件，用于接收用户数据。其类型可设置为日期、多选框和按钮等。具体用法请参考[input API](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-basic-input)。

## 创建input组件

在pages/index目录下的hml文件中创建一个input组件。

 收起自动换行深色代码主题复制

```
<!-- xxx.hml --> < div class = "container" > < input type = "text" > Please enter the content </ input > </ div >
```

 收起自动换行深色代码主题复制

```
/* xxx.css */ .container { width : 100% ; height : 100% ; flex-direction : column; justify-content : center; align-items : center; background-color : #F1F3F5 ; }
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165924.74914061568928737430027547473309:50001231000000:2800:9E7666AF8D74D116B941C47DAB51DF2003C375314A377EC71BD780E000E81FE8.png)

## 设置input类型

通过设置type属性来定义input类型，如将input设置为button、date等。

 收起自动换行深色代码主题复制

```
<!-- xxx.hml --> < div class = "container" > < div class = "div-button" > < dialog class = "dialogClass" id = "dialogId" > < div class = "content" > < text > this is a dialog </ text > </ div > </ dialog > < input class = "button" type = "button" value = "click" onclick = "btnclick" > </ input > </ div > < div class = "content" > < input onchange = "checkboxOnChange" checked = "true" type = "checkbox" > </ input > </ div > < div class = "content" > < input type = "date" class = "flex" placeholder = "Enter date" > </ input > </ div > </ div >
```

 收起自动换行深色代码主题复制

```
/* xxx.css */ .container { width : 100% ; height : 100% ; align-items : center; flex-direction : column; justify-content : center; background-color : #F1F3F5 ; } .div-button { flex-direction : column; align-items : center; } .dialogClass { width : 80% ; height : 200px ; } .button { margin-top : 30px ; width : 50% ; } .content { width : 90% ; height : 150px ; align-items : center; justify-content : center; } .flex { width : 80% ; margin-bottom : 40px ; }
```

 收起自动换行深色代码主题复制

```
// xxx.js export default { btnclick ( ){ this .$element( 'dialogId' ). show () }, }
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165924.60371057900863347017577035997994:50001231000000:2800:9FA1DC65D4961B14C26336DA36635C64E472CFC78927C654273A693516FA2F87.gif)

 说明 

仅当input类型为checkbox和radio时，当前组件选中的属性是checked才生效，默认值为false。

## 事件绑定

向input组件添加translate事件。

 收起自动换行深色代码主题复制

```
<!-- xxx.hml --> < div class = "content" > < text style = "margin-left: -7px;" > < span > Enter text and then touch and hold what you've entered </ span > </ text > < input class = "input" type = "text" ontranslate = "translate" placeholder = "translate" > </ input > </ div >
```

 收起自动换行深色代码主题复制

```
/* xxx.css */ .content { width : 100% ; height : 100% ; flex-direction : column; align-items : center; justify-content : center; background-color : #F1F3F5 ; } .input { margin-top : 50px ; width : 60% ; placeholder- color : gray; } text{ width : 100% ; font-size : 25px ; text-align :center; }
```

 收起自动换行深色代码主题复制

```
// xxx.js import promptAction from '@ohos.promptAction' export default { translate ( e ) { promptAction. showToast ({ message : e. value , duration : 3000 , }); } }
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165924.49781091698254397022787928093048:50001231000000:2800:9C5E10C0601B1A8602F22AE8DBCD128677FA4C110AD4D7343AF07FA8AD7050FB.gif)

## 设置输入提示

通过对input组件添加showError方法来提示输入的错误原因。

 收起自动换行深色代码主题复制

```
<!-- xxx.hml --> < div class = "content" > < input id = "input" class = "input" type = "text" maxlength = "20" placeholder = "Please input text" onchange = "change" > </ input > < input class = "button" type = "button" value = "Submit" onclick = "buttonClick" > </ input > </ div >
```

 收起自动换行深色代码主题复制

```
/* xxx.css */ .content { width : 100% ; height : 100% ; flex-direction : column; align-items : center; justify-content : center; background-color : #F1F3F5 ; } .input { width : 80% ; placeholder- color : gray; } .button { width : 30% ; margin-top : 50px ; }
```

 收起自动换行深色代码主题复制

```
// xxx.js import promptAction from '@ohos.promptAction' export default { data :{ value : '' , }, change ( e ){ this . value = e. value ; promptAction. showToast ({ message : "value: " + this . value , duration : 3000 , }); }, buttonClick ( e ){ if ( this . value . length > 6 ){ this .$element( "input" ). showError ({ error : 'Up to 6 characters are allowed.' }); } else if ( this . value . length == 0 ){ this .$element( "input" ). showError ({ error : this . value + 'This field cannot be left empty.' }); } else { promptAction. showToast ({ message : "success " }); } }, }
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165924.03668384693737982681561708411398:50001231000000:2800:25158A7FF039D2BCA073875A519C5573C6487F43BBF87D841632277DA015182F.gif)

 说明 

该方法在input类型为text、email、date、time、number和password时生效。

## 场景示例

根据场景选择不同类型的input输入框，完成信息录入。

 收起自动换行深色代码主题复制

```
<!-- xxx.hml --> < div class = "container" > < div class = "label-item" > < label > memorandum </ label > </ div > < div class = "label-item" > < label class = "lab" target = "input1" > content: </ label > < input class = "flex" id = "input1" placeholder = "Enter content" /> </ div > < div class = "label-item" > < label class = "lab" target = "input3" > date: </ label > < input class = "flex" id = "input3" type = "date" placeholder = "Enter date" /> </ div > < div class = "label-item" > < label class = "lab" target = "input4" > time: </ label > < input class = "flex" id = "input4" type = "time" placeholder = "Enter time" /> </ div > < div class = "label-item" > < label class = "lab" target = "checkbox1" > Complete: </ label > < input class = "flex" type = "checkbox" id = "checkbox1" style = "width: 100px;height: 100px;" /> </ div > < div class = "label-item" > < input class = "flex" type = "button" id = "button" value = "save" onclick = "btnclick" /> </ div > </ div >
```

 收起自动换行深色代码主题复制

```
/* xxx.css */ .container { flex-direction : column; background-color : #F1F3F5 ; } .label-item { align-items : center; border-bottom-width : 1px ; border-color : #dddddd ; } .lab { width : 400px ;} label { padding : 30px ; font-size : 30px ; width : 320px ; font-family : serif; color : #9370d8 ; font-weight : bold; } .flex { flex : 1 ; } .textareaPadding { padding-left : 100px ; }
```

 收起自动换行深色代码主题复制

```
// xxx.js import promptAction from '@ohos.promptAction' ; export default { data : { }, onInit ( ) { }, btnclick ( e ) { promptAction. showToast ({ message : 'Saved successfully!' }) } }
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165924.81154095559843839371213985411450:50001231000000:2800:DD0A8244F1C9A02571990EE1C8CB6D336DB28B38F081DA336A04EA1CA462F4BD.gif)