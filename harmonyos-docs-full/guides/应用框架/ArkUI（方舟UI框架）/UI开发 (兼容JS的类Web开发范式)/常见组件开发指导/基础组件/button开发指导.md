# button开发指导

button是按钮组件，其类型包括胶囊按钮、圆形按钮、文本按钮、弧形按钮、下载按钮。具体用法请参考[button API](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-basic-button)。

## 创建button组件

在pages/index目录下的hml文件中创建一个button组件。

 收起自动换行深色代码主题复制

```
<!-- xxx.hml --> < div class = "container" > < button type = "capsule" value = "Capsule button" > </ button > </ div >
```

 收起自动换行深色代码主题复制

```
/* xxx.css */ .container { width : 100% ; height : 100% ; flex-direction : column; justify-content : center; align-items : center; background-color : #F1F3F5 ; }
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165937.06157456288073569722477395952795:50001231000000:2800:DC01255B0F18ECE0114CB37CB72F3EC6C101D952C901570495B3E041743ADE4A.png)

## 设置button类型

通过设置button的type属性来选择按钮类型，如定义button为圆形按钮、文本按钮等。

 收起自动换行深色代码主题复制

```
<!-- xxx.hml --> < div class = "container" > < button class = "circle" type = "circle" > + </ button > < button class = "text" type = "text" > button </ button > </ div >
```

 收起自动换行深色代码主题复制

```
/* xxx.css */ .container { width : 100% ; height : 100% ; background-color : #F1F3F5 ; flex-direction : column; align-items : center; justify-content : center; } .circle { font-size : 120px ; background-color : blue; radius: 72px ; } .text { margin-top : 30px ; text- color : white; font-size : 30px ; font-style : normal; background-color : blue; width : 50% ; height : 100px ; }
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165937.53142067597289275098581573513171:50001231000000:2800:E110A502C18838049A3193AE00C09EEF0B040B1E1413782923580CF415F3F3DD.png)

 说明 

- button组件使用的icon图标如果来自云端路径，需要添加网络访问权限 ohos.permission.INTERNET。

如果需要添加ohos.permission.INTERNET权限，则在resources文件夹下的config.json文件里进行权限配置。

 收起自动换行深色代码主题复制

```
<!-- config.json --> "module" : { "reqPermissions" : [ { "name" : "ohos.permission.INTERNET" } ] , }
```

## 显示下载进度

为button组件添加setProgress方法，来实时显示下载进度条的进度。

 收起自动换行深色代码主题复制

```
<!-- xxx.hml --> < div class = "container" > < button class = "button download" type = "download" id = "download-btn" onclick = "setProgress" > {{downloadText}} </ button > </ div >
```

 收起自动换行深色代码主题复制

```
/* xxx.css */ .container { width : 100% ; height : 100% ; background-color : #F1F3F5 ; flex-direction : column; align-items : center; justify-content : center; } .download { width : 280px ; text- color : white; background-color : #007dff ; }
```

 收起自动换行深色代码主题复制

```
// xxx.js import promptAction from '@ohos.promptAction' ; export default { data : { percent : 0 , downloadText : "Download" , isPaused : true , intervalId : null , }, start ( ){ this . intervalId = setInterval ( ()=> { if ( this . percent < 100 ){ this . percent += 1 ; this . downloadText = this . percent + "%" ; } else { promptAction. showToast ({ message : "Download succeeded." }) this . paused () this . downloadText = "Download" ; this . percent = 0 ; this . isPaused = true ; } }, 100 ) }, paused ( ){ clearInterval ( this . intervalId ); this . intervalId = null ; }, setProgress ( e ) { if ( this . isPaused ){ promptAction. showToast ({ message : "Started Downloading" }) this . start (); this . isPaused = false ; } else { promptAction. showToast ({ message : "Paused." }) this . paused (); this . isPaused = true ; } } }
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165937.87848332965572691638473068624152:50001231000000:2800:F4D6C1B8F4CA4056BC0AE6A7B8F56C19C9EA80CE95422E1BEA8DF210EC64880B.gif)

 说明 

setProgress方法只支持button的类型为download。

## 场景示例

在本场景中，开发者可根据输入的文本内容进行button类型切换。

 收起自动换行深色代码主题复制

```
<!-- xxx.hml --> < div class = "container" > < div class = "input-item" > < input class = "input-text" id = "change" type = "{{mytype}}" placeholder = "{{myholder}}" style = "background-color:{{mystyle1}}; placeholder-color:{{mystyle2}};flex-grow:{{myflex}};" name = "{{myname}}" value = "{{myvalue}}" > </ input > </ div > < div class = "input-item" > < div class = "doc-row" > < input type = "button" class = "select-button color-3" value = "text" onclick = "changetype3" > </ input > < input type = "button" class = "select-button color-3" value = "data" onclick = "changetype4" > </ input > </ div > </ div > </ div >
```

 收起自动换行深色代码主题复制

```
/* xxx.css */ .container { flex-direction : column; align-items : center; background-color : #F1F3F5 ; } .input-item { margin-bottom : 80px ; flex-direction : column; } .doc-row { justify-content : center; margin-left : 30px ; margin-right : 30px ; } .input-text { height : 80px ; line-height : 80px ; padding-left : 30px ; padding-right : 30px ; margin-left : 30px ; margin-right : 30px ; margin-top : 100px ; border : 3px solid; border-color : #999999 ; font-size : 30px ; background-color : #ffffff ; font-weight : 400 ; } .select-button { width : 35% ; text-align : center; height : 70px ; padding-top : 10px ; padding-bottom : 10px ; margin-top : 30px ; font-size : 30px ; color : #ffffff ; } .color-3 { background-color : #0598db ; }
```

 收起自动换行深色代码主题复制

```
// xxx.js export default { data : { myflex : '' , myholder : 'Enter text.' , myname : '' , mystyle1 : "#ffffff" , mystyle2 : "#ff0000" , mytype : 'text' , myvalue : '' , }, onInit ( ) { }, changetype3 ( ) { this . myflex = '' ; this . myholder = 'Enter text.' ; this . myname = '' ; this . mystyle1 = "#ffffff" ; this . mystyle2 = "#FF0000" ; this . mytype = 'text' ; this . myvalue = '' ; }, changetype4 ( ) { this . myflex = '' ; this . myholder = 'Enter a date.' ; this . myname = '' ; this . mystyle1 = "#ffffff" ; this . mystyle2 = "#FF0000" ; this . mytype = 'date' ; this . myvalue = '' ; }, }
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165937.22109414072666519282190600431203:50001231000000:2800:EBB2D7A18D5408C7C81FE6F792AF566D78BF2043D68B9337541465F1E508BFDB.gif)