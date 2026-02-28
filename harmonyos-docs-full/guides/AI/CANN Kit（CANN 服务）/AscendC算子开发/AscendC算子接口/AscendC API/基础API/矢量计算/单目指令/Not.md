## 函数功能

按元素做按位取反，计算公式如下，其中PAR表示矢量计算单元一个迭代能够处理的元素个数 :

![image](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20260224165328.24147692619142925416750430671084:50001231000000:2800:C9D61C69400D7E37CFD1359405F6598FE87CE5D050E9FC1C12949CD526679A11.png)

## 函数原型

tensor前n个数据计算：收起自动换行深色代码主题复制

```
template < typename T> __aicore__ inline void Not ( const LocalTensor<T>& dstLocal, const LocalTensor<T>& srcLocal, const int32_t & calCount)
```

   **表1**模板参数说明展开

| 参数名 | 描述 |
| --- | --- |
| T | 操作数数据类型。 |

  **表2**参数说明展开

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| dstLocal | 输出 | 目的操作数。 类型为 LocalTensor ，支持的TPosition为VECIN/VECCALC/VECOUT。 LocalTensor的起始地址需要32字节对齐。 Kirin9020系列处理器，支持的数据类型为： 前n个tensor：uint16_t、int16_t 不支持浮点类型（half/float） KirinX90系列处理器，支持的数据类型为： 前n个tensor：uint16_t、int16_t 不支持浮点类型（half/float） |
| srcLocal | 输入 | 源操作数。 类型为 LocalTensor ，支持的TPosition为VECIN/VECCALC/VECOUT。 LocalTensor的起始地址需要32字节对齐。 源操作数的数据类型需要与目的操作数保持一致。 Kirin9020系列处理器，支持的数据类型为： 前n个tensor支持：uint16_t、int16_t 不支持浮点类型（half/float） KirinX90系列处理器，支持的数据类型为： 前n个tensor：uint16_t、int16_t 不支持浮点类型（half/float） |
| calCount | 输入 | 输入数据元素个数。 |

## 返回值

无

## 支持的型号

Kirin9020系列处理器

KirinX90系列处理器

## 约束说明

操作数地址偏移对齐要求请参见[通用约束](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-general-constraints)。

## 调用示例

本样例中只展示Compute流程中的部分代码。本样例的srcLocal和dstLocal均为int16_t类型，占16位bit。

如果开发者需要运行样例代码，请将该代码段拷贝并替换[样例模板](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-vector-calculation-binocular-more#zh-cn_topic_0000002123589629_section11009mcpsimp)中Compute函数的部分代码即可。

 tensor前n个数据计算样例：收起自动换行深色代码主题复制

```
AscendC:: Not (dstLocal, srcLocal, 512 );
```

结果示例如下。

 收起自动换行深色代码主题复制

```
输入数据(srcLocal): [9 -2 8 ... 9 0] 输出数据(dstLocal): [-10 1 -9 ... -10 -1]
```