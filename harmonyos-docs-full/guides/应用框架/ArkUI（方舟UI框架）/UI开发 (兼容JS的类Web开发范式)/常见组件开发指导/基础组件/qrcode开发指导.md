# qrcode开发指导

生成并显示二维码，具体用法请参考[qrcode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-basic-qrcode)。

## 创建qrcode组件

在pages/index目录下的hml文件中创建一个qrcode组件。

 收起自动换行深色代码主题复制

```
<!-- xxx.hml--> < div class = "container" > < qrcode value = "Hello" > </ qrcode > </ div >
```

 收起自动换行深色代码主题复制

```
/* xxx.css */ .container { width : 100% ; height : 100% ; flex-direction : column; align-items : center; justify-content : center; background-color : #F1F3F5 ; }
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170000.49430813540975632292946399991380:50001231000000:2800:BB49CCFA8BF3B0518E7EB134D864D96B1F0418B20D15D2370E9FE1DB45187DE3.png)

 说明 

qrcode组件在创建的时候value的值为必填项。

## 设置组件类型

通过设置qrcode的type属性来选择按钮类型，如定义qrcode为矩形二维码、圆形二维码。

 收起自动换行深色代码主题复制

```
<!-- xxx.hml--> < div class = "container" > < select onchange = "settype" > < option for = "{{bcol_list}}" value = "{{$item}}" > {{$item}} </ option > </ select > < qrcode value = "Hello" type = "{{qr_type}}" > </ qrcode > </ div >
```

 收起自动换行深色代码主题复制

```
/* xxx.css */ .container { width : 100% ; height : 100% ; flex-direction : column; align-items : center; justify-content : center; background-color : #F1F3F5 ; } select{ margin-top : 50px ; margin-bottom : 50px ; }
```

 收起自动换行深色代码主题复制

```
// index.js export default { data : { qr_type : 'rect' , bcol_list : [ 'rect' , 'circle' ] }, settype ( e ) { this . qr_type = e. newValue }, }
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170000.26204970098991197984355847754434:50001231000000:2800:6ABEE07CB0EF32E1DCDC161E620619CCE8E3E4ED18EC096435438D8C81FCDAAA.gif)

## 设置样式

通过color和background-color样式为二维码设置显示颜色和背景颜色。

 收起自动换行深色代码主题复制

```
<!-- xxx.hml--> < div class = "container" > < qrcode value = "Hello" type = "rect" > </ qrcode > </ div >
```

 收起自动换行深色代码主题复制

```
/* xxx.css */ .container { width : 100% ; height : 100% ; flex-direction : column; align-items : center; justify-content : center; background-color : #F1F3F5 ; } qrcode{ width : 300px ; height : 300px ; color : blue; background-color : #ffffff ; }
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170000.69954821684916878108458367591214:50001231000000:2800:5D95BCB3BB77EE8E67E624DCD5C3CF6BB85A69574629A81378A956698BECD2F0.png)

 说明 

- width和height不一致时，取二者较小值作为二维码的边长，且最终生成的二维码居中显示。
- width和height只设置一个时，取设置的值作为二维码的边长。都不设置时，使用200px作为默认边长。

## 场景示例

在本场景中将二维码与输入框绑定，通过改变输入框的内容改变二维码。

 收起自动换行深色代码主题复制

```
<!-- xxx.hml--> < div class = "container" > < input style = "margin-bottom: 100px;" onchange = "change" > </ input > < qrcode value = "{{textVal}}" > </ qrcode > </ div >
```

 收起自动换行深色代码主题复制

```
/* xxx.css */ .container { width : 100% ; height : 100% ; flex-direction : column; align-items : center; justify-content : center; background-color : #F1F3F5 ; } qrcode{ width : 400px ; height : 400px ; }
```

 收起自动换行深色代码主题复制

```
// index.js export default { data : { textVal : '' }, change ( e ){ this . textVal = e. value } }
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170000.93133704502487916898621199531003:50001231000000:2800:4325663FC03E479E97610106D470B5F0CF255E38276719DE015D21046AF6FBD3.gif)