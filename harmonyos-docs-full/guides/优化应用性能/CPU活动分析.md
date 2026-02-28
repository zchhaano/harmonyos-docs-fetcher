# CPU活动分析

开发者可使用DevEco Profiler的CPU场景调优分析，在应用或元服务运行时，实时显示CPU使用率和线程的运行状态，了解指定时间段内的CPU资源消耗情况，查看系统的关键打点（例如图形系统打点、应用服务框架打点等），进行更具针对性的优化。

## 查看各CPU使用情况

1. 创建CPU分析任务并录制相关数据，操作方法可参考[性能问题定位：深度录制](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/deep-recording)，或在会话区选择**Open File**，导入历史数据。

CPU分析任务支持在录制前单击![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102113.38435834267250288420080055484901:50001231000000:2800:1BC26C93A34592DB4F58D43148A5B3919F5298793165D6A9FC5401A34CE24B57.png)指定要录制的泳道。
2. “CPU Core”泳道显示当前选择调优应用或元服务的CPU的使用率。

可在“CPU Core”右侧的下拉列表中选择显示内容：

  - Slice and Frequency：每个子泳道包含时间片和频率两部分，时间片显示占用该CPU核心的进程、线程。
  - Usage and Frequency：每个子泳道包含CPU核心使用率和频率两部分。

框选主泳道，可对所选时间段内的CPU使用情况进行汇总统计，可查询多时间片的进程维度统计信息、线程维度状态统计信息、线程状态统计信息，以及所有时间片的数据统计信息。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102113.75868462352523022989410578208150:50001231000000:2800:485B0E867F2D67BDA75D61C6AE1040BB23D8B3A53C1A412D7DD57B47CE746CDD.png)
3. 将其展开，子泳道显示各CPU核心调度信息、各CPU核心频率信息以及各CPU核心使用率信息。

说明

将鼠标悬浮在某时间片上时，能够置灰非同进程时间片，通过此方法可以确定时间片的关联性。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102113.76448247853977622489359547476271:50001231000000:2800:994B5C0F30C47AAAC38D36F78FE39BE067ED756738C5FFB293AD40171224AA75.png)
4. 指定时间片，查看统计信息。

  - 单击某个运行状态的时间片，可查询这个时间片的基本运行信息及调度时延信息。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102113.99929579521162186904913827716425:50001231000000:2800:9F88CA4FBFCA18AAEC1AC62A69BC0938BB4E0870BDA91E68576B148419CFABF7.png)
  - 框选多个时间片，则可查询多时间片的进程维度统计信息以及所有时间片的数据统计信息。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102113.26099485178514534018387425857933:50001231000000:2800:CB6C292C18EBE02C74653E49AF46CD42A659A70765B85B8E6803E6D084EAAA5E.png)
  - 开启"View Integrated Scheduling Chain"后，点击CPU时间片泳道的节点可以查看某一个CPU运行线程的完整唤醒调度链。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102113.87256006720456035984002086915054:50001231000000:2800:9440256D1151167156BDB8A6E2D5AEE231CC89CD78ED3070CDD874A5C4A7646F.png)

 说明

- 在任务分析窗口，可以通过“Ctrl+鼠标滚轮”缩放时间轴，通过“Shift+鼠标滚轮”左右移动时间轴。或使用快捷键W/S放大或缩小时间轴，使用A键/D键可以左右移动时间轴。
- 将鼠标悬停在泳道任意位置，可以通过M键添加单点时间标签。
- 鼠标框选要关注的时间段，可以通过“Shift+M”添加时间段时间标签。
- 在任务分析窗口，可以通过“Ctrl+, ”向前选中单点时间标签，通过“Ctrl+. ”向后选中单点时间标签。
- 在任务分析窗口，可以通过“Ctrl+[ ”向前选中时间段时间标签，通过“Ctrl+]”向后选中时间段时间标签。
- CPU分析支持能耗分析，请参见[能耗诊断：Energy分析](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-profiler-energy)。

## 查询进程详情

单击工具控制栏中的![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102113.50723094343675473270923675892743:50001231000000:2800:93897986478A1508B36196051EFC546D5250D34CEA19EBB56EAEA68D45D6BB1B.png)按钮，可以设置是否为精简模式。精简模式下，trace数据量将大幅减少，主要采集当前进程、大桌面进程和render_service进程的trace数据。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102113.21571898809467914710105119761459:50001231000000:2800:0C54ABD2B4EFC41D1F5AB981BEB213AC02E925A1645F7BC0569C3EA78D250C25.png)

 进程泳道显示进程对各CPU核心的占用情况。展开进程泳道，显示进程下的线程列表以及线程的运行状态。

- 单击运行状态的时间片，显示线程在该片段的运行详情，包括起始时间、持续时长、运行状态、频率、线程优先级、所属进程、所属线程、上一运行状态、下一运行状态、唤醒线程，支持跳转到上个或者下个线程运行状态，支持跳转到唤醒线程状态等。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102113.73492310269223674210961355793899:50001231000000:2800:6F0554DA32F2B70F957EB203A60C99C5AE9014051CBB4678FE679EC75651EC46.png)
- 框选Thread泳道中多个运行状态的时间片，可查看此时间段内的不同运行状态的线程的统计信息，包括总耗时时长、最大耗时、最小耗时、平均耗时、处于当前状态的线程数量以及线程中的中载和重载数据统计。说明

中载、重载数据每100ms做一次统计，24ms < Running时长 ≤ 48ms 记为中载，Running时长大于48ms记为重载。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102113.25786706873539745519074349643875:50001231000000:2800:0B64B315053FE40D5DDB5E927237362A60E833E75580F41BC2F488C218309969.png)
- 框选应用进程Process主泳道，可查看此时间段内该进程下的线程并行度统计信息。并行度数据每100ms做一次统计，可以查看100ms内运行的总线程数量、各线程并行的总时间和并行度。点选某一行，可以查看对应线程编号和运行时间段。说明

并行度（Parallelism）取值范围是[1, cpu核数]，数值越小代表并行度越低。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102113.59705455850424780895949570430865:50001231000000:2800:49537F8C5EC0F413B9B1A7D822359C0313657944E6BB7AF4080B968CA7053A42.png)

## 查看Trace详情

当存在Trace任务时，可在对应的线程泳道查看到当前线程已触发的Trace任务层叠图。选择待查询的Trace。

- 点选泳道中的Trace片段，可查看单个Trace详情，包括名称、所属进程、所属线程、起始时间、持续时长、深度等。说明

  - 如果用户对线程进行了自定义打点，在此处亦可查看到对应的User Trace打点信息。
  - 从所在线程名称可分辨当前Trace的类型，系统Trace对应的线程名称为“线程名+线程号”，User Trace对应的线程名称为“打点任务名”。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102113.79579035030703597949419184693477:50001231000000:2800:6910F7F7CA4F66A0723360E96C09F6A28F512865A69068A2BBC37DEF66B02694.png)
- 框选多个Trace片段，可查看到Trace统计信息列表，包括Trace名称、此类Trace的总耗时、单个Trace的平均耗时、以及该时间段内该类Trace的触发次数等。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102113.56211311011594642436473674641698:50001231000000:2800:B5DD97BB5BF98D3897E5CD6B5D415838ECCD8C787E74584313D0652B73F01F5B.png)