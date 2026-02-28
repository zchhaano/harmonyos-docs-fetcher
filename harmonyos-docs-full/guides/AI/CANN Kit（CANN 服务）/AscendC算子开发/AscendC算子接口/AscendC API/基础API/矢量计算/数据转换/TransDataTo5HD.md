## 功能说明

数据格式转换，一般用于将NCHW格式转换成NC1HWC0格式。特别的，也可以用于二维矩阵数据块的转置。完成转置功能时，相比于[Transpose](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-transpose)接口，Transpose仅支持16*16大小的矩阵转置。本接口单次repeat内可处理512Byte的数据（16个datablock），根据数据类型不同，支持不同shape的矩阵转置（比如数据类型为half时，单次repeat可完成16*16大小的矩阵转置），同还可以支持多次repeat操作。

单次repeat内转换规则如下。

- 当输入数据类型是int16_t/uint16_t/half时，每个datablock中包含16个数，指令内部会循环16次，每次循环都会分别从指定的16个datablock中的对应位置取值，组成一个新的datablock单元放入目的地址中。如下图所示，图中的srcLocalList[0]-srcLocalList[15]代表源操作数的16个datablock。**图1**输入数据类型为int16_t/uint16_t/half时的转换规则
![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165325.74473322497837020472674666669999:50001231000000:2800:D46B519408144CFA026ED85F7969518BC767500BDAFB8CDCC83F35FD6E4AFD80.png)

- 当数据类型是float/int32_t/uint32_t时，每个datablock包含8个数，指令内部会循环8次，每次循环都会分别从指定的16个datablock中的对应位置取值，组成2个新的datablock放入目的地址中。如下图所示：**图2**输入数据类型为float/int32_t/uint32_t时的转换规则
![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165326.92435855668301998946972043449392:50001231000000:2800:3F04B846EF6DC28887ED136237691567BD07E72F4138B1837B36F16EF7E69E35.png)

- 当数据类型是int8_t/uint8_t时，每个datablock包含32个数，指令内部会循环16次，每次循环都会分别从指定的16个datablock中的对应位置取值，组成半个datablock放入目的地址中, 读取和存放是在datablock的高半部还是低半部由参数srcHighHalf和dstHighHalf决定。如下图所示：**图3**输入数据类型为int8_t/uint8_t时的转换规则
![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165326.08902463079079936278377953262201:50001231000000:2800:932E305D2DE0A98B3C9F06FAD2C4EF7C9DCE5C3FD69EA829C5A05A0F7D74932C.png)

基于以上的转换规则，使用该接口进行NC1HWC0格式转换或者矩阵转置。NC1HWC0格式转换相对复杂，这里给出其具体的转换方法：

NCHW格式转换成NC1HWC0格式时，如果是数据类型是float/int32_t/uint32_t/int16_t/uint16_t/half，则C0=16；如果数据类型是uint8_t/int8_t，则C0=32。下图以C0=16为例进行介绍：

 **图4**NCHW格式转换成NC1HWC0格式时的转换规则
![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165326.85574707822347714742126407872027:50001231000000:2800:F9E178A2B87352756E24BE50E7532686912892F0B79EACFCCB597A0CDCB735B2.png)  

## 函数原型

dstLocalList与srcLocalList类型为LocalTensor的数组。收起自动换行深色代码主题复制

```
// NCHW_CONV_ADDR_LIST_SIZE值为16 template < typename T> __aicore__ inline void TransDataTo5HD ( const LocalTensor<T> (&dstLocalList)[NCHW_CONV_ADDR_LIST_SIZE], const LocalTensor<T> (&srcLocalList)[NCHW_CONV_ADDR_LIST_SIZE], const TransDataTo5HDParams& nchwconvParams)
```

## 参数说明

 **表1**模板参数说明展开

| 参数名 | 描述 |
| --- | --- |
| T | 操作数数据类型。 Kirin9020系列处理器 KirinX90系列处理器 |

  **表2**参数列表展开

| 参数名称 | 输入/输出 | 含义 |
| --- | --- | --- |
| dstLocalList/dstList | 输出 | 目的操作数地址序列。 类型为 LocalTensor 或者LocalTensor的地址值，LocalTensor支持的TPosition为VECIN/VECCALC/VECOUT。LocalTensor的起始地址需要32B对齐。支持的数据类型参考表1。 |
| srcLocalList/srcList | 输入 | 源操作数地址序列。 类型为 LocalTensor 或者LocalTensor的地址值，LocalTensor支持的TPosition为VECIN/VECCALC/VECOUT。LocalTensor的起始地址需要32B对齐。支持的数据类型参考表1。 数据类型需要与dstLocalList/dstList保持一致。 |
| dstLocal | 输出 | 目的操作数。 类型为 LocalTensor ，连续存储对应LocalTensor的地址值。LocalTensor支持的TPosition为VECIN/VECCALC/VECOUT。LocalTensor的起始地址需要32B对齐。 |
| srcLocal | 输入 | 源操作数。 类型为 LocalTensor ，连续存储对应LocalTensor的地址值。LocalTensor支持的TPosition为VECIN/VECCALC/VECOUT。LocalTensor的起始地址需要32B对齐。 |
| nchwconvParams | 输入 | 控制TransdataTo5HD的数据结构。结构体内包含：读取和写入位置的控制参数，迭代次数，相邻迭代间的地址步长等参数。该数据结构的定义请参考表3。 |

  **表3**TransDataTo5HDParams结构体内参数说明展开

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| dstHighHalf | 输入 | 指定每个dstLocalList地址中的数据存储到datablock的高半部还是低半部，该配置只支持int8_t/uint8_t的数据类型。 支持的数据类型为bool，有以下两种取值： True：表示存储于datablock的高半部。 False：表示存储于datablock的低半部。 |
| srcHighHalf | 输入 | 指定每个srcLocalList地址中的数据从datablock的高半部还是低半部读取，该配置只支持int8_t/uint8_t的数据类型。 支持的数据类型为bool，有以下两种取值： True：表示从datablock的高半部读取。 False：表示从datablock的低半部读取。 |

## 支持的型号

Kirin9020系列处理器

KirinX90系列处理器

## 注意事项

- 进行NCHW格式到NC1HWC0格式的转换时，一般用法是将srcLocalList/dstLocalList中的每个元素配置为每个HW平面的起点。
- 为了性能更优，int8_t/uint8_t时建议先固定dstHighHalf、srcHighHalf，在HW方向repeat后，再改变dstHighHalf、srcHighHalf。
- 为了节省地址空间，开发者可以定义一个Tensor，供源操作数与目的操作数同时使用（即地址重叠），相关约束如下。

  - 对于单次repeat（repeatTimes=1），且源操作数序列与目的操作数序列之间要求100%完全重叠，不支持部分重叠，且每一个block都必须相等。
  - 对于多次repeat（repeatTimes>1），若源操作数序列与目的操作数序列之间存在依赖，即第N次迭代的目的操作数是第N+1次的源操作数，这种情况是不支持地址重叠的。
- 操作数地址偏移对齐要求请参见[通用约束](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-general-constraints)。
- dstLocal与srcLocal中的地址需要连续存放，详见[调用示例](/consumer/cn/doc/harmonyos-guides/cannkit-transdatato5hd#zh-cn_topic_0000002140995609_section1844517782910)。

## 返回值

无

## 调用示例

- NCHW格式转换成NC1HWC0格式调用示例，其中输入数据为half类型，输入NCHW格式为（2, 32, 16, 16），目标格式NC1HWC0为（2, 2, 16, 16, 16）。收起自动换行深色代码主题复制

```
```
- 用于二维矩阵数据块的转置的int8_t（8bit位）调用示例。收起自动换行深色代码主题复制

```
```
- 用于二维矩阵数据块的转置的half（16bit位）调用示例。收起自动换行深色代码主题复制

```
```
- 用于二维矩阵数据块的转置的int32_t（32bit位）调用示例。收起自动换行深色代码主题复制

```
# include "kernel_operator.h" class KernelTransDataTo5HD { public : __aicore__ inline KernelTransDataTo5HD () {} __aicore__ inline void Init (__gm__ uint8_t *src, __gm__ uint8_t *dstGm) { srcGlobal. SetGlobalBuffer ((__gm__ int32_t *)src); dstGlobal. SetGlobalBuffer ((__gm__ int32_t *)dstGm); pipe. InitBuffer (inQueueSrc, 1 , srcDataSize * sizeof ( int32_t )); pipe. InitBuffer (workQueueSrc1, 1 , 16 * sizeof ( uint64_t )); pipe. InitBuffer (workQueueSrc2, 1 , 16 * sizeof ( uint64_t )); pipe. InitBuffer (outQueueDst, 1 , dstDataSize * sizeof ( int32_t )); } __aicore__ inline void Process () { CopyIn (); Compute (); CopyOut (); } private : __aicore__ inline void CopyIn () { AscendC::LocalTensor< int32_t > srcLocal = inQueueSrc. AllocTensor < int32_t >(); AscendC:: DataCopy (srcLocal, srcGlobal, srcDataSize); inQueueSrc. EnQue (srcLocal); } __aicore__ inline void Compute () { AscendC::LocalTensor< int32_t > srcLocal = inQueueSrc. DeQue < int32_t >(); AscendC::LocalTensor< int32_t > dstLocal = outQueueDst. AllocTensor < int32_t >(); AscendC::TransDataTo5HDParams transDataParams; transDataParams.dstHighHalf = false ; transDataParams.srcHighHalf = false ; transDataParams.repeatTimes = 1 ; transDataParams.dstRepStride = 0 ; transDataParams.srcRepStride = 0 ; // 入参类型是LocalTensor的调用方式 AscendC::LocalTensor< int32_t > dstLocalList[ 16 ]; for ( int i = 0 ; i < 16 ; i++) { dstLocalList[i] = dstLocal[width * i]; } AscendC::LocalTensor< int32_t > srcLocalList[ 16 ]; for ( int i = 0 ; i < 16 ; i++) { srcLocalList[i] = srcLocal[width * i]; } AscendC:: TransDataTo5HD (dstLocalList, srcLocalList, transDataParams); outQueueDst. EnQue < int32_t >(dstLocal); inQueueSrc. FreeTensor (srcLocal); } __aicore__ inline void CopyOut () { AscendC::LocalTensor< int32_t > dstLocal = outQueueDst. DeQue < int32_t >(); AscendC:: DataCopy (dstGlobal, dstLocal, dstDataSize); outQueueDst. FreeTensor (dstLocal); } private : AscendC::TPipe pipe; AscendC::TQue<AscendC::QuePosition::VECIN, 1 > inQueueSrc; AscendC::TQue<AscendC::QuePosition::VECIN, 1 > workQueueSrc1; AscendC::TQue<AscendC::QuePosition::VECIN, 1 > workQueueSrc2; AscendC::TQue<AscendC::QuePosition::VECOUT, 1 > outQueueDst; AscendC::GlobalTensor< int32_t > srcGlobal, dstGlobal; int srcDataSize = 128 ; int dstDataSize = 128 ; int width = 8 ; }; extern "C" __global__ __aicore__ void trans5hd_simple_kernel (__gm__ uint8_t *src, __gm__ uint8_t *dstGm) { KernelTransDataTo5HD op; op. Init (src, dstGm); op. Process (); } 输入数据（src）： [ 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127 ] 输出数据（dstGm）： [ 0 8 16 24 32 40 48 56 64 72 80 88 96 104 112 120 1 9 17 25 33 41 49 57 65 73 81 89 97 105 113 121 2 10 18 26 34 42 50 58 66 74 82 90 98 106 114 122 3 11 19 27 35 43 51 59 67 75 83 91 99 107 115 123 4 12 20 28 36 44 52 60 68 76 84 92 100 108 116 124 5 13 21 29 37 45 53 61 69 77 85 93 101 109 117 125 6 14 22 30 38 46 54 62 70 78 86 94 102 110 118 126 7 15 23 31 39 47 55 63 71 79 87 95 103 111 119 127 ]
```