# 案例：ArkTS内存泄漏分析

本案例介绍如何判断应用存在ArkTS泄漏，以及如何通过快照对比找出ArkTS内存泄漏的原因。

## 初步识别内存问题

1. 使用实时监控功能（详细使用方法请参考[性能问题定界：实时监控](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/realtime-monitor)）对应用的内存资源进行监控。正常操作应用，观察运行过程中的应用内存变化情况。当在一段时间内应用内存没有明显增加或者在内存上涨后又逐渐回落至正常水平，则基本可以排除应用存在内存问题；反之，在一段时间内不断上涨且无回落或者内存占用明显增长超出预期，那么则可初步判断应用可能存在内存问题。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102124.45703945531189959983575101993306:50001231000000:2800:2F23B3CAB28CCD42B15896F63C669E9355286E0A7B11EDE41A6966EC65A1D727.png)
2. 当从实时监控页面初步判断应用可能存在内存问题后，可以使用Memory泳道来抓取应用内存在问题场景下的详细数据以及变化趋势，初步定界问题出现的位置。Memory泳道存在Allocation或Snapshot模板中，使用Allocation或Snapshot模板录制均可。
3. 创建模板后，将模板中的其余泳道去除勾选，仅录制Memory泳道的数据。

说明

其余泳道会开启对内存分配、内存对象等数据的抓取，这些功能会带来额外的开销，可能会对我们初步定界问题产生噪音，影响分析，故先排除录制。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102124.45881831424779035210299689020924:50001231000000:2800:BD86CF1B86E80D37237836484379B0E80EAF0DB3C5D786DF56514B72F87D6B0E.png)
4. 点击三角按钮![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102124.94589730676685819535103651915641:50001231000000:2800:08918E200E0812475CCB8C53FD3058D4594C8F282C725D7A5D438C84A0F20345.png)即开始录制。
5. 录制过程中，不断操作应用在问题场景的功能，将问题放大，便于快速定界问题点。
6. 点击下图中方块按钮或者左侧停止按钮结束录制。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102124.24487764978698260831155628098374:50001231000000:2800:60DFD0ABDFC1D5CD536BB86F6EFC18F0C929CF27C99A8DF775D5316B8CF20F57.png)
7. 录制完成后，展开Memory泳道，其中ArkTS Heap表示方舟虚拟机内存，这部分内存受到方舟虚拟机的管控。Native Heap表示Native内存，主要是应用使用到的一些涉及Native的API所申请的内存以及开发者自己的Native代码所申请使用的堆内存（通常是C/C++），这部分内存需要开发者自行管理申请和释放。

当ArkTS Heap有明显的上涨，说明在方舟虚拟机内的堆内存上可能存在内存泄漏，可以使用Snapshot模板进行下一步分析；当Native Heap有明显的上涨，说明Native内存上可能存在内存泄漏，可以使用Allocation模板进行下一步分析。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102124.00801253943801418224007608445795:50001231000000:2800:237828AE56C92157F3D5D1243A89D88361874EBE5D8FAF2FFEE6856D11DD1592.png)

## 使用Snapshot模板分析ArkTS内存问题

### 分析步骤

分析内存泄漏问题步骤如下：

1. 使用Snapshot模板录制数据；
2. 在问题场景前拍摄快照；
3. 触发问题场景后，再次拍摄快照；
4. 对比两次快照的数据，可快速找到泄漏对象并做进一步分析；
5. 当有多个对象在比较视图都存在时，可以重复多次触发问题场景后拍摄快照，分别和问题场景前拍摄的快照进行对比，观察是否有对象出现明显的线性变化趋势，进一步缩小泄漏对象的范围。

### 录制Snapshot模板数据

1. 连接设备后启动应用，点击应用选择框选择需要录制的应用，选择**Snapshot**模板，点击Create Session或双击Snapshot图标即可创建一个Snapshot的录制模板。
2. 创建模板后，点击三角按钮即开始录制。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102124.59395230701157455986364476202644:50001231000000:2800:8A34F5C13E8605D411B966EC4469B5633A6875C2E9D4175CC961FAC9C9D636F2.png)
3. 待右侧泳道全部显示recording后则表明正在录制中。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102124.91380213344789434346363090090494:50001231000000:2800:DB37AA02F5000ACE20FBEBA4F35904013EAEC6BCF17694A131E21991FDAA3B24.png)
4. 拍摄第一次堆快照作为基准（点击图中①处拍摄按钮，待②处显示出紫色条块表示快照拍摄完成）。

说明

方舟虚拟机提供了在获取快照前自动GC（Garbage Collection，对堆内存进行垃圾回收）的能力，因此拍摄快照之前不用主动触发GC。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102124.62396793858348818793897546213882:50001231000000:2800:539EDA2D459DD8B9C5E128E3889707FCEF63F4C0FEA08DEFD0B98BD3FFA0131C.png)
5. 多次触发内存泄漏操作。可以操作5，7，11等这种特殊的次数。比如操作了5次对比两个快照发现有很多创建了5次没释放的场景，则可能存在内存泄漏，再操作7次，如果创建了7次那就可以确认发生了泄漏。
6. 拍摄第二次堆快照。
7. 点击下图中方块按钮或者左侧停止按钮结束录制。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102124.20936768217898743219558820562591:50001231000000:2800:F55F8FE541BCD2A8FDF498B30B3AAFDA6E8C2C200F582D68F6129BC43A002ED7.png)

### 分析ArkTS Heap

1. 在每次拍摄堆快照之前，虚拟机都会触发GC，所以理论上堆快照内存在的对象都是当前虚拟机已经无法GC掉的对象。我们可以将两个堆快照进行比较，来查看哪些对象是在触发问题场景时新增了且不能释放的。切换到窗口下方详情区域的“Comparison”页签，将两次快照进行对比。图中数据的含义是以Snapshot2作为基准，Snapshot2对比Snapshot1的数据变化量。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102124.15684545446739402052212818241299:50001231000000:2800:559D016797700301C67B3FBE6C8EA19879A3F20135519C3024E819849D7B9FA7.png)
2. 优先寻找与触发内存泄漏操作次数强相关、与业务代码强相关的Constructor，首先来分析这些对象是否正常。主要是按照Distance逐渐减小的方式找引用链，可以从references里面一层层去寻找，排查引用链上的可疑对象（一般指与业务代码关联的对象）。

说明

选择一个实例结点，底部搜索栏的Path to GC Root按钮成可点击状态。点击该按钮，系统会计算从GC Roots垃圾收集器根到选定实例对象的最短路径（最短路径是指Distance逐渐-1的路径，最终抵达Distance = 1的结点），并在右侧区域展示。

## 分析Snapshot数据

### 常见对象介绍

**JSArray**

目前所有JSArray展开后为数组里的各个元素：

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102125.72622534614393367198806599978642:50001231000000:2800:80E1988C4B0A498CA5273C356F98A03E882791A3D144998E6FA23CB9FE9ED724.png)

其中__proto__：原型对象，所有数组的__proto__应该是一致的；length：内置属性访问器，可以访问数组长度。

**TaggedDict**

位于(array)标签中，一般为虚拟机内部创建的字典，ArkTS代码层面不可见。

**TaggedArray**

位于(array)标签中，一般为虚拟机内部创建的数组，ArkTS代码层面不可见。

**COWArray**

位于(array)标签中，一般为虚拟机内部创建的数组，ArkTS代码层面不可见。

**JSObject**

JSObject展开后为内部的各个属性如下：

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102125.47541630554363929439124858259426:50001231000000:2800:0D24D0C8F15533E81CCBB9F484B3C7D4859AF095892FFA03EC6CD40B10DAD67A.png)

以下通过具体代码来介绍下实例化对象、声明对象、构造函数间的关系：

 收起自动换行深色代码主题复制

```
// HelloWorldPage .ets class People { old : number name : string constructor ( old : number , name : string ) { this . old = old ; this . name = name ; } printOld ( ) { console . log ( "old = " , this . old ) ; } printName ( ) { console . log ( "name = " , this . name ) ; } } @Entry @Component struct HelloWorldPage { @State message : string = 'Hello World' ; private people : People = new People ( 20 , "Tom" ) ; build ( ) { Row () { Column () { Text ( this . message ) . fontSize ( 50 ) . fontWeight ( FontWeight . Bold ) } . width ( '100%' ) } . height ( '100%' ) } }
```

采集到的snapshot数据如下：

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102125.02627358307408233087590914265793:50001231000000:2800:5C6AB35C035D1F227230D9441846C875D92FE483EE8DCF9611F6250C2AAFBA8D.png)

202169对象对应的是People，其主要声明了对象的属性和方法。

实例化对象的__proto__属性指向声明时的对象，声明对象里则会有constructor构造函数。当实例化多个对象时，实例化对象会有多个，但是声明对象和构造函数只有一个。

**JSFunction**

目前所有JSFunction都在(closure)标签中，展开即可看到所有JSFunction：

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102125.57449885776901700376011849350913:50001231000000:2800:348F42046122A04970BB6BD757902EFC4332DD52A1F09C5E63A9D17E067FB946.png)

每个函数展开后为函数内的各个属性：

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102125.11420814862665496523612209227832:50001231000000:2800:5D5BB50B4FD3136D09D2048D06EC67C02A10F60A82372784D21F6F7775B2095B.png)

其中HomeObject表示父类对象，即该方法属于哪个对象；_proto_表示原型对象；LexicalEnv表示该函数的闭包上下文；name是内置属性访问器，可获取函数名；FunctionExtraInfo表示额外信息，比如一些napi接口会在这里记录函数地址；ProtoOrHClass表示原型或者隐藏类。

如果函数显示为anonymous()，则表示为匿名函数；如果函数显示为JSFunction()，则表示该函数可能为框架层函数，创建函数的时候未设置函数名。对于这两种函数名不可见的情况，可以通过查看其引用来间接确认其名称：

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102125.45173146814050925683107870131312:50001231000000:2800:8CC60DEB22139AA871D07E88162E89BA074B9B5E0750106F5E062FE6537ED575.png)

**ArkInternalConstantPool**

虚拟机创建的常量池，ArkTS代码层面不可见，涉及到的字符串常量会在(array)标签中展示：

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102125.39661338804041557434823164430765:50001231000000:2800:98DAE871813237327EBC4350E3DCE3CB7FB6D139EF92C75FBA238D0F2A4B689D.png)

**LexicalEnv**

闭包变量上下文；闭包是一个链状结构，如下所示：

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102125.30645600764034142112473125865209:50001231000000:2800:4D508EFCAD028962E818B528C1956CBCFDA3DF685F92779AD5D0ECC2695E790F.png)

733这个节点本身是一个闭包数组，其中0号元素是调用者（或者再往上的调用者，以此类推）的闭包；1号元素存储的是调试信息；2号及以后的元素存储的就是闭包传递的变量，上例传递了一个变量。

**InternalAccessor**

内置属性访问器，会有getter和setter方法，通过getter、setter可以获取、设置该属性。

### 分析方法

**查看对象名称**

对于声明对象，可以通过constructor属性来确定对象名称。

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102125.50680733160721364886748504603421:50001231000000:2800:4469EA005B2E6A5F4743D7F1764B62F3FB1B3EE70EEAA6190E4A35ADB0D320FE.png)

对于实例化对象，一般没有constructor，则需要展开__proto__属性后查找constructor；

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102125.48553747284230776775553629989693:50001231000000:2800:BB039A7DEBA66CB923768A451ED8580077C8B3DE01E63DBF5756EA01DF073F0F.png)

若对象里有一些标志性属性，可以通过在代码里搜索属性名称来找到具体是哪个对象。

如果对象间有继承关系，则可以继续展开__proto__：

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260226102125.56694836381586151871453795902520:50001231000000:2800:2B6CD7C6D74E587AD7B5AA058ECE5707D7A6FFC469F424C6C28E65173817C24D.png)

如上图则表明Man对象继承自People对象。