# 如何处理OMG离线模型输出算子类型错误？

Caffe网络中具有相同类型名但计算功能不同的层。比如DetectionOutput层，需要使用算子映射指明为FSRDetectionOutput、SSDDetectionOutput等检测算子类型，否则OMG生成离线模型会执行失败。为了避免出现错误，以下两种方案二选一即可。

- 方案1：可以在OMG命令中加入--op_name_map参数，参考[OMG参数](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-overall-parameter)中op_name_map参数设置。
- 方案2：可以在原始网络proto模型文件中将输出算子类型指定为SSDDetectionOutput等算子类型，如下图所示。

 **图1**输出算子类型修改前（左）和修改后（右）
![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165240.18193529189885197242674081715529:50001231000000:2800:4D8379B2AC4F5FB56282D04C94AA0892BC01746E00698E6DAD7C75B8908C69D6.png)