# CanvasRenderingContext2D对象

说明 

从API version 4开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

使用CanvasRenderingContext2D在[canvas画布组件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-canvas-canvas)上进行绘制，绘制对象可以是矩形、文本、图片等。

**示例：**

```
<!-- xxx.hml -->
<div>
  <canvas ref="canvas1" style="width: 200px; height: 150px; background-color: #ffff00;"></canvas>
  <input type="button" style="width: 180px; height: 60px;" value="handleClick" onclick="handleClick" />
  <input type="button" style="width: 180px; height: 60px;" value="antialias" onclick="antialias" />
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
  antialias() {
    const el = this.$refs.canvas1;
    const ctx = el.getContext('2d', { antialias: true });
    ctx.beginPath();
    ctx.arc(100, 75, 50, 0, 6.28);
    ctx.stroke();
    }
  }
```

- 示意图（关闭抗锯齿）

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170822.56759102809532255197650098171471:50001231000000:2800:7452624CE351700DEAC0F7BFC8BED31AC0A1C5D2626CB41F1CD62754796AD5AD.png)
- 示意图（开启抗锯齿）

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170822.95201607714213329218135917168918:50001231000000:2800:FF51B16B37FB45A9B3C8E4C61EF14C27C7D68CB0CC2AF5FD73BD53BFAAFBE81D.png)

## 属性

 支持设备PhonePC/2in1TabletTVWearable 展开

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| fillStyle | <color> \| CanvasGradient \| CanvasPattern | 指定绘制的填充色。 - 类型为<color>时，表示设置填充区域的颜色。 - 类型为CanvasGradient时，表示渐变对象，使用 createLinearGradient()方法创建。 - 类型为CanvasPattern时，使用 createPattern()方法创建。 超出取值范围填充为黑色。 |
| lineWidth | number | 设置绘制线条的宽度。 |
| strokeStyle | <color> \| CanvasGradient \| CanvasPattern | 设置描边的颜色。 - 类型为<color>时，表示设置描边使用的颜色。 - 类型为CanvasGradient时，表示渐变对象，使用 createLinearGradient()方法创建。 - 类型为CanvasPattern时，使用 createPattern()方法创建。 |
| lineCap | string | 指定线端点的样式，可选值为： - butt：线端点以方形结束。 - round：线端点以圆形结束。 - square：线端点以方形结束，该样式下会增加一个长度和线段厚度相同，宽度是线段厚度一半的矩形。 默认值：butt |
| lineJoin | string | 指定线段间相交的交点样式，可选值为： - round：在线段相连处绘制一个扇形，扇形的圆角半径是线段的宽度。 - bevel：在线段相连处使用三角形为底填充， 每个部分矩形拐角独立。 - miter：在相连部分的外边缘处进行延伸，使其相交于一点，形成一个菱形区域，该属性可以通过设置miterLimit属性展现效果。 默认值：miter |
| miterLimit | number | 设置斜接面限制值，该值指定了线条相交处内角和外角的距离。 默认值：10 |
| font | string | 设置文本绘制中的字体样式。 语法：ctx.font="font-style font-weight font-size font-family" 5+ - font-style(可选)，用于指定字体样式，支持如下几种样式：normal, italic。 - font-weight(可选)，用于指定字体的粗细，支持如下几种类型：normal, bold, bolder, lighter, 100, 200, 300, 400, 500, 600, 700, 800, 900。 - font-size(可选)，指定字号和行高，单位只支持px。 - font-family(可选)，指定字体系列，支持如下几种类型：sans-serif, serif, monospace。 默认值："normal normal 14px sans-serif" |
| textAlign | string | 设置文本绘制中的文本对齐方式，可选值为： - left：文本左对齐。 - right：文本右对齐。 - center：文本居中对齐。 - start：文本对齐界线开始的地方。 - end：文本对齐界线结束的地方。 ltr布局模式下start和left一致，rtl布局模式下start和right一致。 默认值：left |
| textBaseline | string | 设置文本绘制中的水平对齐方式，可选值为： - alphabetic：文本基线是标准的字母基线。 - top：文本基线在文本块的顶部。 - hanging：文本基线是悬挂基线。 - middle：文本基线在文本块的中间。 - ideographic：文字基线是表意字基线；如果字符本身超出了alphabetic 基线，那么ideographic基线位置在字符本身的底部。 - bottom：文本基线在文本块的底部。 与 ideographic 基线的区别在于 ideographic 基线不需要考虑下行字母。 默认值： alphabetic |
| globalAlpha | number | 设置透明度。 范围为[0.0, 1.0]，0.0为完全透明，1.0为完全不透明。若给定值小于0.0，则取值0.0；若给定值大于1.0，则取值1.0。 |
| lineDashOffset | number | 设置画布的虚线偏移量，精度为float。 默认值：0.0 |
| globalCompositeOperation | string | 设置合成操作的方式。类型字段可选值有source-over，source-atop，source-in，source-out，destination-over，destination-atop，destination-in，destination-out，lighter，copy，xor。具体请参考 类型字段说明 。 默认值：source-over |
| shadowBlur | number | 设置绘制阴影时的模糊级别，值越大越模糊，精度为float。 默认值：0.0 |
| shadowColor | <color> | 设置绘制阴影时的阴影颜色。 |
| shadowOffsetX | number | 设置绘制阴影时和原有对象的水平偏移值。 |
| shadowOffsetY | number | 设置绘制阴影时和原有对象的垂直偏移值。 |
| imageSmoothingEnabled | boolean | 用于设置绘制图片时是否进行图像平滑度调整，true为启用，false为不启用。 默认值：true |

### fillStyle

 支持设备PhonePC/2in1TabletTVWearable

```
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
</div>
```

```
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.fillStyle = '#0000ff';
    ctx.fillRect(20, 20, 150, 100);
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170822.34012390305888124007675803589267:50001231000000:2800:83F7A267A90C4B2C4618794B56FCCB6BB3E7F3BA8F2923FFCC5F9D546B2FF394.png)

### lineWidth

 支持设备PhonePC/2in1TabletTVWearable

```
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
</div>
```

```
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.lineWidth = 5;
    ctx.strokeRect(25, 25, 85, 105);
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170822.70416674154465711767626565253360:50001231000000:2800:F768DE36DDDD4120DC6CF3830D553FFD223DF55B5E9902C33480281D560076AD.png)

### strokeStyle

 支持设备PhonePC/2in1TabletTVWearable

```
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
</div>
```

```
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.lineWidth = 10;
    ctx.strokeStyle = '#0000ff';
    ctx.strokeRect(25, 25, 155, 105);
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170822.89800430614343896168771724050321:50001231000000:2800:BA3C4B0EAD567076404A00DEE3CBBFB4AEB3EA077FBEFC228896E402C14AB488.png)

### lineCap

 支持设备PhonePC/2in1TabletTVWearable

```
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
</div>
```

```
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.lineWidth = 8;
    ctx.beginPath();
    ctx.lineCap = 'round';
    ctx.moveTo(30, 50);
    ctx.lineTo(220, 50);
    ctx.stroke();
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170822.41267816036336035793125871467836:50001231000000:2800:0C2D3B5B0B1B170F8ACB6697773F3D2E612C66B81A9F746A85FC2E50484D36F3.png)

### lineJoin

 支持设备PhonePC/2in1TabletTVWearable

```
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
</div>
```

```
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.beginPath();
    ctx.lineWidth = 8;
    ctx.lineJoin = 'miter';
    ctx.moveTo(30, 30);
    ctx.lineTo(120, 60);
    ctx.lineTo(30, 110);
    ctx.stroke();
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170822.55916260802642509535977814876115:50001231000000:2800:7CE8CC58ACBAF1AB333534C0A08F5AB287FD2100B20375A1EED5B5E0F0EF86B3.png)

### miterLimit

 支持设备PhonePC/2in1TabletTVWearable

```
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 500px; height: 500px; "></canvas>
</div>
```

```
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.lineWidth =14;
    ctx.lineJoin = 'miter';
    ctx.miterLimit = 3;
    ctx.moveTo(30, 30);
    ctx.lineTo(120, 60);
    ctx.lineTo(30, 70);
    ctx.stroke();
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170822.87283978740047624476740288445878:50001231000000:2800:51842B8174B3BC004E1A4F360B793C29C17E28303F731436CF7ABFFC329637FA.png)

### font

 支持设备PhonePC/2in1TabletTVWearable

```
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
</div>
```

```
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.font = '30px sans-serif';
    ctx.fillText("Hello World", 20, 60);
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170822.89348273779524501888623176848187:50001231000000:2800:C43A254813EB9CAA54C1DCAFC7265F5919820BBDC420E0BF73D24F775BFDBB8C.png)

### textAlign

 支持设备PhonePC/2in1TabletTVWearable

```
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
</div>
```

```
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.strokeStyle = '#0000ff';
    ctx.moveTo(140, 10);
    ctx.lineTo(140, 160);
    ctx.stroke();
    ctx.font = '18px sans-serif';
    // Show the different textAlign values
    ctx.textAlign = 'start';
    ctx.fillText('textAlign=start', 140, 60);
    ctx.textAlign = 'end';
    ctx.fillText('textAlign=end', 140, 80);
    ctx.textAlign = 'left';
    ctx.fillText('textAlign=left', 140, 100);
    ctx.textAlign = 'center';
    ctx.fillText('textAlign=center',140, 120);
    ctx.textAlign = 'right';
    ctx.fillText('textAlign=right',140, 140);
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170822.23645632272050222825635427744914:50001231000000:2800:AB84F0714A292E0397C911F1F1C7231758F7794738D4CBA6CFB84F9435D0369E.png)

### textBaseline

 支持设备PhonePC/2in1TabletTVWearable

```
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 500px; height: 500px; "></canvas>
</div>
```

```
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.strokeStyle = '#0000ff';
    ctx.moveTo(0, 120);
    ctx.lineTo(400, 120);
    ctx.stroke();
    ctx.font = '20px sans-serif';
    ctx.textBaseline = 'top';
    ctx.fillText('Top', 10, 120);
    ctx.textBaseline = 'bottom';
    ctx.fillText('Bottom', 55, 120);
    ctx.textBaseline = 'middle';
    ctx.fillText('Middle', 125, 120);
    ctx.textBaseline = 'alphabetic';
    ctx.fillText('Alphabetic', 195, 120);
    ctx.textBaseline = 'hanging';
    ctx.fillText('Hanging', 295, 120);
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170822.34469437485048202771453773174696:50001231000000:2800:3142F2B76945169B0DA3C19FB86527BAD0024B3563ED781C343684C005D151E2.png)

### globalAlpha

 支持设备PhonePC/2in1TabletTVWearable

```
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
</div>
```

```
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.fillStyle = 'rgb(255,0,0)';
    ctx.fillRect(0, 0, 50, 50);
    ctx.globalAlpha = 0.4;
    ctx.fillStyle = 'rgb(0,0,255)';
    ctx.fillRect(50, 50, 50, 50);

  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170822.49095208041643867574772887862591:50001231000000:2800:6DF17063A4479F89A0C0E1318947C9A8AA3E804F723E18FAD66F2D66152DF744.png)

### lineDashOffset

 支持设备PhonePC/2in1TabletTVWearable

```
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px; background-color: #ffff00;"></canvas>
</div>
```

```
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.arc(100, 75, 50, 0, 6.28);
    ctx.setLineDash([10,20]);
    ctx.lineDashOffset = 10.0;
    ctx.stroke();
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170822.53809827540118970860265302865751:50001231000000:2800:3D0BB215AB38CB286F420A36E2E5922C633A006ED3E1A83C121A0CFC154FB642.png)

### globalCompositeOperation

 支持设备PhonePC/2in1TabletTVWearable

类型字段说明。

  展开

| 值 | 描述 |
| --- | --- |
| source-over | 在现有绘制内容上显示新绘制内容，属于默认值。 |
| source-atop | 在现有绘制内容顶部显示新绘制内容。 |
| source-in | 在现有绘制内容中显示新绘制内容。 |
| source-out | 在现有绘制内容之外显示新绘制内容。 |
| destination-over | 在新绘制内容上方显示现有绘制内容。 |
| destination-atop | 在新绘制内容顶部显示现有绘制内容。 |
| destination-in | 在新绘制内容中显示现有绘制内容。 |
| destination-out | 在新绘制内容外显示现有绘制内容。 |
| lighter | 显示新绘制内容和现有绘制内容。 |
| copy | 显示新绘制内容而忽略现有绘制内容。 |
| xor | 使用异或操作对新绘制内容与现有绘制内容进行融合。 |

**示例：**

```
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
</div>
```

```
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.fillStyle = 'rgb(255,0,0)';
    ctx.fillRect(20, 20, 50, 50);
    ctx.globalCompositeOperation = 'source-over';
    ctx.fillStyle = 'rgb(0,0,255)';
    ctx.fillRect(50, 50, 50, 50);
    // Start drawing second example
    ctx.fillStyle = 'rgb(255,0,0)';
    ctx.fillRect(120, 20, 50, 50);
    ctx.globalCompositeOperation = 'destination-over';
    ctx.fillStyle = 'rgb(0,0,255)';
    ctx.fillRect(150, 50, 50, 50);
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170822.08307500491215707490084246796645:50001231000000:2800:9920716B90F22BC0FB4E5E41D8A71A9DEB54657A088029B11511D31F4AE67A5A.png)

示例中，新绘制内容是蓝色矩形，现有绘制内容是红色矩形。

### shadowBlur

 支持设备PhonePC/2in1TabletTVWearable

```
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
</div>
```

```
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.shadowBlur = 30;
    ctx.shadowColor = 'rgb(0,0,0)';
    ctx.fillStyle = 'rgb(255,0,0)';
    ctx.fillRect(20, 20, 100, 80);
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170822.34653043722629570716662822850732:50001231000000:2800:7B06E66652FC2818C6B9918CCC4B2EC5F2243A2141BDCAA7CAF846BD2A3430B2.png)

### shadowColor

 支持设备PhonePC/2in1TabletTVWearable

```
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px;"></canvas>
</div>
```

```
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.shadowBlur = 30;
    ctx.shadowColor = 'rgb(0,0,255)';
    ctx.fillStyle = 'rgb(255,0,0)';
    ctx.fillRect(30, 30, 100, 100);
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170822.56142049416435818700164206376179:50001231000000:2800:8E744441832F54A72CB34AD1485069A1A619E55AC757B4973669E329AE7F8E8B.png)

### shadowOffsetX

 支持设备PhonePC/2in1TabletTVWearable

```
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px;"></canvas>
</div>
```

```
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.shadowBlur = 10;
    ctx.shadowOffsetX = 20;
    ctx.shadowColor = 'rgb(0,0,0)';
    ctx.fillStyle = 'rgb(255,0,0)';
    ctx.fillRect(20, 20, 100, 80);
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170822.04438796256310655457303516476473:50001231000000:2800:D96B3BC5FCE41A5085234CFF0B9C8408E1EE7875829847DE2DA0C731C76D0D63.png)

### shadowOffsetY

 支持设备PhonePC/2in1TabletTVWearable

```
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
</div>
```

```
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.shadowBlur = 10;
    ctx.shadowOffsetY = 20;
    ctx.shadowColor = 'rgb(0,0,0)';
    ctx.fillStyle = 'rgb(255,0,0)';
    ctx.fillRect(30, 30, 100, 100);
 }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170823.66335185886238752334571551801025:50001231000000:2800:4809EE0B6D4A5FEBC5F3E580781D0D5B8C5AACA857FF39D07AEB5EC9CEA92F63.png)

### imageSmoothingEnabled

 支持设备PhonePC/2in1TabletTVWearable

```
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
</div>
```

```
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    var img = new Image();
    // 'common/image/example.jpg'需要替换为开发者所需的图像资源文件
    img.src = 'common/image/example.jpg';
    img.onload = function() {
    ctx.imageSmoothingEnabled = false;
    ctx.drawImage(img, 0, 0, 400, 200);
    };
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170823.03170290114014340668977088778046:50001231000000:2800:D312BD43CE8B8CF5C712EDB20C72C7724A07DF4F89AE125C6E4C218229F8CAA4.png)

## 方法

 支持设备PhonePC/2in1TabletTVWearable  

### fillRect

 支持设备PhonePC/2in1TabletTVWearable

fillRect(x: number, y: number, width:number, height: number): void

填充一个矩形。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 指定矩形左上角点的x坐标。 单位：vp |
| y | number | 是 | 指定矩形左上角点的y坐标。 单位：vp |
| width | number | 是 | 指定矩形的宽度。 单位：vp |
| height | number | 是 | 指定矩形的高度。 单位：vp |

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
    ctx.fillRect(20, 20, 200, 150);
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170823.12179227232098121128073136208181:50001231000000:2800:FF9034AD4A1CB28449CA9390E4783F9B583F67C073BC3A9C1B845F670B0C0921.png)

### clearRect

 支持设备PhonePC/2in1TabletTVWearable

clearRect(x: number, y: number, width:number, height: number): void

删除指定区域内的绘制内容。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 指定矩形上的左上角x坐标。 单位：vp |
| y | number | 是 | 指定矩形上的左上角y坐标。 单位：vp |
| width | number | 是 | 指定矩形的宽度。 单位：vp |
| height | number | 是 | 指定矩形的高度。 单位：vp |

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
    ctx.fillStyle = 'rgb(0,0,255)';
    ctx.fillRect(100, 100, 200, 200);
    ctx.clearRect(110, 110, 80, 50);
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170823.43863677909489870680466809620826:50001231000000:2800:095E6E1EFB4B5B32DDE709FAC545AB4349C250D8AA0C088C6B4089BED67E54B3.png)

### strokeRect

 支持设备PhonePC/2in1TabletTVWearable

strokeRect(x: number, y: number, width:number, height: number): void

绘制具有边框的矩形，矩形内部不填充。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 指定矩形的左上角x坐标。 单位：vp |
| y | number | 是 | 指定矩形的左上角y坐标。 单位：vp |
| width | number | 是 | 指定矩形的宽度。 单位：vp |
| height | number | 是 | 指定矩形的高度。 单位：vp |

**示例：**

```
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 500px; height: 500px; "></canvas>
</div>
```

```
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.strokeRect(100, 100, 200, 150);
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170823.83706067166840160907573679693005:50001231000000:2800:4A28E50A749ECD18F19E99C6946E4339CD69C0CD32024580B0AB54E78F8A8A8B.png)

### fillText

 支持设备PhonePC/2in1TabletTVWearable

fillText(text: string, x: number, y: number): void

绘制填充类文本。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | string | 是 | 需要绘制的文本内容。 |
| x | number | 是 | 需要绘制的文本的左下角x坐标。 单位：vp |
| y | number | 是 | 需要绘制的文本的左下角y坐标。 单位：vp |

**示例：**

```
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
</div>
```

```
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.font = '35px sans-serif';
    ctx.fillText("Hello World!", 10, 60);
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170823.79855318760731020045195722131231:50001231000000:2800:620552025532030F4406D1207EFF8D8169582853F9D5DF505168F133152C55CD.png)

### strokeText

 支持设备PhonePC/2in1TabletTVWearable

strokeText(text: string, x: number, y: number): void

绘制描边类文本。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | string | 是 | 需要绘制的文本内容。 |
| x | number | 是 | 需要绘制的文本的左下角x坐标。 单位：vp |
| y | number | 是 | 需要绘制的文本的左下角y坐标。 单位：vp |

**示例：**

```
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
</div>
```

```
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.font = '25px sans-serif';
    ctx.strokeText("Hello World!", 10, 60);
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170823.79391816465908684990557740632009:50001231000000:2800:2147F9E0FB797C2FDD644AEFB1F3FE714699D6DA4FEF2C46D366BB6D023A1420.png)

### measureText

 支持设备PhonePC/2in1TabletTVWearable

measureText(text: string): TextMetrics

该方法返回一个文本测算的对象，通过该对象可以获取指定文本的宽度值。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | string | 是 | 需要进行测量的文本。 |

**返回值：**

  展开

| 类型 | 说明 |
| --- | --- |
| TextMetrics | 包含指定字体的宽度，该宽度可以通过TextMetrics.width来获取。 |

**示例：**

```
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px;"></canvas>
</div>
```

```
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.font = '20px sans-serif';
    var txt = 'Hello World';
    ctx.fillText("width:" + ctx.measureText(txt).width, 20, 60);
    ctx.fillText(txt, 20, 110);
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170823.76035536941939414151636917666390:50001231000000:2800:C0B3182EBB71384875754F004FACA996B5934AA291D63EB4AC243FC7DCCCC8D7.png)

### stroke

 支持设备PhonePC/2in1TabletTVWearable

stroke(): void

进行边框绘制操作。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
</div>
```

```
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.moveTo(25, 25);
    ctx.lineTo(25, 250);
    ctx.lineWidth = '6';
    ctx.strokeStyle = 'rgb(0,0,255)';
    ctx.stroke();
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170823.20344519010342748728863890087268:50001231000000:2800:15C64ACFE1C5F8F385CF35F6AC49A86046BD1F78E7D086518AA8BB2992C5D3AD.png)

### beginPath

 支持设备PhonePC/2in1TabletTVWearable

beginPath(): void

创建一个新的绘制路径。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 500px; height: 500px; "></canvas>
</div>
```

```
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.beginPath();
    ctx.lineWidth = '6';
    ctx.strokeStyle = '#0000ff';
    ctx.moveTo(15, 80);
    ctx.lineTo(280, 80);
    ctx.stroke();
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170823.34284156921982836178085524136227:50001231000000:2800:8E9E2585A3AE185649F098B4E3E102E38BEB5304F5AB2394ED893A33EB99A2AB.png)

### moveTo

 支持设备PhonePC/2in1TabletTVWearable

moveTo(x: number, y: number): void

路径从当前点移动到指定点。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 指定位置的x坐标。 单位：vp |
| y | number | 是 | 指定位置的y坐标。 单位：vp |

**示例：**

```
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
</div>
```

```
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.beginPath();
    ctx.moveTo(10, 10);
    ctx.lineTo(280, 160);
    ctx.stroke();
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170823.41742809420457423947144886287177:50001231000000:2800:8344B71F3B58DE11074F37B11922C065C36150C117DA933A8F2B66DC7FFCFB3D.png)

### lineTo

 支持设备PhonePC/2in1TabletTVWearable

lineTo(x: number, y: number): void

从当前点到指定点进行路径连接。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 指定位置的x坐标。 单位：vp |
| y | number | 是 | 指定位置的y坐标。 单位：vp |

**示例：**

```
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
</div>
```

```
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.beginPath();
    ctx.moveTo(10, 10);
    ctx.lineTo(280, 160);
    ctx.stroke();
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170823.99252245497051557791374507791313:50001231000000:2800:BD3014BE5FE793080BA8E4AFA69E970BAD276B0A01BAF3E251FDFA26D033742F.png)

### closePath

 支持设备PhonePC/2in1TabletTVWearable

closePath(): void

结束当前路径形成一个封闭路径。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px;"></canvas>
</div>
```

```
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.beginPath();
    ctx.moveTo(30, 30);
    ctx.lineTo(110, 30);
    ctx.lineTo(70, 90);
    ctx.closePath();
    ctx.stroke();
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170823.63237265328853352104543835565377:50001231000000:2800:B441374FB1F30A03C0131CD77D5793B3E9E5EE32B1FB1BD4AF5684B10ECD62B0.png)

### createPattern

 支持设备PhonePC/2in1TabletTVWearable

createPattern(image: Image, repetition: string): Object

通过指定图像和重复方式创建图片填充的模板。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| image | Image | 是 | 图源对象，具体参考 Image对象 。 |
| repetition | string | 是 | 设置图像重复的方式，取值为：'repeat'、'repeat-x'、 'repeat-y'、'no-repeat'。 |

**返回值：**

  展开

| 类型 | 说明 |
| --- | --- |
| Object | 指定图像填充的Pattern对象。 |

**示例：**

```
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 1000px; height: 1000px;"></canvas>
</div>
```

```
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    var img = new Image();
    // 'common/images/example.jpg'需要替换为开发者所需的图像资源文件
    img.src = 'common/images/example.jpg';
    var pat = ctx.createPattern(img, 'repeat');
    ctx.fillStyle = pat;
    ctx.fillRect(0, 0, 500, 500);
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170823.82739555670361145688310008635844:50001231000000:2800:9575D957662ADBBFB0CF15A4E0E7FFC2C373E55A9C5846D9960AF065C804B6DE.png)

### bezierCurveTo

 支持设备PhonePC/2in1TabletTVWearable

bezierCurveTo(cp1x: number, cp1y: number, cp2x: number, cp2y: number, x: number, y: number): void

创建三次贝塞尔曲线的路径。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| cp1x | number | 是 | 第一个贝塞尔参数的x坐标值。 单位：vp |
| cp1y | number | 是 | 第一个贝塞尔参数的y坐标值。 单位：vp |
| cp2x | number | 是 | 第二个贝塞尔参数的x坐标值。 单位：vp |
| cp2y | number | 是 | 第二个贝塞尔参数的y坐标值。 单位：vp |
| x | number | 是 | 路径结束时的x坐标值。 单位：vp |
| y | number | 是 | 路径结束时的y坐标值。 单位：vp |

**示例：**

```
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px;"></canvas>
</div>
```

```
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.beginPath();
    ctx.moveTo(10, 10);
    ctx.bezierCurveTo(20, 100, 200, 100, 200, 20);
    ctx.stroke();
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170823.86682627554946523416589587350634:50001231000000:2800:3C8F601BFF32B6C789F544BE16D5E3040167A51E33A35187272C3B33F70BE336.png)

### quadraticCurveTo

 支持设备PhonePC/2in1TabletTVWearable

quadraticCurveTo(cpx: number, cpy: number, x: number, y: number): void

创建二次贝塞尔曲线的路径。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| cpx | number | 是 | 贝塞尔参数的x坐标值。 单位：vp |
| cpy | number | 是 | 贝塞尔参数的y坐标值。 单位：vp |
| x | number | 是 | 路径结束时的x坐标值。 单位：vp |
| y | number | 是 | 路径结束时的y坐标值。 单位：vp |

**示例：**

```
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
</div>
```

```
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.beginPath();
    ctx.moveTo(20, 20);
    ctx.quadraticCurveTo(100, 100, 200, 20);
    ctx.stroke();
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170823.40647086110502719747071464762122:50001231000000:2800:04472B84F9AC62166886EB24B47C42B6DA4A54CE03A06417549A82A1E27A430E.png)

### arc

 支持设备PhonePC/2in1TabletTVWearable

arc(x: number, y: number, radius: number, startAngle: number, endAngle: number, counterclockwise?: boolean): void

绘制弧线路径。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 弧线圆心的x坐标值。 单位：vp |
| y | number | 是 | 弧线圆心的y坐标值。 单位：vp |
| radius | number | 是 | 弧线的圆半径。 单位：vp |
| startAngle | number | 是 | 弧线的起始弧度。 单位：vp |
| endAngle | number | 是 | 弧线的终止弧度。 单位：vp |
| counterclockwise | boolean | 否 | 是否逆时针绘制圆弧，true为逆时针，false为顺时针。 默认值：false |

**示例：**

```
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px;"></canvas>
</div>
```

```
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.beginPath();
    ctx.arc(100, 75, 50, 0, 6.28);
    ctx.stroke();
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170823.31700563764175541665168616704959:50001231000000:2800:5A688E8EA74A65BB4F79E0C39C908730BE2C5C95354199868D18D9DD27360891.png)

### arcTo

 支持设备PhonePC/2in1TabletTVWearable

arcTo(x1: number, y1: number, x2: number, y2: number, radius: number): void

依据圆弧经过的点和圆弧半径创建圆弧路径。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x1 | number | 是 | 圆弧经过的第一个点的x坐标值。 单位：vp |
| y1 | number | 是 | 圆弧经过的第一个点的y坐标值。 单位：vp |
| x2 | number | 是 | 圆弧经过的第二个点的x坐标值。 单位：vp |
| y2 | number | 是 | 圆弧经过的第二个点的y坐标值。 单位：vp |
| radius | number | 是 | 圆弧的圆半径值。 单位：vp |

**示例：**

```
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px;"></canvas>
</div>
```

```
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.moveTo(100, 20);
    ctx.arcTo(150, 20, 150, 70, 50); // Create an arc
    ctx.stroke();
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170823.32393543815739639443434645029187:50001231000000:2800:480EE0553BE509D528787EDE670A86EC544D0C1DF45CCCE33FC5199AD9163C8A.png)

### ellipse

 支持设备PhonePC/2in1TabletTVWearable

ellipse(x: number, y: number, radiusX: number, radiusY: number, rotation: number, startAngle: number, endAngle: number, counterclockwise?: number): void

在规定的矩形区域绘制一个椭圆。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 椭圆圆心的x轴坐标。 单位：vp |
| y | number | 是 | 椭圆圆心的y轴坐标。 单位：vp |
| radiusX | number | 是 | 椭圆x轴的半径长度。 单位：vp |
| radiusY | number | 是 | 椭圆y轴的半径长度。 单位：vp |
| rotation | number | 是 | 椭圆的旋转角度，单位为弧度。 单位：vp |
| startAngle | number | 是 | 椭圆绘制的起始点角度，以弧度表示。 单位：vp |
| endAngle | number | 是 | 椭圆绘制的结束点角度，以弧度表示。 单位：vp |
| counterclockwise | number | 否 | 是否以逆时针方向绘制椭圆，0为顺时针，1为逆时针。其它数值均按默认值处理。 单位：vp 默认值：0 |

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
    ctx.beginPath();
    ctx.ellipse(200, 200, 50, 100, Math.PI * 0.25, Math.PI * 0.5, Math.PI, 1);
    ctx.stroke();
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170823.40807918171682496852816826924236:50001231000000:2800:B2CDF2E71FBE97971CA940F4872133DD384FDC93811046D7BBF9ED4F6AA385D3.png)

### rect

 支持设备PhonePC/2in1TabletTVWearable

rect(x: number, y: number, width: number, height: number): void

创建矩形路径。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 指定矩形的左上角x坐标值。 单位：vp |
| y | number | 是 | 指定矩形的左上角y坐标值。 单位：vp |
| width | number | 是 | 指定矩形的宽度。 单位：vp |
| height | number | 是 | 指定矩形的高度。 单位：vp |

**示例：**

```
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
</div>
```

```
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.rect(20, 20, 100, 100); // Create a 100*100 rectangle at (20, 20)
    ctx.stroke(); // Draw it
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170824.81971244328255809883879149129870:50001231000000:2800:FB1D07E4F136FBD41BF69F82A11780A7EFB625C3411C4EF9338631E750CED124.png)

### fill

 支持设备PhonePC/2in1TabletTVWearable

fill(): void

对封闭路径进行填充。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px;"></canvas>
</div>
```

```
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.rect(20, 20, 100, 100); // Create a 100*100 rectangle at (20, 20)
    ctx.fill(); // Draw it in default setting
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170824.26345221756410275859061034576225:50001231000000:2800:1DC8825ACDBB02E0C70EA802C54F9EACB728632053B671DDC203A1830B59B322.png)

### clip

 支持设备PhonePC/2in1TabletTVWearable

clip(): void

设置当前路径为剪切路径。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 500px; height: 500px;"></canvas>
</div>
```

```
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.rect(100, 100, 200, 200);
    ctx.stroke();
    ctx.clip();
    // Draw red rectangle after clip
    ctx.fillStyle = "rgb(255,0,0)";
    ctx.fillRect(100, 100, 150, 150);
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170824.00494809352132610153367214407468:50001231000000:2800:B033CD6AC5051D72D1515F7F7E0EACDCF77950D99C9A7BAE69A283B23A165432.png)

### rotate

 支持设备PhonePC/2in1TabletTVWearable

rotate(rotate: number): void

针对当前坐标轴进行顺时针旋转。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| rotate | number | 是 | 设置顺时针旋转的弧度值，可以通过Math.PI / 180将角度转换为弧度值。 单位：vp |

**示例：**

```
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px;"></canvas>
</div>
```

```
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.rotate(45 * Math.PI / 180); // Rotate the rectangle 45 degrees
    ctx.fillRect(70, 20, 50, 50);
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170824.24705531122590424174822907284739:50001231000000:2800:4086A1E62E6406AF36DC36DADD13C21139FD38F0A35FD73CD2D8A67D6C9558C2.png)

### scale

 支持设备PhonePC/2in1TabletTVWearable

scale(x: number, y: number): void

设置canvas画布的缩放变换属性，后续的绘制操作将按照缩放比例进行缩放。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 设置水平方向的缩放值。 单位：vp |
| y | number | 是 | 设置垂直方向的缩放值。 单位：vp |

**示例：**

```
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px;"></canvas>
</div>
```

```
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.strokeRect(10, 10, 25, 25);
    ctx.scale(2, 2);// Scale to 200%
    ctx.strokeRect(10, 10, 25, 25);
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170824.25168423772449420601071905855767:50001231000000:2800:B45829C6A6E799A9F504E0EC7AEE904255FCC24C41AAB02049E0A7F5B41A488E.png)

### transform

 支持设备PhonePC/2in1TabletTVWearable

transform(scaleX: number, skewX: number, skewY: number, scale: number, translateX: number, translateY: number): void

transform方法对应一个变换矩阵，想对一个图形进行变化的时候，只要设置此变换矩阵相应的参数，对图形的各个定点的坐标分别乘以这个矩阵，就能得到新的定点的坐标。矩阵变换效果可叠加。

 说明 

变换后的坐标计算方式（x和y为变换前坐标，x'和y'为变换后坐标）：

- x' = scaleX * x + skewY * y + translateX
- y' = skewX * x + scaleY * y + translateY

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scaleX | number | 是 | 指定水平缩放值。 单位：vp |
| skewX | number | 是 | 指定水平倾斜值。 单位：vp |
| skewY | number | 是 | 指定垂直倾斜值。 单位：vp |
| scaleY | number | 是 | 指定垂直缩放值。 单位：vp |
| translateX | number | 是 | 指定水平移动值。 单位：vp |
| translateY | number | 是 | 指定垂直移动值。 单位：vp |

**示例：**

```
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px;"></canvas>
</div>
```

```
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.fillStyle = 'rgb(0,0,0)';
    ctx.fillRect(0, 0, 100, 100);
    ctx.transform(1, 0.5, -0.5, 1, 10, 10);
    ctx.fillStyle = 'rgb(255,0,0)';
    ctx.fillRect(0, 0, 100, 100);
    ctx.transform(1, 0.5, -0.5, 1, 10, 10);
    ctx.fillStyle = 'rgb(0,0,255)';
    ctx.fillRect(0, 0, 100, 100);
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170824.51937234866919145503608950686724:50001231000000:2800:5936D425CCBC418454B87A8DA5F7D46E0DA13222BEBAF279EF8D7BF3162CD62D.png)

### setTransform

 支持设备PhonePC/2in1TabletTVWearable

setTransform(scaleX: number, skewX: number, skewY: number, scale: number, translateX: number, translateY: number): void

setTransform方法使用的参数和transform()方法相同，但setTransform()方法会重置现有的变换矩阵并创建新的变换矩阵。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scaleX | number | 是 | 指定水平缩放值。 单位：vp |
| skewX | number | 是 | 指定水平倾斜值。 单位：vp |
| skewY | number | 是 | 指定垂直倾斜值。 单位：vp |
| scaleY | number | 是 | 指定垂直缩放值。 单位：vp |
| translateX | number | 是 | 指定水平移动值。 单位：vp |
| translateY | number | 是 | 指定垂直移动值。 单位：vp |

**示例：**

```
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px;"></canvas>
</div>
```

```
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.fillStyle = 'rgb(255,0,0)';
    ctx.fillRect(0, 0, 100, 100);
    ctx.setTransform(1,0.5, -0.5, 1, 10, 10);
    ctx.fillStyle = 'rgb(0,0,255)';
    ctx.fillRect(0, 0, 100, 100);
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170824.98261104354580804133161841913313:50001231000000:2800:9BB93343357A9195A6BE2D30778CE51579E22939E3E1BBCD3AB0FD0DFE8D47AE.png)

### translate

 支持设备PhonePC/2in1TabletTVWearable

translate(x: number, y: number): void

移动当前坐标系的原点。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 设置水平平移量。 单位：vp |
| y | number | 是 | 设置竖直平移量。 单位：vp |

**示例：**

```
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px;"></canvas>
</div>
```

```
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.fillRect(10, 10, 50, 50);
    ctx.translate(70, 70);
    ctx.fillRect(10, 10, 50, 50);
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170824.86851747566591271855829637905602:50001231000000:2800:8B367E3A607302AE528CBE525A90B525CCFFD04D6AADB4C9EE874881F933889B.png)

### createPath2D 6+

 支持设备PhonePC/2in1TabletTVWearable

createPath2D(path: Path2D, cmds: string): Path2D

创建一个Path2D对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | Path2D | 是 | Path2D对象。 |
| cmds | string | 是 | SVG的Path描述字符串。 |

**返回值：**

[Path2D对象](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-canvas-path2d)

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
    var path1 = ctx.createPath2D();
    path1.moveTo(100, 100);
    path1.lineTo(200, 100);
    path1.lineTo(100, 200);
    path1.closePath();
    ctx.stroke(path1);
    var path2 = ctx.createPath2D("M150 150 L50 250 L250 250 Z");
    ctx.stroke(path2);
    var path3 = ctx.createPath2D(path2);
    ctx.stroke(path3);
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170824.66035995158112603060103332660974:50001231000000:2800:60689F6C81F0490A1A2EF4EF4E415B2AA46312D83A46A5AD3FDAB4FCBE8E14DF.png)

### drawImage

 支持设备PhonePC/2in1TabletTVWearable

drawImage(image: Image | PixelMap, sx: number, sy: number, sWidth: number, sHeight: number, dx: number, dy: number, dWidth: number, dHeight: number):void

进行图像绘制。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| image | Image \| PixelMap 9+ | 是 | 图片资源，请参考 Image对象 或 PixelMap对象 。 |
| sx | number | 是 | 裁切源图像时距离源图像左上角的x坐标值。 单位：vp |
| sy | number | 是 | 裁切源图像时距离源图像左上角的y坐标值。 单位：vp |
| sWidth | number | 是 | 裁切源图像时需要裁切的宽度。 单位：vp |
| sHeight | number | 是 | 裁切源图像时需要裁切的高度。 单位：vp |
| dx | number | 是 | 绘制区域左上角在x轴的位置。 单位：vp |
| dy | number | 是 | 绘制区域左上角在y 轴的位置。 单位：vp |
| dWidth | number | 是 | 绘制区域的宽度。 单位：vp |
| dHeight | number | 是 | 绘制区域的高度。 单位：vp |

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
    var test = this.$refs.canvas;
    var ctx = test.getContext('2d');
    var img = new Image();
    // 'common/image/test.jpg'需要替换为开发者所需的图像资源文件
    img.src = 'common/image/test.jpg';
    ctx.drawImage(img, 0, 0, 200, 200, 10, 10, 200, 200);
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170824.06360537962179940438746573839460:50001231000000:2800:C0008BC801ACF92EF25473BBD6E30386BD5F422B322B71914F19D3810F28D303.png)

### restore

 支持设备PhonePC/2in1TabletTVWearable

restore(): void

对保存的绘图上下文进行恢复。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px; background-color: #ffff00;"></canvas>
</div>
```

```
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.restore();
  }
}
```

### save

 支持设备PhonePC/2in1TabletTVWearable

save(): void

对当前的绘图上下文进行保存。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px; background-color: #ffff00;"></canvas>
</div>
```

```
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.save();
  }
}
```

### createLinearGradient 6+

 支持设备PhonePC/2in1TabletTVWearable

createLinearGradient(x0: number, y0: number, x1: number, y1: number): Object

创建一个线性渐变色，返回CanvasGradient对象，请参考[CanvasGradient对象](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-canvas-canvasgradient)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x0 | number | 是 | 起点的x轴坐标。 单位：vp |
| y0 | number | 是 | 起点的y轴坐标。 单位：vp |
| x1 | number | 是 | 终点的x轴坐标。 单位：vp |
| y1 | number | 是 | 终点的y轴坐标。 单位：vp |

**返回值：**

  展开

| 类型 | 说明 |
| --- | --- |
| Object | 返回创建的CanvasGradient对象。 |

**示例：**

```
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 500px; height: 500px; background-color: #ffff00;"></canvas>
  <input type="button" style="width: 180px; height: 60px;" value="fillStyle" onclick="handleClick" />
</div>
```

```
// xxx.js
export default {
  handleClick() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    // Linear gradient: start(50,0) end(300,100)
    var gradient = ctx.createLinearGradient(50,0, 300,100);
    // Add three color stops
    gradient.addColorStop(0.0, '#ff0000');
    gradient.addColorStop(0.5, '#ffffff');
    gradient.addColorStop(1.0, '#00ff00');
    // Set the fill style and draw a rectangle
    ctx.fillStyle = gradient;
    ctx.fillRect(0, 0, 500, 500);
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170824.86762551208153558381494220773499:50001231000000:2800:4F4E708FADB987D51F34A3919A66B77ED5D123915CE1402CCC535588B3430262.png)

### createRadialGradient 6+

 支持设备PhonePC/2in1TabletTVWearable

createRadialGradient(x0: number, y0: number, r0: number, x1: number, y1: number, r1: number): Object

创建一个径向渐变色，返回CanvasGradient对象，请参考CanvasGradient。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x0 | number | 是 | 起始圆的x轴坐标。 单位：vp |
| y0 | number | 是 | 起始圆的y轴坐标。 单位：vp |
| r0 | number | 是 | 起始圆的半径。必须是非负且有限的。 单位：vp |
| x1 | number | 是 | 终点圆的x轴坐标。 单位：vp |
| y1 | number | 是 | 终点圆的y轴坐标。 单位：vp |
| r1 | number | 是 | 终点圆的半径。必须为非负且有限的。 单位：vp |

**返回值：**

  展开

| 类型 | 说明 |
| --- | --- |
| Object | 返回创建的CanvasGradient对象。 |

**示例：**

```
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 500px; height: 500px; background-color: #ffff00;"></canvas>
  <input type="button" style="width: 180px; height: 60px;" value="fillStyle" onclick="handleClick" />
</div>
```

```
// xxx.js
export default {
  handleClick() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    // Radial gradient: inner circle(200,200,r:50) outer circle(200,200,r:200)
    var gradient = ctx.createRadialGradient(200,200,50, 200,200,200);
    // Add three color stops
    gradient.addColorStop(0.0, '#ff0000');
    gradient.addColorStop(0.5, '#ffffff');
    gradient.addColorStop(1.0, '#00ff00');
    // Set the fill style and draw a rectangle
    ctx.fillStyle = gradient;
    ctx.fillRect(0, 0, 500, 500);
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170824.97774692717030665217005539801730:50001231000000:2800:CF89A724A5FB04B796B3856AD5E531C7A32D93B9527406A5711470CB5216649D.png)

### createImageData

 支持设备PhonePC/2in1TabletTVWearable

createImageData(width: number, height: number): ImageData

创建新的、空白的、指定大小的ImageData对象，请参考[ImageData对象](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-canvas-imagedata)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| width | number | 是 | ImageData的宽度。 单位：vp |
| height | number | 是 | ImageData的高度。 单位：vp |

**返回值：**

  展开

| 类型 | 说明 |
| --- | --- |
| ImageData | 返回创建的ImageData对象。 |

**示例：**

```
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px; background-color: #ffff00;"></canvas>
</div>
```

```
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    var imageData = ctx.createImageData(50, 100);  // Create ImageData with 50px width and 100px height
  }
}
```

### createImageData

 支持设备PhonePC/2in1TabletTVWearable

createImageData(imageData: ImageData): ImageData

根据一个现有的ImageData对象，重新创建一个宽、高相同但不会复制图像数据的ImageData对象，请参考[ImageData对象](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-canvas-imagedata)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| imageData | ImageData | 是 | 复制现有的ImageData对象。 |

**返回值：**

  展开

| 类型 | 说明 |
| --- | --- |
| ImageData | 返回创建的ImageData对象。 |

**示例：**

```
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px; background-color: #ffff00;"></canvas>
</div>
```

```
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    var imageData = ctx.createImageData(50, 100);  // Create ImageData with 50px width and 100px height
    var newImageData = ctx.createImageData(imageData);  // Create ImageData using the input imageData
  }
}
```

### getImageData

 支持设备PhonePC/2in1TabletTVWearable

getImageData(sx: number, sy: number, sw: number, sh: number): ImageData

以当前canvas指定区域内的像素创建[ImageData对象](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-canvas-imagedata)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sx | number | 是 | 需要输出的区域的左上角x坐标。 单位：vp |
| sy | number | 是 | 需要输出的区域的左上角y坐标。 单位：vp |
| sw | number | 是 | 需要输出的区域的宽度。 单位：vp |
| sh | number | 是 | 需要输出的区域的高度。 单位：vp |

**返回值：**

  展开

| 类型 | 说明 |
| --- | --- |
| ImageData | 返回包含指定区域像素的ImageData对象。 |

**示例：**

```
<!-- xxx.hml -->
<div>
  <canvas id="getImageData" style="width: 200px; height: 150px; background-color: #ffff00;"></canvas>
</div>
```

```
// xxx.js
export default {
  onShow() {
    const test = this.$element('getImageData')
    const ctx = test.getContext('2d');
    var imageData = ctx.getImageData(0, 0, 280, 300);
  }
}
```

### putImageData

 支持设备PhonePC/2in1TabletTVWearable

putImageData(imageData: ImageData, dx: number, dy: number, dirtyX: number, dirtyY: number, dirtyWidth: number, dirtyHeight: number): void

使用ImageData数据裁剪后填充至新的矩形区域。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| imageData | ImageData | 是 | 包含像素值的ImageData对象。 |
| dx | number | 是 | 填充区域在x轴方向的偏移量。 单位：vp |
| dy | number | 是 | 填充区域在y轴方向的偏移量。 单位：vp |
| dirtyX | number | 是 | 源图像数据矩形裁切范围左上角距离源图像左上角的x轴偏移量。 单位：vp |
| dirtyY | number | 是 | 源图像数据矩形裁切范围左上角距离源图像左上角的y轴偏移量。 单位：vp |
| dirtyWidth | number | 是 | 源图像数据矩形裁切范围的宽度。 单位：vp |
| dirtyHeight | number | 是 | 源图像数据矩形裁切范围的高度。 单位：vp |

**示例：**

```
<!-- xxx.hml -->
<div>
  <canvas id="putImageData" style="width: 200px; height: 150px; background-color: #D5D5D5;"></canvas>
</div>
```

```
// xxx.js
export default {
    onShow() {
        const test = this.$element('putImageData')
        const ctx = test.getContext('2d');
        var imgData = ctx.createImageData(100, 100);
        for (var i = 0; i < imgData.data.length; i += 4) {
            imgData.data[i + 0] = 39;
            imgData.data[i + 1] = 135;
            imgData.data[i + 2] = 217;
            imgData.data[i + 3] = 255;
        }
        ctx.putImageData(imgData, 10, 10, 0, 0, 100, 50);
    }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170824.86550019980998983361809085023874:50001231000000:2800:A5DE0B16D30D32E9DD46190086576078BEE8974CB8884B29483D240D77838B33.png)

### putImageData

 支持设备PhonePC/2in1TabletTVWearable

putImageData(imageData: ImageData, dx: number, dy: number): void

使用ImageData数据填充新的矩形区域。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| imageData | ImageData | 是 | 包含像素值的ImageData对象。 |
| dx | number | 是 | 填充区域在x轴方向的偏移量。 单位：vp |
| dy | number | 是 | 填充区域在y轴方向的偏移量。 单位：vp |

**示例：**

```
<!-- xxx.hml -->
<div>
  <canvas id="putImageData" style="width: 200px; height: 150px; background-color: #ffff00;"></canvas>
</div>
```

```
// xxx.js
export default {
  onShow() {
    const test = this.$element('putImageData')
    const ctx = test.getContext('2d');
    var imgData = ctx.createImageData(100, 100);
    for (var i = 0; i < imgData.data.length; i += 4) {
      imgData.data[i + 0] = 255;
      imgData.data[i + 1] = 0;
      imgData.data[i + 2] = 0;
      imgData.data[i + 3] = 255;
  }
    ctx.putImageData(imgData, 10, 10);
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170824.84922215575058707043195759025601:50001231000000:2800:EE3F8C7C9350DD2E24AB5AD975614F33AC48C6E4C88714A8F3BE33764EAD4F9A.png)

### getPixelMap 9+

 支持设备PhonePC/2in1TabletTVWearable

getPixelMap(sx: number, sy: number, sw: number, sh: number): PixelMap

获取用当前canvas指定区域内的像素创建的PixelMap对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sx | number | 是 | 指定区域的左上角x坐标。 单位：vp |
| sy | number | 是 | 指定区域的左上角y坐标。 单位：vp |
| sw | number | 是 | 指定区域的宽度。 单位：vp |
| sh | number | 是 | 指定区域的高度。 单位：vp |

**返回值：**

  展开

| 类型 | 说明 |
| --- | --- |
| PixelMap | 返回包含指定区域像素的PixelMap对象。 |

**示例：**

```
<!-- xxx.hml -->
<div>
  <canvas id="canvasId" style="width: 200px; height: 150px; background-color: #ffff00;"></canvas>
</div>
```

```
// xxx.js
export default {
  onShow() {
    const test = this.$element('canvasId')
    const ctx = test.getContext('2d');
    var pixelMap = ctx.getPixelMap(0, 0, 280, 300);
  }
}
```

### setLineDash

 支持设备PhonePC/2in1TabletTVWearable

setLineDash(segments: Array): void

设置画布的虚线样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| segments | Array | 是 | 作为数组用来描述线段如何交替和间距长度。 |

**示例：**

```
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px; background-color: #ffff00;"></canvas>
</div>
```

```
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    ctx.arc(100, 75, 50, 0, 6.28);
    ctx.setLineDash([10,20]);
    ctx.stroke();
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170824.02751496682317685398156268847073:50001231000000:2800:2B1CBEC979901AB79153F14C8A904B455BE0F4AE5D4675B8318DEA4513AB7010.png)

### getLineDash

 支持设备PhonePC/2in1TabletTVWearable

getLineDash(): Array

获得当前画布的虚线样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

  展开

| 类型 | 说明 |
| --- | --- |
| Array | 返回数组，该数组用来描述线段如何交替和间距长度。 |

**示例：**

```
<!-- xxx.hml -->
<div>
  <canvas ref="canvas" style="width: 200px; height: 150px; "></canvas>
</div>
```

```
// xxx.js
export default {
  onShow() {
    const el = this.$refs.canvas;
    const ctx = el.getContext('2d');
    var info = ctx.getLineDash();
  }
}
```

### transferFromImageBitmap 7+

 支持设备PhonePC/2in1TabletTVWearable

transferFromImageBitmap(bitmap: ImageBitmap): void

显示给定的[ImageBitmap对象](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-canvas-imagebitmap)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

  展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| bitmap | ImageBitmap | 是 | 待显示的ImageBitmap对象。 |

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
    var canvas = this.$refs.canvas.getContext('2d');
    var offscreen = new OffscreenCanvas(500,500);
    var offscreenCanvasCtx = offscreen.getContext("2d");
    offscreenCanvasCtx.fillRect(0, 0, 200, 200);

    var bitmap = offscreen.transferToImageBitmap();
    canvas.transferFromImageBitmap(bitmap);
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170824.19372248784499066711224889566316:50001231000000:2800:3519D4137B236825FE3C8F334FA5B50B53423323176F60E48BF9173CE1C841A5.png)