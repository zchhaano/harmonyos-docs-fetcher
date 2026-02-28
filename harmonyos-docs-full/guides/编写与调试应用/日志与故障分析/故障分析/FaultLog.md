# FaultLog

当应用运行发生错误导致应用进程终止时，应用将会抛出错误日志以通知应用崩溃的原因，开发者可通过查看错误日志分析应用崩溃的原因及引起崩溃的代码位置。

FaultLog由系统自动从设备进行收集，包括如下几类故障信息：

- App Freeze
- CPP Crash
- JS Crash
- System Freeze
- [ASan](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-asan)
- [HWASan](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hwasan)
- [TSan](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-tsan)
- [UBSan](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ubsan)

 说明

调试模式（debug和attach）下，DevEco Studio会屏蔽当前工程的App Freeze和System Freeze等超时检测，避免调试过程出现超时检测影响开发者调试。

当前支持屏蔽的App Freeze故障类型：

- THREAD_BLOCK_3S/THREAD_BLOCK_6S：应用主线程卡死检测，卡住3秒/6秒。
- APP_INPUT_BLOCK：输入响应超时。

当前支持屏蔽的System Freeze故障类型：

- LIFECYCLE_TIMEOUT：app、ability生命周期切换超时。

## 查看FaultLog日志

### 查看设备历史抛出的FaultLog日志

打开FaultLog窗口，将显示当前选中设备抛出的所有FaultLog日志。

FaultLog故障信息左侧按照**应用/元服务包名 > 故障类型 > 故障时间**结构组成，选中具体的故障日期，则会在右侧展示详细的故障信息，并对部分关键信息进行高亮展示，便于开发者进行故障定位。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102016.97458601015433749540938045898189:50001231000000:2800:723B8917BFFA2AE4B0E0C9C021A19E7B31642A1E34B143A5DFE95E3D85F4EEA9.png)

### 查看设备实时抛出的FaultLog日志

当设备抛出FaultLog日志时，DevEco Studio将会弹出消息提示框，开发者点击**Jump to Log**即可跳转至FaultLog窗口查看日志信息。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102016.23134990159610937543102327196721:50001231000000:2800:D69FC1CB3AF5833E654F3DCBE61C267228A8F24BAF3DB8FC6D5B5ACBD1823C24.png)

### 跳转至引起错误的代码行

若抛出的FaultLog中的堆栈信息中的链接或偏移地址指向的是当前工程中的某行代码，该段信息将会被转换为超链接形式，点击后可跳转至对应代码行。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102016.06256639096369373018477732937204:50001231000000:2800:81BE88F8EE6A4D6A13D86FC0E9D5F7A030D4F3E55FF8227E029DA9C9FA24BB3F.png)

## 导出日志

开发者可将当前显示的日志信息保存到本地，以便后续的进一步分析。开发者可根据需要选择保存当前选中节点的日志或保存所有日志。

- 保存当前选中节点的日志：

  - 在当前选中节点右键点击**Export FaultLog**。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102016.35664956264112500393204361608452:50001231000000:2800:1372C10F7641727FF2C899D68C47FFBC3C8B02D70B5973F179B2CBFBFFFE849F.png)
  - 点击Export FaultLog按钮![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102016.43163731348055951918338400037527:50001231000000:2800:B283A53A17E1DB4FC00B712FB53871D9B448C2411B78196A654C510757AF640B.png)，弹出子选项后进一步点击**Export Selected FaultLog**。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102016.87636378631775289317995284813704:50001231000000:2800:75F2EB4F988CA0A01AF3BEB550BB409B5AC45D185CC4C1E14F0FB4A10384E6D2.png)
- 保存所有日志：点击Export FaultLog按钮![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102016.26740329862997691855727395044448:50001231000000:2800:1ED085063893C5BEBDCF36EBE8686EEF848F2F514EF906240D833CC0FD0C2F18.png)，弹出子选项后进一步点击**Export All FaultLog**。

## 查看cppcrash结构化日志

从DevEco Studio 6.0.0 Beta1版本开始，支持对Cpp Crash类型的FaultLog，进行结构化展示和日志过滤。

1. 双击cppcrash日志，**Fault Info**右侧会出现**Fault Analysis**页签。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102016.01987610509702994331903120206463:50001231000000:2800:B1749A615B6D2E1BFEF70A154D61F5B1D51F50373EA327D8DF137205B158308B.png)
2. 点击**Fault Analysis**页签，会展示结构化的日志信息。

  - 页面上方的字段对应了FaultLog中的字段，具体对应关系请查看[字段说明](/consumer/cn/doc/harmonyos-guides/ide-fault-log#section1983219211210)。
  - 页面下方包含Stacks和Logs两个页签。

    - **Stacks**：展示线程的堆栈信息，具体请参考[查看堆栈信息](/consumer/cn/doc/harmonyos-guides/ide-fault-log#section459581010138)。
    - **Logs**：展示FaultLog中的HiLog日志，具体请查看[查看HiLog日志](/consumer/cn/doc/harmonyos-guides/ide-fault-log#section13361239195113)。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102017.28111969832688501679371695326150:50001231000000:2800:281B1AD2C9DE8F7709FE81799D260B740FEDE43C42D104F84DE7F4A9B80D1AA4.png)

### 字段说明

**Fault Analysis**页签中的字段和FaultLog的字段对应关系如下。

 **表1**展开

| Fault Analysis 的字段 | 说明 |
| --- | --- |
| Occurrence time | FaultLog发生的时间，对应FaultLog中的Timestamp字段 |
| Analysis time | 触发日志结构化展示的时间，即双击日志文件的时间 |
| Frontend | 是否是前台应用，对应FaultLog中的Foreground字段 |
| Bundle name | 包名，对应FaultLog中的Module name字段 |
| Device type | 设备类型 |
| App build number | 应用构建号，对应FaultLog中的VersionCode字段 |
| App version | 应用版本，对应FaultLog中的Version字段 |
| Device model | 设备信息，对应FaultLog中的Device info字段 |
| System version | 系统镜像版本，对应FaultLog中的Build info字段 |
| Abnormal signal | 异常信号，对应FaultLog中的Reason字段 |

### 查看堆栈信息

Stacks页面包含了FaultLog中的堆栈信息，并以线程为单元进行折叠，点击展开按钮![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102017.39353082353853281511026067332994:50001231000000:2800:E5BE3B8702DBF896A63EA4EC19C638A5A20EC80F916E882B35556A5821B62286.png)，可以展开对应线程。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102017.34023488415928368075464489262972:50001231000000:2800:BF275413E4FC62EEDD3F58A55683F8F4E06067CF0CEDF2F77F81D3ED1E4EDB47.png)

图中标注1的勾选框是展开应用堆栈，标注2的勾选框是展开系统堆栈，两个勾选框一共组成了四种状态，具体如下表。

 **表2**展开

| 勾选框勾选状态 | 说明 |
| --- | --- |
| 1、2都不勾选 | 展示所有线程，线程处于折叠状态。 |
| 1、2都勾选 | 展示所有线程，线程处于展开状态。 |
| 只勾选1 | 只展示应用线程，线程处于展开状态。 |
| 只勾选2 | 只展示系统线程，线程处于展开状态。 |

### 查看HiLog日志

Logs页面展示了FaultLog中的HiLog日志，支持日志级别的过滤和搜索。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102017.51451819090007669133617444971300:50001231000000:2800:9C98B7D61FEE027382A6A98F70CC7C3F16BF60ED0A6314F1A1A4EBB35FE1AA3F.png)

## 查看appfreeze结构化日志

从DevEco Studio 6.0.0 Beta2版本开始，支持对AppFreeze类型的FaultLog，进行结构化展示和日志过滤。

1. 双击appfreeze日志，**Fault Info**右侧会出现**Fault Analysis**页签。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102017.83849472854601582601582054583271:50001231000000:2800:F0A87BF0B5E55E5C41C4C8F667EF06F0407BD43636FADCB7FBF2D58E64551E73.png)
2. 点击**Fault Analysis**页签，会展示结构化的日志信息。

  - 页面上方的字段对应了FaultLog中的字段，具体对应关系请查看[字段说明](/consumer/cn/doc/harmonyos-guides/ide-fault-log#section15864144624712)。
  - 页面下方包含Stacks、Logs、System、3s/6s Compare四个页签。

    - **Stacks**：展示线程的堆栈信息，使用方式和cppcrash日志相同，具体请参考[查看堆栈信息](/consumer/cn/doc/harmonyos-guides/ide-fault-log#section459581010138)。
    - **Logs**：展示FaultLog中的HiLog日志，使用方式和cppcrash日志相同，具体请参考[查看HiLog日志](/consumer/cn/doc/harmonyos-guides/ide-fault-log#section13361239195113)。
    - **System**：从DevEco Studio 6.0.0 Beta3版本开始，新增System页签，用于在高负载场景下，展示设备CPU/内存的日志信息，具体请参考[查看高负载CPU/内存日志信息](/consumer/cn/doc/harmonyos-guides/ide-fault-log#section179717814915)。
    - **3s/6s Compare**：从DevEco Studio 6.0.2 Beta1版本开始，新增3s/6s Compare页签，用于对[THREAD_BLOCK_6S](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/appfreeze-guidelines#thread_block_6s-应用主线程卡死超时)类型的AppFreeze问题，展示3s和6s时间点的主线程堆栈日志，具体请参考[查看3s/6s堆栈日志](/consumer/cn/doc/harmonyos-guides/ide-fault-log#section76467955514)。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102017.32882432334579445096807533147335:50001231000000:2800:9B83B4A2063A5FD3E91BB9622F80C87010F7BCD42190883AF17DF617B011E7DF.png)

### 字段说明

**Fault Analysis**页签中的字段和FaultLog的字段对应关系如下。

 **表3**展开

| Fault Analysis 的字段 | 说明 |
| --- | --- |
| Occurrence time | FaultLog发生的时间，对应FaultLog中的Timestamp字段 |
| Analysis time | 触发日志结构化展示的时间，即双击日志文件的时间 |
| Frontend | 是否是前台应用，对应FaultLog中的Foreground字段 |
| Bundle name | 包名，对应FaultLog中的Module name字段 |
| Device type | 设备类型 |
| App build number | 应用构建号，对应FaultLog中的VersionCode字段 |
| App version | 应用版本，对应FaultLog中的Version字段 |
| Device model | 设备信息，对应FaultLog中的Device info字段 |
| System version | 系统镜像版本，对应FaultLog中的Build info字段 |
| Freeze type | 冻结类型，对应FaultLog中的Reason字段 |

### 查看堆栈信息

Stacks页签用于查看appfreeze中的堆栈信息，使用方式和cppcrash日志相同，具体请参考[查看堆栈信息](/consumer/cn/doc/harmonyos-guides/ide-fault-log#section459581010138)。

### 查看HiLog日志

Logs页签用于查看appfreeze中的HiLog，使用方式和cppcrash日志相同，具体请参考[查看HiLog日志](/consumer/cn/doc/harmonyos-guides/ide-fault-log#section13361239195113)。

### 查看高负载CPU/内存日志信息

从DevEco Studio 6.0.0 Beta3版本开始，新增System页签，用于在高负载场景下，展示设备CPU/内存的日志信息，有助于分析高负载和appfreeze之间的关联关系。

如下是CPU的相关日志。

①：柱状图表示对应时间点的CPU使用情况（百分比）。

②：鼠标悬浮在柱状图上，会显示CPU总使用率、CPU使用率top5的进程号（Pid）和对应的CPU使用率。

③：选中柱状图后，显示相关的日志。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102017.79580874170923420474832827349362:50001231000000:2800:43971BAB3BE4A7C849FCED9A680D68721F3E252D8DDD24C31482B0EE2A688D31.png)

如下是内存的相关日志。

①：柱状图表示对应时间点的内存使用情况（百分比）。

②：鼠标悬浮在柱状图上，会显示内存使用率、内存占用top5的进程和对应的内存大小。

③：选中柱状图后，显示相关的日志。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102017.82110681687395029088863994916141:50001231000000:2800:88D67A1DF592CC9F1A783D0FA5C8919EEA7F55C270CC59110D0ACAE780AD384D.png)

### 查看3s/6s堆栈日志

从DevEco Studio 6.0.2 Beta1版本开始，新增3s/6s Compare页签，用于对[THREAD_BLOCK_6S](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/appfreeze-guidelines#thread_block_6s-应用主线程卡死超时)类型的AppFreeze问题，展示3s和6s时间点的主线程堆栈日志，并标识栈帧中可能的故障处。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102017.00600966682883825296244208253265:50001231000000:2800:9E8692F7123F115A7FB6858D9A309A7E3CFF748B512D688C91C103D5FE40CE04.png)

如果不是THREAD_BLOCK_6S类型的AppFreeze问题，不会展示3s/6s Compare页签。

## 查看应用终止日志

从DevEco Studio 6.0.2 Beta1版本开始，提供**AppKilled**窗口，用于查看设备上应用终止的相关信息，包括应用异常退出的时间、进程名、是否前台应用、异常退出原因，点击**recordId**可以查看详细的faultlog信息。支持按设备、应用和异常原因对信息进行过滤。

AppKilled窗口中支持查看的异常退出原因请参考[reason字段说明](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hidumper#reason字段说明)，如需对问题进行排查处理，请参考[App Killed（应用终止）检测](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/appkilled-guidelines)。

 说明

2in1、Tablet设备不支持查看APP_INPUT_BLOCK和THREAD_BLOCK_6S类型的数据。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102017.78920963092452613819854387411068:50001231000000:2800:F3351C55FB89B37EDD4CCAC9E6F3131CF903D4A58C04F65023E83789503BEB7B.png)