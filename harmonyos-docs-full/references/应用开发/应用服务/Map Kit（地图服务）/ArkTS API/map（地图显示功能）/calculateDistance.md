## 导入模块

支持设备PhonePC/2in1TabletWearable

```
import { map, mapCommon } from '@kit.MapKit';
```

## calculateDistance

支持设备PhonePC/2in1TabletWearable

calculateDistance(from: mapCommon.LatLng, to: mapCommon.LatLng): number

计算坐标点之间的距离。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**起始版本：**4.1.0(11)

**参数：**

 展开

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| from | mapCommon.LatLng | 是 | 起点坐标。 |
| to | mapCommon.LatLng | 是 | 终点坐标。 |

**返回值：**

 展开

| 类型 | 说明 |
| --- | --- |
| number | 两个坐标点之间的距离，单位：米。 入参为空返回0。 |

  **示例：**

```
let fromLatLng: mapCommon.LatLng = {
  latitude: 38,
  longitude: 118
};
let toLatLng: mapCommon.LatLng = {
  latitude: 39,
  longitude: 119
};

let distance = map.calculateDistance(fromLatLng, toLatLng);
```