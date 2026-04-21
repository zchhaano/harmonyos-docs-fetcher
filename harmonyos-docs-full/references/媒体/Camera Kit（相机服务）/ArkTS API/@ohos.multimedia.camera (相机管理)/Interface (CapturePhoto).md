# Interface (CapturePhoto)

 

获取全质量图和未压缩图的对象。

 ![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/8O_c7taXRRqxny6YqQLKBQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260420T194143Z&HW-CC-Expire=86400&HW-CC-Sign=DE5928F510CB35459961879507EA8F812795093A861034340D117750E688A2C1)  

本模块首批接口从API version 23开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

  

#### 导入模块

```
import { camera } from '@kit.CameraKit';

```

  

#### 属性

**模型约束：** 此接口仅可在Stage模型下使用。

 

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

 

**系统能力：** SystemCapability.Multimedia.Camera.Core

 

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| main | ImageType | 否 | 否 | 全质量图和未压缩图的对象。 |

   

#### release

release(): Promise<void>

 

释放输出资源。使用Promise异步回调。

 

**模型约束：** 此接口仅可在Stage模型下使用。

 

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

 

**系统能力：** SystemCapability.Multimedia.Camera.Core

 

**返回值：**

 

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

  

**示例：**

 

```
import { camera } from '@kit.CameraKit';

async function releaseCapturePhoto(capturePhoto: camera.CapturePhoto): Promise<void> {
  await capturePhoto.release();
}

```