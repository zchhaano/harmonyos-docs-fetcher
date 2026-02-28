# 1001502014 应用未申请scopes或permissions权限的可能原因和解决方法

**问题现象**

调用接口报错1001502014 应用未申请scopes或permissions权限。

**可能原因**

1. 没有申请对应的账号权限。
2. 权限申请成功后，最迟会在25小时后生效。
3. 使用[获取风险等级](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-get-risklevel)能力，但未申请获取风险等级权限。

**解决措施**

1. 申请对应权限，请见[申请账号权限](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-config-permissions)章节。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165544.65457315399080568506843491670295:50001231000000:2800:4B1320F924BE245D504011EFF8AFF79CA3FC256F113449037B839654C6B88714.png)
2. 权限申请通过后，您可通过修改应用工程 > app.json5中的versionCode触发权限生效。**图1**修改前
![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165544.96896838876120233438713522238551:50001231000000:2800:85E4710018F6D22FB5BC7AB096643E9FDFF78EC268B2F82BD9B261A27D99DAE4.png) **图2**修改后
![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165544.06810246668825479706353481469178:50001231000000:2800:A455FBF50114C34B058FA688D72F3674CE606579BC7713377C1F9323BF8C818F.png)
3. 确认是否需要使用获取风险等级能力，如需使用，请参考[获取风险等级](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-get-risklevel)申请对应权限。