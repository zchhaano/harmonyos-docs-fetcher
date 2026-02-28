# form开发指导

form是一个表单容器，支持容器内[Input](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-basic-input)组件内容的提交和重置。具体用法请参考[form API](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-container-form)。

## 创建form组件

在pages/index目录下的hml文件中创建一个form组件。

 收起自动换行深色代码主题复制

```
<!-- xxx.hml --> < div class = "container" > < form style = "width: 100%; height: 20%" > < input type = "text" style = "width:80%" > </ input > </ form > </ div >
```

 收起自动换行深色代码主题复制

```
/* xxx.css */ .container { width : 100% ; height : 100% ; flex-direction : column; justify-content : center; align-items : center; background-color : #F1F3F5 ; }
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165936.40096144532581359758984553240690:50001231000000:2800:B083111BDE1E55999E39D1876D84C66352CC480A6DAF76550E34F17BFA53460D.png)

## 实现表单缩放

为form组件添加click-effect属性，实现点击表单后的缩放效果，click-effect枚举值请参考[通用属性](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-common-attributes)。

 收起自动换行深色代码主题复制

```
<!-- xxx.hml --> < div class = "container" > < form id = "formId" class = "formClass" click-effect = "spring-large" > < input type = "text" > </ input > </ form > </ div >
```

## 设置form样式

通过为form添加background-color和border属性，来设置表单的背景颜色和边框。

 收起自动换行深色代码主题复制

```
/* xxx.css */ .container { width : 100% ; height : 100% ; flex-direction : column; align-items : center; justify-content : center; background-color : #F1F3F5 ; } .formClass { width : 80% ; height : 100px ; padding : 10px ; border : 1px solid #cccccc ; }
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165936.31133417652634328150543347076921:50001231000000:2800:8756AF7026B49A8AFB3D038B7AA0A958E8DF10EC6089B59E22B61672C3EF42BF.gif)

## 添加响应事件

为form组件添加submit和reset事件，来提交表单内容或重置表单选项。

 收起自动换行深色代码主题复制

```
<!-- xxx.hml --> < div class = "container" > < form onsubmit = 'onSubmit' onreset = 'onReset' class = "form" > < div style = "width: 100%;justify-content: center;" > < label > Option 1 </ label > < input type = 'radio' name = 'radioGroup' value = 'radio1' > </ input > < label > Option 2 </ label > < input type = 'radio' name = 'radioGroup' value = 'radio2' > </ input > </ div > < div style = "width: 100%;justify-content: center; margin-top: 20px" > < input type = "submit" value = "Submit" style = "width:120px; margin-right:20px;" > </ input > < input type = "reset" value = "Reset" style = "width:120px;" > </ input > </ div > </ form > </ div >
```

 收起自动换行深色代码主题复制

```
/* index.css */ .container { width : 100% ; height : 100% ; flex-direction : column; justify-items: center; align-items : center; background-color : #F1F3F5 ; } .form { width : 100% ; height : 30% ; margin-top : 40% ; flex-direction : column; justify-items: center; align-items : center; }
```

 收起自动换行深色代码主题复制

```
// xxx.js import promptAction from '@ohos.promptAction' ; export default { onSubmit ( result ) { promptAction. showToast ({ message : result. value . radioGroup }) }, onReset ( ) { promptAction. showToast ({ message : 'Reset All' }) } }
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165936.54120309314072555452152108706098:50001231000000:2800:8B819CA445C0CB3D5D8B640E293B74FAB6AF09CDB924F4960807709F9DF5A593.gif)

## 场景示例

在本场景中，开发者可以选择相应选项并提交或重置数据。

创建[Input](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-basic-input)组件，分别设置type属性为checkbox（多选框）和radio（单选框），再使用form组件的onsubmit和onreset事件实现表单数据的提交与重置。

 收起自动换行深色代码主题复制

```
<!-- xxx.hml --> < div class = "container" > < form onsubmit = "formSubmit" onreset = "formReset" > < text style = "font-size: 30px; margin-bottom: 20px; margin-top: 100px;" > < span > Form </ span > </ text > < div style = "flex-direction: column;width: 90%;padding: 30px 0px;" > < text class = "txt" > Select 1 or more options </ text > < div style = "width: 90%;height: 150px;align-items: center;justify-content: space-around;" > < label target = "checkbox1" > Option 1 </ label > < input id = "checkbox1" type = "checkbox" name = "checkbox1" > </ input > < label target = "checkbox2" > Option 2 </ label > < input id = "checkbox2" type = "checkbox" name = "checkbox2" > </ input > </ div > < divider style = "margin: 20px 0px;color: pink;height: 5px;" > </ divider > < text class = "txt" > Select 1 option </ text > < div style = "width: 90%;height: 150px;align-items: center;justify-content: space-around;" > < label target = "radio1" > Option 1 </ label > < input id = "radio1" type = "radio" name = "myradio" > </ input > < label target = "radio2" > Option 2 </ label > < input id = "radio2" type = "radio" name = "myradio" > </ input > </ div > < divider style = "margin: 20px 0px;color: pink;height: 5px;" > </ divider > < text class = "txt" > Text box </ text > < input type = "text" placeholder = "Enter content." style = "margin-top: 50px;" > </ input > < div style = "width: 90%;align-items: center;justify-content: space-between;margin: 40px;" > < input type = "submit" > Submit </ input > < input type = "reset" > Reset </ input > </ div > </ div > </ form > </ div >
```

 收起自动换行深色代码主题复制

```
/* index.css */ .container { width : 100% ; height : 100% ; flex-direction :column; align-items :center; background-color : #F1F3F5 ; } .txt { font-size : 33px ; font-weight :bold; color :darkgray; } label { font-size : 20px ; }
```

 收起自动换行深色代码主题复制

```
// xxx.js import promptAction from '@ohos.promptAction' ; export default { formSubmit ( ) { promptAction. showToast ({ message : 'Submitted.' }) }, formReset ( ) { promptAction. showToast ({ message : 'Reset.' }) } }
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165936.93450706236411975146336185624573:50001231000000:2800:9360367C5E55C3DED103612497558BDAD7E9F538ADE708C14CFC4B60C9E19686.gif)