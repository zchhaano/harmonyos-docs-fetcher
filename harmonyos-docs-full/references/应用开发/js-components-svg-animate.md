# animate

说明 

该组件从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

设置svg组件的属性动画。

## 权限列表

支持设备PhonePC/2in1TabletTVWearable

无

## 子组件

支持设备PhonePC/2in1TabletTVWearable

不支持。

## 属性

 支持设备PhonePC/2in1TabletTVWearable展开

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| id | string | - | 否 | 组件的唯一标识。 |
| attributeName | string | - | 否 | 设置需要进行动效的属性名。 |
| begin | <time> | 0 | 否 | 设置动效的延迟时间。 支持输入ms(毫秒)、s（秒）、m（分），默认为s(秒)，其他格式不支持。 |
| dur | <time> | 0 | 否 | 设置动效持续时间，如果dur没设置，按照end-begin的结果作为持续时间，小于等于0时，动效不触发。 支持输入ms(毫秒)、s（秒）、m（分），默认为s(秒)，其他格式不支持。 |
| end | <time> | 0 | 否 | 设置动效多久时间后结束。支持输入ms(毫秒)、s（秒）、m（分），默认为s(秒)，其他格式不支持。 |
| repeatCount | <number \| indefinite> | 1 | 否 | 设置动画播放的次数，默认无限次播放(indefinite)，可通过设置为数值1仅播放一次。 |
| fill | <freeze \| remove> | remove | 否 | 设置动画结束时的状态。 |
| calcMode | <discrete \| linear \| paced \| spline> | linear | 否 | 设置动画的插值模式。 discrete：阶跃，from值直接跳转到to的值； linear：线性； paced：线性，设置此项后keyTimes和keyPoints值无效； spline：自定义贝塞尔曲线，spline点定义在keyTimes属性中，每个时间间隔控制点由keySplines定义。 |
| keyTimes | string | - | 否 | 设置关键帧动画的开始时间，值为0~1之间的数值用分号隔开，比如0;0.3;0.8;1。keyTimes、keySplines、values组合设置关键帧动画。keyTimes和values的个数保持一致。keySplines个数为keyTimes个数减一。 |
| keySplines | string | - | 否 | 与keyTimes相关联的一组贝塞尔控制点。定义每个关键帧的贝塞尔曲线，曲线之间用分号隔开。曲线内的两个控制点格式为x1 y1 x2 y2。比如0.5 0 0.5 1; 0.5 0 0.5 1;0.5 0 0.5 1 |
| by | number | - | 否 | 在动画中对某一指定属性，添加相对偏移值，from默认为原属性值。 |
| from | string | - | 否 | 设置需要进行动画的属性的开始值。 如果已经设置了values属性，则from失效。 |
| to | string | - | 否 | 设置需要进行动画的属性的结束值。 如果已经设置了values属性，则to都失效。 |
| values | string | - | 否 | 设置一组动画的变化值。格式为value1;value2;value3。 |

## 示例

支持设备PhonePC/2in1TabletTVWearable

```
<!-- xxx.hml -->
<div class="container">
  <svg width="400" height="400">
    <rect x="20" y="20" width="100" height="100" fill="red" rx="0" ry="20">
      <animate attributeName="rx" values="0;10;30;0" keyTimes="0;0.25;0.75;1" keySplines="0.5 0 0.5 1; 0.5 0 0.5 1; 0.5 0 0.5 1" dur="1000" repeatCount="indefinite">
      </animate>
    </rect>
  </svg>
</div>
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170917.83520979077226868105703464914338:50001231000000:2800:A85CD12F91A64AF3926921A785F712C85673630A5DEAC6DEC116BD3E010A2D9E.gif)

```
<!-- xxx.hml -->
<div class="container">
  <svg width="400" height="400">
    <rect x="20" y="20" width="100" height="100" fill="red" rx="0" ry="20">
      <animate attributeName="fill" from="red" to="blue" dur="1000" repeatCount="indefinite"></animate>
      <animate attributeName="height" from="50" to="150" begin="500" end="1000" repeatCount="indefinite">  </animate>
    </rect>
  </svg>
</div>
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170917.98078017057149101592340575616183:50001231000000:2800:7304B55B9B4311C9AE2A9CC540D62C0D2D196F666659038DD107CDB8DDFFFF7E.gif)

```
<!-- xxx.hml -->
<div class="container">
  <svg width="400" height="400">
    <rect x="20" y="20" width="100" height="100" fill="red" rx="0" ry="20">
      <animate attributeName="rx" values="0;30" dur="1000" repeatCount="indefinite" fill="freeze" calcMode="linear"></animate>
    </rect>
  </svg>
</div>
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170918.07738287600337314344337670102866:50001231000000:2800:0D03F92634EF1153478B054BDBB210B9694ECDCE4E9949F90D46CD9A40E3A769.gif)

```
<!-- xxx.hml -->
<div class="container">
  <svg fill="white" width="600" height="600">
    <circle cx="60" cy="70" r="50" stroke-width="4" fill="white" stroke="blue">
      <animate attributeName="r" from="0" to="50" dur="2000" repeatCount="indefinite"></animate>
      <animate attributeName="cx" from="60" to="200" dur="2000" repeatCount="indefinite"></animate>
    </circle>
    <circle cx="60" cy="200" r="50" stroke-width="4" fill="white" stroke="blue">
      <animate attributeName="stroke-width" from="4" to="10" calcMode="discrete" dur="2000" repeatCount="indefinite"></animate>
      <animate attributeName="stroke" values="red;blue" dur="2000" repeatCount="indefinite"></animate>
    </circle>
    <circle cx="180" cy="200" r="50" stroke-width="10" stroke="red" stroke-dasharray="60 10" stroke-dashoffset="3">
      <animate attributeName="stroke-opacity" from="1.0" to="0.5" dur="2000" repeatCount="indefinite"></animate>
      <animate attributeName="stroke-dashoffset" values="30;0;30" dur="500" repeatCount="indefinite"></animate>
     <animate attributeName="cx" from="180" to="400" dur="2000" repeatCount="indefinite"></animate>
    </circle>
    <circle cx="180" cy="200" r="5" fill="blue">
      <animate attributeName="cx" from="180" to="400" dur="2000" repeatCount="indefinite"></animate>
    </circle>
    <circle cx="60" cy="380" r="50"  fill="blue">
      <animate attributeName="fill" values="red;blue" dur="2000" repeatCount="indefinite"></animate>
    </circle>
    <circle cx="180" cy="380" r="50"  fill="blue">
      <animate attributeName="fill-opacity" from="1.0" to="0.5" dur="2000" repeatCount="indefinite"></animate>
    </circle>
    </svg>
</div>
```

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170918.24947807060121041424884689138751:50001231000000:2800:8A78B2F8BBB1F6AEC250BB3B3DC8E2BC5FB5A4A9B91469097BD999492840540D.gif)