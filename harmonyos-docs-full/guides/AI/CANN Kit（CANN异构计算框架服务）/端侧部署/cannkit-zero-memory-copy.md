# 内存零拷贝

  

#### 概述

对于GPU的纹理数据或模型的输入数据等已经存在于ION内存中的场景，就可以使用“内存零拷贝方式”，即将存放数据的ION内存封装为输入输出张量，直接进行推理，不需要进行输入张量和输出张量的数据拷贝，以便节省内存以及推理时间。

  

#### 使用说明

对于零拷贝使用场景，在模型加载完成后，使用[OH_NNTensor_CreateWithFd](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-neural-network-core-h#oh_nntensor_createwithfd)，将ION内存封装为输入张量“input_tensor”，输出张量"output_tensor"，执行推理。

 ![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/0t7UgosXSUep_QcoSqcVAg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260420T191329Z&HW-CC-Expire=86400&HW-CC-Sign=23288C990CFF657AFC049256659EC7086F4B572937D1D851ACDCC9E45D81C1A0)  

若size为模型输出大小，对于输出张量，建议开发者申请ION内存的大小为![image](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/1RSG16vOS1-DJZ66pVcMiA/zh-cn_image_0000002573855171.png?HW-CC-KV=V1&HW-CC-Date=20260420T191329Z&HW-CC-Expire=86400&HW-CC-Sign=DB75E0A7435945787710427F305A42BA142090E382F9A07745BB301D4196F6A1)。