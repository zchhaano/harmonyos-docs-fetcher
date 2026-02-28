# 能耗诊断：Energy分析

从DevEco Studio 5.1.0 Release版本开始，DevEco Profiler提供Energy模板，帮助用户在应用运行过程中查看能耗信息，包括不同器件的能耗、整机温度以及能耗异常帧，从而方便用户对能耗问题进行调优。此外，Energy模板还集成了Frame、Time、CPU场景分析任务的功能，方便开发者在分析能耗问题的同时同步对比同一时段的其他资源占用情况。

 说明

TV设备暂不支持使用Energy模板进行应用性能分析。

## 定位能耗问题

1. 创建Energy模板任务并录制相关数据，操作方法可参考[性能问题定位：深度录制](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/deep-recording)，或在会话区选择**Open File**，导入历史数据。
2. 录制结束等待处理数据完成。默认包含Energy Anomaly、Temperature以及Energy三条能耗相关泳道：

  - Energy Anomaly泳道：展示能耗相关的异常帧信息。该泳道暂不支持在Wearable设备上进行应用性能分析；
  - Temperature泳道：展示整机的温度信息。该泳道暂不支持在2in1设备上进行应用性能分析；
  - Energy泳道：展示各器件的能耗信息及整机电流信息。
3. 点击Temperature泳道，鼠标悬浮于泳道上可以查看对应时间范围的温度以及温度等级，帮助用户明确温度是否有明显上升，从而进行进一步的能耗定位。观察下方Detail区域，可以看到所选范围内的平均温度、最大温度以及最小温度。![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102109.66553755125189479605651045402138:50001231000000:2800:97ECE5EBC8ABC8B9A52E35FEEDF770EBEEE9C1EA2998E50E675215FBD8BBD4D4.png)
4. 点击Energy泳道，可在下方数据区查看录制范围内具体器件消耗的电量，器件包含：CPU、*Display（屏幕显示耗电量）、GPU、Location（定位模块耗电量）、Camera（相机耗电量）、Bluetooth（蓝牙功能耗电量）、Flashlight（闪光灯功能耗电量）、Audio（声音模块耗电量）、Wifi（无线功能耗电量）、Modem（信号模块耗电量）。*Device表示整机电流消耗情况。

框选Energy泳道数据，Energy Detail中呈现框选时间段内的详情信息。根据不同器件的消耗可结合Callstack泳道的调用栈信息进行进一步分析。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102109.82882436888088383643505098576661:50001231000000:2800:990408535E3B95A6AF5F56D9B65C52EB580330136BBEA36423BBD3DF66AA7BD7.png)
5. 点击Energy Anomaly泳道，鼠标悬浮于泳道上，可以查看空跑的渲染帧数（RS Empty Run）、不能正常调用动态系统合成器（DSS）合成而直接使用GPU进行渲染导致能耗恶化的帧的次数（GPU Consumption）以及CPU高负载异常次数（High CPU Load）。观察下方Details区域，可以看到所选范围内的能耗异常详情，包括能耗异常类型、开始时间、结束时间、能耗异常数量。

说明

2in1设备暂不支持查看RS Empty Run和GPU Consumption。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102109.57446189129977617668397118185567:50001231000000:2800:3821771C473D2ACB3B9B99A32CECB0A94A32FD980734132B3BE2378F31A21794.png)
6. 点击对应的异常类型数据（RS Empty Run和GPU Consumption），右侧More区域展示该异常帧信息，包括帧编号、RS VsyncId、帧持续时间。点击右侧跳转按钮可以跳转到Frame泳道中对应的具体帧，可以根据[查看指定Frame页面布局信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-insight-session-frame#section58691959194312)详细查看页面组件的布局情况，以及识别存在能耗问题的组件。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102109.43014045428223396641981040145695:50001231000000:2800:585D9C441D482B4F9CD026249FD0B63068CB381432FA98D50CF0AECB3B94B046.png)
7. 点击CPU高负载异常数据，右侧More区域展示该异常帧信息，包括进程ID、线程ID、负载值。点击右侧跳转按钮可以跳转到对应线程调用栈。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102109.24802329849861595820135116578418:50001231000000:2800:C220BB954D38863FDB3BFD6814E6A92FBB44F0CC5E1040690C8E0FA6B3929815.png)