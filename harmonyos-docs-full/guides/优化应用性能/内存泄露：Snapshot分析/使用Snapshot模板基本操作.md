## 查看快照详情

1. 创建Snapshot场景调优分析任务，操作方法可参考[性能问题定位：深度录制](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/deep-recording)。

说明

  - 在任务分析窗口，可以通过“Ctrl+鼠标滚轮”缩放时间轴，通过“Shift+鼠标滚轮”左右移动时间轴。或使用快捷键W/S放大或缩小时间轴，使用A键/D键可以左右移动时间轴。
  - 将鼠标悬停在泳道任意位置，可以通过M键添加单点时间标签。
  - 鼠标框选要关注的时间段，可以通过“Shift+M”添加时间段时间标签。
  - 在任务分析窗口，可以通过“Ctrl+, ”向前选中单点时间标签，通过“Ctrl+. ”向后选中单点时间标签。
  - 在任务分析窗口，可以通过“Ctrl+[ ”向前选中时间段时间标签，通过“Ctrl+]”向后选中时间段时间标签。
2. 设置Snapshot泳道。

单击任务左上角的![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102116.22421327371583723571207233357590:50001231000000:2800:180877269EB995D9CF92671C91A5F23A974F6E722EC46971AA47A3F2FC0C04B9.png)进行泳道的筛选，再次单击此按钮可关闭设置并生效。
3. 单击ArkTS Snapshot泳道的“options”下拉列表，可以设置是否需要抓取基础类型number的数据。默认不抓取。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102116.91201736380378046988887454069300:50001231000000:2800:20FE0DCA62230AF98CA03FE4441654AEF3CAAAD94046B6FE59A1BC88848B84DE.png)
4. 开始录制后可观察Memory泳道的内存使用情况，在需要定位的时刻单击任务左上角的![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102116.25818450514530660828557805417649:50001231000000:2800:79058C0ECB98323681B5B34A977F65C03AEAB8E0A293B095BF6AEE0B3FE25B5E.png)启动一次快照。

“ArkTS Snapshot”泳道的紫色区块表示一次快照完成。

 说明

  - 在任务录制过程中，单击分析窗口左上角的![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102117.17337178967287998584723943143768:50001231000000:2800:E41A32A704B43B85B50857370DA5B65C338A8E9AF3CA9979343C189A8A384C09.png)可启动内存回收机制。
  - 当方舟虚拟机的调优对象的某个程序/进程占用的部分内存空间在后续的操作中不再被该对象访问时，内存回收机制会自动将这部分空间归还给系统，降低程序错误概率，减少不必要的内存损耗。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102117.33966197535934510150669059711229:50001231000000:2800:52991A84D1E60D38062F23F8EFC539BF8BC588940C38C572108C7850617E9425.png)

在“Statistics”页签中显示当前快照的详细信息：

  - Constructor：构造器。
  - Count：该对象的数量。
  - Distance：从GC Root到这个对象的距离。
  - Shallow Size：该对象的实际大小。
  - Retained Size：当前对象释放时，总共可以释放的内存大小。
  - Native Size：该对象所引用的Native内存大小。
  - Retained Native Size：当前对象释放时，总共可以释放的Native内存大小。
  - 带![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102117.03861683616938878885892438000256:50001231000000:2800:8E7775FB2E269F15252F7E0881BAAC6B7C59665F3E3B3A93331C723714788DDC.png)标识的对象，表示其为全局对象，可以通过全局window对象直接访问。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102117.42323600102693420682846728558026:50001231000000:2800:C96351FFE407AD669E279F513DF5EBE8E93819A1A32A9E5CD840F133F4612ADE.png)

## 应用对象名称解析

方舟系统目前有方舟应用对象、系统内部框架对象、其他JS对象三类对象，从DevEco Studio 6.0.0 Beta1版本开始，支持对应用对象类的名称进行解析，帮助开发者快速定位问题所在的源码位置，从而提升问题定位效率。

1. 系统内部框架对象：用于描述HarmonyOS操作系统底层框架的核心对象，提供基础系统能力。为方便开发者查看，当前在Statistics中此类对象均归类到（framework）构造器节点下。此类对象均以_GLOBAL开头。
2. 方舟应用对象：用于表示HarmonyOS应用中的具体组件、模块或资源。方舟应用对象需按照以下格式命名展示：收起自动换行深色代码主题复制

```
com.example.app /MainModule@1.0.0/ src /main/ ets /MainPage.ets#MainPage(line: 10)[MainModule] / /格式为BundleName/ SelfModule @Version /FilePath/ File # Class (line: xx)[ RefModule ]
```
3. 其他JS对象：用于描述方舟运行时中与JavaScript引擎相关的对象，提供JS语言层面的基础能力。例如：JSArray、JSSharedObject等。

在 Snapshot分析模板中，支持在Attributes页签点击方舟应用对象名称查看当前所选方舟应用对象的解析结果，便于确认问题出现的位置。各参数含义如下：

- Module：模块信息。
- Class：属性名称。
- Path：编译后的源码路径。支持通过点击属性名称旁边的![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102117.07673276160968744110979657860614:50001231000000:2800:007F778A66E5169FD085D654E0FB0AB4483C959D72476D61CA1054E169F215D5.png)图标直接跳转至工程中的代码位置，方便开发者快速调试。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102117.45757612222029314411038040400291:50001231000000:2800:57508DB0EB224F33F63FBFC9B5EC09296715A6D05245ED1F5C4F9F8B23874B9C.png)

若应用编译模式是release，且启用了源码混淆，方舟应用对象将展示混淆后的数据。支持在Attributes页签查看当前所选应用对象的源码信息。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102117.29126555626884434423879888194432:50001231000000:2800:CC30FB937BE3EA50D3406F9CAFA8F87EB92939AC12C7F1D0400BD7C8D9AC1D59.png)

 说明

- 确保工程代码路径与解析信息匹配，否则跳转可能失败。
- 系统内部框架对象（framework）仅提供基本信息，不支持跳转。
- 对象名称后的line=0时表示无效行号，不支持跳转。

## 节点属性与引用链

在“Snapshot”的“Statistics”页签和“Comparison”页签中，所有实例对象节点展开后会显示"<fields>"以及"<references>"，这两项节点分别代表该实例对象的属性以及该实例对象的引用链信息。

在“Snapshot”的More区域则展示“Fields”和“References”两个页签，分别代表Detail区域所选择对象的属性以及引用链信息，方便快捷查看所选中对象的属性等详细信息，而不需要跳转至对应对象。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102117.50588534032494854278312651400299:50001231000000:2800:A186D6C24B2BBFE0C74090BD408F18F0AF2DC1ED72510F0ADDBC7DEF2615C328.png)

## 节点跳转

在“Snapshot”的“Comparison”页签中，查看内存对象、对象属性及其引用链时，若要查看某一对象的详细信息，可以单击该对象所在行行尾的跳转图标跳转至该对象所在的“Statistics”页签并定位至该对象所在的位置，以查看该对象的详细信息。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102117.63359786815871461454351469025994:50001231000000:2800:9CF298C6C108D865811A7B730AAD033B5A894960794C4738D94CFF9BDEF6BE69.png)

## 历史节点前进/后退

当在“Comparison”和“Statistics”之间进行节点跳转后，单击详情区域左下角的左右箭头可以前进或者后退至下一个或上一个历史节点，以便快速在多个历史节点之间跳转查看。当箭头为激活状态时，表示前进/后退功能可用，当箭头为灰色状态时则代表无法使用该功能。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102117.56839426003251196223285144087448:50001231000000:2800:B0AA4108A6F040A090DA6D534745BBE4695FE3F418B72847B60712A7BDB1BFA3.png)

## 比较快照差异

在“Snapshot”的“Comparison”页签中，以当前选择的快照为base，下拉框选择的快照为Target，即可得到两次快照信息的比较结果。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102117.38531775513633559071002620596534:50001231000000:2800:662FD2CBD904A10B6174F6A3FFBF99DE03E7420708E4B8E14A4CD45BE6D0BFE8.png)

在“Snapshot”的“Comparison”页签中，可进行两次快照的差异比较，比较内容包括新增数、删除数、个数增量、分配大小、释放大小、大小增量等等。通过不断对比，可快速分析和定位内存问题的具体位置。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102117.00656819702048566794198353414510:50001231000000:2800:624BA51DD98363556A3C036A2B8C6AB41C5BB877BF20A3AC2B95698C781CEC0F.png)

## 引用链向最小引用距离展开

Snapshot分析支持一键向引用链最小的引用距离方向展开。系统会计算从GC Roots垃圾收集器根到选定实例对象的最短路径（最短路径是指Distance逐渐-1的路径，最终抵达Distance = 1的节点），通过最短路径，能够清晰地看到该对象的句柄被哪些对象持有，快速定位问题产生的根源。

选择一个实例节点，底部搜索栏的Path to GC Root按钮呈可点击状态。点击该按钮选择搜索模式并确认，系统会计算从GC Roots到选定对象的最短路径，并在右侧区域展示。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102117.77126037007044664540311003548568:50001231000000:2800:7A0CF7B40C7E09913529202194585F4BA32022B589951632CFB79570F36F6594.png)

目前支持单根路径搜索、指定数量的根路径搜索和展示所有根路径三种搜索模式，默认为单根搜索。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102117.54352343876849981104897452664200:50001231000000:2800:07873C5A9638FB516866243A857B1DEF96041BDD5FACB622029A7298EE3DD43E.png)

设置完搜索模式后点击OK，右侧more区域会自动跳转至Shortest Paths页面展示搜索结果。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102117.79528499413566209570625399851344:50001231000000:2800:5A0577A2D7EE1973E2C88161949A77D734D220964F1AE6D6D752D722A8510CD5.png)

## 引用链可视化

从DevEco Studio 6.0.0 Beta1版本开始，Snapshot模板支持将所有引用链以图表形式展示。系统会计算该节点周边的引用节点，并以关系图的形式清晰展示该对象的引用关系，便于定位问题产生的根源。

选择一个实例结点或reference引用关系节点后，底部搜索栏的**Visualization**按钮呈可点击状态。点击该按钮，配置搜索模式后，系统会计算该节点周边的引用节点，并跳转到Graph页签进行展示。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102117.80960634219104401172342167252545:50001231000000:2800:5A198736DAD2D873A84AE0CC016DF8D1AEF3E51139AA5BB02BD72C4EFDC57351.png)

目前支持最多展示30个周边节点，默认展示20个。当前支持以下两种优先级的引用链展开方式：

- Retained Size：按照Retained Size从大到小展示周边节点。
- Distance：按照Distance从小到大展示周边节点。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102118.45169771661369548152893427730488:50001231000000:2800:76D0D7F47D5B549F2694B4035F0041076DD87F31CA450CCE9ED823EBD93ADF36.png)

设置完搜索模式后点击OK，底部页签会自动跳转至Graph页面展示搜索结果，红色标示的是中心节点，线段展示连接的两个节点之间的引用关系。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102118.54294721597914410015880612419139:50001231000000:2800:F6343D240314AD0BB01F8A42995E672DD452AF7685B52CCD9FC29FA564599FD5.png)

支持选中节点，右侧的More区域将展示该节点的详细信息，包括Fields、References和Shortest Paths三个页签。当鼠标悬浮在图形上的节点或线段时，悬浮框将展示对应的详细信息。图形区域支持拖动查看，使用Ctrl+鼠标滚轮可对图形进行缩放。

当在节点点击右键，展示的菜单列表包括以下选项：

- **Show More References**：展示当前节点更多的引用链。配置搜索模式后，重新生成以该节点为中心的引用链图形。
- **Show Path to GC Root**：展示当前节点到GC Root的路径。选择搜索模式后，重新生成以该节点为中心到GC Root的引用链图形。
- **Redraw with this node**：以该节点为中心重绘。
- **Reveal in Statistics**：在Statistics页面中显示该节点。
- **Clear Diagram**：清空当前图表中的所有内容。且清空底部栏的激活状态。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102118.92504580265231947323323454469932:50001231000000:2800:B8D3849422C8E703E27935AC088C22759CF4DA4813730BD42E70035336CC793C.png)

点击**Show More References**、**Show Path to GC Root**和**Redraw with this node**选项后，单击详情区域左下角的左右箭头，可以前进或者后退至下一个或上一个历史图形，以便在多个（最多三个）可视化图形之间跳转查看。当箭头为激活状态时，表示可用，当箭头为灰色状态时则代表无法使用该功能。![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102118.32945705557200461514069886835352:50001231000000:2800:F99B2DDEEA7DB6ECE7BBF48181B84483116C5543CFE8B526386A521E671E5CA9.png)

## 离线导入内存快照

DevEco Profiler支持离线导入内存快照功能，可导入一个或多个.heapsnapshot及.rawheap文件。

您可以在DevEco Profiler主界面的“Create Session”区域中，单击“Open File”，导入.heapsnapshot或.rawheap文件。

 说明

- 导入的单个文件大小不超过1.5G。
- 批量导入的文件数量不超过10个。
- .rawheap文件是应用发生Out of Memory现象时产生的原始内存文件。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102118.97687467159332128352016059782429:50001231000000:2800:501100540EC73FAE903953D08CF32F5F1FE875F218E487460A759D933CB6983B.png)

离线导入内存快照成功后，可以导入与.heapsnapshot或.rawheap文件匹配的.jsleaklist文件，展示jsleakwatcher监控采集到的内存泄漏对象。

 说明

- 导入的单个jsleaklist文件大小不超过30M。
- 导入的jsleaklist文件通过文件中的hash值与已导入的heapsnapshot文件匹配。
- 可多次导入不同的jsleaklist文件，也可同时导入多个不同的jsleaklist文件，重复导入不会覆盖已导入的匹配上的jsleaklist文件。总的导入匹配成功的文件数量不超过导入的heapsnapshot文件。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102118.11183387099803358767047627597443:50001231000000:2800:9CE9C22D746EB81D2776685EE2C2353C6036542AB9339D04AD9C7CF39CCA553A.png)