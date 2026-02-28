# ellipse

说明 

该组件从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

椭圆形状。

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
| cx | <length>\|<percentage> | 0 | 否 | 设置椭圆的x轴坐标。支持属性动画。 |
| cy | <length>\|<percentage> | 0 | 否 | 设置椭圆的y轴坐标。支持属性动画。 |
| rx | <length>\|<percentage> | 0 | 否 | 设置椭圆x轴的半径。支持属性动画。 |
| ry | <length>\|<percentage> | 0 | 否 | 设置椭圆y轴的半径。支持属性动画。 |

## 示例

支持设备PhonePC/2in1TabletTVWearable

```
<!-- xxx.hml -->
<div class="container">
  <svg fill="white" width="400" height="400">
    <ellipse cx="60" cy="200" rx="50" ry="100" stroke-width="4" fill="red" stroke="blue"></ellipse>
    <ellipse cx="220" cy="200" rx="100" ry="50" stroke-width="5" stroke="red" stroke-dasharray="10 5" stroke-dashoffset="3"></ellipse>
  </svg>
</div>
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170859.84760101444213449545939476433779:50001231000000:2800:D89E2C93E8CC6FB30E86BD6D787D1E43CED3C78C1899BB8EDE9C4AC644975AC0.png)