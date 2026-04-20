# Snapshot模板基本操作

  

针对方舟虚拟机，DevEco Profiler提供了内存快照分析能力，结合Memory实时占用情况，分析不同时刻的方舟虚拟机内存对象占用情况及差异。

 

在DevEco Studio 6.0.2及之前版本，Memory泳道统计时支持选择PSS/RSS/USS中的一个或多个，可以从多维度度量当前进程的物理内存使用情况。从DevEco Studio 6.1.0 Beta1开始，Memory泳道统计时固定为PSS、GL、Graph总和，在会话区不支持选择PSS/GL/Graph。

   

#### 查看快照详情

 

1. 创建Snapshot场景调优分析任务，操作方法可参考[性能问题定位：深度录制](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/deep-recording)。
2. 设置Snapshot泳道。 

 

单击任务左上角的![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/TrVOQ5wsRfukrrGd-YvSAg/zh-cn_image_0000002561753311.png?HW-CC-KV=V1&HW-CC-Date=20260420T193620Z&HW-CC-Expire=86400&HW-CC-Sign=7A2F20E1D853C7CCAFD152570B93534DD9AFACA77A49406AA6DADA1AB5DA9F94)进行泳道的筛选，再次单击此按钮可关闭设置并生效。
3. 单击ArkTS Snapshot泳道的“options”下拉列表，可以设置是否需要抓取基础类型number的数据。默认不抓取。 

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/xstDUJRcTTqrwHTs4Xw11g/zh-cn_image_0000002561833297.png?HW-CC-KV=V1&HW-CC-Date=20260420T193620Z&HW-CC-Expire=86400&HW-CC-Sign=9DA60E547E883FB9D349A1A1CF8931A20D8E38BA7C7225C2C0CB1D3845EAEB63)
4. 开始录制后可观察Memory泳道的内存使用情况，在需要定位的时刻单击任务左上角的![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/BxhtgsW5SWWlW9J44SauRQ/zh-cn_image_0000002530913368.png?HW-CC-KV=V1&HW-CC-Date=20260420T193620Z&HW-CC-Expire=86400&HW-CC-Sign=BE5055B478BACF04F39611329177CE2D302037E0CFBB9370A696CA3FB6B0AD86)启动一次快照。 

 

“ArkTS Snapshot”泳道的紫色区块表示一次快照完成。

  ![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/cGNr0CfqTWiF2XX3s06YIg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260420T193620Z&HW-CC-Expire=86400&HW-CC-Sign=13E4E8CBC2232AA9A35CA4258C6C5E92F97024175B3E9279A2850D451283BD90)   

  - 在任务录制过程中，单击分析窗口左上角的![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/3G3bsaquQcqEZgWex9j24A/zh-cn_image_0000002530753366.png?HW-CC-KV=V1&HW-CC-Date=20260420T193620Z&HW-CC-Expire=86400&HW-CC-Sign=FEC4261C4CBF61765301E021C47A3D8944E470BEF00AC462127ED43ACE1860B9)可启动内存回收机制。
  - 当方舟虚拟机的调优对象的某个程序/进程占用的部分内存空间在后续的操作中不再被该对象访问时，内存回收机制会自动将这部分空间归还给系统，降低程序错误概率，减少不必要的内存损耗。

   

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/8QtLuXQiTz6Dy4-VgeliZA/zh-cn_image_0000002561753281.png?HW-CC-KV=V1&HW-CC-Date=20260420T193620Z&HW-CC-Expire=86400&HW-CC-Sign=869EC6C5523B15F90DB6CA1787E6F931B70396CCC55F73F0467BFEFF5BCDABA6)

 

在“Statistics”页签中显示当前快照的详细信息：

 

  - Constructor：构造器。
  - Count：该对象的数量。
  - Distance：从GC Root到这个对象的距离。
  - Shallow Size：该对象的实际大小。
  - Retained Size：当前对象释放时，总共可以释放的内存大小。
  - Native Size：该对象所引用的Native内存大小。
  - Retained Native Size：当前对象释放时，总共可以释放的Native内存大小。
  - 带![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/JCB45UKMRr6c81DaVFFB8g/zh-cn_image_0000002561753279.png?HW-CC-KV=V1&HW-CC-Date=20260420T193620Z&HW-CC-Expire=86400&HW-CC-Sign=3C3B3055D09CC6CF5836911D125496CC9DF2B70414D3143CE800D0B5DCA86CD6)标识的对象，表示其为全局对象，可以通过全局window对象直接访问。

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/AuQc_VttRBu5PgdW3KbD5g/zh-cn_image_0000002530753358.png?HW-CC-KV=V1&HW-CC-Date=20260420T193620Z&HW-CC-Expire=86400&HW-CC-Sign=112C531B3538D5EB9080E969AD403E29BBA38265BF10B0C9151BD852A004B210)

  ![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/nxRVfNrORSybom0gytDXyA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260420T193620Z&HW-CC-Expire=86400&HW-CC-Sign=60DD64C1AD90369B9311D141762A0D96FE1461FAC09C539E50E06E86E318B0E2)   

  - 在任务分析窗口，可以通过“Ctrl+鼠标滚轮”缩放时间轴，通过“Shift+鼠标滚轮”左右移动时间轴；或使用快捷键W/S缩放时间轴，使用A键/D键可以左右移动时间轴。
  - 将鼠标悬停在泳道任意位置，可以通过M键添加单点的时间标签。
  - 鼠标框选要关注的时间段，可以通过“Shift+M”添加时间段的时间标签。
  - 在任务分析窗口，可以通过“Ctrl+, ”向前选中单点的时间标签，通过“Ctrl+. ”向后选中单点的时间标签。
  - 在任务分析窗口，可以通过“Ctrl+[ ”向前选中时间段的时间标签，通过“Ctrl+]”向后选中时间段的时间标签。

    

#### 应用对象名称解析

 

方舟系统目前有方舟应用对象、系统内部框架对象、其他JS对象三类对象，从DevEco Studio 6.0.0 Beta1版本开始，支持对应用对象类的名称进行解析，帮助开发者快速定位问题所在的源码位置，从而提升问题定位效率。

 

1. 系统内部框架对象：用于描述HarmonyOS操作系统底层框架的核心对象，提供基础系统能力。为方便开发者查看，当前在Statistics中此类对象均归类到（framework）构造器节点下。此类对象均以_GLOBAL开头。
2. 方舟应用对象：用于表示HarmonyOS应用中的具体组件、模块或资源。方舟应用对象需按照以下格式命名展示：       

```
com.example.app/MainModule@1.0.0/src/main/ets/MainPage.ets#MainPage(line: 10)[MainModule] //格式为BundleName/SelfModule@Version/FilePath/File#Class(line: xx)[RefModule]

```
3. 其他JS对象：用于描述方舟运行时中与JavaScript引擎相关的对象，提供JS语言层面的基础能力。例如：JSArray、JSSharedObject等。

 

在 Snapshot分析模板中，支持在Attributes页签点击方舟应用对象名称查看当前所选方舟应用对象的解析结果，便于确认问题出现的位置。各参数含义如下：

 

- Module：模块信息。
- Class：属性名称。
- Path：编译后的源码路径。支持通过点击属性名称旁边的![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/YcySKQ29TseyxDK90XGvNg/zh-cn_image_0000002530753336.png?HW-CC-KV=V1&HW-CC-Date=20260420T193620Z&HW-CC-Expire=86400&HW-CC-Sign=C50FEF64C2FDDDABB68E0A9B7532E2572F4C3A8834F1C0FF196F0A9003CDDD21)图标直接跳转至工程中的代码位置，方便开发者快速调试。

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/kUuJzkA_TAyTm00vRvT5xw/zh-cn_image_0000002561753257.png?HW-CC-KV=V1&HW-CC-Date=20260420T193620Z&HW-CC-Expire=86400&HW-CC-Sign=9283A9141BF3023E61240E35A532F4275FBAC4EDF15B425AA8BDD4377AD22FAA)

 

若应用编译模式是release，且启用了源码混淆，方舟应用对象将展示混淆后的数据。支持在Attributes页签查看当前所选应用对象的源码信息。

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/tFZ2i4JURXeg1GTiuwgcpw/zh-cn_image_0000002530913346.png?HW-CC-KV=V1&HW-CC-Date=20260420T193620Z&HW-CC-Expire=86400&HW-CC-Sign=E4D514BA6BFB5AFC645D925E61D350DCAB35FB4D391210AB2E4B2675BCF26D2E)

  ![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4/v3/tHCfPqR1TFmD_nt4PEC6DQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260420T193620Z&HW-CC-Expire=86400&HW-CC-Sign=011F8AE3B19BED2993391DA616D065E13E305112FA27332705E642BB9D8FD2D0)   

- 确保工程代码路径与解析信息匹配，否则跳转可能失败。
- 系统内部框架对象（framework）仅提供基本信息，不支持跳转。
- 对象名称后的line=0时表示无效行号，不支持跳转。

      

#### 节点属性与引用链

 

在“Snapshot”的“Statistics”页签和“Comparison”页签中，所有实例对象节点展开后会显示"<fields>"以及"<references>"，这两项节点分别代表该实例对象的属性以及该实例对象的引用链信息。

 

在“Snapshot”的More区域则展示“Fields”和“References”两个页签，分别代表Detail区域所选择对象的属性以及引用链信息，方便快捷查看所选中对象的属性等详细信息，而不需要跳转至对应对象。

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/AxwzufpfSD6s6IkhoJ_W6w/zh-cn_image_0000002561833277.png?HW-CC-KV=V1&HW-CC-Date=20260420T193620Z&HW-CC-Expire=86400&HW-CC-Sign=3F9B229039E1082612B01D41F02000D6DDC173CACF29E5D1AE6525AB4B0AD86D)

    

#### 节点跳转

 

在“Snapshot”的“Comparison”页签中，查看内存对象、对象属性及其引用链时，若要查看某一对象的详细信息，可以单击该对象所在行行尾的跳转图标跳转至该对象所在的“Statistics”页签并定位至该对象所在的位置，以查看该对象的详细信息。

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/tJw9LvyzQSGl_vnTPB0Bwg/zh-cn_image_0000002530913334.png?HW-CC-KV=V1&HW-CC-Date=20260420T193620Z&HW-CC-Expire=86400&HW-CC-Sign=9A7608F993E9BF34DCBEC6C8449A0511A09E56D84EEAC71CAB29266CC63ECC1E)

    

#### 历史节点前进/后退

 

当在“Comparison”和“Statistics”之间进行节点跳转后，单击详情区域左下角的左右箭头可以前进或者后退至下一个或上一个历史节点，以便快速在多个历史节点之间跳转查看。当箭头为激活状态时，表示前进/后退功能可用，当箭头为灰色状态时则代表无法使用该功能。

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/gPWTi_otSDibIoXsfhW05g/zh-cn_image_0000002561833241.png?HW-CC-KV=V1&HW-CC-Date=20260420T193620Z&HW-CC-Expire=86400&HW-CC-Sign=F96998B48762A1E6CAEFEC0EBD600F59CB2F5105DAD3D26D7C3BC930D76FA3DD)

    

#### 比较快照差异

 

在“Snapshot”的“Comparison”页签中，以当前选择的快照为base，下拉框选择的快照为Target，即可得到两次快照信息的比较结果。

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/NfSlio2LTAyrAsfCpzXVaA/zh-cn_image_0000002530913354.png?HW-CC-KV=V1&HW-CC-Date=20260420T193620Z&HW-CC-Expire=86400&HW-CC-Sign=83342480F944DEC036011B4FCBBE885AECB11FA8DD46B0AEDBDEAF1DC6EA317F)

 

在“Snapshot”的“Comparison”页签中，可进行两次快照的差异比较，比较内容包括新增数、删除数、个数增量、分配大小、释放大小、大小增量等等。通过不断对比，可快速分析和定位内存问题的具体位置。

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/D2LWrrldTiiSexKbBsK2Og/zh-cn_image_0000002561833269.png?HW-CC-KV=V1&HW-CC-Date=20260420T193620Z&HW-CC-Expire=86400&HW-CC-Sign=47E0C7E79E0115DB66F11631BB2430FF5738C55738212B13A8995D704A404480)

    

#### 引用链向最小引用距离展开

 

Snapshot分析支持一键向引用链最小的引用距离方向展开。系统会计算从GC Roots垃圾收集器根到选定实例对象的最短路径（最短路径是指Distance逐渐-1的路径，最终抵达Distance = 1的节点），通过最短路径，能够清晰地看到该对象的句柄被哪些对象持有，快速定位问题产生的根源。

    

#### [h2]DevEco Studio 6.1.0 Beta2及之后版本

 

选择一个实例节点，系统会计算从GC Roots到选定对象的最短路径，并在右侧Shortest Paths页签实时切换和展示。

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/UmsnIT1GTmKBCcIezfq-bQ/zh-cn_image_0000002530753348.png?HW-CC-KV=V1&HW-CC-Date=20260420T193620Z&HW-CC-Expire=86400&HW-CC-Sign=DA1FF040EF8B5BB8557ABD6747468CE0C806BA47AE94D87082CA57E5B986999D)

 

    

#### [h2]DevEco Studio 6.1.0 Beta2之前版本

 

选择一个实例节点，底部搜索栏的Path to GC Root按钮呈可点击状态。点击该按钮选择搜索模式并确认，系统会计算从GC Roots到选定对象的最短路径，并在右侧Shortest Paths页签展示。

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/h5rPUFk_RmCL163w4hV7mQ/zh-cn_image_0000002561753293.png?HW-CC-KV=V1&HW-CC-Date=20260420T193620Z&HW-CC-Expire=86400&HW-CC-Sign=6D60A90B08730E337721F440FBAC741D33EABC4B82C11E812BD40F976914380D)

 

目前支持单根路径搜索、指定数量的根路径搜索和展示所有根路径三种搜索模式，默认为单根搜索。

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/0p4QZ50SREm2YuoiPiY1pA/zh-cn_image_0000002530913328.png?HW-CC-KV=V1&HW-CC-Date=20260420T193620Z&HW-CC-Expire=86400&HW-CC-Sign=C24AE1AC4260D27C03BA8ABA14E3733EC8D15F4B2027ECE20DA076E135B910B3)

 

设置完搜索模式后点击OK，右侧more区域会自动跳转至Shortest Paths页面展示搜索结果。

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/Gp9hrxWLQJKAhwqIHDeHgg/zh-cn_image_0000002530753354.png?HW-CC-KV=V1&HW-CC-Date=20260420T193620Z&HW-CC-Expire=86400&HW-CC-Sign=BC4240955CB002FEDF845B6F04474B23DA066CD1DBDDA4C9CC70B9A4DA8DFD80)

    

#### 引用链可视化

 

从DevEco Studio 6.0.0 Beta1版本开始，Snapshot模板支持将所有引用链以图表形式展示。系统会计算该节点周边的引用节点，并以关系图的形式清晰展示该对象的引用关系，便于定位问题产生的根源。

 

选择一个实例结点或reference引用关系节点后，底部搜索栏的**Visualization**按钮呈可点击状态。点击该按钮，配置搜索模式后，系统会计算该节点周边的引用节点，并跳转到Graph页签进行展示。

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/Ox0pmbYpRvm1KLZhAWCFbQ/zh-cn_image_0000002530753370.png?HW-CC-KV=V1&HW-CC-Date=20260420T193620Z&HW-CC-Expire=86400&HW-CC-Sign=97B1B6C5E156D5C990A72355527A722305EF19C4E23F88857651251A7CB5A04D)

 

目前支持最多展示30个周边节点，默认展示20个。当前支持以下两种优先级的引用链展开方式：

 

- Retained Size：按照Retained Size从大到小展示周边节点。
- Distance：按照Distance从小到大展示周边节点。

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0e/v3/gLnVOgDCQuaHsBn2D-JlFg/zh-cn_image_0000002530753362.png?HW-CC-KV=V1&HW-CC-Date=20260420T193620Z&HW-CC-Expire=86400&HW-CC-Sign=234E051EF8C47A85B8593DA507F89A228CF315BE0E84BE3D63A2DEDEFBD863FC)

 

设置完搜索模式后点击OK，底部页签会自动跳转至Graph页面展示搜索结果，红色标示的是中心节点，线段展示连接的两个节点之间的引用关系。

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/ZumMVuy4SHi8rBQqAENuWg/zh-cn_image_0000002561753263.png?HW-CC-KV=V1&HW-CC-Date=20260420T193620Z&HW-CC-Expire=86400&HW-CC-Sign=F1A81EE3D0C768168AB879BC7E2ECDBBDE10DDD56E96E7C9E4328C634B519389)

 

支持选中节点，右侧的More区域将展示该节点的详细信息，包括Fields、References和Shortest Paths三个页签。当鼠标悬浮在图形上的节点或线段时，悬浮框将展示对应的详细信息。图形区域支持拖动查看，使用Ctrl+鼠标滚轮可对图形进行缩放。

 

当在节点点击右键，展示的菜单列表包括以下选项：

 

- **Show More References**：展示当前节点更多的引用链。配置搜索模式后，重新生成以该节点为中心的引用链图形。
- **Show Path to GC Root**：展示当前节点到GC Root的路径。选择搜索模式后，重新生成以该节点为中心到GC Root的引用链图形。
- **Redraw with this node**：以该节点为中心重绘。
- **Reveal in Statistics**：在Statistics页面中显示该节点。
- **Clear Diagram**：清空当前图表中的所有内容。且清空底部栏的激活状态。

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/zkIWB0ewQJWMdl_AgOYVkg/zh-cn_image_0000002561753265.png?HW-CC-KV=V1&HW-CC-Date=20260420T193620Z&HW-CC-Expire=86400&HW-CC-Sign=8E0D9F628A3E0C2B321F7B7040A11288F08B50329959D80EFE37D625DC080FB7)

 

点击**Show More References**、**Show Path to GC Root**和**Redraw with this node**选项后，单击详情区域左下角的左右箭头，可以前进或者后退至下一个或上一个历史图形，以便在多个（最多三个）可视化图形之间跳转查看。当箭头为激活状态时，表示可用，当箭头为灰色状态时则代表无法使用该功能。

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/aYD62FCQQcuLeIM3HvYVlg/zh-cn_image_0000002530753346.png?HW-CC-KV=V1&HW-CC-Date=20260420T193620Z&HW-CC-Expire=86400&HW-CC-Sign=5A33FC34162062FAC24A077538B2D7527EEC91315C6903B25D47A2292C8E98D4)

    

#### 离线导入内存快照

 

DevEco Profiler支持离线导入内存快照功能，可导入一个或多个.heapsnapshot及.rawheap文件。

 

您可以在DevEco Profiler主界面的“Create Session”区域中，单击“Open File”，导入.heapsnapshot或.rawheap文件。

  ![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/-uBGfB6USheQz9P-5ylcxg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260420T193620Z&HW-CC-Expire=86400&HW-CC-Sign=2C3DE6436E65C480F385AB754AC3922D61E3B23AD3264CF1268CBFACB480DBE9)   

- 导入的单个文件大小不超过1.5G。
- 批量导入的文件数量不超过10个。
- .rawheap文件是应用发生Out of Memory现象时产生的原始内存文件。

   

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/cKDYPQ8gQ1GJBgp4bsAa4w/zh-cn_image_0000002530913322.png?HW-CC-KV=V1&HW-CC-Date=20260420T193620Z&HW-CC-Expire=86400&HW-CC-Sign=29BBD69242E1E46510DBE98BAD5E30DD00319C5ABBFEB4EB955C4E362DE54689)

 

离线导入内存快照成功后，可以导入与.heapsnapshot或.rawheap文件匹配的.jsleaklist文件，展示jsleakwatcher监控采集到的内存泄漏对象。

  ![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/Wuk-0pmPQaGhtBtBoIp1WA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260420T193620Z&HW-CC-Expire=86400&HW-CC-Sign=7E5A4AD379DB2F2BFA0EB2AE43A4DB69A6ADA64BB4AB3C5CEF3766B755D02024)   

- 导入的单个jsleaklist文件大小不超过30M。
- 导入的jsleaklist文件通过文件中的hash值与已导入的heapsnapshot文件匹配。
- 可多次导入不同的jsleaklist文件，也可同时导入多个不同的jsleaklist文件，重复导入不会覆盖已导入的匹配上的jsleaklist文件。总的导入匹配成功的文件数量不超过导入的heapsnapshot文件。

   

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/VUnotd2sTdWOKgZJVDOO-Q/zh-cn_image_0000002530753340.png?HW-CC-KV=V1&HW-CC-Date=20260420T193620Z&HW-CC-Expire=86400&HW-CC-Sign=34F0EDCB2D7421C61C425CA5C6782A1B3DEB09E65EDE04F57637CDFE36195674)

    

#### 解析内存对象

 

从DevEco Studio 6.1.0 Beta2开始，DevEco Profiler支持导入[代码混淆产物nameCache](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-exception-stack-parsing-principle#section19215122372720)文件和[ArkTS调试产物sourceMap](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-exception-stack-parsing-principle#section666114451518)文件，还原文件名称和文件路径。

 

以nameCache文件为例，文件导入前，Class为d8，

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/i690kf7pQnabg7t_OXJdWA/zh-cn_image_0000002561753285.png?HW-CC-KV=V1&HW-CC-Date=20260420T193620Z&HW-CC-Expire=86400&HW-CC-Sign=CFC87EB869A49FEE8883D7FBAF73EB0419844C8B788281E233401F59031D459F)

 

点击工具栏![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/p1PvEvyqTUW1AmSL-quovg/zh-cn_image_0000002530913326.png?HW-CC-KV=V1&HW-CC-Date=20260420T193620Z&HW-CC-Expire=86400&HW-CC-Sign=DBE8E706157099C284793825DE806E9499C3A18EE3CB78081FD2D8931FD86D8E)按钮，导入nameCache文件，Class显示为文件名称MyAbilityStage。

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/0_f2xSfVRISVXJV0mpXr6g/zh-cn_image_0000002530753368.png?HW-CC-KV=V1&HW-CC-Date=20260420T193620Z&HW-CC-Expire=86400&HW-CC-Sign=CBB44878C19AAC4920DEA9B04DE8B0ED77140EF5DA249F5350727E964AB732B3)