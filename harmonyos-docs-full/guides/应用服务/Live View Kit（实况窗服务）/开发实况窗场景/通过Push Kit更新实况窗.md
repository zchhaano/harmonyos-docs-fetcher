## 场景介绍

本地实况窗的更新依赖于应用进程的存活，为了让实况窗在生命周期内正常完成更新和结束，我们更推荐开发者使用Push Kit实时更新实况窗状态。

通过Push Kit更新实况窗的流程如下图：

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165601.78179998637231798316954777692037:50001231000000:2800:36C2BC7539BCA1E93BC3B27CBE5C4777544DD77D76AF7CD793B7FE08FFC03170.png)

1. 使用Push Kit，获取Push Token。
2. 使用Live View Kit创建实况窗成功后，开发者需要将实况窗id、pushToken、实况窗场景event以及业务服务的相关的状态属性保存到业务服务端。
3. 当业务服务的用户订单状态发生变化时，通过Push Kit通道推送更新消息，更新/结束实况窗。

详细开发流程请参见Push Kit[推送实况窗消息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/push-update-liveview)。