## 函数功能

注册Tiling函数。

## 函数原型

收起自动换行深色代码主题复制

```
OpAICoreDef & SetTiling (gert::OpImplRegisterV2::TilingKernelFunc func) ;
```

## 参数说明

 展开

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| func | 输入 | Tiling函数。TilingKernelFunc类型定义如下。 收起 自动换行 深色代码主题 复制 using TilingKernelFunc = UINT32 (*)(TilingContext *); |

## 返回值

[OpAICoreDef](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-opaicoredef)算子定义。

## 约束说明

无