## 概述

支持设备PhoneTablet

此结构体描述游戏应用每帧的相机运动数据，ABR会结合相机运动数据自适应调整FrameBuffer（帧缓冲，下文简称Buffer）分辨率因子。

**起始版本：** 5.0.0(12)

**相关模块：** [GraphicsAccelerate](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_graphics_accelerate)

## 汇总

支持设备PhoneTablet 

### 成员变量

 支持设备PhoneTablet展开

| 名称 | 描述 |
| --- | --- |
| ABR_Vector3 rotation | 相机变换的世界空间旋转欧拉角。 |
| ABR_Vector3 position | 相机变换的世界空间位移。 |

## 结构体成员变量说明

支持设备PhoneTablet 

### position

支持设备PhoneTablet收起自动换行深色代码主题复制

```
ABR_Vector3 ABR_CameraData::position
```

**描述**

相机变换的世界空间位移。

### rotation

支持设备PhoneTablet收起自动换行深色代码主题复制

```
ABR_Vector3 ABR_CameraData::rotation
```

**描述**

相机变换的世界空间旋转欧拉角。