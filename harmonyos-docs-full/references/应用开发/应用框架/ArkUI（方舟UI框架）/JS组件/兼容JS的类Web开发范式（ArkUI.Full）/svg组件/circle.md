# circle

说明 

该组件从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

圆形形状。

## 权限列表

支持设备PhonePC/2in1TabletTVWearable

无

## 子组件

支持设备PhonePC/2in1TabletTVWearable

支持[animate](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-svg-animate)、[animateMotion](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-svg-animatemotion)、[animateTransform](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-svg-animatetransform)。

## 属性

支持设备PhonePC/2in1TabletTVWearable

支持Svg组件[通用属性](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-svg-common-attributes)和以下属性。

 展开

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| id | string | - | 否 | 组件的唯一标识。 |
| cx | <length>\|<percentage> | 0 | 否 | 设置圆心的x轴坐标。支持属性动画。 |
| cy | <length>\|<percentage> | 0 | 否 | 设置圆心的y轴坐标。支持属性动画。 |
| r | <length>\|<percentage> | 0 | 否 | 设置圆的半径。支持属性动画。 |

## 示例

支持设备PhonePC/2in1TabletTVWearable

```
<!-- xxx.hml -->
<div class="container">
  <svg fill="white" width="400" height="400">
    <circle cx="60" cy="200" r="50" stroke-width="4" fill="red" stroke="blue"></circle>
    <circle cx="180" cy="200" r="50" stroke-width="10" stroke="red" stroke-dasharray="10 5" stroke-dashoffset="3"></circle>
  </svg>
</div>
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170853.62539965560419780475504208562901:50001231000000:2800:503CC1C88D3289A7ECA2FC32B1DE169685D51915BC04194BFCEB4EFAFAA2DE23.png)