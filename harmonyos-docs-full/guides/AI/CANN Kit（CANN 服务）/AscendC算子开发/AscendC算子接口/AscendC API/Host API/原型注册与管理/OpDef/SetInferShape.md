## 函数功能

注册Shape推导函数。

## 函数原型

收起自动换行深色代码主题复制

```
OpDef & SetInferShape (gert::OpImplRegisterV2::InferShapeKernelFunc func) ;
```

## 参数说明

 展开

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| func | 输入 | Shape推导函数。InferShapeKernelFunc类型定义如下。 收起 自动换行 深色代码主题 复制 using InferShapeKernelFunc = UINT32 (*)(InferShapeContext *); |

## 返回值

[OpDef](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-opdef)算子定义。

## 约束说明

无