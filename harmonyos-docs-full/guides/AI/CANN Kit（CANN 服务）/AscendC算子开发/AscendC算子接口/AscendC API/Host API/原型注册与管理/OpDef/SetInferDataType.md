## 函数功能

注册DataType推导函数。

## 函数原型

收起自动换行深色代码主题复制

```
OpDef & SetInferDataType (gert::OpImplRegisterV2::InferDataTypeKernelFunc func) ;
```

## 参数说明

 展开

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| func | 输入 | DataType推导函数。 InferDataTypeKernelFunc 类型定义如下。 收起 自动换行 深色代码主题 复制 using InferDataTypeKernelFunc = UINT32 (*)(InferDataTypeContext *); |

## 返回值

[OpDef](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-opdef)算子定义。

## 约束说明

无