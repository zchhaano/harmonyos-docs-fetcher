# canvas组件

说明 

 从API version 4开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

提供画布组件。用于自定义绘制图形。

## 权限列表

支持设备PhonePC/2in1TabletTVWearable

无

## 子组件

支持设备PhonePC/2in1TabletTVWearable

不支持。

## 属性

支持设备PhonePC/2in1TabletTVWearable

支持[通用属性](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-common-attributes)。

## 样式

支持设备PhonePC/2in1TabletTVWearable

支持[通用样式](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-common-styles)。

## 事件

支持设备PhonePC/2in1TabletTVWearable

支持[通用事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-common-events)。

## 方法

支持设备PhonePC/2in1TabletTVWearable

除支持[通用方法](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-common-methods)外，还支持如下方法：

### getContext

支持设备PhonePC/2in1TabletTVWearable

getContext(type: '2d', options?: ContextAttrOptions): CanvasRenderingContext2D

获取canvas绘图上下文。不支持在onInit和onReady中进行调用。

**参数：**

 展开

| 参数名 | 参数类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| type | string | 是 | 设置为'2d'，返回值为2D绘制对象，该对象可用于在画布组件上绘制矩形、文本、图片等。 |
| options 6+ | ContextAttrOptions | 否 | 当前仅支持配置是否开启抗锯齿功能，默认为关闭。 |

**返回值：**

 展开

| 类型 | 说明 |
| --- | --- |
| CanvasRenderingContext2D | 用于在画布组件上绘制矩形、文本、图片等。 |

### toDataURL 6+

支持设备PhonePC/2in1TabletTVWearable

toDataURL(type?: string, quality?: number): string

生成一个包含图片展示的URL。

**参数：**

 展开

| 参数名 | 参数类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| type | string | 否 | 可选参数，用于指定图像格式，默认格式为image/png。 |
| quality | number | 否 | 在指定图片格式为image/jpeg或image/webp的情况下，可以从0到1的区间内选择图片的质量。如果超出取值范围，将会使用默认值0.92。 |

**返回值：**

 展开

| 类型 | 说明 |
| --- | --- |
| string | 图像的URL地址。 |

## ContextAttrOptions 6+

支持设备PhonePC/2in1TabletTVWearable

用于配置Canvas渲染上下文属性的选项对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

 展开

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| antialias | boolean | 否 | 是 | 是否开启抗锯齿功能。 true表示开启抗锯齿功能；false表示不开启抗锯齿功能。 默认值：false |

## 示例

支持设备PhonePC/2in1TabletTVWearable

```
<!-- xxx.hml -->
<div style="margin: 100; flex-direction: column">
  <canvas ref="canvas1" style="width: 200px; height: 150px; background-color: rgb(213, 213, 213);"></canvas>
  <input type="button" style="width: 180px; height: 60px; margin: 13;" value="fillStyle" onclick="handleClick" />
</div>
```

```
// xxx.js
export default {
  handleClick() {
    const el = this.$refs.canvas1;
    var dataURL = el.toDataURL();
    console.info(dataURL);
    // "data:image/png;base64,xxxxxxxx..."
  }
}
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170809.07440324675777619637147000143129:50001231000000:2800:156E33BBA12D6166F416663FFCCFAA347F68C2F40657386962C94A58436DFC00.png)