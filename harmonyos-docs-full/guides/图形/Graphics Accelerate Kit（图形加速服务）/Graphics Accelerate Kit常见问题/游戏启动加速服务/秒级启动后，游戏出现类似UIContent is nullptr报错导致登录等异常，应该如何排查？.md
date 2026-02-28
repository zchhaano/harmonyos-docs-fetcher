# 秒级启动后，游戏出现类似UIContent is nullptr报错导致登录等异常，应该如何排查？

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165411.53721814589725902582493268018506:50001231000000:2800:F35D9D9B84DFFDA0CC7A63CD23DFA9179D5EBC4BD129DB5A5D020EADFB5BF2C1.png)

该报错的原因是游戏秒级启动后，UIAbilityContext值未更新。

排查点：

1. 游戏启动后进入onCreate生命周期，是否更新UIAbilityContext值。

以[Codelab](https://developer.huawei.com/consumer/cn/codelabsPortal/carddetails/tutorials_LaunchAcceleration-ArkTS)示例工程为例，AbilityContext需要在isFirstLaunchFlag判断外设置。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165411.00932482707876040775524950371082:50001231000000:2800:33B7E4CEA1571A6233F6A261DB3BBCBAE04CB20C6EEB5AC14C342CDC87D27B28.png)
2. 针对依赖UIAbilityContext的三方SDK，每次启动是否同步更新UIAbilityContext值。