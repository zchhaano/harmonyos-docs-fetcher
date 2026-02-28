# Path2D对象

路径对象，支持通过对象的接口进行路径的描述，并通过Canvas的[stroke](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-canvas-canvasrenderingcontext2d#stroke)接口进行绘制。

 说明 

 本模块首批接口从API version 4开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## addPath

支持设备PhonePC/2in1TabletTVWearable

addPath(path: Object): void

将另一个路径添加到当前的路径对象中。

**参数：**

 展开

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| path | Object | 需要添加到当前路径的路径对象。 |

**示例：**

```
<!-- xxx.hml -->
<div>
    <canvas ref="canvas" style="width: 500px; height: 500px; background-color: #ffff00;"></canvas>
</div>
```

```
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    var path1 = ctx.createPath2D("M250 150 L150 350 L350 350 Z");
    var path2 = ctx.createPath2D();
    path2.addPath(path1);
    ctx.stroke(path2);
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170903.77825867092038911034248230548963:50001231000000:2800:68365DBA96C950C980867DCF3BA2665FD6E870A5E43B840280B8EF4E4BC4A0BB.png)

## setTransform

支持设备PhonePC/2in1TabletTVWearable

setTransform(scaleX: number, skewX: number, skewY: number, scaleY: number, translateX: number, translateY: number): void

设置路径变换矩阵。

**参数：**

 展开

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| scaleX | number | x轴的缩放比例。 |
| skewX | number | x轴的倾斜角度。 |
| skewY | number | y轴的倾斜角度。 |
| scaleY | number | y轴的缩放比例。 |
| translateX | number | x轴的平移距离。 |
| translateY | number | y轴的平移距离。 |

**示例：**

```
<!-- xxx.hml -->
<div>
    <canvas ref="canvas" style="width: 300px; height: 250px; background-color: #ffff00;"></canvas>
</div>
```

```
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    var path = ctx.createPath2D("M250 150 L150 350 L350 350 Z");
    path.setTransform(0.8, 0, 0, 0.4, 0, 0);
    ctx.stroke(path);
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170904.51312544853147675862730738809094:50001231000000:2800:0A020CC8AFA2A55D2BA772155A2E12585F8340089B8D1DB6D4B2746B75484662.png)

## closePath

支持设备PhonePC/2in1TabletTVWearable

closePath(): void

将路径的当前点移回到路径的起点，当前点到起点间画一条直线。如果形状已经闭合或只有一个点，则此功能不执行任何操作。

**示例：**

```
<!-- xxx.hml -->
<div>
    <canvas ref="canvas" style="width: 500px; height: 500px; background-color: #ffff00;"></canvas>
</div>
```

```
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    var path = ctx.createPath2D();
    path.moveTo(200, 100);
    path.lineTo(300, 100);
    path.lineTo(200, 200);
    path.closePath();
    ctx.stroke(path);
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170904.39057307685590855657033098249999:50001231000000:2800:702122B128B87EDE471F156F62691D288F077A58CCEDD9454F858A3E295FD8CF.png)

## moveTo

支持设备PhonePC/2in1TabletTVWearable

moveTo(x: number, y: number): void

将路径的当前坐标点移动到目标点，移动过程中不绘制线条。

**参数：**

 展开

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| x | number | 目标点X轴坐标。 |
| y | number | 目标点Y轴坐标。 |

**示例：**

```
<!-- xxx.hml -->
<div>
    <canvas ref="canvas" style="width: 300px; height: 250px; background-color: #ffff00;"></canvas>
</div>
```

```
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    var path = ctx.createPath2D();
    path.moveTo(50, 100);
    path.lineTo(250, 100);
    path.lineTo(150, 200);
    path.closePath();
    ctx.stroke(path);
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170904.14065519415058419028823783505948:50001231000000:2800:DE35A320B5BE832EDC91DD033FD5D690EBA9B65DBE35ABC39D68C3A2FD0EFAA2.png)

## lineTo

支持设备PhonePC/2in1TabletTVWearable

lineTo(x: number, y: number): void

从当前点绘制一条直线到目标点。

**参数：**

 展开

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| x | number | 目标点X轴坐标。 |
| y | number | 目标点Y轴坐标。 |

**示例：**

```
<!-- xxx.hml -->
<div>
    <canvas ref="canvas" style="width: 400px; height: 450px; background-color: #ffff00;"></canvas>
</div>
```

```
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    var path = ctx.createPath2D();
    path.moveTo(100, 100);
    path.lineTo(100, 200);
    path.lineTo(200, 200);
    path.lineTo(200, 100);
    path.closePath();
    ctx.stroke(path);
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170904.57743816198135743874612536820434:50001231000000:2800:093D5A8D8F891C198F667E7C6A84B361F6DA2B6B31A1A554A3D022BDC22C6D7A.png)

## bezierCurveTo

支持设备PhonePC/2in1TabletTVWearable

bezierCurveTo(cp1x: number, cp1y: number, cp2x: number, cp2y: number, x: number, y: number): void

创建三次贝塞尔曲线的路径。

**参数：**

 展开

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| cp1x | number | 第一个贝塞尔参数的x坐标值。 |
| cp1y | number | 第一个贝塞尔参数的y坐标值。 |
| cp2x | number | 第二个贝塞尔参数的x坐标值。 |
| cp2y | number | 第二个贝塞尔参数的y坐标值。 |
| x | number | 路径结束时的x坐标值。 |
| y | number | 路径结束时的y坐标值。 |

**示例：**

```
<!-- xxx.hml -->
<div>
    <canvas ref="canvas" style="width: 300px; height: 250px; background-color: #ffff00;"></canvas>
</div>
```

```
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    var path = ctx.createPath2D();
    path.moveTo(10, 10);
    path.bezierCurveTo(20, 100, 200, 100, 200, 20);
    ctx.stroke(path);
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170904.94155350681737633756228142770951:50001231000000:2800:807B4B63D49E7260C18AE6D62DCE5819FA37E4365BF3A19B6893C0635822B1B5.png)

## quadraticCurveTo

支持设备PhonePC/2in1TabletTVWearable

quadraticCurveTo(cpx: number, cpy: number, x: number, y: number): void

创建二次贝塞尔曲线的路径。

**参数：**

 展开

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| cpx | number | 贝塞尔参数的x坐标值。 |
| cpy | number | 贝塞尔参数的y坐标值。 |
| x | number | 路径结束时的x坐标值。 |
| y | number | 路径结束时的y坐标值。 |

**示例：**

```
<!-- xxx.hml -->
<div>
    <canvas ref="canvas" style="width: 300px; height: 250px; background-color: #ffff00;"></canvas>
</div>
```

```
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    var path = ctx.createPath2D();
    path.moveTo(10, 10);
    path.quadraticCurveTo(100, 100, 200, 20);
    ctx.stroke(path);
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170904.38293699176882241341623146352626:50001231000000:2800:A0B580832F4BEBA5FEE6E244DAA158DDABCE689E1F92475C3A34229704A0C9A1.png)

## arc

支持设备PhonePC/2in1TabletTVWearable

arc(x: number, y: number, radius: number, startAngle: number, endAngle: number, counterclockwise?: boolean): void

绘制弧线路径。

**参数：**

 展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 弧线圆心的x坐标值。 |
| y | number | 是 | 弧线圆心的y坐标值。 |
| radius | number | 是 | 弧线的圆半径。 |
| startAngle | number | 是 | 弧线的起始弧度。 |
| endAngle | number | 是 | 弧线的终止弧度。 |
| counterclockwise | boolean | 否 | 是否逆时针绘制圆弧，true为逆时针，false为顺时针。 默认值：false |

**示例：**

```
<!-- xxx.hml -->
<div>
    <canvas ref="canvas" style="width: 300px; height: 250px; background-color: #ffff00;"></canvas>
</div>
```

```
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    var path = ctx.createPath2D();
    path.arc(100, 75, 50, 0, 6.28);
    ctx.stroke(path);
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170904.47197397437835752122726673727848:50001231000000:2800:3AC8E05FFAA1CA3B8AE3117BD8FE36A6C720218A9772F222AABE38082E785B88.png)

## arcTo

支持设备PhonePC/2in1TabletTVWearable

arcTo(x1: number, y1: number, x2: number, y2: number, radius: number): void

依据圆弧经过的点和圆弧半径创建圆弧路径。

**参数：**

 展开

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| x1 | number | 圆弧经过的第一个点的x坐标值。 |
| y1 | number | 圆弧经过的第一个点的y坐标值。 |
| x2 | number | 圆弧经过的第二个点的x坐标值。 |
| y2 | number | 圆弧经过的第二个点的y坐标值。 |
| radius | number | 圆弧的圆半径值。 |

**示例：**

```
<!-- xxx.hml -->
<div>
    <canvas ref="canvas" style="width: 300px; height: 250px; background-color: #ffff00;"></canvas>
</div>
```

```
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    var path = ctx.createPath2D();
    path.arcTo(150, 20, 150, 70, 50);
    ctx.stroke(path);
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170904.46704951935851698123516216566748:50001231000000:2800:DCC4FF2466E09B4E02AD38EDA31EB54C05874B5C766E2ED395F2A63E8559DDCC.png)

## ellipse

支持设备PhonePC/2in1TabletTVWearable

ellipse(x: number, y: number, radiusX: number, radiusY: number, rotation: number, startAngle: number, endAngle: number, counterclockwise?: number): void

在规定的矩形区域绘制一个椭圆。

**参数：**

 展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 椭圆圆心的x轴坐标。 |
| y | number | 是 | 椭圆圆心的y轴坐标。 |
| radiusX | number | 是 | 椭圆x轴的半径长度。 |
| radiusY | number | 是 | 椭圆y轴的半径长度。 |
| rotation | number | 是 | 椭圆的旋转角度，单位为弧度。 |
| startAngle | number | 是 | 椭圆绘制的起始点角度，以弧度表示。 |
| endAngle | number | 是 | 椭圆绘制的结束点角度，以弧度表示。 |
| counterclockwise | number | 否 | 是否以逆时针方向绘制椭圆，0为顺时针，1为逆时针。其它数值均按默认值处理。 默认值：0 |

**示例：**

```
<!-- xxx.hml -->
<div>
    <canvas ref="canvas" style="width: 500px; height: 450px; background-color: #ffff00;"></canvas>
</div>
```

```
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    var path = ctx.createPath2D();
    path.ellipse(200, 200, 50, 100, Math.PI * 0.25, Math.PI * 0.5, Math.PI, 1);
    ctx.stroke(path);
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170904.11363770027610779647159770716842:50001231000000:2800:EFB53001C65B923D899D1B3C7D90E8576C178CECB871D058C79E42540D373A15.png)

## rect

支持设备PhonePC/2in1TabletTVWearable

rect(x: number, y: number, width: number, height: number): void

创建矩形路径。

**参数：**

 展开

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| x | number | 指定矩形的左上角x坐标值。 |
| y | number | 指定矩形的左上角y坐标值。 |
| width | number | 指定矩形的宽度。 |
| height | number | 指定矩形的高度。 |

**示例：**

```
<!-- xxx.hml -->
<div>
    <canvas ref="canvas" style="width: 500px; height: 450px; background-color: #ffff00;"></canvas>
</div>
```

```
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    var path = ctx.createPath2D();
    path.rect(20, 20, 100, 100);
    ctx.stroke(path);
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170904.56736245694611022513784592112701:50001231000000:2800:8B66F3EA689956BCE1D119A04ADA930119857337F62F10C4771901F4B8EB58FC.png)