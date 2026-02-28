# HarmonyOS APK应用和HarmonyOS应用在一键登录场景下的用户数据如何互通

终端设备从HarmonyOS 3.x/4.x（简称HarmonyOS）升级到HarmonyOS NEXT/5.0.x及之后版本（简称HarmonyOS NEXT）。

1. HarmonyOS APK应用使用OpenID关联用户数据时，将用户数据关系切换成UnionID，具体切换指导可以参考：[通过OpenID获取UnionID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/account-api-get-unionid)。
2. HarmonyOS APK应用使用UnionID关联用户数据时，在HarmonyOS NEXT/5.0.x上接入华为账号一键登录获取手机号后，应用需要同时将UnionID和手机号与用户信息进行关联，最终实现应用使用华为账号一键登录和手机号登录数据互通。详细流程可以参考：[用户场景设计](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-phone-unionid-login#section4654113502814)。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165641.83186183942413521795335000790733:50001231000000:2800:CB317EB8951B9FD4C352D2D0D8DB54147C5708DCA8764A87A7DF3A914B021B87.png)