# CanvasGradient对象

说明 

 从API version 4开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

渐变对象。

## addColorStop

支持设备PhonePC/2in1TabletTVWearable

addColorStop(offset: number, color: string): void

设置渐变断点值，包括偏移和颜色。

**参数：**

 展开

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| offset | number | 设置渐变点距离起点的位置占总体长度的比例，范围为0到1。 |
| color | string | 设置渐变的颜色。 |

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
    const gradient = ctx.createLinearGradient(50, 0, 300, 100);
    gradient.addColorStop(0.0, '#ff0000')
    gradient.addColorStop(0.5, '#ffffff')
    gradient.addColorStop(1.0, '#00ff00')
    ctx.fillStyle = gradient
    ctx.fillRect(0, 0, 300, 300)
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170853.97636972409130507379133825288366:50001231000000:2800:6D8444724B60C9D99AC67C6C5247D7E2DDE74BC5785FDF9616286484CBC06F9A.png)