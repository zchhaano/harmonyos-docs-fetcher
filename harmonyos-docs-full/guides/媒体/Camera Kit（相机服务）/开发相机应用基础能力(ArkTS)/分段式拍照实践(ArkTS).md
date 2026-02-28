# 分段式拍照实践(ArkTS)

在开发相机应用时，需要先[申请相关权限](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/camera-preparation)。

当前示例提供完整的分段式拍照流程介绍，方便开发者了解完整的接口调用顺序。

在参考以下示例前，建议开发者查看[分段式拍照(ArkTS)](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/camera-deferred-capture)的具体章节，了解[设备输入](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/camera-device-input)、[会话管理](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/camera-session-management)、[拍照](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/camera-shooting)等单个流程。

## 开发流程

在获取到相机支持的输出流能力后，开始创建拍照流，开发流程如下。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165436.28552726585233607377118461638269:50001231000000:2800:6E782BE780B8CA3ED288286754EA8F2C1700B8B86B048CE874AC375ADBCEDB6B.png)

## 完整示例

Context获取方式请参考：[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

 收起自动换行深色代码主题复制

```
```