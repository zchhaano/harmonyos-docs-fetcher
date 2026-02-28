## 概述

支持设备PhonePC/2in1TabletTV

[HMS_HiAISingleOpExecutor_CreateConvolution](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/cannkit#hms_hiaisingleopexecutor_createconvolution)输入参数。

**起始版本：** 5.0.0(12)

**相关模块：**[CANN](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/cannkit)

**所在头文件：**[hiai_single_op.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/cannkit-hiai-single-op-8h)

## 汇总

支持设备PhonePC/2in1TabletTV 

### 成员变量

 支持设备PhonePC/2in1TabletTV展开

| 名称 | 描述 |
| --- | --- |
| HiAI_SingleOpOptions * options | 指向 HiAI_SingleOpOptions 对象的指针。该值不能为空指针，否则接口调用失败。 |
| HiAI_SingleOpDescriptor * opDesc | 指向卷积算子对应的 HiAI_SingleOpDescriptor 对象的指针。该值不能为空指针，否则接口调用失败。 |
| HiAI_SingleOpTensorDesc * input | 指向输入Tensor描述的指针。该值不能为空指针，否则接口调用失败。 |
| HiAI_SingleOpTensorDesc * output | 指向输出Tensor描述的指针。该值不能为空指针，否则接口调用失败。 |
| HiAI_SingleOpTensor * filter | 指向卷积核Tensor的指针。该值不能为空指针，否则接口调用失败。 |
| HiAI_SingleOpTensor * bias | 指向偏置Tensor的指针。如果卷积没有偏置，则该值可以是空指针。 |

## 结构体成员变量说明

支持设备PhonePC/2in1TabletTV 

### bias

支持设备PhonePC/2in1TabletTV

```
HiAI_SingleOpTensor* HiAI_SingleOpExecutorConvolutionParam::bias
```

**描述**

指向偏置Tensor的指针。如果卷积没有偏置，则该值可以是空指针。

### filter

支持设备PhonePC/2in1TabletTV

```
HiAI_SingleOpTensor* HiAI_SingleOpExecutorConvolutionParam::filter
```

**描述**

指向卷积核Tensor的指针。该值不能为空指针，否则接口调用失败。

### input

支持设备PhonePC/2in1TabletTV

```
HiAI_SingleOpTensorDesc* HiAI_SingleOpExecutorConvolutionParam::input
```

**描述**

指向输入Tensor描述的指针。该值不能为空指针，否则接口调用失败。

### opDesc

支持设备PhonePC/2in1TabletTV

```
HiAI_SingleOpDescriptor* HiAI_SingleOpExecutorConvolutionParam::opDesc
```

**描述**

指向卷积算子对应的[HiAI_SingleOpDescriptor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/cannkit#hiai_singleopdescriptor)对象的指针。该值不能为空指针，否则接口调用失败。

### options

支持设备PhonePC/2in1TabletTV

```
HiAI_SingleOpOptions* HiAI_SingleOpExecutorConvolutionParam::options
```

**描述**

指向[HiAI_SingleOpOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/cannkit#hiai_singleopoptions)对象的指针。该值不能为空指针，否则接口调用失败。

### output

支持设备PhonePC/2in1TabletTV

```
HiAI_SingleOpTensorDesc* HiAI_SingleOpExecutorConvolutionParam::output
```

**描述**

指向输出Tensor描述的指针。该值不能为空指针，否则接口调用失败。