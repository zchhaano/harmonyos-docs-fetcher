# background-position样式动画

通过改变background-position属性（第一个值为X轴的位置，第二个值为Y轴的位置）移动背景图片位置，若背景图位置超出组件则超出部分的背景图不显示。

 收起自动换行深色代码主题复制

```
<!-- xxx.hml --> < div class = "container" > < div class = "content" > </ div > < div class = "content1" > </ div > </ div >
```

 收起自动换行深色代码主题复制

```
/* xxx.css */ .container { height : 100% ; background-color : #F1F3F5 ; display : flex; flex-direction : column; justify-content : center; align-items : center; width : 100% ; } .content { width : 400px ; height : 400px ; /* 不建议图片长宽比为1:1 */ background-image : url ( 'common/images/bg-tv.jpg' ); background-size : 100% ; background-repeat : no-repeat; animation : change 3s infinite; border : 1px solid black; } .content1 { margin-top : 50px ; width : 400px ; height : 400px ; background-image : url ( 'common/images/bg-tv.jpg' ); background-size : 50% ; background-repeat : no-repeat; animation : change1 5s infinite; border : 1px solid black; } /* 背景图片移动出组件 */ @keyframes change{ 0% { background-position : 0px top; } 25% { background-position : 400px top; } 50% { background-position : 0px top; } 75% { background-position : 0px bottom; } 100% { background-position : 0px top; } } /* 背景图片在组件内移动 */ @keyframes change1{ 0% { background-position :left top ; } 25% { background-position : 50% 50% ; } 50% { background-position :right bottom ; } 100% { background-position :left top ; } }
```

 说明 

background-position仅支持背景图片的移动，不支持背景颜色（background-color）。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165937.82264086979077251216847331094425:50001231000000:2800:C96228C000862F80DB55E7FAE14AD2AAC53373F54B977F36E02A6E13EEE14BF1.gif)