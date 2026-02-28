# 案例：Native内存泄漏分析

本案例介绍如何判断应用存在Native内存泄漏，以及如何通过Native Allocation泳道找出Native内存泄漏的原因。

## 初步识别内存问题

1. 使用实时监控功能（详细使用方法请参考[性能问题定界：实时监控](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/realtime-monitor)）对应用的内存资源进行监控。正常操作应用，观察运行过程中的应用内存变化情况。当在一段时间内， 应用内存没有明显增加或者在内存上涨后又逐渐回落至正常水平，则基本可以排除应用存在内存问题；反之，在一段时间内不断上涨，且无回落或者内存占用明显增长超出预期，那么则可初步判断应用可能存在内存问题。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102129.37072306725878533353108805936573:50001231000000:2800:1FC7FA20EFE9440D6E5EE22E552E78EF878043EFE09ADD2B707F7051ACF7D0E0.png)
2. 当从实时监控页面初步判断应用可能存在内存问题后，可以使用Memory泳道来抓取应用内存的详细数据以及变化趋势，初步定界问题出现的位置。Memory泳道存在Allocation或Snapshot模板中，使用Allocation或Snapshot模板录制均可。
3. 创建模板后，将模板中的其余泳道去除勾选，仅录制Memory泳道的数据。

说明

其余泳道会开启对内存分配、内存对象等数据的抓取，这些功能会带来额外的开销，可能会对我们初步定界问题产生影响，建议先排除录制。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102130.16385216561808409376758073296951:50001231000000:2800:C1AC7B812C30218B940CF0932F3C255B0B13F871078EF57209D06141A550F454.png)
4. 点击三角按钮![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102130.31345282519698891804108069912619:50001231000000:2800:3626B8222801D304A0E4DFA815E9DB7327FF6248C68BD959D4AB2E6E0F94DC0B.png)即开始录制。
5. 录制过程中，不断在问题场景操作应用功能，放大问题便于快速定界问题点。
6. 点击下图中方块按钮或者左侧停止按钮结束录制。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102130.08224902953007254748186957624134:50001231000000:2800:22CE676F3CE2CD55D48BFE7B1B03891B742C8FFC044BB8079BF4DB870B388DF4.png)
7. 录制完成后，展开Memory泳道，其中ArkTS Heap表示方舟虚拟机内存，这部分内存受到方舟虚拟机的管控。Native Heap表示Native内存，主要是应用使用到的一些涉及Native API所申请的内存以及开发者自己的Native代码所申请使用的堆内存（通常是C/C++），这部分内存需要开发者自行管理申请和释放。

当ArkTS Heap有明显的上涨，说明在方舟虚拟机内的堆内存上可能存在内存泄漏，可以使用[Snapshot模板](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-snapshot-basic-operations)进行下一步分析；当Native Heap有明显的上涨，说明Native内存上可能存在内存泄漏，可以使用[Allocation模板](/consumer/cn/doc/harmonyos-guides/ide-native-allocation-case#section776643810160)进行下一步分析。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102130.54594234567162977137408959581851:50001231000000:2800:17544F6728FEF420CD5B83949613EBEEEA69DABAECF674D6A7A6AB2D8CE94AAB.png)

## 使用Allocation模板分析Native内存问题

### 录制Allocation模板数据

1. 连接设备后，点击应用选择框选择需要录制的应用，选择**Allocation**模板，点击Create Session或双击Allocation图标即可创建一个Allocation的录制模板。
2. 创建模板后，点击三角按钮即开始录制。

说明

如果要分析启动内存，单击Allocation任务后的![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102130.78843976576576874961713618984307:50001231000000:2800:F3D02E572D8F937467479CEC0F760F142990BAD110A211A89BA2A19317997225.png)按钮。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102130.01988002074904338669940503910703:50001231000000:2800:04327D41F227FFD66F66C533A329FD12CD9DDAC4E1AE95692D7B1DA9664D9073.png)
3. 操作应用复现问题场景，并在问题复现完成后，点击下图中方块按钮或者左侧停止按钮结束录制。

说明

默认使用统计模式采集数据。该模式下工具的采集性能更好、负载更低。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102130.29060053542060214993941149318881:50001231000000:2800:AAEEDDCBC2DFBEECF0C396948B57843C0AC6A299A47ECAED3C7712F669C30559.png)

### 分析Native数据

1. 框选Native Allocation泳道或子泳道。两个子泳道All Heap和All Anonymous VM分别代表使用malloc和mmap函数分配的内存情况。

1. 在下方详情区的“Statistics”页签中选择Created & Existing。

  - All Allocations：框选的时间段的所有分配内存信息。
  - Created & Existing：在框选范围的起点之后分配的，且在框选范围的终点之前没有释放的内存数据。
  - Created & Released：在框选范围的起点之后分配的，且在框选范围的终点之前已经释放的内存数据。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102130.81790672706920201531746177349954:50001231000000:2800:816C20C2CA7DB47B23BB2E0F4B1243362D949AE13A255C3D6DEAD115401F7F38.png)
2. 切换到“Call Trees”页签，该部分数据展示了详细的内存分配栈信息，同样需要选择Created & Existing。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102130.59702410515273430925398435561057:50001231000000:2800:0CF5D8A2340FD23FBDFB7399D764730F8EF50AF9B2FDF2E70D4140D92BE604BB.png)
3. 优先在内存分配栈信息中寻找与业务代码强相关的Symbol Name，即Category中为亮色。从上图中看，主要泄漏点在业务代码侧，需要结合业务代码进行分析。

说明

  - Category中亮色代表开发者调用栈，灰色代表系统调用栈。
  - 栈帧中主要为 Native 栈，除了应用本身编译的一些so及带有部分接口信息的so信息外，其他系统库部分仅展示so库与函数偏移信息，若需要查看这部分信息，需要导入相应版本的带符号的 so 库（具体参考[离线符号解析](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-profiler-data#section11376118192614)）。