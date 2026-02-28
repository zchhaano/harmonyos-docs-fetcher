# 拍照实践(ArkTS)

在开发相机应用时，需要先[申请相关权限](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/camera-preparation)。

当前示例提供完整的拍照流程介绍，方便开发者了解完整的接口调用顺序。

在参考以下示例前，建议开发者查看[相机开发指导(ArkTS)](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/camera-device-management)的具体章节，了解[设备输入](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/camera-device-input)、[会话管理](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/camera-session-management)、[拍照](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/camera-shooting)等单个流程。

## 开发流程

在获取到相机支持的输出流能力后，开始创建拍照流，开发流程如下。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165429.53723317084762835311452604884879:50001231000000:2800:7864B9B7F4DB4A223C0E798C9B326E3F23E7112E92B767FD609E8E0D611A0C43.png)

## 完整示例

Context获取方式请参考：[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

如需要在图库中看到所保存的图片、视频资源，需要将其保存到媒体库，保存方式请参考：[保存媒体库资源](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/photoaccesshelper-savebutton)。

需要在[photoOutput.on('photoAvailable')](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-photooutput#onphotoavailable11)接口获取到buffer时，将buffer在安全控件中保存到媒体库。

 收起自动换行深色代码主题复制

```
```