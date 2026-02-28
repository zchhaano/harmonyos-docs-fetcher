## 函数功能

设置Tensor的数据。

## 函数原型

收起自动换行深色代码主题复制

```
void SetData (TensorData &&data)
```

## 参数说明

 展开

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| data | 输入 | 需要设置的数据。 关于TensorData类型的定义，请参见 TensorData 。 |

## 返回值

无

## 约束说明

无

## 调用示例

收起自动换行深色代码主题复制

```
Tensor t = {{}, {}, {}, {}, nullptr }; void *a = &t; TensorData td (a, nullptr ) ; t. SetData (std:: move (td));
```