# CanvasRenderingContext2D对象

使用CanvasRenderingContext2D在canvas画布组件上进行绘制，绘制对象可以是矩形、文本。

**示例：**

```
<!-- xxx.hml -->
<div>
    <canvas ref="canvas1" style="width: 200px; height: 150px; background-color: #ffff00;"></canvas>
    <input type="button" style="width: 180px; height: 60px;" value="fillStyle" onclick="handleClick" />
</div>
```

```
// xxx.js
export default {
  handleClick() {
    const el = this.$refs.canvas1;
    const ctx = el.getContext('2d');
    ctx.beginPath();
    ctx.arc(100, 75, 50, 0, 6.28);
    ctx.stroke();
  },
}
```

 ![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170825.08669005518999289905941623866935:50001231000000:2800:11D2B0A0CA63E21E0D0DDDFAD1575A38CFA650B055BDAD9EE1AC6F8ECEDCF0D0.png)

## fillRect()

支持设备PhonePC/2in1TabletTVWearableLite Wearable

填充一个矩形。

**参数：**

 展开

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| x | number | 指定矩形左上角点的x坐标。 |
| y | number | 指定矩形左上角点的y坐标。 |
| width | number | 指定矩形的宽度。 |
| height | number | 指定矩形的高度。 |

**示例：**

 ![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170825.48189649173898586792343328658057:50001231000000:2800:F77853C3AD1C80396B8E304F18F007A3023DF4104BF8B330A882C8406E2F2CF6.png)

```
ctx.fillRect(20, 20, 200, 150);
```

## fillStyle

支持设备PhonePC/2in1TabletTVWearableLite Wearable

指定绘制的填充色。

**参数：**

 展开

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| color | <color> | 设置填充区域的颜色。 |

**示例：**

 ![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170825.96883636443440458403276717613682:50001231000000:2800:44A8A3738A590374E1701076C8D8EBE9DC546892B8A78EC3A2906E0DD07B009E.png)

```
ctx.fillStyle = '#0000ff';
ctx.fillRect(20, 20, 150, 100);
```

## strokeRect()

支持设备PhonePC/2in1TabletTVWearableLite Wearable

绘制具有边框的矩形，矩形内部不填充。

**参数：**

 展开

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| x | number | 指定矩形的左上角x坐标。 |
| y | number | 指定矩形的左上角y坐标。 |
| width | number | 指定矩形的宽度。 |
| height | number | 指定矩形的高度。 |

**示例：**

 ![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170826.62441277599557669448160640535169:50001231000000:2800:609A36F27804B324F15CE442861587E5070B66988C7258179E8FFC9C6B37FF8F.png)

```
ctx.strokeRect(30, 30, 200, 150);
```

## fillText()

支持设备PhonePC/2in1TabletTVWearableLite Wearable

绘制填充类文本。

**参数：**

 展开

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| text | string | 需要绘制的文本内容。 |
| x | number | 需要绘制的文本的左下角x坐标。 |
| y | number | 需要绘制的文本的左下角y坐标。 |

**示例：**

 ![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170826.22339404176377359574157679858916:50001231000000:2800:5F662220AB06E79A2E40366006711CC8EBA30EF6A8E8F658CFA9413B13FBFB51.png)

```
ctx.font = '35px sans-serif';
ctx.fillText("Hello World!", 20, 60);
```

## lineWidth

支持设备PhonePC/2in1TabletTVWearableLite Wearable

指定绘制线条的宽度值。

**参数：**

 展开

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| lineWidth | number | 设置绘制线条的宽度。 |

**示例：**

 ![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170826.92420511350006226868685676371377:50001231000000:2800:19315C13CEC12D0FABC8A4E32FDAEBF51AC860F9D337C598CBBE278644F2767C.png)

```
ctx.lineWidth = 5;
ctx.strokeRect(25, 25, 85, 105);
```

## strokeStyle

支持设备PhonePC/2in1TabletTVWearableLite Wearable

设置描边的颜色。

**参数：**

 展开

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| color | <color> | 指定描边使用的颜色 |

**示例：**

 ![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170826.29896552887549118301925946801236:50001231000000:2800:224844D77144C11C4662CD5A5DCE508022DCF4821C4EAE4A43832B3773DF4AF5.png)

```
ctx.lineWidth = 10;
ctx.strokeStyle = '#0000ff';
ctx.strokeRect(25, 25, 155, 105);
```

### stroke() 5+

支持设备PhonePC/2in1TabletTVWearableLite Wearable

进行边框绘制操作。

**示例：**

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170826.93669867607433230838412805663710:50001231000000:2800:71C627BB186214CA800C0F8E49E2EBECB7EE1BC4C2C447A3E66B28E013049CD9.png)

```
ctx.moveTo(25, 25);
ctx.lineTo(25, 105);
ctx.strokeStyle = 'rgb(0,0,255)';
ctx.stroke();
```

### beginPath() 5+

支持设备PhonePC/2in1TabletTVWearableLite Wearable

创建一个新的绘制路径。

**示例：**

 ![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170826.40041636834947762627637642433935:50001231000000:2800:EDD2B326CEED2912CA09ABDBF29DC98B8BD07FED582D26826170C94BD6B6E309.png)

```
ctx.beginPath();
ctx.lineWidth = '6';
ctx.strokeStyle = '#0000ff';
ctx.moveTo(15, 80);
ctx.lineTo(280, 80);
ctx.stroke();
```

### moveTo() 5+

支持设备PhonePC/2in1TabletTVWearableLite Wearable

路径从当前点移动到指定点。

**参数：**

 展开

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| x | number | 指定位置的x坐标。 |
| y | number | 指定位置的y坐标。 |

**示例：**

 ![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170826.32539792295281699257872132962914:50001231000000:2800:420A39F4563F246480A1D07F6B34BD08C67627FAF554CA87290D31C58A413824.png)

```
ctx.beginPath();
ctx.moveTo(10, 10);
ctx.lineTo(280, 160);
ctx.stroke();
```

### lineTo() 5+

支持设备PhonePC/2in1TabletTVWearableLite Wearable

从当前点到指定点进行路径连接。

**参数：**

 展开

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| x | number | 指定位置的x坐标。 |
| y | number | 指定位置的y坐标。 |

**示例：**

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170826.44149254383023881910627136487212:50001231000000:2800:1DBBFC4A87C36938E2048A2CB1DBB976801F10B2D2D16F37963C6DC27429FE6D.png)

```
ctx.beginPath();
ctx.moveTo(10, 10);
ctx.lineTo(280, 160);
ctx.stroke();
```

### closePath() 5+

支持设备PhonePC/2in1TabletTVWearableLite Wearable

结束当前路径形成一个封闭路径。

**示例：**

 ![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170826.05331656873635963320501038548105:50001231000000:2800:ED0AFCE927A524DE4F73020986FBD941E30584D14C759362722168173912DB59.png)

```
ctx.beginPath();
ctx.moveTo(30, 30);
ctx.lineTo(110, 30);
ctx.lineTo(70, 90);
ctx.closePath();
ctx.stroke();
```

## font

支持设备PhonePC/2in1TabletTVWearableLite Wearable

设置文本绘制中的字体样式。

**参数：**

 展开

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| value | string | 字体样式支持：sans-serif, serif, monospace，该属性默认值为30px HYQiHei-65S。 |

**示例：**

 ![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170826.74086035746901166030090780577185:50001231000000:2800:BB8594483D2662C1F89D6E1B214B66008A5CBE22EB6D29B748B4CBA4998B30F1.png)

```
ctx.font = '30px sans-serif';
ctx.fillText("Hello World", 20, 60);
```

## textAlign

支持设备PhonePC/2in1TabletTVWearableLite Wearable

设置文本绘制中的文本对齐方式。

**参数：**

 展开

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| align | string | 可选值为： - left（默认）：文本左对齐； - right：文本右对齐； - center：文本居中对齐； |

**示例：**

 ![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170826.49938190697677209665303754094908:50001231000000:2800:224A3BA79693A58640A502E85447D5D8245F1F305D4AC43D40EC4F54761B7903.png)

```
ctx.strokeStyle = '#0000ff';
ctx.moveTo(140, 10);
ctx.lineTo(140, 160);
ctx.stroke();

ctx.font = '18px sans-serif';

// Show the different textAlign values
ctx.textAlign = 'left';
ctx.fillText('textAlign=left', 140, 100);
ctx.textAlign = 'center';
ctx.fillText('textAlign=center',140, 120);
ctx.textAlign = 'right';
ctx.fillText('textAlign=right',140, 140);
```

## arc() 5+

支持设备PhonePC/2in1TabletTVWearableLite Wearable

绘制弧线路径。

**参数：**

 展开

| 参数 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| x | number | 是 | 弧线圆心的x坐标值，单位：vp。 |
| y | number | 是 | 弧线圆心的y坐标值，单位：vp。 |
| radius | number | 是 | 弧线的圆半径，单位：vp。 |
| startAngle | number | 是 | 弧线的起始弧度，单位：弧度。 |
| endAngle | number | 是 | 弧线的终止弧度，单位：弧度。 |
| anticlockwise | boolean | 否 | 是否逆时针绘制圆弧。 true：逆时针方向绘制弧线。 false：顺时针方向绘制弧线。 默认值：false。 |

**示例：**

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170826.14740223999675347660969575102884:50001231000000:2800:8F675E9FB7112A67CEAA22D5155CC4155DDBDDDAA2F745118919A90023E130EE.png)

```
ctx.beginPath();
ctx.arc(100, 75, 50, 0, 6.28);
ctx.stroke();
```

### rect() 5+

支持设备PhonePC/2in1TabletTVWearableLite Wearable

创建矩形路径。

**参数：**

 展开

| 参数 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| x | number | 是 | 指定矩形的左上角x坐标值，单位：vp。 |
| y | number | 是 | 指定矩形的左上角y坐标值，单位：vp。 |
| width | number | 是 | 指定矩形的宽度，单位：vp。 |
| height | number | 是 | 指定矩形的高度，单位：vp。 |

**示例：**

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170826.07282933796771868341672207256797:50001231000000:2800:38BAA2FCDCDD94E812D6487F809678A73678AA64D4B83A09F960EF065212ADE1.png)

```
ctx.rect(20, 20, 100, 100); // Create a 100*100 rectangle at (20, 20)
ctx.stroke(); // Draw it
```