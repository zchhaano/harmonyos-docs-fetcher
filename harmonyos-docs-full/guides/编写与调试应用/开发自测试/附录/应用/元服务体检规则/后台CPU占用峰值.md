## 规则详情

应用/元服务后台CPU占用峰值：应用/元服务切换到后台等待3min后，开始采集3min内CPU Load < 5%。

## 检测逻辑

1. 执行hdc shell。
2. 执行hidumper --cpuusage <进程pid>命令，获取总的cpu使用率。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102043.89080218531653801297822388005209:50001231000000:2800:2A1B590F1B2C37EE0B59EE86C4BCD1CA01270F3AE5F1D46A4E3502409CCC153A.png)

## 计算逻辑

执行多轮测试，取最大值为cpu占用峰值，cpu占用率须小于5%。