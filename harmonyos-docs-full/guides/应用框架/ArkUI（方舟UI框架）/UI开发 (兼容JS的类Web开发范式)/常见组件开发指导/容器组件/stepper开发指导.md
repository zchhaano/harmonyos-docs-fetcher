# stepper开发指导

当一个任务需要多个步骤时，可以使用stepper组件展示当前进展。具体用法请参考[stepper API](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-container-stepper)。

## 创建stepper组件

在pages/index目录下的hml文件中创建一个stepper组件。

 收起自动换行深色代码主题复制

```
<!-- xxx.hml --> < div class = "container" > < stepper > < stepper-item > < text > Step 1 </ text > </ stepper-item > < stepper-item > < text > Step 2 </ text > </ stepper-item > </ stepper > </ div >
```

 收起自动换行深色代码主题复制

```
/* xxx.css */ .container { width : 100% ; height : 100% ; flex-direction : column; justify-content : center; align-items : center; background-color : #F1F3F5 ; } text{ width : 100% ; height : 100% ; text-align : center; }
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165944.63897558179449614988292987252267:50001231000000:2800:DB9566ED47E4135F52721DB2C23174F25F6D9579799872D9B590DAEC82A831A6.gif)

## 设置index属性

页面默认显示索引值为index的步骤。

 收起自动换行深色代码主题复制

```
<!-- xxx.hml --> < div class = "container" > < stepper index = "2" > < stepper-item > < text > stepper-item1 </ text > </ stepper-item > < stepper-item > < text > stepper-item2 </ text > </ stepper-item > < stepper-item > < text > stepper-item3 </ text > </ stepper-item > </ stepper > </ div >
```

 收起自动换行深色代码主题复制

```
/* xxx.css */ .container { width : 100% ; height : 100% ; flex-direction : column; background-color : #F1F3F5 ; } text{ width : 100% ; height : 100% ; text-align : center; }
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165944.56011549747385260507839889533324:50001231000000:2800:C398931F828704690085FCCC2927DDEB7630D5AF631BE4224331A5E009F5E9A4.gif)

通过设置label属性，自定义stepper-item的提示按钮。

 收起自动换行深色代码主题复制

```
<!-- xxx.hml --> < div class = "container" > < stepper index = "1" > < stepper-item label = "{{label_1}}" > < text > stepper-item1 </ text > </ stepper-item > < stepper-item label = "{{label_2}}" > < text > stepper-item2 </ text > </ stepper-item > < stepper-item label = "{{label_3}}" > < text > stepper-item3 </ text > </ stepper-item > < stepper-item > < text > stepper-item4 </ text > </ stepper-item > </ stepper > </ div >
```

 收起自动换行深色代码主题复制

```
/* xxx.css */ .container { width : 100% ; height : 100% ; flex-direction : column; background-color : #F1F3F5 ; } text{ width : 100% ; height : 100% ; text-align : center; }
```

 收起自动换行深色代码主题复制

```
// xxx.js export default { data : { label_1 :{ nextLabel : 'NEXT' , status : 'normal' }, label_2 :{ prevLabel : 'BACK' , nextLabel : 'NEXT' , status : 'normal' }, label_3 :{ prevLabel : 'BACK' , nextLabel : 'END' , status : 'disabled' }, }, }
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165944.87160098227691372975169555625001:50001231000000:2800:72D4EA1505B4E94237DD9F95183F4B4705FB1AC9216B37B66AC2427FDE7D2A45.gif)

## 设置样式

stepper组件默认填充父容器，通过border和background-color设置边框、背景色。

 收起自动换行深色代码主题复制

```
<!-- xxx.hml --> < div class = "container" > < div class = "stepperContent" > < stepper class = "stepperClass" > < stepper-item > < text > stepper-item1 </ text > </ stepper-item > </ stepper > </ div > </ div >
```

 收起自动换行深色代码主题复制

```
/* xxx.css */ .container { width : 100% ; height : 100% ; flex-direction : column; align-items : center; justify-content : center; background-color : #F1F3F5 ; } .stepperContent { width : 300px ; height : 300px ; } .stepperClass { border : 1px solid silver ; background-color : white; } text{ width : 100% ; height : 100% ; text-align : center; }
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165944.38372541317851193761275080503524:50001231000000:2800:5BC87D545776E313918971638D677757779A653F35FF388A1DF8131564D0CE01.png)

## 添加事件

stepper分别添加finish，change，next，back，skip事件。

- 当change与next或back同时存在时，会先执行next或back事件再去执行change事件。
- 重新设置index属性值时要先清除index的值再重新设置，否则检测不到值的改变。

 收起自动换行深色代码主题复制

```
<!-- xxx.hml --> < div class = "container" style = "background-color:#F1F3F5;" > < div > < stepper onfinish = "stepperFinish" onchange = "stepperChange" onnext = "stepperNext" onback = "stepperBack" onskip = "stepperSkip" id = "stepperId" index = "{{index}}" > < stepper-item > < text > stepper-item1 </ text > < button value = "skip" onclick = "skipClick" > </ button > </ stepper-item > < stepper-item > < text > stepper-item2 </ text > < button value = "skip" onclick = "skipClick" > </ button > </ stepper-item > < stepper-item > < text > stepper-item3 </ text > </ stepper-item > </ stepper > </ div > </ div >
```

 收起自动换行深色代码主题复制

```
/* xxx.css */ .doc-page { width : 100% ; height : 100% ; flex-direction : column; align-items : center; justify-content : center; } stepper-item{ width : 100% ; flex-direction : column; align-self : center; justify-content : center; } text{ margin-top : 45% ; justify-content : center; align-self : center; margin-bottom : 50px ; } button { width : 80% ; height : 60px ; margin-top : 20px ; }
```

 收起自动换行深色代码主题复制

```
// xxx.js import promptAction from '@ohos.promptAction' ; export default { data : { index : 0 , }, stepperSkip ( ){ this . index = 2 ; }, skipClick ( ){ this .$element( 'stepperId' ). setNextButtonStatus ({ status : 'skip' , label : 'SKIP' }); }, stepperFinish ( ){ promptAction. showToast ({ message : 'All Finished' }) }, stepperChange ( e ){ console . info ( "stepperChange" +e. index ) promptAction. showToast ({ // index表示当前步骤的序号 message : 'Previous step: ' +e. prevIndex + "-------Current step:" +e. index }) }, stepperNext ( e ){ console . info ( "stepperNext" +e. index ) promptAction. showToast ({ // pendingIndex表示将要跳转的序号 message : 'Current step:' +e. index + "-------Next step:" +e. pendingIndex }) var index = { pendingIndex :e. pendingIndex } return index; }, stepperBack ( e ){ console . info ( "stepperBack" +e. index ) var index = { pendingIndex : e. pendingIndex } return index; } }
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165944.90515206676788207430696309688546:50001231000000:2800:A8480CEB22CF3D00FF964D4095CF6DEA4FA381223BD2D5F76D8D08BF6CA12C63.gif)