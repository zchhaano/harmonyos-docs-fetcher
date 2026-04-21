# 使用DevTools进行网页内存分析

  

#### 开启DevTools

DevTools为Chrome浏览器自带工具，[下载](https://www.google.com.hk/intl/en_uk/chrome/)并启动Chrome浏览器后，在需要进行内存分析的页面按下F12或者Shift+Ctrl+I启动DevTools开发者工具。

  

#### 获取js堆内存快照

在内存界面下选择堆快照，点击获取快照即可对当前页面进行一次内存快照。

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0e/v3/8-xv877aTlyPBLtabPw1Cg/zh-cn_image_0000002573855329.png?HW-CC-KV=V1&HW-CC-Date=20260420T193618Z&HW-CC-Expire=86400&HW-CC-Sign=3C7F10E90310172E0EACFE7228E6B8B42495123B0CF18C50522C6D19F6B7EF4A)

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/5bC9TWU5QfKLatYlc4fbRQ/zh-cn_image_0000002573975309.png?HW-CC-KV=V1&HW-CC-Date=20260420T193618Z&HW-CC-Expire=86400&HW-CC-Sign=A545C1BAF23416D0AA55982F1F78DA0FD43D4736DD20D735F17F37B88918E594)

  

#### 堆快照分析

 

#### [h2]摘要(Summary)

摘要展示当前内存快照的概览。其中：

 

- 构造函数(Constructor):表示对象的构造器
- 距离(Distance):与GCroot的引用链距离。当出现同一类对象距离不同的情况，要注意代码逻辑可能出现问题。
- 对象计数(Object Count)：跟在构造器后方的灰色数字，表示当前构造器所构造的对象总数。
- 浅层大小(Shallow Size)：对象自身占用的内存大小。
- 保留大小(Retained Size)：当一个对象被释放后，系统虚拟机可以释放的总内存。

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/31tzx5vZQvSFdpJV4uOwcg/zh-cn_image_0000002543375076.png?HW-CC-KV=V1&HW-CC-Date=20260420T193618Z&HW-CC-Expire=86400&HW-CC-Sign=D747326D9BFC058E3A76FF395A5EDCD7909DE4FB5490C1D8FC723B3FDBAFA170)

 

在摘要界面的右侧有一个选择栏，用户可以选择查看特定的对象，例如下图中选择“在快照2和快照3之间分配的对象”，这样生成的摘要可以用于定位内存问题发生的位置。

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/aymYogtsTJS_ROaygcTakg/zh-cn_image_0000002543215416.png?HW-CC-KV=V1&HW-CC-Date=20260420T193618Z&HW-CC-Expire=86400&HW-CC-Sign=D6D83F04EB2EAE5AA8564C0857AF3AE912ACD6625C7647F8C2CDF476CA12E07E)

  

#### [h2]比较(Comparison)

在比较(Comparison)中可以将当前快照与另一个快照比较，跟踪对象属性和内存占用的变化。其中：

 

- 构造函数：对象的构造器。
- 新对象数(New)：该对象构造器下有多少新的对象被创建。
- 已销毁(Deleted)：该对象构造器下有多少新对象被销毁。
- 增量(Delta)：新对象与被删除对象的差值。
- 分配大小(Alloc Size)：两份快照间分配的内存大小。
- 已释放大小(Freed Size)：两份快照间释放的内存大小。
- 大小增量(Size Delta)：分配大小和已释放大小的差值。

 

可以根据比较界面不同快照间的差异分析内存问题。

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/K_AZa5EDQn6ySivHHUs8rA/zh-cn_image_0000002573855331.png?HW-CC-KV=V1&HW-CC-Date=20260420T193618Z&HW-CC-Expire=86400&HW-CC-Sign=E820B304EF11A6241DFE2690B62389A885D2575D8B7F8D8C9CF5D592CE0E2536)

  

#### [h2]控制(Containment)

控制(Containment)提供了一个自上而下的树形界面，该界面允许浏览和探索堆内存中的内容。我们可以用它来分析任意变量的引用情况。

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/Tg5JhlHgRt-mcrKMekiKbg/zh-cn_image_0000002573975311.png?HW-CC-KV=V1&HW-CC-Date=20260420T193618Z&HW-CC-Expire=86400&HW-CC-Sign=9E02C9E39F8BE48637F4F8C3933ABFA369180F0FD1ED4C93360AE764202E91EB)

  

#### [h2]统计信息(Statistics)

统计信息(Statistics)用一个饼图展示各个类型对象的内存占用比例。

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/pPw-Vo0ERPyjVA63e7DWEQ/zh-cn_image_0000002543375078.png?HW-CC-KV=V1&HW-CC-Date=20260420T193618Z&HW-CC-Expire=86400&HW-CC-Sign=6A7A8E1AF79098AB12253ED9A4F0C5AE782CC0578BCDF7BF85569CA5EC15759F)

  

#### 内存泄漏分析流程

1. 打开一个可能存在内存泄漏问题的页面并启用DevTools。下图展示的页面来自GitHub上的[memory-leak-simulation](https://github.com/Buchatech/JavaScript-Memory-Leak-Simulation)项目，该网页通过设置全局数组并不断向其推入'memory leak'字符串来模拟内存泄漏场景。

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/hx9kkG0ES0iwgzGJnzMuFQ/zh-cn_image_0000002543215418.png?HW-CC-KV=V1&HW-CC-Date=20260420T193618Z&HW-CC-Expire=86400&HW-CC-Sign=C9006F351819CA39B0366C868EAAE4108FF9948DCDBE89FD787D2360508C6A6E)
2. 在性能界面录制可能导致内存泄漏的用户操作，以识别引起内存泄漏的用户操作或组件。下图显示，网页已加载完毕，但内存仍在持续上升，表明可能存在内存泄漏问题。对于包含大量动态组件和频繁DOM操作的网页，内存曲线可能呈起伏状态。持续观察内存起伏的最低值变化，若最低值逐渐上升，怀疑网页存在内存泄漏问题。

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/uUl7q4sQS06yFvzrjClXzA/zh-cn_image_0000002573855333.png?HW-CC-KV=V1&HW-CC-Date=20260420T193618Z&HW-CC-Expire=86400&HW-CC-Sign=8E24556D00E6D52AEE44D0A6B3F7062CC327646AAC6B5898C071669B0A8D0C08)
3. 我们对这个网页进行第一次堆快照，发现Array占用了28M内存，基于该对象的内存占用显著高于正常值(通常在几MB范围内)，可以判断该对象可能存在内存泄漏问题。

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/9YSu4RmnQfOaaecEBt1Oxw/zh-cn_image_0000002573975313.png?HW-CC-KV=V1&HW-CC-Date=20260420T193618Z&HW-CC-Expire=86400&HW-CC-Sign=15A3AF0C1EF226B5E6475A39DB9E9B5EE357EA13B9CE5775EE9732C26ED22593)
4. 对网页进行可能会造成内存泄漏的操作，操作完成后进行第二次堆快照，然后选择两个快照间分配的对象，观察到Array构造器新产生约16MB内存占用。

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/cPYtSGXdQKOUFAXqDtEMjQ/zh-cn_image_0000002543375080.png?HW-CC-KV=V1&HW-CC-Date=20260420T193618Z&HW-CC-Expire=86400&HW-CC-Sign=B35117D370AFD2D48861E123E70E7E2C0B64284F2CEDF8447F092E4CF0740E8B)
5. 查看**比较(comparison)**，选择快照3并使用快照2作为比较对象，观察到Array构造器新产生了4030个对象，占用了16.1MB空间，但只释放了184B空间，根据此结果，确定内存泄漏发生在Array中。

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/m_Dn--1-Tv6mDgk5mpV1-w/zh-cn_image_0000002543215420.png?HW-CC-KV=V1&HW-CC-Date=20260420T193618Z&HW-CC-Expire=86400&HW-CC-Sign=E654AD031F43C57A1C2882E7040A8010BC2272ADCD0C1639D13C672D885E7FE8)
6. 录制1-2分钟的堆快照来获得包含时间轴的摘要视图，这与性能界面中的视图类似。使用此视图可以分析是哪个动作造成了内存占用的变化。录制快照时选择“时间轴上的分配情况”选项，点击录制。完成想要测试的动作后，停止录制即可生成内存堆时间轴视图。

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/bMUW7fQvQ42qLJvbgy72gg/zh-cn_image_0000002573855335.png?HW-CC-KV=V1&HW-CC-Date=20260420T193618Z&HW-CC-Expire=86400&HW-CC-Sign=2D1D89A8D2DA1846048B7B8052EA8B12788655E0903909F93DFF7FCDF7B9C429)
7. 在结果的时间轴上，使用左键滑动选择想要查看的区域，即可查看选定时间段内的内存分配情况。从下图中框选部分可以看到，在选定时间内，Array构造器产生了两千个新对象。利用该功能，可以明确不同操作对内存的影响。

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/r8NrhsW7RFSPW2wrsF97XA/zh-cn_image_0000002573975315.png?HW-CC-KV=V1&HW-CC-Date=20260420T193618Z&HW-CC-Expire=86400&HW-CC-Sign=1DAC130DB5B81C458D53BDEB43CB2F037206AC7E4B2241E66660F29342EB4E29)