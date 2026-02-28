## 功能说明

- 可实现16*16的二维矩阵数据块的转置。
- 可实现[N, C, H, W]与[N, H, W, C]互相转换。

## 函数原型

- 普通转置，支持16*16的二维矩阵数据块进行转置收起自动换行深色代码主题复制

```
template < typename T> void Transpose ( const LocalTensor<T>& dstLocal, const LocalTensor<T>& srcLocal)
```
- 增强转置，支持16*16的二维矩阵数据块转置，支持[N, C, H, W]与[N, H, W, C]互相转换收起自动换行深色代码主题复制

```
template < typename T> void Transpose ( const LocalTensor<T> &dstLocal, const LocalTensor<T> &srcLocal, const LocalTensor< uint8_t > &sharedTmpBuffer, const TransposeParamsExt &transposeParams)
```

## 参数说明

 **表1**模板参数说明展开

| 参数名 | 描述 |
| --- | --- |
| T | 操作数的数据类型。 普通转置接口: Kirin9020系列处理器，支持的数据类型为：half/int16/uint16 KirinX90系列处理器，支持的数据类型为：half/int16/uint16 增强转置接口: 参考 表4 。 |

  **表2**接口参数说明展开

| 参数名称 | 输入/输出 | 含义 |
| --- | --- | --- |
| dstLocal | 输出 | 目的操作数。 类型为 LocalTensor ，支持的TPosition为VECIN/VECCALC/VECOUT。 LocalTensor的起始地址需要32字节对齐。 |
| srcLocal | 输入 | 源操作数。 类型为 LocalTensor ，支持的TPosition为VECIN/VECCALC/VECOUT。 LocalTensor的起始地址需要32字节对齐。 数据类型需要与dstLocal保持一致。 |
| sharedTmpBuffer | 输入 | 共享的临时Buffer Tensor，sharedTmpBuffer的大小参考 表5 。 |
| transposeParams | 输入 | 控制Transpose的数据结构。结构体内包含：输入的shape信息和transposeType参数。该数据结构的定义请参考 表3 。 收起 自动换行 深色代码主题 复制 struct VtransposeParams { uint16_t nSize; uint16_t cSize; uint16_t hSize; uint16_t wSize; TransposeType transposeType; }; |

  **表3**VtransposeParams结构体内参数说明展开

| 参数名称 | 含义 |
| --- | --- |
| nSize | n轴长度，取值范围：m∈[0, 65535]。默认值为0。 |
| cSize | c轴长度，取值范围：m∈[0, 65535]。默认值为0。 |
| hSize | h轴长度，取值范围：m∈[0, 65535]。默认值为0。 |
| wSize | w轴长度，取值范围：m∈[0, 65535]。默认值为0。 |
| transposeType | 数据排布及reshape的类型，类型为TransposeType枚举类。 收起 自动换行 深色代码主题 复制 enum class TransposeType : uint8_t { TRANSPOSE_TYPE_NONE, // default value TRANSPOSE_NZ2ND_0213, // 当前不支持 TRANSPOSE_NZ2NZ_0213, // 当前不支持 TRANSPOSE_NZ2NZ_012_WITH_N, // 当前不支持 TRANSPOSE_NZ2ND_012_WITH_N, // 当前不支持 TRANSPOSE_NZ2ND_012_WITHOUT_N, // 当前不支持 TRANSPOSE_NZ2NZ_012_WITHOUT_N, // 当前不支持 TRANSPOSE_ND2ND_ONLY, // 当前不支持 TRANSPOSE_ND_UB_GM, // 当前不支持 TRANSPOSE_GRAD_ND_UB_GM, // 当前不支持 TRANSPOSE_ND2ND_B16, // [16,16]二维矩阵转置 TRANSPOSE_NCHW2NHWC, // [N,C,H,W]->[N,H,W,C]， TRANSPOSE_NHWC2NCHW // [N,H,W,C]->[N,C,H,W] }; 注意 当transposeType为TRANSPOSE_ND2ND_B16时，hSize和wSize必须传入16，nSize和cSize传入无效。 |

  **表4**增强转置接口支持的数据类型展开

| transposeType | 支持的数据类型 |
| --- | --- |
| TRANSPOSE_ND2ND_B16 | Kirin9020系列处理器 KirinX90系列处理器 说明 如果要实现int16_t/half类型，shape为[16, 16]二维矩阵的转置，可使用普通转置接口。 |
| TRANSPOSE_NCHW2NHWC | Kirin9020系列处理器 KirinX90系列处理器 |
| TRANSPOSE_NHWC2NCHW | Kirin9020系列处理器 KirinX90系列处理器 |

  **表5**增强转置接口sharedTmpBuffer所需的大小展开

| transposeType | 支持的数据类型 |
| --- | --- |
| TRANSPOSE_ND2ND_B16 | Kirin9020系列处理器 KirinX90系列处理器 |
| TRANSPOSE_NCHW2NHWC | Kirin9020系列处理器 KirinX90系列处理器 |
| TRANSPOSE_NHWC2NCHW | Kirin9020系列处理器 KirinX90系列处理器 |

## 支持的型号

Kirin9020系列处理器

KirinX90系列处理器

## 注意事项

- 操作数地址偏移对齐要求请参见[通用约束](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-general-constraints)。
- 该指令不可迭代（即不能通过repeatTimes重复）。
- [N, C, H, W]与[N, H, W, C]互相转换，H * W需要32B对齐。
- 普通转置接口支持srcLocal和dstLocal复用。
- 增强转置接口，transposeType为TRANSPOSE_ND2ND_B16时支持srcLocal和dstLocal复用，transposeType为TRANSPOSE_NCHW2NHWC、TRANSPOSE_NHWC2NCHW时不支持srcLocal和dstLocal复用。

## 返回值

无

## 调用示例

- 普通接口调用示例，该示例对[16, 16]的half类型矩阵进行转置。收起自动换行深色代码主题复制

```
```
- 增强接口调用示例，完成half类型的[N, C, H, W]->[N, H, W, C]转置。收起自动换行深色代码主题复制

```
# include "kernel_operator.h" template < typename T> class Kernel4dTrans { public : __aicore__ inline Kernel4dTrans () {} __aicore__ inline void Init (__gm__ uint8_t *srcGm, __gm__ uint8_t *dstGm) { inputSize = N * C * H * W; tmpBufferSize = (C + 2 ) * 16 * 16 ; srcGlobal. SetGlobalBuffer ((__gm__ T *)srcGm); dstGlobal. SetGlobalBuffer ((__gm__ T *)dstGm); pipe. InitBuffer (inQueueSrcVecIn, 1 , inputSize* sizeof (T)); pipe. InitBuffer (inQueueSrcVecOut, 1 , inputSize* sizeof (T)); pipe. InitBuffer (tmpQueue, 1 , tmpBufferSize * sizeof (T)); } __aicore__ inline void Process () { CopyIn (); Compute (); CopyOut (); } private : __aicore__ inline void CopyIn () { AscendC::LocalTensor<T> srcLocal = inQueueSrcVecIn. AllocTensor <T>(); AscendC:: DataCopy (srcLocal, srcGlobal, inputSize); inQueueSrcVecIn. EnQue (srcLocal); } __aicore__ inline void Compute () { AscendC::LocalTensor<T> srcLocal = inQueueSrcVecIn. DeQue <T>(); AscendC::LocalTensor<T> dstLocal = inQueueSrcVecOut. AllocTensor <T>(); AscendC::LocalTensor< uint8_t > stackBuffer = tmpQueue. AllocTensor < uint8_t >(); AscendC::TransposeParamsExt transposeParams; transposeParams.nSize = N; transposeParams.cSize = C; transposeParams.hSize = H; transposeParams.wSize = W; transposeParams.transposeType = transposetype; AscendC:: Transpose (dstLocal, srcLocal, stackBuffer, transposeParams); inQueueSrcVecOut. EnQue <T>(dstLocal); inQueueSrcVecIn. FreeTensor (srcLocal); tmpQueue. FreeTensor (stackBuffer); } __aicore__ inline void CopyOut () { AscendC::LocalTensor<T> dstLocal = inQueueSrcVecOut. DeQue <T>(); AscendC:: DataCopy (dstGlobal, dstLocal, inputSize); inQueueSrcVecOut. FreeTensor (dstLocal); } private : AscendC::TPipe pipe; AscendC::TQue<AscendC::QuePosition::VECIN, 1 > inQueueSrcVecIn; AscendC::TQue<AscendC::QuePosition::VECOUT, 1 > inQueueSrcVecOut; AscendC::TQue<AscendC::QuePosition::VECCALC, 1 > tmpQueue; AscendC::GlobalTensor<T> srcGlobal; AscendC::GlobalTensor<T> dstGlobal; uint32_t N = 3 ; uint32_t C = 3 ; uint32_t H = 2 ; uint32_t W = 8 ; uint32_t inputSize, tmpBufferSize; AscendC::TransposeType transposetype = AscendC::TransposeType::TRANSPOSE_NCHW2NHWC; }; extern "C" __global__ __aicore__ void transpose_kernel (__gm__ uint8_t * srcGm, __gm__ uint8_t * dstGm) { Kernel4dTrans<half>op; op. Init (srcGm, dstGm); op. Process (); }
```