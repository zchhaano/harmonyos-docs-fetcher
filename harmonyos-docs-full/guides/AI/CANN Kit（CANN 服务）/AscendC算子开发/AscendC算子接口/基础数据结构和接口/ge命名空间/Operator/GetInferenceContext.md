## 函数功能

获取当前算子传递InferShape推导所需要的关联信息，比如前面算子的shape和DataType信息。

## 函数原型

收起自动换行深色代码主题复制

```
InferenceContextPtr GetInferenceContext () const ;
```

## 参数说明

无

## 返回值

 展开

| 类型 | 描述 |
| --- | --- |
| InferenceContextPtr | 返回当前operator的推理上下文。 InferenceContextPtr是指向InferenceContext类的指针的别名： 收起 自动换行 深色代码主题 复制 using InferenceContextPtr = std::shared_ptr<InferenceContext>; |

## 异常处理

无

## 约束说明

无