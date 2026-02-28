# search开发指导

提供搜索框组件，用于提供用户搜索内容的输入区域，具体用法请参考[search](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-basic-search)。

## 创建search组件

在pages/index目录下的hml文件中创建一个search组件。

 收起自动换行深色代码主题复制

```
<!-- xxx.hml--> < div class = "container" > < search > </ search > </ div >
```

 收起自动换行深色代码主题复制

```
/* xxx.css */ .container { width : 100% ; height : 100% ; flex-direction : column; align-items : center; justify-content : center; background-color : #F1F3F5 ; }
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170000.22496254478899997717171616223011:50001231000000:2800:9C6A7536254988B510855F1D857D9E8FB90C674A79D0057439E395E10CB363FD.png)

## 设置属性

通过设置hint、icon和searchbutton属性设置搜索框的提示文字、图标和末尾搜索按钮的内容。

 收起自动换行深色代码主题复制

```
<!-- xxx.hml--> < div class = "container" > < search hint = "Please enter the search content" searchbutton = "search" icon = "/common/search1.png" > </ search > </ div >
```

 收起自动换行深色代码主题复制

```
/* xxx.css */ .container { width : 100% ; height : 100% ; flex-direction : column; align-items : center; justify-content : center; background-color : #F1F3F5 ; }
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170001.29796034631956260644815118963924:50001231000000:2800:2203E4C791C67156D7EFEB28F5875CA26D6191F1B77FEC01C212E7DD36535814.png)

## 添加样式

通过color、placeholder-color和caret-color样式来设置搜索框的文本颜色、提示文本颜色和光标颜色。

 收起自动换行深色代码主题复制

```
<!-- xxx.hml--> < div class = "container" > < search hint = "Please enter the search content" searchbutton = "search" > </ search > </ div >
```

 收起自动换行深色代码主题复制

```
/* xxx.css */ .container { width : 100% ; height : 100% ; flex-direction : column; align-items : center; justify-content : center; background-color : #F1F3F5 ; } search{ color : black; placeholder- color : black; caret-color : red; }
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170001.52486166350430156731923300039265:50001231000000:2800:33D6FCEE43745E3F064AA3E63D986062E3C574862D3B924D98F6717592878DF9.gif)

## 绑定事件

向search组件添加change、search、submit、share和translate事件，对输入信息进行操作。

 收起自动换行深色代码主题复制

```
<!-- xxx.hml--> < div class = "container" > < text style = "margin-left: -7px;" > < span > Enter text and then touch and hold what you've entered </ span > </ text > < search hint = "Please enter the search content" searchbutton = "search" onsearch = "search" onchange = "change" ontranslate = "translate" onshare = "share" onsubmit = "submit" > </ search > </ div >
```

 收起自动换行深色代码主题复制

```
/* xxx.css */ .container { width : 100% ; height : 100% ; flex-direction : column; align-items : center; justify-content : center; background-color : #F1F3F5 ; } text{ width : 100% ; font-size : 25px ; text-align : center; margin-bottom : 100px ; }
```

 收起自动换行深色代码主题复制

```
// index.js import promptAction from '@ohos.promptAction' ; export default { search ( e ){ promptAction. showToast ({ message : e. value , duration : 3000 , }); }, translate ( e ){ promptAction. showToast ({ message :  e. value , duration : 3000 , }); }, share ( e ){ promptAction. showToast ({ message :  e. value , duration : 3000 , }); }, change ( e ){ promptAction. showToast ({ message :  e. value , duration : 3000 , }); }, submit ( e ){ promptAction. showToast ({ message : 'submit' , duration : 3000 , }); } }
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170001.92510264891929660084510079025841:50001231000000:2800:C013B3735636B35A2D77DCD08316BC2CD93090BC3C2BD78F7192FB731D5818B0.gif)

## 场景示例

在本场景中通过下拉菜单选择search、Textarea和Input组件来实现搜索和输入效果。

 收起自动换行深色代码主题复制

```
<!-- xxx.hml--> < div style = "flex-direction: column;align-items: center;justify-content: center; width: 100%;" > < select class = "slt1" id = "slt1" onchange = "setfield" > < option value = "search" > search </ option > < option value = "textarea" > Textarea </ option > < option value = "input" > Input </ option > </ select > < div if = "{{showsearch}}" style = "flex-direction: column;align-items: center;margin-top: 50px;height: 400px;justify-content: space-around;" > < search class = "field" id = "search1" hint = "search1" onsubmit = "submit" onchange = "change" > </ search > < search class = "field" id = "search2" icon = "common/search1.png" hint = "search2" show = "{{showsec}}" onsubmit = "submit" onchange = "change" > </ search > </ div > < div if = "{{showtextarea}}" style = "flex-direction: column;align-items: center;margin-top: 50px;height: 400px;justify-content: space-around;" > < textarea class = "field" id = "textarea1" extend = "true" placeholder = "textarea1" onchange = "change" > </ textarea > < textarea class = "field" id = "textarea2" extend = "true" placeholder = "textarea2" onchange = "change" show = "{{showsec}}" > </ textarea > </ div > < div if = "{{showinput}}" style = "flex-direction: column;align-items: center;margin-top: 50px;height: 400px;justify-content: space-around;" > < input type = "text" class = "field" id = "input1" placeholder = "input1" onchange = "change" > </ input > < input type = "text" class = "field" id = "input2" placeholder = "input2" onchange = "change" show = "{{showsec}}" > </ input > </ div > </ div >
```

 收起自动换行深色代码主题复制

```
/* xxx.css */ .field { width : 80% ; color : mediumaquamarine; font-weight : 600 ; placeholder- color : orangered; } .slt1 { font-size : 50px ; position : absolute; left : 50px ; top : 50px ; }
```

 收起自动换行深色代码主题复制

```
// index.js import promptAction from '@ohos.promptAction' ; export default { data : { showsearch : true , showtextarea : false , showinput : false , showsec : true , }, setfield ( e ) { this . field = e. newValue if (e. newValue == 'search' ) { this . showsearch = true this . showtextarea = false this . showinput = false } else if (e. newValue == 'textarea' ) { this . showsearch = false this . showtextarea = true this . showinput = false } else { this . showsearch = false this . showtextarea = false this . showinput = true } }, submit ( e ) { promptAction. showToast ({ message : '搜索！' , duration : 2000 }) }, change ( e ) { promptAction. showToast ({ message : '内容:' + e. text , duration : 2000 }) } }
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170001.43231433768774532226490595681081:50001231000000:2800:F09644F1E8B764B0241D3E3C7E792AA17036C617C3FF07F0CF9E5DEC8DBFE1F9.gif)