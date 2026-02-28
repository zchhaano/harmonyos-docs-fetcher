# 并行并发：Concurrency分析

任务池（TaskPool）（详细信息请参考[@ohos.taskpool（启动任务池）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-taskpool)）是为应用程序提供一个多线程的运行环境，降低整体资源的消耗、提高系统的整体性能，且您无需关心线程实例的生命周期。您可以使用任务池API创建后台任务（Task），并对所创建的任务进行如任务执行、任务取消的操作。

DevEco Profiler提供的Concurrency场景分析能力，帮助开发者针对并行并发场景，录制并行并发关键数据，分析Task的生命周期、吞吐量、耗时等性能问题。Concurrency模板支持展示ArkTS异步接口、NAPI异步接口、TaskPool、FFRT并发模型相关信息，并集成ArkTS Callstack、Callstack、Process信息，支持用户从Task生命周期关联到具体调用栈信息，方便用户定位并行并发性能问题。

## 查看Task统计信息

1. 选择展开某个泳道，可以用options下拉框筛选不同进程。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102110.92125167390687827162385241589158:50001231000000:2800:C3A3AA0BBFF20CF90D05F84DE34D9C05B378A59879AF2022D50B4E803AA59E72.png)
2. 框选子泳道中某段时间范围，详情区会出现该时段内，泳道对应执行状态下，并行并发任务的统计信息。
3. 点击Task Name的跳转按钮可跳转到对应的Task泳道。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102110.73684111916088465145322067570108:50001231000000:2800:9638FC96FCE6C7DF2809EB535B0F65027F1C16603562AFDEA12AC16862E39EB0.png)

## 查看某一个Task的所有状态

1. 选择展开某个泳道，可以用options下拉框筛选不同进程。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102110.86221737369208571385428271306506:50001231000000:2800:7DCAADC724E5623C50D7FACEA6196E846EC9584C8AFCBA467B9E717ABB8CC508.png)
2. 框选子泳道中某段时间范围，可以看到该Task在框选时间范围内的任务状态。
3. 点击Task Name的跳转按钮可跳转到对应线程的泳道，可查看在该Task执行时间范围内，trace文件的打点信息，反映的是线程该时段内的函数执行情况。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102110.84337038584115901883486722836420:50001231000000:2800:DEB92C702EFDD90C867948E063EAD365B12FCA4527395542C6408EB734FD22B5.png)
4. 展开Async ArkTS泳道，可单独查看ArkTS异步调用任务详情。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102111.66761880361223676344930101162310:50001231000000:2800:2D1D4E2887CECB5CE979887DCDEE6EECF93451A7F650306744260F210D584173.png)
5. 展开Async NAPI泳道，单独查看NAPI异步调用任务详情。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102111.29786237929221152164512335523053:50001231000000:2800:7C690018A3A3D6038DFC1248823217C4474D3DE718894993CABDA24FB3395442.png)

## 查看Task的某个状态

点击Task子泳道的某个执行节点，Details详情区里会出现task在该状态下的详细信息。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102111.92731466369139542626479385319548:50001231000000:2800:835989CD38A4C45DC6154156DD5B7BCBCDD2A51CA1EEAE90355953E3C3DB8B80.png)