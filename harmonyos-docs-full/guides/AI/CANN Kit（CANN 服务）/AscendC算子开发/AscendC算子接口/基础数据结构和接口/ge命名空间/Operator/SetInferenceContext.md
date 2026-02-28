## 函数功能

向当前算子传递InferShape推导所需要的关联信息，比如前面算子的shape和DataType信息。

## 函数原型

收起自动换行深色代码主题复制

```
void SetInferenceContext ( const InferenceContextPtr &inference_context) ;
```

## 参数说明

 展开

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| inference_context | 输入 | 当前operator的推理上下文。 InferenceContextPtr是指向InferenceContext类的指针的别名： 收起 自动换行 深色代码主题 复制 using InferenceContextPtr = std::shared_ptr<InferenceContext>; |

## 返回值

无

## 异常处理

无

## 约束说明

无