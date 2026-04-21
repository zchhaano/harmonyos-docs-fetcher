# 基本架构

 

如下展示了总体的硬件基本架构。其中，AI Core通过数据总线与硬件结构中其它基本单元相连接，基于AscendC开发的算子，通过总线传输并最终运行在AI Core上。下文的编程模型基于硬件架构的抽象进行介绍，了解该内容能够更好的理解编程模型；对于需要完成高性能编程的深度开发者，更需要了解硬件架构相关知识，最佳实践中很多内容都以本章为基础进行介绍。

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/iICSmgnKQXqxKTUjo-8aJQ/zh-cn_image_0000002543215260.png?HW-CC-KV=V1&HW-CC-Date=20260420T191336Z&HW-CC-Expire=86400&HW-CC-Sign=C6395E831AE2B7BADC305146D1248FC3E0C1F8CFD0BE4F7D79F72B95D4709221)

 

AI Core负责执行标量、向量和张量相关的计算密集型算子，包括三种基础**计算单元**：Cube（矩阵）计算单元、Vector（向量）计算单元和Scalar（标量）计算单元，同时还包含**存储单元**（包括硬件存储和用于数据搬运的搬运单元）和**控制单元**。硬件架构根据Cube计算单元和Vector计算单元是否同核部署分为**耦合架构**和**分离架构**两种。

 

Kirin9020/KirinX90系列处理器：耦合架构

 

#### 耦合架构

耦合架构是指Cube计算单元和Vector计算单元同核部署，架构图如下图所示。下图中列出了计算架构中的[存储单元](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-storage-unit)和[计算单元](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-computing-unit)，箭头表示数据处理流向，MTE1/MTE2/MTE3代表[搬运单元](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-storage-unit)。

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/zMmgIONISvyBtKHOWXjIPA/zh-cn_image_0000002573855175.png?HW-CC-KV=V1&HW-CC-Date=20260420T191336Z&HW-CC-Expire=86400&HW-CC-Sign=806BE38AB3B54D97FDD771DF762B6ACF5BECDF350E06BFA15BF429DC624260E5)

 ![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/ymuTGBffTd6JOr4ibS-P8A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260420T191336Z&HW-CC-Expire=86400&HW-CC-Sign=A531E36863C6201681B0AB65F0FA2887CA17AAD637912DA7E21B1F61EF0CF004)  

图中的虚线箭头表明Kirin9020/KirinX90系列处理器支持Scalar直接读写GM数据。

   

#### 分离架构

如下图所示，分离架构将AI Core拆成矩阵计算(AI Cube、AIC)和向量计算(AI Vector、AIV)两个独立的核，每个核都有自己的Scalar单元，能独立加载自己的代码段，从而实现矩阵计算与向量计算的解耦，在系统软件的统一调度下互相配合达到计算效率优化的效果。AIV与AIC之间通过Global Memory进行数据传递。

 

![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/5YszeoP4T1SFuvsfTZm9wQ/zh-cn_image_0000002573975155.png?HW-CC-KV=V1&HW-CC-Date=20260420T191336Z&HW-CC-Expire=86400&HW-CC-Sign=343E2399685BE275EA21C0E786AAD65FB102B41F8A05C4FFAD10CE8F61D4F36D)

 

- AIC架构

 

  - 包含4个并行执行单元（搬运单元和计算单元）：MTE1、MTE2、Cube、Scalar。
  - 包含7个内存单元：GM（核外）、L1、L0A、L0B，L0C、BiasTable Buffer、FixPipe Buffer。
- AIV架构

 

  - 包含4个并行执行单元：MTE2、MTE3、Vector、Scalar。
  - 包含2个内存单元：GM（核外）、UB。
- 典型计算数据流

 

  - Vector计算：GM-UB- [Vector]-UB-GM。
  - Cube计算：GM-L1-L0A/L0B-Cube-L0C-FixPipe-GM、GM-L1-L0A/L0B-Cube-L0C-FixPipe-L1。