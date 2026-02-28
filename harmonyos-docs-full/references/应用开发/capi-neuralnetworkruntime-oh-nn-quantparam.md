# OH_NN_QuantParam

```
typedef struct OH_NN_QuantParam {...} OH_NN_QuantParam
```

## 概述

支持设备PhonePC/2in1Tablet

量化信息。

在量化的场景中，32位浮点型数据根据以下公式量化为定点数据：

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170136.05103396858235019606898931841997:50001231000000:2800:13849C51A33F2ECF141FB91C2FC50BCD0ADCD8505C5470EE7A90D8B5E94B12F0.png)

其中s和z是量化参数，在OH_NN_QuantParam中通过scale和zeroPoint保存，r是浮点数，q是量化后的结果，q_min是量化后下界，q_max是量化后的上界，计算方式如下：

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170136.68254284665842472180547309049545:50001231000000:2800:CAFD4674384A3B81E4FD8CECC27317C856A8DC7C51EFDBC916FD11F66871C10C.png)

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170136.62877469283381484249805663045308:50001231000000:2800:E95CCF47338DF4B69DA2C620C91C88FAA476425BBABE268E4B939B48A0A45BAE.png)

clamp函数定义如下：

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224170136.11508483977259852546922009202399:50001231000000:2800:0BFDF0C119CC51637DE75A1E619AAD4511D1C256261E788F1F4EF5918EDB383B.png)

**起始版本：** 9

**废弃版本：** 11

**替代接口：** [NN_QuantParam](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-neuralnetworkruntime-nn-quantparam)

**相关模块：** [NeuralNetworkRuntime](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-neuralnetworkruntime)

**所在头文件：** [neural_network_runtime_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-neural-network-runtime-type-h)

## 汇总

支持设备PhonePC/2in1Tablet 

### 成员变量

 支持设备PhonePC/2in1Tablet展开

| 名称 | 描述 |
| --- | --- |
| uint32_t quantCount | 指定numBits、scale和zeroPoint数组的长度。在per-layer量化的场景下，quantCount通常指定为1，即一个张量所有通道共享一套量化参数；在per-channel量化场景下，quantCount通常和张量通道数一致，每个通道使用自己的量化参数。 |
| const uint32_t *numBits | 量化位数。 |
| const double *scale | 指向量化公式中scale数据的指针。 |
| const int32_t *zeroPoint | 指向量化公式中zero point数据的指针。 |