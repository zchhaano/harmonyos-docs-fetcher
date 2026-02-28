# extension调试

开发者可通过两种方式对[Extension Ability](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/extensionability-overview)生命周期函数进行调试。

- 应用安装到设备上后，通过等待调试方式进行调试。
- 修改运行调试配置项，指定当前运行或调试的Ability为Extension Ability。

## 等待调试方式

1. 参考[等待调试](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-arkts-attach-to-process)对当前调试工程进行调试。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102042.20192903105390640120815423378432:50001231000000:2800:C5553DD6CC6D54D3524BE044C76320CAB281118EE3505CB3D29EED2CC2B28F10.png)
2. 在Extension Ability生命周期内设置断点。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102042.19226371005212151655009439786073:50001231000000:2800:EC1D3E95FA24A400C459FD1B6DE5D855D63CAE9B3E81F20FE9C145401084CAD3.png)
3. 等待Extension Ability生命周期函数代码调用从而命中断点。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102042.67291305264408213004767132104287:50001231000000:2800:90D13C7C57F39EF1EEBB4767A3450D555475197B3E36A3447DDD2AB659C5A6EE.png)

## 修改运行配置方式

1. 在运行调试窗口，运行配置项**Launch Options**选择**Specified Ability**。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102042.90710810947069157703410529075260:50001231000000:2800:C3337D046313D376B42375B1F41D73548F6B32E1569B47586A725C180A24A71D.png)
2. 选择需要进行调试的Extension Ability。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102042.06642576594767702469852142713631:50001231000000:2800:FB315B79C0A3BB464E934B5B2EBF69FFBC7CF2E3A6C10BCD018BCA9DBEF368D8.png)
3. 点击**OK**保存配置后，点击调试按钮![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102042.04283086938140531117630969632081:50001231000000:2800:9FA8B3CB90C35357B568020D1E7067A9D079917CD685CA9C62AC77F4177356A7.png)，启动调试即可命中 Extension Ability 中的生命周期函数断点。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102042.27645240618460963331074048992376:50001231000000:2800:82F7C8E0CF084C0BA245D0903A36B53D88FCB5470EE4A47C024855226B2F37EB.png)