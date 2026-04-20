# Types

 ![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/9mSoV7EoT0C6dybXUEodWA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260420T194146Z&HW-CC-Expire=86400&HW-CC-Sign=47EB20E4B051CE44240A5E86152391EF296C6F5E501009E5A19705705DFE374B)  

本模块首批接口从API version 23开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

  

#### ImageType

type ImageType = image.Image | image.Picture

 

图片容器类型，用于获取全质量图和未压缩图(YUV)。

 

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

 

**系统能力：** SystemCapability.Multimedia.Camera.Core

 

| 类型 | 说明 |
| --- | --- |
| image.Image | 图片容器类型，用于获取全质量图。 |
| image.Picture | 图片容器类型，用于获取未压缩图(YUV)。 |