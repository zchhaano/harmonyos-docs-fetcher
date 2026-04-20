# @ohos.multimedia.avCastPickerParam (投播组件参数)

 

avCastPickerParam提供了[@ohos.multimedia.avCastPicker](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-multimedia-avcastpicker)组件状态枚举值。

 ![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/gxPlS5RvRzOnYzKPW6jjTQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260420T194113Z&HW-CC-Expire=86400&HW-CC-Sign=2DF1DF29863A3DA95FC6E99E026085EF44C3EF2C450665944D85A01AA522AA5B)  

本模块首批接口从API version 11开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

  

#### AVCastPickerState

投播组件设备列表状态参数选项。

 

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

 

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

 

| 名称 | 值 | 说明 |
| --- | --- | --- |
| STATE_APPEARING | 0 | 组件显示。 |
| STATE_DISAPPEARING | 1 | 组件消失。 |

   

#### AVCastPickerStyle 12+

投播组件样式参数选项。

 

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

 

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

 

| 名称 | 值 | 说明 |
| --- | --- | --- |
| STYLE_PANEL | 0 | 面板样式。 |
| STYLE_MENU | 1 | 菜单样式。 |

   

#### AVCastPickerColorMode 12+

投播组件显示模式参数选项。

 

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

 

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

 

| 名称 | 值 | 说明 |
| --- | --- | --- |
| AUTO | 0 | 跟随系统模式。 |
| DARK | 1 | 深色模式。 |
| LIGHT | 2 | 浅色模式。 |