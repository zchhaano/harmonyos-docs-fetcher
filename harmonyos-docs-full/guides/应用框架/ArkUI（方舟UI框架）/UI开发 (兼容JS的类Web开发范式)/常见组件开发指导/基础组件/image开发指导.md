# image开发指导

image是图片组件，用来渲染展示图片。具体用法请参考[image](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-basic-image)组件。

## 创建image组件

在pages/index目录下的hml文件中创建一个image组件。

 收起自动换行深色代码主题复制

```
<!-- index.hml --> < div class = "container" > < image style = "height: 30%;" src = "common/images/bg-tv.jpg" > </ image > </ div >
```

 收起自动换行深色代码主题复制

```
/* xxx.css */ .container { width : 100% ; height : 100% ; flex-direction : column; justify-content : center; align-items : center; background-color : #F1F3F5 ; }
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165950.95588522783732523087146139435570:50001231000000:2800:72EDE3C0E26A67E64017F898E49F04C72AF8F3C4857B07022338AA8EE941F89C.png)

## 设置image样式

通过设置width、height和object-fit属性定义图片的宽、高和缩放样式。

 收起自动换行深色代码主题复制

```
<!-- index.hml --> < div class = "container" > < image src = "common/images/bg-tv.jpg" > </ image > </ div >
```

 收起自动换行深色代码主题复制

```
/* xxx.css */ .container { width : 100% ; height : 100% ; flex-direction : column; align-items : center; justify-content : center; background-color : #F1F3F5 ; } image{ width : 80% ; height : 500px ; border : 5px solid saddlebrown; border-radius : 20px ; object-fit : contain; match-text- direction :true; }
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165950.45449003473640113245909454823415:50001231000000:2800:476DCFE86A6F4665C2FFB7DF35F8634FD5C10474F60EE53DD42D40FC2C064194.png)

## 加载图片

图片成功加载时触发complete事件，返回加载的图源尺寸。加载失败则触发error事件，打印图片加载失败。

 收起自动换行深色代码主题复制

```
<!-- index.hml --> < div class = "container" > < div > < image src = "common/images/bg-tv.jpg" oncomplete = "imageComplete(1)" onerror = "imageError(1)" > </ image > </ div > < div > < image src = "common/images/bg-tv1.jpg" oncomplete = "imageComplete(2)" onerror = "imageError(2)" > </ image > </ div > </ div >
```

 收起自动换行深色代码主题复制

```
/* xxx.css */ .container { width : 100% ; height : 100% ; flex-direction : column; justify-content : center; align-self : center; background-color : #F1F3F5 ; } .container div { margin-left : 10% ; width : 80% ; height : 300px ; margin-bottom : 40px ; }
```

 收起自动换行深色代码主题复制

```
// index.js import promptAction from '@ohos.promptAction' ; export default { imageComplete ( i,e ){ promptAction. showToast ({ message : "image " +i+ "'s width" + e. width + "----image " +i+ "'s height" +e. height , duration : 3000 , }) }, imageError ( i,e ){ setTimeout ( ()=> { promptAction. showToast ({ message : "Failed to load image " +i+ "." , duration : 3000 , }) }, 3000 ) } }
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165950.30103016721457746129575955870007:50001231000000:2800:D68BAF68441DA2E4B252BA4FC6ADC7AB8161CF78FE74C3749758291B2FDD4811.gif)

## 场景示例

在本场景中，开发者长按图片后将慢慢隐藏图片，当完全隐藏后再重新显示原始图片。定时器setInterval每隔一段时间改变图片透明度,实现慢慢隐藏的效果，当透明度为0时清除定时器，设置透明度为1。

 收起自动换行深色代码主题复制

```
<!-- index.hml --> < div class = "page-container" > < div class = "content" > < div class = "image-container" > < image class = "testimage" src = "{{testuri}}" style = "opacity:{{imageopacity}};" onlongpress = "changeopacity" > </ image > </ div > < div class = "text-container" > < text style = "font-size: 37px;font-weight:bold;color:orange;text-align: center;width: 100%;" > Touch and hold the image </ text > </ div > </ div > </ div >
```

 收起自动换行深色代码主题复制

```
/* xxx.css */ .page-container { width : 100% ; height : 100% ; flex-direction :column; align-self : center; justify-content : center; background-color : #F1F3F5 ; background-color : #F1F3F5 ; } .content { flex-direction :column; } .image-container { width : 100% ; height : 300px ; align-items : center; justify-content : center; } .text-container { margin-top : 50px ; width : 100% ; height : 60px ; flex-direction : row; justify-content : space-between; } .testimage { width : 100% ; height : 400px ; object-fit : scale-down; border-radius : 20px ; }
```

 收起自动换行深色代码主题复制

```
// index.js import promptAction from '@ohos.promptAction' ; export default { data : { testuri : 'common/images/bg-tv.jpg' , imageopacity : 1 , timer : null }, changeopacity : function ( ) { promptAction. showToast ({ message : 'Touch and hold the image.' }) var opval = this . imageopacity * 20 clearInterval ( this . timer ); this . timer = setInterval ( ()=> { opval--; this . imageopacity = opval / 20 if (opval=== 0 ) { clearInterval ( this . timer ) this . imageopacity = 1 } }, 100 ); } }
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165950.69329813133788776718773977944037:50001231000000:2800:8858CEDAE0C3530FDF9256797F965BB9AC763D506EDEAA8E3DD8ACCBD9E4F50E.gif)